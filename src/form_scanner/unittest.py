import unittest
from unittest.mock import patch
from requests.exceptions import HTTPError
import main  # assuming your function is in a file named main.py

class TestScrapeUrl(unittest.TestCase):
    def setUp(self):
        self.valid_url = 'https://www.example.com'
        self.non_existent_url = 'https://www.nonexistentwebsite.com'
        self.http_error_url = 'https://www.httperror.com'

    @patch('requests.get')
    def test_scrape_valid_url(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = '<html><body><main><h1>Test Title</h1></main></body></html>'
        result = main.scrape_url(self.valid_url)
        self.assertEqual(result['page_title'], 'Test Title')

    @patch('requests.get')
    def test_scrape_non_existent_url(self, mock_get):
        mock_get.return_value.status_code = 404
        result = main.scrape_url(self.non_existent_url)
        self.assertEqual(result['error'], '404 Not Found')

    @patch('requests.get')
    def test_scrape_http_error(self, mock_get):
        mock_get.side_effect = HTTPError('HTTP Error occurred')
        result = main.scrape_url(self.http_error_url)
        self.assertEqual(result['error'], 'HTTP error: HTTP Error occurred')

if __name__ == '__main__':
    unittest.main()