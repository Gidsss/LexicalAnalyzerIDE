'''
All productions must have an __str__() method
'''

class PrefixExpression:
    prefix_tok = None
    op = None
    right = None
    def __str__(self):
        return f"{self.op} {self.right}"

class InfixExpression:
    left = None
    op = None
    right = None
    def __str__(self):
        return f"({self.left} {self.op} {self.right})"

class StringFmt:
    def __init__(self):
        self.start = None
        self.mid = []
        self.exprs = []
        self.end = None

    def __str__(self):
        result = f"\"{self.start.lexeme[1:-1]}"
        for m,e in zip(self.mid, self.exprs):
            result += f"| {e} |"
            result += f"{m.lexeme[1:-1]}"
        if self.exprs:
            result += f"| {self.exprs[-1]} |"
        result += f"{self.end.lexeme[1:-1]}\""
        return result

class ArrayLiteral:
    elements = []
    def __str__(self):
        result = "{"
        for e in self.elements:
            result += f"{e}, "
        return result[:-2] + "}"

class ArrayDeclaration:
    id = None
    dtype = None
    value = None
    size = None
    length = None
    is_const: bool = False

    def __str__(self, indent = 0):
        result =  f"declare: {self.id}\n"
        result += f"{' ' * (indent+4)}type: {self.dtype}\n"
        if self.value:
            result += f"{' ' * (indent+4)}value: {self.value}\n"
        if self.size:
            result += f"{' ' * (indent+4)}size: {self.size}\n"
        if self.length:
            result += f"{' ' * (indent+4)}length: {self.length}\n"
        if self.is_const:
            result += f"{' ' * (indent+4)}constant\n"
        return result

class Declaration:
    id = None
    dtype = None
    value = None
    is_const: bool = False

    def __str__(self, indent = 0):
        result =  f"declare: {self.id}\n"
        result += f"{' ' * (indent+4)}type: {self.dtype}\n"
        if self.value and self.value:
            result += f"{' ' * (indent+4)}value: {self.value}\n"
        if self.is_const:
            result += f"{' ' * (indent+4)}constant\n"
        return result

class Function:
    id = None
    rtype = None
    params: list = []
    body: list = []

class Class:
    id = None
    params: list = []
    body: list = []
    properties: list = []
    methods: list = []

class Program:
    'the root node of the syntax tree'
    globals: list = []
    functions: list = []
    classes: list = []

    def print(self):
        print("globals")
        for g in self.globals:
            print(g)
        print("functions")
        for fn in self.functions:
            print(fn)
        print("classes")
        for c in self.classes:
            print(c)
