def add_words(text: str, is_paragraph: bool, is_start: bool, is_line: bool,
              is_bold: bool, is_italic: bool, spaces: int) -> str:
    star_num = 0
    star_num = star_num + 1 if is_italic else star_num
    star_num = star_num + 2 if is_bold else star_num
    stars = '*' * star_num
    if is_paragraph:
        return f'{"\n" if is_start else ""}{"&nbsp;" * spaces}{stars}{text.strip()}{stars}\n'
    elif is_line:
        return f'{"&nbsp;" * spaces}{stars}{text.strip()}{stars}  \n'
    else:
        return f'{" " * spaces}{stars}{text.strip()}{stars}'
