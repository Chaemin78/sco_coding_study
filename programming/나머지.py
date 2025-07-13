rest = []
for i in range(10): 
    num = int(input())
    rest.append(num %42)
    
print(len(set(rest)))