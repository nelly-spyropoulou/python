import random

#******************************
def make_sos(lista):

    for i in range(0,len(lista)-2):
        m=[]
        for j in range(i,i+3):
            m.append(lista[j])
        M.append(m)

    return
#*******************************

#******************************
def count_sos():
    x=0

    for i in range(len(M)):
        temp_string=""
        for j in M[i]:
            temp_string+=j
        if temp_string=="SOS":
            x+=1

    print(times,x)
    return x
#******************************

tot_sos=0

stiles = int(input("Δώσε πλάτος ορθογωνίου (>=3) : "))
grames = int(input("Δώσε ύψος ορθογωνίου (>=3) : "))

for times in range(100):

    M=[] # Master table
    L=[] # ορθογωνίο

    for i in range(grames):
        L1=[]
        for j in range(stiles):
            L1.append("O")
        L.append(L1)

    theseis = (grames * stiles)


    i=0
    while i <  theseis//2:
        x=random.randint(0,theseis-1)
        row=x//stiles
        col=x%stiles
        if L[row][col]=="O":
            L[row][col]="S"
            i+=1


    for row in range(grames):
        print(L[row])
    print()



#***** Horizontal *****
    for row in range(0,grames):
        L1=[]
        for col in range(0,stiles):
            L1.append( L[row][col] )
        if len(L1) > 3:
            make_sos(L1)
        else:
            M.append(L1)

    """
    print("horizontal")
    hor=len(M)
    for i in range(0,hor):
        print(M[i])
    """

    """
            h=0
            for k in range(j,j+4):
                if L[i][k]==1:
                    h+=1
            if h==4:
                hor+=1
            print("grammi",i,"perasma",j,"vrethikan",h,"synolo tetrades",hor)
    """

    #***** Verical *****
##    print("vertical"+"\n")
    for col in range(0,stiles):
        L1=[]
        for row in range(0,grames):
            L1.append(L[row][col])
        if len(L1) > 3:
            make_sos(L1)
        else:
            M.append(L1)


    """
            h=0
            for k in range(i,i+4):
                if L[k][col]==1:
                    h+=1
            if h==4:
                ver+=1
            print("stili",j,"perasma",i,"vrethikan",h,"synolo tetrades",ver)
    """
    """
    ver=len(M)
    for i in range(hor,ver):
        print(M[i])
    print()
    """

    """
    #***** 1η διαγώνιος *****
    print("diagonia 1")


    L1=[]
    for row in range(0,diastash):
        L1.append(L[row][row])
    if len(L1) > 4:
        make_tetrades(L1)
    else:
        M.append(L1)
    """




    row_var=0
    col_var=0
    fl=0


    row=row_var

    for i in range(0,stiles):

        L1=[]
        fl=0
        col=col_var
        while fl==0:
            L1.append(L[row][col])


            row+=1
            col-=1
            if row >= grames or col < 0 :
                fl=1

##        print(L1)
        if len(L1) > 3:
            make_sos(L1)
        elif len(L1) == 3:
            M.append(L1)


        row=0
        col_var+=1

    row_var=1
    col_var=stiles-1
    fl=0
    for i in range(row_var,grames):

        L1=[]
        fl=0

        row=row_var
        col=col_var
        while fl==0:
            L1.append(L[row][col])


            row+=1
            col-=1
            if row >= grames or col < 0 :
                fl=1

##        print(L1)
        if len(L1) > 3:
            make_sos(L1)
        elif len(L1) == 3:
            M.append(L1)


        row_var+=1
        col_var=stiles-1



    #***** 2η διαγώνιος *****
##    print("\n"+"diagonia 2")

    row_var=grames-1
    col_var=0
    fl=0



    for i in range(0,grames):

        L1=[]
        fl=0
        row=row_var
        col=col_var
        while fl==0:
            L1.append(L[row][col])


            row+=1
            col+=1
            if row >= grames or col >= stiles :
                fl=1

##        print(L1)
        if len(L1) > 3:
            make_sos(L1)
        elif len(L1) == 3:
            M.append(L1)


        row_var-=1
        col_var=0

    row_var=0
    col_var=1
    fl=0
    for i in range(1,stiles):

        L1=[]
        fl=0

        row=row_var
        col=col_var
        while fl==0:
            L1.append(L[row][col])


            row+=1
            col+=1
            if row >= grames or col >= stiles :
                fl=1

##        print(L1)
        if len(L1) > 3:
            make_sos(L1)
        elif len(L1) == 3:
            M.append(L1)


        row_var=0
        col_var+=1

    tot_sos += count_sos()

print( tot_sos )
print( round(tot_sos/100,2) )
