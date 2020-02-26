a = raw_input("Create file ooo.txt?")
if a[0] == "y" or a[0]=="Y":
   f = open("ooo.txt", "w")
   f.write("Oooo\nOooo\n")
   f.close()
   print "file created"

a = raw_input("Perform the code?")
if a[0] == "y" or a[0]=="Y":
    f = open("ooo.txt","r+")
    f.seek(1, 0)
    f.write("t")
    print f.read(1)
    f.write("p")
    f.seek(0,0)
    f.write("S")
    f.seek(-5,2)
    f.write("n")
    f.read(1)
    f.write("w!")
    f.close()

