#打印100以内的素数（质数：只能被1和它本身整除）
def prime(num): #定义函数是素数
    for z in range(2, num): #z历遍（2包括，num不含)（左闭右开）
        if divmod(num, z)[1] == 0:#如果num%z取余，看第二位【1】
            return False #如果等于0，证明不是素数
    return True #如果不等于0就是素数

if __name__ == '__main__':
    print([i for i in range(2, 101) if prime(i)])
    #i的范围在2到100之间，历遍。如果i是质数

    #假设i=5；prime(5)；z历遍（2，5）也就是可能是2，3，4；
    #(num,z)就分别可能是(5,2)/(5,3)/(5/4)
    #divmod(num,z)结果是(2,1)/(1,2)/(1,1)
    #(num,z)[1]第二位，等于零就不是素数
