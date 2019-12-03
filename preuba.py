import  json, requests, urllib3
        
temp = float("28.7")
state = int("1")
env = { "id_ac": "G81","temp":temp,"state":state,"motion":state }
data = json.dumps(env)
http = urllib3.PoolManager()
reps = http.request('POST', 'https://ac-ctrl.herokuapp.com/regforhour', headers={'Content-Type':'application/json'},
                 data = data)
print(resp)
# params = json.dumps(env)
# resp = requests.post("https://ac-ctrl.herokuapp.com/regforhour", data = params)
# print(resp.text)