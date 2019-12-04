import re


class Numbers:
    @staticmethod
    def increasing(number):
        a = list(str(number))
        a.sort()
        a = map(str, a)
        return ''.join(a) == str(number)

    @staticmethod
    def duplicate_number(number):
        match = re.search(r'(\d)\1', str(number))
