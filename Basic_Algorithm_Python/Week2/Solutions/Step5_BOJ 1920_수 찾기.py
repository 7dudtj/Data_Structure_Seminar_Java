# �̺�Ž�� �Լ�
def doBinarySearch(data, target):
    # left, mid, right �� �ʱ⼳��
    mid = 0
    left = 0
    right = len(data)-1

    # �̺�Ž�� ����
    while (left <= right):
        mid = (left+right)//2

        # ���� ã�� ���
        if (target == data[mid]):
            return 1
        # target�� data[mid]���� ���� ���
        if (target < data[mid]):
            right = mid - 1
        # target�� data[mid]���� ū ���
        else:
            left = mid + 1
    
    # ���� ã�� ���� ���
    return 0


# N�� �Է¹�������
N = int(input())

# N���� ������ �Է¹޾� ����Ʈ�� �������ּ���
data = list(map(int, input().split()))

# N���� ������ ������������ �������ּ���
data.sort()

# M�� �Է¹�������
M = int(input())

# M���� ������ �Է¹޾� ����Ʈ�� �������ּ���
query = list(map(int, input().split()))

# M���� ���� ���ؼ� ���縦 �����մϴ�
# �ð����⵵�� �����Ͽ� ��üŽ���� �ƴ� �̺�Ž���� �մϴ�
for i in range(M):
    target = query[i] # target: Ž���ϰ��� �ϴ� ��
    answer = doBinarySearch(data, target) # �̺�Ž�� �Լ�
    print(answer) # Ž���� ���� ���� ���θ� ����մϴ�