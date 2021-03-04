upp = open("upp.txt", "w")
afile = open("low.txt", "r")
line = afile.readline()
line = line.upper()
upp.writelines(line)
for line in afile:
  
  line = afile.readline()
  line = line.upper()
  upp.write(line)
