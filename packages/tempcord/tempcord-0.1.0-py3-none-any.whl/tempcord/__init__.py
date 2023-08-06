from __future__ import annotations
import typing as t

from dataclasses import dataclass
from enum import Enum, auto

T = t.TypeVar("T")


class TokenType(Enum):
    # data types
    INTEGER = auto()
    BOOLEAN = auto()
    STRING = auto()

    # syntax
    KEYWORD = auto()
    BLOCKSTART = auto()
    BLOCKEND = auto()

    def __repr__(self) -> str:

        return self.name


@dataclass
class Token:
    type: TokenType
    value: t.Any | None


def char(inp: str):

    return ord(inp)


def between(first: int, num: int, last: int):

    return first <= num and num <= last


def uppercaseletter(code: int):
    return between(char("A"), code, char("Z"))


def lowercaseletter(code: int):
    return between(char("a"), code, char("z"))


def letter(code: int):

    return lowercaseletter(code) or uppercaseletter(code)


def digit(code: int):

    return between(char("0"), code, char("9"))


def hexdigit(code: int):

    return (
        digit(code)
        or between(char("A"), code, char("F"))
        or between(char("a"), code, char("f"))
    )


def preprocess(inp: str) -> t.List[int]:
    codepoints: t.List[int] = []

    for value in inp:

        codepoints.append(char(value))

    return codepoints


def tokenize(codepoints: t.List[int]) -> t.List[Token]:

    tokens = []

    codepoint_stream = iter(codepoints)
    curr = next(codepoint_stream)

    end = False

    while not end:

        try:

            if letter(curr):  # keyword start char
                keyword_context = ""

                while not end:

                    if letter(curr):

                        keyword_context += chr(curr)

                        curr = next(codepoint_stream)

                    else:

                        if keyword_context.lower() == "yes":
                            tokens.append(Token(TokenType.BOOLEAN, True))

                        elif keyword_context.lower() == "no":
                            tokens.append(Token(TokenType.BOOLEAN, False))

                        else:
                            tokens.append(Token(TokenType.KEYWORD, keyword_context))

                        keyword_context = ""

                        break

            elif digit(curr):  # number start char

                digit_context = ""

                while not end:

                    if digit(curr):

                        digit_context += chr(curr)

                        curr = next(codepoint_stream)

                    else:
                        tokens.append(Token(TokenType.INTEGER, int(digit_context)))
                        digit_context = ""
                        break

            elif curr == char("#"):  # hex digit starter
                hexdigit_context = ""

                curr = next(codepoint_stream)

                while not end:

                    if hexdigit(curr):
                        hexdigit_context += chr(curr)

                        curr = next(codepoint_stream)

                    else:

                        tokens.append(
                            Token(TokenType.INTEGER, int(hexdigit_context, 16))
                        )
                        hexdigit_context = ""

                        break

            elif curr == char('"'):  # string start char

                str_context = ""

                curr = next(codepoint_stream)

                while not end:

                    if curr != char('"'):

                        if curr == char("\\"):  # escape string
                            curr = next(codepoint_stream)
                            str_context += chr(curr)

                            curr = next(codepoint_stream)

                        else:
                            str_context += chr(curr)
                            curr = next(codepoint_stream)

                    elif curr == char('"'):

                        tokens.append(Token(TokenType.STRING, str_context))

                        str_context = ""

                        break

            elif curr == char("{"):  # block start

                tokens.append(Token(TokenType.BLOCKSTART, None))

                curr = next(codepoint_stream)

            elif curr == char("}"):  # block end

                tokens.append(Token(TokenType.BLOCKEND, None))

                curr = next(codepoint_stream)

            curr = next(codepoint_stream)

        except StopIteration:

            end = True

    return tokens


object_nodes = [
    "footer",
    "field",
    "image",
    "provider",
    "author",
    "thumbnail",
    "video",
    "message",
    "embed",
]

list_nodes = [
    "embeds",
    "messages",
    "fields",
]

value_nodes = [
    "content",
    "title",
    "description",
    "url",
    "timestamp",
    "color",
    "name",
    "value",
    "inline",
    "text",
    "icon",
    "height",
    "width",
]


@dataclass
class ValueNode:
    keyword: str
    value: t.Any

    def eval(self):

        return self.value


@dataclass
class DeclarationNode:
    value: t.List[ObjectNode | ValueNode | ListNode]

    def eval(self):

        data = []

        for el in self.value:

            data.append(el.eval())

        return data


@dataclass
class ObjectNode:
    keyword: str
    value: DeclarationNode

    def eval(self):

        data = {}

        declare_node = self.value

        for el in declare_node.value:

            data[el.keyword] = el.eval()

        return data


@dataclass
class ListNode:
    keyword: str
    value: DeclarationNode

    def eval(self):

        data = []

        declare_node = self.value

        for el in declare_node.value:

            data.append(el.eval())

        return data


class Parser:
    def __init__(self, stream: t.Iterator[Token]) -> None:
        self.tokens = stream
        self.curr: t.Optional[Token] = None

        self.advance()

    def advance(self):
        try:

            self.curr = next(self.tokens)

        except StopIteration:
            self.curr = None

    def parse(self):

        res = self.create_node()

        if self.curr:
            raise Exception(f"unknown token {self.curr}")

        return res

    def create_node(self):

        result = None

        while self.curr != None:

            # starter token

            if self.curr.type == TokenType.KEYWORD and self.curr.value in list_nodes:

                result = self.create_list_node()

            elif (
                self.curr.type == TokenType.KEYWORD and self.curr.value in object_nodes
            ):

                result = self.create_object_node()

            elif self.curr.type == TokenType.KEYWORD and self.curr.value in value_nodes:
                result = self.create_value_node()

            elif self.curr.type == TokenType.BLOCKSTART:

                result = self.create_declare_node()

            self.advance()

        return result

    def create_list_node(self):

        keyword = self.curr.value
        self.advance()
        return ListNode(keyword, self.create_declare_node())

    def create_object_node(self):

        keyword = self.curr.value
        self.advance()
        return ObjectNode(keyword, self.create_declare_node())

    def create_value_node(self):
        keyword = self.curr.value
        self.advance()
        value = self.curr.value
        return ValueNode(keyword, value)

    def create_declare_node(self):

        data = []

        if self.curr.type == TokenType.BLOCKSTART:

            while self.curr.type != TokenType.BLOCKEND:

                if (
                    self.curr.type == TokenType.KEYWORD
                    and self.curr.value in list_nodes
                ):

                    data.append(self.create_list_node())

                elif (
                    self.curr.type == TokenType.KEYWORD
                    and self.curr.value in object_nodes
                ):

                    data.append(self.create_object_node())

                elif (
                    self.curr.type == TokenType.KEYWORD
                    and self.curr.value in value_nodes
                ):

                    data.append(self.create_value_node())

                self.advance()

            return DeclarationNode(value=data)


def parse(tokens: t.List[Token]):

    stream = iter(tokens)

    return Parser(stream).parse()


def compile(inp: str):

    codepoints = preprocess(inp)
    tokens = tokenize(codepoints)
    ast = parse(tokens)

    return ast.eval()
