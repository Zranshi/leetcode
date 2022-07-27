#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
  string replaceSpace(string s)
  {
    int count = 0, len = s.size();
    // 统计空格数量
    for (char c : s) {
      if (c == ' ')
        count++;
    }
    // 修改 s 长度
    s.resize(len + 2 * count);
    // 倒序遍历修改
    for (int i = len - 1, j = s.size() - 1; i < j; i--, j--) {
      if (s[i] != ' ')
        s[j] = s[i];
      else {
        s[j - 2] = '%';
        s[j - 1] = '2';
        s[j] = '0';
        j -= 2;
      }
    }
    return s;
  }
};

int
main(int argc, char const* argv[])
{
  Solution s = Solution();
  string str = "We are happy.";
  cout << s.replaceSpace(str) << endl;
  return 0;
}
