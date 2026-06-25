'''
1 inche = 2.54cm
'''
def inche_to_cms(n):
    return n*2.54

n=float(input("Enter in Inches : "))

a = inche_to_cms(n)

print(f"{n} Inches = {a} cm")