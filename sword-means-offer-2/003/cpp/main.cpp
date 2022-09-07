#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
  int countOnes(int x)
  {
    int ones = 0;
    while (x > 0) {
      x &= (x - 1);
      ones++;
    }
    return ones;
  }
  vector<int> countBits(int n)
  {
    vector<int> bits(n + 1);
    for (size_t i = 0; i <= n; i++) {
      bits[i] = countOnes(i);
    }
    return bits;
  }
};

int
main(int argc, char const* argv[])
{
  auto v = Solution().countBits(2);
  for (size_t i = 0; i < v.size(); i++) {
    cout << v.at(i);
  }

  return 0;
}
