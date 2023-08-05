class Fizzbuzz:
    @staticmethod
    def fizzBuzz(num):
        string = ''
        if num % 3 == 0:
            string += 'Fizz'
        if num % 5 == 0:
            string += 'Buzz'
        if string == '':
            string += str(num)
        return string if string else f'{num}'


if __name__ == '__main__':
    for i in range(0, 100):
        result = Fizzbuzz.fizzBuzz(i)
        print(result)

