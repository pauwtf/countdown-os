# ============================================================
# COUNTDOWN OS — LAYOUT CONTRACT
# Version: 1.2 Elegance
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


def validate_hierarchy(actual, expected, path=""):

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
                f"Missing KWGT component: {current_path}"
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


def build_layout_contract(layout):

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

    validate_hierarchy(
        layout["components"],
        REQUIRED_HIERARCHY
    )

    return layout