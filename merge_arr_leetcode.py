
# def merge(arr):
#     new_arr = []
#     count = len(arr)-1
#     for i in range(count):
#         if arr[i][-1] >= arr[i+1][0]:
#             new_arr.append([arr[i][0],arr[i+1][-1]])
#             # arr.pop(i)
#             # arr.pop(i)
#             # count= len(arr)
#         else:
#             new_arr.append(arr[i])

#     return new_arr



def merge(arr,new_arr=[]):
    if len(arr)== 0 :
        return new_arr
    if len(arr) == 1 :
        new_arr.append(arr[0])
        return new_arr
    if (arr[0][-1] >= arr[1][0]) and (arr[0][-1] < arr[1][1]):
        new_arr.append([arr[0][0],arr[1][-1]])
        arr.pop(0)
        arr.pop(0)
    else :
        new_arr.append(arr[0])
        arr.pop(0)
    return merge(arr=arr,new_arr=new_arr)
print(merge([[1,3],[2,6],[8,10],[15,18]]))

        