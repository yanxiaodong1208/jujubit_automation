# 隐式字符串拼接（Implicit String Concatenation）编译时合并，效率高
# "this" + " is" + " a string"	显式拼接	运行时合并，可跨变量
# f"this is {name}"	f-string	运行时格式化，最灵活
from random import random
from unicodedata import name

_CELL_IMAGE_CHAIN = (
    "**/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther"
    "/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther"
    "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]"
    "/XCUIElementTypeCollectionView/XCUIElementTypeCell[{index}]"
    "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage"
)

print(_CELL_IMAGE_CHAIN.format(index=1))
print(_CELL_IMAGE_CHAIN.format(index=2))


stuAll = (
    "this "
    "is "
    "{name}"
)
print(type(stuAll))
print(stuAll.format(name='lily'))
print(stuAll.format(name='bob'))
nname = "frerger"
print(f"aaaaa{nname.isalpha()}", nname)
