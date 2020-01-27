def entity_count(filename):
    fd=open(filename,"r")
    data=fd.readlines()
    sub="host"
    sub1="}"
    
    for i,line in enumerate(data):
        if line.startswith(sub):
            print(i,(line))
        if (sub1) in line:
            print(i,(line ))
        
    
    
        
        
    
            
            
			
			
			
			
			
def main():
    filename="dhcpd.conf"
    entity_count(filename)
    return
    
if (__name__ == "__main__"):
    main()
		