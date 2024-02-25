#number = (input("Enter a number: "))
#digit = number % 2 != 0
#def odd_numbers(number: str) -> str:
#if number % 2 != 0:
    # print(number)

def bigger_odds(numbers):
    #return int (max([number for number in numbers if number % 2 != 0])
    return max(filter(lambda n: int(n) % 2 == 1, numbers))

