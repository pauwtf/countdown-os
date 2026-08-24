# ============================================================
# COUNTDOWN OS — COMPONENT SYSTEM
# Version: 1.2 Elegance
# ============================================================


# ============================================================
# COMPONENT
# ============================================================

class Component:
    """
    Componente base del Component System v1.2.

    Cada componente puede tener:

        - id
        - type
        - position
        - size
        - properties
        - children

    El sistema de componentes es independiente de KWGT.
    """

    def __init__(
        self,
        component_id,
        component_type="component",
        position=None,
        size=None,
        properties=None,
        children=None,
    ):

        self.id = component_id

        self.type = component_type

        self.position = (
            position.copy()
            if position is not None
            else {
                "x": 0,
                "y": 0,
            }
        )

        self.size = (
            size.copy()
            if size is not None
            else {}
        )

        self.properties = (
            properties.copy()
            if properties is not None
            else {}
        )

        self.children = (
            list(children)
            if children is not None
            else []
        )


    # ========================================================
    # CHILDREN
    # ========================================================

    def add_child(self, child):
        """
        Añade un componente hijo.
        """

        if not isinstance(child, Component):
            raise TypeError(
                "child must be an instance of Component"
            )

        self.children.append(child)

        return child


    def remove_child(self, child):
        """
        Elimina un componente hijo.
        """

        if child in self.children:
            self.children.remove(child)

        return child


    # ========================================================
    # POSITION
    # ========================================================

    def set_position(self, x, y):
        """
        Define la posición local del componente.
        """

        self.position = {
            "x": x,
            "y": y,
        }

        return self


    # ========================================================
    # SIZE
    # ========================================================

    def set_size(self, width, height):
        """
        Define las dimensiones del componente.
        """

        self.size = {
            "width": width,
            "height": height,
        }

        return self


    # ========================================================
    # PROPERTIES
    # ========================================================

    def set_property(self, key, value):
        """
        Define una propiedad visual o funcional.
        """

        self.properties[key] = value

        return self


    def get_property(self, key, default=None):
        """
        Obtiene una propiedad del componente.
        """

        return self.properties.get(
            key,
            default
        )


    # ========================================================
    # SERIALIZATION
    # ========================================================

    def to_dict(self):
        """
        Convierte el componente en un diccionario.

        La estructura resultante es independiente
        del sistema de coordenadas de KWGT.
        """

        component = {
            "id": self.id,
            "type": self.type,
            "position": {
                "x": self.position.get("x", 0),
                "y": self.position.get("y", 0),
            },
        }


        # ----------------------------------------------------
        # SIZE
        # ----------------------------------------------------

        if self.size:
            component["size"] = self.size.copy()


        # ----------------------------------------------------
        # PROPERTIES
        # ----------------------------------------------------

        if self.properties:
            component["properties"] = (
                self.properties.copy()
            )


        # ----------------------------------------------------
        # CHILDREN
        # ----------------------------------------------------

        if self.children:

            component["children"] = [
                child.to_dict()
                for child in self.children
            ]


        return component


    # ========================================================
    # REPRESENTATION
    # ========================================================

    def __repr__(self):

        return (
            f"Component("
            f"id={self.id!r}, "
            f"type={self.type!r}, "
            f"children={len(self.children)}"
            f")"
        )