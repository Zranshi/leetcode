#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
  int divide(int a, int b)
  {
    if (a == INT_MIN) {
      if (b == 1) {
        return INT_MIN;
      } else if (b == -1) {
        return INT_MAX;
      }
    } else if (b == INT_MIN) {
      return a == INT_MIN ? 1 : 0;
    } else if (a == 0) {
      return 0;
    }
    bool rev = false;
    if (a > 0) {
      a = -a;
      rev = !rev;
    }
    if (b > 0) {
      b = -b;
      rev = !rev;
    }
    auto quickAdd = [](int y, int z, int x) {
      int result = 0, add = y;
      while (z) {
        if (z & 1) {
          if (result < x - add) {
            return false;
          }
          result += add;
        }
        if (z != 1) {
          if (add < x - add) {
            return false;
          }
          add += add;
        }
        z >>= 1;
      }
      return true;
    };

    int left = 1, right = INT_MAX, ans = 0;
    while (left <= right) {
      int mid = left + ((right - left) >> 1);
      bool check = quickAdd(b, mid, a);
      if (check) {
        ans = mid;
        if (mid == INT_MAX) {
          break;
        }
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
    return rev ? -ans : ans;
  }
};

int
stringToInteger(string input)
{
  return stoi(input);
}

int
main()
{
  string line;
  while (getline(cin, line)) {
    int a = stringToInteger(line);
    getline(cin, line);
    int b = stringToInteger(line);

    int ret = Solution().divide(a, b);

    string out = to_string(ret);
    cout << out << endl;
  }
  return 0;
}
