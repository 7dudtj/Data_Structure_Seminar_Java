# N�� �Է¹�������
N = int(input())

# N���� ���� ��� ����Ʈ�� ���弼��
list = []

# N���� ���� �Է¹޾Ƽ� ����Ʈ�� �����ϼ���
# Hint: list.append() �Լ��� ����ϼ���
for _ in range(0, N):
    value = int(input())
    list.append(value)

# ����Ʈ�� ������������ �����ϼ���
# Hint: list.sort() �Լ��� ����ϼ���
list.sort()

# ���ĵ� ����� ����ϼ���
for i in range(0, N):
    print(list[i])