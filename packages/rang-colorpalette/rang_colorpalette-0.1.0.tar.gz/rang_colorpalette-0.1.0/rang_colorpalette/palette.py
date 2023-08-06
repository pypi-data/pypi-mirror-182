from typing import Any

try:
    from rang_colorpalette import color
except ModuleNotFoundError:
    import color


class NamedPalette:
    def __init__(self, name: str, source=None) -> None:
        self.palette_name = name
        self.__named_palette = {}
        self.source = source

    def __getitem__(self, name: str) -> color.Color:
        name = name.upper()
        return self.__named_palette[name]

    def __setitem__(self, name: str, value: Any) -> None:
        name = name.upper()
        if not isinstance(value, color.Color):
            try:
                value = color.Color(value)
            except color.InvalidColorCodeException:
                raise TypeError(
                    f"The item {value} [{type(value)}] is not a color. Use Color()."
                )
        self.__named_palette[name] = value


class LinearPalette:
    def __init__(self, name: str, source=None) -> None:
        self.palette_name = name
        self.__list_palette = []
        self.colors = []
        self.source = source

    def __getitem__(self, index: int) -> color.Color:
        if not isinstance(index, int):
            raise TypeError(f"Expects int , got {type(index)}")
        return self.__list_palette[index]

    def add(self, value: Any) -> None:
        if not isinstance(value, color.Color):
            try:
                value = color.Color(value)
            except color.InvalidColorCodeException:
                raise TypeError(
                    f"The item {value} [{type(value)}] is not a color. Use Color()."
                )

        self.__list_palette.append(value)
