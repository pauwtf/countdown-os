# ============================================================
# COUNTDOWN OS — COMPONENT SYSTEM
# Version: 1.2 Elegance
# ============================================================


# ============================================================
# IMPORTS
# ============================================================

from layout_tokens import (
    HEADER,
    COUNTER,
    JOURNEY,
    FOOTER,
)


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

    Las properties representan características visuales
    abstractas del componente.

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
        """
        Valida las propiedades del componente
        utilizando el Component Property Schema.
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

        La propiedad se valida después
        de ser modificada.
        """

        if not isinstance(key, str):
            raise TypeError(
                "Property key must be a string"
            )

        if not key.strip():
            raise ValueError(
                "Property key cannot be empty"
            )

        previous_value = self.properties.get(
            key
        )

        self.properties[key] = value

        try:

            self.validate()

        except Exception:

            if previous_value is None:
                self.properties.pop(
                    key,
                    None
                )

            else:
                self.properties[key] = (
                    previous_value
                )

            raise

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

            previous_value = (
                self.properties[key]
            )

            del self.properties[key]

            try:

                self.validate()

            except Exception:

                self.properties[key] = (
                    previous_value
                )

                raise

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
    Construye la jerarquía visual base
    de Countdown OS.

    Las propiedades visuales abstractas
    pertenecen ahora a los componentes.

    Las coordenadas continúan perteneciendo
    al Layout Engine.

    FONT SIZE MIGRATION
    -------------------

    Los componentes de tipo text contienen
    ahora su propio font_size.

    layout_tokens.py continúa siendo utilizado
    únicamente como fuente de valores iniciales
    mientras termina la migración.
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

            "font_size": (
                HEADER[
                    "title"
                ][
                    "font_size"
                ]
            )
        }
    )


    # --------------------------------------------------------
    # DAYS
    # --------------------------------------------------------

    days = Component(
        "Days",
        properties={
            "type": "text",

            "font_size": (
                HEADER[
                    "days"
                ][
                    "font_size"
                ]
            ),

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


    # --------------------------------------------------------
    # VERTICAL
    # --------------------------------------------------------

    vertical = Component(
        "Vertical",
        properties={
            "type": "gradient"
        }
    )


    # --------------------------------------------------------
    # HORIZONTAL
    # --------------------------------------------------------

    horizontal = Component(
        "Horizontal",
        properties={
            "type": "gradient"
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


    # --------------------------------------------------------
    # DAYS REMAINING
    # --------------------------------------------------------

    days_remaining = Component(
        "DaysRemaining",
        properties={
            "type": "text",

            "font_size": (
                COUNTER[
                    "days_remaining"
                ][
                    "font_size"
                ]
            )
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

    # --------------------------------------------------------
    # LINE
    # --------------------------------------------------------

    line = Component(
        "Line",
        properties={
            "type": "shape"
        }
    )


    # --------------------------------------------------------
    # ORIGIN
    # --------------------------------------------------------

    origin = Component(
        "Origin",
        properties={
            "type": "shape"
        }
    )


    # --------------------------------------------------------
    # PLANE
    # --------------------------------------------------------

    plane = Component(
        "Plane",
        properties={
            "type": "text",

            "font_size": (
                JOURNEY[
                    "plane"
                ][
                    "font_size"
                ]
            ),

            "value": "✈"
        }
    )


    # --------------------------------------------------------
    # HEARTS
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # DESTINATION
    # --------------------------------------------------------

    destination = Component(
        "Destination",
        properties={
            "type": "text",

            "font_size": (
                JOURNEY[
                    "hearts"
                ][
                    "destination"
                ][
                    "font_size"
                ]
            )
        }
    )


    # --------------------------------------------------------
    # ARRIVAL
    # --------------------------------------------------------

    arrival = Component(
        "Arrival",
        properties={
            "type": "text",

            "font_size": (
                JOURNEY[
                    "hearts"
                ][
                    "arrival"
                ][
                    "font_size"
                ]
            )
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

            "font_size": (
                FOOTER[
                    "font_size"
                ]
            )
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
    print("       COUNTDOWN OS — COMPONENT SYSTEM")
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

    plane_component = tree.find(
        "Plane"
    )

    title_component = tree.find(
        "Title"
    )

    days_remaining_component = tree.find(
        "DaysRemaining"
    )

    footer_component = tree.find(
        "Footer"
    )

    print(
        f"Found Plane: "
        f"{plane_component is not None}"
    )

    print(
        f"Plane type: "
        f"{plane_component.get_property('type')}"
    )

    print(
        f"Plane font_size: "
        f"{plane_component.get_property('font_size')}"
    )

    print()

    print(
        f"Title font_size: "
        f"{title_component.get_property('font_size')}"
    )

    print(
        f"DaysRemaining font_size: "
        f"{days_remaining_component.get_property('font_size')}"
    )

    print(
        f"Footer font_size: "
        f"{footer_component.get_property('font_size')}"
    )

    print()

    print(
        "🟢 Component font_size properties initialized"
    )

    print()