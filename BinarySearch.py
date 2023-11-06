def RBS( arr ,l, h,x):
    if (l == h):
        if arr[l]==x:
            return l
        else :
            return -1
    if l <= h:
        mid=(l+h)//2
        if arr[mid]==x:
            return mid
        if arr[mid]>x :
            return RBS(arr,l,(mid-1),x)
        else:
            return RBS(arr,(mid+1),h,x)
    return -1

if __name__ == '__main__':
    arr=[2,3,4,10,40]
    x= 1

    result=RBS(arr,0,len(arr)-1,x)
    if result != -1:
        print("Element present at index:",result)
    else:
        print("Element is not present!")
