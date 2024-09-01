import unittest

from src.main.python.transformer.transformer import import_file_lines, to_csv, import_file_string, replace_chars, \
    tokenize


class MyTestCase(unittest.TestCase):

    def test_import_lines(self):
        lines = import_file_lines("../../resources/testfile_1.txt")
        for line in lines:
            print(line)

    def test_import_string(self):
        import_file_string("../../resources/testfile_1.txt")

    def test_replace_chars(self):
        (self.assertEqual("*ʔ-ga2 'mute/dumb/stupid'",
         replace_chars("*÷-gaTM (PLB) 'mute/dumb/\nstupid' {57, 165}")))

    def test_tokenize(self):
        string = import_file_string("../../resources/testfile_2.txt")
        tokens = tokenize(string)
        print(tokens)
        self.assertEqual(10, len(tokens))

    def test_to_csv(self):
        self.assertEqual("*ʔ; \n", to_csv("*÷"))
        self.assertEqual("*ʔa ~ *ga; \n", to_csv("*÷a & *ga"))
        self.assertEqual("*ʔ-ga2;mute/dumb/stupid\n", to_csv("*÷-gaTM (PLB) 'mute/dumb/\nstupid' {57, 165}"))
        self.assertEqual("*ʔaŋ- ~ *ʔak-;noun prefix\n", to_csv("*÷a≥- & *÷ak- 'noun pre-\nfix' {522}"))

if __name__ == '__main__':
    unittest.main()
