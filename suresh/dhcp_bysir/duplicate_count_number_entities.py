def read_file(filename):
    fd=open(filename,"r")
    
    data=fd.readlines()
    #print("data :%s" %data)
    sub="fixed-address"
    sub1="host"
    list=[]
    
    for line in data:
        if sub in line:
            list=[]
            a=line.split()
            b=(a.pop())
            c=b.replace(";","  ")
            f=c.split('.')
            print(f)
            for x in range(214,217):
                print(f[0]+"."+f[1]+"."+f[2]+"."+str(x)+'\n')
            
            
            
            
                
            
            
    
def main():
    filename="dhcpd.conf"
    read_file(filename)
    return
    
if (__name__ == "__main__"):
    main()