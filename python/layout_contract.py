# ============================================================
# COUNTDOWN OS — LAYOUT CONTRACT
# Version: 1.2 Elegance
# ============================================================

"""
Contrato entre la jerarquía real de KWGT
y el Layout Engine de Countdown OS.

La jerarquía aquí debe reflejar 1:1
la estructura del widget en KWGT.
"""


# ============================================================
# OFFICIAL KWGT HIERARCHY
# ============================================================

REQUIRED_HIERARCHY = {

    "Background": {

        "Background_shape": {

            "BackgroundShape": {}
        }
    },

    "Cover": {

        "coverImage": {

            "coverText": {}
        }
    },

    "Header": {

        "Title": {

            "TitleText": {}
        },

        "Days": {

            "DaysText": {}
        }
    },

    "Gradient": {

        "Vertical": {

            "GradientVerticalShape": {}
        },

        "Horizontal": {

            "GradientHorizontalShape": {}
        }
    },

    "Counter": {

        "DaysRemaining": {

            "DaysRemainingText": {}
        }
    },

    "Content": {

        "journey": {

            "Line": {

                "JourneyLineShape": {}
            },

            "Origin": {

                "OriginShape": {}
            },

            "Plane": {

                "PlaneText": {}
            },

            "Hearts": {

                "Destination": {

                    "DestinationText": {}
                },

                "Arrival": {

                    "ArrivalText": {}
                }
            }
        }
    },

    "Footer": {

        "FooterText": {}
    },

    "test": {

        "TestText": {}
    }
}


# ============================================================
# HIERARCHY VALIDATION
# ============================================================

def validate_hierarchy(
    actual,
    expected,
    path=""
):
    """
    Comprueba recursivamente que la jerarquía
    generada por el Layout Engine coincida con
    la jerarquía oficial de KWGT.
    """

    if not isinstance(actual, dict):

        raise TypeError(
            f"Component '{path}' "
            f"must be a dictionary."
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
                f"KWGT component "
                f"'{current_path}' "
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
    Garantiza que una posición tenga
    coordenadas numéricas.
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
            f"Position coordinates "
            f"must be numeric: {position}"
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
    Normaliza recursivamente un componente.

    Las propiedades position son convertidas
    a coordenadas numéricas.
    """

    if not isinstance(
        component,
        dict
    ):

        raise TypeError(
            f"Component must be "
            f"a dictionary: {component}"
        )

    normalized = {}

    for key, value in component.items():

        if key == "position":

            normalized[key] = (
                normalize_position(value)
            )

        elif isinstance(
            value,
            dict
        ):

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

    if not isinstance(
        canvas,
        dict
    ):

        raise TypeError(
            "Canvas must be a dictionary."
        )

    try:

        width = float(
            canvas["width"]
        )

        height = float(
            canvas["height"]
        )

    except (
        KeyError,
        TypeError,
        ValueError
    ) as error:

        raise ValueError(
            "Canvas requires numeric "
            "width and height."
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
# BUILD CONTRACT
# ============================================================

def build_layout_contract(layout):
    """
    Construye el contrato público de layout.json.
    """

    if not isinstance(
        layout,
        dict
    ):

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

    # --------------------------------------------------------
    # CANVAS
    # --------------------------------------------------------

    canvas = normalize_canvas(
        layout["canvas"]
    )

    # --------------------------------------------------------
    # COMPONENTS
    # --------------------------------------------------------

    components = layout["components"]

    # --------------------------------------------------------
    # HIERARCHY
    # --------------------------------------------------------

    validate_hierarchy(
        components,
        REQUIRED_HIERARCHY
    )

    # --------------------------------------------------------
    # NORMALIZE
    # --------------------------------------------------------

    normalized_components = (
        normalize_component(
            components
        )
    )

    # --------------------------------------------------------
    # PUBLIC CONTRACT
    # --------------------------------------------------------

    return {

        "layout": {

            "canvas": canvas,

            "components":
                normalized_components
        }
    }