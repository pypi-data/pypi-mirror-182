真 = True
假 = False
空 = None
打印 = print
输入 = input


求绝对值=abs
求幂值=pow
求四舍五入=round
求商和余数=divmod
求和 = sum

字符串转表达式=eval
转二进制=bin
转八进制=oct
转十六进制=hex
转字符成统一码=ord
转统一码成字符=chr


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

是否是后者的子类=issubclass
是否为此种类型=isinstance
获取类型=type
是否包含属性=hasattr
获取对象的属性值=getattr
设置对象的属性值=setattr
删除对象的某属性=delattr
是否可调用=callable

整数=int
浮点数=float
复数=complex

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
    是否仅含正整数 = str.isdigit
    是否仅含字母 = str.isalpha
    加宽_左对齐 = str.ljust
    加宽_右对齐 = str.rjust
    加宽_居中= str.center
    格式化=format
    连接序列=str.join
    查找子串=str.find
    查找子串_从右侧=str.rfind
    替换=str.replace


class 列表(list):
    反转列表 = list.reverse

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