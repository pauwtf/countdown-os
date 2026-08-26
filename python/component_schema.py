# ============================================================
# COUNTDOWN OS — COMPONENT PROPERTY SCHEMA
# Version: 1.2 Elegance
# ============================================================


class ComponentSchemaError(Exception):
    """
    Error producido cuando un componente
    no cumple el schema definido.
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

        "allowed": {

            "type",

            "visible"
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

            "color",

            "opacity",

            "visible",

            "radius"
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

            "color_start",

            "color_end",

            "opacity",

            "angle",

            "visible"
        }
    }
}


# ============================================================
# COMPONENT TYPE
# ============================================================

def get_component_type(properties):

    if not isinstance(properties, dict):

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

    if component_type not in PROPERTY_SCHEMA:

        raise ComponentSchemaError(
            f"Unknown component type: "
            f"'{component_type}'"
        )

    return component_type


# ============================================================
# PROPERTY VALIDATION
# ============================================================

def validate_properties(properties):

    if not isinstance(properties, dict):

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

    for key in properties:

        if key not in allowed_properties:

            raise ComponentSchemaError(
                f"Property '{key}' is not allowed "
                f"for component type "
                f"'{component_type}'"
            )

    return True


# ============================================================
# COMPONENT VALIDATION
# ============================================================

def validate_component(component):

    if component is None:

        raise ComponentSchemaError(
            "Component cannot be None"
        )

    properties = component.properties

    validate_properties(
        properties
    )

    return True