# ============================================================
# COUNTDOWN OS — COMPONENT SYSTEM
# Version: 1.2 Elegance
# ============================================================

from component_schema import (
    validate_properties,
    ComponentSchemaError
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

        # ----------------------------------------------------
        # Validate initial properties
        # ----------------------------------------------------

        if self.properties:
            self.validate()


    # ========================================================
    # VALIDATION
    # ========================================================

    def validate(self):
        """
        Valida todas las properties actuales
        contra el Component Schema.
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

        La propiedad se valida inmediatamente
        contra el Component Schema.

        Si el nuevo estado completo del componente
        es inválido, la modificación no se conserva.
        """

        if not isinstance(key, str):
            raise TypeError(
                "Property key must be a string"
            )

        if not key.strip():
            raise ValueError(
                "Property key cannot be empty"
            )

        previous_value = (
            self.properties.get(
                key,
                None
            )
        )

        had_previous_value = (
            key in self.properties
        )

        self.properties[key] = value

        try:

            self.validate()

        except Exception:

            # ----------------------------------------------
            # Rollback
            # ----------------------------------------------

            if had_previous_value:

                self.properties[key] = (
                    previous_value
                )

            else:

                del self.properties[key]

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

        El componente se mantiene válido después
        de eliminar la propiedad.
        """

        if key not in self.properties:
            return False

        previous_value = (
            self.properties[key]
        )

        del self.properties[key]

        try:

            self.validate()

        except Exception:

            # ----------------------------------------------
            # Rollback
            # ----------------------------------------------

            self.properties[key] = (
                previous_value
            )

            raise

        return True


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

        self.validate()

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
    pertenecen al Component System.

    Las coordenadas pertenecen
    al Layout Engine.
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

    title = Component(
        "Title",
        properties={
            "type": "text"
        }
    )

    days = Component(
        "Days",
        properties={
            "type": "text"
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
            "type": "gradient"
        }
    )

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

    days_remaining = Component(
        "DaysRemaining",
        properties={
            "type": "text"
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

    content.add