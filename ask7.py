import datetime
import urllib.request
import json
dtoday = datetime.datetime.now()
li2 = []
for i in range(1,82):
    li2.append(0)
for i in range(0,1):
    dtoday = dtoday - datetime.timedelta(days=1)
    drawlist = []
    dstring = dtoday.strftime("%Y-%m-%d")
    url = "https://api.opap.gr/draws/v3.0/1100/draw-date/{}/{}/draw-id".format(dstring,dstring)
    url_draws_of_day = urllib.request.urlopen(url)
    html = url_draws_of_day.read()
    html = html.decode()
    drawIds = json.loads(html,strict=False)
    drawlist.append(drawIds)
    for i in range(0,2):
        d = drawlist[0][i]
        url2 = "https://api.opap.gr/draws/v3.0/1100/draw-id/{}/{}".format(str(d),str(d))
        url_of_each_draw = urllib.request.urlopen(url2)
        html = url_of_each_draw.read()
        html = html.decode()
        num = json.loads(html,strict=False)
        for draw in num["content"]:
            temp = draw ["winningNumbers"]["list"]
            print(temp)
            for k in range(1,20):
                li2[temp[k]] += 1
print("Συχνότερα εμφανίζεται ο αριθμός:" ,li2.index(max(li2)))
