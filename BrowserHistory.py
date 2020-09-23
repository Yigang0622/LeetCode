# 1472. 设计浏览器历史记录
# https://leetcode-cn.com/problems/design-browser-history/

class BrowserHistory:


    def __init__(self, homepage: str):
        self.history = [homepage]
        self.idx = 0

    def visit(self, url: str) -> None:
        self.history.append(url)
        self.idx += 1

    def back(self, steps: int) -> str:
        pass

    def forward(self, steps: int) -> str:
        pass



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)