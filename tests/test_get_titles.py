import json
import unittest

from youtube_api import get_titles


class TestGetTitles(unittest.TestCase):
    def setUp(self):
        with open('tests/fixtures/sample_search.json', 'r', encoding='utf-8') as f:
            self.sample = json.load(f)

    def test_returns_titles(self):
        expected = ['first video', 'second video']
        self.assertEqual(get_titles(self.sample), expected)

    def test_missing_next_page_token(self):
        data = dict(self.sample)
        data.pop('nextPageToken', None)
        expected = ['first video', 'second video']
        self.assertEqual(get_titles(data), expected)


if __name__ == '__main__':
    unittest.main()
