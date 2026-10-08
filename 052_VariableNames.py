# Değişkenlerin x ve y gibi isimleri olabileceği gibi uzun ve açıklayıcı isimleri de olabilir.
"""
Python'da değişken kuralları:
    Bir değişken ismi harf veya alttan çizgi ile başlamadlıdır.
    Bir değişken ismi sayı ile başlayamaz.
    Bir değişken ismi (A-z, 0-9, ve _) barındırabilir.
    Değişken isimleri büyük küçük harf duyarlıdır.
    Değişken isimleri Python anahtar kelimelerinden biri olamaz.
"""

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Multi Words Variable Names
# Camel Case
myVariableName = "John"

# Pascal Case
MyVariableName = "John" 

# Snake Case
my_variable_name = "John"

# Birden fazla değişkene değer atama
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
print()

# Birden fazla değişkene bir değer atama
x = y = z = "Orange"
print(x)
print(y)
print(z)
print()

# Koleksiyonu açma
# Eğer list, tuple vb. koleksiyonunuz varsa. Python bunları çıkartrak değişkenlere atamanıza izin verir.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
print()