import math

# My approach is to consider that the earlier permutations will
# have the lowest digits in the most significant positions.
# I can determine the number of permutations with the lowest digit
# in the most significant position. For instance, there are 9! 
# possible numbers with 0 in the most significant position. 
# 1e6 / 9! is around 2.7... So I can deduce that 0 and 1 are not
# in the most significant position, but 2 is.
# I then remove 2 from the possible digits, and repeat the algorithm.
# I also know that I have ruled out the lowest 2*9! options. So I can
# subtract that number from 1e6. So I am then looking for the 274240th 
# permutation with the remaining digits. 

digitList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
answer = ""

order = (1e6)-1

for ii in range(len(digitList)):
	permsNext = math.factorial(len(digitList)-1)
	orderReduce = math.floor(order / permsNext )
	order = order - orderReduce * permsNext	
	answer = answer + str( digitList[orderReduce])
	del digitList[ orderReduce ]

print(answer)
