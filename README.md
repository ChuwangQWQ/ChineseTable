# ChineseTable 是一个用于创建和显示表格的 Python 库

ChineseTable 是一个用于创建和显示表格的 Python 库。它提供了简单的 API 来创建表格，并支持三种不同的样式：thin、double 和 bold。这个库的主要目的是让用户能够轻松地创建和显示表格，特别是在处理数据时。

## 安装

可以通过 pip 安装这个库：

```
pip install table
```

## 使用示例

以下是一个简单的示例，展示了如何使用 table.py 创建一个表格并显示它：

```python
from ChineseTable import Table, Raw, setStyle

# 创建一个表格对象
table = Table([
    Raw(['Name', 'Age', 'City']),
    Raw(['Alice', '30', 'New York']),
    Raw(['Bob', '25', 'San Francisco']),
    Raw(['Charlie', '35', 'Los Angeles'])
])

# 设置表格样式为 bold
setStyle('bold')

# 显示表格
print(table)
```

这将输出以下内容：
```
┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━┓
┃Name         ┃Age          ┃City         ┃
┣━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━┫
┃Alice        ┃30           ┃New York     ┃
┣━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━┫
┃Bob          ┃25           ┃San Francisco┃
┣━━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━┫
┃Charlie      ┃35           ┃Los Angeles  ┃
┗━━━━━━━━━━━━━┻━━━━━━━━━━━━━┻━━━━━━━━━━━━━┛
```

#### 注:库目前只适配等宽字体，并且Raw参数列表中的内容必须为字符串类型。本库支持中文！

总之，ChineseTable 是一个功能强大的 Python 库，用于创建和显示表格。通过简单的 API 和丰富的功能，用户可以轻松地处理数据并创建复杂的表格。