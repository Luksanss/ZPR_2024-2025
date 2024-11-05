A = int(input("strana a: "))
B = int(input("strana b: "))
C = int(input("strana c: "))


if (A + B <= C):
    print("Neni trojuhelnik")
elif (A + C <= B):
    print("Neni trojuhelnik")
elif (B + C <= A):
    print("Neni trojuhelnik")
else:
    print("Trojuhelnik")