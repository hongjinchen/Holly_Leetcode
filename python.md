## Python数据结构

字符串（**str**）：字符串是用引号括起来的**任意文本**，是编程语言中最常用的数据类型。
列表（**list**）：列表是**有序的集合**，可以向其中添加或删除元素。
元组（**tuple**）：元组也是**有序集合**，元组中的数无法修改。即元组是**不可变的**。
字典（**dict**）：字典是**无序的集合**，是由键值对（key-value）组成的。
集合（**set**）：是一组 key 的集合，每个元素都是唯一，**不重复且无序的**。



### 1. 列表（List）

- **定义和用途**: 存储一系列有序元素的动态数组。

- **多元素类型**: 列表可以存储不同类型的元素——**比如整数、浮点数、字符串等。**

- **性能**: 列表在添加或删除元素时性能较好，但对于数值计算不如数组高效。

- **可变性**: 可变。

- **语法**: 使用方括号，例如：`[1, 2, 3]`。

- **主要操作**: `append`, `remove`, `insert`, `sort`等。

  #### **常见操作**

  1. **切片**，同字符串

  2. `append`和 `extend`向列表中添加元素

     ```python
     >>> mylist1 = [1, 2]
     >>> mylist2 = [3, 4]
     >>> mylist3 = [1, 2]
     
     >>> mylist1.append(mylist2)
     >>> print(mylist1)
     [1, 2, [3, 4]]
     
     >>> mylist3.extend(mylist2)
     >>> print(mylist3)
     [1, 2, 3, 4]
     ```

     

  3. **删除元素**

     `del`:根据下标进行删除

     `pop`：删除最后一个元素

     `remove`：根据元素的值进行删除

     ```python
     >>> mylist4 = ['a', 'b', 'c', 'd']
     
     >>> del mylist4[0]
     >>> print(mylist4)
     ['b', 'c', 'd']
     
     >>> mylist4.pop()
     >>> print(mylist4)
     ['b', 'c']
     
     >>> mylist4.remove('c')
     >>> print(mylist4)
     ['b']
     ```

     

  4. **元素排序 `sort`：**是将`list`按特定顺序重新排列，默认为由小到大，参数 `reverse=True`可改为倒序，由大到小。

  ```python
  >>> mylist5 = [1, 5, 2, 3, 4]
  >>> mylist5.sort()
  >>> print(mylist5)
  [1, 2, 3, 4, 5]
  >>> mylist5.reverse()
  >>> print(mylist5)
  [5, 4, 3, 2, 1]
  ```

  1. **`reverse`：**是将`list`逆置。

     

### 2. 元组（Tuple）

- **定义和用途**: 存储一系列**有序元素的不可变数组。**

- **可变性**: 不可变。

- **语法**: 使用圆括号，例如：`(1, 2, 3)`。

- **主要操作**: 访问和切片。

  

### 3. 字典（Dict）

- **定义和用途**: 存储键值对的数据结构。

- **可变性**: **字典中的值可以改变，但键必须是不可变的**（如字符串、元组）。在Python中，一个对象能否作为字典的键取决于该对象是否是不可变（hashable）的。只有当一个对象是不可变的，且实现了`__hash__()`方法，它才能作为字典的键。通常，自定义对象是可哈希的，它们的哈希值基于它们的`id()`，但你可以通过定义`__hash__()`和`__eq__()`方法来改变这个行为。**如果一个对象是可变的，比如列表，它默认是不能作为字典的键的。**

- **语法**: 使用**大括号和冒号分隔键和值**，例如：`{'key1': 'value1', 'key2': 'value2'}`。

- **主要操作**: `keys`, `values`, `items`, `get`, `setdefault`等。

  #### **字典常见操作**

  1. 清空字典 `dict.clear()`

     ```python
     >>> dict1 = {'key1':1, 'key2':2}
     >>> dict1.clear()
     >>> dict1
     {}
     ```

  2. 指定删除：使用 `pop`方法来指定删除字典中的**某一项**（随机的）。

     ```python
     >>> dict1 = {'key1':1, 'key2':2}
     >>> d1 = dict1.pop('key1')
     >>> dict1
     {'key2': 2}
     >>> d1
     1
     ```

  3. 遍历字典

     ```python
     >>> dict2 = {'key1':1, 'key2':2}
     >>> mykey = [key for key in dict2]  # ['key1', 'key2']
     >>> mykey
     ['key1', 'key2']
     >>> myvalue = [value for value in dict2.values()]
     >>> myvalue
     [1, 2]
     >>> key_value = [(k, v) for k, v in dict2.items()]
     >>> key_value
     [('key1', 1), ('key2', 2)]
     ```

  4. `fromkeys`用于创建一个新字典，以序列中元素做字典的键，`value`为字典所有键对应的初始值。

  ```python
  >>> keys = ['zhangfei', 'guanyu', 'liubei', 'zhaoyun']
  >>> dict.fromkeys(keys, 0)
  {'zhangfei': 0, 'guanyu': 0, 'liubei': 0, 'zhaoyun': 0}
  ```

  

### 4. 集合（Set）

- **定义和用途**: **存储一组无序且唯一的元素。**

- **可变性**: 可变。

- **语法**: 使用大括号，例如：`{1, 2, 3}`。

- **主要操作**: `add`, `remove`, `union`, `intersection`等。

  

### 5. 字符串（String）

- **定义和用途**: **存储字符序列。**

- **可变性**: 不可变。

- **语法**: 使用单引号或双引号，例如：`'hello'`或`"hello"`。

- **主要操作**: **`split`, `replace`, `upper`, `lower`等。**

  #### **常见操作**

  1. **切片**：'luobodazahui'[1:3]

  2. ``join`：可以用来连接字符串，将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串。`'-'.join(['luo', 'bo', 'da', 'za', 'hui'])`

  3. `String.replace(old,new,count)`：将字符串中的 `old`字符替换为 `New`字符，`count`为替换的个数 `'luobodazahui-haha'.replace('haha', 'good')`

  4. **split**：切割字符串，得到一个列表

     ```python
     >>> mystr5 = 'luobo,dazahui good'
     
     >>> print(mystr5.split())  # 默认以空格分割
     ['luobo,dazahui', 'good']
     
     >>> print(mystr5.split('h'))  # 以h分割
     ['luobo,daza', 'ui good']
     
     >>> print(mystr5.split(','))  # 以逗号分割
     ['luobo', 'dazahui good']
     ```

     

  **一行代码实现数值交换**

  ```python
  >>> a, b = 1, 2
  >>> a, b = b, a
  >>> print(a, b)
  ```

  

  **is 和 == 的区别**

  `==`是比较操作符，只是判断对象的**值**（value）是否一致，而 `is` 则判断的是对象之间的身份（**内存地址**）是否一致。对象的身份，可以通过 `id()` 方法来查看。

  ```python
  >>> c = d = [1, 2]
  >>> e = [1, 2]
  
  >>> print(c is d)
  True
  
  >>> print(c == d)
  True
  
  >>> print(c is e)
  False
  
  >>> print(c == e)
  True
  ```

  只有 `id`一致时，`is`比较才会返回 `True`，而当 `value`一致时，`==` 比较就会返回 `True`。

  

  `*arg` 和 `**kwarg` 作用

  允许我们在调用函数的时候传入**多个实参**

  ```python
  >>> def test(*arg, **kwarg):
  ...     if arg:
  ...         print("arg:", arg)
  ...     if kwarg:
  ...         print("kearg:", kwarg)
  ...
  >>> test('ni', 'hao', key='world')
  arg: ('ni', 'hao')
  kearg: {'key': 'world'}
  ```

  

  **[lambda x:i*x for i in range(4)]**

  ```python
  >>> def num():
  ...     return [lambda x:i*x for i in range(4)]
  ...
  >>> [m(1) for m in num()]
  [3, 3, 3, 3]
  ```

  

### 6. 数组（Array）

- **定义和用途**: 存储**固定大小和类型的元素序列。**

- **可变性**: 可变。

- **语法**: 使用`array`模块，例如：`array('i', [1, 2, 3])`。

- **主要操作**: `append`, `pop`, `insert`等。

  

### 7. 栈（Stack）和队列（Queue）

- **定义和用途**: 栈用于后进先出（LIFO）的数据存储，队列用于先进先出（FIFO）。

- **可变性**: **可变**。

- **实现方式**: 通常使用列表或特殊的库，如`collections.deque`。

- **主要操作**: 栈有`push`和`pop`，队列有`enqueue`和`dequeue`。

  

### 8. 链表（LinkedList）

- **定义和用途**: 存储一系列**有序元素**，每个元素包含值和指向下一个元素的**引用**。
- **可变性**: 可变。
- **实现方式**: Python没有内置支持，但可以用类来实现。
- **主要操作**: `insert`, `delete`, `find`等



### 数据类型转换

**在Python中，数据类型转换主要是通过内置函数实现的，因为Python是动态类型语言，所以在运行时会自动进行一些类型推断和转换。但有时候我们需要显式地进行类型转换，以确保变量的类型符合我们的预期，这样可以避免运行时错误。**

下面是一些最常用的Python数据类型转换函数：

1. `int(x [,base])`：将x转换为一个整数。base表示进制，默认是十进制。
   
   ```python
   int(3.5)  # 输出: 3
   int("1010", 2)  # 输出: 10, 字符串表示的二进制转为整数
   ```
   
   2. `float(x)`：将x转换到一个浮点数。
```python
float(1)  # 输出: 1.0
float("3.14")  # 输出: 3.14
```

3. `str(x)`：将对象x转换为字符串形式。
   
   ```python
   str(10)  # 输出: "10"
   str([1, 2, 3])  # 输出: "[1, 2, 3]"
   ```
   
   4. `bool(x)`：将x转换为Boolean类型，如果x是非零数值、非空字符串、非空对象等，返回`True`，否则返回`False`。
```python
   bool(0)  # 输出: False
   bool("")  # 输出: False
   bool("Some string")  # 输出: True
```

5. `list(x)`：将序列x转换为一个列表。
   
   ```python
   list("123")  # 输出: ['1', '2', '3']
   list({1, 2, 3})  # 输出: [1, 2, 3]
   ```
   
   6. `tuple(x)`：将序列x转换为一个元组。
```python
   tuple([1, 2, 3])  # 输出: (1, 2, 3)
```

7. `dict(d)`：创建一个字典。d必须是一个序列 (key,value)元组。
   
   ```python
   dict([(1, 'one'), (2, 'two')])  # 输出: {1: 'one', 2: 'two'}
   ```
   
   8. `set(x)`：转换为可变集合。
```python
   set([1, 2, 3, 1])  # 输出: {1, 2, 3}
```

9. `frozenset(x)`：转换为不可变集合。
   ```python
   frozenset([1, 2, 3, 1])  # 输出: frozenset({1, 2, 3})
   ```

10. `bytes(x[, encoding[, errors]])`：将x转换为bytes类型。
    
    ```python
    bytes("hello", "utf-8")  # 输出: b'hello'
    ```
    
    11. `bytearray(x[, encoding[, errors]])`：将x转换为bytearray类型。
```python
    bytearray("hello", "utf-8")  # 输出: bytearray(b'hello')
```

12. `complex(real[, imag])`：创建一个复数。
    
    ```python
    complex(1, 2)  # 输出: (1+2j)
    ```

这些函数都可以用于将数据从一种类型转换为另一种类型，但它们不会改变原始对象，而是创建转换后的类型的新实例。在进行转换时，如果数据无法被转换成有效的类型，如尝试将文本字符串转换成整数，则会抛出`ValueError`异常。使用这些转换函数时，需要确保数据是可转换的，以避免异常。



## python的回收机制

Python 使用一种称为**引用计数的内存管理机制**，以及一个垃圾回收器来清理不再使用的对象。下面我将详细地解释这两个方面。

**引用计数（Reference Counting）**

在 Python 中，每个对象都有一个与之关联的引用计数。当创建一个对象并将其分配给一个变量时，这个对象的引用计数就变为1。如果这个对象被其他变量引用，其引用计数会相应增加。每当一个对象的引用被删除或离开其作用域，引用计数就会减1。当引用计数达到0时，内存就会被释放。

```python
# 创建一个对象（引用计数为 1）
a = [1, 2, 3]

# 引用同一对象（引用计数增加到 2）
b = a

# 解除一个引用（引用计数减少到 1）
del a

# 解除另一个引用（引用计数减少到 0，对象被删除）
del b
```

**垃圾回收（Garbage Collection）**

引用计数有一些局限性，尤其是不能处理引用循环。垃圾回收机制可以检测到这样的循环，并将其打破。

```python
# 创建引用循环
a = {}
b = {}
a['b'] = b
b['a'] = a

# 此时即使 del a 和 del b，a 和 b 仍然存在引用循环，不会被销毁
```

Python 的垃圾回收机制主要基于“代”（**Generations**）的概念。所有新创建的对象开始时都位于**第一代（youngest generation）**。如果第一代的对象经过一次垃圾回收仍然存在，则被移动到第二代。同理，第二代对象经过垃圾回收后仍然存在的话，则被移动到第三代。

Python 默认开启垃圾回收机制，但你也可以手动控制它：

- `gc.collect()`：手动运行垃圾回收。
- `gc.set_threshold()`：设置垃圾回收触发的阈值。
- `gc.get_stats()`：获取垃圾回收统计信息。

**综合**

Python 的内存管理机制综合了引用计数和垃圾回收，以达到高效和准确的内存回收。这使得在大多数情况下，开发者可以不必担心内存泄漏，而可以集中精力去解决更有意义的问题。

希望这个详细的解释能帮助你更好地理解 Python 的内存回收机制。



## **解释型和编译型语言的区别**

- **编译型语言**：**把做好的源程序全部编译成二进制的可运行程序。然后，可直接运行这个程序。如：C，C++ ；**

  编译型语言的源代码在程序运行之前需要一个单独的编译过程，将源代码转换成机器码或者中间码（如Java的字节码）。编译过程通常由编译器完成，这个过程涉及源代码的分析、优化和转换。

  **特点**：

  - **性能**：编译后的代码通常执行速度快，因为它已经是优化后的机器码。
  - **一次编译，多处运行**：编译后的程序（如果是生成机器码的话）依赖于特定的操作系统和硬件平台。如果是生成中间码（如Java字节码），则可以在任何有对应虚拟机的平台上运行。
  - **部署**：用户只需部署编译后的程序，无需源代码。
  - **开发周期**：编写、编译和测试的周期可能比较长，因为每次更改后都需要重新编译。

  **例子**：C、C++、Go、Rust、Swift和Java（注意Java是特例，它编译成字节码，然后由JVM解释或即时编译执行）。

  

- **解释型语言**：**把做好的源程序翻译一句，然后执行一句，直至结束，如：Python。**

  解释型语言的源代码通常在程序执行时由一个解释器逐行或逐块转换成中间表示或直接执行，不需要单独的编译过程。

  **特点**：

  - **便利性**：代码可以即写即运行，适合快速开发和原型设计。
  - **跨平台**：解释器可以为不同的操作系统提供，使得写一次代码可以在多个平台上运行。
  - **灵活性**：易于调试和测试，因为可以逐行运行代码并立即查看结果。
  - **性能**：通常来说，解释型语言在运行时的性能较编译型语言慢，因为每次执行时都需要进行源代码到机器码的转换。

  **例子**：Python、Ruby、Perl、PHP、JavaScript和Shell脚本。



## python浅拷贝和深拷贝

#### python浅拷贝（Shallow Copy）

1. 使用切片操作（只适用于列表和其他序列类型）。

   ```python
   original_list = [1, [2, 3], 4]
   copied_list = original_list[:]
   ```

2. 使用 `copy` 模块的 `copy()` 函数。

   ```python
   import copy
   copied_object = copy.copy(original_object)
   ```

3. 对于字典，可以使用 `dict.copy()` 方法。

   ```python
   original_dict = {'a': 1, 'b': [2, 3]}
   copied_dict = original_dict.copy()
   ```

4. 对于集合，可以使用 `set.copy()` 方法。

   ```python
   original_set = {1, 2, 3}
   copied_set = original_set.copy()
   ```



#### python深拷贝（Deep Copy）

深拷贝会复制对象以及其包含的所有嵌套对象。这意味着，**生成的新对象是原始对象的完全独立副本。**

1. 使用 模块的  函数。

   ```python
   deepcopy()
   ```

   ```python
   import copy
   deep_copied_object = copy.deepcopy(original_object)
   ```



#### 深拷贝示例

```python
import copy

original_list = [1, [2, 3], 4]
deep_copied_list = copy.deepcopy(original_list)

# 修改原始列表
original_list[0] = 0
original_list[1][0] = 0

# 输出两个列表
print("Original:", original_list)  # Output: [0, [0, 3], 4]
print("Deep Copied:", deep_copied_list)  # Output: [1, [2, 3], 4]
```



## 装饰器

装饰器是 Python 的一种高级特性，用于修改或增强函数或方法的行为。**它们通常用于代码重用或者功能抽象。**装饰器是一种特殊类型的函数，**它接受一个函数作为输入，然后返回一个新的函数。**



#### 定义装饰器

一个简单的装饰器示例如下：

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# 当调用 say_hello() 时，实际上调用的是 my_decorator(say_hello)()
say_hello()
```



#### 使用装饰器

装饰器通常使用 `@` 符号和装饰器函数名来应用，紧跟在被装饰函数的定义之前。

```python
@my_decorator
def my_function():
    pass
```

这实际上是以下代码的语法糖：

```python
my_function = my_decorator(my_function)
```



## 生成器

生成器是一种用于创建迭代器的简单而强大的工具。与普通函数不同，生成器函数允许你使用 `yield` 语句暂停函数的执行，并在稍后恢复。

#### 创建生成器

1. **生成器函数**：使用 `yield` 关键字定义。

   ```python
   def my_generator():
       yield 1
       yield 2
       yield 3
   ```

2. **生成器表达式**：与列表推导式类似，但使用圆括号。

   ```python
   gen = (x * x for x in range(3))
   ```

#### 使用生成器

生成器可以用 `for` 循环进行迭代：

```python
for item in my_generator():
    print(item)
```

或者用 `next()` 函数逐个获取值：

```python
gen = my_generator()
print(next(gen))  # 输出 1
print(next(gen))  # 输出 2
```

### 区别和联系

1. **目的**：**装饰器用于修改或增强函数**，**而生成器用于创建可迭代对象。**
2. **语法**：**装饰器使用 `@` 符号和装饰器函数**，**生成器使用 `yield` 关键字或生成器表达式。**
3. **用例**：装饰器通常用于**日志、权限校验**等，生成器常用于流式处理大量数据。



## 迭代器（Iterator）

1. **定义方式**：迭代器是实现了 `__iter__()` 和 `__next__()` 方法的类。
2. **状态保存**：与生成器类似，迭代器也保存其状态，用于下一次的迭代。
3. **资源占用**：除非特别设计，否则迭代器通常在内存中保存整个序列。
4. **可重用但不自动重置**：迭代器可以多次遍历，但必须手动重置（例如，通过重新初始化）。
5. **灵活性**：因为它是基于类的，所以在功能上更加灵活。你可以定义更复杂的操作。

```python
# 迭代器示例
class MyIterator:
    def __init__(self):
        self.numbers = [1, 2, 3]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.numbers):
            result = self.numbers[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

iter = MyIterator()
print(next(iter))  # 输出 1
print(next(iter))  # 输出 2
```

**主要区别总结：**

- **定义方式不同**：生成器是用函数定义的，而迭代器是用类定义的。
- **简洁与灵活性的权衡**：生成器通常代码更少、更简洁，但迭代器更灵活。
- **内存效率**：生成器通常更内存高效，因为它们不需要一次性加载整个序列到内存。
- **用途**：生成器通常用于一次性遍历数据，迭代器更适用于需要多次遍历或手动控制遍历过程的场合。



## Magic Method

Magic methods，也被称**作特殊方法或双下方法**，是Python中的特殊的内置方法，它们以双下划线开头和结尾（例如 `__init__`、`__str__` 等）。这些方法为开发者**提供了创建或自定义行为的方式，**例如定义一个对象的迭代行为、上下文管理协议、运算符重载等。

一些常见的 magic methods 包括：

- `__init__(self, ...)`: 构造器，当一个实例被创建时调用。
- `__del__(self)`: 析构器，当一个实例被销毁时调用。
- `__str__(self)`: 定义 `str()` 被调用时的行为。
- `__repr__(self)`: 定义 `repr()` 被调用时的行为，通常用于调试。
- `__eq__(self, other)`: 定义相等性行为的 `==` 运算符。
- `__len__(self)`: 定义当 `len()` 被调用时的行为。
- `__getitem__(self, key)`: 定义获取元素的行为，例如 `obj[key]`。
- `__setitem__(self, key, value)`: 定义设置元素的行为，例如 `obj[key] = value`。
- `__iter__(self)`: 定义迭代器协议的 `iter()` 方法。
- `__next__(self)`: 定义迭代器协议的 `next()` 方法。

通过实现这些 magic methods，您可以定义自定义类型的行为，使其更接近内置类型的行为。



### 私有变量和受保护变量

- `__name`：双下划线前缀的变量被视为类的私有变量。Python会对这样的变量名称进行改写（name mangling），在类的内部可以访问，但在类的外部不可直接访问。它用于当你想避免子类重写这些变量时。
- `_value`：单下划线前缀的变量通常被视为受保护的变量（protected），这是一个约定俗成的规则，意味着它只应该被类本身和子类访问，但实际上它是可访问的，这依赖于程序员的遵守。

例如：

```python
class MyClass:
    def __init__(self):
        self.__private_var = "I am private"
        self._protected_var = "I am protected"

obj = MyClass()
# print(obj.__private_var) # 这会抛出异常
print(obj._protected_var)  # 这通常不推荐，但是是可能的
```



## 栈和堆

在Python中，栈（Stack）和堆（Heap）是两种用于内存分配的数据结构，它们在内存管理中扮演不同的角色。理解它们之间的区别对于编写高效和优化的Python代码非常重要。下面是栈和堆的主要区别：

- #### 栈（Stack）

1. **内存分配**：栈用于**静态内存分配**。这意味着在**程序编译时就已经分配了内存空间**。
2. **访问速度**：**栈上的内存分配和回收速度非常快。这是因为它使用后进先出（LIFO）的方式来管理数据。**
3. **存储内容**：通常用于存储局部变量、函数参数、返回地址等。
4. **生命周期**：栈中的数据通常在声明的函数运行结束后就会被清除。
5. **大小限制**：栈的大小通常有限，它取决于操作系统，一旦超出这个限制就会导致栈溢出错误。
6. **管理方式**：由操作系统自动管理，不需要程序员手动控制。

- #### 堆（Heap）

1. **内存分配**：堆用于**动态内存分配**，**内存的分配和释放是在程序运行时进行的**。
2. **访问速度**：**堆上的内存分配和回收速度相对较慢，因为涉及到更复杂的内存管理系统。**
3. **存储内容**：通常用于存储需要长时间存活或大小不确定的数据，如动态分配的数组、对象等。
4. **生命周期**：堆中的数据生命周期较长，直到被垃圾回收或程序结束。
5. **大小限制**：堆的大小受限于计算机系统中的可用内存，通常比栈大得多。
6. **管理方式**：需要程序员或垃圾回收机制来手动管理。

- #### 在Python中的应用

- Python作为一种高级语言，其内存管理主要是由Python的内存管理器和垃圾回收器自动处理的。
- 局部变量和函数调用的上下文通常存储在栈上。
- 当你在Python中创建对象（如列表、字典、类实例等）时，这些对象通常存储在堆上。



# 测试

## 单元测试--unittest

在Python中进行单元测试通常涉及使用内置的`unittest`框架。这个框架提供了一套丰富的工具来构建和运行测试，帮助开发者确保代码的正确性和稳定性。

### 基本步骤

1. **编写测试用例**：创建一个继承自`unittest.TestCase`的类，并在该类中编写一系列的测试方法。

2. **设置和拆卸**：使用`setUp()`和`tearDown()`方法来进行每个测试前后的准备和清理工作。

3. **断言**：使用断言方法（如`assertEqual()`, `assertTrue()`, `assertRaises()`等）来检查代码行为是否符合预期。

4. **运行测试**：通过命令行或IDE运行测试。

### 示例

以下是一个简单的单元测试示例，假设我们有一个名为`math_functions.py`的文件，其中包含一个`add`函数，用于计算两个数的和：

```python
# math_functions.py

def add(x, y):
    return x + y
```

为了对这个函数进行单元测试，我们可以创建一个测试类，如下所示：

```python
# test_math_functions.py

import unittest
from math_functions import add

class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()
```

在这个测试类中，`TestMathFunctions` 继承了 `unittest.TestCase`。`test_add` 方法中使用了 `assertEqual` 来检查 `add` 函数的输出是否符合预期。
