def ip_to_int(ip):
    octets = ip.split('.')
    ip_integer = 0
    for idx,octet in enumerate(octets,1):
        ip_integer += ((256**(4-idx))*int(octet))
    return ip_integer

def int_to_ip(integer):
    ip = []
    for i in range(4): 
        octet = (integer >> 32-(8*(i+1))) & 255
        ip.append(str(octet))
    return '.'.join(ip)

def cidr_to_int(cidr):
    return 2**32-2**(32-cidr)