"""saeson"""
def main():
    """saeson"""
    m = int(input())
    d = int(input())
    s = ()
    if m in [1,2] or (m == 3 and d < 21):
        s = "winter"
    elif m == 3 and d > 20:
        s = "spring"
    elif m in [4,5] or (m == 6 and d < 21):
        s = "spring"
    elif m == 6 and d > 20:
        s = "summer"
    elif m in [7,8] or (m == 9 and d < 21):
        s = "summer"
    elif m == 9 and d > 20:
        s = "fall"
    elif m in [10,11] or (m == 12 and d < 21):
        s = "fall"
    elif m == 12 and d > 20:
        s = "winter"
    print (s)
main()
