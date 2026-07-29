"""หารลงตัว"""
def main():
    """หารลงตัว"""
    num1 = int(input())
    num2 = int(input())
    de = num1 % num2
    if not de:
        print ("yes")
    else:
        print ("no")
main()
