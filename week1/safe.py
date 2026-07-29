"""safe"""
def main():
    """safe"""
    X = str(input())
    Y = int(input())
    if X == "H" and Y == 4567:
        print ("safe unlocked")
    elif X == "H":
        print ("safe locked - change digit")
    elif Y == 4567:
        print ("safe locked - change char")
    else:
        print ("safe locked")
main()
