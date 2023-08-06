from .helpers import add_words


class MdMaker:
    def __init__(self, filename: str, mode: str) -> None:
        self.filename = filename
        self.mode = mode
        self.content = ''

    def save_file(self):
        with open(self.filename, self.mode) as f:
            f.write(self.content)

    def add_header(self, level: int, text: str):
        self.content += f'{"\n" if self.content else ""}{"#" * level} {text.strip()}\n'

    def add_paragraph(self, text: str, is_bold: bool = False,
                      is_italic: bool = False, indents: int = 0):
        is_start = len(self.content) > 0
        self.content += add_words(text, True, is_start, False,
                                  is_bold, is_italic, indents)

    def add_text(self, text: str, is_bold: bool = False,
                 is_italic: bool = False, spaces: int = 1):
        self.content += add_words(text, False, False, False,
                                  is_bold, is_italic, spaces)

    def add_line(self, text: str, is_bold: bool = False,
                 is_italic: bool = False, indents: int = 0):
        self.content += add_words(text, False, False,
                                  True, is_bold, is_italic, indents)
