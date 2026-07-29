"""Saitama"""
def main():
    """Saitama"""
    quest1 = int(input())
    quest2 = int(input())
    quest3 = int(input())
    quest4 = int(input())
    po1 = int(input())
    po2 = int(input())
    po3 = int(input())
    po4 = int(input())
    count1 = (quest1 + po1 - 1) // po1
    count2 = (quest1 + po2 - 1) // po2
    count3 = (quest1 + po3 - 1) // po3
    count4 = (quest1 + po4 - 1) // po4
    print(max(count1, count2, count3, count4))
main()
