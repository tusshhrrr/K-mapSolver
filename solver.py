# Roll No.:2018201
# Name:Tushar
# Section:A
# Group:1
#CSE-IP HW-2
#K-Map minimization



def stringtolist():

    """Changes the input strings into two different lists (i.e. minterms and dontcares
    Precondition:strings are of type m0,m1,m2,...,mn and d0,d1,d2,...dn."""
    global nvar,minterms, dontcares

    minterms=minterms.replace(","," ")   #replacing comma (,) with spaces
    dontcares=dontcares.replace(","," ") #replacing comma (,) with spaces
    minterms=minterms.split()            #spliiting minterms string into minterms list
    dontcares=dontcares.split()          #spliiting dontcares string into dontcares list
    minterms=list(map(int,minterms))     #converting data type from string to int
    dontcares=list(map(int,dontcares))   #converting data type from string to int



def dectobin():
    """Converts the element of minterms and dontcares into binary and appends into a new list binmin"""
    global minterms,dontcares,binmin
    binmin=[]                            #creating an empty list

    minterms.extend(dontcares)           #extending the minterms list
    for c in minterms:
        binm =((bin(c)[2:]))             #using bin function to get the binary of the integer
        if len(binm)==1:
            binm="000"+ binm
        if len(binm)==2:
            binm="00"+ binm
        if len(binm)==3:
            binm="0"+ binm              #making all the binary number of 4 bits
        binmin.append(binm)             #appending binary numbers in the binmin list


def prime2reducer():
    """Creates Prime implicants of size 2 and keeps record of minterms ,the prime implicants are made of"""
    global binmin,bindont,prime2,prime2dec
    prime2=[]                           #keeps the binary representatiion of prime implicants
    prime2dec=[]                        #keeps the minterms in decimal of which the respective prime implicant is made of


    for i in range (len(binmin)):
        y=0                             #Flag to catch the terms which are present in no prime implicant
        for j in range (len(binmin)):
            z = 0                       #Flag to catch that two binary numbers differ at only one place
            for k in range (0,4):



                if binmin[i][k]!=binmin[j][k]:    #comparing bits of the of the binary numbers
                    x=k                           #index of the different bit

                    z=z+1

            if z == 1:                           #checking if they differ only by 1
                y=y+1

                if x==0:
                    r="-"+binmin[i][1:]          #replacing the different bit with "-"
                elif x==3:
                    r=binmin[i][:3]+"-"          #replacing the different bit with "-"
                else:
                    r=binmin[i][:x]+"-"+binmin[i][x+1:]     #replacing the different bit with "-"
                if r in prime2:                             #checking if prime implicant already present in list
                    prime2=prime2
                else:
                    prime2.append(r)                        #appending the prime implicant if not present
                    prime2dec.append([minterms[i],minterms[j]])    #appending the list of respective minterms of prime implicants

        if y==0:                                            #if any binary term isn't icluded in a prime implicant
            prime2.append(binmin[i])                        #appending binary term in the list
            prime2dec.append([minterms[i]])                 #appending its respective minterm



def prime4reducer():
    """Creates Prime implicants of size 4 and keeps record of minterms ,the prime implicants are made of"""
    global prime2,prime4,prime4dec
    prime4=[]                                              #keeps the binary representatiion of prime implicants
    prime4dec=[]                                           #keeps the minterms in decimal of which the respective prime implicant is made of


    for i in range(len(prime2)):
        y = 0                                              #Flag to catch the terms which are present in no prime implicant of size 4
        for j in range(len(prime2)):
            z = 0                                          #Flag to catch that two binary numbers differ at only one place
            for k in range(0, 4):

                if prime2[i][k] != prime2[j][k]:           #comparing bits of the of the binary numbers
                    x = k                                  #index of the different bit

                    z = z + 1

            if z == 1:                                     #checking if they differ only by 1
                y = y + 1

                if x == 0:
                    r = "-" + prime2[i][1:]                #replacing the different bit with "-"
                elif x == 3:
                    r = prime2[i][:3] + "-"                #replacing the different bit with "-"
                else:
                    r = prime2[i][:x] + "-" + prime2[i][x + 1:]     #replacing the different bit with "-"
                if r in prime4:                            #checking if prime implicant already present in list
                    prime4 = prime4
                else:
                    prime4.append(r)                       #appending the prime implicant if not present
                    prime4dec.append(prime2dec[i]+prime2dec[j])       #appending the list of respective minterms of prime implicants

        if y == 0:                                      #if any binary term or prime implicant of size 2 isn't icluded in a prime implicant of size 4
            prime4.append(prime2[i])                    #appending prime implicant of size 2 and binary terms in the list
            prime4dec.append(prime2dec[i])              #appending its respective minterms




def prime8reducer():
    """Creates Prime implicants of size 8 and keeps record of minterms ,the prime implicants are made of"""
    global prime4,prime8,prime8dec
    prime8=[]                  #keeps the binary representatiion of prime implicants
    prime8dec=[]               #keeps the minterms in decimal of which the respective prime implicant is made of

    for i in range(len(prime4)):
        y = 0                  #Flag to catch the terms which are present in no prime implicant of size 4
        for j in range(len(prime4)):
            z = 0              #Flag to catch that two binary numbers differ at only one place
            for k in range(0, 4):

                if prime4[i][k] != prime4[j][k]:       #comparing bits of the of the binary numbers
                    x = k                #index of the different bit

                    z = z + 1

            if z == 1:                    #checking if they differ only by 1
                y = y + 1

                if x == 0:
                    r = "-" + prime4[i][1:]          #replacing the different bit with "-"
                elif x == 3:
                    r = prime4[i][:3] + "-"          #replacing the different bit with "-"
                else:
                    r = prime4[i][:x] + "-" + prime4[i][x + 1:]     #replacing the different bit with "-"
                if r in prime8:                       #checking if prime implicant already present in list
                    prime8 = prime8
                else:
                    prime8.append(r)                    #appending the prime implicant if not present
                    prime8dec.append(prime4dec[i] + prime4dec[j])          #appending the list of respective minterms of prime implicants

        if y == 0:                                    #if any binary term or prime implicant of size 2 or prime implicant of size 4 isn't icluded in a prime implicant of size 8
            prime8.append(prime4[i])                  #appending that term in the list
            prime8dec.append(prime4dec[i])            #appending its respective minterms




def prime16reducer():
    """Creates Prime implicants of size 16 and keeps record of minterms ,the prime implicants are made of"""
    global prime8,prime16,prime16dec
    prime16=[]                                           #keeps the binary representatiion of prime implicants
    prime16dec=[]                                        #keeps the minterms in decimal of which the respective prime implicant is made of


    for i in range(len(prime8)):
        y = 0                                                   #Flag to catch the terms which are present in no prime implicant of size 16
        for j in range(len(prime8)):
            z = 0                                               #Flag to catch that two binary numbers differ at only one place
            for k in range(0, 4):

                if prime8[i][k] != prime8[j][k]:                        #comparing bits of the of the binary numbers
                    x = k                                               #index of the different bit

                    z = z + 1

            if z == 1:                                                  #checking if they differ only by 1
                y = y + 1

                if x == 0:
                    r = "-" + prime8[i][1:]                              #replacing the different bit with "-"
                elif x == 3:
                    r = prime8[i][:3] + "-"                              #replacing the different bit with "-"
                else:
                    r = prime8[i][:x] + "-" + prime8[i][x + 1:]          #replacing the different bit with "-"
                if r in prime16:                                   #checking if prime implicant already present in list
                    prime16 = prime16
                else:
                    prime16.append(r)                                   #appending the prime implicant if not present
                    prime16dec.append(prime8dec[i]+prime8dec[j])        #appending its respective minterms

        if y == 0:                                #if any binary term or prime implicant of size 2,4,8 isn't icluded in a prime implicant of size 4
            prime16.append(prime8[i])                #appending that term in the list
            prime16dec.append(prime8dec[i])          #appending its respective minterms

def dontcareimplemt(string1,string1dec):
    """Implemets the whole don't care thing and removes the redundant don't care terms
    string1 is list of prime implicants.
    string1dec is the list of minterms of the respective prime implicants"""

    p1 = -1                    # index in string1dec
    for c in string1dec:
        p1 = p1 + 1
        p = 0;z=0              #flags for keeping count of don't cares and repeated minterms in a prime implicant
        for i in range(len(c)):
            y = 0;u=0          #flags for making sure they don't get counted more than once
            for k in range(len(string1dec)):

                if c[i] in dontcares: #if found element in dontcares
                    y = y + 1
                    if y == 1:     #if counted once
                        p = p + 1  #increase p by 1
                elif c!=string1dec[k]: # if current minterms is not equal to selected minterms
                    if c[i] in string1dec[k]:  #if found element in minterms list
                        u=u+1
                        if u==1:        #if counted once
                            z=z+1       #increase z by 1


        if p >= 1 and p+z== len(c):
            string1dec[p1] = ["*"]       #replacing redundant don'tcare terms in minterm list
            string1[p1] = ["*"]          #replacing redundant don'tcare terms in prime implicant list





def removeredundant(string2,string2dec):
    """ removes the redundant terms
        string2 is list of prime implicants.
        string2dec is the list of minterms of the respective prime implicants"""
    q = -1                 # index of string2dec
    for c in string2dec:
        q = q + 1
        flag = []           #flag list to keep count how many times respective terms are repeated
        for i in range(len(c)):
            coun = 0         #counts the no. of times a particular minterm is repeated
            for k in range(len(string2dec)):
                coun += string2dec[k][:].count(c[i])
            flag.append(coun)   #appending count to the list
        di = 0   #for counting how many terms are repeated more than once
        for c in flag:
            if c > 1:
                di = di + 1
        if di == len(flag):   #if all the terms are repeated more than once
            string2dec[q] = ["*"]      #replacing redundant don'tcare terms in minterm list
            string2[q] = ["*"]         #replacing redundant don'tcare terms in prime implicant list







def var2outp():
    """Removes["*"] terms and does formatting of the ouput for 2 vriable K map """
    global output, prime4, prime4dec,prime41dec,prime42dec,prime41,prime42,stringOut
    prime41dec=[]          #new lists to hold prime implicats and minterms after removing redundant terms
    prime42dec=[]
    prime41 = []
    prime42 = []
    dontcareimplemt(prime4,prime4dec)   #removing redundant don't care terms


    for c in prime4dec:    #removing ["*"] terms and appending them to a new list
        if c!=["*"]:       #if term not equal to ["*"]
            prime41dec.append(c)    #append to the new list
    for c in prime4:        #removing ["*"] terms and appending them to a new list
        if c!=["*"]:        #if term not equal to ["*"]
            prime41.append(c)    #append to the new list

    removeredundant(prime41,prime41dec)      #removing redundant terms




    for c in prime41dec:    #removing ["*"] terms and appending them to a new list
        if c!=["*"]:        #if term not equal to ["*"]
            prime42dec.append(c)     #append to the new list
    for c in prime41:        #removing ["*"] terms and appending them to a new list
        if c!=["*"]:          #if term not equal to ["*"]
            prime42.append(c)   #append to the new list
    if prime42 == [] :  #if resultant prime implicant list is empty
        output.append("0")                    #output is zero


    else:
        for c in prime42:

            if c[2:]!="--":     #if last two bits are not dashes
                if c[2]=="0":   #if 3rd bit is 0
                    bit="w'"
                elif c[2]=="1":  # if 3rd bit is 1
                    bit="w"
                elif c[2]== "-": #if 3rd bit is "-"
                     bit=""
                if c[3]=="0":
                    bit=bit + "x'"
                elif c[3]=="1":
                    bit=bit + "x"
                elif c[3]=="-":
                    bit=bit+""

                output.append(bit)                   #bit is the character represntation of 1 minterm


            else:
                output.append("1")                    #output is 1 if last two places of minterm are the dashesm.
    output.sort()  # sorting the terms lexographically
    for c in output:
        if stringOut == "":
            stringOut = c
        else:
            stringOut = stringOut + "+" + c  # joining results of the different minterms





def var3outp():
    """Removes["*"] terms and does formatting of the ouput for 3 vriable K map """
    global output, prime8, prime8dec,prime81dec,prime81,prime82dec,prime82,stringOut
    prime81dec = []        #new lists to hold prime implicats and minterms after removing redundant terms
    prime81=[]
    prime82=[]
    prime82dec = []
    dontcareimplemt(prime8,prime8dec)        #removing redundant don't care terms
    for c in prime8dec:                #removing ["*"] terms and appending them to a new list
        if c!=["*"]:                   #if term not equal to ["*"]
            prime81dec.append(c)       #append to the new list
    for c in prime8:                   #removing ["*"] terms and appending them to a new list
        if c!=["*"]:                   #if term not equal to ["*"]
            prime81.append(c)          #append to the new list
    removeredundant(prime81,prime81dec)      #removing redundant terms
    for c in prime81dec:                #removing ["*"] terms and appending them to a new list
        if c!=["*"]:                    #if term not equal to ["*"]
            prime82dec.append(c)        #append to the new list
    for c in prime81:                   #removing ["*"] terms and appending them to a new list
        if c!=["*"]:                    #if term not equal to ["*"]
            prime82.append(c)           #append to the new list
    if prime82 == []:   #if resultant prime implicant list is empty
        output.append("0")                       #output is zero
    else:
        for c in prime82:
            if c[1:] != "---":              #if last three bits are not dashes
                if c[1] == "0":             #if 2nd bit is 0
                    bit = "w'"
                elif c[1] == "1":           #if 2nd bit is 1
                    bit = "w"
                elif c[1] == "-":           #if 2nd bit is -
                    bit = ""
                if c[2] == "0":
                    bit = bit + "x'"
                elif c[2] == "1":
                    bit = bit + "x"
                elif c[2] == "-":
                    bit = bit + ""
                if c[3] == "0":
                    bit = bit + "y'"
                elif c[3] == "1":
                    bit = bit + "y"
                elif c[3] == "-":
                    bit = bit + ""

                output.append(bit)                 #bit is the character represntation of 1 minterm

                    # Formatting in terms of a ,b and c instead of 0,1 and -.
            else:
                output.append("1")       #output is 1 if last three places of minterm are the dashes.
    output.sort()  # sorting the terms lexographically
    for c in output:
        if stringOut == "":
            stringOut = c
        else:
            stringOut = stringOut + "+" + c  # joining results of the different minterms





def var4outp():
    """Removes["*"] terms and does formatting of the ouput for 4 vriable K map """
    global output,prime16,prime16dec,prime161dec,prime162dec,prime151,prime162,stringOut
    prime161dec = []      #new lists to hold prime implicats and minterms after removing redundant terms
    prime161 = []
    prime162 = []
    prime162dec = []
    dontcareimplemt(prime16,prime16dec)     #removing redundant don't care terms

    for c in prime16dec:                    #removing ["*"] terms and appending them to a new list
        if c!=["*"]:                        #if term not equal to ["*"]
            prime161dec.append(c)           #append to the new list
    for c in prime16:                       #removing ["*"] terms and appending them to a new list
        if c!=["*"]:                        #if term not equal to ["*"]
            prime161.append(c)              #append to the new list

    removeredundant(prime161,prime161dec)   #removing redundant terms
    for c in prime161dec:                   #removing ["*"] terms and appending them to a new list
        if c!=["*"]:                        #if term not equal to ["*"]
            prime162dec.append(c)           #append to the new list
    for c in prime161:                      #removing ["*"] terms and appending them to a new list
        if c!=["*"]:                        #if term not equal to ["*"]
            prime162.append(c)              #append to the new list
    if prime162 == []:   #if resultant prime implicant list is empty and don'tcares list is not empty
        output.append("0")                         #output is zero
    else:
        for c in prime162:
            if c[:] != "----":               #if all the bits are not dashes
                if c[0] == "0":              #if 1st bit is 0
                    bit = "w'"
                elif c[0] == "1":             #if 1st bit is 1
                    bit = "w"
                elif c[0] == "-":             #if 1st bit is -
                    bit = ""
                if c[1] == "0":
                    bit = bit + "x'"
                elif c[1] == "1":
                    bit = bit + "x"
                elif c[1] == "-":
                    bit = bit + ""
                if c[2] == "0":
                    bit = bit + "y'"
                elif c[2] == "1":
                    bit = bit + "y"
                elif c[2] == "-":
                    bit = bit + ""
                if c[3] == "0":
                    bit = bit + "z'"
                elif c[3] == "1":
                    bit = bit + "z"
                elif c[3] == "-":
                    bit = bit + ""

                output.append(bit)                #bit is the character represntation of 1 minterm

                    # Formatting in terms of a,b,c and d instead of 0,1 and -.

            else:

               output.append("1")            #output is 1 if  all bits of minterm are the dashes.

    output.sort()             #sorting the terms lexographically
    for c in output:
        if stringOut=="":
            stringOut=c
        else:
            stringOut=stringOut+ "+" + c  #joining results of the different minterms



def minFunc(numVar, stringIn):
    """Changes input string into minterm and dontcare strings separately
    numVar is no. of variables.
    stringIn is a string of the format (a0,a1,a2, ...,an) d(d0,d1, ...,dm)"""
    global nvar,minterms,dontcares,output,stringOut
    stringOut=""
    output=[]
    nvar=numVar
    e=stringIn.index(")")     # index of first ")"
    minterms=stringIn[1:e]    #slicing string for the minterm
    d=stringIn.index("(",e)   #index of first "(" after index e.
    dontcares=stringIn[d+1:-1]   #slicing string for the dontcares
    stringtolist()
    dectobin()
    prime2reducer()
    prime4reducer()
    prime8reducer()
    prime16reducer()
    if nvar==2:
        var2outp()
    if nvar==3:
        var3outp()
    if nvar==4:
        var4outp()

    return stringOut










