try:
    infile = open("sample.txt", "r")
    outfile = open("desti.txt", "w")
    content = infile.read()
    outfile.write(content)
except FileNotFoundError:
    print("File not found")
except:
    print("opps some thing went worng...")
