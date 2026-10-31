import requests
url="http://192.168.0.105:5000/autorisation"
s=[]
for i in range(57245724):
    r=requests.get(url)
    s.append(r.status_code)
    if i%1000==0:
        print(i,s)
        s=[]

#print(r.text)
#print(r.status_code)