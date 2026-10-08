# Değişkenler veri tiplerini barındırmak için kullanılır.
# Python'da değişkenleri tanımlamak için komut bulunmaz.
# Değişkene veri atandığında oluşturulur.
# Değişkenlere özellikle tür atanmaz ve sonradan türü değiştirilebilir.
x = 5
y = "John"
print(x)
print(y)
print("\n")

x = 4
x = "Sally"
print(x)
print("\n")

# Değişkene spesifik bir türde değer atamak istiyorsanız bunu casting(tür dönüşümü) ile yapabilirsiniz.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0 

# type() fonskiyonu ile değişkenin türünü öğrenebilirsiniz.
x = 5
y = "John"
print(type(x))
print(type(y)) 
print("\n")

# String değişkenler "" veya '' kullanılarak tanımlanabilir.
x = "John"
# is the same as
x = 'John'

# Değişken adları büyük küçük harf duyarlıdır(Case-Sensitive).
a = 4
A = "Sally"
# A will not overwrite a

