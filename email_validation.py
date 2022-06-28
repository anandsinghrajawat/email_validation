email=input("enter your email : ")#g@g.in ,1g@g.in
k,j,d=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@"in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1        
                if k==1 or j==1 or d==1:
                     print("wrong email because email contains either space or upper case letter")
            else:
                print("wrong email because dot must be at second or third position from the end")
        else:
            print("wrong email because email must contain one @")
    else:
        print("wrong email because first letter must be alphabet")
else:
    print("wrong email because lenght must be greater then six")   
    
        