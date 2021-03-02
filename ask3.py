import urllib.request
from urllib.parse import urlparse
import json
import datetime

date_and_time = datetime.datetime.now() - datetime.timedelta(days=1) #twrinh hmeromhnia kai wra
today_date = date_and_time.strftime("%Y-%m-%d") #shmerinh hmeromhnia
day = int(date_and_time.strftime("%d"))
year_and_month = date_and_time.strftime("%Y-%m")

for i in range(1, day +2): #klirwseis apo thn 1h tou mhna mexri thn trexousa mera
    if i < 10:
        i = '0' + str(i)
    url = "https://api.opap.gr/draws/v3.0/1100/draw-date/{}/{}/?page=1"
    u = urlparse(url)
    path = '/draws/v3.0/1100/draw-date/' + year_and_month +'-' + str(i) + '/' + year_and_month + '-' + str(i)   #allazw thn hmeromhnia kai thn selida kathe fora
    r = urllib.request.urlopen("https://api.opap.gr" + path)
    html = r.read()
    html = html.decode()
    data = json.loads(html)
    selida = str(data['totalPages']-1) #epeidh oi selides ksekinoun apo 0 sthn arithmisi
    query = '?page=' + selida
    new_url = "https://api.opap.gr" + path + query
    r = urllib.request.urlopen(new_url)
    html = r.read()
    html = html.decode()
    data = json.loads(html, strict=False)
    len_cont = len(data['content'])
    first_draw = data['content'][len_cont-1]['winningNumbers']['list']
    print(first_draw )
