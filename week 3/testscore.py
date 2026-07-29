"""testscore"""
def main():
    """testscore"""
    amount = int(input())
    itam = []
    for _ in range(0, amount):
        score = int(input())
        itam.append(score)
    itam.sort()
    print (itam[-1])
    print (itam.count(itam[-1]))
main()
