import string

kata = []

def init():
	a = string.ascii_lowercase
	for i in range(len(a)):
		kata.append(a[i])

init()
while (True):
	nama = str(input("nama: "))
	for i in kata:
		if i in nama: break
		else:
			continue
	break


print(nama)
