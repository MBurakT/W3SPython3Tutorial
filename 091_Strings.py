a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print()

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
print()

# Stringler Arraydir.
a = "Hello, World!"
print(a[1])
print()

# String karakterleri döngü ile dönme
for i in "banana":
    print(i)
print()

# Stringlerin uzunluğu len() fonksiyonu ile bulunur.
a = "Hello, World!"
print(len(a))
print()

# Stringlerin içinde aradığımız kelimeler için "in" kullanılır.
txt = "The best things in life are free!"
print("free" in txt)
print()

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")
print()

txt = "The best things in life are free!"
print("expensive" not in txt)
print()

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("NO, 'expensive' is NOT present.")

print()

