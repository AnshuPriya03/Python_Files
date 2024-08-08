m1=int(input("Enter marks of test1:"))
m2=int(input("Enter marks of test2:"))
m3=int(input("Enter marks of test3:"))

if m1<=m2 & m1<m3:
    agmarks=(m2+m3)/2
elif m2<=m1 & m2<m3:
    agmarks=(m1+m3)/2
elif m3<=m2 & m3<m1:
    agmarks=(m2+m1)/2

print("avgmarks of best of two tests is", agmarks);