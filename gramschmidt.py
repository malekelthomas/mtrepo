import copy
def dotproduct(vect1, vect2):
    dot = 0
    #print(vect1, vect2)
    for i in range(len(vect1)):
        dot+=vect1[i]*vect2[i]
    return dot

def scalarmult(c, vect):
    for i in range(len(vect)):
        vect[i]*=c
    return vect

def add(vect1, vect2):
    v = []
    for i in range(len(vect1)):
        v.append(vect1[i]+vect2[i])
    return v

def sub(vect1, vect2):
    v = []
    for i in range(len(vect1)):
        v.append(vect1[i]-vect2[i])
    return v


def projection(vect, vect2):
    projection1 = [0]*len(vect)
    topdot = dotproduct(vect, vect2)
    botdot = dotproduct(vect,vect)
    v = scalarmult((topdot/botdot), vect)
    projection1 = add(projection1,v)
    #print(projection1)
    return projection1

def projonsub(vect, subspace):
    projection = [0]*len(vect)
    u = subspace[:]
    for i in u:
        topdot = dotproduct(vect, i)
        botdot = dotproduct(i,i)
        v = scalarmult((topdot/botdot), i)
        projection = add(projection,v)
    return projection
        


        
        
        
            
def checkdim(vectorlist):
    for i in range(len(vectorlist)-1):
        if len(vectorlist[i]) != len(vectorlist[i+1]):
            print(vectorlist[i],"Incompatible with dimension",len(vectorlist[i+1]))
            return False
        
    else:
        return True

def checkortho(vectorlist):
    if len(vectorlist) == 1:
        return True
    if checkdim(vectorlist) == True:
        a = {}
        k = 0
        while k < len(vectorlist):
            key = k
            value = vectorlist[k]
            a[key] = value
            k+=1

        for i in a.keys():
            dotproduct1 = 0
            for k in a.keys():
                if k == i:
                    continue
                dotproduct1 = dotproduct(a[i],a[k])
                if dotproduct != 0:
                    return False
        return True
            
def gramschmidt(vectorlist):
    if checkortho(vectorlist) == True:
        print("Gram-Schmidt not required.")
    elif input("Basis not orthogonal. Create orthogonal basis? Y or N:") == "Y":
        
        a = {}
        k = 0
        while k < len(vectorlist):
            key = k
            value = vectorlist[k]
            a[key] = value
            k+=1
        
        orthobase = [a[0][:]]
        
        j = 0
        while j <len(orthobase):
            z = orthobase[:]
            if j+1 not in a.keys():
                break
            if len(z) == 1:
                g = projection(copy.deepcopy(z[0]),a[1])
                f = sub(a[1],g)
                z.append(f)
            else:
                g = projonsub(a[j+1][:], copy.deepcopy(z))
                f = sub(a[j+1][:],g[:])
                z.append(f[:])

                    
                    
            j+=1
            orthobase = z[:]
                
        for i in range(len(orthobase)):
            print("x"+str(i), end = ' ')
            for j in range(len(orthobase[i])):
                print(orthobase[i][j], end=' ')
            print()
                           

def inputlists(num):
    vects = []
    for i in range(num):
        g = (input("Enter vector: "))
        z = []
        for i in g:
            if i != ' ':
                z.append(int(i))
        vects.append(z)
    return vects

def printvect(vect):
    for i in vect:
        print(i)
    
                    
                                     
                    
            
        


def main():
    g = int(input("How many vectors?: "))

    vects = inputlists(g)
    gramschmidt(vects)

    
                     
            
        


if __name__ == "__main__":
    main()


    
    
