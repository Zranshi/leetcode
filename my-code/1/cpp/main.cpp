#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
  vector<int> twoSum(vector<int>& nums, int target)
  {
    unordered_map<int, int> hash_table;
    for (int i = 0; i < nums.size(); i++) {
      auto it = hash_table.find(target - nums[i]);
      if (it != hash_table.end()) {
        return { it->second, i };
      }
      hash_table[nums[i]] = i;
    }
    return {};
  }
};

int
main(int argc, char const* argv[])
{
  vector<int> nums = { 2, 7, 11, 15 };
  auto res = Solution().twoSum(nums, 9);
  for (int i = 0; i < res.size(); i++) {
    cout << res.at(i);
  }

  return 0;
}
