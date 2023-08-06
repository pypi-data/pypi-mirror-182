from __future__ import annotations

import typing as t

from dataclasses import dataclass
from enum import Enum, auto


from .consts import OBJECT_KEYWORDS, LIST_KEYWORDS, VALUE_KEYWORDS

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
class Token(t.Generic[T]):
    type: TokenType
    value: T


@dataclass
class ValueNode:
    keyword: str
    value: t.Any


@dataclass
class DeclarationNode:
    value: t.List[ObjectNode | ValueNode | ListNode]


@dataclass
class ObjectNode:
    keyword: str
    value: DeclarationNode


@dataclass
class ListNode:
    keyword: str
    value: DeclarationNode


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

    tokens: t.List[Token[t.Any]] = []

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

                    elif curr == char("_"):

                        keyword_context += chr(curr)

                        curr = next(codepoint_stream)

                    else:

                        if keyword_context.lower() == "yes":
                            tokens.append(Token(TokenType.BOOLEAN, True))

                        elif keyword_context.lower() == "no":
                            tokens.append(Token(TokenType.BOOLEAN, False))

                        else:
                            tokens.append(
                                Token(TokenType.KEYWORD, keyword_context)
                            )

                        keyword_context = ""

                        break

            elif digit(curr):  # number start char

                digit_context = ""

                while not end:

                    if digit(curr):

                        digit_context += chr(curr)

                        curr = next(codepoint_stream)

                    else:
                        tokens.append(
                            Token(TokenType.INTEGER, int(digit_context))
                        )
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


def parse_list_node(curr: Token[str], stream: t.Iterator[Token]):
    return ListNode(curr.value, parse_declare_node(next(stream), stream))


def parse_object_node(curr: Token[str], stream: t.Iterator[Token]):
    return ObjectNode(curr.value, parse_declare_node(next(stream), stream))


def parse_value_node(curr: Token, stream: t.Iterator[Token]):
    kw = curr.value
    curr = next(stream)
    val = curr.value
    return ValueNode(kw, val)


def parse_declare_node(curr: Token, stream: t.Iterator[Token]):

    if curr.type == TokenType.BLOCKSTART:

        data: t.List[ObjectNode | ListNode | ValueNode] = []

        while curr.type != TokenType.BLOCKEND:

            if curr.type == TokenType.KEYWORD and curr.value in LIST_KEYWORDS:

                data.append(parse_list_node(curr, stream))

            elif (
                curr.type == TokenType.KEYWORD
                and curr.value in OBJECT_KEYWORDS
            ):

                data.append(parse_object_node(curr, stream))

            elif (
                curr.type == TokenType.KEYWORD and curr.value in VALUE_KEYWORDS
            ):

                data.append(parse_value_node(curr, stream))

            curr = next(stream)

        return DeclarationNode(data)


def parse_node(curr: Token, stream: t.Iterator[Token]):

    result: t.Optional[ListNode | ObjectNode | ValueNode] = None

    end = False

    while not end:

        try:

            if curr.type == TokenType.KEYWORD and curr.value in LIST_KEYWORDS:

                result = parse_list_node(curr, stream)

            elif (
                curr.type == TokenType.KEYWORD
                and curr.value in OBJECT_KEYWORDS
            ):

                result = parse_object_node(curr, stream)

            elif (
                curr.type == TokenType.KEYWORD and curr.value in VALUE_KEYWORDS
            ):

                result = parse_value_node(curr, stream)

            elif curr.type == TokenType.BLOCKSTART:

                result = parse_declare_node(curr, stream)

            curr = next(stream)

        except StopIteration:

            end = True

    return result


def parse(tokens: t.List[Token]):

    stream = iter(tokens)

    curr = next(stream)

    return parse_node(curr, stream)


def evaluate(ast: ObjectNode | ListNode | ValueNode):

    if isinstance(ast, ObjectNode):

        object_data = {}
        declarations = ast.value

        for declaration in declarations.value:

            object_data[declaration.keyword] = evaluate(declaration)

        return object_data

    elif isinstance(ast, ListNode):

        list_data = []

        declarations = ast.value

        for declaration in declarations.value:

            list_data.append(evaluate(declaration))

        return list_data

    elif isinstance(ast, ValueNode):

        return ast.value


def compile(inp: str):

    codepoints = preprocess(inp)
    tokens = tokenize(codepoints)
    ast = parse(tokens)
    result = evaluate(ast)

    return result
