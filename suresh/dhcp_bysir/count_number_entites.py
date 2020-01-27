def read_file(filename):
    fd=open(filename,"r")
    data=fd.readlines()
    #print("data :%s" %data)
    sub="fixed-address"
    sub1="host"
    list=[]
    
    for line in data:
        if sub in line:
            a=line.split()
            b=(a.pop())
            print(b)
            c=b.replace(";","  ")
            f=c.split('.')
            #print(f)
            g=int(f[3])+1
            g=str(g)
            h=f.pop(3)
            #print(h)
            ip=".".join(f)
            current_ip=ip+"."+g
            yield current_ip
            
def main():
    filename="dhcpd.conf"
    result=read_file(filename)
    e=list(result)
    fixed_ip=e[-1]
    print("fixed-adress"+" "+fixed_ip)
    
    
    return
    
if (__name__ == "__main__"):
    main()