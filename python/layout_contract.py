# ============================================================
# COUNTDOWN OS — LAYOUT CONTRACT
# Version: 1.2 Elegance
# ============================================================

"""
Contrato formal entre:

KWGT Component Hierarchy
        ↓
Layout Engine
        ↓
layout.json
        ↓
KWGT Renderer
"""


# ============================================================
# OFFICIAL KWGT HIERARCHY
# ============================================================

REQUIRED_HIERARCHY = {
    "background": {},

    "cover": {
        "image": {
            "text": {}
        }
    },

    "header": {
        "title": {
            "text": {}
        },
        "days": {
            "text": {}
        }
    },

    "gradient": {
        "vertical": {},
        "horizontal": {}
    },

    "counter": {
        "days_remaining": {
            "text": {}
        }
    },

    "content": {
        "journey": {
            "line": {
                "shape": {}
            },

            "origin": {
                "shape": {}
            },

            "plane": {
                "text": {}
            },

            "hearts": {
                "destination": {
                    "text": {}
                },

                "arrival": {
                    "text": {}
                }
            }
        }
    },

    "footer": {
        "text": {}
    },

    "test": {}
}


# ============================================================
# REQUIRED COMPONENTS
# ============================================================

def validate_hierarchy(
    actual,
    expected,
    path=""
):
    """
    Compara recursivamente la jerarquía generada
    contra la jerarquía oficial de KWGT.

    No comprueba todavía valores visuales.
    Comprueba únicamente estructura.
    """

    if not isinstance(actual, dict):
        raise TypeError(
            f"Component '{path}' must be a dictionary."
        )

    for name, children in expected.items():

        current_path = (
            f"{path}.{name}"
            if path
            else name
        )

        if name not in actual:
            raise ValueError(
                f"Missing KWGT component: "
                f"{current_path}"
            )

        actual_component = actual[name]

        if not isinstance(
            actual_component,
            dict
        ):
            raise TypeError(
                f"KWGT component '{current_path}' "
                f"must be a dictionary."
            )

        validate_hierarchy(
            actual_component,
            children,
            current_path
        )

    return True


# ============================================================
# POSITION
# ============================================================

def normalize_position(position):
    """
    Garantiza que una posición tenga coordenadas numéricas.
    """

    if not isinstance(position, dict):
        raise TypeError(
            "Position must be a dictionary."
        )

    if "x" not in position:
        raise ValueError(
            "Position is missing 'x'."
        )

    if "y" not in position:
        raise ValueError(
            "Position is missing 'y'."
        )

    try:
        x = float(position["x"])
        y = float(position["y"])

    except (TypeError, ValueError) as error:
        raise TypeError(
            f"Position coordinates must be numeric: "
            f"{position}"
        ) from error

    return {
        "x": x,
        "y": y
    }


# ============================================================
# COMPONENT NORMALIZATION
# ============================================================

def normalize_component(component):
    """
    Normaliza un componente sin modificar
    su contenido visual.
    """

    if not isinstance(component, dict):
        raise TypeError(
            f"Component must be a dictionary: "
            f"{component}"
        )

    normalized = {}

    for key, value in component.items():

        if key == "position":

            normalized[key] = normalize_position(
                value
            )

        elif isinstance(value, dict):

            normalized[key] = (
                normalize_component(value)
            )

        else:

            normalized[key] = value

    return normalized


# ============================================================
# CANVAS
# ============================================================

def normalize_canvas(canvas):
    """
    Normaliza las dimensiones del canvas.
    """

    if not isinstance(canvas, dict):
        raise TypeError(
            "Canvas must be a dictionary."
        )

    try:
        width = float(canvas["width"])
        height = float(canvas["height"])

    except (KeyError, TypeError, ValueError) as error:
        raise ValueError(
            "Canvas requires numeric width "
            "and height."
        ) from error

    return {
        "width": width,
        "height": height,
        "anchor": canvas.get(
            "anchor",
            "center"
        )
    }


# ============================================================
# LAYOUT CONTRACT
# ============================================================

def build_layout_contract(layout):
    """
    Construye el contrato público de layout.json.

    La jerarquía debe corresponder a la estructura
    real documentada del widget en KWGT.
    """

    if not isinstance(layout, dict):
        raise TypeError(
            "Layout must be a dictionary."
        )

    if "canvas" not in layout:
        raise ValueError(
            "Layout is missing 'canvas'."
        )

    if "components" not in layout:
        raise ValueError(
            "Layout is missing 'components'."
        )

    canvas = normalize_canvas(
        layout["canvas"]
    )

    components = layout["components"]

    # --------------------------------------------------------
    # Hierarchy validation
    # --------------------------------------------------------

    validate_hierarchy(
        components,
        REQUIRED_HIERARCHY
    )

    # --------------------------------------------------------
    # Normalize components
    # --------------------------------------------------------

    normalized_components = (
        normalize_component(
            components
        )
    )

    # --------------------------------------------------------
    # Public contract
    # --------------------------------------------------------

    return {
        "layout": {
            "canvas": canvas,
            "components": normalized_components
        }
    }