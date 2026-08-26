# ============================================================
# COUNTDOWN OS — COMPONENT SCHEMA
# Version: 1.2 Elegance
# ============================================================

"""
Contrato de propiedades del Component System.

Este módulo define:

    - qué propiedades puede tener cada tipo de componente
    - qué propiedades son obligatorias
    - qué tipos de valores son válidos
    - cómo validar un conjunto de properties

IMPORTANTE:

Este módulo NO conoce:

    - KWGT
    - coordenadas
    - Web Get
    - layout_tokens
    - progress
    - rendering

Su responsabilidad es únicamente validar
las propiedades abstractas de los componentes.
"""


# ============================================================
# PROPERTY TYPES
# ============================================================

PROPERTY_TYPES = {

    "type": str,

    "font_size": (int, float),

    "value": str,

    "width": (int, float),

    "height": (int, float),

    "size": (int, float),

    "radius": (int, float),

    "shape_type": str,

    "direction": str,

    "color": str,

    "opacity": (int, float),

    "weight": (int, float),

    "alignment": str,

}


# ============================================================
# COMPONENT SCHEMAS
# ============================================================

COMPONENT_SCHEMAS = {

    # ========================================================
    # CONTAINER
    # ========================================================

    "container": {

        "allowed": {
            "type",
        },

        "required": {
            "type",
        },
    },


    # ========================================================
    # TEXT
    # ========================================================

    "text": {

        "allowed": {
            "type",
            "font_size",
            "value",
            "alignment",
            "weight",
        },

        "required": {
            "type",
        },
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
        },

        "required": {
            "type",
        },
    },


    # ========================================================
    # GRADIENT
    # ========================================================

    "gradient": {

        "allowed": {
            "type",
            "direction",
            "color",
            "opacity",
            "width",
            "height",
        },

        "required": {
            "type",
        },
    },
}


# ============================================================
# VALID COMPONENT TYPES
# ============================================================

VALID_COMPONENT_TYPES = set(
    COMPONENT_SCHEMAS.keys()
)


# ============================================================
# VALIDATION ERROR
# ============================================================

class ComponentSchemaError(ValueError):
    """
    Error producido cuando un componente
    no cumple su contrato de propiedades.
    """

    pass


# ============================================================
# COMPONENT TYPE
# ============================================================

def get_component_type(properties):
    """
    Obtiene el tipo declarado por un conjunto
    de properties.

    El campo `type` es obligatorio.
    """

    if not isinstance(properties, dict):

        raise ComponentSchemaError(
            "Component properties must be a dictionary"
        )

    if "type" not in properties:

        raise ComponentSchemaError(
            "Component properties require 'type'"
        )

    component_type = properties["type"]

    if not isinstance(
        component_type,
        str
    ):

        raise ComponentSchemaError(
            "Component 'type' must be a string"
        )

    if component_type not in VALID_COMPONENT_TYPES:

        raise ComponentSchemaError(
            "Unknown component type: "
            f"{component_type}"
        )

    return component_type


# ============================================================
# PROPERTY TYPE VALIDATION
# ============================================================

def validate_property_type(
    key,
    value,
):
    """
    Valida que una propiedad utilice
    el tipo de dato correcto.
    """

    if key not in PROPERTY_TYPES:

        return

    expected_type = PROPERTY_TYPES[key]

    if not isinstance(
        value,
        expected_type
    ):

        raise ComponentSchemaError(
            f"Property '{key}' has invalid type. "
            f"Expected {expected_type}, "
            f"got {type(value).__name__}"
        )


# ============================================================
# PROPERTY VALUE VALIDATION
# ============================================================

def validate_property_value(
    key,
    value,
):
    """
    Valida restricciones básicas de valores.
    """

    if key in {
        "font_size",
        "width",
        "height",
        "size",
        "radius",
    }:

        if value < 0:

            raise ComponentSchemaError(
                f"Property '{key}' "
                "cannot be negative"
            )


    if key == "opacity":

        if value < 0 or value > 1:

            raise ComponentSchemaError(
                "Property 'opacity' "
                "must be between 0 and 1"
            )


    if key == "alignment":

        valid_alignments = {
            "left",
            "center",
            "right",
        }

        if value not in valid_alignments:

            raise ComponentSchemaError(
                "Invalid alignment: "
                f"{value}"
            )


    if key == "shape_type":

        valid_shapes = {
            "rectangle",
            "circle",
            "line",
        }

        if value not in valid_shapes:

            raise ComponentSchemaError(
                "Invalid shape_type: "
                f"{value}"
            )


    if key == "direction":

        valid_directions = {
            "vertical",
            "horizontal",
            "diagonal",
        }

        if value not in valid_directions:

            raise ComponentSchemaError(
                "Invalid gradient direction: "
                f"{value}"
            )


# ============================================================
# VALIDATE PROPERTIES
# ============================================================

def validate_properties(properties):
    """
    Valida completamente un conjunto de properties.

    Devuelve True si el contrato es válido.
    """

    component_type = get_component_type(
        properties
    )

    schema = COMPONENT_SCHEMAS[
        component_type
    ]

    allowed = schema["allowed"]

    required = schema["required"]


    # ========================================================
    # REQUIRED
    # ========================================================

    missing = required - set(
        properties.keys()
    )

    if missing:

        raise ComponentSchemaError(
            "Missing required properties: "
            f"{sorted(missing)}"
        )


    # ========================================================
    # UNKNOWN PROPERTIES
    # ========================================================

    unknown = (
        set(properties.keys())
        - allowed
    )

    if unknown:

        raise ComponentSchemaError(
            "Unknown properties for "
            f"component type '{component_type}': "
            f"{sorted(unknown)}"
        )


    # ========================================================
    # PROPERTY TYPES + VALUES
    # ========================================================

    for key, value in properties.items():

        validate_property_type(
            key,
            value
        )

        validate_property_value(
            key,
            value
        )


    return True


# ============================================================
# COMPONENT TYPE VALIDATION
# ============================================================

def validate_component_type(
    component_type
):
    """
    Comprueba que exista un tipo de componente válido.
    """

    if component_type not in VALID_COMPONENT_TYPES:

        raise ComponentSchemaError(
            "Unknown component type: "
            f"{component_type}"
        )

    return True


# ============================================================
# SCHEMA ACCESS
# ============================================================

def get_schema(
    component_type
):
    """
    Devuelve una copia del schema
    de un tipo de componente.
    """

    validate_component_type(
        component_type
    )

    schema = COMPONENT_SCHEMAS[
        component_type
    ]

    return {

        "allowed": set(
            schema["allowed"]
        ),

        "required": set(
            schema["required"]
        ),
    }


# ============================================================
# MANUAL TEST
# ============================================================

if __name__ == "__main__":

    print()
    print("=" * 50)
    print("       COUNTDOWN OS — COMPONENT SCHEMA")
    print("=" * 50)


    # ========================================================
    # VALID TEXT
    # ========================================================

    text_properties = {

        "type": "text",

        "font_size": 30,

        "value": "✈",

        "alignment": "center",

        "weight": 400,
    }

    validate_properties(
        text_properties
    )

    print(
        "✓ Text schema valid"
    )


    # ========================================================
    # VALID SHAPE
    # ========================================================

    shape_properties = {

        "type": "shape",

        "shape_type": "circle",

        "size": 5,
    }

    validate_properties(
        shape_properties
    )

    print(
        "✓ Shape schema valid"
    )


    # ========================================================
    # VALID GRADIENT
    # ========================================================

    gradient_properties = {

        "type": "gradient",

        "direction": "vertical",

        "color": "#000000",

        "opacity": 0.5,

        "width": 400,

        "height": 200,
    }

    validate_properties(
        gradient_properties
    )

    print(
        "✓ Gradient schema valid"
    )


    # ========================================================
    # VALID CONTAINER
    # ========================================================

    container_properties = {

        "type": "container"
    }

    validate_properties(
        container_properties
    )

    print(
        "✓ Container schema valid"
    )


    # ========================================================
    # SUCCESS
    # ========================================================

    print()
    print(
        "🟢 Component schema validated"
    )
    print()