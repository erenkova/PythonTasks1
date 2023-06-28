s=input()
m=s.count("ический")
f=s.count("ическая")
n=m+f
print(s.replace(("ический" or "ическая"), ".", n))