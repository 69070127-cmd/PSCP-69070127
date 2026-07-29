"""color"""
def main():
    """color"""
    color1 = input()
    color2 = input()
    if {color1, color2} == {"Red", "Yellow"}:
        print("Orange")
    elif {color1, color2} == {"Red", "Blue"}:
        print("Violet")
    elif {color1, color2} == {"Yellow", "Blue"}:
        print("Green")
    else:
        print("Error")
main()
