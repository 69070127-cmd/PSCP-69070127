"""minvalue"""
def main():
    """minvalue"""
    amount = int(input())
    item = []
    for _ in range(0, amount):
        value = int(input())
        item.append (value)
    item.sort()
    print (item[0])
main()
