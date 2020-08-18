import copy


class Solution:
    min_time = 0
    solution = []

    def solve(self, tasks):
        tasks = sorted(tasks)
        n = len(tasks)
        # 最坏情况
        self.min_time = sum(tasks)
        avg = sum(tasks) // 3
        task_queue = [[], [], []]
        self.solution = copy.deepcopy(task_queue)
        self.search(task_queue, n, tasks, avg)

    def search(self, current_task_queue, n, tasks, avg):

        if len(tasks) == 0:
            # 计算最长队列时间
            max_queue_time = max(sum(current_task_queue[0]), sum(current_task_queue[1]), sum(current_task_queue[2]))

            if max_queue_time < self.min_time:
                self.min_time = max_queue_time
                self.solution = copy.deepcopy(current_task_queue)
                print(current_task_queue)

            return

        # 拿取任务队列中的第一个任务
        task = tasks.pop()
        # 放在0，1，2三个打印队列中的一个
        for slot in range(3):

            c = copy.deepcopy(current_task_queue)
            c[slot].append(task)

            # 如果当前任意一个队列总任务时间大于当前最优时间，则放弃继续搜索
            if sum(current_task_queue[0]) >= self.min_time or sum(current_task_queue[1]) >= self.min_time or sum(
                    current_task_queue[2]) >= self.min_time:
                # 剪枝
                return

            t = copy.deepcopy(tasks)
            self.search(c, n, t, avg)


# tasks = [4, 8, 15, 16, 17, 18, 19, 20]
# tasks = [50,1,1,1,1,1,1,1,1,1,1,1,80,30]
tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 104, 1, 2, 3, 4, 5, 112, 7, 7, 8, 123, 10]
# tasks = [500,400,300,300,300,300]
r = Solution().solve(tasks)
