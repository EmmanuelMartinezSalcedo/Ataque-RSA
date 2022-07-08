import random
import math

def Euclides(n,m):
    if m==0:
        return n
    else:
        return Euclides(m,(n%m)) 

def EuclidesEXT(n,m):
    if m==0:
        return (n,1,0)
    else:
        (d,x2,y2)=EuclidesEXT(m, n%m)
        (x,y)=(y2,x2-(((n//m)-((n//m)%1))*y2))
        return(d,x,y)

def Inverso(a,n):
    if Euclides(a,n)==1:
        (d,x,y)=EuclidesEXT(a,n)
        return (int(x%n))

def EsCompuesto(a,n2,t,u):
    x= pow(a,u,n2)
    if x == 1 or x == n2 - 1:
        return False
    for i in range(t-1):
        x=pow(x, 2,n2)
        if x == n2 - 1:
            return False
    return True

def MillerRabin(n3,s):
    t2=0
    u2=n3-1
    while u2 % 2 == 0:
        u2 = u2 // 2
        t2 = t2 + 1
    for i in range(s):
        a1 = random.randrange(2, n3)
        if EsCompuesto(a1,n3,t2,u2) == True:
            return False
    return True

def PrimoRandBITS(k,s2):
    while True:
        r=random.randrange(2,pow(2,k),2)
        r=r+1
        aux=MillerRabin(r,s2)
        if aux==True:
            break
        else:
            continue
    return r

def phi(n4):
    r=0
    for i in range(1,n4):
        d=Euclides(i,n4)
        if d==1:
            r=r+1
    return r

def RSA_KEY_GENERATOR(k):
    while True:
        p=PrimoRandBITS(int(k/2),4)
        q=PrimoRandBITS(int(k/2),4)
        if p==q:
            continue
        else:
            break

    n5=p*q
    φ=phi(p)*phi(q)
    
    while True:
        e=random.randrange(2,φ)
        if Euclides(e,φ)==1:
            break
        else:
            continue

    d2=Inverso(e,φ)
    return(n5,e,d2)

def MOD_RSA_KEY_GENERATOR(p,q,e):

    n5=p*q
    phi_euler=phi(p)*phi(q)
    d2=Inverso(e,phi_euler)
    return(n5,e,d2)

def MOD2_RSA_KEY_GENERATOR(n,e):

    phi_euler=phi(n)
    d2=Inverso(e,phi_euler)
    return(n,e,d2)

def SemiprimeFact(n):
    a=0
    b=0
    while n % 2 == 0:
        a=2,
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
     
        while (n % i == 0):
            if a==2:
                b=i
            else:
                a=i
            n = n / i
    
    if n > 2:
        if a==2:
            c=int(n)
        else:
            b=int(n)
        return(a,b)

def EXPMOD(a,x,n):
    if x==0:
        return 1
    elif x%2==0:
        t = EXPMOD(a,x/2,n)
        return ((t*t)%n)
    else:
        t = EXPMOD(a,x-1,n)
        a = a%n
        return ((t*a)%n)

#PREGUNTA 1:
#e=65537
#n=999630013489
#c=747120213790
#(p,q)=SemiprimeFact(n)
#(n,e,d)=MOD_RSA_KEY_GENERATOR(p,q,e)

#m=EXPMOD(c,d,n)
#c=EXPMOD(m,e,n)
#print("m= ",m)
#print("c= ",c)

#PREGUNTA 2:
# e1=7
# e2=11

# c1=35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516052471686245831933544
# c2=35794234179725868774991807832568455403003778024228226193532908190484670252364665786748759822531352444533388184

# n =35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516111204504060317568667

# (a,b,c)=EuclidesEXT(e1,e2)

# aux=Inverso(c2,n)

# m1 = pow(c1,b,n)
# m2 = pow(aux,-1*c,n)

# m=(m1 * m2) % n

# print('m= ',m)

# print('c1= ',pow(m,e1,n))
# print('c2= ',pow(m,e2,n))

#PREGUNTA 3:
