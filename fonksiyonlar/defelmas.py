##boşluk fonksiyonu
def bosluk(adet):
    for a in range(int(adet)):
        print(" ",end="")
##sag fonksiyonu
def sag(adet):
    for a in range(int(adet)):
        print("/",end="")
##sol fonksiyonu
def sol(adet):
    for a in range(int(adet)):
        print("\\",end="")
##atla fonksiyonu
def atla(adet):
    for a in range(int(adet)):
        print()
        ##boşluk fonksiyonu
##üstfonksiyonu
def üst(çap):
    baslangic = çap/2-1
    for a in range(int(çap/2)):
        bosluk(baslangic-a)

        sag(1)
        bosluk(a*2)
        sol(1)
        atla(1)
##alt fonksiyonu
def alt(çap):
    baslangic = çap-2
    for a in range(int(çap/2)):
        bosluk(a)
        sol(1)
        bosluk(baslangic-a*2)
        sag(1)
        atla(1)
##elmas fonksiyonu
def elmas(çap):
    üst(çap)
    alt(çap)
##0 a basıldımadıgı sürece süren döngü
while True:
    boyut = int(input("elmasın çapını giriniz : "))
    if boyut==0:
     quit()
    
    elmas(boyut)