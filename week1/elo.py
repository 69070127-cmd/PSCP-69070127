"""Elo"""
ra = int(input())
rb = int(input())
x = input("")
if x == "A":
    print(f"{1 / (1 + 10 ** ((rb - ra) / 400)):.2f}")
else:
    print(f"{1 /(1 + 10 ** ((ra - rb) / 400)):.2f}")
