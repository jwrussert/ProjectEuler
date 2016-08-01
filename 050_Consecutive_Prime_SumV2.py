import math
logbase = 1.005 #this number is sort of arbitrary, but i found that this logbase kept the lists of primes relatively short and made the search quick

def OrderedSieve(limit):
    j = 2
    PrimeList = [True]*limit
    PrimesSorted = []

    for i in range(1+math.floor(math.log(limit,logbase))):
        PrimesSorted.append([])
                   
    degree = 0

#set all of the composite number indices to False
    for i in range(2,limit):
        if PrimeList[i] == True:
            while i*j < limit:
                PrimeList[i*j] = False
                j = j+1

        j = 2

#create an indexed list of lists containing all prime numbers in a given range
    j = 1        
    for i in range(2, limit):
        degree = math.floor(math.log(i,logbase))
        if PrimeList[i] == True:
            PrimesSorted[degree].append(i)
    return PrimesSorted

def Sieve(limit):
    j = 2
    PrimeList = [True]*limit
    Primes = []

#set all of the composite number indices to False
    for i in range(2,limit):
        if PrimeList[i] == True:
            while i*j < limit:
                PrimeList[i*j] = False
                j = j+1

        j = 2
#create a single list containing all prime numbers under a given limit
    j = 1        
    for i in range(2, limit):
        if PrimeList[i] == True:
            Primes.append(i)
    return Primes


#function to determine if a number is prime
def PrimeCheck(num):
    degree = math.floor(math.log(num,logbase))
    PrimesList = PrimesSorted[degree]
    
    for i in range(len(PrimesList)):
        if PrimesList[i] == num:
            return True
        if PrimesList[i] > num:
            return False

    return False

#generate a list of prime numbers
limit = 1000000
Primes = Sieve(limit)
PrimesSorted = OrderedSieve(limit)

#create variables for tracking the sums and lengths of sequences.
#set values low so they will be exceeded during evaluation
SequenceSum = 1
SequenceLength = 1

#create a running sum variable that can be cycled through in the loops
CurrentSum = 0

for i in range(len(Primes)):
    if Primes[i] < (limit/20): #don't continue search if the lowest prime in sequence is more than a twentieth the limit
        CurrentSum = Primes[i] #start by setting running sum equal to the first value in the sequence

        j = 0

        #i chose to use a while loop instead of a for loop because the condition
        #isn't a property of the index, but of the sum of the full sequence
        while CurrentSum + Primes[i+j] < limit:  #add each consecutive prime until the sum exceeds the limit
            j = j+1  #it just seemed easiest to start with j = 0 and add 1 at the beginning of the loop
            CurrentSum = CurrentSum + Primes[i+j] #add value of next prime number
            if j > SequenceLength:  #make sure the sequence is long enough to be a contender before checking anything
                if PrimeCheck(CurrentSum):  #if it's also prime, then it's the top result so far
                    SequenceSum = CurrentSum
                    SequenceLength = j

print(SequenceSum, "is the sum of ", SequenceLength +1, " consecutive prime numbers.")



        
