import random


def generate_coupon(lower, upper, number):
    coupon_numbers = set([])
    for i in range(number):
        coupon = random.randint(lower, upper)
        coupon_numbers.add(coupon)

    return  coupon_numbers


if __name__ == "__main__":
    lower_range = int(input("Enter the lower range: "))
    upper_range = int(input("Enter the upper range: "))
    number = int(input("Enter number of unique coupon numbers to generate: "))
    list = generate_coupon(lower_range, upper_range, number)
    print(list)
