# ============================================================
# COUNTDOWN OS — LAYOUT ENGINE
# Version: 1.2 Elegance
# ============================================================

from layout_tokens import (
    CANVAS,
    BACKGROUND,
    COVER,
    HEADER,
    GRADIENT,
    COUNTER,
    CONTENT,
    JOURNEY,
    FOOTER,
    TEST
)

from component import (
    build_countdown_tree,
    build_component_tree,
)

from kwgt_coordinate_adapter import (
    adapt_directional_position,
    adapt_dual_x_position
)


# ============================================================
# POSITION RESOLUTION
# ============================================================

def resolve_position(parent_position, local_position):
    """
    Resuelve una posición parent-relative.

    absolute = parent + local
    """

    parent_x, parent_y = parent_position
    local_x, local_y = local_position

    try:
        parent_x = float(parent_x)
        parent_y = float(parent_y)
        local_x = float(local_x)
        local_y = float(local_y)

    except (TypeError, ValueError) as error:

        raise TypeError(
            "Layout coordinates must be numeric. "
            f"parent={parent_position}, "
            f"local={local_position}"
        ) from error

    return {
        "x": parent_x + local_x,
        "y": parent_y + local_y
    }


# ============================================================
# KWGT POSITION HELPERS
# ============================================================

def resolve_kwgt_position(position):
    """
    Convierte una posición interna del Layout Engine
    a coordenadas direccionales de KWGT.

    Countdown OS:

        +X = derecha
        -X = izquierda
        +Y = arriba
        -Y = abajo
    """

    return adapt_directional_position(
        position["x"],
        position["y"]
    )


# ============================================================
# PROGRESS
# ============================================================

def normalize_progress(progress):
    """
    Normaliza progress al rango 0..1.
    """

    if progress is None:
        return 0.0

    try:
        progress = float(progress)

    except (TypeError, ValueError) as error:

        raise TypeError(
            f"Progress must be numeric: {progress}"
        ) from error

    return max(
        0.0,
        min(progress, 1.0)
    )


# ============================================================
# PLANE
# ============================================================

def resolve_plane_position(progress):
    """
    Calcula la posición dinámica del Plane.

    El Plane utiliza dos coordenadas X:
        x_left
        x_right

    y permanece independiente.
    """

    progress = normalize_progress(progress)

    return {
        "x_left": (
            JOURNEY["plane"]["travel"]
            * progress
        ),

        "x_right": (
            JOURNEY["plane"]["x_right"]
        ),

        "y": (
            JOURNEY["plane"]["y"]
        )
    }


# ============================================================
# COMPONENT DATA
# ============================================================

def build_component_data(event):
    """
    Construye los datos visuales que alimentan
    el Component System.

    Esta función NO cambia el modelo de componentes.
    Solo prepara los valores dinámicos del evento.
    """

    progress = normalize_progress(
        event.get("progress")
    )

    plane = resolve_plane_position(
        progress
    )

    return {

        "title": event.get(
            "titleDisplay",
            ""
        ),

        "days": event.get(
            "daysDisplay",
            ""
        ),

        "notes": event.get(
            "notesDisplay",
            ""
        ),

        "destination": event.get(
            "destinationDisplay",
            ""
        ),

        "arrival": event.get(
            "arrivalDisplay",
            ""
        ),

        "progress": progress,

        "plane": plane
    }


# ============================================================
# COMPONENT TREE
# ============================================================

def build_layout_components(event):
    """
    Construye el árbol de componentes de Countdown OS.

    El Component System controla la jerarquía.
    El Layout Engine controla los datos y posiciones.
    """

    data = build_component_data(event)

    tree = build_countdown_tree(
        data=data
    )

    return tree


# ============================================================
# BUILD LAYOUT
# ============================================================

def build_layout(event):

    # --------------------------------------------------------
    # COMPONENT TREE
    # --------------------------------------------------------

    components = build_layout_components(
        event
    )

    # --------------------------------------------------------
    # LAYOUT CONTRACT
    # --------------------------------------------------------

    layout = {

        "version": "1.2",

        "system": (
            "Countdown OS Layout System"
        ),

        "canvas": {

            "width": CANVAS["width"],

            "height": CANVAS["height"],

            "anchor": CANVAS["anchor"]
        },

        "components": components
    }

    return layout