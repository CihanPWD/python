##while döngüsü
while True:
##kullanıcıdan veri alma
    isim = input(str("isminizi giriniz : "))
    soy_Ad = input("soyadınızı giriniz : ")
    yaş = input("yaşınızı giriniz : ")
    şehir = input(str("yaşadığınız şehir i giriniz : "))
    ekrana_Basılacak_Yazı = """
    ismini nedir : {}
    soyadınız nedir : {}
    yaşınız kaç : {}
    yaşadıpınız şehir : {}


    """.format(isim,soy_Ad,yaş,şehir)
    print(ekrana_Basılacak_Yazı)
    ##format dönüştürme ve ekrana bastırm
    exit()



