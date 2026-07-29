"""สลับตัวเลข"""
def main():
    """สลับตัวเลข"""
    num = input()
    num1 = int(num)
    y = input()
    num2 = int(num[::-1])
    if 10 <= num1 <=99:
        if y =="+":
            print(f"{num} + {num2} = {num1 + num2} ")
        if y =="*":
            print(f"{num} * {num2} = {num1 * num2}")
main()
