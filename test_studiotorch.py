# test_studiotorch.py
"""
Tests for StudioTorch module.
"""

import unittest
from studiotorch import StudioTorch

class TestStudioTorch(unittest.TestCase):
    """Test cases for StudioTorch class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = StudioTorch()
        self.assertIsInstance(instance, StudioTorch)
        
    def test_run_method(self):
        """Test the run method."""
        instance = StudioTorch()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
