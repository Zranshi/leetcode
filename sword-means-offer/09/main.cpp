#include <bits/stdc++.h>

using namespace std;

class CQueue
{
public:
  stack<int> main_stk;
  stack<int> assist_stk;
  CQueue() {}

  void appendTail(int value) { assist_stk.push(value); }

  int deleteHead()
  {
    int res;
    if (main_stk.empty()) {
      if (assist_stk.empty()) {
        return -1;
      }
      while (!assist_stk.empty()) {
        main_stk.push(assist_stk.top());
        assist_stk.pop();
      }
    }
    res = main_stk.top();
    main_stk.pop();
    return res;
  }
};
