#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  int maxProduct(vector<string> &words) {
    int length = words.size();
    vector<int> masks(length);
    for (size_t i = 0; i < length; i++) {
      string word = words[i];
      int word_length = word.size();
      for (size_t j = 0; j < word_length; j++) {
        masks[i] |= 1 << (word[j] - 'a');
      }
    }
    int max_prod = 0;
    for (size_t i = 0; i < length; i++) {
      for (int j = i + 1; j < length; j++) {
        if ((masks[i] & masks[j]) == 0) {
          max_prod = max(max_prod, int(words[i].size() * words[j].size()));
        }
      }
    }
    return max_prod;
  }
};

int main(int argc, char const *argv[]) {
  vector<string> words = {"abcw", "baz", "foo", "bar", "fxyz", "abcdef"};
  auto res = Solution().maxProduct(words);
  cout << res;
  return 0;
}
