class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # to get the smaller array
        if len(nums1) <= len(nums2):
            x = nums1 
            y = nums2
        else:
            x = nums2
            y = nums1
        
        # case 1: if one array is empty
        
        if len(x) == 0:
            if len(y)%2 == 0:
                return (y[len(y)//2-1] + y[len(y)//2])/2
            else:
                return y[len(y)//2]
    
        # Set the boundaries for binary search
        
        lx =0 
        rx = len(x)
        
        # partition the array 
        
        subarrayx = (lx + rx) //2
        subarrayy = (len(x)+len(y)+1) //2 - subarrayx
        
        while True:
        
        # Case 2: x[subarrayx..] or y[..subarrayy] is empty, preventing access error
            if subarrayx == len(x) or subarrayy == 0:
                # The second comparison from (2) i automatically satified
                if x[subarrayx-1] <= y[subarrayy]:
                    if (len(x)+len(y))%2 == 1:
                        # y[..subarrayy] empty
                        if subarrayy == 0:
                            return x[subarrayx-1]
                        else:
                            return max(x[subarrayx-1],y[subarrayy-1]) 
                    else:
                        # x[subarrayx..] and y[..subarrayy] are empty
                        if subarrayy == 0 and subarrayx == len(x):
                            return (x[subarrayx-1] + y[subarrayy])/2
                        # y[..subarrayy] empty
                        elif subarrayy == 0:
                            return (x[subarrayx-1] + min(y[subarrayy],x[subarrayx]))/2
                        #x[subarrayx..] empty
                        else:
                            return (max(x[subarrayx-1],y[subarrayy-1]) + y[subarrayy])/2
                else:
                    #IMPORTANT Rx goes with -1 in binary search!
                    rx = subarrayx-1

            #case 3
            elif subarrayx == 0 or subarrayy == len(y):
                if x[subarrayx] >= y[subarrayy-1]:
                    if (len(x)+len(y))%2 == 1:
                        if subarrayx == 0:
                            return y[subarrayy-1]
                        else:
                            return max(x[subarrayx-1],y[subarrayy-1]) 
                    else:
                        if subarrayy == len(y) and subarrayx == 0:
                            return (x[subarrayx] + y[subarrayy-1])/2
                        elif subarrayx == 0:
                            return (y[subarrayy-1] + min(y[subarrayy],x[subarrayx]))/2
                        else:
                            return (max(x[subarrayx-1],y[subarrayy-1]) + x[subarrayx])/2

                else:
                    #IMPORTANT Lx goes with +1 in binary search!
                    lx = subarrayx+1

            # Case 3
            else:
                # We are done
                if (x[subarrayx-1] <= y[subarrayy] and x[subarrayx] >= y[subarrayy-1]):
                    if (len(x)+len(y))%2 == 1:
                        return max(x[subarrayx-1], y[subarrayy-1])
                    else:
                        return (max(x[subarrayx-1], y[subarrayy-1])+min(x[subarrayx], y[subarrayy]))/2
                # We need go to the left
                elif x[subarrayx-1] > y[subarrayy]:
                    rx = subarrayx-1
                # We need to go to the right
                else:
                    lx = subarrayx+1
                    
            # Adjust for binary search
            subarrayx = (rx + lx)//2
            subarrayy = (len(x)+len(y)+1)//2 - subarrayx
            