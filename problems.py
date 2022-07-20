# dict={}
# st=input("enter string:")
# for i in st:
#     # if(dict.get(i)):
#     #       dict[i]=dict.get(i)+1
#     # else:
#      #     dict[i]=1
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1    
# print(dict)


# dict={}
# st=input("enter string:")
# s=st.casefold()
# for i in s:
#     # if(dict.get(i)):
#     #       dict[i]=dict.get(i)+1
#     # else:
#      #     dict[i]=1
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1    
# print(dict)


# lst=[]
# while True:
#     a=input("enter op")
#     b=a.split()
#     if(b[0]=='stop'):
#         break
#     elif(b[0]=='push'):
#         lst.append(b[1])
#         print(lst)
#     elif(b[0]=='pop'):
#         lst.remove(b[1])
#         print(lst)
#     elif(b[1] in  lst):
#         print("element does not exist")    
#     else:
#         print("wrong op")    
        
dict={}
while True:
    a=input()
    b=a.split()
    if(b[0]=='stop'):
        break
    if(b[0] in dict):
        dict[b[0]]= dict[b[0]].union({b[1]})
        print(dict)
    else:
        dict[b[0]]={b[1]}
        print(dict)
print(dict)
