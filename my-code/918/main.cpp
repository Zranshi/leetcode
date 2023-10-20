// @Time     : 2023/07/19 21:44
// @Author   : Ranshi
// @File     : main.cpp
// @Doc      : 918. 环形子数组的最大和
#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  int maxSubarraySumCircular(vector<int> &nums) {
    int n = nums.size();
    deque<pair<int, int>> q;
    int pre = nums[0], res = nums[0];
    q.push_back({0, pre});
    for (int i = 1; i < 2 * n; i++) {
      while (!q.empty() && q.front().first < i - n) {
        q.pop_front();
      }
      pre += nums[i % n];
      res = max(res, pre - q.front().second);
      while (!q.empty() && q.back().second >= pre) {
        q.pop_back();
      }
      q.push_back({i, pre});
    }
    return res;
  }
};

int main() {
  vector<int> nums = {1, 2, 3, 4};
  cout << Solution().maxSubarraySumCircular(nums) << endl;
}
