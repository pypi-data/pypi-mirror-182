def check_hex(code: str):
    if not isinstance(code, (str, int)):
        return False

    if isinstance(code, str) and len(code) not in (6, 7):
        return False

    if isinstance(code, int):
        code = f"{hex(code)}"

    if code.startswith("#"):
        code = code.strip("#")
    if code.startswith("0x"):
        code = code.lstrip("0x")

    if len(code) != 6:
        return False

    try:
        int(code, 16)
    except ValueError as ex:
        return False

    return True


def extract_hex(code):
    if code.startswith("#"):
        code = code.strip("#")

    r = code[:2]
    g = code[2:4]
    b = code[4:]

    return int(r, 16), int(g, 16), int(b, 16)


def format_hex(code: str) -> str:
    if not check_hex(code):
        raise InvalidColorCodeException()

    if isinstance(code, int):
        code = f"#{hex(code).lstrip('0x')}"

    if not code.startswith("#"):
        code = "#" + code
    code = str(code).lower()
    return code


class Color:
    def __init__(self, color_code: str) -> None:
        self.hex = format_hex(color_code)
        self.r, self.g, self.b = extract_hex(self.hex)

    def get_r(self):
        return self.r

    def get_g(self):
        return self.g

    def get_b(self):
        return self.b

    def get_hex(self):
        return self.hex

    def __str__(self) -> str:
        return self.hex

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Color):
            return self.hex == __o.get_hex()
        try:
            c = Color(__o)
            return c.get_hex() == self.get_hex()
        except InvalidColorCodeException as ex:
            return False


class InvalidColorCodeException(Exception):
    pass
