from typing import Union, TypeAlias, Any, Callable, Iterator

import math


def split_out_br(inst: str) -> str: return '\\n'.join(inst.split('\n'))


def split_out_quotes(inst: str) -> str: return '\\"'.join(inst.split('"'))


class Entry(object):
    prev: Union["Entry", None] = None
    value: Any = None
    next: Union["Entry", None] = None

    def __init__(self, value: Any): self.value = value

    def __str__(self) -> str: return self.value.__str__()

    def __repr__(self) -> str: return self.value.__repr__()

    def __class_getitem__(cls, *args, **kwargs): pass


class Lst(object):
    _content: list[Entry] = None

    def __init__(self, in_list: list | None = None):
        self._content = list()
        if not (in_list is None):
            for val in in_list: self.append(val)

    def __len__(self) -> int: return len(self._content)

    def append(self, value: Any) -> Entry:
        if isinstance(value, Entry):
            entry: Entry = value
            entry.prev, entry.next = None, None
        else: entry: Entry = Entry(value = value)

        if len(self) > 0:
            former_last: Entry = self._content[-1]
            entry.prev = former_last
            former_last.next = entry
        self._content.append(entry)

        return entry

    def insert(self, idx: int, value: Any) -> Entry:
        if idx < 0: idx += len(self)
        if idx < 0: raise IndexError('placeholder')
        if idx > len(self): raise IndexError('placeholder')
        if isinstance(value, Entry):
            entry: Entry = value
            entry.prev, entry.next = None, None
        else: entry: Entry = Entry(value = value)

        if idx > 0:
            prev: Entry = self._content[idx - 1]
            prev.next = entry
            entry.prev = prev
        if idx < len(self):
            nextt: Entry = self._content[idx]
            nextt.prev = entry
            entry.next = nextt
        self._content.insert(idx, entry)

        return entry

    def index(self, value: Any) -> int:
        if len(self) == 0: raise ValueError(f"{value} not in list")
        entry = self._content[0]
        while True:
            if entry.value == value: break
            if entry.next is None: raise ValueError(f"{value} not in list")
            entry = entry.next
        return self._content.index(entry)

    def remove(self, entry: Entry) -> "Lst":
        entry_idx = self._content.index(entry)
        if not (entry.prev is None): entry.prev.next = entry.next
        if not (entry.next is None): entry.next.prev = entry.prev

        _tmp_content = self._content
        self._content = self._content[:entry_idx]
        self._content.extend(_tmp_content[entry_idx + 1:])

        return self

    def substitute(self, start: Entry, stop: Entry, new_contents: list[Any]) -> "Lst":
        start_idx: int = self._content.index(start)
        stop_idx: int = self._content.index(stop)
        new_start: Entry = Entry(value = new_contents[0])
        if len(new_contents) == 0: raise AssertionError('placeholder')
        elif len(new_contents) > 1: new_stop: Entry = Entry(value = new_contents[-1])
        else: new_stop: Entry = new_start

        new_start.prev = start.prev
        if not (start.prev is None):
            start.prev.next = new_start
        new_stop.next = stop.next
        if not (stop.next is None):
            stop.next.prev = new_stop

        _tmp_content = self._content
        self._content = self._content[:start_idx]
        self._content.append(new_start)
        if not (new_start is new_stop):
            for new_val in new_contents[1:-1]: self.append(new_val)
            self.append(new_stop)
        self._content.extend(_tmp_content[stop_idx + 1:])

        return self

    def __getitem__(self, item: int): return self._content[item]

    def __class_getitem__(cls, *args, **kwargs): pass

    def __setitem__(self, item: int, value: Any):
        if isinstance(value, Entry): raise TypeError('palceholder')
        self._content[item].value = value

    def __str__(self) -> str: return str([entry.value for entry in self._content])

    def __repr__(self) -> str: return repr([entry.value for entry in self._content])


space_char: str = ' '
linebreak_char: str = '\n'
comment_char: str = '#'
#
define_alias_char: str = '&'
reference_alias_char: str = '*'
#
double_colon_char: str = ':'
bracket_left_char: str = '['
bracket_right_char: str = ']'
curly_left_char: str = '{'
curly_right_char: str = '}'
comma_char: str = ','
#
minus_or_dash_char: str = '-'
point_char: str = '.'
underscore_char: str = '_'
#
digit_chars: str = '0123456789'
exponent_char: str = 'e'
#
str_delimiter: str = '"'
backslash_char: str = '\\'
#
letter_lower_chars: str = 'abcdefghijklmnopqrstuvwxyz'
letter_upper_chars: str = letter_lower_chars.upper()
letter_all_chars = letter_lower_chars + letter_upper_chars
#
letter_and_digit_chars = letter_all_chars + underscore_char + digit_chars
#
true: str = 'true'
false: str = 'false'
null: str = 'null'
inf: str = 'inf'
minf: str = '-inf'


content_t: TypeAlias = float | int | str | bool | None | dict[str, "Token"] | tuple[bool, str]
content_t = content_t | Lst[Entry[Lst[Entry["Token"]]]]


class Token(object):
    ttype: str = None
    content: content_t = None

    class TType(object):  # token type
        INDENT: str = 'indent'
        LINENO: str = 'line-number'
        LINEBREAK: str = 'line-break'

        STRING: str = 'str'
        INTEGER: str = 'int'
        FLOAT: str = 'float'
        BOOL: str = 'bool'
        NULL: str = 'null'
        INF: str = 'infinity'
        MINF: str = '-infinity'

        BRACKET_LEFT: str = 'bracket-left'
        BRACKET_RIGHT: str = 'bracket-right'
        CURLY_LEFT: str = 'curly-left'
        CURLY_RIGHT: str = 'curly-right'

        KEY: str = 'key'
        PAIR: str = 'key-value-pair'
        COMMA: str = 'comma'

        ALIASDEF: str = 'alias-define'
        ALIASREF: str = 'alias-reference'
        ALIASKEY: str = 'alias-reference-and-key'

        LIST: str = 'list'
        DICT: str = 'dict'
        LISTINL: str = 'list-inline'
        DICTINL: str = 'dict-inline'
        DASH: str = 'dash'  # aka "-"

    def __init__(self, ttype: str, content: content_t = None):
        self.ttype = ttype
        self.content = content

    def __str__(self) -> str:
        if isinstance(self.content, Token): _c: str = self.content.ttype
        elif isinstance(self.content, str): _c: str = '"' + split_out_quotes(split_out_br(self.content)) + '"'
        elif isinstance(self.content, list):
            _pre_join: list[str] = [' '.join(entry.ttype for entry in block) for block in self.content]
            _c: str = '<' + ', '.join(_pre_join) + '>'
        else: _c: str = str(self.content)
        return f'Token(ttype: {self.ttype}, content: {_c})'

    def __repr__(self) -> str: return self.__str__()


def indent_token(indent: int) -> Token: return Token(ttype = Token.TType.INDENT, content = indent)


def line_number_token(number: int) -> Token: return Token(ttype = Token.TType.LINENO, content = number)


def line_break_token() -> Token: return Token(ttype = Token.TType.LINEBREAK)


def key_token(key: str) -> Token: return Token(ttype = Token.TType.KEY, content = key)


def pair_token(key: Token, value: Token) -> Token:
    return Token(ttype = Token.TType.PAIR, content = dict(key = key, value = value))


def string_token(content: str) -> Token: return Token(ttype = Token.TType.STRING, content = content)


def int_token(number: int) -> Token: return Token(ttype = Token.TType.INTEGER, content = number)


def float_token(number: float) -> Token: return Token(ttype = Token.TType.FLOAT, content = number)


def inf_token(positive: bool = True, content: str | None = None) -> Token:
    if positive: return Token(ttype = Token.TType.INF, content = content)
    return Token(ttype = Token.TType.MINF, content = content)


def bool_token(val: bool, content: str | None = None) -> Token:
    return Token(ttype = Token.TType.BOOL, content = (val, content))


def null_token(content: str | None = None) -> Token: return Token(ttype = Token.TType.NULL, content = content)


def alias_define_token(key: str) -> Token: return Token(ttype = Token.TType.ALIASDEF, content = key)


def alias_reference_token(key: str) -> Token: return Token(ttype = Token.TType.ALIASREF, content = key)


def comma_token() -> Token: return Token(ttype = Token.TType.COMMA)


def bracket_token(bracket: str) -> Token:
    if bracket == bracket_left_char: return Token(ttype = Token.TType.BRACKET_LEFT)
    if bracket == bracket_right_char: return Token(ttype = Token.TType.BRACKET_RIGHT)
    if bracket == curly_left_char: return Token(ttype = Token.TType.CURLY_LEFT)
    if bracket == curly_right_char: return Token(ttype = Token.TType.CURLY_RIGHT)
    raise AssertionError('placeholder')


def list_token(contents: Lst[Entry[Lst[Entry[Token]]]]) -> Token:
    return Token(ttype = Token.TType.LIST, content = contents)


def list_inline_token(contents: Lst[Entry[Lst[Entry[Token]]]]) -> Token:
    return Token(ttype = Token.TType.LISTINL, content = contents)


def dict_token(contents: Lst[Entry[Lst[Entry[Token]]]]) -> Token:
    return Token(ttype = Token.TType.DICT, content = contents)


def dict_inline_token(contents: Lst[Entry[Lst[Entry[Token]]]]) -> Token:
    return Token(ttype = Token.TType.DICTINL, content = contents)


def dash_token() -> Token: return Token(ttype = Token.TType.DASH)


class Parser(object):
    serial: str = None
    token: list[Token] = None

    def __init__(self, serial: str):
        self.serial = serial
        self.tokenize()

    def tokenize(self):
        self.tokenize__atomic()
        self.tokenize__inline_struct_compression()  # inline structs are: inline-list and inline-dict
        self.tokenize__regular_struct_compression()  # r

    def _deserialize(self, token: Token, vc: Callable = list) -> Any:
        if token.ttype == Token.TType.INTEGER: return token.content
        if token.ttype == Token.TType.FLOAT: return token.content
        if token.ttype == Token.TType.INF: return math.inf
        if token.ttype == Token.TType.MINF: return -math.inf
        if token.ttype == Token.TType.STRING: return token.content
        if token.ttype == Token.TType.BOOL: return token.content[0]
        if token.ttype == Token.TType.NULL: return None
        if token.ttype in (Token.TType.LISTINL, Token.TType.LIST):
            listt: list = list()
            for group in token.content:
                for entry in group.value:
                    sub_token: Token = entry.value
                    listt.append(self._deserialize(sub_token, vc = vc))
            return listt
        if token.ttype in (Token.TType.DICTINL, Token.TType.DICT):
            dictt: dict = dict()
            for group in token.content:
                for entry in group.value:
                    pair: Token = entry.value
                    dictt[pair.content['key'].content] = self._deserialize(pair.content['value'], vc = vc)
            return dictt
        raise AssertionError('placeholder')

    def parse(self, vec_constructor: Callable = list) -> Any:
        out: Any | None = None
        switch: int = True
        for entry in self.token:
            token: Token = entry.value
            if token.ttype in (Token.TType.LINENO, Token.TType.INDENT, Token.TType.LINEBREAK): continue
            if switch:
                out = self._deserialize(token, vc = vec_constructor)
                switch = False
            else: raise AssertionError('placeholder')
        if switch: print("WARNING: yamello file appears to be essentially empty!")
        return out

    @staticmethod
    def retrieve_char(pointer: int, line: str, reaction: Callable[[int, str], Any] | None = None):
        try: return line[pointer]
        except IndexError:
            if reaction is None: raise AssertionError('placeholder')
            else: return reaction(pointer, line)

    def tokenize__atomic(self) -> None:
        rows = list()

        lines: Iterator[str] = iter(self.serial.splitlines())
        continue_to_next_line = True
        pointer: int = -1
        line: str = ""
        token_line: list[Token] = list()
        line_no: int = 0
        while True:
            if continue_to_next_line:
                line_no += 1
                continue_to_next_line = False
                pointer: int = 0
                try: line: str = next(lines)
                except StopIteration: break
                if (len(rows) == 0) or (len(rows[-1]) > 2):
                    token_line = list()
                    rows.append(token_line)
                    token_line.append(line_number_token(line_no))
                else:
                    token_line = rows[-1]
                    if token_line[-1].ttype != Token.TType.INDENT: raise AssertionError('palceholder')
                    if token_line[-2].ttype != Token.TType.LINENO: raise AssertionError('palceholder')
                    token_line.pop()
                    token_line[-1].content = line_no

                keep_on_while: bool = True
                indent: int = 0
                while keep_on_while:
                    char = self.retrieve_char(pointer, line, lambda *args: None)
                    if (char is None) or (char == comment_char): continue_to_next_line = True
                    if char != space_char: keep_on_while = False
                    else:
                        indent += 1
                        pointer += 1
                else: token_line.append(indent_token(indent = indent))
                if continue_to_next_line: continue

            char = self.retrieve_char(pointer, line, lambda *args: None)
            if (char is None) or (char == comment_char):
                continue_to_next_line = True
                continue

            elif char == space_char:
                while (char := self.retrieve_char(pointer, line, lambda *args: None)) == space_char: pointer += 1
                if char is None: continue_to_next_line = True
                continue

            elif char in (define_alias_char, reference_alias_char):
                pointer += 1
                if char == define_alias_char:
                    pointer, token = self._gather_string(pointer, line)
                    token = alias_define_token(token.content)
                elif char == reference_alias_char:
                    pointer, token = self._gather_string(pointer, line)
                    token = alias_reference_token(token.content)
                else: raise AssertionError('placeholder')
                token_line.append(token)
                continue

            elif char == double_colon_char:
                pointer += 1
                try: token: Token = token_line[-1]
                except IndexError: raise AssertionError('placeholder')
                if token.ttype == Token.TType.ALIASREF: token_line[-1].ttype = Token.TType.ALIASKEY
                else:
                    if token.ttype != Token.TType.STRING:
                        if token.ttype == Token.TType.BOOL: token = string_token(token.content[1])
                        elif token.ttype in (Token.TType.INF, Token.TType.NULL): token = string_token(token.content)
                        else: raise AssertionError('placeholder')
                        token_line[-1] = token
                    token_line[-1].ttype = Token.TType.KEY
                continue

            elif char == comma_char:
                token_line.append(comma_token())
                pointer += 1
                continue

            elif char in (bracket_left_char, curly_left_char, bracket_right_char, curly_right_char):
                token_line.append(bracket_token(char))
                pointer += 1
                continue

            else:
                if char == '-':
                    sub_pointer: int = pointer + 1
                    sub_char = self.retrieve_char(sub_pointer, line)
                    if sub_char == space_char:
                        token_line.append(dash_token())
                        pointer = sub_pointer
                        continue

                try:
                    pointer, token = self.gather_base_datatype(pointer, line)
                    token_line.append(token)
                    continue
                except AssertionError: pass

            print(f"WARNING: {line[pointer:]}")
            pointer += 1

        self.token: Lst[Entry[Token]] = Lst()
        for row in rows:
            if len(row) < 2: raise AssertionError('placeholder')
            if row[0].ttype != Token.TType.LINENO: raise AssertionError('placeholder')
            if row[1].ttype != Token.TType.INDENT: raise AssertionError('placeholder')
            for entry in row: self.token.append(entry)
            self.token.append(line_break_token())

    def tokenize__inline_struct_compression(self):
        line_number: Entry | None = None
        while True:
            stack: list[list[Entry]] = list()
            for entry in self.token:
                token: Token = entry.value
                if token.ttype == Token.TType.LINENO: line_number = entry
                elif token.ttype in (Token.TType.BRACKET_LEFT, Token.TType.CURLY_LEFT):
                    stack.append([line_number, entry])
                elif token.ttype in (Token.TType.BRACKET_RIGHT, Token.TType.CURLY_RIGHT):
                    line_no_of_left, left = stack.pop()
                    line_no_of_right, right = line_number, entry
                    contents: Lst[Entry[Lst[Entry[Token]]]] = Lst()
                    contents.append(Lst())
                    sub_entry: Entry = left
                    while True:
                        sub_entry = sub_entry.next
                        sub_token: Token = sub_entry.value
                        if sub_entry is right: break
                        if sub_token.ttype in (Token.TType.LINENO, Token.TType.INDENT, Token.TType.LINEBREAK): continue
                        if sub_token.ttype == Token.TType.COMMA: contents.append(Lst())
                        else: contents[-1].value.append(sub_entry.value)
                    if token.ttype == Token.TType.BRACKET_RIGHT:
                        inline_struct_token: Token = list_inline_token(contents = contents)
                    elif token.ttype == Token.TType.CURLY_RIGHT:
                        inline_struct_token: Token = dict_inline_token(contents = contents)
                    else: raise AssertionError('placeholder')
                    self.token.substitute(start = left, stop = right, new_contents = [inline_struct_token])
                    break
            else: break
        if len(stack) > 0: raise AssertionError('placeholder')

        alias_map: dict[str, Token] = dict()
        self.resolve_all_alias(self.token, alias_map)

        self.resolve_all_inline_key_pairs(self.token, inside_inline = False)
        self.validate_inline_structs(self.token, inside_inline_list = False, inside_inline_dict = False)

    def resolve_all_alias(self, tokens: Lst[Entry[Token]], alias_map: dict[str, Token]):
        alias_define_token_removal_set: set[Entry] = set()
        for entry in tokens:
            token: Token = entry.value
            if token.ttype in (Token.TType.LISTINL, Token.TType.DICTINL):
                for group in token.content:
                    self.resolve_all_alias(group.value,
                                           alias_map)
            if token.ttype in (Token.TType.LIST, Token.TType.DICT):  # cannot exist yet
                raise AssertionError('placeholder')
            elif token.ttype == Token.TType.ALIASDEF:
                if not (entry.next.value.ttype in (Token.TType.STRING, Token.TType.INTEGER, Token.TType.FLOAT,
                                                   Token.TType.NULL, Token.TType.INF, Token.TType.MINF,
                                                   Token.TType.KEY, Token.TType.LISTINL, Token.TType.DICTINL)):
                    raise AssertionError('placeholder')
                alias_map[token.content] = entry.next.value
                alias_define_token_removal_set.add(entry)
            elif token.ttype == Token.TType.ALIASREF:
                sub_token: Token = alias_map[token.content]
                if sub_token.ttype == Token.TType.KEY: sub_token = string_token(content = sub_token.content)
                entry.value = sub_token
            elif token.ttype == Token.TType.ALIASKEY: entry.value = key_token(key = alias_map[token.content].content)
        for entry in alias_define_token_removal_set: tokens.remove(entry)

    def resolve_all_inline_key_pairs(self, tokens: Lst[Entry[Token]], inside_inline: bool):
        key_token_removal_set: set[Entry] = set()
        key_token_substitutes: dict[Entry, Token] = dict()
        for entry in tokens:
            token: Token = entry.value
            if token.ttype in (Token.TType.LISTINL, Token.TType.DICTINL):
                for group in token.content:
                    self.resolve_all_inline_key_pairs(group.value, inside_inline = True)
            if token.ttype in (Token.TType.LIST, Token.TType.DICT):  # cannot exist yet
                raise AssertionError('placeholder')
            if inside_inline and (token.ttype == Token.TType.KEY):
                value_entry: Entry = entry.next
                value_token: Token = value_entry.value
                key_token_removal_set.add(entry)
                key_token_substitutes[value_entry] = pair_token(key = token, value = value_token)
        for entry in key_token_removal_set: tokens.remove(entry)
        for entry, new_token in key_token_substitutes.items(): entry.value = new_token

    def validate_inline_structs(self,
                                tokens: Lst[Entry[Token]],
                                inside_inline_list: bool,
                                inside_inline_dict: bool):
        for entry in tokens:
            token: Token = entry.value
            if token.ttype in (Token.TType.LISTINL, Token.TType.DICTINL):
                for group in token.content:
                    self.validate_inline_structs(group.value,
                                                 inside_inline_list = (token.ttype == Token.TType.LISTINL),
                                                 inside_inline_dict = (token.ttype == Token.TType.DICTINL))
            if token.ttype in (Token.TType.LIST, Token.TType.DICT):  # cannot exist yet
                raise AssertionError('placeholder')
            if inside_inline_list:
                if len(tokens) != 1: raise AssertionError('placeholder')
                if not (token.ttype in (Token.TType.STRING, Token.TType.INTEGER, Token.TType.FLOAT,
                                        Token.TType.NULL, Token.TType.INF, Token.TType.MINF,
                                        Token.TType.LISTINL, Token.TType.DICTINL)):
                    raise AssertionError('placeholder')
            if inside_inline_dict:
                if len(tokens) != 1: raise AssertionError('placeholder')
                if token.ttype != Token.TType.PAIR: raise AssertionError('placeholder')
                key: Token = token.content['key']
                val: Token = token.content['value']
                if key.ttype != Token.TType.KEY: raise AssertionError('palceholder')
                if not (val.ttype in (Token.TType.STRING, Token.TType.INTEGER, Token.TType.FLOAT,
                                      Token.TType.NULL, Token.TType.INF, Token.TType.MINF,
                                      Token.TType.LISTINL, Token.TType.DICTINL)):
                    raise AssertionError('placeholder')

    def tokenize__regular_struct_compression(self):
        while True:
            if self.tokenize__regular_dict(): continue
            if self.tokenize__regular_list(): continue
            break
        self.resolve_all_regular_key_pairs(self.token)
        self.validate_regular_structs(self.token, inside_regular_list = False, inside_regular_dict = False)

    def tokenize__regular_dict(self) -> bool:
        line_number: Entry | None = None
        last_key_indent: int = -1  # indent of latest (most inner) key found so far -> indicates dict
        # last_dash_indent: int = -1  # indent of latest (most inner) dash (i.e. '-') found so far -> indicates list
        current_line_indent: int = -1  # current indentation of this line
        stack: list[list[Entry | int]] = list()  # for identifying most inner regular dict
        found_key_already: bool = False  # for key found on a line (since there can only be one)
        for idx, entry in enumerate(self.token):
            token: Token = entry.value
            if token.ttype == Token.TType.LINENO:  # also means: entered new line/row!
                line_number = entry
                found_key_already = False  # new line -> reset the 'found key on this line'-flag
            elif token.ttype == Token.TType.INDENT:
                current_line_indent = token.content
                if current_line_indent < last_key_indent:  # gen. structure: LINENO, INDENT, ..., LINEBREAK  ...
                    prev_entry: Entry = entry.prev
                    prev_token: Token = prev_entry.value
                    if prev_token.ttype != Token.TType.LINENO: raise AssertionError('placeholder')
                    pprev_entry: Entry = prev_entry.prev
                    pprev_token: Token = pprev_entry.value
                    if pprev_token.ttype != Token.TType.LINEBREAK: raise AssertionError('placeholder')
                    ppprev_entry: Entry = pprev_entry.prev
                    stack[-1][-2:] = line_number, ppprev_entry  # ... gather last token just before latest linebreak
            elif (idx + 1 == len(self.token)) and (len(stack) > 0):  # special treatment for end of file ...
                current_line_indent = -1  # ... acts like a sudden set back of indent
                if token.ttype != Token.TType.LINEBREAK: raise AssertionError('placeholder')
                prev_entry: Entry = entry
                while prev_entry.value.ttype in (Token.TType.LINENO, Token.TType.INDENT, Token.TType.LINEBREAK):
                    prev_entry = prev_entry.prev  # there could be an arbitrary number of empty lines to traverse
                stack[-1][-2:] = line_number, prev_entry
            elif token.ttype == Token.TType.KEY:
                if found_key_already: raise AssertionError('placeholder')  # only 1 key per line allowed (regular dict)
                else: found_key_already = True
                if current_line_indent > last_key_indent:  # suddenly higher indent -> new regular dict introduced
                    stack.append([line_number, current_line_indent, entry, None, None])
                last_key_indent = current_line_indent
            elif token.ttype == Token.TType.DASH:
                # if current_line_indent > last_dash_indent: last_dash_indent = current_line_indent
                prev_entry: Entry = entry.prev
                while prev_entry.value.ttype != Token.TType.INDENT:
                    if prev_entry.value.ttype != Token.TType.DASH: raise AssertionError("placeholder")
                    prev_entry = prev_entry.prev
                current_line_indent += 2  # dash contributes to (effective) indentation

            if (current_line_indent < last_key_indent) and (len(stack) > 0):  # sudden indentation set back -> resolve
                _stack_out = stack.pop()
                line_no_of_left: Entry = _stack_out[0]
                key_indent: int = _stack_out[1]
                # if not (last_dash_indent is None):
                #     if last_dash_indent == key_indent: raise AssertionError('placeholder')  # dict  -xor-  list
                #     if last_dash_indent > key_indent: return False  # list even more inner struct than dict right now
                left: Entry = _stack_out[2]
                line_no_of_right: Entry = _stack_out[3]
                right: Entry = _stack_out[4]

                contents: Lst[Entry[Lst[Entry[Token]]]] = Lst()
                contents.append(Lst())
                contents[-1].value.append(left.value)
                sub_entry: Entry = left

                hit_value: bool = False
                value_before_linebreak: bool = True
                value_indent: int | None = None
                cur_indent: int = -1
                while True:
                    sub_entry = sub_entry.next
                    sub_token: Token = sub_entry.value
                    if sub_entry is right: break
                    if sub_token.ttype in (Token.TType.LINENO, Token.TType.INDENT, Token.TType.LINEBREAK):
                        if sub_token.ttype == Token.TType.LINEBREAK:
                            if not hit_value: value_before_linebreak = False
                            cur_indent = -1  # reset
                        elif sub_token.ttype == Token.TType.INDENT: cur_indent = sub_token.content
                        continue
                    elif sub_token.ttype == Token.TType.KEY:
                        hit_value = False  # reset
                        value_before_linebreak = True  # reset
                        contents.append(Lst())
                    elif sub_token.ttype == Token.TType.DASH:
                        if cur_indent == key_indent: raise AssertionError('placeholder')
                        return False
                    else:
                        if hit_value: raise AssertionError('placeholder')
                        else: hit_value = True
                        if value_before_linebreak:
                            if sub_token.ttype in (Token.TType.LIST, Token.TType.DICT):
                                raise AssertionError('placeholder')
                        else:
                            if value_indent is None:
                                if cur_indent > key_indent: value_indent = cur_indent
                                else: raise AssertionError('placeholder')
                            elif value_indent != cur_indent: raise AssertionError('placeholder')
                    contents[-1].value.append(sub_entry.value)
                contents[-1].value.append(right.value)
                regular_dict_token: Token = dict_token(contents = contents)
                self.token.substitute(start = left, stop = right, new_contents = [regular_dict_token])
                return True

    def tokenize__regular_list(self) -> bool:
        line_number: Entry | None = None
        last_dash_indent: int = -1  # indent of latest (most inner) key found so far
        current_line_indent: int = -1  # current indentation of this line
        stack: list[list[Entry | int]] = list()  # for identifying most inner regular dict
        for idx, entry in enumerate(self.token):
            token: Token = entry.value
            if token.ttype == Token.TType.LINENO:  # also means: entered new line/row!
                line_number = entry
            elif token.ttype == Token.TType.INDENT:
                current_line_indent = token.content
                if current_line_indent < last_dash_indent:  # gen. structure: LINENO, INDENT, ..., LINEBREAK  ...
                    prev_entry: Entry = entry.prev
                    prev_token: Token = prev_entry.value
                    if prev_token.ttype != Token.TType.LINENO: raise AssertionError('placeholder')
                    pprev_entry: Entry = prev_entry.prev
                    pprev_token: Token = pprev_entry.value
                    if pprev_token.ttype != Token.TType.LINEBREAK: raise AssertionError('placeholder')
                    ppprev_entry: Entry = pprev_entry.prev
                    stack[-1][-2:] = line_number, ppprev_entry  # ... gather last token just before latest linebreak
            elif (idx + 1 == len(self.token)) and (len(stack) > 0):  # special treatment for end of file ...
                current_line_indent = -1  # ... acts like a sudden set back of indent
                if token.ttype != Token.TType.LINEBREAK: raise AssertionError('placeholder')
                prev_entry: Entry = entry
                while prev_entry.value.ttype in (Token.TType.LINENO, Token.TType.INDENT, Token.TType.LINEBREAK):
                    prev_entry = prev_entry.prev  # there could be an arbitrary number of empty lines to traverse
                stack[-1][-2:] = line_number, prev_entry
            elif token.ttype == Token.TType.DASH:
                if current_line_indent > last_dash_indent:
                    last_dash_indent = current_line_indent
                    stack.append([line_number, current_line_indent, entry, None, None])
                prev_entry: Entry = entry.prev
                while prev_entry.value.ttype != Token.TType.INDENT:
                    if prev_entry.value.ttype != Token.TType.DASH: raise AssertionError("placeholder")
                    prev_entry = prev_entry.prev
                current_line_indent += 2  # dash contributes to (effective) indentation

            if (current_line_indent < last_dash_indent) and (len(stack) > 0):  # sudden indentation set back -> resolve
                _stack_out = stack.pop()
                line_no_of_left: Entry = _stack_out[0]
                dash_indent: int = _stack_out[1]
                left: Entry = _stack_out[2]
                line_no_of_right: Entry = _stack_out[3]
                right: Entry = _stack_out[4]

                contents: Lst[Entry[Lst[Entry[Token]]]] = Lst()
                contents.append(Lst())
                sub_entry: Entry = left

                hit_value: bool = False
                value_before_linebreak: bool = True
                value_indent: int | None = None
                cur_indent: int = -1
                while True:
                    sub_entry = sub_entry.next
                    sub_token: Token = sub_entry.value
                    if sub_entry is right: break
                    if sub_token.ttype in (Token.TType.LINENO, Token.TType.INDENT, Token.TType.LINEBREAK):
                        if sub_token.ttype == Token.TType.LINEBREAK:
                            if not hit_value: value_before_linebreak = False
                            cur_indent = -1  # reset
                        elif sub_token.ttype == Token.TType.INDENT: cur_indent = sub_token.content
                        continue
                    elif sub_token.ttype == Token.TType.DASH:
                        hit_value = False  # reset
                        value_before_linebreak = True  # reset
                        contents.append(Lst())
                    else:
                        if hit_value: raise AssertionError('placeholder')
                        else: hit_value = True
                        if not value_before_linebreak:
                            if value_indent is None:
                                if cur_indent > dash_indent: value_indent = cur_indent
                                else: raise AssertionError('placeholder')
                            elif value_indent != cur_indent: raise AssertionError('placeholder')
                        contents[-1].value.append(sub_entry.value)
                if right.value.ttype == Token.TType.DASH: raise AssertionError('placeholder')
                contents[-1].value.append(right.value)
                regular_list_token: Token = list_token(contents = contents)
                self.token.substitute(start = left, stop = right, new_contents = [regular_list_token])
                return True

    def resolve_all_regular_key_pairs(self, tokens: Lst[Entry[Token]]):
        key_token_removal_set: set[Entry] = set()
        key_token_substitutes: dict[Entry, Token] = dict()
        for entry in tokens:
            token: Token = entry.value
            if token.ttype in (Token.TType.LIST, Token.TType.DICT):
                for group in token.content:
                    self.resolve_all_regular_key_pairs(group.value)
            if token.ttype == Token.TType.KEY:
                value_entry: Entry = entry.next
                value_token: Token = value_entry.value
                key_token_removal_set.add(entry)
                key_token_substitutes[value_entry] = pair_token(key = token, value = value_token)
        for entry in key_token_removal_set: tokens.remove(entry)
        for entry, new_token in key_token_substitutes.items(): entry.value = new_token

    def validate_regular_structs(self,
                                 tokens: Lst[Entry[Token]],
                                 inside_regular_list: bool,
                                 inside_regular_dict: bool):
        for entry in tokens:
            token: Token = entry.value
            if token.ttype in (Token.TType.LIST, Token.TType.DICT):
                for group in token.content:
                    self.validate_regular_structs(group.value,
                                                  inside_regular_list = (token.ttype == Token.TType.LIST),
                                                  inside_regular_dict = (token.ttype == Token.TType.DICT))
            if inside_regular_list:
                if len(tokens) != 1: raise AssertionError('placeholder')
                if not (token.ttype in (Token.TType.STRING, Token.TType.INTEGER, Token.TType.FLOAT,
                                        Token.TType.NULL, Token.TType.INF, Token.TType.MINF,
                                        Token.TType.LISTINL, Token.TType.DICTINL,
                                        Token.TType.LIST, Token.TType.DICT)):
                    raise AssertionError('placeholder')
            if inside_regular_dict:
                if len(tokens) != 1: raise AssertionError('placeholder')
                if token.ttype != Token.TType.PAIR: raise AssertionError('placeholder')
                key: Token = token.content['key']
                val: Token = token.content['value']
                if key.ttype != Token.TType.KEY: raise AssertionError('palceholder')
                if not (val.ttype in (Token.TType.STRING, Token.TType.INTEGER, Token.TType.FLOAT,
                                      Token.TType.NULL, Token.TType.INF, Token.TType.MINF,
                                      Token.TType.LISTINL, Token.TType.DICTINL,
                                      Token.TType.LIST, Token.TType.DICT)):
                    raise AssertionError('placeholder')

    '''
        atomic tokenizing tools
        =======================
    '''
    def expect_chars_and_get_past(self, pointer: int, line: str, expected: str):
        for char_expected in expected:
            char = self.retrieve_char(pointer, line)
            if char != char_expected: raise AssertionError('placeholder')
            pointer += 1
        return pointer

    def get_past_whitespace(self, pointer: int, line: str, expect_at_least_one_space: bool = False) -> int:
        if expect_at_least_one_space: pointer = self.expect_chars_and_get_past(pointer, line, space_char)
        while True:
            char = self.retrieve_char(pointer, line, lambda *args: None)
            if char is None: break
            if char != space_char: break
            pointer += 1
        return pointer

    def _gather_string(self, pointer: int, line: str) -> tuple[int, Token]:
        pointer = self.get_past_whitespace(pointer, line)

        out: str = ""
        first_char: bool = True
        expect_closing_str_delimiter: bool = False
        while True:
            char = self.retrieve_char(pointer, line)
            if char == str_delimiter:
                if first_char:
                    expect_closing_str_delimiter = True
                    first_char = False
                    pointer += 1
                    continue
                elif line[pointer - 1] != backslash_char:
                    if expect_closing_str_delimiter:
                        pointer += 1
                        break
                    else: raise AssertionError('placeholder')
            elif first_char:
                if not (char in letter_all_chars + underscore_char): raise AssertionError('placeholder')
            elif not expect_closing_str_delimiter:
                if not (char in letter_and_digit_chars): break

            out += char

            first_char = False
            pointer += 1
        return pointer, string_token(content = out)

    def _gather_int_or_float(self, pointer: int, line: str) -> tuple[int, Token]:
        pointer = self.get_past_whitespace(pointer, line)

        out: str = ''
        minus_allowed: int = 1
        point_appeared: bool = False
        most_recent_char_was_digit: bool = False
        expect_one_more_digit: bool = False
        exponent_appeared: bool = False
        while True:
            char = self.retrieve_char(pointer, line, lambda *args: None)
            if char == minus_or_dash_char:
                if minus_allowed > 0:
                    out += char
                    most_recent_char_was_digit = False
                    expect_one_more_digit = True
                else: raise AssertionError('placeholder')
            elif char in (None,
                          linebreak_char,
                          space_char,
                          comma_char,
                          comment_char,
                          double_colon_char,
                          curly_right_char,
                          bracket_right_char): break
            elif char in digit_chars:
                out += char
                most_recent_char_was_digit = True
                expect_one_more_digit = False
            elif char == point_char:
                if not most_recent_char_was_digit: raise AssertionError('placeholder')
                if point_appeared: raise AssertionError('placeholder')
                out += char
                point_appeared = True
                most_recent_char_was_digit = False
                expect_one_more_digit = True
            elif char == underscore_char:
                if not most_recent_char_was_digit: raise AssertionError('placeholder')
                out += char
                most_recent_char_was_digit = False
                expect_one_more_digit = True
            elif char == exponent_char:
                if not most_recent_char_was_digit: raise AssertionError('placeholder')
                if exponent_appeared: raise AssertionError('placeholder')
                exponent_appeared = True
                out += char
                point_appeared = True
                most_recent_char_was_digit = False
                expect_one_more_digit = True
                minus_allowed = 2
            else: raise AssertionError('placeholder')
            minus_allowed = max(0, minus_allowed - 1)
            pointer += 1
        if expect_one_more_digit: raise AssertionError('placeholder')
        if len(out) == 0: raise AssertionError('placeholder')

        if point_appeared: return pointer, float_token(number = float(out))
        return pointer, int_token(number = int(out))

    def _gather_false_true_null_inf(self, pointer: int, line: str) -> tuple[int, Token]:
        pointer = self.get_past_whitespace(pointer, line)
        special: str = ''
        while True:
            special += self.retrieve_char(pointer, line)
            for keyword in (true, false, null, inf, minf):
                if special.lower() in keyword: break
            else: raise AssertionError('placeholder')
            pointer += 1
            if special.lower() == true:
                token: Token = bool_token(True, content = special)
                break
            if special.lower() == false:
                token: Token = bool_token(False, content = special)
                break
            if special.lower() == null:
                token: Token = null_token(content = special)
                break
            if special.lower() == inf:
                token: Token = inf_token(content = special)
                break
            if special.lower() == minf:
                token: Token = inf_token(positive = False, content = special)
                break
        return pointer, token

    def gather_base_datatype(self, pointer: int, line: str) -> tuple[int, Token]:
        pointer = self.get_past_whitespace(pointer, line)

        char = self.retrieve_char(pointer, line)
        if char in (letter_all_chars + minus_or_dash_char):
            try: return self._gather_false_true_null_inf(pointer, line)
            except AssertionError: pass
        if (char == str_delimiter) or (char in (letter_all_chars + underscore_char)):
            return self._gather_string(pointer, line)
        return self._gather_int_or_float(pointer, line)
