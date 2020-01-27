def get_data_by_filename(filename):
    fd=open(filename,"r")
    data=fd.readlines()
    list=[]
    for line in data:
        list.append(line)
    print(list)
    
def get_entry_position(data,n):
    fd=open(data,"r")
    read_data=fd.readlines()[:n]
    sub="host"
    sub1="}"
    n=len(read_data)
    list=[]
    
    for i,line in enumerate(read_data):
        if line.startswith(sub):
            list.append(i)
            #print(line)
            
            
        if (sub1) in line:
            (list.append(i))
            #print(list)
            
            pos=([set(list[i],list[i+1]) for i in range(0,len(list),2)])
            #print(line)
            print(" ")
            print(((pos.pop())))
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
def main():
    filename="dhcpd.conf"
    get_data_by_filename(filename)
    n=int(input("enter the number"))
    get_entry_position(filename,n)
    
    return
    
if (__name__ == "__main__"):
    main()