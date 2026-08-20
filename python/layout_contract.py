# ============================================================
# COUNTDOWN OS — LAYOUT CONTRACT
# Version: 1.2 Elegance
# ============================================================

"""
Define y normaliza el contrato de datos que conecta:

Layout Engine
      ↓
layout.json
      ↓
KWGT
"""


# ============================================================
# REQUIRED COMPONENT HIERARCHY
# ============================================================

REQUIRED_COMPONENTS = {
    "cover": [],

    "header": [
        "title",
        "days"
    ],

    "counter": [
        "days"
    ],

    "journey": [
        "line",
        "origin",
        "plane",
        "hearts"
    ],

    "footer": []
}


# ============================================================
# POSITION
# ============================================================

def normalize_position(position):
    """
    Normaliza una posición a:

    {
        "x": number,
        "y": number
    }
    """

    if not isinstance(position, dict):
        raise TypeError(
            f"Position must be a dict. "
            f"Received: {position}"
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
            f"Position coordinates must be numeric. "
            f"Received: {position}"
        ) from error

    return {
        "x": x,
        "y": y
    }


# ============================================================
# COMPONENT VALIDATION
# ============================================================

def validate_component_hierarchy(components):
    """
    Comprueba que todos los componentes requeridos
    existan en el Layout Contract.
    """

    if not isinstance(components, dict):
        raise TypeError(
            "Components must be a dictionary."
        )

    for component, children in REQUIRED_COMPONENTS.items():

        if component not in components:
            raise ValueError(
                f"Missing required component: "
                f"{component}"
            )

        component_data = components[component]

        if not isinstance(component_data, dict):
            raise TypeError(
                f"Component '{component}' "
                f"must be a dictionary."
            )

        for child in children:

            if child not in component_data:
                raise ValueError(
                    f"Missing required child "
                    f"'{component}.{child}'"
                )

    return True


# ============================================================
# COMPONENT NORMALIZATION
# ============================================================

def normalize_component(component):
    """
    Normaliza un componente individual.

    Si tiene position, garantiza que sus coordenadas
    sean numéricas.
    """

    if not isinstance(component, dict):
        raise TypeError(
            f"Component must be a dictionary. "
            f"Received: {component}"
        )

    normalized = dict(component)

    if "position" in normalized:
        normalized["position"] = normalize_position(
            normalized["position"]
        )

    return normalized


# ============================================================
# LAYOUT CONTRACT
# ============================================================

def build_layout_contract(layout):
    """
    Convierte el resultado del Layout Engine
    en el contrato público de layout.json.
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

    canvas = layout["canvas"]
    components = layout["components"]

    # --------------------------------------------------------
    # Canvas
    # --------------------------------------------------------

    if not isinstance(canvas, dict):
        raise TypeError(
            "Canvas must be a dictionary."
        )

    try:
        canvas_width = float(canvas["width"])
        canvas_height = float(canvas["height"])

    except (KeyError, TypeError, ValueError) as error:
        raise ValueError(
            "Canvas must contain numeric "
            "'width' and 'height'."
        ) from error

    canvas_contract = {
        "width": canvas_width,
        "height": canvas_height,
        "anchor": canvas.get(
            "anchor",
            "center"
        )
    }

    # --------------------------------------------------------
    # Validate hierarchy
    # --------------------------------------------------------

    validate_component_hierarchy(
        components
    )

    # --------------------------------------------------------
    # Normalize components
    # --------------------------------------------------------

    components_contract = {}

    for component_name, component_data in components.items():

        components_contract[
            component_name
        ] = normalize_component(
            component_data
        )

    # --------------------------------------------------------
    # Public contract
    # --------------------------------------------------------

    return {
        "layout": {
            "canvas": canvas_contract,
            "components": components_contract
        }
    }