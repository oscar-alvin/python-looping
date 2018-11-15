import os
import sys

def segitiga():
	os.system('cls')
	a = int(input("masukkan sebuah bilangan : "))
	print("LOOPING KE 1")
	for i in range(0, a, 1):
		for j in range(0, i, 1):
			sys.stdout.write("*")
		print("")
	print("LOOPING KE 2")
	for i in range(a, 0, -1):
		for j in range(0, i, 1):
			sys.stdout.write("*")
		print("")
	print("LOOPING KE 3")
	for i in range(a, 0, -1):
		for j in range(0, a-i, 1):
			sys.stdout.write(" ")
		for k in range(0, 2*i-1, 1):
			sys.stdout.write("*")
		print("")

def kotak():
	os.system('cls')
	a = int(input("masukkan sebuah bilangan : "))
	print("")
	for i in range(0, a, 1):
		for j in range(0, a, 1):
			sys.stdout.write("*")
		print("")
		print("")

def kalkulator():
	os.system('cls')
	print("PROGRAM KALKULATOR PYTHON")
	print("===============================")
	a = int(input("Masukkan angka 1 : "))
	b = int(input("Masukkan angka 2 : "))
	print("Hasil penjumlahan {} + {} = {}".format(a, b, a+b))
	print("Hasil pengurangan {} - {} = {}".format(a, b, a-b))
	print("Hasil perkalian   {} * {} = {}".format(a, b, a*b))
	print("Hasil pembagian   {} - {} = {}".format(a, b, a/b))
	print("")
def author():
	os.system('cls')
	print("CREATED BY ALVIN MEKO - 672010193");
	print("");
	
def menu():
	os.system('cls')
	print("		MENU PILIHAN ")
	print("------------------------")
	print("1. SEGITIGA")
	print("2. KOTAK")
	print("3. KALKULATOR")
	print("4. AUTHOR")
	pilih = int(input("MASUKKAN PILIHAN ANDA : "))
	if pilih == 1:
		segitiga()
	elif pilih == 2:
		kotak()
	elif pilih == 3:
		kalkulator()
	elif pilih == 4:
		author()
ulang = 'y'
while ulang =='y':
	menu()
	ulang = raw_input("Kembali ke menu utama ? (y/n) : ")