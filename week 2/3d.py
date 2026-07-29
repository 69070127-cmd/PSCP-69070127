"""3d"""
def main():
    """3d"""
    X1,Y1,Z1 = map(int ,input().split())
    X2,Y2,Z2 = map(int ,input().split())
    d = (((X1 - X2) ** 2) + ((Y1 - Y2) ** 2) + ((Z1 - Z2) ** 2)) ** 0.5
    print (f"{d:.2f}")
main()
