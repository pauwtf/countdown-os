# ============================================================
# COUNTDOWN OS — COMPONENT PROPERTY SCHEMA
# Version: 1.2 Elegance
# ============================================================


# ============================================================
# SCHEMA ERROR
# ============================================================

class ComponentSchemaError(ValueError):
    """
    Error producido cuando un componente
    no cumple el Property Schema.
    """
    pass


# ============================================================
# PROPERTY DEFINITIONS
# ============================================================

PROPERTY_SCHEMA = {

    # ========================================================
    # CONTAINER
    # ========================================================

    "container": {

        "required": [],

        "optional": {

            "type": str,
        }
    },


    # ========================================================
    # TEXT
    # ========================================================

    "text": {

        "required": [],

        "optional": {

            "type": str,

            "value": str,

            "font_size": (int, float),

            "font_family": str,

            "font_weight": str,

            "alignment": str,

            "line_height": (int, float),

            "max_lines": int,

            "letter_spacing": (int, float),

            "opacity": (int, float),
        }
    },


    # ========================================================
    # SHAPE
    # ========================================================

    "shape": {

        "required": [],

        "optional": {

            "type": str,

            "shape_type": str,

            "width": (int, float),

            "height": (int, float),

            "size": (int, float),

            "radius": (int, float),

            "opacity": (int, float),
        }
    },


    # ========================================================
    # GRADIENT
    # ========================================================

    "gradient": {

        "required": [],

        "optional": {

            "type": str,

            "direction": str,

            "start": str,

            "end": str,

            "start_opacity": (int, float),

            "end_opacity": (int, float),

            "opacity": (int, float),
        }
    },
}


# ============================================================
# VALID COMPONENT TYPES
# ============================================================

COMPONENT_TYPES = set(
    PROPERTY_SCHEMA.keys()
)


# ============================================================
# TYPE VALIDATION
# ============================================================

def validate_component_type(
    component_type
):
    """
    Valida que el tipo del componente
    exista en el schema.
    """

    if not isinstance(
        component_type,
        str
    ):
        raise ComponentSchemaError(
            "Component type must be a string"
        )

    if component_type not in COMPONENT_TYPES:

        raise ComponentSchemaError(
            f"Unknown component type: "
            f"{component_type}"
        )

    return True


# ============================================================
# PROPERTY TYPE VALIDATION
# ============================================================

def validate_property_type(
    property_name,
    value,
    expected_type
):
    """
    Valida el tipo de una propiedad.
    """

    # --------------------------------------------------------
    # Boolean
    # --------------------------------------------------------

    if expected_type is bool:

        if not isinstance(
            value,
            bool
        ):

            raise ComponentSchemaError(
                f"Property '{property_name}' "
                f"must be bool"
            )

        return


    # --------------------------------------------------------
    # Numeric
    # --------------------------------------------------------

    if expected_type in (
        int,
        float,
        (int, float)
    ):

        if (
            not isinstance(
                value,
                (int, float)
            )
            or isinstance(
                value,
                bool
            )
        ):

            raise ComponentSchemaError(
                f"Property '{property_name}' "
                f"must be numeric"
            )

        return


    # --------------------------------------------------------
    # Generic isinstance
    # --------------------------------------------------------

    if not isinstance(
        value,
        expected_type
    ):

        if isinstance(
            expected_type,
            tuple
        ):

            expected_name = " or ".join(
                item.__name__
                for item in expected_type
            )

        else:

            expected_name = (
                expected_type.__name__
            )

        raise ComponentSchemaError(
            f"Property '{property_name}' "
            f"must be {expected_name}"
        )


# ============================================================
# COMPONENT TYPE FROM PROPERTIES
# ============================================================

def get_component_type(
    properties
):
    """
    Obtiene el tipo del componente
    desde sus propiedades.
    """

    if not isinstance(
        properties,
        dict
    ):

        raise ComponentSchemaError(
            "Component properties "
            "must be a dictionary"
        )

    if "type" not in properties:

        raise ComponentSchemaError(
            "Component properties "
            "require 'type'"
        )

    component_type = (
        properties["type"]
    )

    validate_component_type(
        component_type
    )

    return component_type


# ============================================================
# VALIDATE PROPERTIES
# ============================================================

def validate_properties(
    properties
):
    """
    Valida todas las propiedades de un componente.

    El tipo del componente se obtiene
    desde properties['type'].
    """

    component_type = (
        get_component_type(
            properties
        )
    )

    schema = PROPERTY_SCHEMA[
        component_type
    ]

    required = schema[
        "required"
    ]

    optional = schema[
        "optional"
    ]


    # ========================================================
    # REQUIRED PROPERTIES
    # ========================================================

    for property_name in required:

        if property_name not in properties:

            raise ComponentSchemaError(
                f"Component type "
                f"'{component_type}' "
                f"requires property "
                f"'{property_name}'"
            )


    # ========================================================
    # PROPERTY VALIDATION
    # ========================================================

    allowed_properties = set(
        optional.keys()
    )

    allowed_properties.update(
        required
    )

    for property_name, value in (
        properties.items()
    ):

        # ----------------------------------------------------
        # Unknown property
        # ----------------------------------------------------

        if (
            property_name
            not in allowed_properties
        ):

            raise ComponentSchemaError(
                f"Property "
                f"'{property_name}' "
                f"is not allowed for "
                f"component type "
                f"'{component_type}'"
            )


        # ----------------------------------------------------
        # Type validation
        # ----------------------------------------------------

        if property_name in optional:

            expected_type = optional[
                property_name
            ]

        else:

            # Required properties
            # should also have a schema.
            expected_type = optional.get(
                property_name
            )

            if expected_type is None:

                raise ComponentSchemaError(
                    f"No type definition "
                    f"for required property "
                    f"'{property_name}'"
                )

        validate_property_type(
            property_name,
            value,
            expected_type
        )


    return True


# ============================================================
# PROPERTY ACCESS
# ============================================================

def get_property_schema(
    component_type
):
    """
    Devuelve el schema completo
    de un tipo de componente.
    """

    validate_component_type(
        component_type
    )

    return PROPERTY_SCHEMA[
        component_type
    ]


# ============================================================
# ALLOWED PROPERTIES
# ============================================================

def get_allowed_properties(
    component_type
):
    """
    Devuelve las propiedades permitidas
    para un tipo de componente.
    """

    schema = get_property_schema(
        component_type
    )

    return set(
        schema["required"]
    ) | set(
        schema["optional"].keys()
    )


# ============================================================
# MANUAL TEST
# ============================================================

if __name__ == "__main__":

    print()
    print("=" * 55)
    print(
        "       COUNTDOWN OS — PROPERTY SCHEMA"
    )
    print("=" * 55)

    print()

    # ========================================================
    # VALID CONTAINER
    # ========================================================

    validate_properties({
        "type": "container"
    })

    print(
        "✓ Container schema"
    )


    # ========================================================
    # VALID TEXT
    # ========================================================

    validate_properties({

        "type": "text",

        "value": "UNTIL ALEX",

        "font_size": 18,

        "alignment": "center"
    })

    print(
        "✓ Text schema"
    )


    # ========================================================
    # VALID SHAPE
    # ========================================================

    validate_properties({

        "type": "shape",

        "shape_type": "rectangle",

        "width": 400,

        "height": 200
    })

    print(
        "✓ Shape schema"
    )


    # ========================================================
    # VALID GRADIENT
    # ========================================================

    validate_properties({

        "type": "gradient",

        "direction": "vertical",

        "start": "#000000",

        "end": "#FFFFFF"
    })

    print(
        "✓ Gradient schema"
    )


    # ========================================================
    # INVALID PROPERTY
    # ========================================================

    try:

        validate_properties({

            "type": "text",

            "banana": "invalid"
        })

        raise AssertionError(
            "Invalid property was accepted"
        )

    except ComponentSchemaError:

        print(
            "✓ Unknown property rejected"
        )


    # ========================================================
    # INVALID TYPE
    # ========================================================

    try:

        validate_properties({

            "type": "unknown"
        })

        raise AssertionError(
            "Unknown component type was accepted"
        )

    except ComponentSchemaError:

        print(
            "✓ Unknown component type rejected"
        )


    # ========================================================
    # INVALID VALUE TYPE
    # ========================================================

    try:

        validate_properties({

            "type": "text",

            "font_size": "large"
        })

        raise AssertionError(
            "Invalid property type was accepted"
        )

    except ComponentSchemaError:

        print(
            "✓ Invalid property type rejected"
        )


    print()
    print(
        "🟢 Property Schema validation passed"
    )
    print()