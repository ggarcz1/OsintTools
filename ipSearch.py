import requests, json
ip = input('Enter an IPv4, IPV6, or domain name to get geolocation data:\n')
response = requests.get('http://ip-api.com/json/'+ip)
data = json.loads(response.content)
for idx in data:
    print(str(idx)+': '+str(data[idx]))
