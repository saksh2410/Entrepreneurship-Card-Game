// Missing number from the given array  
#include<iostream>
#include<string.h>
#include<vector>

using namespace std;

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        
        bool pos[10000] = {0};
        for(int i=0; i< nums.size(); i++)
        {
            pos[nums [i]] = 1;
        }

        for(int i=0; i< nums.size(); i++)
        {
            if(pos[i] == 0)
                return i;
        }
        return nums.size();
    }
};
int main()
{
   vector<int>nums;
   
   
}