#A list of ASCII character codes
num_list = (67, 65, 82, 80, 69, 68, 73, 69, 77)
# A list of binary code, each group of 8 is a letter.
# 0b must be in front of the group of 8 in order for python to translate.
bin_list = (0b01100111, 0b01101111, 0b01101111, 0b01100100, 0b00100000, 0b01101111, 0b01101110, 0b01100101,0b00100001)
#An empty list to hold our converted codes
alpha_list = []
beta_list = []
#Loops through the above list and prints out the character(Letter) for each corresponding code.
for item in bin_list:
	#Stores the converted code (item) and stores it in item
	item = chr(item)
	#Adds the newly converted code (item) to the empty list alpha_list
	alpha_list.append(item)
print "".join(alpha_list)

for item in num_list:
    item = chr(item)
    beta_list.append(item)
print "".join(beta_list)
# The function below adds a comma after every 8 characters.
b_list = ('011001110110111101101111011001000010000001101111011011100110010100100001')
def setup_bin(b, every = 8):
	n_list = []
	for i in xrange(0, len(b), every):
		n_list.append(b[i:i + every])

	return ",".join(n_list)
	
print setup_bin(b_list, every = 8)