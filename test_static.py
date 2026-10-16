"""Dependency-free structural checks for the first mobile quiz MVP."""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

PAGE = Path(__file__).with_name("index.html")

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.buttons = 0
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "button":
            self.buttons += 1

class QuizSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = PAGE.read_text(encoding="utf-8")
        cls.parsed = PageParser()
        cls.parsed.feed(cls.source)

    def test_required_controls(self):
        self.assertTrue({"mode-exam", "mode-all", "count", "score", "question", "periodic-table", "options", "feedback", "next"} <= self.parsed.ids)
        self.assertGreaterEqual(self.parsed.buttons, 1)

    def test_mobile_viewport(self):
        self.assertIn('name="viewport"', self.source)

    def test_quiz_flow_present(self):
        for function in ("newQuestion", "answer", "shuffle"):
            self.assertIn("function " + function + "(", self.source)
        self.assertIn("aria-live", self.source)

    def test_full_main_periodic_table_grid(self):
        self.assertIn("repeat(18", self.source)
        self.assertIn("repeat(7", self.source)
        self.assertIn("for(let p=1;p<=7;p++)", self.source)
        self.assertIn("for(let g=1;g<=18;g++)", self.source)
        for symbol in ("H", "He", "Li", "Ne", "Na", "Ar", "K", "Kr", "Cs", "Rn", "Fr", "Og"):
            self.assertRegex(self.source, r"\['" + symbol + r"','")

    def test_only_direct_horizontal_neighbors_are_questions(self):
        self.assertIn("byPosition.get(e.p+'-'+(e.g+dir))", self.source)
        self.assertIn(".filter(q=>q.answer)", self.source)

    def test_answer_is_revealed_after_response(self):
        self.assertIn("renderTable(true)", self.source)
        self.assertIn("answer-cell", self.source)

    def test_two_difficulty_modes(self):
        self.assertIn("difficulty='exam'", self.source)
        self.assertIn("function activeQuestions()", self.source)
        self.assertIn("function setDifficulty(next)", self.source)
        self.assertIn("q.element.p>=2&&q.element.p<=4", self.source)

    def test_high_contrast_question_and_answer_colors(self):
        self.assertIn("background:#ffd84d", self.source)
        self.assertIn("background:#087f5b", self.source)

if __name__ == "__main__":
    unittest.main()
