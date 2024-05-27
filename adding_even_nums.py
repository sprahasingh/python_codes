target = int(input("Enter number till which you want sum of all even numbers:\n"))
total=0
for n in range(2,target+1,2):
  total+=n
print(f"The sum of even numbers till {target} is {total}")
