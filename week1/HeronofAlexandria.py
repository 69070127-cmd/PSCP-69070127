"""Heronformula"""
A = float(input())
B = float(input())
C = float(input())
S = (A + B + C) / 2
D = (S * (S - A) * (S - B) * (S - C)) ** 0.5
print (f"{D:.3f}")
