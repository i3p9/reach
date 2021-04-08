from airport import all_info
from airport import get_ssid
from airport import get_noise

def banner():
    print("[Reach: A WiFi Channel Analyzer]")
    print("""
########  ########    ###     ######  ##     ##
##     ## ##         ## ##   ##    ## ##     ##
##     ## ##        ##   ##  ##       ##     ##
########  ######   ##     ## ##       #########
##   ##   ##       ######### ##       ##     ##
##    ##  ##       ##     ## ##    ## ##     ##
##     ## ######## ##     ##  ######  ##     ##
    """)


def free_channel():
    data = all_info()
    free = []
    for i in range(1,14):
        flag = 0
        for j in range(len(data)):
            if (int(data[j][3]) == i):
                flag += 1
        if(flag<1):
            free.append(i)

    return free
'''
    def recommend_v1():
        free_chn = free_channel()
        recommend = []

        for i in range(len(free_chn)):
            if(free_chn[i]!= 1 or free_chn[i]!= 2 or free_chn[i]!= 3):
                recommend.append(6)
                recommend.append(6)
            elif(free_chn[i]!= 4 or free_chn[i]!= 5 or free_chn[i]!= 6):
                recommend.append()
'''
def weak_aps():
    data = all_info()
    weak_ap_index = []
    for i in range(len(data)):
        if(abs(int(data[i][2])) > 70):
            weak_ap_index.append(i)

    return weak_ap_index

def get_snr():
    data = all_info()
    noise = get_noise()
    snr=[]
    for i in range(len(data)):
        tmp_snr = int(data[i][2]) - int(noise)
        snr.append(tmp_snr)

    return snr

banner()
alldata = all_info()
current = get_ssid()
free_chn = free_channel()
'''
alldata[i][0] is SSID
alldata[i][2] is RSSI
alldata[i][3] is channel
'''
print("--------------------")
print("All free channels: ")
if(len(free_chn) == 0):
    print("No free channels available, please pick a channel with the most amount of RSSI")
else:
    print(free_chn)
'''
high_channels = [1,2,3,4,5,6,7,8,9,10,11,12,13]

print("On 2.4Ghz, the best channels to stay on is 1,6 or 11")
'''
print("--------------------")
print("All used channels: ")
for i in range(len(alldata)):
    print("Channel ",alldata[i][3], " used by SSID: ",alldata[i][0])

print("--------------------")
print("Weak APs (RSSI more than -70): ")
weak = weak_aps()
#for i in range(len(alldata)):

for i in weak:
    print("SSID: ",alldata[i][0],", RSSI: ",alldata[i][2], ", On channel: ",alldata[i][3])

snr = get_snr()
print("--------------------")
print("Signal to Noise ratio against: ")

for i in range(len(alldata)):
    print("SSID: ",alldata[i][0],", SNR: ",snr[i])

print("--------------------")
print("You are currently connected to SSID:",get_ssid())
print("The best channles for 2.4GHz is 1,6,11. If none are available,")
print("Look at the Weak APs and you can use the channles of the Weak APs without much interference")
