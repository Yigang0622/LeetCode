# 1472. 设计浏览器历史记录
# https://leetcode-cn.com/problems/design-browser-history/

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [''] * 5000
        self.history[0] = homepage
        self.idx = 0
        self.top = 0

    def visit(self, url: str) -> None:
        self.idx += 1
        self.history[self.idx] = url
        self.top = self.idx

    def back(self, steps: int) -> str:
        if steps >= self.idx:
            self.idx = 0
        else:
            self.idx -= steps
        return self.history[self.idx]

    def forward(self, steps: int) -> str:

        if self.idx + steps <= self.top:
            self.idx = self.idx + steps
            return self.history[self.idx]
        else:
            self.idx = self.top
            return self.history[self.idx]




# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)