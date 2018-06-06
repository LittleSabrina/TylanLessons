# 函数定义
def compare():
    a = 1
    b = 2
    _list = [1, 3, 4, 5]
    print(a in _list)
    print(a not in _list)
    condition_1 = a == b
    print(f"condition_1 is {condition_1}")
    print(not a == b)
    if not condition_1:
        print("a is not equal to b")
    else:
        print("a is equal to b")


if __name__ == '__main__':
    # 函数调用
    compare()
