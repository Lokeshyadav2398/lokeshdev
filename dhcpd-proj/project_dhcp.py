def get_data(fname):
	fd = open(fname,"r")
	data = fd.readlines()
	list = []
	for line in data:
		list.append(line)
	print(list)
	
def get_entry_position(fname):
	fd = open(fname,"r")
	data = fd.readlines()  #[:n]
	sub1 = "host"
	sub2 = "}"
	list1 = []
	for i,line in enumerate(data):
		if line.startswith(sub1):
			list1.append(i)
		if line.startswith(sub2):
			list1.append(i)	
	print(list1)
	
def get_last_entry_data(fname):
	lines = [16,17,18,19,20]
	i = 0
	fd = open(fname,'r')
	for data in fd:
		if i in lines:
			print(data)
		i = i+1
def generate_new_dhcp_conf_entry(data,new_mac,new_sysname):
	print(data)
	
def new_ipaddr(fname):
	fd = open(fname,"r")
	data = fd.readlines()
	sub = "fixed"
	for i,line in enumerate(data):
		if sub in line:
			f = line.split( )
			g = f[1].rstrip(";").split(".")
			h = int(g[3])+1
			h = str(h)
			i = g.pop(3)
			ip = ".".join(g)+"."+h+";"
			new_ip ="	"+f[0]+" "+ip
			print(new_ip)
	
	
	
def main():
	fname = "dhcpd.conf"
	get_data(fname)		
	#n = int(input("enter any number :"))
	get_entry_position(fname)
	data = get_last_entry_data(fname)
	new_mac = "A0:B5:D9:D6:E1:F2"
	new_sysname = "Loki_laptop"
	generate_new_dhcp_conf_entry(data,new_mac,new_sysname)
	new_ipaddr(fname)
	
if(__name__=="__main__"):
	main()
	
	"""
for i,line in enumerate(data):
		pos_list = []
		if line.startswith(sub1):
			list1.append(i)
		if line.startswith(sub2):
			list1.append(i)	
			pos = ([(list1[i],list1[i+1]) for i in range(0,len(list1),2)])
			print(pos)
		"""