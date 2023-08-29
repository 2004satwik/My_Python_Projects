import urllib.request, urllib.parse, urllib.error
data = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
s=data.decode().read()
print(s)
