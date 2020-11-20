from fractions import Fraction
a=int(input('Numaratorul primei fractii:'))
b=int(input('Numitorul primei fractii:'))
c=int(input('Numaratorul celei de a doua fractie:'))
d=int(input('Numitorul celei de a doua fractie:'))
s=Fraction(a, b)+ Fraction(c, d)
p=Fraction(a, b)* Fraction(c, d)
print(f'a) suma este {s}, b) produsul este {p}')