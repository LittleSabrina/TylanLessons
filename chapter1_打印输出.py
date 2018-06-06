# 函数定义
def print_test(name, score):
    print(f"Student {name}'s score is {score}")
    score += 1
    # 函数返回值
    return name, score


# 函数定义
def list_test(list_any: list, operation="insert", yuansu="moren", location=0):
    print(f"list_any is {list_any}")
    if operation == "append":
        # 在list的结尾增加元素
        list_any.append(yuansu)
    elif operation == "insert":
        # 在list_any列表指定索引位置增加元素，0是第一位，1是第二位
        list_any.insert(location, yuansu)
    else:
        print("No such operation defined.")
    print(f"list_any is {list_any}")
    # 函数返回值
    return list_any


if __name__ == '__main__':
    # 例子1：print练习
    print("例子1")
    name = "chensi"
    score = 99
    # 调用print_test(name,score)函数并打印其返回值
    print(print_test(name, score))

    # 例子2：list练习
    print("例子2")
    list_a = [1, 2, 323, 23, 4, 5]
    ope = "insert"
    # yuansu = "chensi"
    loca = 1  # 第二位
    aaaaa = list_test(list_any=list_a, operation=ope, location=loca)
    print(aaaaa)
