# 2606�� DFS�� Ǯ���
# ������ �Է¹ޱ�
import sys
input = sys.stdin.readline

# dfs �Լ��� ���弼��
def dfs(graph, v, visited):
    global count
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            count += 1
            dfs(graph, i, visited)

# ��ǻ���� ���� N���� ��������
N = int(input())

# ����Ǿ��ִ� ��ǻ���� ���� ���� M���� ��������
M = int(input())
 
# graph list �����ϼ���
graph = [[] for _ in range(N+1)]

# visited list �����ϼ���
visited = [False for _ in range(N+1)]

# count ������ �����ϼ��� (global variable)
count = 0
 
# ����Ǿ��ִ� ��ǻ���� ���� �Է¹޾Ƽ� �׷����� ���弼��
for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

# dfs�� �����ϼ���
dfs(graph, 1, visited)

# ����� ����ϼ���
print(count)