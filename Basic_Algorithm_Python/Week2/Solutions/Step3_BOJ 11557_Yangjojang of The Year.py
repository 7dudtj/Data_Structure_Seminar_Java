# �׽�Ʈ���̽��� ���� �Է¹�������
T = int(input())

# �׽�Ʈ���̽��� T�� ����
for _ in range(T):
    # ����Ǯ�̸� ���� ������ ����
    dic = {}
    max = 0

    # �б��� ���� �Է¹�������
    N = int(input())

    # �б��� �� �Һ� ������ �Է¹�������
    for i in range(N):
        S, L = input().split()

        # �Է¹��� ������ dictionary�� �����ϼ���
        # Hint: key: L, value: S
        dic[int(L)] = S

    # dictionary���� key�� �������� �������� �����ϼ���
    sortedDic = sorted(dic.items())

    # �� �Һ� ���� ���� �б��� �̸��� ����ϼ���
    print(sortedDic[-1][1])