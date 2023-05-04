x = int(input('Geben Sie Zahl 1 ein: '))
y = int(input('Geben Sie Zahl 2 ein: '))

while y==0:
    print("Division durch 0 nicht möglich")
    y = int(input("Geben Sie Zahl 2 erneut ein"))
print("Das Ergebnis der Division ist: "x/y)