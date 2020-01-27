def entity_count(filename,n):
    fd=open(filename,"r")
    data=fd.readlines()[:n]
    sub="host"
    sub1="}"
    n=len(data)
    list=[]
    
    for i,line in enumerate(data):
        if line.startswith(sub):
           
            (list.append(i))
            
            
            
        if (sub1) in line:
            
            print(i)
            (list.append(i))
    print(list)
    
    
    pos_list=[(list[i],list[i+1]) for i in range(0,(len(list)-1),2)]
    print(pos_list)
    print(pos_list.pop())
            
        
    
    
        
        
    
            
            
			
			
			
			
			
def main():
    filename="dhcpd.conf"
    n=18
    result=entity_count(filename,n)
    
    return
    
if (__name__ == "__main__"):
    main()
		