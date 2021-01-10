from typing import List
from docx2python import docx2python


class SectionBase:
    def __init__(self):
        self.heading = None
        self.paragraphs = []

    def strip_pars(self):
        for i in range(len(self.paragraphs)):
            p = self.paragraphs[i]
            start = 0

            while start < len(p) and not p[start].isalpha():
                start += 1

            self.paragraphs[i] = p[start:]


class Subsection(SectionBase):
    def __init__(self, pars: List[str]):
        super().__init__()
        self.subtext = None
        self.create(pars)

    def create(self, pars: List[str]):
        # Find index of first letter in first paragraph
        first = pars[0]
        start = 0
        while start < len(first) and not first[start].isalpha():
            start += 1

        dash = first.find('-')
        if (dash != -1 and dash < start) or len(pars) < 2:
            raise ValueError('This is not a valid subsection')
        else:
            self.heading = pars[0].title().replace('\t', '')

        # Find index of first letter in second paragraph
        second = pars[1]
        start = 0
        while start < len(second) and not second[start].isalpha():
            start += 1

        dash = second.find('-')
        if dash == -1 or dash > start:
            self.subtext = second[start:]
            self.paragraphs = pars[2:]
        else:
            self.paragraphs = pars[1:]

        self.strip_pars()

    def __str__(self):
        ret = f'{self.heading}\n'

        if self.subtext:
            ret += f'\t{self.subtext}\n\t\t- '
        else:
            ret += '\t\t- '

        ret += '\n\t\t- '.join(self.paragraphs)
        return ret


class Section(SectionBase):
    def __init__(self, pars: List[str]):
        super().__init__()
        self.subsections = []
        self.create(pars)

    def create(self, pars: List[str]):
        self.heading = pars[0].title().replace('\t', '')
        self.paragraphs = [self.parse_paragraph(p) for p in pars[1:]]
        self.create_subsections()
        self.strip_pars()

    def create_subsections(self):
        split_indices = [i for i in range(len(self.paragraphs)) if self.paragraphs[i] == '']

        if len(split_indices) == 0:
            try:
                self.subsections.append(Subsection(self.paragraphs))
            except ValueError:
                return
            else:
                return

        i = 0
        while i < len(split_indices):
            if i == 0:
                self.subsections.append(Subsection(self.paragraphs[0:split_indices[0]]))

            if i + 1 == len(split_indices):
                self.subsections.append(Subsection(self.paragraphs[split_indices[i] + 1:]))
            else:
                self.subsections.append(Subsection(self.paragraphs[split_indices[i] + 1:split_indices[i + 1]]))

            i += 1

    @staticmethod
    def parse_paragraph(par: str):
        # Return an empty string if the paragraph is empty or contains only a tab escape
        if par.strip() in ['', '\t']:
            return ''

        # Otherwise, return the original itself
        return par

    def __str__(self):
        ret = f'{self.heading}\n\t- '

        if len(self.subsections) == 0:
            ret += '\n\t- '.join(self.paragraphs)
        else:
            ret += '\n\t'.join([str(s) for s in self.subsections])

        return ret


class Resume:
    def __init__(self, path: str):
        self.sections = []

        raw = docx2python(path).body[0][0][0]

        chunks = self.chunk_raw_body(raw)
        for chunk in chunks[1:]:
            self.sections.append(Section(chunk))

    def __str__(self):
        return '\n\n'.join([str(s) for s in self.sections])

    @staticmethod
    def chunk_raw_body(body: List[str]):
        boundaries = []
        num_pars = len(body)

        i = 0
        while i < num_pars:
            current = []
            while i < num_pars and body[i] in ['', '\t']:
                current.append(i)
                i += 1

            if len(current) > 1:
                if len(boundaries) == 0:
                    boundaries.append([0, current[0]])
                else:
                    boundaries[-1][1] = current[0]

                boundaries.append([current[-1] + 1, None])

            i += 1

        chunks = []
        for start, stop in boundaries:
            if stop:
                chunks.append(body[start:stop])
            else:
                chunks.append(body[start:])

        return chunks
