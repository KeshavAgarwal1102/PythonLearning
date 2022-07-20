# from pickle import APPEND


# fname='keshav'
# if fname=="Keshav".lower():
#     print("True")
# else:
#     print("false")    
# f1name='keshav'
# if(fname=='keshav' and f1name=='Keshav'):
#     print("true")
# else:
#     print("false") 
# # if(fname=='keshav' && f1name=='Keshav'):
# #     print("true")
# # else:
# #     print("false")   
# if(fname=='keshav' and not f1name=='Keshav'):
#     print("true")
# else:
#     print("false")       
# if(fname=='keshav'):
#     print("FirstName")
# elif(fname=='Keshav'):
#     print("yes")          


# if 'keshav' in [1,2,3,'keshav']:
#     print("keshav in the list")
# elif 'a' in 'Keshav':
#     print("char found")
# else:
#     print("nothing is good")     


# #input from user and print the chars whose ascii value in even
# name=input("enter string :")
# for i in name:
#     print(ord(i))
#     if(ord(i)%2==0):
#         print("value is even for "+i)
# print(ord(" "))    
# if(name is fname):
#     print("true")
# else:
#     print("false")   


#take n input from user and append them to list
# lst=[]
# n=int(input("enter the no of inputs"))
# for i in range(0,n):
#     a=input()
#     lst.append(a),lst.count('a')
# print(lst.count(2))
# print(lst)
a=int(input("Enter a number"))
dict={}
for i in range(1,2*a+1):
    if(i%2!=0):
       b=input()
       lst=[]
       dict={
        b:lst
       }

    
    else:
        c=input()
        dict[b].append(c)

print(dict)

