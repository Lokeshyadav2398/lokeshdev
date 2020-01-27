def last_entity(filename,n):
    fd=open(filename,"r")
    data=fd.readlines()[-n:]
    n=len(data)
    list=[]
    for line in data:
        print(list.append(line))
        
            
    
    
    
   
        
 




def main():
    filename="dhcpd.conf"
    n=5
    last_entity(filename,n)
    return
    
if (__name__ == "__main__"):
    main() 