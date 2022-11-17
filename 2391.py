from dataclasses import replace

garbage = ["G", "P", "GP", "GG"]
travel = [2, 4, 3]
Mnumber = 0
Pnumber = 0
Gnumber = 0
MList = 0
PList = 0
GList = 0
Mtime = 0
Ptime = 0
Gtime = 0
index=0
for item in garbage:
    if "M" in item:
        Mnumber = Mnumber+item.count("M")
        MList = index
    if "P" in item:
        Pnumber = Pnumber+item.count("P")
        PList = index
    if "G" in item:
        Gnumber = Gnumber+item.count("G")
        GList = index
    index=index+1
for index in range(MList):
    Mtime = Mtime+travel[index]
for index in range(PList):
    Ptime = Ptime+travel[index]
for index in range(GList):
    Gtime = Gtime+travel[index]
Gtime=Gtime+Gnumber
Ptime=Ptime+Pnumber
Mtime=Mtime+Mnumber
total=Gtime+Ptime+Mtime
print(total)