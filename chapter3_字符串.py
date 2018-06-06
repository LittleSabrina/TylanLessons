def str_learn(name):
    # 打印字符串指定索引位字符
    print(name[0])
    print(name[1])

    # 输出name字符串倒数第一位
    print(name[-1])
    print(name[-2])

    # 倒序输出字符串name
    print(name[::-1])
    # 输出name字符串从第0位到倒数第2位
    print(name[0:-1])

    # 按指定字符(比如n)切割字符串
    print(name.split("n")[0])

    # 用指定字符连接字符串
    print(".".join(name.split("n")))
    _list = ["1", "2", "7", "4"]
    print("&".join(_list))
    print("lantianyou".join(_list))

    # 输出字符串长度
    print(len(name))

    # 替换字符串中的n为m
    print(name.replace("", "m"))

    # 判断字符串中的字符是否均为大写
    print(name.isupper())
    print(name.upper().isupper())

    # 判断字符串中的字符是否均为小写
    print(name.islower())

    # 字符串首字母大写并打印
    your_name = ""
    # range(len(name))的意思是在len(name)长度内的变化
    # len(name)的值为6 所以range(len(name))就是 0,1,2,3,4,5 这6位元素
    # 所以 i in range(len(name)) i的值就会轮流是 0,1,2,3,4,5 这6个值
    for i in range(len(name)):
        print(f"i is {i}")
        if i == 0:
            your_name += name[i].upper()
        else:
            your_name += name[i].lower()
    print(your_name)

    # 返回指定字符在字符串中的位置
    print(name.index("s"))

    j = 0
    while True:
        if j < len(name):
            print(name[j])
            j += 1
        else:
            break

    print(f"j is {j}")

    j -= 1
    while j >= 0:
        print(name[j])
        j -= 1


if __name__ == '__main__':
    name = "chensi"
    str_learn(name)
