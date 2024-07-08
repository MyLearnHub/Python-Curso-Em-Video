import urllib.request
import urllib.error

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except urllib.error.URLError:
    print(f"\033[0;31mO site Pudim não está acessível no momento.\033[m")
else:
    print(f"\033[0;32mConsegui acessar o site Pudim com sucesso!\033[m")
    print(site.read())
