import requests, json, serial, time

line = serial.Serial('/dev/ttyACM0', 9600)
resp = requests.get("https://ac-ctrl.herokuapp.com/ac")
data = resp.json()
val = data[0].get("state")
while True:
    time.sleep(2)
    resp = requests.get("https://ac-ctrl.herokuapp.com/ac")
    data = resp.json()
    
    if(int(data[0].get("state")) != int(val)):
        var = '1'.encode()
        line.write(var)
        dta = line.readline()
        temp = float(dta[0:5])
        state = int(dta[6:8])
        data = { "id_ac": "G81","temp":temp,"state":state,"motion":state }
        http = urllib3.PoolManager()
        r = http.request('POST', 'https://ac-ctrl.herokuapp.com/regforhour', headers={'Content-Type':'application/json'},
                 body = json.dumps(data))
        val = data[0].get("state")