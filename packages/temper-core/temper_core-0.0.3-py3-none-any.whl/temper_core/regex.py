import re
import temper_core
import typing


def compiled_regex_compiled_find(_, compiled: re.Pattern, text: str, regex_refs):
    match = compiled.search(text)
    if match is None:
        return temper_core.NO_RESULT
    Match = regex_refs.match.__class__
    Group = regex_refs.match.groups[0].__class__
    groups = match.groupdict()
    # Python indices are already in code points.
    full = () if "full" in groups else (Group("full", match.group(), match.start()),)
    groups = full + tuple(
        Group(name, value or "", match.start(name)) for (name, value) in groups.items()
    )
    return Match(groups)


def compiled_regex_compiled_found_in(_, compiled: re.Pattern, text: str):
    return compiled.search(text) is not None


def compiled_regex_compile_formatted(_, formatted: str):
    return re.compile(formatted, re.ASCII)


def regex_formatter_push_capture_name(_, out: typing.List[str], name: str):
    out.append(rf"?P<{name}>")


def regex_formatter_push_code_to(
    _, out: typing.List[str], code: int, insideCodeSet: bool
):
    # Ignore insideCodeSet for now.
    # TODO(tjp, regex): Get fancier, including with work in Temper.
    out.append(rf"\U{code:08x}")
