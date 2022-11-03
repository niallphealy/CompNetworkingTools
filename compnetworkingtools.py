ip = input("Enter IP: ")
# maskprompt = input("type m for mask, c for cidr")

# if maskprompt == "m" :
mask = input("Enter mask: ")
# else :
# 	c = input("Enter cidr: ")


ip = ip.split(".")
mask = mask.split(".")
binip = []
binmask = []
finandop = []

for byte in ip:
	binip.append(bin(int(byte)).replace("0b", "").zfill(8))

for byte in mask:
	binmask.append(bin(int(byte)).replace("0b", "").zfill(8))

# to find network id
x = 0
while x < 4 :
	j = 0
	while j < 8:
		if (binip[x][j] == "1") and (binmask[x][j] == "1") :
			finandop.append("1")
		else:
			finandop.append("0")
		j+=1;
	finandop.append(".")
	x+=1;

finandop.pop(len(finandop)-1)

finandopstr = "".join(finandop)
# finandopstr.split(".")
final_string = []
print("Network ID: ", end="")
for byte in finandopstr.split(".") :
	final_string.append(int(byte, 2))

print(final_string)

# to find broadcast address

cidr = -1
x = 0

y = 0
for y in range(4):
	for x in range(8) :
		if (cidr == -1) :
			if(binmask[y][x] == "0") :
				cidr = x + y*8
				break
		else:
			break


broadcast_string = "".join(binip)

broadcast_address_ending = broadcast_string[cidr-1:-1]
broadcast_address_ending = broadcast_address_ending.replace("0", "1")

broadcast_address = broadcast_string[0:cidr] 
broadcast_address = broadcast_address + broadcast_address_ending


byte = []

for i in range(4):
	for j in range(8):
		byte.append(broadcast_address[j+i*8])
	print(int("".join(byte), 2), end="")
	print(".",end="")
	byte = []