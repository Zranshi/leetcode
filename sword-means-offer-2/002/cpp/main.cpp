#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
  string addBinary(string a, string b)
  {
    string ans;
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());

    int n = max(a.size(), b.size()), carry = 0;
    for (size_t i = 0; i < n; ++i) {
      carry += i < a.size() ? (a.at(i) == '1') : 0;
      carry += i < b.size() ? (b.at(i) == '1') : 0;
      ans.push_back((carry % 2) ? '1' : '0');
      carry /= 2;
    }

    if (carry) {
      ans.push_back('1');
    }
    reverse(ans.begin(), ans.end());

    return ans;
  }
};

string
stringToString(string input)
{
  assert(input.length() >= 2);
  string result;
  for (int i = 1; i < input.length() - 1; i++) {
    char currentChar = input[i];
    if (input[i] == '\\') {
      char nextChar = input[i + 1];
      switch (nextChar) {
        case '\"':
          result.push_back('\"');
          break;
        case '/':
          result.push_back('/');
          break;
        case '\\':
          result.push_back('\\');
          break;
        case 'b':
          result.push_back('\b');
          break;
        case 'f':
          result.push_back('\f');
          break;
        case 'r':
          result.push_back('\r');
          break;
        case 'n':
          result.push_back('\n');
          break;
        case 't':
          result.push_back('\t');
          break;
        default:
          break;
      }
      i++;
    } else {
      result.push_back(currentChar);
    }
  }
  return result;
}

int
main()
{
  string line;
  while (getline(cin, line)) {
    string a = stringToString(line);
    getline(cin, line);
    string b = stringToString(line);

    string ret = Solution().addBinary(a, b);

    string out = ret;
    cout << out << endl;
  }
  return 0;
}
