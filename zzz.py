class Solution:
    def Search(self,arr:list[4,5,6,7,0,1,2],num=4):
            pivot=self.Pivot(arr)
            if pivot==-1:
                return  self.Binary_Search(arr,num,start_index=0,end_index=len(arr)-1)
            if arr[pivot]==num:
                print (pivot)
            if num>=arr[0]:
                return self.Binary_Search(arr,num,start_index=0,end_index=pivot-1)
            return self.Binary_Search(arr,num,start_index=pivot+1,end_index=len(arr)-1)
        
    def Binary_Search(arr,num,start_index,end_index):
            while start_index <= end_index:
                mid_index=start_index+((end_index-start_index)//2)
                mid_num=arr[mid_index]
                if mid_num==num:
                    return mid_index
                if mid_num>num:
                    end_index=mid_index-1
                else:
                    start_index=mid_index+1
            return -1 

    def Pivot(arr):
            start=0
            end=len(arr)-1
            while start <= end:
                mid=start+(end-start)//2
                if arr[mid] > arr[mid+1]:
                    return mid
                if arr[mid] < arr[mid-1]:
                    return mid-1
                if arr[start]>=arr[mid]:
                    end=mid-1
                if arr[start] < arr[mid]:
                    start=mid+1
            return -1
s=Solution()
print(s.Search([4,5,6,7,0,1,2],4))