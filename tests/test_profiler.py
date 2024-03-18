
# Example test in test_profiler.py
import unittest
from dataprocprofiler.profiler import profile_function

class TestProfiler(unittest.TestCase):
    def test_profiler_decorator(self):
        @profile_function
        def sample_function():
            return sum([i for i in range(10000)])
        
        result = sample_function()
        self.assertEqual(result, 49995000)

if __name__ == '__main__':
    unittest.main()
