#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  int numSubarrayProductLessThanK(vector<int> &nums, int k) {
    int n = nums.size(), ret = 0, prod = 1, i = 0;
    for (int j = 0; j < n; j++) {
      prod *= nums[j];
      while (i <= j && prod >= k) {
        prod /= nums[i];
        ++i;
      }
      ret += j - i + 1;
    }
    return ret;
  }
};

int main(int argc, char const *argv[]) {
  vector<int> nums = {10, 5, 2, 6};
  cout << Solution().numSubarrayProductLessThanK(nums, 100);
  return 0;
}
