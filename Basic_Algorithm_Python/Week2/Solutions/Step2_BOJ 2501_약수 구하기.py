# N�� K�� ��������
N, K = map(int, input().split())

# ��üŽ���� ���� ����� ã������
num = 0
answer = 0
for i in range(1, N+1):
    if (N%i == 0): 
        num += 1
    if (num == K):
        answer = i
        break # for�� Ż��

# ������ ����ϼ���
print(answer)