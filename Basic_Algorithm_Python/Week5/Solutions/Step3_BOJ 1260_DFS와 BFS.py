# import libraries
from collections import deque
import sys
input = sys.stdin.readline

# dfs �Լ��� ���弼��
def dfs(v):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

# bfs �Լ��� ���弼��
def bfs(s):
    queue = deque()
    queue.append(s)
    visited[s] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# N, M, V�� �Է¹�������
N, M, V = map(int, input().split())

# graph list�� �����ϰ�, ������ �Է¹޾� �׷����� ���弼��
graph = [[] for _ in range(N+1)]
for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

# graph�� ������������ �����ϼ���
# Hint: graph[1]���� graph[N]���� ���� �������� ����
for i in range(1, N+1): # �� ������ �̿� ���鿡 ���ؼ�
    graph[i].sort() # �������� ����

# dfs�� ���� visited list�� ����� dfs�� �����ϼ���
visited = [False for _ in range(N+1)]
dfs(V)

# �� �ѱ�
print() 

# bfs�� ���� visited list�� ����� bfs�� �����ϼ���
visited = [False for _ in range(N+1)]
bfs(V)