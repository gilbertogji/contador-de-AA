import re
archivo=input('nombre del archivo:')
fhandle=open(archivo)

#para tomar la secuencia de una cadena y ponerla como un handle seguido
fhA=open('seccuenciadealfapden.txt').read()
sfhA=fhA.split("\n")
y=""
for x in sfhA:
    y=y+x
    #y=secuencia de alfa

#la secuencia de beta la copie sin espacios, directamente
fhB=open('secB.txt').read()
sfhB=fhB.split("\n")
yB=""
for x in sfhB:
    yB=yB+x

fhG=open('secG.txt').read()
sfhG=fhG.split("\n")
yG=""
for x in sfhB:
    yG=yB+x

lstA=[]
lstB=[]
lstG=[]
for x1x in fhandle:
    if "/A" in x1x:
        z=re.findall(':([0-9]+)', x1x)
        if z[0] not in lstA:
            lstA.append(z[0])
    if "/B" in x1x:
        z=re.findall(':([0-9]+)', x1x)
        if z[0] not in lstB:
            lstB.append(z[0])
    if "/G" in x1x:
        z=re.findall(':([0-9]+)', x1x)
        if z[0] not in lstG:
            lstG.append(z[0])
print('residuos en A')
for x3x in lstA:
    x3x=int(x3x)
    print(x3x, y[x3x-1])
print('residuos en B')
for x3x in lstB:
    x3x=int(x3x)
    print(x3x, yB[x3x-1])
print('residuos en G')
for x3x in lstG:
    x3x=int(x3x)
    print(x3x, yG[x3x-1])
