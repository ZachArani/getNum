from collections import deque
from random import uniform


class RandomGen:
    """ RandomGen is the class that handles the generation of random number"""

    def __init__(self):
        self.queue = deque()

    def get_num(self):
        """ This method is for getting the random number.
        This method, uses the deque data structure to keep track of the last 750 generated
        random number.

        :returns Unique from last 750 generation, a random number from 1 to 1 Million.
        """
        num = self.get_random_num()
        while num not in self.queue:
            num = self.get_random_num()
            if len(self.queue) >= 749:
                self.queue.pop()
            self.queue.append(num)
        return num

    @staticmethod
    def get_random_num():
        """ Uses the generic random generator to get a random num between 1 to 1 M
        :returns A random number between 1 and 1 Million.
        """
        return round(uniform(1, 1000000))
