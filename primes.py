"""Primes"""

class Primes:
    """Primes generator"""

    integers = {}

    def load(self, end, begin = 0) -> tuple:
        """Loads tuple with definition if integer is an prime number
        Args:
            end (int):   end of range
            begin (int): begin of range
        Returns:
            tuple
        """
        for i in range(0, end + 1):
            self.integers[i] = 1
        self.integers[0] = self.integers[1] = 0
        for j in range(0, end + 1):
            if self.integers[j]:
                for i in range(j*2, end + 1, j):
                    self.integers[i] = 0

    def generate(self, end, begin = 0) -> tuple:
        """Generates tuple of primes from defined range
        Args:
            end (int):   end of range
            begin (int): begin of range
        Returns:
            tuple
        """
        self.load(end, begin)
        result = []
        for i in self.integers:
            if self.integers[i] and i >= begin:
                result.append(i)
        return result

    def isPrimes(self, number) -> bool:
        """Checks if integer is an prime number
        Args
            number (int)
        Returns:
            bool
        """
        self.load(number, number)
        return self.integers[number]

if __name__ == '__main__':
    print(Primes().__doc__)
