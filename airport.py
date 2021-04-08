import subprocess

def all_info():
    scan_cmd = subprocess.Popen(['airport', '-s'],    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    scan_out, scan_err = scan_cmd.communicate()
    data = str(scan_out).split("\\n")[1:-1]
    col = 7
    row = len(data)
    sorted = [[0] * col for _ in range(row)]
    i = 0

    for thing in data:
        name = thing[0:32].lstrip()
        sorted[i][0]=name
        thing = thing[32:]
        mac_address = thing[1:18]
        sorted[i][1]=mac_address
        thing = thing[18:]
        rssi = thing[1:4]
        sorted[i][2]=rssi
        thing = thing[4:]
        channel = thing[1:9].strip()
        channel_fix, nouse, nouse2 = channel.partition(',')
        sorted[i][3]=channel_fix
        thing = thing[9:]
        Y_or_N, region, security = thing.split(' ',2)
        sorted[i][4]=Y_or_N
        sorted[i][5]=region
        sorted[i][6]=security
        i+=1

    return sorted

def get_ssid():
    findssid = subprocess.Popen(['airport', '-I'],    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    ssid_data, ssid_err = findssid.communicate()
    data = str(ssid_data).split("\\n")[12:13]
    ssid = data[0].lstrip()
    ssid = ssid.strip("SSID: ")
    return ssid

def get_noise():
    findnoise = subprocess.Popen(['airport', '-I'],    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    noise_data, noise_err = findnoise.communicate()
    data = str(noise_data).split("\\n")[2:3]
    noise = data[0].lstrip()
    noise = noise.strip("agrCtlNoise: ")
    return noise
