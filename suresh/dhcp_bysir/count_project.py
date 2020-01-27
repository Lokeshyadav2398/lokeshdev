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
            #print(b)
            c=b.replace(";","  ")
            f=c.split('.')
            #print(f)
            g=int(f[3])+1
            g=str(g)
            h=f.pop(3)
            #print(h)
            ip=".".join(f)
            print(ip+"."+g)


def start_position(filename):
    fd=open(filename,"r")
    data=fd.readlines()
    sub="host"
    sub1="}"
    
    for i,line in enumerate(data):
        if line.startswith(sub):
            print(i,line)
            


def start_end(filename):
    fd=open(filename,"r")
    data=fd.readlines()
    sub="host"
    sub1="}"
    
    for i,line in enumerate(data):
        if line.startswith(sub):
            print(i,line)
        if (sub1) in line:
            print(i,line)
        
        
            
            
            
            
            
            
            
               
            
            
                
            
            
    
def main():
    filename="dhcpd.conf"
    read_file(filename)
    start_position(filename)
    start_end(filename)
    return
    
if (__name__ == "__main__"):
    main()