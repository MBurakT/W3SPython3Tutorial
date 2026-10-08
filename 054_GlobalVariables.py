# Global değişkenler fonksiyonların dışında tanımlanmış değişkenlerdir.
# Global değişkenler herkes tarafından kullanılabilir. Fonskiyonların içinde ve dışında da kullabilirler.
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()
print()

# Eğer fonskiyonun içinde aynı isimli bir değişken tanımlarsanız bu değişken local değişken olacaktır.
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
print()

# global anahtar kelimesi
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
print()

# Ayrıca global değişkeni fonskiyonun içinde kullanmak isterseniz global anahtar kelimesini kullanabilirsiniz.
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

