# This is the better version

def threeSum(arr):
    ans = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            a = -arr[i]-arr[j]
            if i == j and a == arr[i] and a == arr[j]:
                pass
            else:
                if a in arr and arr[i] != arr[j] and arr[i]<0 and arr[j]>=0 and a > arr[i] and a < arr[j]:
                    ans.append("[ {}, {}, {}]".format(arr[i],arr[j],a))
    return ans
arr = [-3,-2,-1,0,1,2,3,5]
arr.sort

print(threeSum(arr))
