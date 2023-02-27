def quick_merge(list1, list2):
    result = []

    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):   # прицепление остатка
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]
    
    return result

n = int(input())
list1 = []

for i in range (n):
    i = input()
 
 
    list1.append(i.split())

index = 0
result = []
    
for index in range(n):
    if index>=n-1:
        break

    # result = quick_merge(result,list[index])
    
    # res = quick_merge(list1[index], list1[index+1])
     
    
   
print(result) 

      
    

    

# result = quick_merge(list1, list2)

    

# # list1 = input()
# # list2 = input()
# # list4 = list1.split()
# # list5 = list2.split()
# # list3 = quick_merge(list4, list5)
# # print(*list3)

# list = [[1,2,3],[4,5,6],[7,8,9]]

# list_2 = quick_merge(list[1],list[2])
# print(list_2)