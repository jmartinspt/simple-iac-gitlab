"""
Unit testing of the automatic batch processing application
"""
import unittest
from src.app import squares
 
 
class AppTests(unittest.TestCase):
    def test_app(self):
        """Simple Tests"""
        self.assertEqual(squares(10), 100)
        self.assertNotEqual(squares(2), 5)
    
    def test_errors(self):
        """Check that method fails when parameter type is not numeric"""
        with self.assertRaises(TypeError):
            squares("foo")
    
    def suite():
        _suite = unittest.TestSuite()
        _suite.addTest(AppTests('test_app'))
        _suite.addTest(AppTests('test_errors'))
        return _suite
    
    
    if __name__ == "__main__":
        runner = unittest.TextTestRunner()
        runner.run(suite())