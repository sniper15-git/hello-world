# test_app.py
import unittest
from app import hello_world

class TestApp(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello,World!")

    if_name_ == '_main_': # type: ignore
    unittest.main()