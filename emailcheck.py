email = input("Enter your Email : ") #g@g.c/i, royrinku343@gmail.com
k,p,end = 0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if email[-4]=="." or email[-3]==".":
                for i in email:
                    if i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            p=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        end = 1
                if k==1 or p==1 or end==1:
                    print("Wrong email 5")
                else:
                    print("Email is Right")
            else:
                print("Wrong email 4")
        else:
            print("wrong Email 3")
    else:
        print("Wrong Email 2")
else:
    print("Wrong Email 1")
