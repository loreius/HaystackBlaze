# test_haystackblaze.py
"""
Tests for HaystackBlaze module.
"""

import unittest
from haystackblaze import HaystackBlaze

class TestHaystackBlaze(unittest.TestCase):
    """Test cases for HaystackBlaze class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HaystackBlaze()
        self.assertIsInstance(instance, HaystackBlaze)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HaystackBlaze()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
