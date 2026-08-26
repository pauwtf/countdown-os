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
# COMPONENT TYPE
# ============================================================

def get_component_type(properties):

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