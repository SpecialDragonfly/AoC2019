import re

from collections import Counter

class Numbers:
    @staticmethod
    def increasing(number):
        a = list(str(number))
        a.sort()
        a = map(str, a)
        return ''.join(a) == str(number)

    @staticmethod
    def duplicate_number(number):
        return re.search(r'(\d)\1', str(number)) is not None

    @staticmethod
    def counter_thing(number):
        return Counter(list(str(number))).values()