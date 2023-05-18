infile= open('./sample.txt','r')
outfile=open('./sample2.txt','w')
lines=chars=0
for line in infile:
    lines +=1
    chars +=len(line)
    outfile.write(line)

print(lines,chars)