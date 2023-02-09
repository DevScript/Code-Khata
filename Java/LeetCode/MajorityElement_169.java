//LEETCODE PROBLEM
//LEVEL - Easy
//169. Majority Element

/* JAVA ACCEPTED SOLUTION O(n^2) */

class Solution {
    public int majorityElement(int[] nums) {
        int a=nums.length/2;
        
        for(int i=0;i<nums.length;i++)
        {
            int temp=nums[i];
            int count=0;
            for(int j=0;j<nums.length;j++)
            {
                if(nums[j]==temp)
                    count++;
            }
            if(count>a)
                return temp;
        }
        return -1;
        
    }
}

/*
 * Approach : Two for loops. 
 * Iterate through each eleemnt of the nums array. For each element, iterate again through the nums array and count the occurence of that element. 
 * If count is greater than floor(n/2) then the element is the majority element.
 * TC- O(n^2)
 * SC - O(1)
*/
