"""
Author: Jonas Treadwell
File Name: Sort an Array of 0s, 1s, and 2s
Description/Instructions: You don't need to read input or print anything. Your task is to complete the function sort012() that takes an array arr and N as input parameters and sorts the array in-place.
"""

class Solution:
    
    def sort012(self,arr,n):
        low=0
        high=n-1
        mid=0
        

        while mid<=high:
            
            
            if arr[mid]==0:
                arr[mid] , arr[low] = arr[low] , arr[mid]
                mid+=1
                low+=1
                
            
            elif arr[mid]==1:
                mid+=1
                
            
            else:
                arr[mid] , arr[high] = arr[high] , arr[mid]
                high-=1
