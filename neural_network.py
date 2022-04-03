# # complexity O(N)
# class Solution:
   
#    def check(self,A,B,N):
#        isSame = True
       
#        A = sorted(A)
#        B = sorted(B)
       
#        for i,j in zip(A,B):
#            if ( i != j):
#                isSame = False
#                break
       
#        return isSame


# x=[1,3,2,5,2]
# y=x[::-1]
# print(y)
# arr=[1,2,3,4,45]
# x=arr
# print(x)

# x=[1,2,3,4,3,3]
# print(x.count(3))
# print(x.index(3))
# for i in range(2):
#     print(x.index(3))
# i=0
# y=x.count(3)
# while(i<2):
#     if :
#         i+=1
# print(i)
    
# Python3 implementation to
# find first element
# occurring k times

# function to find the
# first element occurring
# k number of times
def firstElement(arr, n, k):

	# dictionary to count
	# occurrences of
	# each element
	count_map = {}
	for i in range(0, n):
		if k in count_map.keys():
            x=count_map.get(2)
            return
	
	# for i in range(0, n):
		
	# 	# if count of element == k ,
	# 	# then it is the required
	# 	# first element
	# 	if (count_map[arr[i]] == k):
	# 		return arr[i]
	# 	i += 1
			
	# no element occurs k times
	return -1

# Driver Code
if __name__=="__main__":

	arr = [1, 7, 4, 3, 4, 8, 7]
	n = len(arr)
	k = 2
	print(firstElement(arr, n, k))

# This code is contributed
# by Abhishek Sharma
