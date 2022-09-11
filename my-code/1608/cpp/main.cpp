#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  int specialArray(vector<int> &nums) {
    sort(nums.begin(), nums.end(), greater<int>());
    int n = nums.size();
    for (size_t i = 1; i <= n; i++) {
      if (nums[i - 1] >= i && (i == n || nums[i] < i)) {
        return i;
      }
    }
    return -1;
  }
};

int main(int argc, char const *argv[]) {
  vector<int> nums = {3, 5};
  cout << Solution().specialArray(nums);
  return 0;
}
