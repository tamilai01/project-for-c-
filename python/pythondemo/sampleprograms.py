
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
snake=['so waste','so irritated','juzt look','vomit']
sri.extend(snake)
print(sri)
sri.clear()
print(sri)