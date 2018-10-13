rowery = ['unibike', 'romet', 'accent', 'skladak']

print(rowery[0])
print(rowery[1])

print("\n")

for s in rowery:
    print(s)

print("\n")

for idx in range( len(rowery) ) :
    print("idx: " + str(idx) + " : " + rowery[idx])
print("\n")
l = rowery[2:]
for s in rowery[2:3]:
    print(s)

nazwa_roweru = "unibike"
print(nazwa_roweru[:2])
print(nazwa_roweru[1:])


if len(nazwa_roweru) > 0:
    ostatnia_litera = nazwa_roweru[-1]
    print(ostatnia_litera)
else:
    print("Pusty string")

print("\n")

rowery = ['unibike', 'romet', 'accent', 'skladak', '']
for nazwa in rowery:
    if len(nazwa) > 0:
        ostatnia_litera = nazwa[-1]
        print(ostatnia_litera)
    else:
        print("Pusty string")

print("\n")

rowery = ['unibike', 'romet', 'accent', 'skladak']
bike = raw_input('Enter name of your bike: ')
if bike in rowery:
    print(bike)
else:
    print("Nie ma takiego roweru")
