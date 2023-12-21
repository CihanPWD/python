##değişken ve input girişleri
sayi_1 = float(input("1 ci sayiyi giriniz : "))
sayi_2 = float(input("2ci sayiyi giriniz :  "))
işlem = (input("yaptırmak istediginiz işlemi giriniz : "))
## koşul bloğu
if işlem == "+":
  print("işlem sonuç : ",sayi_1+sayi_2)
elif işlem == "-":
  print("işlem sonuç : ",sayi_1-sayi_2)
elif işlem == "*":
  print("işlem sonuç : ",sayi_1*sayi_2)
elif işlem == "/":
  print("işlem sonuç : ",sayi_1/sayi_2)
  ##kodu bitiren fonksiyon
else : 
  print("4 işlem sembölleri girsene lan ayı")