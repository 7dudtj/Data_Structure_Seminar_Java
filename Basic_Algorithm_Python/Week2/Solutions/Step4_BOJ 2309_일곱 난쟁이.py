# ��ȩ �������� Ű�� �޾Ƽ� ����Ʈ�� �����ϼ���
dwarf = []
for _ in range(9):
    height = int(input())
    dwarf.append(height)

# ��ȩ �������� Ű�� ���� ���ϼ���
sumOfHeight = 0
for i in range(9):
    sumOfHeight += dwarf[i]

# ��¥ ������ 2���� ã���ּ���
oneIdx = -1
twoIdx = -1
for i in range(0, 8):
    for j in range(1, 9):
        # ��¥ ������ 2���� ã�� ���
        if (dwarf[i]+dwarf[j] == sumOfHeight-100):
            # �� �������� ��ġ�� �������ּ���
            oneIdx = i
            twoIdx = j

# ��¥ �������� Ű�� ����Ʈ���� 0���� ������ּ���
dwarf[oneIdx] = 0
dwarf[twoIdx] = 0

# �������� Ű�� ������������ �������ּ���
dwarf.sort() # [0, 0, 1�� ... 7��]

# ��¥ ������ 7���� Ű�� ������ּ���
for i in range(2, 9):
    print(dwarf[i])
