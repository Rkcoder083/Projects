import math
import snumpy


def respo(a):
    if "hi" in a or "hello" in a:
        print("Hi I am matAi.I will help you to solve simple mathematical problem..:)")
    elif "bye" in a or "quit" in a:
        print("Ok bye ,I will wait untill you run me...:)")
        return 1
    elif "sum" in a or "add" in a:
        t=[]
        s=[]
        su=0
        for i in a:
            if i in "0123456789" or i==' ':
                t.append(i)
        w=""
        t.append(" ")
        for i in range(len(t)):
            if t[i] in "01234567890":
               w=w+str(t[i])
            elif t[i]==' ':
                g=w
                if w=='':
                    g='0'
                    continue
                s.append(g)
                w=""
        for  i in s:
            su+=int(i)
        print("THE SUM IS ",su)

    elif "diff" in a or "difference" in a or "sub" in a:
        t = []
        s = []
        for i in a:
            if i in "0123456789" or i == ' ':
                t.append(i)
        w = ""
        t.append(" ")
        for i in range(len(t)):
            if t[i] in "01234567890":
                w = w + str(t[i])
            elif t[i] == ' ':
                g = w
                if w == '':
                    g = '0'
                    continue
                s.append(g)
                w = ""
        su=int(s[0])
        for i in range(1,len(s)):
            su -= int(s[i])
        print("THE DIFFERENCE IS ",su)
    elif "div" in a :
        t = []
        s = []
        su = 0

        for i in a:
            if i in "0123456789" or i == ' ':
                t.append(i)
        w = ""
        t.append(" ")
        for i in range(len(t)):
            if t[i] in "01234567890":
                w = w + str(t[i])
            elif t[i] == ' ':
                g = w
                if w == '':
                    g = '0'
                    continue
                s.append(g)
                w = ""
        print("THE DIVIDED VALUE IS ",int(s[0])/int(s[1]))
    elif "prod" in a or "multi" in a:
        t = []
        s = []
        su = 0

        for i in a:
            if i in "0123456789" or i == ' ':
                t.append(i)
        w = ""
        t.append(" ")
        for i in range(len(t)):
            if t[i] in "01234567890":
                w = w + str(t[i])
            elif t[i] == ' ':
                g = w
                if w == '':
                    g = '0'
                    continue
                s.append(g)
                w = ""
        su=1
        for i in s:
            su *= int(i)
        print("THE PRODUCT IS ",su)
    elif "tan" in a:
        h=[]
        w=""
        for i in a:
            if i in "0123456789":
                h.append(i)
        for i in h:
            w+=i
        l=math.radians(int(w))
        print("THE VALUE IS ",math.tan(l))
    elif "sin" in a:
        h=[]
        w=""
        for i in a:
            if i in "0123456789":
                h.append(i)
        for i in h:
            w+=i
        l=math.radians(int(w))
        print("THE VALUE IS ",math.sin(l))
    elif "cos" in a:
        h=[]
        w=""
        for i in a:
            if i in "0123456789":
                h.append(i)
        for i in h:
            w+=i
        l=math.radians(int(w))
        print("THE VALUE IS ",math.cos(l))

    else:
        print("THE VALUE IS ",eval(a))

while True:
    print("USER: ",end="")
    a=input().strip()
    print("AI:",end="")
    z=respo(a.lower())
    if z==1:
        break