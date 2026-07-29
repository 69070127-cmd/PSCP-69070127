"""Bill"""
def main():
    """Bill"""
    price = int(input())
    service = price * 0.10
    if service < 50:
        service = 50
    elif service > 1000:
        service = 1000
    price2 = price+service
    vat = price2 * 0.07
    X = price2 + vat
    print (f"{X:.2f}")
main()
