"""
File: rational.py
Resources to manipulate rational numbers.
"""

class Rational(object):
    """Represents a rational number."""

    def __init__(self, numer, denom):
        """Constructor creates a number with the given numerator
        and denominator and reduces it to lowest terms."""
        self._numer = numer
        self._denom = denom
        self._reduce()

    def numerator(self):
        """Returns the numerator."""
        return self._numer
  
    def denominator(self):
        """Returns the denominator."""
        return self._denom
   
    def __str__(self):
        """Returns the string representation of the number."""
        return str(self._numer) + "/" + str(self._denom)

    def _reduce(self):
        """Helper to reduce the number to lowest terms."""
        divisor = self._gcd(self._numer, self._denom)
        self._numer = self._numer // divisor
        self._denom = self._denom // divisor

    def _gcd(self, a, b):
        """Euclid's algorithm for greatest common divisor."""
        (a, b) = (max(a, b), min(a, b))
        while b > 0:
            (a, b) = (b, a % b)
        return a

    # Methods for arithmetic and comparisons go here

    def __add__(self, other):
        """Returns the sum of the numbers."""
        newNumer = self._numer * other._denom + \
                   other._numer * self._denom
        newDenom = self._denom * other._denom
        return Rational(newNumer, newDenom)

    def __truediv__(self, other):
        """Returns the result of dividing two Rational numbers using /.
           Use __floordiv__ to overload //."""
        pass

    def __lt__(self, other):
        """Returns True if self < other."""
        extremes = self._numer * other._denom
        means = other._numer * self._denom
        return extremes < means

    def __eq__(self, other):
        """Tests self and other for equality."""
        if type(self) != type(other):
            return False
        else:
            return self._numer == other._numer and \
                   self._denom == other._denom

    def __ne__(self, other):
        """Tests self and other for inequality."""
        return not self == other

    def __gt__(self, other):
        """Returns True if self > other."""
        #return (not self < other) and (not self == other)
        extremes = self._numer * other._denom
        means = other._numer * self._denom
        return extremes > means

    def __le__(self, other):
        """Returns True if self <= other."""
        #return (self < other) or (self == other)
        extremes = self._numer * other._denom
        means = other._numer * self._denom
        return extremes <= means

    def __ge__(self, other):
        """Returns True if self >= other."""
        #return (self > other) or (self == other)
        extremes = self._numer * other._denom
        means = other._numer * self._denom
        return extremes >= means
        
        



