def halo_dunia(Halo_Dunia):
    print (Halo_Dunia)

halo_dunia("hay") 


def ucapan(Anda_ada_pada_fungsi):
	print (Anda_ada_pada_fungsi)

ucapan("Anda ada pada fungsi")


def perkalian(a,b):
	c = a*b 
	return c

# Program Utama
print( perkalian(5,10))


def contohScope(X): 
	X = 10
	print (X)

# program utama
X = 30
print (contohScope(X)) 
