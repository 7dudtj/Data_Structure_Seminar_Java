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
        if (True): # if ������ ä���ּ���
            return 1
        # target�� data[mid]���� ���� ���
        if (True): # if ������ ä���ּ���
            continue # ���⸦ �������ּ���
        # target�� data[mid]���� ū ���
        else:
            continue # ���⸦ �������ּ���
    
    # ���� ã�� ���� ���
    return 0


# N�� �Է¹�������


# N���� ������ �Է¹޾� ����Ʈ�� �������ּ���
data = [] # ���⸦ �������ּ���

# N���� ������ ������������ �������ּ���


# M�� �Է¹�������
M = 0 # ���⸦ �������ּ���

# M���� ������ �Է¹޾� ����Ʈ�� �������ּ���
query = [] # ���⸦ �������ּ���

# M���� ���� ���ؼ� ���縦 �����մϴ�
# �ð����⵵�� �����Ͽ� ��üŽ���� �ƴ� �̺�Ž���� �մϴ�
for i in range(M):
    target = query[i] # target: Ž���ϰ��� �ϴ� ��
    answer = doBinarySearch(data, target) # �̺�Ž�� �Լ�
    print(answer) # Ž���� ���� ���� ���θ� ����մϴ�