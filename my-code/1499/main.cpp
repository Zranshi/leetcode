// @Time     : 2023/07/20 21:55
// @Author   : Ranshi
// @File     : main.cpp
// @Doc      : 1499. 满足不等式的最大值

#include <climits>
#include <functional>
#include <iostream>
#include <queue>
#include <utility>

using namespace std;

class Solution {
public:
  using pii = pair<int, int>;
  int findMaxValueOfEquation(vector<vector<int>> &points, int k) {
    int res = INT_MIN;
    priority_queue<pii, vector<pii>, greater<pii>> heap;
    for (auto &point : points) {
      int x = point[0], y = point[1];
      while (!heap.empty() && x - heap.top().second > k) {
        heap.pop();
      }
      if (!heap.empty()) {
        res = max(res, x + y - heap.top().first);
      }
      heap.emplace(x - y, x);
    }
    return res;
  }
};

int main() {
  vector<vector<int>> points = {
      {1, 3},
      {2, 0},
      {5, 10},
      {6, -10},
  };
  cout << Solution().findMaxValueOfEquation(points, 1) << endl;
}
