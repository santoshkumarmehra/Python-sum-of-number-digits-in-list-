arr=[143,15,27,365412344,4326]
new_arr=[]

for i in arr:
	str_ele=str(i)
	sum=0
	for j in str_ele:
		sum=sum+int(j)
	new_arr.append(sum)

print(arr)
print(new_arr)
