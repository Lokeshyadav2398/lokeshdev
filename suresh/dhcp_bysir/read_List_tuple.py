def get_data_by_filename(filename):
    fd=open(filename,"r")
    read_data=fd.readlines()
    data=[]
    for line in read_data:
        data.append(line)
        print(data)
    return data
def entry_position(a):
       
        pos=a
        pos_list=[(pos[i],pos[i+1],pos[i+2],pos[i+3]) for i in range(0,(len(pos)-3),4)]
        #print(pos_list)
        return (pos_list)
        
def last_entry(b):
    last=b
    last_pos=last.pop()
    position=list(last_pos)
    fixed=position[1]
    fixed_address=fixed.lstrip().replace(";"," ")
    ip_add=(fixed_address.split()[1])
    print(ip_add)
    
    return ip_add
    

def generate_new_ip(c):
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
    
def generate_new_dhcp_conf_entry(start_pos,end_pos,data,new_mac,new_sysname):
    #print(f"host {new_sysname} {")
    print(f"hardware {new_mac} ")
    print(f"fixed_address {data}")
    print("}")
    
    
    
    
    
    
    
    
    
    
    
    
def main():
    filename="dhcpd.conf"
    x=get_data_by_filename(filename)
    y=entry_position(x)
    e=last_entry(y)
    z=generate_new_ip(e)
    new_mac="f0:g5:d9:e1:f2"
    new_sysname="mani"
    generate_new_dhcp_conf_entry(23,27,z,new_mac,new_sysname)
    
    return
    
if (__name__ == "__main__"):
    main()