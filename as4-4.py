import random
words=['dualipa' , 'harrystyles' , 'imaginedragons' , 'theweeknd' , 'coldplay' , 'shawnmendes' , 'halsey' , 'billieeilish' , 'postmalone' , 'lanadelrey' , 'eminem' , 'arianagrande' , 'edsheeran' ]
word=random.choice(words)
word=list(word)
true_chars=['-']*len(word)
print(true_chars)
score=len(word)
print('Singers')
while True :
    char=input('enter a char :')
    for i in range(len(word)) :
        if word[i]==char :
            true_chars[i]=char
    if char not in word :
        score-=1
        print(score)

    print(true_chars)
    if word==true_chars :
        print('you win :) ')
        break
    if score==0 :
        print('you lost :( ')
        break