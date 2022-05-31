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

# graph list�� �����ϼ���
graph = [[] for _ in range(N+1)] # 0 1 2 .. N-1 N / [ [] [] [] ... [] [] ]

# visited list�� �����ϼ���
visited = [False for _ in range(N+1)] # 0 1 2 .. N-1 N / [ False, False, False, ... False, False ]

# count ������ �����ϼ���
count = 0

# ����Ǿ��ִ� ��ǻ���� ���� �Է¹޾Ƽ� �׷����� ���弼��
for _ in range(M):
    node1, node2 = map(int, input().split()) # (node1)----(node2)
    graph[node1].append(node2) # node1 --> node2
    graph[node2].append(node1) # node2 --> node1 

# queue�� �����ϼ���
queue = deque()

# 1�� ��ǻ�͸� �湮�ϼ���
queue.append(1)
visited[1] = True

# bfs�� �����ϼ���
while queue: # queue�� �������� ��
    v = queue.popleft() # �ϳ� �̰�
    count += 1
    for i in graph[v]: # v�� �̿� ������ �߿���
        if not visited[i]: # �湮�� �ȵ� �̿���
            queue.append(i) # queue�� �ְ�
            visited[i] = True # �湮 ���� üũ

# ����� ����ϼ���
print(count-1)