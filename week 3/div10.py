"""หาร10"""
def main():
    """หาร10"""
    num = int(input())
    num1 = num // 10
    item = [0]
    x = 10
    for _ in range (num1):
        item.append(x)
        x += 10
    print (*item[::-1])
main()
