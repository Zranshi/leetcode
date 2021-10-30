// @Time     : 2021/10/28 23:32
// @Author   : Ranshi
// @File     : main.cpp
// @Doc      : 496. 下一个更大元素 I
#include <vector>

class Solution {
 public:
  vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    unordered_map<int, int> hashmap;
    stack<int> st;
    for (int i = nums2.size() - 1; i >= 0; --i) {
      int num = nums2[i];
      while (!st.empty() && num >= st.top()) {
        st.pop();
      }
      hashmap[num] = st.empty() ? -1 : st.top();
      st.push(num);
    }
    vector<int> res(nums1.size());
    for (int i = 0; i < nums1.size(); ++i) {
      res[i] = hashmap[nums1[i]];
    }
    return res;
  }
};
