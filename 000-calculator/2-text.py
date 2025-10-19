# text
print('spam eggs')
print("Paris  rabbit got your back :)! Yay!")
print('1975')

print('doesn\'t')
print("doesn't")
print('"yes," they said.')
print("\"yes,\" they said.")
print('"Isn\'t," they said.')

s = 'First line.\nSecond line.'
print(s)

print('C:\some\name')
print(r'C:\some\name')

print("""\
Usage: thingy [OPTIONS]
      -h                    Display this usage message
      -H hostname           Hostname to connect to
""")

print( 3 * 'un' + 'ium')

print('Py' 'thon')

text = ('Put several strings within parentheses '
        'to have them joined together')
print(text)

prefix = 'Py'
print(prefix + 'thon')

word = 'Python'
print(word[0]) # karakter posisi ke 0
print(word[5]) # karakter posisi ke 5
print(word[-1]) # karakter terakhir
print(word[-2]) # karakter kedua terakhir
print(word[-6])

print(word[0:2]) # karakter dari posisi ke 0 (included) sampai ke 2 (excluded)
print(word[2:5]) # karakter dari posisi ke 2 (included) sampai ke 5 (excluded)
print(word[:2]) # karakter dari posisi pertama sampai ke 2
print(word[4:]) # karakter dari posisi keempat sampai akhir
print(word[-2:])
print(word[:2] + word[2:])
print(word[:4] + word[4:])
print(word[4:42])
print(word[42:])

print('J' + word[1:])
print(word[:2] + 'py')

s = 'supercalifragilisticexpialidocious'
print(len(s))