# 算法

## 前置

切题

- Clarification 明确题目要求
- Possible solutions 所有可能解法
  - compare (time/space)
  - optimal 最优
- Coding
- Test cases

五遍刷题

- 第一遍
  - 5-10 分钟：读题 + 思考
  - 有思路：开始做和写代码 或 直接看解法：多解法，比较解法优劣
  - 默写背诵
- 第二遍
  - 马上自己写 → LeetCode 提交
  - 多种解法比较、体会 → 优化
- 第三遍
  - 24 小时后，再重复做题
  - 不同解法的熟练程度 → 专项练习
- 第四遍
  - 一周后：反复回来练习相同的题目
- 第五遍
  - 面试前一周恢复性训练

时间复杂度：

- 树的遍历：前、中、后 O(n)
- 图的遍历：O(n)
- 搜索算法：DFS、BFS O(n)
- 二分查找：O(logn)

跳表：

- 升维思想
- 空间换时间
- 多级索引 增加 log2n 个级索引
- 时间复杂度 logn
- 维护成本较高

### 数组、链表、跳表

- 1. [两数之和](https://leetcode-cn.com/problems/two-sum/)
- 11 [盛水最多的容器](https://leetcode-cn.com/problems/container-with-most-water/) ※
- 15 [三数和](https://leetcode-cn.com/problems/3sum/)
- 21 [合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/)
- 26 [删除有序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)
- 66 [加一](https://leetcode-cn.com/problems/plus-one/)
- 70 [爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)
- 88 [合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array/)
- 141 [环形链表](https://leetcode-cn.com/problems/linked-list-cycle/)
- 189 [旋转数组](https://leetcode-cn.com/problems/rotate-array/)
- 283 [移动零](https://leetcode-cn.com/problems/move-zeroes/)

### 栈、队列、优先队列、双端队列

- 20 [有效的括号](https://leetcode-cn.com/problems/valid-parentheses/)
- 42 [接雨水](https://leetcode-cn.com/problems/trapping-rain-water/) ※
- 84 [柱状图中最大的矩形](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/) ※
- 155 [最小栈](https://leetcode-cn.com/problems/min-stack/)
- 239 [滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/)
- 84 [柱状图中最大的矩形](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/)
- 42 [接雨水](https://leetcode-cn.com/problems/trapping-rain-water/) ※
- 739 每日温度
- 496 下一个更大元素
- 316 去除重复字母
- 901 股票价格跨度
- 402 移掉 K 位数字
- 481 最短无序连续子数组
<!-- 单调队列[<i>To Be Done</i>] -->

### 哈希表、映射、集合

- 49 [异位词](https://leetcode.cn/problems/group-anagrams/)
- 242 有效的字母异位词
- 641 实现双端队列

### 树、二叉树、二叉搜索树

- 94 二叉树中序遍历
- 144 二叉树前序遍历
- 429 N 叉树的层序遍历
- 589 N 叉树的前序遍历
- 590 N 叉树的后序遍历

### 泛型递归、树的递归

- 70 爬楼梯
- 22 括号生成 ※
- 226. 翻转二叉树
- 98. 验证二叉搜索树
- 104. 二叉树的最大深度
- 111. 二叉树的最小深度 ※
- 297. 二叉树的序列化与反序列化 ※

### 分治、回溯

- 50. Pow(x, n)
- 78. 子集
- 169. 多数元素
- 17. 电话号码的字母组合 ※
- 51. N 皇后 ※

### 深度优先搜索和广度优先搜索

- 102 [二叉树的层序遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal/)
- 433. 最小基因变化 ※
- 22. 括号生成
- 515. 在每个树行中找最大值
- 127. 单词接龙 ※
- 126. 单词接龙 II ※
- 200 [岛屿数量](https://leetcode.cn/problems/number-of-islands/)
- 529. 扫雷游戏 ※

### 岛屿系列问题

- 200 [岛屿数量](https://leetcode.cn/problems/number-of-islands/)
- 463. 岛屿的周长
- 695. 岛屿的最大面积
- 827. 最大人工岛

### 贪心算法 部分题目增加了测试用例，不能使用贪心

- 322. 零钱兑换 ※
- 860. 柠檬水找零
- 122. 买卖股票的最佳时机 II
- 455. 分发饼干
- 874. 模拟行走机器人 ※※
- 55. 跳跃游戏
- 45. 跳跃游戏 II ※

### 二分查找

单调性 上下界 索引访问

- 69. x 的平方根
- 367. 有效的完全平方数
- 33. 搜索旋转排序数组 ※
- 74. 搜索二维矩阵
- 153. 寻找旋转排序数组中的最小值 ※

### 动态规划 ※※※※※※

- 32. 最长有效括号 ※
- 45. 跳跃游戏 II ※ 边界问题
- 53. 最大子序和
- 55. 跳跃游戏
- 62. 不同路径 √ dp 初始化方式
- 63. 不同路径 II ※※ 需要重点讨论障碍物的情况
- 64. 最小路径和 ※ 初始状态 dp[0][i] dp[i][0]
- 72. 编辑距离
- 70. 爬楼梯
- 76. 最小覆盖子串 ※ 滑动窗口
- 85. 最大矩形 ※ 转换为 84 题
- 91. 解码方法 ※ s[i] s[i-1] 是否为'0' dp[i] dp[i-1] dp[i-2]
- 115. 不同的子序列 ※※
- 152. 乘积最大子数组 ※
- 198. 打家劫舍 ※ dp[0] dp[1],滚动数组空间优化
- 120. 三角形最小路径和 ※ bottom to up 解法很精妙
- 121. 买卖股票的最佳时机 ※
- 122. 买卖股票的最佳时机 II ※
- 123. 买卖股票的最佳时机 III ※
- 188. 买卖股票的最佳时机 IV ※※
- 279. 完全平方数 ※※ 背包/零钱问题的转化
- 213. 打家劫舍 II ※ robRange
- 221. 最大正方形 ※ 递推关系的证明?
- 300. 最长递增子序列 ※ dp + 二分
- 309. 最佳买卖股票时机含冷冻期 ※※※
- 312. 戳气球 ※※
       <https://leetcode-cn.com/circle/article/qiAgHn/>
- 322. 零钱兑换 ※※※ 细节
- 354. 俄罗斯套娃信封问题
- 363. 矩形区域不超过 K 的最大数值和 ???
- 403. 青蛙过河 ???
- 410. 分割数组的最大值 ??? dp 按照长度、前缀，枚举最后一个划分 二分枚举可能的最大值
- 516. 最长回文子序列 ※
- 518. 零钱兑换 II ※ 题解中 排列和组合的对比
- 552. 学生出勤记录 II ※※
- 621. 任务调度器 ※※
- 647. 回文子串 ※※ 中心点的枚举数量， left，right 计算方式
- 714. 买卖股票的最佳时机含手续费 ※
- 746. 使用最小花费爬楼梯
- 818. 赛车 ？？？
- 980. 不同路径 III ※※※
- 1143. 最长公共子序列 ※ 考虑为什么取值范围是 m+1,n+1

### 字典树和并查集

- 208. 实现 Trie ※ (前缀树)
- 212 [单词搜索](https://leetcode.cn/problems/word-search-ii/submissions/) trie + 回溯
- 200 [岛屿数量](https://leetcode.cn/problems/number-of-islands/)
- 130. 被围绕的区域 以边界上的 O 为起点遍历
- 547. 省份数量 ※

### 高级搜索 剪枝 双向 BFS 启发式搜索(Heuristic Search )

- 22. 括号生成
- 36. 有效的数独 ※
- 37. 解数独 ※
- 51. N 皇后
- 70. 爬楼梯
- 127. 单词接龙
- 433. 最小基因变化
- 773. 滑动谜题
- 1091. 二进制矩阵中的最短路径

### 红黑树和 AVL 树

- 概念理解

### 位运算

<https://leetcode-cn.com/problems/power-of-two/solution/2de-mi-by-leetcode-solution-rny3/>

- 51. N 皇后
- 52. N 皇后 II
- 190. 颠倒二进制位 ※
- 191. 位 1 的个数
- 231. 2 的幂 ※
- 338. 比特位计数

### 布隆过滤器和 LRU 缓存 LFU

- 了解对应的实现
- 146 [LRU 缓存机制](https://leetcode-cn.com/problems/lru-cache/)

### 排序算法

- 选择排序、插入排序、冒泡排序
- 快排、归并
- 堆排序
- 计数排序、桶排序、基数排序
- 56 [合并区间](https://leetcode.cn/problems/merge-intervals/)
- 242 有效的字母异位词
- 493. 翻转对 逆序对 归并排序 ※
- 1122. 数组的相对排序 ※※ python sort(cmp=None, key=None, reverse=False) 参数学习
- 1244 ?

### 字符串算法

#### 字符串基础

- 8. 字符串转换整数 (atoi)
- 43. 字符串相乘
- 58. 最后一个单词的长度 倒序查找
- 387. 字符串中的第一个唯一字符
- 709. 转换成小写字母 ※ chr ord 32 65 90
- 771. 宝石与石头

#### 字符串操作

- 14 [最长公共前缀](https://leetcode.cn/problems/longest-common-prefix/)
- 151. 翻转字符串里的单词
- 344. 反转字符串
- 541. 反转字符串 II
- 557. 反转字符串中的单词 III
- 917. 仅仅反转字母 ※

#### 异位词问题

- 49 [字母异位词分组](https://leetcode.cn/problems/group-anagrams/)
- 242. 有效的字母异位词
- 438. 找到字符串中所有字母异位词 ※

#### 回文串问题

- 5. 最长回文子串
- 125. 验证回文串 ※ isalnum 判断是否字符或数字
- 680. 验证回文字符串 Ⅱ ※

#### 最长子串、子序列问题

- 5. 最长回文子串
- 72. 编辑距离
- 1143. 最长公共子序列

#### 字符串 +DP 问题

- 10. 正则表达式匹配 ※※※
- 44. 通配符匹配 ※
- 115. 不同的子序列 ※

- 32. 最长有效括号 ※
- 205. 同构字符串 ※

---

### 确定有限状态机

- 65. 有效数字 ？？？
- 393. UTF-8 编码验证 ※

### 前缀和相关题目

- 303. 区域和检索 - 数组不可变
- 304. 二维区域和检索 - 矩阵不可变 ※
- 363. 矩形区域不超过 K 的最大数值和 ※※ ???

### 二分

- 875. 爱吃香蕉的珂珂
- 1482. 制作 m 束花所需的最少天数 ※
- 1011. 在 D 天内送达包裹的能力 ※
- 1552. 两球之间的磁力 ※※

### 滑动窗口

- 3. 无重复字符的最长子串
- 76. 最小覆盖子串
- 438. 找到字符串中所有字母异位词
- 567. 字符串的排列

背包问题 416. 分割和子集 474. 一和零 494. 目标和 879. 盈利计划 1049. 最后一块石头的重量 ii

- 1449. 数位成本和为目标值的最大数字
- 1450. 零钱兑换
- 1451. 零钱兑换 ii
- 1452. 完全平方数

## labuladong 的算法小抄

### 动态规划

- 509. 斐波那契数
- 300.  最长递增子序列
- 354. 俄罗斯套娃信封问题
- 53. 最大子序和
- 1143. 最长公共子序列
- 72. 编辑距离
- 5. 最长回文子串
- 516. 最长回文子序列 ※
- 1312. 让字符串成为回文串的最少插入次数
- 10. 正则表达式匹配 ※※※
- 651. 四键键盘 vip ※
- 887. 鸡蛋掉落 ※
- 312. 戳气球 ※※
- 416. 分割等和子集
- 518. 零钱兑换 II ※
- 198. 打家劫舍
- 213. 打家劫舍 II ※ robRange
- 337. 打家劫舍 III
- 494. 目标和

### 数据结构

- 146 [LRU 缓存机制](https://leetcode-cn.com/problems/lru-cache/)
- 460. LFU 缓存 ※
- 98. 验证二叉搜索树
- 99. 恢复二叉搜索树 ※※
- 100. 相同的树
- 450. 删除二叉搜索树中的节点 ※
- 700. 二叉搜索树中的搜索
- 701. 二叉搜索树中的插入操作 ※
- 105 [从前序与中序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
- 124 [二叉树中的最大路径和](https://leetcode.cn/problems/binary-tree-maximum-path-sum/)
- 222. 完全二叉树的节点个数
- 297. 二叉树的序列化与反序列化
- 236. 二叉树的最近公共祖先 ※
- 496. 下一个更大元素 I
- 503. 下一个更大元素 II ※
- 239. 滑动窗口最大值
- 234. 回文链表
- 206 [反转链表](https://leetcode-cn.com/problems/reverse-linked-list/)
- 92. 反转链表 II ※
- 25. K 个一组翻转链表

### 算法思维

- 78. 子集 ※
- 77. 组合
- 46 [全排列](https://leetcode.cn/problems/permutations/)
- 37. 解数独 ※
- 22 括号生成 ※
- 773. 滑动谜题 ※
- 1118. 一月有多少天
- 1. 两数之和
- 170. 两数之和 III 数据结构设计
- 167. 两数之和 II - 输入有序数组
- 15 [三数和](https://leetcode-cn.com/problems/3sum/)
- 18. 四数之和
- 224. 基本计算器
- 227. 基本计算器 II
- 772. 基本计算器 iii
- 969. 煎饼排序
- 560. 和为 K 的子数组
- 341. 扁平化嵌套列表迭代器

### 高频面试

- 204. 计数质数 ※
- 372. 超级次方 ※
- 704. 二分查找
- 34. 在排序数组中查找元素的第一个和最后一个位置
- 875. 爱吃香蕉的珂珂
- 42 接雨水 ※
- 83. 删除排序链表中的重复元素
- 516. 最长回文子序列 ※
- 55. 跳跃游戏
- 45. 跳跃游戏 II ※
- 56 [合并区间](https://leetcode.cn/problems/merge-intervals/)
- 435. 无重叠区间
- 452. 用最少数量的箭引爆气球
- 20 有效的括号
- 855. 考场就座 ※
- 990. 等式方程的可满足性
- 292. Nim 游戏
- 877. 石子游戏
- 319. 灯泡开关
- 752. 打开转盘锁

---

## 剑指 Offer

- 剑指 Offer 03. 数组中重复的数字
- 剑指 Offer 04. 二维数组中的查找
- 剑指 Offer 05. 替换空格
- 剑指 Offer 06. 从尾到头打印链表
- 剑指 Offer 07. 重建二叉树 ※※
- 剑指 Offer 09. 用两个栈实现队列
- 剑指 Offer 10- I. 斐波那契数列 ※
- 剑指 Offer 10- II. 青蛙跳台阶问题 ※
- 剑指 Offer 11. 旋转数组的最小数字 ※※※
- 剑指 Offer 12. 矩阵中的路径 ※※※※※
- 剑指 Offer 13. 机器人的运动范围 ※※
- 剑指 Offer 14- I. 剪绳子 ???
- 剑指 Offer 14- II. 剪绳子 II ???
- 剑指 Offer 15. 二进制中 1 的个数 ※
- 剑指 Offer 16. 数值的整数次方 ※※
- 剑指 Offer 17. 打印从 1 到最大的 n 位数 ※※※
- 剑指 Offer 18. 删除链表的节点 ※※
- 剑指 Offer 19. 正则表达式匹配 ※※※※※※
- 剑指 Offer 20. 表示数值的字符串 ???放弃了
- 剑指 Offer 21. 调整数组顺序使奇数位于偶数前面
- 剑指 Offer 22. 链表中倒数第 k 个节点
- 剑指 Offer 25. 合并两个排序的链表
- 剑指 Offer 26. 树的子结构 ※
- 剑指 Offer 27. 二叉树的镜像 ※※※
- 剑指 Offer 28. 对称的二叉树 ※
- 剑指 Offer 29. 顺时针打印矩阵 ※
- 剑指 Offer 30. 包含 min 函数的栈 ※※※
- 剑指 Offer 31. 栈的压入、弹出序列 ※
- 剑指 Offer 32 - I. 从上到下打印二叉树
- 剑指 Offer 32 - II. 从上到下打印二叉树 II ※
- 剑指 Offer 32 - III. 从上到下打印二叉树 III ※※※
- 剑指 Offer 33. 二叉搜索树的后序遍历序列 ※※※※
- 剑指 Offer 34. 二叉树中和为某一值的路径 ※※※※
- 剑指 Offer 35. 复杂链表的复制 ※
- 剑指 Offer 36. 二叉搜索树与双向链表 ※※※※
- 剑指 Offer 37. 序列化二叉树
- 剑指 Offer 38. 字符串的排列 ※※
- 剑指 Offer 39. 数组中出现次数超过一半的数字
- 剑指 Offer 40. 最小的 k 个数 ※※※※
- 剑指 Offer 41. 数据流中的中位数 ※※※※
- 剑指 Offer 42. 连续子数组的最大和
- 剑指 Offer 43. 1 ～ n 整数中 1 出现的次数 ???
- 剑指 Offer 44. 数字序列中某一位的数字 ???
- 剑指 Offer 45. 把数组排成最小的数 ※※※※
- 剑指 Offer 46. 把数字翻译成字符串
- 剑指 Offer 47. 礼物的最大价值
- 剑指 Offer 48. 最长不含重复字符的子字符串 ※※
- 剑指 Offer 49. 丑数 ※※※
- 剑指 Offer 50. 第一个只出现一次的字符
- 剑指 Offer 51. 数组中的逆序对 ※※※※
- 剑指 Offer 52. 两个链表的第一个公共节点 ※※
- 剑指 Offer 53 - I. 在排序数组中查找数字 I
- 剑指 Offer 53 - II. 0 ～ n-1 中缺失的数字 ※※
- 剑指 Offer 54. 二叉搜索树的第 k 大节点 ※※
- 剑指 Offer 55 - I. 二叉树的深度
- 剑指 Offer 55 - II. 平衡二叉树 ※※
- 剑指 Offer 56 - I. 数组中数字出现的次数 ※※※※
- 剑指 Offer 56 - II. 数组中数字出现的次数 II ※※※※
- 剑指 Offer 57. 和为 s 的两个数字 ※※※※
- 剑指 Offer 57 - II. 和为 s 的连续正数序列 ※※※※
- 剑指 Offer 58 - I. 翻转单词顺序 ※※
- 剑指 Offer 58 - II. 左旋转字符串
- 剑指 Offer 59 - I. 滑动窗口的最大值 ※※
- 剑指 Offer 59 - II. 队列的最大值 ※※
- 剑指 Offer 60. n 个骰子的点数 ???
- 剑指 Offer 61. 扑克牌中的顺子 ※※※※
- 剑指 Offer 62. 圆圈中最后剩下的数字 ???
- 剑指 Offer 63. 股票的最大利润 ※
- 剑指 Offer 64. 求 1+2+…+n ※※※※
- 剑指 Offer 65. 不用加减乘除做加法 ???
- 剑指 Offer 66. 构建乘积数组 ※※※※
- 剑指 Offer 67. 把字符串转换成整数 ???
- 剑指 Offer 68 - I. 二叉搜索树的最近公共祖先 ※※※※
- 剑指 Offer 68 - II. 二叉树的最近公共祖先 ※※※※

## 剑指 Offer 专项训练

### 正数

- 剑指 Offer II 001. 整数除法
- 剑指 Offer II 002. 二进制加法
- 剑指 Offer II 003. 前 n 个数字二进制中 1 的个数
- 剑指 Offer II 004. 只出现一次的数字 ?
- 剑指 Offer II 005. 单词长度的最大乘积

### 数组

- 剑指 Offer II 006. 排序数组中两个数字之和
- 剑指 Offer II 007. 数组中和为 0 的三个数 ※
- 剑指 Offer II 008. 和大于等于 target 的最短子数组
- 剑指 Offer II 009. 乘积小于 K 的子数组 ※
- 剑指 Offer II 010. 和为 k 的子数组
- 剑指 Offer II 011. 0 和 1 个数相同的子数组 ※
- 剑指 Offer II 012. 左右两边子数组的和相等
- 剑指 Offer II 013. 二维子矩阵的和 ※

### 字符串

- 剑指 Offer II 014. 字符串中的变位词 ※
- 剑指 Offer II 015. 字符串中的所有变位词
- 剑指 Offer II 016. 不含重复字符的最长子字符串
- 剑指 Offer II 017. 含有所有字符的最短字符串
- 剑指 Offer II 018. 有效的回文
- 剑指 Offer II 019. 最多删除一个字符得到回文
- 剑指 Offer II 020. 回文子字符串的个数

### 链表

- 剑指 Offer II 021. 删除链表的倒数第 n 个结点 ※※
- 剑指 Offer II 022. 链表中环的入口节点 ※※※
- 剑指 Offer II 023. 两个链表的第一个重合节点
- 剑指 Offer II 024. 反转链表
- 剑指 Offer II 025. 链表中的两数相加
- 剑指 Offer II 026. 重排链表 ※※
- 剑指 Offer II 027. 回文链表 ※
- 剑指 Offer II 028. 展平多级双向链表 ※※※
- 剑指 Offer II 029. 排序的循环链表 ※

### 哈希表

- 剑指 Offer II 030. 插入、删除和随机访问都是 O(1) 的容器 ※
- 剑指 Offer II 031. 最近最少使用缓存
- 剑指 Offer II 032. 有效的变位词
- 剑指 Offer II 033. 变位词组
- 剑指 Offer II 034. 外星语言是否排序 ※
- 剑指 Offer II 035. 最小时间差 v

### 栈

- 剑指 Offer II 036. 后缀表达式
- 剑指 Offer II 037. 小行星碰撞 ?
- 剑指 Offer II 038. 每日温度
- 剑指 Offer II 039. 直方图最大矩形面积
- 剑指 Offer II 040. 矩阵中最大的矩形

### 队列

- 剑指 Offer II 041. 滑动窗口的平均值
- 剑指 Offer II 042. 最近请求次数
- 剑指 Offer II 043. 往完全二叉树添加节点 ※
- 剑指 Offer II 044. 二叉树每层的最大值
- 剑指 Offer II 045. 二叉树最底层最左边的值
- 剑指 Offer II 046. 二叉树的右侧视图

### 树

- 剑指 Offer II 047. 二叉树剪枝 ※
- 剑指 Offer II 048. 序列化与反序列化二叉树 ※
- 剑指 Offer II 049. 从根节点到叶节点的路径数字之和 ※※※
- 剑指 Offer II 050. 向下的路径节点之和 ※※※
- 剑指 Offer II 051. 节点之和最大的路径
- 剑指 Offer II 052. 展平二叉搜索树 ※
- 剑指 Offer II 053. 二叉搜索树中的中序后继 ※※
- 剑指 Offer II 054. 所有大于等于节点的值之和
- 剑指 Offer II 055. 二叉搜索树迭代器 ※※
- 剑指 Offer II 056. 二叉搜索树中两个节点之和
- 剑指 Offer II 057. 值和下标之差都在给定的范围内 ?
- 剑指 Offer II 058. 日程表 ?

### 堆

- 剑指 Offer II 059. 数据流的第 K 大数值 ?
- 剑指 Offer II 060. 出现频率最高的 k 个数字 ?
- 剑指 Offer II 061. 和最小的 k 个数对 ??

### 前缀树

- 剑指 Offer II 062. 实现前缀树
- 剑指 Offer II 063. 替换单词 ?
- 剑指 Offer II 064. 神奇的字典 ??
- 剑指 Offer II 065. 最短的单词编码
- 剑指 Offer II 066. 单词之和
- 剑指 Offer II 067. 最大的异或 ?

### 二分 offer

- 剑指 Offer II 068. 查找插入位置 ※
- 剑指 Offer II 069. 山峰数组的顶部
- 剑指 Offer II 070. 排序数组中只出现一次的数字 ※
- 剑指 Offer II 071. 按权重生成随机数 ※※※
- 剑指 Offer II 072. 求平方根
- 剑指 Offer II 073. 狒狒吃香蕉

### 排序

- 剑指 Offer II 074. 合并区间
- 剑指 Offer II 075. 数组相对排序 ※
- 剑指 Offer II 076. 数组中的第 k 大的数字 ※
- 剑指 Offer II 077. 链表排序 ※※
- 剑指 Offer II 078. 合并排序链表 ※

### 回溯法

- 剑指 Offer II 079. 所有子集
- 剑指 Offer II 080. 含有 k 个元素的组合
- 剑指 Offer II 081. 允许重复选择元素的组合 ※※※
- 剑指 Offer II 082. 含有重复元素集合的组合 ※
- 剑指 Offer II 083. 没有重复元素集合的全排列 ※
- 剑指 Offer II 084. 含有重复元素集合的全排列
- 剑指 Offer II 085. 生成匹配的括号
- 剑指 Offer II 086. 分割回文子字符串 ※※※
- 剑指 Offer II 087. 复原 IP ※※※

### 动态规划 offer

- 剑指 Offer II 088. 爬楼梯的最少成本 ※
- 剑指 Offer II 089. 房屋偷盗
- 剑指 Offer II 090. 环形房屋偷盗
- 剑指 Offer II 091. 粉刷房子
- 剑指 Offer II 092. 翻转字符 ※※※※
- 剑指 Offer II 093. 最长斐波那契数列 ※※※※
- 剑指 Offer II 094. 最少回文分割 ※※※※
- 剑指 Offer II 095. 最长公共子序列
- 剑指 Offer II 096. 字符串交织 ※※※※
- 剑指 Offer II 097. 子序列的数目 ※※
- 剑指 Offer II 098. 路径的数目
- 剑指 Offer II 099. 最小路径之和
- 剑指 Offer II 100. 三角形中最小路径之和
  <https://leetcode-cn.com/problems/combination-sum-iv/solution/xi-wang-yong-yi-chong-gui-lu-gao-ding-bei-bao-wen-/>
- 剑指 Offer II 101. 分割等和子集 ※※※
- 剑指 Offer II 102. 加减的目标值 ※※※
- 剑指 Offer II 103. 最少的硬币数目 ※※※
- 剑指 Offer II 104. 排列的数目 ※※※

### 图

- 剑指 Offer II 105. 岛屿的最大面积
- 剑指 Offer II 106. 二分图 ※※※
- 剑指 Offer II 107. 矩阵中的距离 ※※※
- 剑指 Offer II 108. 单词演变
- 剑指 Offer II 109. 开密码锁
- 剑指 Offer II 110. 所有路径 ※
- 剑指 Offer II 111. 计算除法 ※※※
- 剑指 Offer II 112. 最长递增路径 ※※
- 剑指 Offer II 113. 课程顺序 ※
- 剑指 Offer II 114. 外星文字典
- 剑指 Offer II 115. 重建序列
- 剑指 Offer II 116. 省份数量
- 剑指 Offer II 117. 相似的字符串
- 剑指 Offer II 118. 多余的边
- 剑指 Offer II 119. 最长连续序列

---

## 每日一题

- 1877. 数组中最大数对和的最小值
- 138. 复制带随机指针的链表
- 1893. 检查是否区域内所有整数都被覆盖 ※※ 差分数组 前缀和
- 1713. 得到子序列的最少操作次数 ？？？
- 671. 二叉树中第二小的节点
- 863. 二叉树中所有距离为 K 的结点 ※ 构建父节点关系 图
- 1104. 二叉树寻路 ???
- 611. 有效三角形的个数 ※
- 43. 字符串相乘

---

## Microsoft-Hiring

### todo

Microsoft-Hiring：一个微软HR做的网站，一些微软介绍以及题目
[题目列表](https://github.com/Microsoft-Hiring/microsoft-hiring.github.io/blob/master/pages/problems/leetcode.md)

共241道题 日均2~3道题 4个月内完成？

### need vip

- 277 [Find the Celebrity](https://leetcode-cn.com/problems/find-the-celebrity/)
- 346 [Moving Average from Data Stream](https://leetcode-cn.com/problems/moving-average-from-data-stream/)
- 253 [Meeting Rooms II](https://leetcode-cn.com/problems/meeting-rooms-ii/)
- 252 [Meeting Rooms](https://leetcode.cn/problems/meeting-rooms/)
- 772 [basic calculator iii](https://leetcode.cn/problems/basic-calculator-iii/)

### LeetCode

- 146 [LRU 缓存机制](https://leetcode-cn.com/problems/lru-cache/)
- 692 [Top K Frequent Words](https://leetcode-cn.com/problems/top-k-frequent-words/) 如何实现最大堆
- 206 [Reverse Linked List](https://leetcode-cn.com/problems/reverse-linked-list/) 解法: [递归](https://leetcode-cn.com/problems/reverse-linked-list/solution/dong-hua-yan-shi-206-fan-zhuan-lian-biao-by-user74/)
- 24 [Swap Nodes in Pairs](https://leetcode.cn/problems/swap-nodes-in-pairs/)
- 21 [Merge Two Sorted Lists](https://leetcode.cn/problems/merge-two-sorted-lists/)
- 56 [Merge Intervals](https://leetcode.cn/problems/merge-intervals/)
- 268 [Missing Number](https://leetcode.cn/problems/missing-number/)
- 212 [Word Search II](https://leetcode.cn/problems/word-search-ii/submissions/)
- 88 [Merge Sorted Array](https://leetcode.cn/problems/merge-sorted-array/)
- 14 [Longest Common Prefix](https://leetcode.cn/problems/longest-common-prefix/)
- 328 [Odd Even Linked List](https://leetcode.cn/problems/odd-even-linked-list/)
- 68 [Text Justification](https://leetcode.cn/problems/text-justification/) **
- 171 [Excel Sheet Column Number](https://leetcode.cn/problems/excel-sheet-column-number/)
- 11 [Container With Most Water](https://leetcode.cn/problems/container-with-most-water/)
- 124 [Binary Tree Maximum Path Sum](https://leetcode.cn/problems/binary-tree-maximum-path-sum/)
- 46 [Permutations](https://leetcode.cn/problems/permutations/)
- 200 [Number of Islands](https://leetcode.cn/problems/number-of-islands/)
- 102 [Binary Tree Level Order Traversal](https://leetcode.cn/problems/binary-tree-level-order-traversal/)
- 15 [3Sum](https://leetcode.cn/problems/3sum/)
- 79 [Word Search](https://leetcode.cn/problems/word-search/)
- 105 [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
- 49 [Group Anagrams](https://leetcode.cn/problems/group-anagrams/)
- 210 [Course Schedule II](https://leetcode.cn/problems/course-schedule-ii/)
- 4 [Median of Two Sorted Arrays](https://leetcode.cn/problems/median-of-two-sorted-arrays/) 还得再看看
- 3 [Longest Substring Without Repeating Characters](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)
- 78 [subsets](https://leetcode.cn/problems/subsets/)
- 468 [Validate IP Address](https://leetcode.cn/problems/validate-ip-address/) TODO
- 151 [Reverse Words in a String](https://leetcode.cn/problems/reverse-words-in-a-string/)
- 235 [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/) 简单题都不会了
- 236 [Lowest Common Ancestor of a Binary Tree](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/) 需要回顾
- 165 [Compare Version Numbers](https://leetcode.cn/problems/compare-version-numbers/)
- 117 [Populating Next Right Pointers in Each Node II](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/)
- 20 [Valid Parentheses](https://leetcode.cn/problems/valid-parentheses/)
- 722 [Remove Comments](https://leetcode.cn/problems/remove-comments/) TODO
- 215 [Kth Largest Element in an Array](https://leetcode.cn/problems/kth-largest-element-in-an-array/submissions/)
