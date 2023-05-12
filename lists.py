from typing import List
from decorators import currency


fruits = ["apple", "banana", "cherry"]
new_fruits = []

for x in fruits:
    if "a" in x:
        new_fruits.append(x)
print(new_fruits)


def get_data(args=None):
    if args:
        return [1, 2, 3, 6]


lowest = min(get_data() or ["0"])
print(lowest)


# closures


def say():
    greeting = "Hello"

    def world():
        print(greeting)

    return world


fn = say()
print(fn.__code__.co_freevars)

# decorators
# It doesnt cahange the function, it just wraps it


@currency
def net_price(price, tax):
    return price * (1 + tax)


print(net_price(100, 0.05))


def sum_even_numbers(numbers: List[int]) -> int:
    """Given a list of integers, return the sum of all even numbers in the list."""
    return sum(num for num in numbers if num % 2 == 0)