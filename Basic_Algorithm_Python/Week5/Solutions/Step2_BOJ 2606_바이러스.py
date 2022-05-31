# 2606�� DFS�� Ǯ���
# ������ �Է¹ޱ�
import sys
input = sys.stdin.readline

# dfs �Լ��� ���弼��
def dfs(graph, v, visited): # v�� ���� Ž���Ϸ� ������ ��
    global count
    visited[v] = True # Ž�������ϱ� �湮 ���� üũ
    for i in graph[v]: # v�� �̿� ������ �߿���
        if not visited[i]: # �湮�� ���� ���� ������ �ִٸ�
            count += 1
            dfs(graph, i, visited) # �湮���� ���� �̿� ������ dfs�� Ž��

# ��ǻ���� ���� N���� ��������
N = int(input())

# ����Ǿ��ִ� ��ǻ���� ���� ���� M���� ��������
M = int(input())
 
# graph list�� �����ϼ���
graph = [[] for _ in range(N+1)] # 0 1 2 .. N-1 N / [ [] [] [] ... [] [] ]

# visited list�� �����ϼ���
visited = [False for _ in range(N+1)] # 0 1 2 .. N-1 N / [ False, False, False, ... False, False ]

# count ������ �����ϼ��� (global variable)
count = 0
 
# ����Ǿ��ִ� ��ǻ���� ���� �Է¹޾Ƽ� �׷����� ���弼��
for _ in range(M):
    node1, node2 = map(int, input().split()) # (node1)----(node2)
    graph[node1].append(node2) # node1 --> node2
    graph[node2].append(node1) # node2 --> node1

# dfs�� �����ϼ���
dfs(graph, 1, visited) # 1: Ž���� ���� ����

# ����� ����ϼ���
print(count)