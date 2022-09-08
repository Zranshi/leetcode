#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
  int singleNumber(vector<int>& nums)
  {
    int ans = 0;
    for (size_t i = 0; i < 32; i++) {
      int total = 0;
      for (int num : nums) {
        total += ((num >> i) & 1);
      }
      if (total % 3) {
        ans |= (1 << i);
      }
    }
    return ans;
  }
};

int
main(int argc, char const* argv[])
{
  vector<int> nums = { 2, 2, 3, 2 };
  auto res = Solution().singleNumber(nums);
  cout << res;
  return 0;
}
