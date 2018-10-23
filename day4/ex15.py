from sys import argv

script, filename = argv

txt = open(filename)

print("Here's your file %r" %filename)
print(txt.read())
txt.close()
print("Type the filename again:")
filename_again = input(">")
txt_again = open(filename_again)
print(txt_again.read())
txt_again.close()