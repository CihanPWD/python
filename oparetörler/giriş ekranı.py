##kullanıcıdan veri alma
kullanıcı_adı = input("kullanıcı adınızı giriniz : ")
kullanıcı_şifre = input("kullanıcı şifreni gir : ")
#veri tabanındaki data
belirli_kullanıcı_adı = "haydar" 
belirli_şifre = "bakacaz"
##if bloğu 
if belirli_kullanıcı_adı !=kullanıcı_adı:
    print("hatali kullanıcı adı girdiniz")
if belirli_şifre != kullanıcı_şifre:
    print("şifre hatalı")
else :
    print("giriş yaptınız")
    