class String_UWU:
    def __init__(self, val: str):
        expect_type_is_in(val, self.stringable_types(),
                               msg=f"OwO... that ain't stringable!")
        self.val: str = val

    ## UTILS
    def stringable_types(self) -> list[type]:
        return [str, String_UWU, int, float, bool, Array_UWU]
    def valid_operands(self) -> list[type]:
        return [str, String_UWU]
class Array_UWU:
    def __init__(self, vals: list):
        self.val: list = vals
    ## UTILS
    def valid_array_elems(self) -> list[type]:
        return [str, String_UWU, int, float, bool, Array_UWU]
    def valid_operands(self) -> list[type]:
        return [list, Array_UWU]

class TypeError(Exception):
    pass
def expect_type_is_in(actual, expecteds: list[type], msg: str):
    for expected in expecteds:
        if not isinstance(actual, expected):
            raise TypeError(f"{msg}\nExpected any in {expecteds} !!\nGot {type(actual)} !!!")
    return True
