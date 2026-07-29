"""rabit2"""
def main():
    """rabit2"""
    width, langth, floor = map(int ,input().split())
    price = int(input())
    x = ((width * 2) + (langth * 2)) * floor
    print (x)
    print (x * price)
main()
