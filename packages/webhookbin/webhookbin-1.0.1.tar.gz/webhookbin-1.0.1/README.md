# webhookbin-library
Python library for https://www.webhookbin.net

Install with pip 
```
pip install webhookbin
```

Examples:
```py
import webhookbin

print(webhookbin.makebin().text)

print(webhookbin.post({"data": "here"}).text)

print(webhookbin.get().text)

print(webhookbin.makebin("both").text)

print(webhookbin.makebin("post").text)

print(webhookbin.makebin("get").text)

print(webhookbin.post({"data": "here"},headers={"Customheader": "Something"}).text)

headers = {"Customheader": "Something"}

print(webhookbin.post({"data": "here"},headers=headers,token="DBwIfrB_9BDycs0a4rm0YVRrgsPPpmS2_Vl11ElKpIM").text)

print(webhookbin.get(delete=False).text)

print(webhookbin.get(orderby="acending").text)

print(webhookbin.get(token="DBwIfrB_9BDycs0a4rm0YVRrgsPPpmS2_Vl11ElKpIM").text)

print(webhookbin.patch().text)
```
