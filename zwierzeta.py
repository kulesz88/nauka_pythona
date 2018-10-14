file = open("zwierzeta.txt", "r")

zwierzeta = []

for l in file:
    zwierzeta.append(l.strip())
file.close()

#print(zwierzeta)

while True:
    pytanie = raw_input("Czy chcesz dodac zwierze: ")
    if pytanie == 'yes':
        nowe_zwierze = raw_input('Podaj zwierze: ')
        zwierzeta.append(nowe_zwierze)
    else:
        break

#print(zwierzeta)

out = open("zwierzeta2.txt", "w")
for z in zwierzeta:
    out.write(z + "\n")
out.close()
