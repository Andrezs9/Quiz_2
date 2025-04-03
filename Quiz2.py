# Quiz 2 (B)
casos=int(input())

dentro=0
fuera=0 

for i in range (casos):
    x=int(input(""))
    if x >=10 and x <=20:
        dentro=dentro + 1
    else:
        fuera = fuera + 1
print (f"{dentro} in")
print (f"{fuera} out")
