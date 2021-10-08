""" 
https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/
剑指 Offer 62. 圆圈中最后剩下的数字

(idx + m -1) mod n 
"""


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        x = 0
        for i in range(2, n+1):
            x = (x+m) % i
        return x
    
    def lastRemaining(self, n: int, m: int) -> int:
        arr = list(range(n))
        idx = 0
        while n > 1:
            idx = (idx + m -1) % n
            arr.remove(arr[idx])
            n-=1
        return arr[0]
    # public int lastRemaining(int n, int m) {
    #     ArrayList<Integer> list = new ArrayList<>(n);
    #     for (int i = 0; i < n; i++) {
    #         list.add(i);
    #     }
    #     int idx = 0;
    #     while (n > 1) {
    #         idx = (idx + m - 1) % n;
    #         list.remove(idx);
    #         n--;
    #     }
    #     return list.get(0);
    # }


