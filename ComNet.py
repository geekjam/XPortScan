import socket
def __GetLocalIpAddr(ifname):
    #in linux
    import fcntl
    import struct
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
	    0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15])
    )[20:24])

def GetLocalIpAddr():
    ip_str = socket.gethostbyname(socket.gethostname())
    if '127' in ip_str >=0 :
        try:
            ip_str = getipaddr('eth0')
	except:
	    try:
		ip_str = __GetLocalIpAddr('wlan0')
	    except:
		pass
    return ip_str


