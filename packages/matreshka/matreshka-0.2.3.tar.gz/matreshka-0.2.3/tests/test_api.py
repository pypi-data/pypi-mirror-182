import unittest
import re


class MatreshkaTestCase(unittest.TestCase):
    def test_search_secret_key(self):
        tmpl = r'\bEVOLUTION\b'
        self.assertTrue(re.search(tmpl, 'Кодовое слово: EVOLUTION'))

# TODO
    # Загрузить метод для тестирования.
    # Распаковать архив.



