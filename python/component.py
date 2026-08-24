# ============================================================
# COUNTDOWN OS — COMPONENT SYSTEM
# Version: 1.2 Elegance
# ============================================================


# ============================================================
# COMPONENT
# ============================================================

class Component:
    """
    Componente base del sistema visual de Countdown OS.

    Cada componente puede tener:
        - nombre
        - propiedades
        - hijos

    Esto permite construir una jerarquía visual
    independiente del sistema de coordenadas.
    """

    def __init__(
        self,
        name,
        properties=None,
    ):
        self.name = name
        self.properties = properties or {}
        self.children = []

    # ========================================================
    # CHILDREN
    # ========================================================

    def add_child(self, component):
        """
        Añade un componente hijo.
        """

        if not isinstance(component, Component):
            raise TypeError(
                "component must be an instance of Component"
            )

        self.children.append(component)

        return component

    # ========================================================
    # FIND
    # ========================================================

    def find(self, name):
        """
        Busca recursivamente un componente por nombre.
        """

        if self.name == name:
            return self

        for child in self.children:

            result = child.find(name)

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
        """

        result = {}

        result.update(self.properties)

        for child in self.children:

            result[child.name] = child.to_dict()

        return result


# ============================================================
# COUNTDOWN OS COMPONENT TREE
# ============================================================

def build_countdown_tree():
    """
    Construye la jerarquía visual base de Countdown OS.

    El árbol representa la estructura visual,
    no las coordenadas ni la lógica de KWGT.
    """

    # ========================================================
    # ROOT
    # ========================================================

    countdown = Component(
        "Countdown"
    )

    # ========================================================
    # BACKGROUND
    # ========================================================

    background = Component(
        "Background"
    )

    countdown.add_child(
        background
    )

    # ========================================================
    # COVER
    # ========================================================

    cover = Component(
        "Cover"
    )

    countdown.add_child(
        cover
    )

    # ========================================================
    # HEADER
    # ========================================================

    header = Component(
        "Header"
    )

    title = Component(
        "Title"
    )

    days = Component(
        "Days"
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
        "Gradient"
    )

    vertical = Component(
        "Vertical"
    )

    horizontal = Component(
        "Horizontal"
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
        "Counter"
    )

    days_remaining = Component(
        "DaysRemaining"
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
        "Content"
    )

    journey = Component(
        "Journey"
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
        "Line"
    )

    origin = Component(
        "Origin"
    )

    plane = Component(
        "Plane"
    )

    hearts = Component(
        "Hearts"
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
        "Destination"
    )

    arrival = Component(
        "Arrival"
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
        "Footer"
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
    print("       COUNTDOWN OS — COMPONENT SYSTEM")
    print("=" * 50)

    print()
    print(f"Root: {tree.name}")

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
    print("🟢 Component tree generated")
    print()