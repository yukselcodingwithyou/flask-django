import unittest
from hello import hello_flask


class HelloTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.tester = hello_flask.test_client(self)

    def test_hello(self):
        response = self.tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')

    def test_hello_name_success(self):
        response = self.tester.get("/name", content_type="html/text")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello name!')

    def test_hello_name_fail(self):
        response = self.tester.get("/not_name", content_type="html/text")
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.data, b'Hello name!')