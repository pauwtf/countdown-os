# ============================================================
# COUNTDOWN OS — COMPONENT SYSTEM
# Version: 1.2 Elegance
# ============================================================

from component_schema import (
    validate_properties
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

        if not isinstance(name, str):

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

        self.validate()


    # ========================================================
    # VALIDATION
    # ========================================================

    def validate(self):

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

        La propiedad se valida inmediatamente
        contra el Component Property Schema.
        """

        if not isinstance(key, str):

            raise TypeError(
                "Property key must be a string"
            )

        if not key.strip():

            raise ValueError(
                "Property key cannot be empty"
            )

        self.properties[key] = value

        self.validate()

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

    Las propiedades visuales abstractas pertenecen
    al Component System.

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
            "type": "container",
            "visible": True,
            "opacity": 1.0
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
            "type": "container",
            "visible": True,
            "opacity": 1.0
        }
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
            "type": "container",
            "visible": True,
            "opacity": 1.0
        }
    )


    title = Component(
        "Title",
        properties={
            "type": "text",

            "font_size": 40,

            "font_weight": "regular",

            "color": "white",

            "align": "left",

            "visible": True,

            "opacity": 1.0
        }
    )


    days = Component(
        "Days",
        properties={
            "type": "text",

            "font_size": 18,

            "font_weight": "regular",

            "color": "white",

            "align": "left",

            "value": "days",

            "visible": True,

            "opacity": 1.0
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
            "type": "container",
            "visible": True,
            "opacity": 1.0
        }
    )


    vertical = Component(
        "Vertical",
        properties={
            "type": "gradient",

            "shape_type": "rectangle",

            "direction": "vertical",

            "color_start": "transparent",

            "color_end": "black",

            "opacity": 1.0,

            "visible": True
        }
    )


    horizontal = Component(
        "Horizontal",
        properties={
            "type": "gradient",

            "shape_type": "rectangle",

            "direction": "horizontal",

            "color_start": "transparent",

            "color_end": "black",

            "opacity": 1.0,

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
            "type": "container",
            "visible": True,
            "opacity": 1.0
        }
    )


    days_remaining = Component(
        "DaysRemaining",
        properties={
            "type": "text",

            "font_size": 20,

            "font_weight": "regular",

            "color": "white",

            "align": "left",

            "visible": True,

            "opacity": 1.0
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
            "type": "container",
            "visible": True,
            "opacity": 1.0
        }
    )


    journey = Component(
        "Journey",
        properties={
            "type": "container",
            "visible": True,
            "opacity": 1.0
        }
    )


    content.add_child(
        journey
    )

    countdown.add_child(
        content
    )


    # ========================================================
    # JOURNEY
    # ========================================================

    line = Component(
        "Line",
        properties={
            "type": "shape",

            "shape_type": "rectangle",

            "width": 520,

            "height": 5,

            "color": "white",

            "opacity": 1.0,

            "visible": True
        }
    )


    origin = Component(
        "Origin",
        properties={
            "type": "shape",

            "shape_type": "circle",

            "size": 10,

            "color": "white",

            "opacity": 1.0,

            "visible": True
        }
    )


    plane = Component(
        "Plane",
        properties={
            "type": "text",

            "font_size": 18,

            "font_weight": "regular",

            "color": "white",

            "value": "✈",

            "visible": True,

            "opacity": 1.0
        }
    )


    hearts = Component(
        "Hearts",
        properties={
            "type": "container",

            "visible": True,

            "opacity": 1.0
        }
    )


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
    # HEARTS
    # ========================================================

    destination = Component(
        "Destination",
        properties={
            "type": "text",

            "font_size": 15,

            "font_weight": "regular",

            "color": "white",

            "align": "center",

            "visible": True,

            "opacity": 1.0
        }
    )


    arrival = Component(
        "Arrival",
        properties={
            "type": "text",

            "font_size": 15,

            "font_weight": "regular",

            "color": "white",

            "align": "center",

            "visible": True,

            "opacity": 1.0
        }
    )


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

            "font_size": 14,

            "font_weight": "regular",

            "color": "white",

            "align": "left",

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

    print("=" * 50)

    print(
        "       COUNTDOWN OS — COMPONENT SYSTEM"
    )

    print("=" * 50)


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


    plane = tree.find(
        "Plane"
    )

    print()

    print(
        f"Plane type: "
        f"{plane.get_property('type')}"
    )


    print()

    print(
        f"Plane font size: "
        f"{plane.get_property('font_size')}"
    )


    print()

    print(
        f"Plane visible: "
        f"{plane.get_property('visible')}"
    )


    print()

    print(
        f"Vertical gradient direction: "
        f"{tree.find('Vertical').get_property('direction')}"
    )


    print()

    print(
        f"Header type: "
        f"{tree.find('Header').get_property('type')}"
    )


    print()

    print(
        "🟢 Component visual properties initialized"
    )

    print()