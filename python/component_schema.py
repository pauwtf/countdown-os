# ============================================================
# COUNTDOWN OS — COMPONENT PROPERTY SCHEMA
# Version: 1.2 Elegance
# ============================================================


# ============================================================
# SCHEMA ERROR
# ============================================================

class ComponentSchemaError(Exception):
    """
    Error producido cuando un componente
    no cumple el Component Property Schema.
    """

    pass


# ============================================================
# PROPERTY RULES
# ============================================================

PROPERTY_RULES = {

    # ========================================================
    # COMMON
    # ========================================================

    "type": {
        "value_type": "string"
    },

    "visible": {
        "value_type": "boolean"
    },

    "opacity": {
        "value_type": "number",
        "min": 0.0,
        "max": 1.0
    },


    # ========================================================
    # TEXT
    # ========================================================

    "value": {
        "value_type": "string"
    },

    "font_size": {
        "value_type": "number",
        "min": 0.0
    },

    "font_family": {
        "value_type": "string"
    },

    "font_weight": {
        "value_type": "integer",
        "allowed_values": {
            100,
            200,
            300,
            400,
            500,
            600,
            700,
            800,
            900
        }
    },

    "font_style": {
        "value_type": "string",
        "allowed_values": {
            "normal",
            "italic"
        }
    },

    "color": {
        "value_type": "string"
    },

    "align": {
        "value_type": "string",
        "allowed_values": {
            "left",
            "center",
            "right"
        }
    },

    "max_width": {
        "value_type": "number",
        "min": 0.0
    },

    "max_lines": {
        "value_type": "integer",
        "min": 1
    },


    # ========================================================
    # SHAPE
    # ========================================================

    "shape_type": {
        "value_type": "string",
        "allowed_values": {
            "rectangle",
            "circle",
            "rounded_rectangle"
        }
    },

    "width": {
        "value_type": "number",
        "min": 0.0
    },

    "height": {
        "value_type": "number",
        "min": 0.0
    },

    "size": {
        "value_type": "number",
        "min": 0.0
    },

    "radius": {
        "value_type": "number",
        "min": 0.0
    },


    # ========================================================
    # GRADIENT
    # ========================================================

    "direction": {
        "value_type": "string",
        "allowed_values": {
            "vertical",
            "horizontal",
            "diagonal"
        }
    },

    "color_start": {
        "value_type": "string"
    },

    "color_end": {
        "value_type": "string"
    }
}


# ============================================================
# PROPERTY SCHEMA
# ============================================================

PROPERTY_SCHEMA = {

    # ========================================================
    # CONTAINER
    # ========================================================

    "container": {

        "allowed": {

            "type",
            "visible",
            "opacity"
        }
    },


    # ========================================================
    # TEXT
    # ========================================================

    "text": {

        "allowed": {

            "type",
            "value",
            "font_size",
            "font_family",
            "font_weight",
            "font_style",
            "color",
            "opacity",
            "visible",
            "align",
            "max_width",
            "max_lines"
        }
    },


    # ========================================================
    # SHAPE
    # ========================================================

    "shape": {

        "allowed": {

            "type",
            "shape_type",
            "width",
            "height",
            "size",
            "radius",
            "color",
            "opacity",
            "visible"
        }
    },


    # ========================================================
    # GRADIENT
    # ========================================================

    "gradient": {

        "allowed": {

            "type",
            "shape_type",
            "width",
            "height",
            "direction",
            "color_start",
            "color_end",
            "opacity",
            "visible"
        }
    }
}


# ============================================================
# TYPE VALIDATION
# ============================================================

def _validate_value_type(
    key,
    value,
    expected_type
):
    """
    Valida el tipo de dato de una propiedad.
    """

    if expected_type == "string":

        if not isinstance(
            value,
            str
        ):

            raise ComponentSchemaError(
                f"Property '{key}' must be a string"
            )

        return


    if expected_type == "boolean":

        if not isinstance(
            value,
            bool
        ):

            raise ComponentSchemaError(
                f"Property '{key}' must be a boolean"
            )

        return


    if expected_type == "integer":

        if (
            isinstance(value, bool)
            or not isinstance(value, int)
        ):

            raise ComponentSchemaError(
                f"Property '{key}' must be an integer"
            )

        return


    if expected_type == "number":

        if (
            isinstance(value, bool)
            or not isinstance(
                value,
                (int, float)
            )
        ):

            raise ComponentSchemaError(
                f"Property '{key}' must be numeric"
            )

        return


    raise ComponentSchemaError(
        f"Unknown property value type "
        f"'{expected_type}' for '{key}'"
    )


# ============================================================
# RANGE VALIDATION
# ============================================================

def _validate_range(
    key,
    value,
    rule
):
    """
    Valida límites numéricos.
    """

    if "min" in rule:

        if value < rule["min"]:

            raise ComponentSchemaError(
                f"Property '{key}' must be >= "
                f"{rule['min']}"
            )


    if "max" in rule:

        if value > rule["max"]:

            raise ComponentSchemaError(
                f"Property '{key}' must be <= "
                f"{rule['max']}"
            )


# ============================================================
# ENUM VALIDATION
# ============================================================

def _validate_allowed_values(
    key,
    value,
    rule
):
    """
    Valida valores pertenecientes
    a un conjunto permitido.
    """

    allowed_values = rule.get(
        "allowed_values"
    )

    if allowed_values is None:
        return

    if value not in allowed_values:

        raise ComponentSchemaError(
            f"Invalid value for property "
            f"'{key}': {value!r}. "
            f"Allowed values: "
            f"{sorted(allowed_values)}"
        )


# ============================================================
# COMPONENT TYPE
# ============================================================

def get_component_type(properties):
    """
    Obtiene y valida el tipo de componente.
    """

    if not isinstance(
        properties,
        dict
    ):

        raise ComponentSchemaError(
            "Component properties must be a dictionary"
        )


    component_type = properties.get(
        "type"
    )


    if component_type is None:

        raise ComponentSchemaError(
            "Component properties require 'type'"
        )


    if not isinstance(
        component_type,
        str
    ):

        raise ComponentSchemaError(
            "Component type must be a string"
        )


    if component_type not in PROPERTY_SCHEMA:

        raise ComponentSchemaError(
            "Unknown component type: "
            f"'{component_type}'"
        )


    return component_type


# ============================================================
# PROPERTY VALIDATION
# ============================================================

def validate_properties(properties):
    """
    Valida todas las propiedades de un componente.

    Comprueba:

        1. estructura
        2. component type
        3. propiedad permitida
        4. tipo de dato
        5. valores permitidos
        6. rangos numéricos
    """

    if not isinstance(
        properties,
        dict
    ):

        raise ComponentSchemaError(
            "Component properties must be a dictionary"
        )


    component_type = get_component_type(
        properties
    )


    allowed_properties = PROPERTY_SCHEMA[
        component_type
    ][
        "allowed"
    ]


    for key, value in properties.items():

        # ====================================================
        # PROPERTY ALLOWED
        # ====================================================

        if key not in allowed_properties:

            raise ComponentSchemaError(
                f"Property '{key}' is not allowed "
                f"for component type "
                f"'{component_type}'"
            )


        # ====================================================
        # PROPERTY RULE
        # ====================================================

        rule = PROPERTY_RULES.get(
            key
        )


        if rule is None:

            raise ComponentSchemaError(
                f"No validation rule exists "
                f"for property '{key}'"
            )


        # ====================================================
        # TYPE
        # ====================================================

        _validate_value_type(
            key,
            value,
            rule["value_type"]
        )


        # ====================================================
        # RANGE
        # ====================================================

        if rule["value_type"] in {
            "number",
            "integer"
        }:

            _validate_range(
                key,
                value,
                rule
            )


        # ====================================================
        # ALLOWED VALUES
        # ====================================================

        _validate_allowed_values(
            key,
            value,
            rule
        )


    return True


# ============================================================
# COMPONENT VALIDATION
# ============================================================

def validate_component(component):
    """
    Valida una instancia de Component.
    """

    if component is None:

        raise ComponentSchemaError(
            "Component cannot be None"
        )


    if not hasattr(
        component,
        "properties"
    ):

        raise ComponentSchemaError(
            "Object is not a valid Component"
        )


    validate_properties(
        component.properties
    )


    return True


# ============================================================
# MANUAL TEST
# ============================================================

if __name__ == "__main__":

    print()
    print("=" * 60)
    print("       COUNTDOWN OS — COMPONENT PROPERTY SCHEMA")
    print("=" * 60)


    # ========================================================
    # VALID TEXT
    # ========================================================

    valid_text = {

        "type": "text",

        "value": "UNTIL ALEX",

        "font_size": 18,

        "font_family": "default",

        "font_weight": 400,

        "font_style": "normal",

        "color": "#FFFFFF",

        "opacity": 1.0,

        "visible": True,

        "align": "center",

        "max_width": 300,

        "max_lines": 1
    }


    validate_properties(
        valid_text
    )

    print()
    print("✓ Valid text properties")


    # ========================================================
    # VALID SHAPE
    # ========================================================

    valid_shape = {

        "type": "shape",

        "shape_type": "rectangle",

        "width": 400,

        "height": 200,

        "color": "#FFFFFF",

        "opacity": 1.0,

        "visible": True
    }


    validate_properties(
        valid_shape
    )

    print(
        "✓ Valid shape properties"
    )


    # ========================================================
    # VALID GRADIENT
    # ========================================================

    valid_gradient = {

        "type": "gradient",

        "shape_type": "rectangle",

        "width": 400,

        "height": 200,

        "direction": "vertical",

        "color_start": "#FFFFFF",

        "color_end": "#000000",

        "opacity": 1.0,

        "visible": True
    }


    validate_properties(
        valid_gradient
    )

    print(
        "✓ Valid gradient properties"
    )


    # ========================================================
    # INVALID OPACITY
    # ========================================================

    try:

        validate_properties({

            "type": "text",

            "opacity": 2.0
        })

        raise AssertionError(
            "Invalid opacity was accepted"
        )

    except ComponentSchemaError:

        print(
            "✓ Invalid opacity rejected"
        )


    # ========================================================
    # INVALID FONT WEIGHT
    # ========================================================

    try:

        validate_properties({

            "type": "text",

            "font_weight": 450
        })

        raise AssertionError(
            "Invalid font weight was accepted"
        )

    except ComponentSchemaError:

        print(
            "✓ Invalid font weight rejected"
        )


    # ========================================================
    # INVALID ALIGNMENT
    # ========================================================

    try:

        validate_properties({

            "type": "text",

            "align": "diagonal"
        })

        raise AssertionError(
            "Invalid alignment was accepted"
        )

    except ComponentSchemaError:

        print(
            "✓ Invalid alignment rejected"
        )


    # ========================================================
    # INVALID TYPE
    # ========================================================

    try:

        validate_properties({

            "type": "unknown"
        })

        raise AssertionError(
            "Invalid component type was accepted"
        )

    except ComponentSchemaError:

        print(
            "✓ Invalid component type rejected"
        )


    # ========================================================
    # COMPLETE
    # ========================================================

    print()
    print(
        "🟢 Component Property Schema validated"
    )

    print()