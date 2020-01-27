def entity_count(filename):
    fd=open(filename,"r")
    data=fd.read()
    sub="host"
    sub1="}"
    i=data.find(sub)
    #print(i)
    i=0
    while i!=-1:
        print(sub,"is available at index" ,i)
        i=data.find(sub,i+1,len(data))
        
        
    
            
            
			
			
			
			
			
def main():
    filename="dhcpd.conf"
    entity_count(filename)
    return
    
if (__name__ == "__main__"):
    main()
		