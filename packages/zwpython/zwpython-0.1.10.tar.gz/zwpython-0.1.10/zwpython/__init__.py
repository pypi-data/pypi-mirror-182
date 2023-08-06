'''
zwpython

作者: 山东郭老师 (sdnygls@126.com)

主页: https://tx.glsnh.cn/zwpython.html

使用教程: 微信小程序《教学辅助工具》

升级: pip install --upgrade zwpython

'''

import random


真 = True
假 = False
空 = None
# 打印 = print
输入 = input

# 数值相关
求绝对值=abs
求幂值=pow
求四舍五入=round
求商和余数=divmod
求和 = sum
# 整数=int
# 浮点数=float
复数=complex
# 比较大小=cmp(x,y)

字符串转表达式=eval

# 转换
# 转真假值=bool
# 转字节可变数组=bytearray
# 转不可变字节数组=bytearray
# 转内存查看对象=memoryview
转二进制=bin
转八进制=oct
转十六进制=hex
转字符成统一码=ord
转统一码成字符=chr


# 序列相关
获取长度 = len
获取最大值 = max
获取最小值 = min
获取排序后列表 = sorted
获取反转后序列 = reversed
范围 = range
迭代器=iter
切片器=slice
映射器=map
过滤器=filter
下一个=next
枚举器 = enumerate
打包器 = zip
是否全为真=all
是否某项为真=any


# class相关
是否是后者的子类=issubclass
是否为此种类型=isinstance      # isinstance(10, (int, float)) # True
获取类型=type
是否包含属性=hasattr
获取对象的属性值=getattr
设置对象的属性值=setattr
删除对象的某属性=delattr
是否可调用=callable

文件_打开文件=open

英文关键字 = ['and', 'or', 'not', 'is', 'in', 'if', 'else', 'elif', 'assert','return'
    , 'while', 'break', 'for', 'continue', 'pass', 'del','from','import']
英文关键字2 = ['try', 'except', 'finally', 'raise', 'lambda','global','nonlocal','lambda']


def 打印(*内容: object, 分隔符: str = ' ', 结束: str = '\n') -> None:
    print(*内容, sep=分隔符, end=结束)


def 文件_是否存在(路径文件名):
    是否存在=True
    try:
        f = open(路径文件名)
        f.close()
        是否存在=True
    except IOError:
        是否存在=False
    return 是否存在

def 文件_打开文本文件(路径文件名, 模式:str):
    '''
    模式: 'r'只读，'w'可写，'a'追加。。。

    举例：with 打开文件('txt.txt', 'r') as wj:
    '''
    return open(路径文件名, 模式, encoding='utf-8')

def 文件_读取文本(路径文件名):
    with open(路径文件名, 'r', encoding='utf-8') as wj:
        return wj.read()

def 文件_写入文本(路径文件名,文本内容):
    with open(路径文件名, 'w', encoding='utf-8') as wj:
        return wj.write(文本内容)

def 文件_追加文本(路径文件名,文本内容):
    with open(路径文件名, 'a', encoding='utf-8') as wj:
        return wj.write(文本内容)

class 整数(int):
    pass

class 浮点数(float):
    pass

真假值=bool

class 字符串(str):
    转大写_首字母 = str.capitalize
    转小写字母 = str.lower
    转大写字母 = str.upper
    切换大小写 = str.swapcase
    删除左侧 = str.lstrip
    删除右侧 = str.rstrip
    删除两侧 = str.strip
    统计出现次数 = str.count
    是否以子串结束 = str.endswith
    是否以子串开头 = str.startswith
    是否仅含空格 = str.isspace
    是否仅含数字 = str.isnumeric
    是否仅含正整数 = str.isdigit # 只对正整数有效，负数及小数均返回不正确
    是否仅含字母 = str.isalpha
    加宽_左对齐 = str.ljust
    加宽_右对齐 = str.rjust
    加宽_居中= str.center
    # 用子串分割成三元组 = str.partition
    # 用子串分割成三元组从右侧 = str.rpartition
    # 分割成列表_按行 = str.splitlines
    格式化=format
    连接序列=str.join
    查找子串=str.find   # 找不到会返回-1
    查找子串_从右侧=str.rfind
    替换=str.replace

    # def 替换(self, 被替换: str, 替换成: str):
    #     return self.replace(被替换, 替换成)
    #

    # 分割成列表=str.split
    def 分割成列表(self, 分割符: str=' '):
        return 列表(self.split(分割符))


class 列表(list):
    反转列表 = list.reverse  # 参数不能中文提示，无需参数的使用这种

    def 排序(self, 比较元素=None, 是否降序=False):
        self.sort(key=比较元素, reverse=是否降序)

    def 添加元素(self, 新元素):
        return self.append(新元素)

    def 添加多个元素(self, 新增序列):
        return self.extend(新增序列)

    def 插入元素(self, 位置, 新增元素):
        return self.insert(位置, 新增元素)

    def 删除某元素(self, 元素):
        # 删除列表中某个元素的第一个匹配项
        return self.remove(元素)

    def 删除末尾元素(self, 序号=-1):
        # 删除列表中后面的1个元素,默认最后1个
        return self.pop(序号)

    def 统计出现次数(self, 元素) -> int:
        return self.count(元素)

    def 查找元素位置(self, 元素) -> int:
        # 查找元素中列表中第一次出现的位置,找不到会抛出异常ValueError: x is not in list,建议先判断 x in list
        return self.index(元素)


class 元组(tuple):
    def 统计出现次数(self, 元素) -> int:
        return self.count(元素)

    def 查找元素位置(self, 元素) -> int:
        # 查找元素中元组中第一次出现的位置,找不到会抛出异常ValueError: x is not in list,建议先判断 x in list
        return self.index(元素)


class 字典(dict):
    创建字典_序列为键 = dict.fromkeys
    获取所有键 = dict.keys
    获取所有值 = dict.values
    获取键值对= dict.items
    获取键的值 = dict.get
    获取键的值_无则加 = dict.setdefault
    删除键的值 = dict.pop
    随机删除键值对 = dict.popitem
    清空 = dict.clear
    复制 = dict.copy
    更新同键的值 = dict.update

def 创建字典_序列为键(序列, 默认值=None) ->字典 :
    return 字典(dict.fromkeys(序列, 默认值))


class 集合(set):
    添加元素 = set.add
    更新集合 = set.update
    删除元素 = set.remove
    删除元素 = set.discard
    随机删除元素 = set.pop
    获取交集 = set.intersection
    删除交集外元素 = set.intersection_update
    获取差集 = set.difference
    删除差集外元素 = set.difference_update
    获取异或 = set.symmetric_difference
    删除异或外元素 = set.symmetric_difference_update
    是否被包含 = set.issubset
    是否包含子集 = set.issuperset
    是否不相交 = set.isdisjoint


class 随机数():
    生成随机数 = random.random
    生成范围内随机数 = random.uniform
    获取范围内整数 = random.randint
    获取随机元素 = random.choice
    打乱顺序 = random.shuffle
    获取定长片段 = random.sample
# import sys
# class 系统():
#     退出程序=sys.exit

函数名称='''
打印,输入'''

if __name__ == '__main__':
    打印('函数名称')

