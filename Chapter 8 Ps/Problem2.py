def convert(f):
    return 5*(f-32)/9

f=int(input("Enter Temp in F : "))
c = convert(f)
print(f"{round(c,2)}°C")