# N�� K�� ��������
N, K = map(int,input().split())

# N���� ����� ���� �迭�� ���弼��
arr = [i for i in range(1,N+1)] 

# ���ŵ� ����� ��� answer �迭�� ���弼��
answer = []

# ���ŵ� ����� index�� �����ϼ���
idx = 0

# N���� �����ϼ���
for i in range(N):
    # idx ���� K-1 �ø�����
    idx += (K-1)

    # idx�� arr �迭 ũ�⸦ �Ѿ ���
    if idx >= len(arr):
        idx %= len(arr)

    # �� ����� �����ϼ���
    answer.append(str(arr[idx]))
    arr.pop(idx)

# �似Ǫ�� ������ ����ϼ���
print("<",', '.join(answer),">", sep="")