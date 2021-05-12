n, m = input().split()
n = int(n)
m = int(m)
cd = []

for i in range(1, n+1):
	if n % i == 0 and m % i == 0:
		cd.append(i)
		
print(cd)
