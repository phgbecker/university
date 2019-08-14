class Fibonacci(object):

    @staticmethod
    def apply(number):
        return number if (number < 2) else (Fibonacci.apply(number - 1) + Fibonacci.apply(number - 2))
