class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        w = self.overLap(A,C,E,G)
        h = self.overLap(B,D,F,H)
        area1 = (D - B) * (C - A)
        area2 = (H - F) * (G - E)
        return area1 + area2 - w * h

    # p1 p2 在 和 p3 p4 部分重合（左右），或者两个线完全重合（上短下长或上长下短）
    def overLap(self, p1, p2, p3, p4):
        if p1 <= p3 and p2 <= p4 and p2 > p3:
            return p2 - p3
        elif p3 <= p1 and p4 <= p2 and p1 < p4:
            return p4 - p1
        elif p1 >= p3 and p4 >= p2:
            return p2 - p1
        elif p3 >= p1 and p2 >= p4:
            return p4 - p3
        else:
            return 0


A = -3
B = 0
C = 3
D = 4
E = 0
F = -1
G = 9
H = 2
s = Solution().computeArea(A, B, C, D, E, F, G, H)
