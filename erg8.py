import urllib.request
import json

def getKeys(lex):
    line = []
    for key in lex.keys():
        line.append(key)

    return line

def price(symbolism, symbols_comp=["EUR"]):
    url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}&e=CCCAGG'\
            .format(symbolism.upper(), ','.join(symbols_comp).upper())
    r=urllib.request.urlopen(url)
    html=r.read()
    html=html.decode()
    data=json.loads(html)
    return data

file = input("Enter file location: ")
file1 = open(file,'r')
file1 = file1.read()
file1 = json.loads(file1)
x=getKeys(file1)
tmp={}
for i in x:
    tmp1 = price(i)
    tmp[i] = tmp1["EUR"]*file1[i]
print('Το web-portofolio σας είναι: ')
print(fil1)
print('Σε ευρώ είναι: ')
print(tmp)
