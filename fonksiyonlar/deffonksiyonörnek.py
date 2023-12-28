##kenid fonksiyonunu oluşturma 
def hipo(a,b,c):
    ##if bloğu 
    if a**2 + b**2 == c**2:
        return "bu üçgen dik üçgendir"
    ##üçgen dik açı değilse çalışicak kod
    else:
        return "bu üçgen dik üçgen değil kardeşim"
##ekrana fonksiyonumuzu yazdırma 
print(hipo(3,4,6))