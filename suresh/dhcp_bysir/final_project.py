def get_data_by_filename(filename):
    fd=open(filename,"r")
    read_data=fd.readlines()
    data=[]
    for line in read_data:
        data.append(line)
        print(data)
    return data
def entry_position(a):
    data1=a
    list=[]
    sub="host"
    sub1="}"
    for i,line in enumerate(data1):
        if line.startswith(sub):
            (list.append(i))
        if (sub1) in line:
            print(i)
            (list.append(i))
            print(list)
    pos_list=[(list[i],list[i+1]) for i in range(0,(len(list)-1),2)]
    print(pos_list)
    return pos_list
	
def last_entry(b):
    last=b
    last_pos=last.pop()
    a,b=(last_pos)
    
    
    return last_pos,a,b
    

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
    print(f"host {new_sysname} ", "{")
    print(f"hardware {new_mac} ")
    print(f"fixed_address {data}")
    print("}")
    
    
    
    
    
    
    
    
    
    
    
    
def main():
    filename="dhcpd.conf"
    x=get_data_by_filename(filename)
    y=entry_position(x)
    ip="192.168.1.217"
    e=last_entry(y)
    z=generate_new_ip(ip)
    new_mac="f0:g5:d9:e1:f2"
    new_sysname="mani"
    generate_new_dhcp_conf_entry(y,new_mac,new_sysname)
    
    return
    
if (__name__ == "__main__"):
    main()
            
	