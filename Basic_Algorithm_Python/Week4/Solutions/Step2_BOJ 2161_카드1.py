# queue �������� �����ϼ���
from queue import Queue
q = Queue()

# N�� �Է¹ް� ť�� N���� ī�带 ��������
N = int(input())
for i in range(1, N+1):
    q.put(i)

# ���� ī�带 ��Ƶ� list �����ϼ���
answer = []

# queue���� �۾��� �����ϼ���
# queue�� ī�尡 �������� �� ����
while (q.qsize() > 0):
    # ī�� ������
    outCard = q.get()
    answer.append(outCard)
    # queue�� ī�尡 ������ ��, �� �� ī�带 �� �ڷ� ������
    if (q.qsize() > 0):
        inCard = q.get()
        q.put(inCard)

# ������ ī���� ���� ī�带 ����ϼ���
print(*answer)