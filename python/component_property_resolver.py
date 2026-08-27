# ============================================================
# COUNTDOWN OS — COMPONENT PROPERTY RESOLVER
# Version: 1.2 Elegance
# ============================================================


class ComponentPropertyResolver:
    """
    Resuelve propiedades visuales de Countdown OS.

    Prioridad:

        1. Component property
        2. Fallback / legacy value
        3. Explicit default
        4. None

    Opacity usa internamente la escala 0.0–1.0.

    Conversión desde KWGT:

        100% → 1.00
         86% → 0.86
         60% → 0.60
         30% → 0.30
          5% → 0.05
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
    # PROPERTY CHECKS
    # ========================================================

    def has_component_property(
        self,
        key,
    ):
        """
        Comprueba si existe una propiedad
        directamente en el componente.
        """

        if self.component is None:
            return False

        return self.component.has_property(
            key
        )


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

        Lista / tupla:

            ["font_size", "color"]

        Diccionario:

            {
                "font_size": 18,
                "color": "#FFFFFF"
            }

        Los valores del diccionario funcionan
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


    # ========================================================
    # VISUAL PROPERTY HELPERS
    # ========================================================

    def resolve_font_size(
        self,
        default=None,
    ):

        return self.resolve(
            "font_size",
            default
        )


    def resolve_color(
        self,
        default=None,
    ):

        return self.resolve(
            "color",
            default
        )


    def resolve_opacity(
        self,
        default=None,
    ):
        """
        Resuelve opacity en escala 0.0–1.0.

        También acepta temporalmente porcentajes
        0–100 para facilitar la migración de valores
        directamente medidos en KWGT.

        Ejemplos:

            100 → 1.00
             86 → 0.86
             60 → 0.60
             30 → 0.30
              5 → 0.05
        """

        value = self.resolve(
            "opacity",
            default
        )

        if value is None:
            return None


        try:

            value = float(
                value
            )

        except (
            TypeError,
            ValueError
        ) as error:

            raise TypeError(
                f"Opacity must be numeric: {value}"
            ) from error


        # ====================================================
        # KWGT PERCENTAGE → INTERNAL NORMALIZED VALUE
        # ====================================================

        if (
            value > 1.0
            and value <= 100.0
        ):

            value /= 100.0


        if (
            value < 0.0
            or value > 1.0
        ):

            raise ValueError(
                "Opacity must be between "
                "0.0 and 1.0, or a percentage "
                f"from 0 to 100: {value}"
            )


        return value


    def resolve_visibility(
        self,
        default=None,
    ):

        return self.resolve(
            "visible",
            default
        )


    def resolve_alignment(
        self,
        default=None,
    ):

        return self.resolve(
            "align",
            default
        )


    def resolve_font_weight(
        self,
        default=None,
    ):

        return self.resolve(
            "font_weight",
            default
        )


    def resolve_font_family(
        self,
        default=None,
    ):

        return self.resolve(
            "font_family",
            default
        )


    def resolve_font_style(
        self,
        default=None,
    ):

        return self.resolve(
            "font_style",
            default
        )


    def resolve_shape_type(
        self,
        default=None,
    ):

        return self.resolve(
            "shape_type",
            default
        )


    def resolve_width(
        self,
        default=None,
    ):

        return self.resolve(
            "width",
            default
        )


    def resolve_height(
        self,
        default=None,
    ):

        return self.resolve(
            "height",
            default
        )


    def resolve_size(
        self,
        default=None,
    ):

        return self.resolve(
            "size",
            default
        )


    def resolve_radius(
        self,
        default=None,
    ):

        return self.resolve(
            "radius",
            default
        )


    def resolve_direction(
        self,
        default=None,
    ):

        return self.resolve(
            "direction",
            default
        )


    def resolve_color_start(
        self,
        default=None,
    ):

        return self.resolve(
            "color_start",
            default
        )


    def resolve_color_end(
        self,
        default=None,
    ):

        return self.resolve(
            "color_end",
            default
        )


# ============================================================
# SIMPLE PROPERTY API
# ============================================================

def resolve_component_property(
    component,
    key,
    fallback=None,
):
    """
    Resuelve una propiedad individual.
    """

    resolver = ComponentPropertyResolver(
        component=component
    )

    return resolver.resolve(
        key,
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
    Resuelve múltiples propiedades.
    """

    resolver = ComponentPropertyResolver(
        component=component
    )

    return resolver.resolve_many(
        properties
    )


# ============================================================
# OPACITY API
# ============================================================

def resolve_component_opacity(
    component,
    fallback=None,
):
    """
    Resuelve opacity usando la escala
    interna 0.0–1.0.
    """

    resolver = ComponentPropertyResolver(
        component=component
    )

    return resolver.resolve_opacity(
        fallback
    )


# ============================================================
# MANUAL TEST
# ============================================================

if __name__ == "__main__":

    from component import Component


    print()
    print("=" * 60)
    print("       COUNTDOWN OS — PROPERTY RESOLVER")
    print("=" * 60)


    # ========================================================
    # COMPONENT
    # ========================================================

    title = Component(
        "Title",
        properties={
            "type": "text",
            "font_size": 18,
            "color": "#FFFFFF",
            "opacity": 0.86,
            "visible": True,
            "align": "left"
        }
    )


    resolver = ComponentPropertyResolver(
        component=title
    )


    # ========================================================
    # VISUAL PROPERTIES
    # ========================================================

    print()

    print(
        f"Font size: "
        f"{resolver.resolve_font_size()}"
    )

    print(
        f"Color: "
        f"{resolver.resolve_color()}"
    )

    print(
        f"Opacity: "
        f"{resolver.resolve_opacity()}"
    )

    print(
        f"Visible: "
        f"{resolver.resolve_visibility()}"
    )

    print(
        f"Align: "
        f"{resolver.resolve_alignment()}"
    )

    print(
        f"Font weight: "
        f"{resolver.resolve_font_weight()}"
    )


    # ========================================================
    # OPACITY NORMALIZATION
    # ========================================================

    print()
    print(
        "KWGT opacity normalization:"
    )


    for percentage in [
        100,
        86,
        60,
        30,
        5
    ]:

        resolver = ComponentPropertyResolver(
            fallback={
                "opacity": percentage
            }
        )

        normalized = resolver.resolve_opacity()

        print(
            f"  {percentage}% → "
            f"{normalized:.2f}"
        )


    print()
    print(
        "🟢 Property Resolver ready"
    )

    print()