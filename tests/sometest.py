import unittest2
from sparky.dataIO import *

from sparktestingbase.testcase import SparkTestingBaseTestCase, SparkTestingBaseReuse


class HelloWorldTest(SparkTestingBaseReuse):
    """Simple hell world example test."""

    def test_basic(self):
        """Test a parallelize & collect."""
        input = ["hello world"]
        rdd = self.sc.parallelize(input)
        result = rdd.collect()
        assert result == input

    def test_samecontext_1(self):
        """Set a system property"""
        self.sc.setLocalProperty("pandas", "123")

    def test_samecontext_2(self):
        """Test that we have the same context."""
        assert self.sc.getLocalProperty("pandas") == "123"

    def test_samecontext_3(self):
        """Test that we have the same context 3."""
        r = print_from_dataio()
        assert r == 'hello123'


if __name__ == "__main__":
    unittest2.main()

