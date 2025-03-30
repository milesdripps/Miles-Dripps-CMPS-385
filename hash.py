# CMPS 385: Hash table
#
# Miles Dripps
#
import math

class Hash:
    def __init__(self, size):
        # Hashtable of input size
        self.TABLE_SIZE = size
        self.hashtable = [None] * self.TABLE_SIZE

    def HashFunction(self, value):
        #ensure the values are positive integers
        return int(abs(math.floor(value % self.TABLE_SIZE)))

    def HashInsertion(self, value):
        hash_key = self.HashFunction(value) # Get the key of the value

        valid_insertion = False

        while valid_insertion == False:
            if self.hashtable[hash_key] is None: # if empty spot
                valid_insertion = True
            elif self.hashtable[hash_key] == -1: # if previously deleted spot
                valid_insertion = True
            else: # if spot is taken
                print(f"[ -x ]Collision for {value}. Finding next spot... ")
                hash_key = (hash_key + 1) % self.TABLE_SIZE

        self.hashtable[hash_key] = value #put the value at the new spot
        print(f"[ -> ]{value} placed at index {hash_key}")

    def HashDeletion(self, value):
        hash_key = self.HashFunction(value) # get supposed key from value

        while self.hashtable[hash_key] is not None:
            if self.hashtable[hash_key] == value:       # if there is a match
                print(f"[ X ]{value} deleted from index {hash_key} ")
                self.hashtable[hash_key] = -1
                return 0
            else:
                hash_key = (hash_key + 1) % self.TABLE_SIZE #iterate until key is none
        print(f"[ ! ]{value} not found.")

    def printTable(self):
        print(self.hashtable)



def main():
    #Examples
    hashtable = Hash(20)
    hashtable.HashInsertion(572)
    hashtable.HashInsertion(823)
    hashtable.HashInsertion(7)
    hashtable.HashInsertion(59)
    hashtable.HashInsertion(17)

    hashtable.HashDeletion(823)
    hashtable.HashDeletion(8)
    hashtable.HashDeletion(17)

    #test values with the same modulus of 20(example size)
    hashtable.HashInsertion(823)
    hashtable.HashInsertion(423)
    hashtable.HashDeletion(423)

    hashtable.printTable()

main()