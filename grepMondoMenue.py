#!/usr/bin/env python3
import urllib.request, json, datetime
url=urllib.request.urlopen("https://www.mondo-daily.de/_ajax-card.php")
data = json.loads(url.read().decode())
menueDate=datetime.datetime.strptime(data["date"], "%Y-%m-%d")

print("\n*Mondo Daily Menue "+menueDate.strftime("%d.%m.%Y")+"*")
if datetime.datetime.now().strftime("%d.%m.%Y")==menueDate.strftime("%d.%m.%Y"):
    for foodType in data["category"]:
        if ((foodType=='type_1')|(foodType=='type_2')|(foodType=='type_3')):
            print("\n_"+data['category'][foodType]["title"]+"_")
            for key in data['category'][foodType]["articles"]:
                if key["sold"]:
                    print("-> ~*"+key["title"].rstrip('\r\n')+"* "+key["price"]+" EUR ("+key["description"].rstrip('\r\n')+")~")
                else:
                    print("-> *"+key["title"].rstrip('\r\n')+"* "+key["price"]+" EUR ("+key["description"].rstrip('\r\n')+")")
