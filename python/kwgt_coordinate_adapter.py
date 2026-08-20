# ============================================================
# COUNTDOWN OS — KWGT COORDINATE ADAPTER
# Version: 1.2 Elegance
# ============================================================


def adapt_directional_position(x, y):
    """
    Converts Countdown OS signed coordinates into
    KWGT directional position fields.

    Countdown OS:
        +X = right
        -X = left
        +Y = down
        -Y = up

    KWGT:
        x_right
        x_left
        y_down
        y_up
    """

    x = float(x or 0)
    y = float(y or 0)

    return {
        "x_right": max(x, 0),
        "x_left": max(-x, 0),
        "y_down": max(y, 0),
        "y_up": max(-y, 0)
    }


def adapt_dual_x_position(x_left, x_right, y):
    """
    Converts a KWGT dual-X component.

    Used by components such as Plane that expose:
        X left
        X right
        Y
    """

    return {
        "x_left": float(x_left or 0),
        "x_right": float(x_right or 0),
        "y": float(y or 0)
    }