"""
 * Project name(项目名称)：Python_tuple元组
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/22 
 * Time(创建时间)： 12:29
 * Version(版本): 1.0
 * Description(描述)：
 元组和列表（list）的不同之处在于：
列表的元素是可以更改的，包括修改元素值，删除和插入元素，所以列表是可变序列；
而元组一旦被创建，它的元素就不可更改了，所以元组是不可变序列。
(element1, element2, ... , element n)
其中 element1~element n 表示元组中的各个元素，个数没有限制，只要是 Python 支持的数据类型就可以。

 """

if __name__ == '__main__':
    # Python创建元组
    num = (7, 14, 21, 28, 35)
    print(num)
    num1 = 1, 2, 3
    print(num1)
    # 当创建的元组中只有一个字符串类型的元素时，该元素后面必须要加一个逗号,，否则 Python 解释器会将它视为字符串
    str1 = ("hello")
    print(str1)
    print(type(str1))
    str2 = ("hello",)
    print(str2)
    print(type(str2))

    # 将字符串转换成元组
    tup1 = tuple("hello")
    print(tup1)
    # 将列表转换成元组
    list1 = ['Python', 'Java', 'C++', 'JavaScript']
    tup2 = tuple(list1)
    print(tup2)
    # 将字典转换成元组
    dict1 = {'a': 100, 'b': 42, 'c': 9}
    tup3 = tuple(dict1)
    print(tup3)
    # 将区间转换成元组
    range1 = range(1, 6)
    tup4 = tuple(range1)
    print(tup4)
    # 创建空元组
    print(tuple())

    # Python访问元组元素
    range2 = range(0, 20)
    tup5 = tuple(range2)
    print(tup5)
    print(tup5[3])
    print(tup5[4])
    print(tup5[6])
    print(tup5[8])
    print(tup5[9])
    print(tup5[0])
    print(tup5[18])
    print(tup5[-6])
    print(tup5[-9])
    print(tup5[4:9])
    print(tup5[3:15:2])
    range3 = range(0, 20)
    tup6 = tuple(range3)
    print(tup5 + tup6)
    print(tup5 * 10)

    # Python删除元组
    del tup6
    # print(tup6)

    input()
