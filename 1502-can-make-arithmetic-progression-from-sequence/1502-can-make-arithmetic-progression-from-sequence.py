class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[0]-arr[1]
        count = 0
        i = 0
        for i in range(len(arr)-1):
            if arr[i]-arr[i+1]==diff:
                count+=1
            if count==(len(arr)-1):
                return True
        return False