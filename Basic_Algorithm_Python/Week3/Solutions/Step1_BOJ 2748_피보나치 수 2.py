# n�� �Է¹�������
n = int(input())

# dp�� ������ �迭�� ���弼��
dp = [0 for _ in range(n+1)]

# �ʱⰪ�� �������ּ���
# Hint: dp[0] = 0, dp[1] = 1
dp[1] = 1

# dp�� �����ϼ���
for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]

# n��° �Ǻ���ġ ���� ����ϼ���
print(dp[-1])