import pyshorteners as sh

link = input("enter Url:")

s = sh.Shortener()
x = (s.tinyurl.short(link))

print(x)