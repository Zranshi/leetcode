// @Time     : 2023/07/20 13:45
// @Author   : Ranshi
// @File     : main.cpp
// @Doc      : 1768. 交替合并字符串

#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  string mergeAlternately(string word1, string word2) {
    int idx1 = 0, idx2 = 0, merge_idx = 0;
    string merge;
    merge.reserve(word1.size() + word2.size());
    while (idx1 < word1.size() || idx2 < word2.size()) {
      if (idx1 < word1.size()) {
        merge.push_back(word1.at(idx1));
        ++idx1;
      }
      if (idx2 < word2.size()) {
        merge.push_back(word2.at(idx2));
        ++idx2;
      }
    }
    return merge;
  }
};

int main() {
  string word1 = "abc";
  string word2 = "pqrs";
  cout << Solution().mergeAlternately(word1, word2) << endl;
}
