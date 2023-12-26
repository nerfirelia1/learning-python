zegary = []
temperatury = []

with open("dane_systemy1.txt") as s1:
    for line in s1:
        z, t = line.split()
        zegary.append(int(z, 2))
        temperatury.append(int(t, 2))

zegary2 = []
temperatury2 = []

with open("dane_systemy2.txt") as s2:
    for line in s2:
        z, t = line.split()
        zegary2.append(int(z, 4))
        temperatury2.append(int(t, 4))

zegary3 = []
temperatury3 = []

with open("dane_systemy3.txt") as s3:
    for line in s3:
        z, t = line.split()
        zegary3.append(int(z, 8))
        temperatury3.append(int(t, 8))

# zad.1
t1 = min(temperatury)
t2 = min(temperatury2)
t3 = min(temperatury3)

with open("wyniki58.txt", "w") as file:
    file.write("Zad.1.\n")
    file.write("-" + bin(t1)[3:] + "\n")
    file.write("-" + bin(t2)[3:] + "\n")
    file.write("-" + bin(t3)[3:] + "\n")

# zad.2
ile2 = 0
godz = 12
for i in range(len(zegary)):
    if zegary[i] != godz and zegary2[i] != godz and zegary3[i] != godz:
        ile2 += 1
    godz += 24

with open("wyniki58.txt", "a") as file:
    file.write("Zad.2\n")
    file.write(str(ile2) + "\n")

# zad.3
ile3 = 1
maxi = temperatury[0]
maxi2 = temperatury2[0]
maxi3 = temperatury3[0]

for i in range(1, len(temperatury)):
    rekord = False
    if maxi < temperatury[i]:
        maxi = temperatury[i]
        rekord = True
    if maxi2 < temperatury2[i]:
        maxi2 = temperatury2[i]
        rekord = True
    if maxi3 < temperatury3[i]:
        maxi3 = temperatury3[i]
        rekord = True
    if rekord:
        ile3 += 1

with open("wyniki58.txt", "a") as file:
    file.write("Zad.3\n")
    file.write(str(ile3) + "\n")
