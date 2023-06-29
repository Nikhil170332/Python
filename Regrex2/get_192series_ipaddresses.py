import re
def ips(*arg):
    ls = arg
    valid_ips = []
    required_ips = []
    pattern = re.compile("^((25[0-4]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-4]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$")
    req_pattern = re.compile("^(192\.((25[0-4]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){2}(25[0-4]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]))$")
    for k in arg:
        p = re.search(pattern,k)
        if p:
            valid_ips.append(k)
            if (re.search(req_pattern,k)):
                required_ips.append(k)
            else:
                pass
        else:
            pass
    print("valid IPs are\n",valid_ips)
    print("Required 192 series IPs are\n",required_ips)
    
ips('0.0.0.0','1.0.0.0','192.168.1.0','192.32.32.0','192.220.254.0','172.31.0.0','10.0.0.0','8.8.8.8','132.220.220.0','132.257.255.255')