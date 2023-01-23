#include <bits/stdc++.h>
using namespace std;

int maxSubArray(vector<int> &nums)
{
    // Kadane's algorithm

    int max_sum = INT_MIN;
    int curr_sum = 0;

    for (int elem : nums)
    {
        curr_sum += elem;

        if (curr_sum > max_sum)
            max_sum = curr_sum;

        if (curr_sum < 0)
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