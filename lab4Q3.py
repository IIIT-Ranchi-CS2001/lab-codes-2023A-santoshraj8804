CourseCODE=[ "CS-2001","MA-2001","CS-2003","CS-2005"]
CourseName=["PYTHON","MATHS","ARCHITECTURE","THEORY OF COMPUTATION"]
l=[]

for i in range(len(CourseCODE)):
    l.append(CourseCODE[i]+":"+CourseName[i])

print(l)