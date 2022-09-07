#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
  vector<int> constructArray(int n, int k)
  {
    vector<int> answer;
    for (size_t i = 1; i < n - k; i++) {
      answer.push_back(i);
    }
    for (size_t i = n - k, j = n; i <= j; ++i, --j) {
      answer.push_back(i);
      if (i != j) {
        answer.push_back(j);
      }
    }
    return answer;
  }
};

int
main(int argc, char const* argv[])
{
  auto res = Solution().constructArray(3, 1);
  return 0;
}

// [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
