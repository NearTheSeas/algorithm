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

数组、链表、跳表

- 1 两数和
- 11 盛水最多的容器 ※
- 15 三数和
- 21 合并两个有序链表
- 26 删除有序数组中的重复项
- 66 加一
- 70 爬楼梯
- 88 合并两个有序数组
- 141 环形链表
- 189 旋转数组
- 283 移动零

栈、队列、优先队列、双端队列

- 20 有效的括号
- 42 接雨水 ※
- 84 柱状图中最大的矩形 ※
- 155 最小栈
- 239 滑动窗口最大值

单调队列[<i>To Be Done</i>]

- 84 柱状图中最大的矩形
- 42 接雨水
- 739 每日温度
- 496 下一个更大元素
- 316 去除重复字母
- 901 股票价格跨度
- 402 移掉 K 位数字
- 481 最短无序连续子数组

哈希表、映射、集合

- 49 异位词
- 242 有效的字母异位词
- 641 实现双端队列

树、二叉树、二叉搜索树

- 94 二叉树中序遍历
- 144 二叉树前序遍历
- 429 N 叉树的层序遍历
- 589 N 叉树的前序遍历
- 590 N 叉树的后序遍历

泛型递归、树的递归

- 70 爬楼梯
- 22 括号生成 ※
- 226. 翻转二叉树
- 98. 验证二叉搜索树
- 104. 二叉树的最大深度
- 111. 二叉树的最小深度 ※
- 297. 二叉树的序列化与反序列化 ※

第 08 课丨分治、回溯

- 50. Pow(x, n)
- 78. 子集
- 169. 多数元素
- 17. 电话号码的字母组合 ※
- 51. N 皇后 ※

第 09 课丨深度优先搜索和广度优先搜索

- 102. 二叉树的层序遍历
- 433. 最小基因变化 ※
- 22. 括号生成
- 515. 在每个树行中找最大值
- 127. 单词接龙 ※
- 126. 单词接龙 II ※
- 200. 岛屿数量 ※
- 529. 扫雷游戏 ※

岛屿系列问题

- L200. 岛屿数量
- 463. 岛屿的周长
- 695. 岛屿的最大面积
- 827. 最大人工岛

第 10 课丨贪心算法 部分题目增加了测试用例，不能使用贪心

- 322. 零钱兑换 ※
- 860. 柠檬水找零
- 122. 买卖股票的最佳时机 II
- 455. 分发饼干
- 874. 模拟行走机器人 ※※
- 55. 跳跃游戏
- 45. 跳跃游戏 II ※

第 11 课丨二分查找
单调性 上下界 索引访问

- 69. x 的平方根
- 367. 有效的完全平方数
- 33. 搜索旋转排序数组 ※
- 74. 搜索二维矩阵
- 153. 寻找旋转排序数组中的最小值 ※

第 12 课丨动态规划 ※※※※※※

- 62. 不同路径 ※ dp 初始化方式
- 1143. 最长公共子序列
- 70. 爬楼梯
- 120. 三角形最小路径和 ※ bottom to up 解法很精妙
- 53. 最大子序和
- 152. 乘积最大子数组 ※
- 322. 零钱兑换 ※
- 198. 打家劫舍 ※ python 解法 滚动数组
- 213. 打家劫舍 II
- 121. 买卖股票的最佳时机 ※
- 122. 买卖股票的最佳时机 II
- 123. 买卖股票的最佳时机 III ※
- 188. 买卖股票的最佳时机 IV ???
- 714. 买卖股票的最佳时机含手续费 ※
- 309. 最佳买卖股票时机含冷冻期 ???
       https://leetcode-cn.com/circle/article/qiAgHn/
- 279. 完全平方数 ※※ 背包问题的转化
- 72. 编辑距离
- 55. 跳跃游戏
- 45. 跳跃游戏 II ※
- 63. 不同路径 II ※ 需要重点讨论障碍物的情况
- 980. 不同路径 III ??
- 518. 零钱兑换 II ※ 题解中 排列和组合的对比
- 32. 最长有效括号 ※
- 64. 最小路径和
- 91. 解码方法 ※ s[i] s[i-1] 是否为'0' dp[i] dp[i-1] dp[i-2]
- 221. 最大正方形 ※ 递推关系的证明?
- 363. 矩形区域不超过 K 的最大数值和 ???
- 403. 青蛙过河 ???
- 410. 分割数组的最大值 ??? 二分
- 552. 学生出勤记录 II ???
- 621. 任务调度器 ※※
- 647. 回文子串 ※ 中心点的枚举数量， left，right 计算方式
- 76. 最小覆盖子串 ※ 滑动窗口
- 312. 戳气球 ※

前缀和相关题目

- 363. 矩形区域不超过 K 的最大数值和 ???
- 304. 二维区域和检索 - 矩阵不可变

特殊二分

- 875. 爱吃香蕉的珂珂
- 1482. 制作 m 束花所需的最少天数
- 1011. 在 D 天内送达包裹的能力
- 1552. 两球之间的磁力

第 13 课丨字典树和并查集

- 208. 实现 Trie (前缀树)
- 212. 单词搜索 II
- 200. 岛屿数量
- 130. 被围绕的区域
- 547. 省份数量

第 14 课丨高级搜索 剪枝 双向BFS 启发式搜索(Heuristic Search )

- 70. 爬楼梯
- 22. 括号生成
- 51. N 皇后
- 36. 有效的数独
- 37. 解数独
- 127. 单词接龙
- 433. 最小基因变化
- 1091. 二进制矩阵中的最短路径
- 773. 滑动谜题


第 15 课丨红黑树和 AVL 树

第 16 课丨位运算

第 17 课丨布隆过滤器和 LRU 缓存

第 18 课丨排序算法

第 19 课丨高级动态规划

第 20 课丨字符串算法
