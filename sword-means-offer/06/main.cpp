#include <bits/stdc++.h>

using namespace std;

struct ListNode
{
  int val;
  ListNode* next;
  ListNode(int x)
    : val(x)
    , next(NULL){};
};

class Solution
{
public:
  vector<int> reversePrint(ListNode* head)
  {
    stack<int> stk;
    vector<int> res;
    while (head != nullptr) {
      stk.push(head->val);
      head = head->next;
    }
    while (!stk.empty()) {
      res.push_back(stk.top());
      stk.pop();
    }
    return res;
  }
};

int
main(int argc, char const* argv[])
{
  ListNode pre_head = ListNode(0);
  ListNode* idx = &pre_head;
  vector<int> data = { 1, 3, 2 };
  for (int i = 0; i < data.size(); i++) {
    ListNode ln = ListNode(data[i]);
    idx->next = &ln;
    idx = idx->next;
  }

  auto v = Solution().reversePrint(pre_head.next);

  for (int i = 0; i < v.size(); i++) {
    cout << v[i];
    if (i != v.size()) {
      cout << ", ";
    }
  }

  return 0;
}
