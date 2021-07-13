""" 
https://leetcode-cn.com/problems/relative-sort-array/
1122. 数组的相对排序

list.sort(cmp=None, key=None, reverse=False)
cmp︰ 指定一個比較函式的話，會使用該比較函式進行排序
key︰ 指定元素的某一列為key鍵值, 也就是按照元素的某一列來進行排序
reverse︰排序規則，reverse=True 降序，reverse=False 升序（預設）。
 """

from typing import List, Tuple


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        def mycmp(x: int) -> Tuple[int, int]:
            return (0, rank[x]) if x in rank else (1, x)
        rank = {x: i for i, x in enumerate(arr2)}
        arr1.sort(key=mycmp)
        return arr1
