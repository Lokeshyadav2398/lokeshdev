def get_dhcpd_conf(fname):
    fd = open(fname,"r")
    data = fd.readlines()
    return data

def get_next_ip(data):
    sub4 = "fixed-address"
    for i,line in enumerate(data):
        if sub4 in line:
            f = line.split( )
            g = f[1].rstrip(";").split(".")
            h = int(g[3])+1
            h = str(h)
            i = g.pop(3)
            ip = ".".join(g)+"."+ h
    return ip

def generage_new_entry(sysname, macaddr, new_ip):
    print(f"host {sysname}", "{")
    print(f"\thardware ethernet {macaddr};")
    print(f"\tfixed-address {new_ip};")
    print(f"\toption routers 192.168.1.1;")
    print("}")
    return

                            
def main():
    sysname = "Lokesh_laptop"
    macaddr = "A0:B5:D9:D6:E1:F2;"
    fname = "ip.txt"
    data = get_dhcpd_conf("ip.txt")
    new_ip = get_next_ip(data)
    generage_new_entry(sysname, macaddr, new_ip)
        
if(__name__=="__main__"):
    main()

