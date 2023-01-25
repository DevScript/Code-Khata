#include <bits/stdc++.h>
using namespace std;

int maxSubArray(vector<int> &nums)
{
    // Kadane's algorithm to find the subarray with maximum sum

    int max_sum = INT_MIN; // this will store the maximum sum of the subarray
    int curr_sum = 0;

    // traveersing the entire vector for finding the max sum subarray
    for (int elem : nums) 
    {
        curr_sum += elem; // updating the current sum

        if (curr_sum > max_sum) // found a subarray with a greater sum
            max_sum = curr_sum;

        if (curr_sum < 0) // this elem would not contribute to the max sum subarray array
            curr_sum = 0;
    }

    return max_sum;
}

int main()
{
    int n;
    cin >> n;
    vector<int> v(n);
    for (int i = 0; i < n; i++)
    {
        cin >> v[i];
    }

    int max_sum = maxSubArray(v);
    cout<<max_sum<<endl;

    return 0;
}