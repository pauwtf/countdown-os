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

    El Component System define la estructura
    y las propiedades visuales abstractas.

    NO conoce:

        - KWGT
        - coordenadas KWGT
        - Web Get
        - fórmulas KWGT
        - rendering
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
        """
        Valida las propiedades del componente
        utilizando Component Property Schema.
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

        if not isinstance(key, str):

            raise TypeError(
                "Property key must be a string"
            )

        if not key.strip():

            raise ValueError(
                "Property key cannot be empty"
            )

        updated_properties = (
            self.properties.copy()
        )

        updated_properties[key] = value

        validate_properties(
            updated_properties
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
        Comprueba si existe una propiedad.
        """

        return key in self.properties


    def remove_property(
        self,
        key,
    ):
        """
        Elimina una propiedad.

        No permite eliminar 'type',
        porque todos los componentes necesitan
        conservar su tipo.
        """

        if key == "type":

            raise ValueError(
                "Component type cannot be removed"
            )

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
        Busca recursivamente un componente.
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
        Convierte el árbol en diccionario.
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
    Construye el árbol visual de Countdown OS.

    Las propiedades visuales pertenecen al
    Component System.

    Las coordenadas pertenecen al Layout Engine.
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

    background_shape = Component(
        "BackgroundShape",
        properties={
            "type": "shape",
            "shape_type": "rectangle",
            "width": 400,
            "height": 200
        }
    )

    background.add_child(
        background_shape
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

    cover_image = Component(
        "CoverImage",
        properties={
            "type": "container"
        }
    )

    cover_text = Component(
        "CoverText",
        properties={
            "type": "text",
            "value": "♡",
            "font_size": 240
        }
    )

    cover_image.add_child(
        cover_text
    )

    cover.add_child(
        cover_image
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


    # --------------------------------------------------------
    # TITLE
    # --------------------------------------------------------

    title = Component(
        "Title",
        properties={
            "type": "text",
            "value": "UNTIL ALEX",
            "font_size": 18
        }
    )


    # --------------------------------------------------------
    # DAYS
    # --------------------------------------------------------

    days = Component(
        "Days",
        properties={
            "type": "text",
            "value": "days",
            "font_size": 15
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


    vertical = Component(
        "Vertical",
        properties={
            "type": "gradient",
            "direction": "vertical"
        }
    )


    horizontal = Component(
        "Horizontal",
        properties={
            "type": "gradient",
            "direction": "horizontal"
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


    days_remaining = Component(
        "DaysRemaining",
        properties={
            "type": "text",
            "value": "44",
            "font_size": 100
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
    # JOURNEY
    # ========================================================

    line = Component(
        "Line",
        properties={
            "type": "shape",
            "shape_type": "rectangle",
            "width": 258,
            "height": 1
        }
    )


    origin = Component(
        "Origin",
        properties={
            "type": "shape",
            "shape_type": "circle",
            "size": 5
        }
    )


    plane = Component(
        "Plane",
        properties={
            "type": "text",
            "value": "✈",
            "font_size": 30
        }
    )


    hearts = Component(
        "Hearts",
        properties={
            "type": "container"
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
            "value": "",
            "font_size": 14
        }
    )


    arrival = Component(
        "Arrival",
        properties={
            "type": "text",
            "value": "",
            "font_size": 14
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
            "value": "",
            "font_size": 10
        }
    )


    countdown.add_child(
        footer
    )


    # ========================================================
    # VALIDATE COMPLETE TREE
    # ========================================================

    def validate_tree(component):

        component.validate()

        for child in component.children:

            validate_tree(
                child
            )


    validate_tree(
        countdown
    )


    # ========================================================
    # RETURN
    # ========================================================

    return countdown


# ============================================================
# TREE SERIALIZATION
# ============================================================

def build_component_tree():
    """
    Construye el árbol y devuelve
    su representación serializable.
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
    print(
        "       COUNTDOWN OS — COMPONENT SYSTEM"
    )
    print("=" * 60)

    print()

    print(
        f"Root: {tree.name}"
    )

    print()

    print("Root properties:")

    print(
        tree.properties
    )

    print()

    print("Components:")

    for child in tree.children:

        print(
            f"  └── {child.name}"
        )

    print()

    plane = tree.find(
        "Plane"
    )

    print(
        f"Plane type: "
        f"{plane.get_property('type')}"
    )

    print(
        f"Plane value: "
        f"{plane.get_property('value')}"
    )

    print(
        f"Plane font size: "
        f"{plane.get_property('font_size')}"
    )

    print()

    title = tree.find(
        "Title"
    )

    print(
        f"Title font size: "
        f"{title.get_property('font_size')}"
    )

    print()

    line = tree.find(
        "Line"
    )

    print(
        f"Line width: "
        f"{line.get_property('width')}"
    )

    print(
        f"Line height: "
        f"{line.get_property('height')}"
    )

    print()

    print(
        "🟢 Component properties configured"
    )

    print()