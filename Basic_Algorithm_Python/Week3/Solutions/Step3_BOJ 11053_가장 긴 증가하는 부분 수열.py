# N�� �Է¹�������
N = int(input())

# N���� ������ ������ ���� A�� ����Ʈ�� ��������
A = list(map(int, input().split()))

# dp�� ������ �迭�� ���弼��
# Hint: ��� �ʱⰪ�� 1
dp = [1 for _ in range(N)]

# dp�� �����ϼ���
for i in range(1, N):
    for j in range(0, i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j]+1)

# ���� A�� ���� �� �����ϴ� �κ� ������ ���̸� ����ϼ���
print(max(dp))