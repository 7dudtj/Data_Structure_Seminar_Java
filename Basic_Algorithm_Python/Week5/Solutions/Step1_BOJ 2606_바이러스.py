# 2606�� BFS�� Ǯ���
# ������ �Է¹ޱ�
import sys
input = sys.stdin.readline

# import deque
from collections import deque

# ��ǻ���� ���� N���� ��������
N = int(input())

# ����Ǿ��ִ� ��ǻ���� ���� ���� M���� ��������
M = int(input())

# graph list �����ϼ���
graph = [[] for _ in range(N+1)]

# visited list �����ϼ���
visited = [False for _ in range(N+1)]

# count ������ �����ϼ���
count = 0

# ����Ǿ��ִ� ��ǻ���� ���� �Է¹޾Ƽ� �׷����� ���弼��
for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

# queue�� �����ϼ���
queue = deque()

# 1�� ��ǻ�͸� �湮�ϼ���
queue.append(1)
visited[1] = True

# bfs�� �����ϼ���
while queue:
    v = queue.popleft()
    count += 1
    for i in graph[v]:
        if not visited[i]:
            queue.append(i)
            visited[i] = True

# ����� ����ϼ���
print(count-1)