#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  int minOperations(vector<string> &logs) {
    int ans = 0;
    for (auto log : logs) {
      if (log == "../") {
        if (ans != 0) {
          --ans;
        }
      } else if (log == "./") {
        continue;
      } else {
        ++ans;
      }
    }
    return ans;
  }
};

int main(int argc, char const *argv[]) {
  vector<string> logs = {"d1/", "d2/", "../", "d21/", "./"};
  cout << Solution().minOperations(logs);
  return 0;
}
