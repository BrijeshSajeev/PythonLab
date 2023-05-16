infile=open('./sample3.dat','r')
outfile=open('./sample4.dat','w')

s=0
s=infile.read()
print(s)
s= s.split()
print(s)
sum =0
for i in s:
    sum += int(i)

outfile.write(str(sum))
