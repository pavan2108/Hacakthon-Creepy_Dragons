'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def freq_fun(value):
	value = str(value)
	freq = dict()
	for i in range(0,len(value)):
	    #print(value[i])
	    if value[i] not in freq:
	        freq[value[i]] = 1
	    else:
	        freq[value[i]] = freq[value[i]] + 1
	return freq
	
def are_same_dicts(dict1, dict2):
	for key in dict1:
		value = dict1[key]
		if key in dict2:
			if dict2[key] != value:
				return False
		else:
			return False
	return True
			 
	
def is_special_number(value):
    value_sq = value * 2
    #print(value_sq)
    freq, freq_sq = freq_fun(value), freq_fun(value_sq)
    #print(freq)
    #print(freq_sq)
    return are_same_dicts(freq, freq_sq)
for _ in range(int(input())):
    x = int(input())
    y = int(input())
    c = is_special_number(x)
    d = is_special_number(y)
    if(c and d):
    	print(1)
    else:
    	print(0)
