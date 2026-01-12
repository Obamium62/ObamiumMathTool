import colorama

print("\033[32mOBAMIUMS MATH TOOL V 1 . 0 . 199 \n")
print("\033[31mWarning: If Inputs Are Incorrect e.g a Letter In a Number Input The Program Will Close")

#tools i want to add

#rationalization
#sine rule
#cosinerule
#factorization
#pythagoras
#trig questions

#pre requsite tools
def sqrt(Snum):
    num=2
    while abs(Snum-(num*num))>1e-9:
        num=0.5*(num+(Snum/num))
    return num


def colorGreen():
    print("\033[32m")
def colorBlue():
    print("\033[36m")
def colorOrange():
    print("\033[33m")
def colorPurple():
    print("\033[35m")


#tools
def expander():
    while True:  
        
        colorBlue()
        choice=int(input("1. Expand Double  Brackets \n2. Expand Triple Brackets \n3. Go Back \nEnter your choice: "))
        
        if choice==1:
            print("input each variable value in the form (ax+b)(cx+d)")
            
            colorGreen()

            a=float(input("a: "))
            b=float(input("b: "))
            c=float(input("c: "))
            d=float(input("d: "))
            
            x2var=a*c
            x1var=(b*c+a*d)
            cvar=b*d
            colorPurple()
            print(f"result: {x2var}x^2+{x1var}x+{cvar}")

        if choice==2:
            print("input each variable value in the form (ax+b)(cx+d)(ex+f)")
            
            colorGreen()
            
            a=float(input("a: "))
            b=float(input("b: "))
            c=float(input("c: "))
            d=float(input("d: "))
            e=float(input("e: "))
            f=float(input("f: "))
            print("calculating...")
            x3var=(a*c*f)
            x2var=(b*c*e+a*d*e+a*c*f)
            x1var=(b*d*e+b*c*f+a*d*f)
            cvar=(b*d*f)
            colorPurple()
            print(f"result: {x3var}x^3+{x2var}x^2+{x1var}x+{cvar}")
        if choice==3:
            break


def quadraticSolver():
    
    colorBlue()
    print("give the coefficients in the form ax^2+bx+c")
    
    colorGreen()
    
    a=float(input("a: "))
    b=float(input("b: "))
    c=float(input("c: "))

    #only gotta deal with real roots because sparx yay
    colorPurple()
    
    if (b*b-4*a*c)<0:
        print("No Real Solutions")
        x1="N/A"
        x2="N/A"
    else:
        x1=((-b)+sqrt((b*b-4*a*c)))/2
        x2=((-b)-sqrt((b*b-4*a*c)))/2

    xcoord=-(b/(2*a))
    ycoord=((xcoord*xcoord)*a)+(xcoord*b)+(c)

    yinter=c
    if (b*b-4*a*c)<0:
        print(f"Roots: {x1} and {x2} \nTurning Point: ({round(xcoord,8)},{round(ycoord,8)})\nYintercept (useless): (0,{round(yinter,8)})")
    else:
        print(f"Roots: {round(x1,8)} and {round(x2,8)} \nTurning Point: ({round(xcoord,8)},{round(ycoord,8)})\nYintercept (useless): (0,{round(yinter,8)})")


def nthterm():
    while True:    
        colorBlue()
        print("Choose Squence Type:\n1. Linear\n2. Quadratic\n3. Geometric\n4.Go Back")
        choice=int(input("Selected: "))

        #linear case
        colorGreen()

        if choice==1:
            term1=float(input("term1: "))
            term2=float(input("term2: "))
            term3=float(input("term3: "))
            if (term3-term2)!=(term2-term1):
                colorPurple()
                print("This Sequence Isnt Linear :(")
            else:
                n=term2-term1
                k=term1-(term2-term1)
                colorPurple()
                if k>=0:
                    print(f"nth term: {n}n+{k}")
                else:
                    print(f"nth term: {n}n{k}")
        
        #Quadratic case

        if choice==2:
            
            term1=float(input("term1: "))
            term2=float(input("term2: "))
            term3=float(input("term3: "))

            n2=(0.5*term3-term2+0.5*term1)
            n=(-1.5*term3+4*term2-2.5*term1)
            k=(term3-3*term2+3*term1)

            colorPurple()

            if 2*(n2)!=((term3-term2)-(term2-term1)):
            
                print("This Sequence Is not Quadratic Perhaps Try Geometric")
            
            else:

                if n >=0 and k >=0:
                    print(f"mnth term: {n2}n^2+{n}n+{k}")
                if n < 0 and k >=0:
                    print(f"mnth term: {n2}n^2{n}n+{k}")
                if n >=0 and k < 0:
                    print(f"mnth term: {n2}n^2+{n}n{k}")
                if n < 0 and k < 0:
                    print(f"mnth term: {n2}n^2{n}n{k}")

        #Geometric case

        if choice==3:

            term1=float(input("term1: "))
            term2=float(input("term2: "))
            term3=float(input("term3: "))

            colorPurple()

            if round(sqrt((term3/term1)),8)!=(term2/term1):
            
                print("This Sequence Is not Geometric Perhaps Try Quadratic?")
            
            else:

                print(f"nth term: {term1} x {term2/term1}^n-1")
        
        if choice==4:
            break

#remember to add new tools to the alltools function
def allTools():
    while True:
        colorOrange()
        toolChoice=int(input("select a tool from the list to use: \n1. Bracket Expander\n2. Quadratic Solver\n3. nth term solver\n4. Exit\n tool chosen : "))
        if toolChoice==1:
            expander()
        if toolChoice==2:
            quadraticSolver()
        if toolChoice==3:
            nthterm()
        if toolChoice==4:
            break

allTools()