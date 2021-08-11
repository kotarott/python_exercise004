# クラスの作成
class Test:
    x = 1
    y = 2

    def test_method1(self):
        print(self.x)

    def test_method2(self, hennsu1):
        print('引数：', hennsu1)


# インスタンス化
x = Test()

# x.test_method1()
# x.test_method2("test")


# コンストラクタ：初期値の設定
class Test2:
    val = []

    def __init__(self):
        print("init:", str(self.val))
        self.val.append(1)
        self.val.append(2)
        self.val.append(3)

    def test_method1(self):
        print("test:", str(self.val))

# y = Test2()
# y.test_method1()


# コンストラクタ：値指定もできる
class Test3:
    val = []

    def __init__(self, val1, val2):
        print("before:", str(self.val))
        self.val.append(1)
        self.val.append(val1)
        self.val.append(val2)
        print("after:", str(self.val))

# z = Test3(3, 5)


# デストラクタ：インスタンスの削除
class Test4:
    val = []
    def __del__(self):
        print("delete class")

# a = Test4()
# del a


# 変数
# クラス変数：クラスに依存。インスタンス、クラス双方から呼び出しできる。
# インスタンス変数：インスタンスに依存している変数。インスタンスごとに設定できる。
# クラス変数とインスタンス変数の変数名が一緒の場合、インスタンス変数が優先される。

class Test5:
    val ="クラス変数"
    def __init__(self, hensu1):
        self.x = hensu1

# b = Test5("インスタンス：b")
# c = Test5("インスタンス：c")
# print("クラス変数：", b.val, c.val, Test5.val)
# print("インスタンスb：", b.x)
# print("インスタンスc：", c.x)


# 継承：継承したクラスの変数、メソッドを呼び出せる。
# 変数名が同じ⇒Childが優先される。
# super().メソッド名 とすれば、名前が同じでも親クラスを呼び出せる。
# コンストラクタ（初期値）はChildのみ　Parentのコンストラクタ呼び出しはsuper().__init__()

class Parent:
    parent_val = "Parent"

    def parent_function(self):
        print("ParentMethod:", self.parent_val)

    def test(self):
        print("ParentMethod")

class Child(Parent):
    child_val = "Child"

    def child_function(self):
        print("ChildMethod:", self.child_val)

    def test(self):
        print("ChildMethod")
        print("↓super()")
        super().test()

# child = Child()
# print(child.parent_val)
# print(child.child_val)
# child.parent_function()
# child.child_function()
# child.test()


# staticメソッド、classメソッド

# staticメソッド：インスタンスの作成なしに直接呼び出しできる。
    # @staticmethod　とデコレートする必要あり。

class TestStatic:
    @staticmethod
    def test():
        print("staticメソッドです。")

# d = TestStatic()
# d.test()
# TestStatic.test()


# classメソッド：インスタンス生成なしに直接呼び出せる。
    # インスタンスメソッドとはことなり、引数にインスタンスを受け取らず、クラスを受け取る。
    # @classmethod でデコレートする。

class TestClass:
    def __init__(self):
        self.x = 0
        self.y = 0

    def test_print(self):
        print(self.x, self.y)

    @classmethod
    def test(cls, x, y):
        print("Classメソッドです。", cls)
        new_test = cls()
        new_test.x = x
        new_test.y = y
        return new_test

f = TestClass()
f.test_print()
f.test(1, 2)
f.test_print()

g = TestClass.test(3, 4)
g.test_print()
