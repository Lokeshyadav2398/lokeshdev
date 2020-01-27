def entity_count(filename):
    fd=open(filename,"r")
    data=fd.readlines()
    sub="host"
    sub1="}"
    list=[]
    s=[  for i,line in enumerate(data) if line.startswith(sub)  if sub1 in line]
    print(s)
	
        
    
    
        
        
    
            
            
			
			
			
			
			
def main():
    filename="dhcpd.conf"
    entity_count(filename)
    return
    
if (__name__ == "__main__"):
    main()
		