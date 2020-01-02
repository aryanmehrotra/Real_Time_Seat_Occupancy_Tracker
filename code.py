import matplotlib.pyplot as plt
import requests
import time
def Plot(Occupied,Unoccupied):
    labels='Occupied','Unoccupied'
    sizes=[Occupied,Unoccupied]
    colors=['gold','yellowgreen']
    explode = (0.1, 0)
    plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=0)
    plt.axis('equal')
    plt.show()
print("Initialising Real Time Seat Occupancy Tracker")
time.sleep(1)
print("Connecting to the Server")
time.sleep(1)
print("Connection Established")
time.sleep(1)
while True:
    print("Getting The Status")
    url = "https://cloud.boltiot.com/remote/8048e7f6-315e-45bf-999b-27e357d67636/digitalRead"

    querystring0 = {"pin":"0","deviceName":"BOLT3849125"}
    querystring1 = {"pin":"1","deviceName":"BOLT3849125"}

    headers = {
        'Cache-Control': "no-cache"
        }

    response0 = requests.request("GET", url, headers=headers, params=querystring0)
    response1 = requests.request("GET", url, headers=headers, params=querystring1)
    dic0=response0.text
    dic1=response1.text
    dict0=eval(dic0)
    dict1=eval(dic1)
    print(dict0)
    print(dict1)
    if((dict0['value'])=="0" and (dict1['value'])=="0"):
        Occupied=2
        Unoccupied=0
        Plot(2,0)
    elif((dict0['value'])=="0" and (dict1['value'])=="1" or (dict0['value'])=="1" and (dict1['value'])=="0" ):
        Occupied=1
        Unoccupied=1
        Plot(1,1)
    elif((dict0['value'])=="1" and (dict1['value'])=="1"):
        Unoccupied=2
        Occupied=0
        Plot(0,2)
    else:
        print("Try Again Later")
    time.sleep(1)
    print("Please wait we are refreshing the code for you : Wait time 1 sec")
    print("Connecting to the Server")
    print("Connection Established")








