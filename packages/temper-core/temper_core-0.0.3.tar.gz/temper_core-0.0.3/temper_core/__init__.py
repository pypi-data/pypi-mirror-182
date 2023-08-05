from abc import ABC, abstractmethod
from codecs import iterencode, encode
from collections import deque
from itertools import islice
from math import inf, isnan, copysign
import re

class NoResultException(Exception):
    def __init__(self, message = "NO_RESULT"):
        Exception.__init__(self, message)

class TemperType:
    def __init__(self, tag, pytype, base):
        self._tag = tag
        self._base = base
        self._pytype = pytype

    def __repr__(self):
        return self._tag

    def __eq__(self, other):
        return self is other or (
            isinstance(other, TemperType)
            and self._tag == other._tag
            and self._base == other._base
        )


class TemperObject(ABC):
    "All user-defined classes include this marker class."


class TemperEnum(TemperObject, ABC):
    "Enum classes are user-defined classes additionally with this marker."


def get_static(type_guard, symbol):
    "There's no way to extract the class from a type guard at this time."
    return NotImplemented


def temper_print(value):
    "Temper semantics for printing."
    try:
        if value == vVoid:
            print("Void")
        elif isinstance(value, str):
            print(value)
        else:
            print(repr(value))
        return vVoid
    except Exception:
        raise NoResultException()


def str_cat(*parts):
    "Concatenate parts into a single string."
    return "".join(map(str, parts))


def no_result():
    raise NoResultException()


def generic_cmp(left, right):
    if (left == 0 and right == 0):
        return generic_cmp(copysign(1, left), copysign(1, right))
    return (left > right) - (left < right)


def generic_eq(left, right):
    if (left == 0 and right == 0):
        return generic_eq(copysign(1, left), copysign(1, right))
    return left == right


def generic_not_eq(left, right):
    if (left == 0 and right == 0):
        return generic_not_eq(copysign(1, left), copysign(1, right))
    return left != right


def generic_lt_eq(left, right):
    return generic_cmp(left, right) <= 0


def generic_lt(left, right):
    return generic_cmp(left, right) < 0


def generic_gt_eq(left, right):
    return generic_cmp(left, right) >= 0


def generic_gt(left, right):
    return generic_cmp(left, right) > 0


def bool_not(value):
    return not value


def arith_int_div(dividend, divisor):
    try:
        return dividend // divisor
    except ArithmeticError:
        raise NoResultException()


def arith_dub_div(dividend, divisor):
    try:
        return dividend / divisor
    except ArithmeticError:
        raise NoResultException()


def isinstance_int(val):
    "Python bool is a subclass of int, but Temper treats them as separate types."
    return isinstance(val, int) and not isinstance(val, bool)

def isinstance_char(val):
    "Temper char are represented as single character strings."
    return isinstance(val, str) and len(val) == 1


def cast_none(val):
    if val is not None:
        raise NoResultException()
    return val


def cast_by_type(val, py_type):
    "Cast to a python type by an isinstance check."
    if not isinstance(val, py_type):
        raise NoResultException()
    return val

def cast_by_test(val, predicate):
    "This cast validates that a temper function meets some predicate, e.g. callable."
    if not predicate(val):
        raise NoResultException()
    return val

class Nexter:
    "Construct a consumer function that calls next on an iterator; mimics the javascript generator interface."
    __slots__ = ("_iterator", "value", "done")

    def __init__(self, iterable):
        self._iterator = iter(iterable())
        self.value = None
        self.done = False

    def __call__(self):
        if not self.done:
            try:
                self.value = next(self._iterator)
            except NoResultException as e:
                self.done = True
                raise e
            except StopIteration:
                self.done = True
                raise NoResultException()
        return self


class Label(BaseException):
    "A label enables labled breaks with reasonably readable python"
    __slots__ = ()

    def __enter__(self):
        return self

    def continue_(self):
        raise self

    def break_(self):
        raise self

    def __exit__(self, _exc_type, exc, _traceback):
        return exc is self


class LabelPair(BaseException):
    "Handles an edge case in the semantics of labeled breaks."
    __slots__ = ("continuing",)

    def __init__(self):
        self.continuing = InnerLabel()

    def __enter__(self):
        return self

    def break_(self):
        raise self

    def continue_(self):
        raise self.continuing

    def __exit__(self, _exc_type, exc, _exc_tb):
        return exc is self


class InnerLabel(BaseException):
    __slots__ = ()

    def __enter__(self):
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        return exc_val is self


class Symbol:
    __slots__ = ("_text",)

    def __init__(self, text):
        self._text = text

    @property
    def text(self):
        return self._text

    def __eq__(self, other):
        return (
            self._text == other._text if isinstance(other, Symbol) else NotImplemented
        )

    def __hash__(self):
        return hash(self._text)

    def __repr__(self):
        return "symbol({!r})".format(self._text)

    def __str__(self):
        return self._text


class StringSlice(ABC):
    __slots__ = ()

    @abstractmethod
    def __iter__(self):
        raise NotImplementedError()
        yield 0

    @abstractmethod
    def advance(self, count):
        raise NotImplementedError()

    @abstractmethod
    def _left_plus(self, count):
        raise NotImplementedError()

    @abstractmethod
    def __bool__(self):
        raise NotImplementedError()

    @abstractmethod
    def __len__(self):
        raise NotImplementedError()

    @abstractmethod
    def __str__(self):
        raise NotImplementedError()

    def has_at_least(self, count):
        return count <= 0 or self._left_plus(count) is not None

    def read(self):
        try:
            return next(iter(self))
        except StopIteration:
            raise NoResultException()

    @property
    def length(self):
        return len(self)

    def to_string(self):
        return str(self)

    @property
    def is_empty(self):
        return not self


class Utf8StringSlice(StringSlice):
    __slots__ = ("_content", "_left")

    def __init__(self, left, content):
        if left >> 2 >= len(content):
            left = 0
            content = ""
        self._left = left
        self._content = content

    def __iter__(self):
        left, content = self._left, self._content
        utf8 = "utf-8"
        idx, sub = left >> 2, left & 3
        if sub:
            for byt in islice(encode(content[idx], utf8), sub, None):
                yield int(byt)
            idx += 1
        for buf in iterencode(_str_iter_at(content, idx), utf8):
            yield from map(int, buf)

    def __bool__(self):
        return bool(self._content)

    def __len__(self):
        left, content = self._left, self._content
        return sum(_utf8_size(char) for char in _str_iter_at(content, left >> 2)) - (
            left & 3
        )

    def _left_plus(self, count):
        left, content = self._left, self._content
        len_content = len(content)
        idx, sub = left >> 2, left & 3

        while count > 0 and idx < len_content:
            rem = _utf8_size(content[idx]) - sub
            if rem > count:
                sub += count
                count = 0
            else:
                count -= rem
                sub = 0
                idx += 1

        return None if count else idx << 2 | sub

    def advance(self, count):
        if count <= 0:
            result = self
        else:
            left, content = self._left_plus(count), self._content
            if left is None:
                left, content = 0, ""
            result = Utf8StringSlice(left, content)
        return result

    def to_json(self):
        left, content = self._left, self._content
        right = len(content) << 2
        return {"left": left, "right": right, "content": content}

    def __str__(self):
        left, content = self._left, self._content
        idx, sub = left >> 2, left & 3
        if sub:
            pre = "\ufffd"
            idx += 1
        else:
            pre = ""
        return pre + content[idx:]


class Utf16StringSlice(StringSlice):
    __slots__ = ("_content", "_left")

    def __init__(self, left, content):
        if left >> 1 >= len(content):
            left = 0
            content = ""
        self._left = left
        self._content = content

    def __iter__(self):
        left, content = self._left, self._content
        utf16 = "utf-16-be"
        idx, sub = left >> 1, left & 1
        if sub:
            for hi, lo in islice(_iter_pairs(encode(content[idx], utf16)), sub, None):
                yield hi << 8 | lo
            idx += 1
        for buf in iterencode(_str_iter_at(content, idx), utf16):
            for hi, lo in _iter_pairs(buf):
                yield hi << 8 | lo

    def __bool__(self):
        return bool(self._content)

    def __len__(self):
        left, content = self._left, self._content
        return sum(_utf16_size(char) for char in _str_iter_at(content, left >> 1)) - (
            left & 1
        )

    def _left_plus(self, count):
        left, content = self._left, self._content
        len_content = len(content)
        idx, sub = left >> 1, left & 1

        while count > 0 and idx < len_content:
            rem = _utf16_size(content[idx]) - sub
            if rem > count:
                sub += count
                count = 0
            else:
                count -= rem
                sub = 0
                idx += 1

        return None if count else idx << 1 | sub

    def advance(self, count):
        if count <= 0:
            result = self
        else:
            left, content = self._left_plus(count), self._content
            if left is None:
                left, content = 0, ""
            result = Utf16StringSlice(left, content)
        return result

    def to_json(self):
        left, content = self._left, self._content
        right = len(content) << 1
        return {"left": left, "right": right, "content": content}

    def __str__(self):
        left, content = self._left, self._content
        idx, sub = left >> 1, left & 1
        if sub:
            pre = "\ufffd"
            idx += 1
        else:
            pre = ""
        return pre + content[idx:]


class CodePointsStringSlice(StringSlice):
    __slots__ = ("_content", "_left")

    def __init__(self, left, content):
        if left >= len(content):
            content = ""
            left = 0
        self._left = left
        self._content = content

    def __iter__(self):
        left, content = self._left, self._content
        return (ord(c) for c in _str_iter_at(content, left))

    def __len__(self):
        return len(self._content) - self._left

    def __bool__(self):
        return bool(self._content)

    def _left_plus(self, count):
        left = self._left + count
        return None if left > len(self._content) else left

    def advance(self, count):
        if count <= 0:
            result = self
        else:
            left, content = self._left_plus(count), self._content
            if left is None:
                left, content = 0, ""
            result = CodePointsStringSlice(left, content)
        return result

    def __str__(self):
        return self._content[self._left :]

    def to_json(self):
        left, content = self._left, self._content
        return {"left": left, "right": len(content), "content": content}


class DenseBitVector:
    "An expandable bitvector backed by a bytearray."
    __slots__ = ("_bytearray",)
    _not0 = re.compile(rb"[^\0]")  # Any byte other than 0
    _tail0 = re.compile(rb"\0*$")  # Trailing 0 bytes

    def __init__(self, capacity):
        "Capacity is in bits."
        self._bytearray = bytearray((capacity + 7) >> 3)

    def __bool__(self):
        "Test if any bit is set."
        return bool(self._not0.search(self._bytearray))

    def __bytes__(self):
        "Convert the bit vector into a read-only bytes value."
        return self._tail0.sub(b"", self._bytearray)

    def get(self, idx):
        "Read a bit from the vector as a boolean; or false if out of bounds."
        if idx < 0:
            return False
        ba = self._bytearray
        byte_index = idx >> 3
        if byte_index >= len(ba):
            return False
        return bool(ba[byte_index] & (1 << (idx & 7)))

    def set(self, idx, bit):
        "Set a bit in the bit vector, expanding the vector as needed."
        if idx < 0:
            raise NoResultException()
        ba = self._bytearray
        byte_size = len(ba)
        byte_index = idx >> 3
        if byte_index >= byte_size:
            ba.extend(b"\0" * (byte_index + 1 - byte_size))
        mask = 1 << (idx & 7)
        if bit:
            ba[byte_index] |= mask
        else:
            ba[byte_index] &= ~mask
        return vVoid


# Type tags

tAnyValue = TemperType("AnyValue", object, None)
tDenseBitVector = TemperType("DenseBitVector", DenseBitVector, tAnyValue)
tBoolean = TemperType("Boolean", bool, tAnyValue)
tChar = TemperType("Char", str, tAnyValue)
tClass = TemperType("Class", type, tAnyValue)
tClosRec = TemperType("ClosRec", None, tAnyValue)
tDeque = TemperType("Deque", deque, tAnyValue)
tDouble = TemperType("Double", float, tAnyValue)
tFunction = TemperType("Function", None, tAnyValue)
tInt = TemperType("Int", int, tAnyValue)
tList = TemperType("List", tuple, tAnyValue)
tListBuilder = TemperType("ListBuilder", list, tAnyValue)
tNull = TemperType("Null", type(None), tAnyValue)
tProblem = TemperType("Problem", None, None)
tString = TemperType("String", str, tAnyValue)
tStringSlice = TemperType("StringSlice", StringSlice, tAnyValue)
tSymbol = TemperType("Symbol", Symbol, tAnyValue)

tCodePointsStringSlice = TemperType(
    "CodePointsStringSlice", CodePointsStringSlice, tStringSlice
)
tUtf8StringSlice = TemperType("Utf8StringSlice", Utf8StringSlice, tStringSlice)
tUtf16StringSlice = TemperType("Utf16StringSlice", Utf16StringSlice, tStringSlice)
tTuple = TemperType("Tuple", tuple, tAnyValue)
tVoid = TemperType("Void", tuple, tTuple)
vVoid = ()


## Constructors


def string_utf8(string):
    "Implements extension method String::utf8"
    return Utf8StringSlice(0, string)


def string_utf16(string):
    "Implements extension method String::utf8"
    return Utf16StringSlice(0, string)


def string_code_points(string):
    "Implements extension method String::utf8"
    return CodePointsStringSlice(0, string)


## Extension methods


def int_to_string(num, radix=10):
    "Implements extension method Int::toString"
    if not 2 <= radix < 36:
        raise NoResultException()
    elif radix == 10:
        return str(num)
    elif radix == 16:
        return "%x" % (num,)
    elif radix == 8:
        return "%o" % (num,)
    else:

        def seq(rem):
            if rem == 0:
                yield "0"

            while rem:
                yield "0123456789abcdefghijklmnopqrstuvwxyz"[rem % radix]
                rem //= radix

            if num < 0:
                yield "-"

        return "".join(reversed(list(seq(abs(num)))))


def float64_to_string(value):
    "Implements extension method Float64::toString"
    if value == inf:
        return "∞"
    elif value == -inf:
        return "-∞"
    elif isnan(value):
        return "NaN"
    else:
        return str(value)

def boolean_to_string(value):
    return "true" if value else "false"


def string_split(string, separator):
    "Split a string, returning a list of elements."
    return string.split(separator)


def list_filter(lst, predicate):
    "Filter a list of elements, aborting on no-result."
    return [*filter(predicate, lst)]


def list_get(lst, index):
    "Get an item from a list by index."
    if index < 0:  # Prohibit python index semantics
        raise NoResultException()
    try:
        return lst[index]
    except IndexError:
        raise NoResultException()


def list_get_or(lst, index, default):
    "Get an item from a list by index with a default."
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return default


def list_builder_add(lst: list, elem, at=None):
    "Append a single element to a list."
    if at is None:
        lst.append(elem)
    else:
        if at < 0 or at > len(lst):
            raise NoResultException()
        lst.insert(at, elem)
    return vVoid


def list_builder_add_all(lst, elems, at=None):
    "Append multiple elements to a list."
    if at is None:
        lst.extend(elems)
    else:
        if at < 0 or at > len(lst):
            raise NoResultException()
        lst[at:at] = elems
    return vVoid


def list_join(lst, separator, stringifier):
    "Join a list of items after converting them to strings."
    return separator.join(map(stringifier, lst))


def list_map(lst, func):
    "Map a list of elements."
    return tuple(map(func, lst))


def list_builder_reverse(lst):
    "Reverses a list in place."
    lst.reverse()


def list_builder_set(lst, idx, val):
    "Set a list element, returning no result if out of bounds, or void on success."
    if idx < 0:
        raise NoResultException()
    try:
        lst[idx] = val
    except IndexError:
        raise NoResultException()
    else:
        return vVoid


def list_map_dropping(lst, func):
    "Map a list of elements, omitting any for which func produces no result."
    results = []
    for e in lst:
        try:
            results.append(func(e))
        except NoResultException:
            pass
    return tuple(results)

def list_slice(lst, start_inclusive, end_exclusive):
    "Almost exactly a Python slice, but indices are constrained to be >= 0."
    # TODO(tjp): Cheaper to always say tuple here, or separate out for ListBuilder use?
    return tuple(lst[max(start_inclusive, 0) : max(end_exclusive, 0)])


def deque_add(deq, elem):
    "Defer to deque.add."
    deq.append(elem)
    return vVoid


def deque_remove_first(deq):
    "Defer to deque.popleft, except returning no result when the deque is empty."
    if not deq:
        raise NoResultException()
    return deq.popleft()

def dense_bit_vector_set(instance, idx, bit):
    "Sets a bit within a dense bit vector."
    return instance.set(idx, bit)


## Utility functions


def _count_iter(iterable):
    "Use a constrained deque to consume an enumeration of the iterable, giving us the count."
    last = deque(enumerate(iterable, 1), 1)
    return last.pop()[0] if last else 0


def _str_iter_at(string, offset):
    "Return a string iterator skipped forward by 'offset' characters."
    iterator = iter(string)
    if offset:
        iterator.__setstate__(offset)
    return iterator


def _utf8_size(char):
    num = ord(char)
    if 0 <= num < 0o200:
        return 1
    elif 0o200 <= num < 0o4000:
        return 2
    elif 0o4000 <= num < 0o100000:
        return 3
    else:
        return 4


def _utf16_size(char):
    return 1 + (ord(char) >= 0x10000)


def _iter_pairs(iterable):
    "Convert a stream like [1, 2, 3, 4] to [(1, 2), (3, 4)]."
    iterator = iter(iterable)
    # The semantics of zip are that it draws from iterators in a round-robin fashion. Passing the same iterator
    # twice thus converts a list into pairs.
    # We're not using zip_longest, so we must ensure the list has an even length.
    return zip(iterator, iterator)
