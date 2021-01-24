class FizzBuzz:
    def game(num):
        
        if not str(num).isnumeric():
            return "ValueError"

        if((int(num)%15) == 0):
            return "FizzBuzz"
        elif((int(num)%3) == 0):
            return "Fizz"
        elif((int(num)%5) == 0):
            return "Buzz"
        else:
            return "None"