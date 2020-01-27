def get_data_by_filename(filename):
    fd = open(filename,"r")
    read_data = fd.readlines()

    return read_data

def entry_position(data):
    tlist=[]
    str_host = "host"
    end_of_entry = "}"
    for i,line in enumerate(data):
        if line.startswith(str_host):
            spos = i+1

        if end_of_entry in line:
            epos = i+1
            tlist.append((spos, epos))

    return tlist
	
def last_entry(b):
    last=b
    last_pos=last.pop()
    a,b=(last_pos)
    
    
    return last_pos,a,b
    

def generate_new_ip(data):
    ip="192.168.1.217"
    return ip
    ip=c.split(".")
    #print(ip)
    ipv=int(ip[3])+1
    str(ipv)
    d=ip.pop(3)
    #print(d)
    e=".".join(ip)
    #print(e)
    new_ip=e+"."+str(ipv)
    print(new_ip)
    return new_ip
    
#def generate_new_dhcp_conf_entry(start_pos,end_pos,data,new_mac,new_sysname):
def generate_new_dhcp_conf_entry(newip, new_mac, new_sysname):
    print(f"host {new_sysname} ", "{")
    print(f"\thardware {new_mac}; ")
    print(f"\tfixed_address {newip};")
    print(f"\toption routers 192.168.1.1;")

    print("};")
    
    
    
    
    
    
    
    
    
    
    
    
def main():
    filename="dhcpd.conf"
    data = get_data_by_filename(filename)

    entries = entry_position(data)

    le_sp, le_ep = entries[-1]

    newip = generate_new_ip(data[le_sp-1:le_ep])

    new_mac="f0:g5:d9:e1:f2"
    new_sysname="mani"

    generate_new_dhcp_conf_entry(newip, new_mac, new_sysname)
    
    return
    
if (__name__ == "__main__"):
    main()
            
	
