import requests as req

params = {'username': 'Ryan', 'password': 'password'}
r = req.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
print("Cookie is set to:")
print(r.cookies.get_dict())
print("-----------")
print("Going to profile page...")
r = req.get("http://pythonscraping.com/pages/cookies/profile.php", cookies=r.cookies)
print(r.text)
