def testpas():
    while True:
        c=0
        
        print("Input your password")
        a=input()
        print("Confirm your password")
        b=input()
        for i in a:
            c+=1
        if c<8:
            print("Too short")
            testpas()
            break
        elif "123" in a:
            print("Too simple")
            
            testpas()
            break
        elif a!=b:
            print("Passwords doesn't match")
            testpas()
            break
        else:
            print("Ok")
            return 1
            
        
testpas()  