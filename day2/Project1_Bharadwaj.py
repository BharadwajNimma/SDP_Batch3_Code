l=input("Enter a numbers")
k=l.split(",")
list=[]
for num in range(0,len(k)):
     list.clear()
     sum=0
     isDivisibleBy2=False
     isDivisibleBy3=False
     s=str(k[num])
     if(s[len(s)-1]=="0" or s[len(s)-1]=="5"):
          list.append(5)
          #print(k[num],"is divisible by 5")
     if(s[len(s)-1]=="0" or s[len(s)-1]=="2" or s[len(s)-1]=="4" or s[len(s)-1]=="6" or s[len(s)-1]=="8"):
          list.append(2)
          #print(k[num],"is divisible by 2")
          isDivisibleBy2=True
     c=k[num]
     while(len(c)>1):
         for i in c:
             sum+=int(i)
         c=str(sum)
     if(c=="3" or c=="9" or c=="6"):
          list.append(3)
          #print(k[num],"is divisible by 3")
          isDivisibleBy3=True
     if(s[len(s)-2]=="0" or s[len(s)-2]=="2" or s[len(s)-2]=="4" or s[len(s)-2]=="6" or s[len(s)-2]=="8"):
          if(s[len(s)-1]=="0" or s[len(s)-1]=="4" or s[len(s)-1]=="8"):
               list.append(4)
              #print(k[num],"is divisible by 4") 
     if(s[len(s)-2]=="1" or s[len(s)-2]=="3" or s[len(s)-2]=="5" or s[len(s)-2]=="7" or s[len(s)-2]=="9"):
          if(s[len(s)-1]=="2" or s[len(s)-1]=="6"):
               list.append(4)
              #print(k[num],"is divisible by 4")
     if(isDivisibleBy2==True and isDivisibleBy3==True):
          list.append(6)
          #print(k[num],"divisible by 6")
     if(c=="9"):
          list.append(9)
        #print(k[num],"is divisible by 9")
     c=k[num]
     while(len(c)>1):
          a=int(c[:-1])
          b=int(c[-1])
          c=a*2+b
          c=str(c)
     if(c=="0" or c=="8"):
          list.append(8)
          #print(k[num],"is divisible by 8")
     c=k[num]
     while(len(c)>2):
          temp2=int(c[:-1])
          temp3=int(c[-1])
          c=temp2-2*temp3
          c=str(c)
     if(c=="0" or c=='7'):
          list.append(7)
         #print(k[num],"is divisible by 7")
     for z in range(len(list)):
          print(k[num],"is divisible by",list[z],end=' ')
     
     
          

          
    


    
    

    
    
    
