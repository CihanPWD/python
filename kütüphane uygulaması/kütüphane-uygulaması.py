##kitap listesi ve menü 
kitap_listesi = list()
menü = """

1) Kitap Ekle
2) Kitap Çıkar
3) Kitapları Göster
Q) Çıkış

"""
##kitap ekleme fonksiyonu
def kitap_ekle(liste,kitap):
    liste += [kitap]
    print("Kitap başarıyla eklendi.")
#kitap çıkartma fonksiyonları
def kitap_cikar():
    pass
#var olan kitapları göster
def kitap_göster(liste):
    for a in liste:
        print("Kitap Adı >>>>>>>>",a)
        #uygulamadan çıkış
def cikis():
    print("Bizi tercih ettiğiniz için teşekkür ederiz...")
    quit()
#algoritmanin sürekli dönmesi için döngü 
while True:
    print(menü)
    secim = input("Seçiminiz : ")
    if secim =="1":
        kitap_adi = input("Kitap Adı : ")
        kitap_ekle(kitap_listesi,kitap_adi)
    elif secim=="2":
        kitap_adi = input("Kitap Adı : ")
        kitap_cikar()
    elif secim=="3":
        kitap_göster(kitap_listesi)
    elif secim=="Q" or secim=="q":
        cikis()
    else:
        print("Hatalı giriş yaptınız!")
    input("Ana menüye dönmek için enter'a basınız!")