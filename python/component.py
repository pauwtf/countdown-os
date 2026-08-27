# ============================================================
# COUNTDOWN OS — COMPONENT SYSTEM
# Version: 1.2 Elegance
# ============================================================

from component_schema import (
    validate_properties,
)


# ============================================================
# COMPONENT
# ============================================================

class Component:
    """
    Componente base del sistema visual de Countdown OS.

    Cada componente contiene:

        - name
        - properties
        - children

    Las properties representan características
    visuales abstractas del componente.

    IMPORTANTE:

    El Component System NO conoce:

        - KWGT
        - coordenadas KWGT
        - Web Get
        - fórmulas KWGT
        - lógica de rendering

    Es independiente del sistema de coordenadas.
    """

    def __init__(
        self,
        name,
        properties=None,
    ):

        if not isinstance(
            name,
            str
        ):
            raise TypeError(
                "Component name must be a string"
            )

        if not name.strip():
            raise ValueError(
                "Component name cannot be empty"
            )

        self.name = name

        self.properties = (
            properties.copy()
            if properties
            else {}
        )

        self.children = []

        # ====================================================
        # PROPERTY VALIDATION
        # ====================================================

        if self.properties:
            validate_properties(
                self.properties
            )


    # ========================================================
    # VALIDATION
    # ========================================================

    def validate(self):
        """
        Valida las propiedades actuales
        contra Component Property Schema.
        """

        validate_properties(
            self.properties
        )

        return True


    # ========================================================
    # PROPERTIES
    # ========================================================

    def set_property(
        self,
        key,
        value,
    ):
        """
        Define o actualiza una propiedad.

        La propiedad se valida inmediatamente.
        """

        if not isinstance(
            key,
            str
        ):
            raise TypeError(
                "Property key must be a string"
            )

        if not key.strip():
            raise ValueError(
                "Property key cannot be empty"
            )

        candidate = self.properties.copy()

        candidate[key] = value

        validate_properties(
            candidate
        )

        self.properties[key] = value

        return value


    def get_property(
        self,
        key,
        default=None,
    ):
        """
        Obtiene una propiedad.

        Si no existe, devuelve default.
        """

        return self.properties.get(
            key,
            default
        )


    def has_property(
        self,
        key,
    ):
        """
        Comprueba si el componente posee
        una propiedad.
        """

        return key in self.properties


    def remove_property(
        self,
        key,
    ):
        """
        Elimina una propiedad.

        Devuelve True si existía.
        """

        if key in self.properties:

            del self.properties[key]

            return True

        return False


    # ========================================================
    # CHILDREN
    # ========================================================

    def add_child(
        self,
        component,
    ):
        """
        Añade un componente hijo.
        """

        if not isinstance(
            component,
            Component
        ):
            raise TypeError(
                "component must be an instance of Component"
            )

        self.children.append(
            component
        )

        return component


    # ========================================================
    # FIND
    # ========================================================

    def find(
        self,
        name,
    ):
        """
        Busca recursivamente un componente
        por nombre.
        """

        if self.name == name:
            return self

        for child in self.children:

            result = child.find(
                name
            )

            if result is not None:
                return result

        return None


    # ========================================================
    # SERIALIZATION
    # ========================================================

    def to_dict(self):
        """
        Convierte el componente y sus hijos
        en una estructura de diccionario.

        Las propiedades pertenecen directamente
        al componente.

        Los hijos aparecen bajo su propio nombre.
        """

        result = {}

        result.update(
            self.properties
        )

        for child in self.children:

            result[child.name] = (
                child.to_dict()
            )

        return result


# ============================================================
# COUNTDOWN OS COMPONENT TREE
# ============================================================

def build_countdown_tree():
    """
    Construye la jerarquía visual de Countdown OS.

    Las propiedades visuales conocidas del widget
    se almacenan en los componentes.

    Las coordenadas continúan perteneciendo
    al Layout Engine.
    """

    # ========================================================
    # ROOT
    # ========================================================

    countdown = Component(
        "Countdown",
        properties={
            "type": "container"
        }
    )


    # ========================================================
    # BACKGROUND
    # ========================================================

    background = Component(
        "Background",
        properties={
            "type": "container"
        }
    )

    countdown.add_child(
        background
    )


    # ========================================================
    # COVER
    # ========================================================

    cover = Component(
        "Cover",
        properties={
            "type": "container"
        }
    )

    cover_text = Component(
        "CoverText",
        properties={
            "type": "text",

            "value": "♥",

            "font_family": "Roboto",

            "font_size": 240,

            "color": "#FFFFFF",

            "opacity": 0.30,

            "visible": True,

            "align": "left"
        }
    )

    cover.add_child(
        cover_text
    )

    countdown.add_child(
        cover
    )


    # ========================================================
    # HEADER
    # ========================================================

    header = Component(
        "Header",
        properties={
            "type": "container"
        }
    )


    # ========================================================
    # TITLE
    # ========================================================

    title = Component(
        "Title",
        properties={
            "type": "text",

            "font_family": "Cutive Mono",

            "font_size": 18,

            "color": "#FFFFFF",

            "opacity": 0.86,

            "visible": True,

            "align": "left"
        }
    )


    # ========================================================
    # DAYS
    # ========================================================

    days = Component(
        "Days",
        properties={
            "type": "text",

            "font_family": "Cutive Mono",

            "font_size": 15,

            "color": "#FFFFFF",

            "opacity": 1.0,

            "visible": True,

            "align": "left",

            "value": "days"
        }
    )


    header.add_child(
        title
    )

    header.add_child(
        days
    )

    countdown.add_child(
        header
    )


    # ========================================================
    # GRADIENT
    # ========================================================

    gradient = Component(
        "Gradient",
        properties={
            "type": "container"
        }
    )


    # ========================================================
    # VERTICAL GRADIENT
    # ========================================================

    vertical = Component(
        "Vertical",
        properties={
            "type": "gradient",

            "shape_type": "rectangle",

            "width": 380,

            "height": 180,

            "direction": "vertical",

            "color_start": "#FFFFFF",

            "color_end": "#000000",

            "visible": True
        }
    )


    # ========================================================
    # HORIZONTAL GRADIENT
    # ========================================================

    horizontal = Component(
        "Horizontal",
        properties={
            "type": "gradient",

            "shape_type": "rectangle",

            "width": 380,

            "height": 180,

            "direction": "horizontal",

            "color_start": "#FFFFFF",

            "color_end": "#000000",

            "visible": True
        }
    )


    gradient.add_child(
        vertical
    )

    gradient.add_child(
        horizontal
    )

    countdown.add_child(
        gradient
    )


    # ========================================================
    # COUNTER
    # ========================================================

    counter = Component(
        "Counter",
        properties={
            "type": "container"
        }
    )


    # ========================================================
    # DAYS REMAINING
    # ========================================================

    days_remaining = Component(
        "DaysRemaining",
        properties={
            "type": "text",

            "font_family": "Cutive Mono",

            "font_size": 100,

            "color": "#FFFFFF",

            "opacity": 1.0,

            "visible": True,

            "align": "left"
        }
    )


    counter.add_child(
        days_remaining
    )

    countdown.add_child(
        counter
    )


    # ========================================================
    # CONTENT
    # ========================================================

    content = Component(
        "Content",
        properties={
            "type": "container"
        }
    )


    # ========================================================
    # JOURNEY
    # ========================================================

    journey = Component(
        "Journey",
        properties={
            "type": "container"
        }
    )

    content.add_child(
        journey
    )

    countdown.add_child(
        content
    )


    # ========================================================
    # LINE
    # ========================================================

    line = Component(
        "Line",
        properties={
            "type": "shape",

            "shape_type": "rectangle",

            "width": 258,

            "height": 1,

            "radius": 20,

            "color": "#FFFFFF",

            "opacity": 0.60,

            "visible": True
        }
    )


    # ========================================================
    # ORIGIN
    # ========================================================

    origin = Component(
        "Origin",
        properties={
            "type": "shape",

            "shape_type": "circle",

            "size": 5,

            "color": "#FFFFFF",

            "opacity": 1.0,

            "visible": True
        }
    )


    # ========================================================
    # PLANE
    # ========================================================

    plane = Component(
        "Plane",
        properties={
            "type": "text",

            "font_family": "Cutive Mono",

            "font_size": 30,

            "color": "#FFFFFF",

            "opacity": 1.0,

            "visible": True,

            "align": "left",

            "value": "✈"
        }
    )


    # ========================================================
    # HEARTS
    # ========================================================

    hearts = Component(
        "Hearts",
        properties={
            "type": "container"
        }
    )


    # ========================================================
    # DESTINATION
    # ========================================================

    destination = Component(
        "Destination",
        properties={
            "type": "text",

            "font_family": "Cutive Mono",

            "font_size": 14,

            "color": "#FFFFFF",

            "opacity": 1.0,

            "visible": True,

            "align": "left",

            "value": "♡"
        }
    )


    # ========================================================
    # ARRIVAL
    # ========================================================

    arrival = Component(
        "Arrival",
        properties={
            "type": "text",

            "font_family": "Cutive Mono",

            "font_size": 14,

            "color": "#FFFFFF",

            "opacity": 1.0,

            "visible": True,

            "align": "left",

            "value": "❤️"
        }
    )


    # ========================================================
    # JOURNEY CHILDREN
    # ========================================================

    journey.add_child(
        line
    )

    journey.add_child(
        origin
    )

    journey.add_child(
        plane
    )

    journey.add_child(
        hearts
    )


    # ========================================================
    # HEART CHILDREN
    # ========================================================

    hearts.add_child(
        destination
    )

    hearts.add_child(
        arrival
    )


    # ========================================================
    # FOOTER
    # ========================================================

    footer = Component(
        "Footer",
        properties={
            "type": "text",

            "visible": True,

            "opacity": 1.0
        }
    )

    countdown.add_child(
        footer
    )


    # ========================================================
    # RETURN TREE
    # ========================================================

    return countdown


# ============================================================
# TREE SERIALIZATION
# ============================================================

def build_component_tree():
    """
    Construye el árbol y devuelve su representación
    serializable.
    """

    tree = build_countdown_tree()

    return {
        tree.name: tree.to_dict()
    }


# ============================================================
# MANUAL TEST
# ============================================================

if __name__ == "__main__":

    tree = build_countdown_tree()

    print()
    print("=" * 60)
    print("       COUNTDOWN OS — COMPONENT SYSTEM")
    print("=" * 60)

    print()
    print(
        f"Root: {tree.name}"
    )

    print()
    print("Children:")

    for child in tree.children:

        print(
            f"  └── {child.name}"
        )

    print()
    print(
        f"Found Plane: "
        f"{tree.find('Plane') is not None}"
    )

    print()
    print(
        f"Plane type: "
        f"{tree.find('Plane').get_property('type')}"
    )

    print()
    print(
        f"Title font size: "
        f"{tree.find('Title').get_property('font_size')}"
    )

    print()
    print(
        f"Title opacity: "
        f"{tree.find('Title').get_property('opacity')}"
    )

    print()
    print(
        f"Title color: "
        f"{tree.find('Title').get_property('color')}"
    )

    print()
    print(
        f"Days Remaining font size: "
        f"{tree.find('DaysRemaining').get_property('font_size')}"
    )

    print()
    print("🟢 Component properties initialized")
    print()