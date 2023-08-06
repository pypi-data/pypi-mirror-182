import difflib

red = lambda text: f"\033[38;2;255;0;0m{text}\033[38;2;255;255;255m"
green = lambda text: f"\033[38;2;0;255;0m{text}\033[38;2;255;255;255m"
white = lambda text: f"\033[38;2;255;255;255m{text}\033[38;2;255;255;255m"

red_html = lambda text: f'<span style="color: red">{text}'
green_html = lambda text: f'<span style="color: green">{text}'
black_html = lambda text: f'<span style="color: black">{text}'


def parse_console_diff(old, new):
    result = ""
    codes = difflib.SequenceMatcher(a=old, b=new).get_opcodes()

    for code in codes:
        if code[0] == "equal":
            result += white(old[code[1] : code[2]])
        elif code[0] == "delete":
            result += red(old[code[1] : code[2]])
        elif code[0] == "insert":
            result += green(new[code[3] : code[4]])
        elif code[0] == "replace":
            result += red(old[code[1] : code[2]]) + green(new[code[3] : code[4]])
    return result


def parse_html_diff(old, new):
    result = ""
    codes = difflib.SequenceMatcher(a=old, b=new).get_opcodes()

    for code in codes:
        if code[0] == "equal":
            result += black_html(old[code[1] : code[2]])
        elif code[0] == "delete":
            result += red_html(old[code[1] : code[2]])
        elif code[0] == "insert":
            result += green_html(new[code[3] : code[4]])
        elif code[0] == "replace":
            result += red_html(old[code[1] : code[2]]) + green_html(
                new[code[3] : code[4]]
            )
    return result
