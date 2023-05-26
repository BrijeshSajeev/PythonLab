try:
    infile = open("desti.txt", "r")
    outfile = open("sample.txt", "w")
    content = infile.read()
    outfile.write(content)


except FileNotFoundError:
    print("File not found")
except:
    print("opps some thing went worng...")
