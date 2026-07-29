"""แลกเปลี่ยนเหรียญ"""
def main():
    """แลกเปลี่ยนเหรัยญ"""
    value = int(input())
    ten = value // 10
    tende = value % 10
    five = tende // 5
    fivede = tende % 5
    two = fivede // 2
    twode = fivede % 2
    one = twode // 1
    print ("10 = "+ str(ten))
    print ("5 = "+ str(five))
    print ("2 = "+ str(two))
    print ("1 = "+ str(one))
main()
