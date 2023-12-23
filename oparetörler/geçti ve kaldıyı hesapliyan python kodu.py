##değişken ve veri alma
öğrenci_notu = (input("aldığınız notu giriniz : "))
##notu float a çevirme
float(öğrenci_notu)
#taktir teşekür hesaplama geçti 
if öğrenci_notu >="85" :
    print("taktirle geçtiniz")
elif öğrenci_notu >="70" :
    print("teşekür aldınız")
elif öğrenci_notu >="50" :
    print("sınıfı geçtiniz")
else :
    print("sınıfta kaldın baban seni dövicek")