#include <bits/stdc++.h>
using namespace std;

// Time complexity: O(N) -> Linear time
// Space complexity: O(1) -> Constant space

// if no profit can be made, RETURN 0
int maxProfit(vector<int> &prices) {
    int n = prices.size();

    int max_profit = INT_MIN;
    int min_price = prices[0];

    for (int i = 0; i < n; ++i) {
        min_price = min(min_price, prices[i]); // to buy the stock on this day

        int curr_profit = prices[i] - min_price;
        max_profit = max(max_profit, curr_profit); // to sell the stock on this day
    }

    // no profit made
    if (max_profit == INT_MIN)
        max_profit = 0;

    return max_profit;
}

int main() {
    cout<<"Enter n: ";
    int n;
    cin>>n;
    vector<int> v(n);
    cout<<"Enter prices on n days: ";
    for(int i=0; i<n; i++) {
        cin>>v[i];
    }
    // calculate max profit
    int max_profit = maxProfit(v);
    
    cout<<"Max Profit: "<<max_profit<<endl;

    return 0;
}