n = int(input())
array = input().split()

max = int(array[0])

for i in range(n):
	if int(array[i]) > max:
		max = int(array[i])
		
print(max)
