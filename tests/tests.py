#!/usr/bin/env python3

import os
import unittest

from jumble import parse_word_list_file, jumble


class JumbleTests(unittest.TestCase):

    def setUp(self) -> None:
        # change to the dir of this file so we can use the words_test.txt file
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

    def test_dict(self):
        jumble_dict = parse_word_list_file("words_test.txt")

        self.assertIn("dgo", jumble_dict)
        self.assertNotIn("dog", jumble_dict)
        self.assertIn("dog", jumble_dict["dgo"])
        self.assertIn("god", jumble_dict["dgo"])
        self.assertEqual(2, len(jumble_dict["dgo"]))
        self.assertNotIn("robot", jumble_dict)
        self.assertIn("robot", jumble_dict["boort"])
        self.assertEqual(1, len(jumble_dict["boort"]))
        self.assertIn("orb", jumble_dict["bor"])

    def test_jumble(self):
        jumble_dict = parse_word_list_file("words_test.txt")

        self.assertEqual(0, len(jumble(jumble_dict, "laser")))
        self.assertIn("or", jumble(jumble_dict, "bro"))
        self.assertIn("orb", jumble(jumble_dict, "bro"))
        self.assertIn("rob", jumble(jumble_dict, "bro"))
        self.assertNotIn("robot", jumble(jumble_dict, "robot"))
        self.assertEqual(12, len(jumble(jumble_dict, "robot")))


if __name__ == '__main__':
    unittest.main()
