
#leap year ornot not
"""
print("LEAP YEAR OR NOT");
print("*****************");
year=int(input("enter the year to check:"));
if(year%4)==0:
    if(year%100)==0:
        if(year%400)==0:
            print("it is leap year");
        else:
            print("it is not a leap year");
    else:
            print("it is a leap year");
else:
    print("it is not leap year");


"""
#array
#array is a variable used to store multiple values in a single variable

a=['apple','orange','grape']

x=len(a)
print(x)


o=a[2]
print(o)


a[2]='gova'
print(a)


a.append("gova")
print(a)


a.pop(1)
print(a)


a.remove('apple')
print(a)


t=a.count('gova')
print(t)


sri=['so beautiful','so elegant','juzt look','like wow']
snake=['wrost','stupid','donkey','wastegirl']
for x in snake:
    print(x);
for x in "chithuruban":
    print(x)

sri.extend(snake)
print(sri)


sri.clear()
print(sri)

snake.sort();
print(snake)


snake.reverse();
print(snake)

tamil=[1,2,3,4,5,6]
print(tamil)
egdict={
        "snake":"tamil",                                   
        "sri":"mental",
         "year":2003
    }
print(egdict)
print(egdict["year"])

for x in tamil:
    
    if x==6:
        print(x)
i=1
while i<10:
    print(i)
    if(i==8):
        break
    i+=1
    





