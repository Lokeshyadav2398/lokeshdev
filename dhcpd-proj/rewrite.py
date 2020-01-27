def rewrite(fname):
	fd = open(fname,"r")
	sub1 = "Lokesh_laptop"
	sub2 = "A0:B5:D9:D6:E1:F2;"
	sub3 = "hardware"
	sub4 = "fixed"
	sub5 = "option"
	sub6 = "}"
	data = fd.readlines()
	list = []
	for i,line in enumerate(data):
		if line.startswith("host"):
			a = line.split( )
			b = a.pop(1)
			a = a[0] +" "+ sub1 +" " + a[1]
			list.append(a)
				
		elif sub3 in line:
			d = line.split( )
			e = d.pop(2)
			d = "	" + d[0] +" "+ d[1] +" "+ sub2
			list.append(d)
				
		elif sub4 in line:
			f = line.split( )
			g = f[1].rstrip(";").split(".")
			h = int(g[3])+1
			h = str(h)
			i = g.pop(3)
			ip = ".".join(g)+"."+h+";"
			new_ip ="	"+f[0]+" "+ip
			list.append(new_ip)
				
		elif sub5 in line:
			l = ""+line
			list.append(l)
				
		elif line.startswith(sub6):
			list.append(line)
	print(list)
	wfd = open("new_entry.txt",'w')
	for data in list:
		print(data)
		print("\n")
		wfd.write(data)
		wfd.write("\n")
		
def main():
	fname = "ip.txt"
	rewrite(fname)
	
if(__name__=="__main__"):
	main()

