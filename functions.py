# def fun(number):
#     for i in range(1,11):
#        print(number*i)

# fun(5)    


# def makelst(lst):
#     lst.append("keshav")
#     lst.append("agarwal")
#     lst.append("cs")
#     return lst
# lst=[]
# print(makelst(lst))    



# def isString():
#     st=input("Enter String")
#     # if(st.upper()==st):
#     if st.isupper():
#         return True
#     else:
#         return False    

# print(isString())
# def sum_ascii(st):
#     total=0
#     for i in st:
#         total=total+ord(i)      
#     return total

# st=input("enter string")    
# print(sum_ascii(st))

# print(61*121)
# def sum_ascii(st):
#     return sum(map(ord,st))

# st="shivangi"
# print(sum_ascii(st))


#write a function which take two string username and password and return a string which contain first 4 chars of name and last 4 char of password
# def generateString(username,passward):
#     return (username[:4]+passward[-4:])

# username=input("enter user name:")
# passward=input("enter passward:")
# print(generateString(username,passward))


#input a string and check how many times sequence of two consecutive chars are same as orignal alphabet
# def no_of_same_sequence(st):
#     total=0
#     for i in range(0,len(st)-1):
#         if((ord(st[i])+1)==ord(st[i+1])):
#             total+=1
#     return total
# st=input("enter string:")
# print(no_of_same_sequence(st))

#print even number in list
def print_even(lst):
    for i in lst:
        if(i%2==0):
            print(i)
            
lst=[1,2,3,4,5,6,7,8,6,5,6,89,232,374,98534,344821]
print_even(lst)