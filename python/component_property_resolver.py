# ============================================================
# COUNTDOWN OS — COMPONENT PROPERTY RESOLVER
# Version: 1.2 Elegance
# ============================================================


# ============================================================
# COMPONENT PROPERTY RESOLVER
# ============================================================

class ComponentPropertyResolver:
    """
    Resuelve propiedades visuales de Countdown OS.

    Orden de resolución:

        1. Component property
        2. Legacy / layout_tokens fallback
        3. Explicit default
        4. None

    Este sistema permite migrar progresivamente
    desde layout_tokens.py hacia Component System
    sin romper la implementación existente.
    """

    # ========================================================
    # INITIALIZATION
    # ========================================================

    def __init__(
        self,
        component=None,
        fallback=None,
    ):

        self.component = component

        self.fallback = (
            fallback.copy()
            if fallback
            else {}
        )


    # ========================================================
    # COMPONENT
    # ========================================================

    def set_component(
        self,
        component,
    ):
        """
        Cambia el componente utilizado
        por el resolver.
        """

        self.component = component

        return component


    # ========================================================
    # FALLBACK
    # ========================================================

    def set_fallback(
        self,
        fallback,
    ):
        """
        Reemplaza los valores fallback.
        """

        if fallback is None:
            fallback = {}

        if not isinstance(
            fallback,
            dict
        ):
            raise TypeError(
                "fallback must be a dictionary"
            )

        self.fallback = fallback.copy()

        return self.fallback


    # ========================================================
    # HAS COMPONENT PROPERTY
    # ========================================================

    def has_component_property(
        self,
        key,
    ):
        """
        Comprueba si la propiedad existe
        directamente en el componente.
        """

        if self.component is None:
            return False

        return self.component.has_property(
            key
        )


    # ========================================================
    # HAS FALLBACK PROPERTY
    # ========================================================

    def has_fallback_property(
        self,
        key,
    ):
        """
        Comprueba si existe una propiedad
        en el fallback.
        """

        return key in self.fallback


    # ========================================================
    # RESOLVE
    # ========================================================

    def resolve(
        self,
        key,
        default=None,
    ):
        """
        Resuelve una propiedad.

        Prioridad:

            Component
                ↓
            Fallback
                ↓
            Default
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


        # ====================================================
        # COMPONENT
        # ====================================================

        if self.component is not None:

            if self.component.has_property(
                key
            ):

                return self.component.get_property(
                    key
                )


        # ====================================================
        # FALLBACK
        # ====================================================

        if key in self.fallback:

            return self.fallback[key]


        # ====================================================
        # DEFAULT
        # ====================================================

        return default


    # ========================================================
    # FONT SIZE
    # ========================================================

    def resolve_font_size(
        self,
        default=None,
    ):
        """
        Resuelve específicamente font_size.

        La prioridad continúa siendo:

            Component font_size
                ↓
            Resolver fallback
                ↓
            Default
        """

        return self.resolve(
            "font_size",
            default
        )


    # ========================================================
    # RESOLVE REQUIRED
    # ========================================================

    def resolve_required(
        self,
        key,
    ):
        """
        Resuelve una propiedad obligatoria.

        Si no existe ni en Component ni en fallback,
        lanza KeyError.
        """

        value = self.resolve(
            key,
            None
        )

        if value is None:

            raise KeyError(
                "Required component property "
                f"not found: {key}"
            )

        return value


    # ========================================================
    # RESOLVE MANY
    # ========================================================

    def resolve_many(
        self,
        properties,
    ):
        """
        Resuelve múltiples propiedades.

        properties puede ser:

            ["font_size", "color"]

        o:

            {
                "font_size": 18,
                "color": "white"
            }

        En el segundo caso, los valores funcionan
        como fallbacks.
        """

        if isinstance(
            properties,
            (list, tuple)
        ):

            result = {}

            for key in properties:

                result[key] = self.resolve(
                    key
                )

            return result


        if isinstance(
            properties,
            dict
        ):

            result = {}

            for key, fallback in properties.items():

                result[key] = self.resolve(
                    key,
                    fallback
                )

            return result


        raise TypeError(
            "properties must be a list, tuple, "
            "or dictionary"
        )


# ============================================================
# SIMPLE FUNCTION API
# ============================================================

def resolve_component_property(
    component,
    key,
    fallback=None,
):
    """
    API simple para resolver una propiedad.
    """

    resolver = ComponentPropertyResolver(
        component=component
    )

    return resolver.resolve(
        key,
        fallback
    )


# ============================================================
# FONT SIZE API
# ============================================================

def resolve_font_size(
    component,
    fallback=None,
):
    """
    API específica para font_size.

    Ejemplo:

        resolve_font_size(
            title_component,
            18
        )

    Resultado:

        Component font_size si existe.

        De lo contrario:

        fallback.
    """

    resolver = ComponentPropertyResolver(
        component=component
    )

    return resolver.resolve_font_size(
        fallback
    )


# ============================================================
# MULTIPLE PROPERTY API
# ============================================================

def resolve_component_properties(
    component,
    properties,
):
    """
    Resuelve múltiples propiedades de un componente.
    """

    resolver = ComponentPropertyResolver(
        component=component
    )

    return resolver.resolve_many(
        properties
    )


# ============================================================
# MANUAL TEST
# ============================================================

if __name__ == "__main__":

    from component import Component


    print()
    print("=" * 55)
    print("       COUNTDOWN OS — PROPERTY RESOLVER")
    print("=" * 55)


    # ========================================================
    # COMPONENT
    # ========================================================

    title = Component(
        "Title",
        properties={
            "type": "text",
            "font_size": 24
        }
    )


    # ========================================================
    # COMPONENT PRIORITY
    # ========================================================

    value = resolve_component_property(
        title,
        "font_size",
        18
    )

    print()
    print(
        f"Component property: {value}"
    )


    # ========================================================
    # FONT SIZE API
    # ========================================================

    font_size = resolve_font_size(
        title,
        18
    )

    print(
        f"Resolved font_size: {font_size}"
    )


    # ========================================================
    # FALLBACK
    # ========================================================

    fallback_value = resolve_component_property(
        title,
        "color",
        "white"
    )

    print(
        f"Fallback property: {fallback_value}"
    )


    # ========================================================
    # DEFAULT
    # ========================================================

    default_value = resolve_component_property(
        title,
        "opacity"
    )

    print(
        f"Missing property: {default_value}"
    )


    # ========================================================
    # MULTIPLE
    # ========================================================

    properties = resolve_component_properties(
        title,
        {
            "font_size": 18,
            "color": "white",
            "opacity": 1.0
        }
    )

    print()
    print("Resolved properties:")

    for key, value in properties.items():

        print(
            f"  {key}: {value}"
        )


    print()
    print(
        "🟢 Property Resolver font_size migration ready"
    )

    print()