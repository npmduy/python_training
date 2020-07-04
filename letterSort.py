inStr =input('Input a string: ')

def letterCount(letter, string):
    c=0
    for i in string:
        if i==letter:
            c+=1
    return c

l='A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z'.split(', ')

ansList = []
leastLetter = inStr[0]
c=0

for i in range(len(inStr)):
    for letter in inStr:
        if l.index(letter.upper())<l.index(leastLetter.upper()):
            leastLetter=letter
            
    c=letterCount(leastLetter,inStr)
    ansList.append(leastLetter*c)
    inStr=inStr.replace(leastLetter,'')
    c=0
    try:
        leastLetter=inStr[0]
    except:
        pass
ans = []

for i in range(len(ansList)):
    if ansList[i]!='':
        ans.append(ansList[i])
#for i in range(c):
#    ansList.remove('')
print(ans)
    