# T�� ��������
T = int(input())

# Tȸ �ݺ�
for i in range(T):
    # stack list�� �����ϰ� �Է� �� ���� ��������
    stack = []
    ps = input()
    
    # �Է¿� ���� ����
    for item in ps:
        # stack�� ���� �ʾ�����
        if stack:
            # item: "("
            if item =='(':
                stack.append(item)
            # item: ")"
            else:
                if stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(item)
        # stack�� �������
        else:
            stack.append(item)

    # �� �ٿ� ���� ��� ���
    if stack:
        print("NO")
    else:
        print("YES")