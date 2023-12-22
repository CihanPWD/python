### menü ekranı 
print("""

1 istanbul 
      
2 ankara 

3 izmir 

4 konya


""")
##if bloğu
a = input("birini seçiniz : ")
if a =="1": 
 b = input("neden istanbul : ")
elif a =="2":
 b = input("neden ankara yi seçtin kro :  ")
elif a =="3": 
 b = input("izmirin neyi meşhur : ")
elif a == "4":
 b = input("konyalılar etliekmek mi : ")
 ## 4 seçenekten biri çıkmazsa
else:
 print("sayi ile seç hayvan")