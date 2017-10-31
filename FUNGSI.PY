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

# fungsi mulai di sini 
def swap(x, y):
	print ("Dalam fungsi:") 
	print ("\tSebelum proses:") 
	print ("\t\tNilai x", x) 
	print ("\t\tNilai y", y)
	z = x 
	x = y 
	y = z
	print ("\tSetelah proses:") 
	print ("\t\tNilai x", x) 
	print ("\t\tNilai y", y)

# program utama mulai di sini 
x = 12
y = 3
print ("Sebelum memanggil fungsi, x bernilai", x) 
print ("Sebelum memanggil fungsi, y bernilai", y) 
swap(x,y)
print ("Setelah memanggil fungsi, x bernilai", x)
print ("Setelah memanggil fungsi, y bernilai", y)

def faktorial(nilai):
		if nilai <= 1:
			return 1 
		else:
 

			return nilai * faktorial(nilai - 1) 

#Program utama
for i in range(11):
	print (i, faktorial(i)) 

def perkalian(a,b):
	c = a*b 
	return c

# Program Utama
print( perkalian(5,10))

# Fungsi Fibonacci 
def fibonacci(n): 
	if n < 0:
		print ("Tidak ada bilangan yang bernilai negatif")
	if n == 0 or n == 1:
		return n 
	else:
		return fibonacci(n-1) + fibonacci(n-2) 
 
# Program utama
# nilai = int(raw_input("Masukkan sebuah bilangan : " ))
# hasil = fibonacci(nilai)
print (20,6765) 

def perkalian(x, y):
	z = x * y
	print ("Nilai x =",x)
	print ("Nilai y =",y) 
	print ("x * y =",z)

# program utama mulai di sini 
	perkalian = (10*2)
	print (perkalian (y = 15,x = 5))
