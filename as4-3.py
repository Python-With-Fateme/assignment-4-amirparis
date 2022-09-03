n=int(input('enter the arraye lenght : '))
x=[]

while len(x)!=n :
    number = float(input('enter your number : '))
    if number%2==0 :
        x.append(number)
print(x)
x.sort()
print('nozouli' , x)
x.sort(reverse=True)
print('soudi' , x)