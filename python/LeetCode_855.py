""" 
https://leetcode-cn.com/problems/exam-room/
855. 考场就座
"""


class ExamRoom:

    def __init__(self, n: int):
        self.N = n
        self.students = []

    def seat(self) -> int:
        if not self.students:
            student = 0
        else:
            dist, student = self.students[0], 0
            for i, s in enumerate(self.students):
                if i:
                    prev = self.students[i-1]
                    d = (s - prev) // 2
                    if d > dist:
                        dist, student = d, prev + d

            d = self.N - 1 - self.students[-1]
            if d > dist:
                student = self.N - 1

        bisect.insort(self.students, student)
        return student

    def leave(self, p: int) -> None:
        self.students.remove(p)
        # Your ExamRoom object will be instantiated and called as such:
        # obj = ExamRoom(n)
        # param_1 = obj.seat()
        # obj.leave(p)
