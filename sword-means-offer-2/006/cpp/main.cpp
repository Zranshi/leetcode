#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  vector<int> twoSum(vector<int> &numbers, int target) {
    for (int i = 0, j = numbers.size() - 1; i < j;) {
      if (numbers[i] + numbers[j] < target)
        ++i;
      else if (numbers[i] + numbers[j] > target)
        --j;
      else
        return {i, j};
    }
    return {-1, -1};
  }
};

int main(int argc, char const *argv[]) {
  vector<int> numbers = {1, 2, 4, 6, 10};
  auto res = Solution().twoSum(numbers, 8);
  for (auto num : res) {
    cout << num;
  }
  return 0;
}
