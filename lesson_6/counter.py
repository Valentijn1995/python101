from unittest import TestCase
import unittest

class Counter:

    def __init__(self, initial_count=0):
        '''
        Create a new Counter. The initial count is
        zero by default.
        '''
        self._count = initial_count
    
    def increase(self):
        '''
        Increase the count by one.
        '''
        self._count = self._count + 1

    def decrease(self):
        '''
        Decrease the count by one.
        '''
        if self._count > 0:
            self._count = self._count - 1
        else:
            raise RuntimeError("The count cannot be a negative value")
    
    def get_count(self):
        '''
        Get the total count amount.
        '''
        return self._count


class TestCounter(TestCase):

    def setUp(self):
        '''
        The method is called before every test case.
        It allows you to initialize the veriables you
        need during the test cases.
        '''
        self._counter = Counter()

    def test_increase(self):
        '''
        Tests if counter is increased when the
        increase method is called. 
        '''
        count_before_inc = self._counter.get_count()
        self._counter.increase()
        count_after_inc = self._counter.get_count()
        self.assertEqual(count_before_inc + 1, count_after_inc)

    def test_decrease(self):
        '''
        Test if counter is descreased when the
        descrease method is called.
        '''
        self._counter.increase()
        count_before_dec = self._counter.get_count()
        self._counter.decrease()
        count_after_dec = self._counter.get_count()
        self.assertEqual(count_before_dec - 1, count_after_dec)

    def test_decrease_failure(self):
        '''
        Test if the counter raises the proper
        exception when the count is decreased
        below zero.
        '''
        with self.assertRaises(RuntimeError):
            self._counter.decrease()

    def tearDown(self):
        '''
        This method is called after every
        test case. It allows you to cleanup.
        '''
        self._counter = None


if __name__ == "__main__":
    unittest.main()

