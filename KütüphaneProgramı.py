#KÜTÜPHANE PROGRAMI
kitapliste=[]

menu="""
1) Kitap Ekle
2) Kitap Çıkar
3) Kitapları Göster
Q) Çıkış Yap
"""
def kitapekle(liste,kitap):
	liste+=[kitap]
	print("Kitap Eklendi!")
	input("Ana menüye dönmek için ENTER'a basınız...")

def kitapcikar():
	pass

def listele(liste):
	for a in liste:
		print("Kitap Adı :",a)
	input("Ana menüye dönmek için ENTER'a basınız...")

def cikis():
	quit()

while True:
	print(menu)

	secim=input("Seçiminiz\n=>")

	if secim=="1":
		kitapadi=input("Kitap Adı\n=>")
		kitapekle(kitapliste,kitapadi)
	elif secim=="2":
		kitapcikar()
	elif secim=="3":
		listele(kitapliste)
	elif secim=="Q" or secim=="q":
		cikis()
	else:
		print("HATA!\nOlmayan Bir Seçenek Girdiniz!")
		input("Ana menüye dönmek için ENTER'a basınız...")