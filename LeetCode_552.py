""" 
https://leetcode-cn.com/problems/student-attendance-record-ii/
552. 学生出勤记录 II
https://leetcode-cn.com/problems/student-attendance-record-ii/solution/javadong-tai-gui-hua-ru-he-yi-bu-bu-si-kao-yu-shi-/

dp[1][1][0] = 1; // A，第一层，有A，末尾没有L，1A0L
dp[1][0][1] = 1; // L，第一层，无A，末尾1个L，0A1L
dp[1][0][0] = 1; // P，第一层，无A，末尾没有L，0A0L

当前这末尾+P
无A末尾无L 可来自上一层  无A末尾无L   +     无A末尾1L   +    无A末尾2L
0A0L     =                  0A0L      +       0A1L      +       0A2L
dp[i][0][0] =          (dp[i - 1][0][0]  + dp[i - 1][0][1] + dp[i - 1][0][2]) % _MOD;
同理，接着推
1A0L     =       1A0L       +       1A1L      +       1A2L
dp[i][1][0] = (dp[i - 1][1][0] + dp[i - 1][1][1] + dp[i - 1][1][2]) % _MOD;

+L
0A1L = 0A0L
dp[i][0][1] = dp[i - 1][0][0];
0A2L = 0A1L
dp[i][0][2] = dp[i - 1][0][1];
1A1L = 1A0L
dp[i][1][1] = dp[i - 1][1][0];
1A2L = 1A1L
dp[i][1][2] = dp[i - 1][1][1];

+A
此处的 dp[i][1][0] 在上面 +P 时已经开始出现，故此处应 +=
1A0L = 0A0L + 0A1L + 0A2L
dp[i][1][0] += (dp[i - 1][0][0] + dp[i - 1][0][1] + dp[i - 1][0][2]) % _MOD;


"""


class Solution:
    # 看不懂的神操作
    """ 
    C[0] = no A, ends in no L
    C[1] = no A, ends in 1 L
    C[2] = no A, ends in 2 Ls
    C[3] = 1 A, ends in no L
    C[4] = 1 A, ends in 1 L
    C[5] = 1 A, ends in 2 Ls
    """
    def checkRecord(self, n: int) -> int:
    	C, m = [1,1,0,1,0,0], 10**9 + 7
    	for i in range(n-1):
    		a, b = sum(C[:3]) % m, sum(C[3:]) % m
    		C = [a, C[0], C[1], a + b, C[3], C[4]]
    	return (sum(C) % m)
