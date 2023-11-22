# JAVA

## Java 基础语法

一个 Java 程序可以认为是一系列对象的集合，而这些对象通过调用彼此的方法来协同工作。下面简要介绍下类、对象、方法和实例变量的概念。

- **对象**：对象是类的一个实例，有状态和行为。例如，一条狗是一个对象，它的状态有：颜色、名字、品种；行为有：摇尾巴、叫、吃等。
- **类**：类是一个模板，它描述一类对象的行为和状态。
- **方法**：方法就是行为，一个类可以有很多方法。逻辑运算、数据修改以及所有动作都是在方法中完成的。
- **实例变量**：每个对象都有独特的实例变量，对象的状态由这些实例变量的值决定。



<img src="https://www.runoob.com/wp-content/uploads/2013/12/662E827A-FA32-4464-B0BD-40087F429E98.jpg" alt="img" style="zoom: 67%;" />





### 基本语法

编写 Java 程序时，应注意以下几点：

- **大小写敏感**：Java 是大小写敏感的，这就意味着标识符 Hello 与 hello 是不同的。
- **类名**：对于所有的类来说，类名的首字母应该大写。如果类名由若干单词组成，那么每个单词的首字母应该大写，例如 **MyFirstJavaClass** 。
- **方法名**：所有的方法名都应该以小写字母开头。如果方法名含有若干单词，则后面的每个单词首字母大写。
- **源文件名**：源文件名必须和类名相同。当保存文件的时候，你应该使用类名作为文件名保存（切记 Java 是大小写敏感的），文件名的后缀为 **.java**。（如果文件名和类名不相同则会导致编译错误）。
- **主方法入口**：所有的 Java 程序由 **public static void main(String[] args)** 方法开始执行。



### Java 标识符

Java 所有的组成部分都需要名字。**类名、变量名以及方法名都被称为标识符。**

关于 Java 标识符，有以下几点需要注意：

- 所有的标识符都应该以**字母（A-Z 或者 a-z）,美元符（$）、或者下划线（_）开始**

- 首字符之后可以是**字母（A-Z 或者 a-z）,美元符（$）、下划线（_）或数字的任何字符组合**

- **关键字不能用作标识符**

- 标识符是**大小写敏感的**

- 合法标识符举例：age、$salary、_value、__1_value

- 非法标识符举例：123abc、-salary

  

### Java修饰符

像其他语言一样，Java可以使用修饰符来修饰类中方法和属性。主要有两类修饰符：

- 访问控制修饰符 : **default, public , protected, private**

- 非访问控制修饰符 : **final**, **abstract**, **static**, **synchronized**

  
  
  ### 访问控制修饰符
  
  1. **default**：当没有显式地定义访问控制修饰符时，默认使用的是default。这意味着代码中的成员（类、方法、变量等）对同一个包内的类是可见的。对于不同包内的类，这些成员是不可见的。
  2. **public**：public修饰符指定成员是公共的，意味着任何其他类都可以访问这些成员，不受包限制。
  3. **protected**：protected修饰符指定成员在同一个包内的类或不同包中的子类可见。
  4. **private**：private修饰符指定成员是私有的，只有声明这些成员的类才可以访问它们。即使是这个类的子类或同一个包中的其他类也无法访问。
  
  ### 非访问控制修饰符
  
  1. **final**：final修饰符用于声明属性、方法和类。
  
     - **对变量**：如果用final修饰一个变量，则该变量的值不可变。
     - **对方法**：用final修饰的方法不能被子类覆盖。
     - **对类**：用final修饰的类不能被继承。
  
  2. **abstract**：abstract修饰符用于创建抽象类和抽象方法。
  
     - **抽象类**：不能被实例化，通常用作其他类的超类。
     - **抽象方法**：没有具体实现，必须在子类中被覆盖和实现。
  
  3. **static**：static修饰符指示成员（变量、方法、块或类）是静态的，这意味着这些成员属于类，而不是属于任何特定的类实例。静态成员可以在没有创建类实例的情况下被访问。
  
  4. **synchronized**：synchronized修饰符用于方法或代码块。synchronized方法或代码块确保在同一时刻只有一个线程可以执行该段代码。这对于实现线程安全是必要的，当多个线程尝试同时更新共享数据时，可以防止数据不一致。
  
     

### Java 变量

Java 中主要有如下几种类型的变量

- **局部变量**

  局部变量是在方法内部、构造方法内部、或者任何块内部（比如在`if`、`for`或`while`块中）声明的变量。这些变量只在声明它们的区域内可见，并且它们的生命周期也限制在这个区域内。一旦区域执行完毕，局部变量就会从栈内存中消失。

  - **声明位置**：方法、构造器或块内部。
  - **作用域**：局部变量的作用域局限于它们被声明的块。
  - **生命周期**：当控制离开声明它们的块时结束。
  - **初始化**：局部变量不会得到默认初始化，它们在使用前必须显式初始化。
  - **存储**：存储在栈内存中。

  **示例**：

  ```java
  void myMethod() {
      int localVar = 10; // localVar 是一个局部变量
      System.out.println(localVar);
  }
  ```

  

- **类变量（静态变量）**

  类变量或静态变量是使用**`static`关键字**声明的，并且它们在类级别上存在，而不是实例级别上。这意味着类的所有实例共享同一个静态变量。类变量是在类加载时创建的，并在程序结束时销毁。

  - **声明位置**：在类中，但方法或块之外。
  - **作用域**：可以在类被加载时访问，直到程序结束。
  - **生命周期**：随着类的加载而创建，随着程序结束而销毁。
  - **初始化**：类变量会得到默认初始化，即即使你没有显式初始化一个静态变量，它也会被赋予一个默认值（例如`int`类型的默认值是`0`）。
  - **存储**：存储在方法区内存中。

  **示例**：

  ```java
  class MyClass {
      static int classVar = 20; // classVar 是一个类变量（静态变量）
  
      void myMethod() {
          System.out.println(classVar);
      }
  }
  ```

  

- **成员变量（非静态变量）**

**成员变量（Member Variables）**，也称为字段（Fields），是**定义在类中的变量**，用于存储对象的状态信息。在面向对象编程（OOP）中，成员变量对应着对象的属性。

以下是关于成员变量的一些关键点：

1. **作用域**：成员变量通常有类级别的作用域。这意味着它们可以被类中的所有方法访问，也可以被类的对象访问，具体取决于它们的访问修饰符（如 `private`, `protected`, `public`）。
2. **初始化**：在Java中，如果你没有显式地为成员变量赋值，它们会被自动初始化为默认值（例如，数值类型默认为0，布尔类型默认为`false`，对象引用默认为`null`）。
3. **实例变量与类变量**：
   - **实例变量**：没有用 `static` 修饰的成员变量称为实例变量。每个对象有自己的一套实例变量副本。
   - **类变量**：用 `static` 修饰的成员变量称为类变量或静态变量。类的所有实例共享同一份类变量副本。
4. **生命周期**：实例变量的生命周期与对象的生命周期一致，而类变量的生命周期从它被加载到内存开始直到程序结束。
5. **访问控制**：可以使用访问修饰符控制其他类对成员变量的访问。例如，使用 `private` 修饰符使成员变量仅在定义它的类内部可见，这是封装的一部分。

下面是一个Java类示例，展示了实例变量和类变量的使用：

```java
public class Person {
    // 实例变量
    private String name;
    private int age;

    // 类变量
    public static int numberOfPeople = 0;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
        Person.numberOfPeople++; // 更新类变量
    }

    // 方法可以访问成员变量
    public void sayHello() {
        System.out.println("Hello, my name is " + name + " and I am " + age + " years old.");
    }
}

public class Main {
    public static void main(String[] args) {
        Person alice = new Person("Alice", 25);
        Person bob = new Person("Bob", 30);

        alice.sayHello(); // 使用Alice的实例变量
        bob.sayHello(); // 使用Bob的实例变量

        System.out.println(Person.numberOfPeople); // 输出类变量，显示创建了多少个Person对象
    }
}
```

在上面的例子中，`name` 和 `age` 是实例变量，每个 `Person` 对象都有自己的 `name` 和 `age` 副本。`numberOfPeople` 是一个类变量，由 `Person` 类的所有实例共享。



## Java 数据类型

变量就是申请内存来存储值。也就是说，当创建变量的时候，需要在内存中申请空间。

内存管理系统根据变量的类型为变量分配存储空间，分配的空间只能用来储存该类型数据。

![img](https://www.runoob.com/wp-content/uploads/2013/12/2020-10-27-code-mem.png)

因此，通过定义不同类型的变量，可以在内存中储存整数、小数或者字符。

Java 的数据类型可以分为两大类：**基本数据类型（Primitive Data Types）和引用数据类型（Reference Data Types）。**



### **基本数据类型/内置数据类型**

Java语言提供了八种基本类型。六种数字类型（四个整数型，两个浮点型），一种字符类型，还有一种布尔型。

**byte：**

- byte 数据类型是8位、有符号的，以二进制补码表示的整数；
- 最小值是 **-128（-2^7）**；
- 最大值是 **127（2^7-1）**；
- 默认值是 **0**；
- byte 类型用在大型数组中节约空间，主要代替整数，因为 byte 变量占用的空间只有 int 类型的四分之一；
- 例子：byte a = 100，byte b = -50。

**short：**

- short 数据类型是 16 位、有符号的以二进制补码表示的整数
- 最小值是 **-32768（-2^15）**；
- 最大值是 **32767（2^15 - 1）**；
- Short 数据类型也可以像 byte 那样节省空间。一个short变量是int型变量所占空间的二分之一；
- 默认值是 **0**；
- 例子：short s = 1000，short r = -20000。

**int：**

- int 数据类型是32位、有符号的以二进制补码表示的整数；
- 最小值是 **-2,147,483,648（-2^31）**；
- 最大值是 **2,147,483,647（2^31 - 1）**；
- 一般地整型变量默认为 int 类型；
- 默认值是 **0** ；
- 例子：int a = 100000, int b = -200000。

**long：**

- long 数据类型是 64 位、有符号的以二进制补码表示的整数；
- 最小值是 **-9,223,372,036,854,775,808（-2^63）**；
- 最大值是 **9,223,372,036,854,775,807（2^63 -1）**；
- 这种类型主要使用在需要比较大整数的系统上；
- 默认值是 **0L**；
- 例子： **long a = 100000L**，**long b = -200000L**。
  "L"理论上不分大小写，但是若写成"l"容易与数字"1"混淆，不容易分辩。所以最好大写。

**float：**

- float 数据类型是单精度、32位、符合IEEE 754标准的浮点数；
- float 在储存大型浮点数组的时候可节省内存空间；
- 默认值是 **0.0f**；
- 浮点数不能用来表示精确的值，如货币；
- 例子：float f1 = 234.5f。

**double：**

- double 数据类型是双精度、64 位、符合 IEEE 754 标准的浮点数；

- 浮点数的默认类型为 double 类型；

- double类型同样不能表示精确的值，如货币；

- 默认值是 **0.0d**；

- 例子：

  ```
  double   d1  = 7D ;
  double   d2  = 7.; 
  double   d3  =  8.0; 
  double   d4  =  8.D; 
  double   d5  =  12.9867; 
  ```

  7 是一个 int 字面量，而 7D，7. 和 8.0 是 double 字面量。

**boolean：**

- boolean数据类型表示一位的信息；
- 只有两个取值：true 和 false；
- 这种类型只作为一种标志来记录 true/false 情况；
- 默认值是 **false**；
- 例子：boolean one = true。

**char：**

- char 类型是一个单一的 16 位 Unicode 字符；

- 最小值是 **\u0000**（十进制等效值为 0）；

- 最大值是 **\uffff**（即为 65535）；

- char 数据类型可以储存任何字符；

- 例子：char letter = 'A';。

  

  ### 类型默认值

| **数据类型**           | **默认值** |
| :--------------------- | :--------- |
| byte                   | 0          |
| short                  | 0          |
| int                    | 0          |
| long                   | 0L         |
| float                  | 0.0f       |
| double                 | 0.0d       |
| char                   | 'u0000'    |
| String (or any object) | null       |
| boolean                | false      |



### **引用数据类型/对象数据类型**

- 在Java中，引用类型的变量非常类似于C/C++的指针。引用类型指向一个对象，指向对象的变量是引用变量。这些变量在声明时被指定为一个特定的类型，比如 Employee、Puppy 等。变量一旦声明后，类型就不能被改变了。

- 对象、数组都是引用数据类型。

- 所有引用类型的默认值都是null。

- 一个引用变量可以用来引用任何与之兼容的类型。

  

#### **对象（Object）**

**任何继承自 `Object` 类的类型。**



#### String

1. **不可变性（Immutability）**:
   - `String` 对象一旦创建，其值就不能更改。任何对字符串的修改实际上都会创建一个新的 `String` 对象。
   - 这种不可变性使得 `String` 在多线程环境中安全使用，因为它们不会被并发修改。
2. **字符串常量池（String Pool）**:
   - 为了提高效率和节省内存，Java 虚拟机（JVM）维护一个特殊的内存区域，称为字符串常量池。
   - 当创建字符串字面量（例如 `String s = "hello";`）时，JVM 首先检查字符串常量池中是否已存在相同内容的字符串。如果存在，就重用该对象；如果不存在，才创建一个新对象。
3. **创建字符串**:
   - 字符串可以通过字面量方式创建（如 `String s = "hello";`）或者使用 `new` 关键字（如 `String s = new String("hello");`）。
4. **常用方法**:
   - `String` 类提供了多种方法用于字符串处理，如 `length()`（返回字符串长度）、`charAt(int index)`（返回指定索引处的字符）、`substring(int beginIndex, int endIndex)`（返回子字符串）、`equals(Object another)`（比较字符串内容）等。
5. **字符串连接**:
   - 可以使用 `+` 运算符或 `concat()` 方法来连接字符串。例如，`"Hello, " + "world!"` 结果是 `"Hello, world!"`。
6. **字符串转换**:
   - `String` 类提供了方法将其他类型的数据转换为字符串，例如使用 `valueOf()` 方法。
7. **字符串比较**:
   - 使用 `equals()` 方法来比较字符串的内容是否相等，而不是使用 `==` 运算符。`==` 运算符比较的是对象引用，而不是内容。
8. **不变类的好处**:
   - 不可变性简化了编程，使得 `String` 对象易于传递、比较和缓存，同时也有助于提高应用程序的安全性。



#### **数组（Array）**

一个**存储同类型数据的连续空间**。

- **固定大小**：数组的大小在初始化时被确定，之后不能更改。

- **类型严格**：数组可以**持有原始数据类型**（如 `int[]`, `double[]`）或对象（如 `String[]`），但创建后，类型就固定了。

- **性能高**：由于**大小固定**和直接索引访问，数组在性能上有优势。

- **多维数组**：Java支持多维数组。

- **语法**：使用方括号定义和访问数组，例如 `int[] array = new int[10];`，`int firstItem = array[0];`。

  

#### **ArrayList（动态数组）**

- **动态大小**：`ArrayList`是一个**实现了 `List` 接口的动态数组类，可以在运行时调整大小。**`ArrayList` 是一个可以动态增长和缩减的索引序列，它内部使用数组来存储元素。

- **仅对象类型**：`ArrayList`只能持有对象类型（如 `Integer`, `String`），**不能持有原始数据类型。**

- **性能较低**：由于需要动态扩容和数据移动，`ArrayList`在某些操作上比数组慢。

- **泛型支持**：可以定义持有特定类型对象的 `ArrayList`，如 `ArrayList<String>`。

- **数组扩容**：当添加元素超出当前数组容量时，**`ArrayList` 会创建一个新的更大的数组，并将旧数组的内容复制到新数组中。**

  



#### **LinkedList**

`LinkedList` 在 Java 中是一个**双向链表**的实现，它实现了 **`List` 接口和 `Deque` 接口**，这意味着它既可以作为列表也可以作为双端队列使用。

**数据结构**

- **双向链表**：`LinkedList` 的每个元素（节点）都包含了**对前一个和后一个元素的引用**，这允许双向遍历。
- **节点**：链表中的数据被存储在“节点”中，节点封装了元素值以及前后节点的链接。

**性能特点**

- **动态大小**：与数组不同，`LinkedList` 的大小是动态的，它可以根据需要增长或缩减。

- **元素访问**：访问链表中的元素是线性时间复杂度，因为要从头（或尾）开始遍历列表直到找到目标位置。

- **插入和删除**：在链表中添加或删除元素是非常快的（理论上是常数时间O(1)），因为这些操作只涉及改变节点的链接，而不需要像数组那样移动其他元素。

  

#### **HashMap**

`HashMap` 存储**键值对（key-value pairs）**，**允许使用键（key）来快速检索值（value）**。它使用**哈希表（hash table）**来存储这些键值对，因此提供了常数时间的复杂度（O(1)）来插入和查找元素，前提是哈希函数将元素均匀地分布在桶中。

下面是一个简单的`HashMap`例子：

```java
import java.util.HashMap;
import java.util.Map;

public class Example {
    public static void main(String[] args) {
        Map<String, Integer> ageMap = new HashMap<>();
        ageMap.put("Alice", 25);
        ageMap.put("Bob", 30);
        ageMap.put("Charlie", 35);

        // 通过键检索值
        Integer age = ageMap.get("Alice");
        System.out.println("Alice's age: " + age); // 输出 "Alice's age: 25"
    }
}
```

在这个例子中，`ageMap` 是一个引用变量，它指向 `HashMap` 实例。在Java中，除了原始数据类型（如 `int`, `char`, `double` 等）之外，所有的类和数组都是引用类型，包括`HashMap`。当你创建一个`HashMap`对象时，你实际上是在堆上创建了一个对象，并且`ageMap`变量保存了指向那个对象的引用。



在 Java 的 `HashMap` 中，数据是以键值对的形式存储的。以下是其实现的主要特点：

- **散列和桶**：每个键通过散列函数转换成一个散列码（hash code），该散列码决定了键值对存储的桶（bucket）位置。桶通常是数组的索引。

- **碰撞处理**：如果两个不同的键产生了相同的散列码，会发生碰撞。`HashMap` 使用链表或红黑树来处理碰撞，也就是说，相同桶内的元素会形成一个链表或树结构。当链表长度超过一定阈值时，链表会转换成红黑树，以改善搜索性能。

- **动态重哈希**：当`HashMap`中的元素数量达到一定比例时（即装载因子阈值），`HashMap` 会动态地重新分配内存空间，进行扩容和重哈希以保持操作的效率。

  

#### **枚举（Enum）**

一种特殊的类，它可以有**一组预定义的常量。**(类似python中生成器)

**生活中的枚举**
「枚举」语义上表示「有限个」「离散的」「可以罗列」的值，在生活中表示「有限个」「离散的」「可以罗列」的例子有很多，例如：

性别：男、女；
一年四季：春、夏、秋、冬；
一年有 12 个月：1 月、2 月、3 月、4 月、5 月、6 月、7 月、8 月、9 月、10 月、11 月、12 月；
一周有 7 天：星期一、星期二、星期三、星期四、星期五、星期六、星期天；
交通工具：自行车、骑车、公交、地铁、轮船、飞机（可能还有，但是数量有限，它们就可以使用枚举类来表示）；
「力扣」的问题等级：简单、中等、困难；
「力扣」一次提交的结果：通过、超时、超出内存、编译不能通过、错误答案；
一个 Web 后台系统自定义的状态码：有限个，可以罗列的，正确的状态码一般用 200，重定向码 3xx（以 3 开头）、客户端错误状态码 4xx（以 4 开头）、 服务端错误状态码 5xx（以 5 开头）。



**Java 中已经有的枚举类**

其实在 Java 中，有很多状态是使用枚举来定义的，例如：

线程的状态。在 Java 的标准库中表现为 java.lang.Thread 内部的枚举类：

State：NEW、RUNNABLE、BLOCKED、WAITING、TIMED_WAITING、TERMINATED；

Spring 框架支持标准的数据库事务隔离级别，体现在类 org.springframework.transaction.annotation.Isolation：

**DEFAULT**、**READ_UNCOMMITTED**、**READ_COMMITTED**、**REPEATABLE_READ**、**SERIALIZABLE**。



**没有枚举类的时候我们怎么做**

如果没有枚举类，我们这样表示「有限」「可以罗列」。众所周知，「力扣」目前对问题难度的等级划分有 「简单」「中等」「困难」，如果没有枚举类，我们可以使用 0、1、2 来表示这三个等级。


   ```java
   public class LeetCodeProblemLevel {
       public static final int EASY = 0;
   
   	public static final int MEDIUM = 1;
   
   	public static final int HARD = 2;
    }
   ```


   问题是：如果我们需要把「力扣问题的难度等级」作为参数传递给某个方法的参数，该方法可以接受任意值的整数，例如传入 4 都是可以的。

   ```java
   public class Solution {
       public void dealWithLevel(int leetCodeProblemLevel) {
           // 需要校验 leetCodeProblemLevel 的值只能为 0、1、2
       }
   }
   ```


   如果我们需要记录日志、进行打印，程序输出的还是整数值：

   ```java
   public static void main(String[] args) {
       // 0
       System.out.println(LeetCodeProblemLevel.EASY);
   
       // 1
       System.out.println(LeetCodeProblemLevel.MEDIUM);
   
       // 2
       System.out.println(LeetCodeProblemLevel.HARD);
   }
   ```

   所以上面的代码实际上还是 Java 规定的类型：整型。可以将它们参与「加」「减」「乘」「除」运算，虽然没有人会这么做。这种做法相当于只是给 0、1、2 起了一个别名。

   Java 的设计者们设计了枚举类，来表示有限、离散这样的概念，并且枚举类是一个自定义的类型。可以自定义类型，就可以让编译器帮助我们进行类型检查（表现为：如果在 IDE 中类型不匹配，编译就不能通过）。

   

   **枚举是只有有限个对象的自定义类型**
   可以使用关键字 enum 定义枚举类，枚举类的命名规则和类的命名规则是一样的，枚举类编译以后是 .class 文件。在以前没有枚举的时候，我们一般使用常量来表示枚举。枚举对象的命名，一般也使用常量的命名方式：全用大写字母。

   ```java
   public enum LeetCodeProblemLevel {
       // EASY、MEDIUM、HARD 分别表示 3 个唯一的对象，使用英文逗号隔开，最后使用英文分号
       EASY, MEDIUM, HARD;
   }
   ```

   **说明：**

   使用 enum 代替 class 关键字，表示这是一个枚举类。事实上「枚举类」设计出来就是为了 表示一个特别的类型，这个类型里只有有限个对象，因此如果我们在同一个包下创建一个名为 LeetCodeProblemLevel 的 Java 类是不被允许的；

   这个类里只有三个对象，这三个对象分别是 EASY 、MEDIUM、HARD 。可以认为 LeetCodeProblemLevel 这个类只需要创建三个对象，这三个对象分别使用 EASY 、MEDIUM、HARD 表示。
   此时打印枚举，输出的就是我们写在枚举类里的大写字母：

   ```java
   public static void main(String[] args) {
       // EASY
       System.out.println(LeetCodeProblemLevel.EASY);
       // MEDIUM
       System.out.println(LeetCodeProblemLevel.MEDIUM);
       // HARD
       System.out.println(LeetCodeProblemLevel.HARD);
   }
   ```


   枚举类在编译后会生成一个继承自 java.lang.Enum 的子类，这个子类会为每个枚举常量创建一个静态实例，并放入一个静态数组中。即所有的枚举类默认继承了 java.base 模块下的 java.lang.Enum 。

   

   大家可以点开源码看一下：

   ```java
   public abstract class Enum<E extends Enum<E>>
       implements Constable, Comparable<E>, Serializable {
       /**
        * The name of this enum constant, as declared in the enum declaration.
        * Most programmers should use the {@link #toString} method rather than
        * accessing this field.
        */
       private final String name;
       // 省略
   
       public String toString() {
           return name;
       }
    
   // 省略
   
   }
   ```

   这里的 name 就是我们定义的 enum 类里的大写字母，**toString() 直接返回了 name。**

   

   **枚举类表示了唯一性**

   枚举类被设计出来，是为了表示某个系统里的 唯一性。例如我们说到春季，大家的意识里只会有一个春暖花开的春季。在没有枚举类的时候，要保证唯一性，需要严格编码与测试。而枚举类重写了 equals() 和 hashCode() 方法，以及实现了 Serializable 接口，保证了枚举对象的唯一性和序列化一致性。

   

   **设计枚举类的好处**

   **有了枚举类：**

   编辑器会帮助我们进行参数类型检查，在编译期就会检查代码是否正确；
   有了更明确的语义，记录日志、打印枚举值输出的时候就容易被人们理解。

   **总结**

   枚举类反映了现实生活中一个事物只有 **有限个** 状态；
   枚举类可以让编译器帮助我们执行 **类型检查**，避免传递**错误的参数值**；
   每一个枚举类里面第一行用大写字母表示的就是枚举类里的有限个对象。



```java
public enum LeetCodeProblemLevel {

    EASY("简单", "不需要专门学习算法，或者刚开始学习就可以解决的问题"), MEDIUM("中等", "常规问题，考查了常见的数据结构，题型相对单一"), HARD("困难", "需要一些技巧，如果缺少训练，以前没有做过，不容易做出来");

    private String name;

    private String description;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    LeetCodeProblemLevel(String name, String description) {
        this.name = name;
        this.description = description;
    }

}
```

**说明：**

EASY("简单", "不需要专门学习算法，或者刚开始学习就可以解决的问题"), MEDIUM("中等", "常规问题，考查了常见的数据结构，题型相对单一"), HARD("困难", "需要一些技巧，如果缺少训练，以前没有做过，不容易做出来"); 这一行表示了这个枚举类只有 3 个对象，这 3 个对象分别用 EASY、MEDIUM 和 HARD 来表示；

这里 name 和 description 就是我们上面说的对于枚举类的**唯一对象的附加信息**，所以我们需要在枚举类的对象后面使用 (属性值 1, 属性值 2,...) 这样的方式给属性**赋值**，这其实就是在调用构造函数，通过构造函数给每一个对象的成员变量赋值；



#### **字符串（String）**

虽然 `String` 类型在 Java 中实际上是一个对象，但由于其在 Java 中的特殊地位和常用性，有时它被视为一个单独的数据类型。



#### **接口（Interface）**

一种**定义方法但不实现的类型。**

当然，让我们详细了解一下每个Java集合接口的特性及其常见的实现类和它们的数据结构：

**0. Collection接口**

这是最基本的集合接口**，它是List、Set和Queue接口的父接口**。它定义了所有集合共有的方法，如添加、删除、清空集合等。



**1. List接口**

它表示一个**有序的集合**，可以包含**重复的元素**。它提供了一种**通过索引访问集合元素的方法**，常用的实现类有ArrayList、LinkedList等。

- **ArrayList**：基于动态数组的实现，提供快速的随机访问和高效的遍历。但是，插入和删除元素（尤其是列表的开头）时效率较低，因为可能涉及移动元素。

- **LinkedList**：基于双向链表的实现，优化了在列表的开头和中间的插入和删除操作，但随机访问元素相比于ArrayList较慢。

  

**2. Set接口**

它代表一个**不包含重复元素的集合**。它**不保证集合的迭代顺序**；特别是某些实现（如HashSet）不对迭代顺序做任何保证。常见的实现类有HashSet、LinkedHashSet和TreeSet。

- **HashSet**：基于哈希表实现，提供了快速的插入、删除和查找操作。它不保证元素的顺序。

- **LinkedHashSet**：类似于HashSet，但它使用链表维护元素的插入顺序，因此迭代访问Set时可以预期的顺序。

- **TreeSet**：基于红黑树的实现，元素会按照自然排序或指定的Comparator排序。提供有序的集合操作，但是增删查的操作效率低于HashSet。

  

**3. Queue接口**

它代表了**先进先出（FIFO）的队列**。Queue接口的常见实现有LinkedList和PriorityQueue。

- **LinkedList**：既实现了List接口，也实现了Queue接口，可以作为队列使用。

- **PriorityQueue**：基于优先级堆（通常是二叉堆）的实现，元素会根据其自然顺序或者构造时传入的Comparator来进行排序。

  

**4. Deque接口**

它是Queue的一个子接口，代表**双端队列**，**允许元素从两端插入和移除**。实现这个接口的类可以被用作队列、栈或双端队列。LinkedList和ArrayDeque是Deque接口的两个常见实现。

- **ArrayDeque**：基于可变大小的数组实现的双端队列，没有容量限制。它比Stack和LinkedList（当作栈使用时）更高效。
- **LinkedList**：同样实现了Deque接口，因此也可以作为一个双端队列使用。



**5. Map接口**

在 Java 中，`Map` 是一个接口，它是集合框架的一部分，**用于存储键值对（key-value pairs）**。`Map` 接口和其实现类提供了一种有效的方式来存储和操作键值对。以下是关于 `Map` 的一些关键特点：

1. **键值对存储**:

   - 在 `Map` 中，每个键都映射到一个值。**键不能重复，每个键只能映射到一个值。**

2. **无序集合**:

   - 一般情况下，**`Map` 中的元素不保证有特定的顺序**。不过，某些 `Map` 实现（如 `LinkedHashMap`）**可以保持元素的插入顺序或访问顺序。**

3. **键的唯一性**:

   - **`Map` 的每个键都是唯一的。如果试图插入一个已存在键的新值，该键的原值将被替换。**

4. **常用实现:**

   - `HashMap`：基于哈希表的 `Map` 实现，提供了最佳的一般性能。
   - `TreeMap`：基于红黑树的 `Map` 实现，其元素按照键的自然顺序或比较器排序。
   - `LinkedHashMap`：类似于 `HashMap`，但它维护着元素的插入顺序或访问顺序。
   - `Hashtable`：和 `HashMap` 类似，但它是同步的。由于 `Collections.synchronizedMap` 和 `ConcurrentHashMap` 的出现，它的使用已经减少。

5. **主要方法**:

   - `put(K key, V value)`：向 `Map` 中添加键值对。
   - `get(Object key)`：根据键获取值。
   - `remove(Object key)`：根据键移除键值对。
   - `containsKey(Object key)`：检查 `Map` 是否包含指定的键。
   - `containsValue(Object value)`：检查 `Map` 是否包含一个或多个键映射到指定值。
   - `size()`：返回 `Map` 中的键值对数量。
   - `isEmpty()`：检查 `Map` 是否为空。
   - `clear()`：清空 `Map`。

6. **泛型**:

   - `Map` 接口支持泛型，例如 `Map<String, Integer>`，其中 `String` 是键的类型，`Integer` 是值的类型。

     

**6. SortedSet接口**

它扩展了**Set接口**，保证集合中的**元素处于排序状态**。SortedSet的一个常见实现是TreeSet。

- **TreeSet**：如前所述，**TreeSet实现了SortedSet接口，使用红黑树结构，保证了元素的排序和唯一性。**



**7. SortedMap接口**

它**扩展了Map接口**，确保键处于**排序状态**。它的一个常见实现是TreeMap。

- **TreeMap**：作为SortedMap的唯一实现（标准Java库中），使用红黑树保证键的排序。



**8. NavigableSet和NavigableMap接口**

- **TreeSet**和**TreeMap**：这两个集合类除了实现了SortedSet和SortedMap接口外，还实现了NavigableSet和NavigableMap接口，提供了额外的导航方法，比如`lower`、`floor`、`ceiling`、`higher`，以便更精确地控制元素的排序。



### 自动类型转换

**整型、实型（常量）、字符型数据可以混合运算。运算中，不同类型的数据先转化为同一类型，然后进行运算。**

转换从低级到高级。

```
低  ------------------------------------>  高

byte,short,char—> int —> long—> float —> double 
```

数据类型转换必须满足如下规则：

- 1. 不能对boolean类型进行类型转换。

- \2. 不能把对象类型转换成不相关类的对象。

- \3. 在把容量大的类型转换为容量小的类型时必须使用强制类型转换。

- \4. 转换过程中可能导致溢出或损失精度，例如：

  ```
  int i =128;   
  byte b = (byte)i;
  ```

  因为 byte 类型是 8 位，最大值为127，所以当 int 强制转换为 byte 类型时，值 128 时候就会导致溢出。

- \5. 浮点数到整数的转换是通过舍弃小数得到，而不是四舍五入，例如：

  ```
  (int)23.7 == 23;        
  (int)-45.89f == -45
  ```



**自动类型转换**

必须满足转换前的数据类型的**位数要低于转换后的数据类型**，例如: short数据类型的位数为16位，就可以自动转换位数为32的int类型，同样float数据类型的位数为32，可以自动转换为64位的double类型。

**实例**

```java
public class ZiDongLeiZhuan{
        public static void main(String[] args){
            char c1='a';//定义一个char类型
            int i1 = c1;//char自动类型转换为int
            System.out.println("char自动类型转换为int后的值等于"+i1);
            char c2 = 'A';//定义一个char类型
            int i2 = c2+1;//char 类型和 int 类型计算
            System.out.println("char类型和int计算后的值等于"+i2);
        }
}
```

运行结果为:

```
char自动类型转换为int后的值等于97
char类型和int计算后的值等于66
```



**解析：**c1 的值为字符 **a** ,查 ASCII 码表可知对应的 int 类型值为 97， A 对应值为 65，所以 **i2=65+1=66**。



**强制类型转换**

- 1. 条件是转换的数据类型必须是兼容的。

- 2. 格式：(type)value type是要强制类型转换后的数据类型 实例：

  **实例**

  ```java
  public class QiangZhiZhuanHuan{
      public static void main(String[] args){
          int i1 = 123;
          byte b = (byte)i1;//强制类型转换为byte
          System.out.println("int强制类型转换为byte后的值等于"+b);
      }
  }
  ```

  运行结果：

  ```
  int强制类型转换为byte后的值等于123
  ```





### 泛型（Generics）

![image-20230130152512916](https://pic.leetcode.cn/1679896545-DJQgEA-image.png)

泛型（Generics）是Java语言中的一个特性，**它允许在编译时提供类型检查和消除类型转换。**在不使用泛型的代码中，**具体的类型信息通常不在编译时期可用，而是在运行时处理，这可能导致类型转换错误**。泛型的引入是为了解决这个问题，增强程序的类型安全性和可读性。

泛型的核心概念包括：

1. **类型参数化**：通过类型参数化，你可以编写一个能适应任何类型的类、接口或方法。类型参数只在编译时有效，编译器用具体的类型替换类型参数，并执行类型检查。

2. **类型安全**：泛型提供编译时类型安全检查，这意味着你在编译时就会被告知是否正确地使用了类型，而不是等到运行时才抛出`ClassCastException`。

3. **类型擦除**：Java泛型的一个重要特性是类型擦除。这意味着泛型类型参数在编译后的字节码中会被擦除（或替换），这样程序就像没有使用泛型一样。在运行时，所有泛型类实例都属于同一原始类型。

4. **泛型类**：是指定义了一个或多个类型变量的类。例如，`ArrayList<E>` 中的 `E` 就是一个类型变量，它代表了存储在列表中的元素类型。

5. **泛型接口**：如同泛型类，泛型接口也是定义了一个或多个类型变量的接口。

6. **泛型方法**：方法可以定义自己的类型参数，这些参数在方法调用时指定具体的类型。这允许该方法在不同类型上操作，同时保持类型安全。

7. **限定的类型参数**：可以限制类型参数必须继承自特定类，或者实现特定接口。

泛型的一个常见用例是在集合类中，例如 `List`、`Map`、`Set` 等，它们都使用泛型来指定集合元素的类型。这样就不需要将集合中的元素从 `Object` 类型转换为具体的类型。

下面是泛型的一个简单示例：

```java
// 泛型类示例
public class Box<T> {
    private T t; // T是该类的类型参数

    public void set(T t) {
        this.t = t;
    }

    public T get() {
        return t;
    }
}

// 泛型接口示例
public interface List<E> {
    void add(E x);
    Iterator<E> iterator();
}

// 泛型方法示例
public static <U> void printArray(U[] array) {
    for (U element : array) {
        System.out.print(element + " ");
    }
    System.out.println();
}

// 使用泛型类
Box<Integer> integerBox = new Box<Integer>();
integerBox.set(10);
Integer someInteger = integerBox.get();

// 使用泛型方法
String[] strings = { "Hello", "World" };
printArray(strings); // 显示调用泛型方法
```





### 静态（Static）特性

1. **静态类型（Static Typing）**: Java是一种静态类型语言，这意味着所有变量的类型必须在编译时就已确定。编译器会对类型进行检查，以确保例如不会将字符串赋给整型变量等类型错误。这些类型信息在编译时确定并在运行时保持不变。

2. **静态变量（Static Variables）**: 如前所述，用 `static` 关键字声明的变量属于类，而不是类的实例。这种变量在类加载时创建，在程序结束时销毁。

3. **静态方法（Static Methods）**: 类似地，**`static` 方法属于类本身而不是对象实例。它们可以在不创建类实例的情况下调用。**

4. **静态绑定（Static Binding）**: 当一个方法或属性在编译时就被绑定到一个特定的类或对象上，这称为静态绑定（或早期绑定）。Java中的静态方法和属性（通过类名来访问的）都是静态绑定的。

   

### 动态（Dynamic）特性

1. **动态类型（Dynamic Typing）**: 尽管Java本身不是动态类型语言，但Java的某些特性具有动态性，如反射（Reflection），可以在运行时动态地检查和调用对象的属性和方法。

2. **动态绑定（Dynamic Binding）**: 在Java中，方法的调用通常是动态绑定的，这意味着在编译时并不确定程序将调用哪个具体的方法。**具体调用哪个方法是在运行时决定的，这依赖于对象的实际类型。例如，通过多态，一个父类引用可以指向子类对象，而调用的方法则是子类的方法。**

3. **动态内存分配（Dynamic Memory Allocation）**: **Java中的对象是在运行时动态创建的**，并在**堆内存上分配空间**。与静态分配（如数组的大小，在编译时必须已知）相比，动态内存分配允许程序在运行时根据需要创建任意数量的对象。

   

### 数据类型与静态/动态的关系

- **基本数据类型**（如 `int`, `double`, `boolean`）在Java中是**静态类型的**，因为它们在编译时就必须声明，而且它们的**大小和结构在编译时就已确定。**

- **对象数据类型**（或引用类型）如类实例，则是**动态创建的**，因为它们是在运行时实例化的，它们的行为（哪个方法被调用）可能具有动态绑定的特性。

  

## Java 对象和类

### 面向对象编程（OOP）的四大基本概念

**封装、继承、多态和抽象**

Java 是一种广泛使用的面向对象的编程语言，支持面向对象编程（OOP）的四大基本概念：封装、继承、多态和抽象。此外，它还涵盖了类、对象、实例、方法和重载等关键概念。我将依次详细解释每一个概念：

1. **多态（Polymorphism）**： 多态是面向对象编程中的一个核心概念，它指的是允许不同类的对象对同一消息做出响应的能力。在Java中，多态通常通过**重载（同一类中的方法名相同，但参数列表不同）**和**重写（子类重写继承自父类的方法）**来实现。

2. **继承（Inheritance）**： 继承是一种机制，其中一个新类继承另一个类的属性和方法。在Java中，继承使用 `extends` 关键字。它允许代码的重用，并建立一个类的层次结构。

3. **封装（Encapsulation）**： 封装是将数据（属性）和代码（方法）作为一个单一的单元或对象的过程。在Java中，通常通过将类的成员设为私有（private），然后提供公开（public）的方法来获取（getters）和设置（setters）这些属性的值来实现封装。

4. **抽象（Abstraction）**： 抽象是简化复杂现实世界的过程，通过创建简化的模型，只包含对当前问题域重要的信息。在Java中，抽象可以通过使用抽象类和接口来实现。抽象类不能被实例化，而是被其他类继承。接口则可以定义一组方法，但不提供它们的实现。

   

#### **多态**

多态（Polymorphism）是面向对象编程中的一个重要概念，**它允许你使用一个接口来表示多种数据类型**。在 Java 中，多态主要通过**接口、继承和方法重载来实现**。下面我会详细解释这个概念。

**主要类型：**

1. **编译时多态（静态多态）**：主要是通过**方法重载**实现的。
2. **运行时多态（动态多态）**：主要是通过**继承和接口**实现的。



**编译时多态**

**方法重载**是一种**编译时多态**。同一个类中可以有**多个同名但参数列表不同的方法。**

```java
public class Calculator {
    public int add(int a, int b) {
        return a + b;
    }

    public double add(double a, double b) {
        return a + b;
    }
}
```



**运行时多态**

1. **继承**：**子类继承父类**，子类对象可以赋**值给父类引用**。

   ```java
   class Animal {
       void makeSound() {
           System.out.println("Animal makes a sound");
       }
   }
   
   class Dog extends Animal {
       void makeSound() {
           System.out.println("Dog barks");
       }
   }
   
   Animal myAnimal = new Dog();  // Dog 对象存储在 Animal 类型的变量中
   myAnimal.makeSound();  // 输出 "Dog barks"
   ```

2. **接口**：一个类可以实现多个接口，接口的实例可以指向实现该接口的任何类的对象。

   ```java
   interface Drawable {
       void draw();
   }
   
   class Circle implements Drawable {
       public void draw() {
           System.out.println("Drawing a circle");
       }
   }
   
   Drawable d = new Circle();
   d.draw();
   ```

**优点：**

1. **代码可重用**：你可以编写能以多种方式工作的代码。
2. **可扩展性**：你可以添加新的类型，而不必修改现有的代码。
3. **维护性**：代码结构更清晰，更易于管理和维护。

**注意事项：**

1. 运行时多态在 Java 中是通过**虚拟方法表（Virtual Method Table**）来实现的，这会带来一定的性能开销。
2. 需要正确地使用方法覆盖（**Override**）和重载（**Overload**）。

多态是面向对象编程的**四大基本特性之一（封装、继承、多态和抽象）**。正确地使用多态可以使代码更灵活、可扩展和易于维护。



#### 继承

在 Java 中，继承是一种允许我们**重用代码和建立类之间关系的机制**。通过继承，一个类（称为子类或派生类）可以获得另一个类（称为父类或基类）的字段（变量）和方法。下面详细介绍 Java 中继承的各个方面。

**基础语法**

要创建一个子类，您可以使用 **`extends`** 关键字：

```java
public class Animal {
    public void makeSound() {
        System.out.println("Some generic animal sound");
    }
}

public class Dog extends Animal {
    // Dog 类继承了 Animal 类
}
```

在这个例子中，`Dog` 类继承了 `Animal` 类，因此 `Dog` 类具有 `Animal` 类的所有非私有属性和方法。您可以创建一个 `Dog` 对象并调用 `makeSound` 方法，即使 `Dog` 类自己并没有定义这个方法：

```
Dog myDog = new Dog();
myDog.makeSound();  // 输出 "Some generic animal sound"
```



**调用父类的方法和构造函数**

子类可以使用 `super` 关键字来调用父类的方法和构造函数。

```java
public class Dog extends Animal {
    @Override
    public void makeSound() {
        super.makeSound();
        System.out.println("Woof woof");
    }
}
```



**final 关键字**

如果一个类用 `final` 关键字标记，那么它**不能被继承。**

```java
public final class ImmutableClass {
    // 代码
}
```

同样地，`final` 方法不能在子类中被覆盖。



**Object 类**

在 Java 中，所有类都是 `Object` 类的子类（直接或间接）。这意味着每个 Java 对象都有 `Object` 类的方法，如 `toString()`, `equals()`, `hashCode()` 等。



**抽象类和接口**

- **抽象类**: 定义了一些方法但没有完全实现的类。这些类通常包含抽象方法（没有实现的方法），子类必须提供实现。

- **接口**: 是一种完全抽象的类，它只定义（而不实现）方法。Java 支持多接口继承。

  

##### 覆盖（Override）和重载（Overload）

`覆盖（Override）` 和 `重载（Overload）` 是 Java 中两个非常重要的概念，它们在形式和目的上有明显的不同。下面详细解释它们之间的主要区别。

- **覆盖（Override）**

1. **定义**: 子类提供了一个**与父类方法签名（方法名和参数类型）完全相同的方法。**

2. **目的**: 为了**改变继承自父类的同名方法的行为。**

3. **修饰符**: 必须与父类方法的修饰符相同或更为宽松。例如，如果父类方法是 `protected`，则子类覆盖的方法可以是 `protected` 或 `public`。

4. **返回类型**: 必须与父类方法的返回类型相同或是其子类型。

5. **抛出异常**: 子类覆盖的方法所抛出的异常应该是被父类抛出异常的子集。

6. **运行时行为**: Java 使用**运行时多态性**来选择要执行的方法版本，即它执行的是对象实际类的方法版本。

   ```java
   class Animal {
       void makeSound() {
           System.out.println("Animal sound");
       }
   }
   
   class Dog extends Animal {
       @Override  // 这个注解是可选的，但有助于编译器检查
       void makeSound() {
           System.out.println("Dog barks");
       }
   }
   ```



- **重载（Overload）**

1. **定义**: **在同一个类中定义一个与已有方法名相同但参数列表不同的方法。**

2. **目的**: 让同一个方法可以有不同类型或数量的参数。

3. **修饰符**: 可以与已有的重载方法有不同的访问修饰符。

4. **返回类型**: 可以与已有的重载方法有不同的返回类型。

5. **抛出异常**: 可以与已有的重载方法有不同的异常抛出列表。

6. **编译时行为**: Java 使用**编译时多态性**来解析应该调用。

   ```java
   public class Calculator {
       public int add(int a, int b) {
           return a + b;
       }
   
       public double add(double a, double b) {
           return a + b;
       }
   }
   ```



**主要区别总结**

|                 | 覆盖（Override）           | 重载（Overload）         |
| --------------- | -------------------------- | ------------------------ |
| 方法签名        | 必须与父类相同             | 必须与同类中其他方法不同 |
| 返回类型        | 与父类相同或是其子类型     | 可以不同                 |
| 修饰符          | 不能比父类更严格           | 可以不同                 |
| 所在类          | 子类                       | 同一个类                 |
| 抛出的异常      | 只能是父类异常的子集或相同 | 可以不同                 |
| 运行/编译时行为 | 运行时多态                 | 编译时多态               |

这两个概念在 Java 中是非常基础和重要的，正确理解和使用它们可以使代码更为灵活和可维护。



**Example**

```java
public class Inherit {

    abstract class Speaker {
        abstract public void speak();
    }

    class Cat extends Speaker {
        public void speak() {
            System.out.printf("Woof!");
        }
    }

    class Dog extends Speaker {
        public void speak() {
            System.out.printf("Meow!");
        }
    }

    Inherit() {
        Speaker d = new Dog();
        Speaker c = new Cat();
        d.speak();
        c.speak();
    }

    public static void main(String[] args) {
        new Inherit();
    }
}

```

在这段代码中，我们有一个抽象类 `Speaker` 和两个继承自 `Speaker` 的子类 `Cat` 和 `Dog`。每个子类都提供了 `speak` 方法的具体实现。`Cat` 类的 `speak` 方法打印 `"Woof!"`，而 `Dog` 类的 `speak` 方法打印 `"Meow!"`。

在 `Inherit` 类的构造函数中，我们创建了一个 `Dog` 类型的对象 `d` 和一个 `Cat` 类型的对象 `c`，并调用了它们的 `speak` 方法。尽管它们被声明为 `Speaker` 类型的引用，但由于Java中的动态绑定，调用的将是实际对象类型的 `speak` 方法。

因此，以下输出将被产生：

```
Meow!Woof!
```

这里 `Dog` 类的实例 `d` 先调用了 `speak` 方法，打印了 `"Meow!"`，然后 `Cat` 类的实例 `c` 调用了 `speak` 方法，打印了 `"Woof!"`。



#### **封装（Encapsulation）**

封装是将数据（属性）和代码（方法）作为一个单一的单元或对象的过程。在Java中，通常通过将类的成员设为私有（private），然后提供公开（public）的方法来获取（getters）和设置（setters）这些属性的值来实现封装。



#### **抽象（Abstraction）**

抽象是简化复杂现实世界的过程，通过创建简化的模型，只包含对当前问题域重要的信息。在Java中，抽象可以通过使用抽象类和接口来实现。抽象类不能被实例化，而是被其他类继承。接口则可以定义一组方法，但不提供它们的实现。



### 类（Class）

在Java中，类（Class）是一种用户定义的蓝图或原型，从中创建对象。类表示在创建对象时封装数据的属性和行为的方法的组合。每个对象都是其父类的实例，具有该类定义的状态（属性）和行为（方法）。

- ### 类的基本概念


- **属性（Fields or Members）**: 类中的属性是用来存储对象的状态信息的变量。属性可以有各种数据类型，如int, String等。
- **方法（Methods）**: 方法定义了类的行为。它们是在类的上下文中执行的函数，可以修改类的内部状态或执行操作。
- **构造函数（Constructors）**: 构造函数是一种特殊类型的方法，用于初始化新创建的对象。它可以设置对象的初始状态。
- **封装（Encapsulation）**: Java通过将属性和实现细节隐藏在类内部，并**通过公共方法（getter和setter）提供属性的访问**，从而实现封装。
- **继承（Inheritance）**: Java支持基于类的**继承**，允许一个类继承另一个类的属性和方法，从而实现代码重用。
- **多态性（Polymorphism）**: Java通过方法**重载和重写支持多态性**，允许使用统一接口访问不同的底层形式（例如，同一个方法名称可以用于不同类型的对象调用不同的方法）。



Java 语言支持的**变量类型**有：

- **局部变量（Local Variables）：**定义在方法、构造方法或语句块中的变量，作用域只限于**当前方法**、构造方法或语句块中。局部变量必须在使用前声明，并且不能被访问修饰符修饰。

- **成员变量（Instance Variables）：**定义在**类中、方法之外的变量**，作用域为整个类，可以被类中的任何方法、构造方法和语句块访问。成员变量可以被访问修饰符修饰。

- **静态变量（Class Variables）：**定义在类中、方法之外的变量，并且使用 **`static` 关键字修饰**，作用域为整个类，可以被类中的任何方法、构造方法和语句块访问，静态变量的值在程序运行期间只有一个副本。静态变量可以被访问修饰符修饰。

- **参数变量（Parameters）：**方法定义时声明的变量，作为**调用该方法时传递给方法的值**。**参数变量的作用域只限于方法内部**。

  

- ### 类的声明


下面是一个简单的Java类声明的例子：

```java
public class Animal {
    // 属性（成员变量）
    String name;
    
    // 构造函数
    public Animal(String name) {
        this.name = name;
    }
    
    // 方法
    public void eat() {
        System.out.println(name + " is eating.");
    }
}
```

在这个例子中，`Animal` 类有一个属性 `name` 和一个方法 `eat()`。还有一个构造函数，用于创建 `Animal` 对象的实例。



- ### 创建对象


你可以使用 `new` 关键字和构造函数创建类的实例：

```java
Animal myDog = new Animal("Rover");
```

这行代码创建了一个 `Animal` 类型的对象，并将其赋值给变量 `myDog`。



- **声明**：声明一个对象，包括对象名称和对象类型。
- **实例化**：使用关键字 new 来创建一个对象。
- **初始化**：使用 new 创建对象时，会调用构造方法初始化对象。



- #### 访问实例变量和方法

通过已创建的对象来访问成员变量和成员方法，如下所示：

```java
/* 实例化对象 */
Object referenceVariable = new Constructor();
/* 访问类中的变量 */
referenceVariable.variableName;
/* 访问类中的方法 */
referenceVariable.methodName();
```



- ### 类的访问级别


- **public**: 如果一个类被声明为public，那么这个类可以被任何其他类访问。
- **默认（无修饰符）**: 如果类没有修饰符（即默认访问级别），它只能被同一个包中的类访问。

类还可以包含静态（static）变量和方法，这些变量和方法属于类本身，而不是类的任何实例。

Java类是Java编程语言的核心，因为Java是一种面向对象的语言，所以几乎所有的功能都是通过类和对象来实现的。



#### This

在Java中，`this` 是一个引用变量，指向当前对象。这个关键字在几种不同的上下文中使用，但是它主要被用来：

1. **区分实例变量和参数**：当方法参数与类的实例变量同名时，可以使用 `this` 来解决命名冲突。
2. **在构造器中调用另一个构造器**：可以用 `this()` 调用同一个类中的另一个构造器。
3. **传递当前对象**：可以传递当前对象给方法或者构造器。
4. **返回当前类的实例**：可以从方法中返回当前类的实例。

下面是 `this` 关键字使用的示例：

```java
public class MyClass {
    private int value;

    public MyClass(int value) {
        // 使用 this 关键字区分实例变量和参数
        this.value = value;
    }

    public void setValue(int value) {
        // 再次使用 this 关键字区分实例变量和参数
        this.value = value;
    }

    public void print() {
        // 使用 this 传递当前对象
        printValue(this);
    }

    public void printValue(MyClass obj) {
        System.out.println(obj.value);
    }
}
```



## **Java的回收机制（Garbage Collection）**

- Java的**垃圾回收（Garbage Collection, GC）**是自动内存管理的一个过程。Java虚拟机（JVM）中的垃圾回收器负责查找并删除内存中不再使用的对象，以释放和重用资源。

  垃圾回收的基本原理是确定哪些内存是“可达”的，即哪些内存仍被程序中的引用变量所引用，哪些是“不可达”的。不可达的内存认为是垃圾，可以被回收。

  ### 垃圾回收机制主要步骤：

  1. **标记（Mark）**：
     - 这一步涉及到识别那些仍然被程序中的引用变量所引用的对象。任何无法到达的对象都被视为垃圾。
  2. **删除/回收（Sweep）**：
     - 这一步涉及到实际清理那些标记为垃圾的对象，并回收它们所占用的内存空间。

  ### 垃圾回收算法：

  1. **标记-清除（Mark and Sweep）**：
     - 最基本的收集算法，它分为“标记”和“清除”两个阶段：首先标记出所有活动的对象，然后清除所有未标记的对象。
  2. **复制（Copying）**：
     - 将存活的对象从当前内存区域复制到另一个，清除所有剩余的垃圾对象，这种方式适用于新生代（Young Generation）。
  3. **标记-整理（Mark and Compact）**：
     - 类似于标记-清除算法，但在清除结束后，它会移动所有存活的对象，将它们压缩到内存的一端，以解决内存碎片问题。
  4. **分代收集（Generational Collection）**：
     - **JVM的堆内存被分成新生代和老年代。大多数对象在新生代中创建并很快死去。分代收集算法根据对象的存活周期的不同，在不同的区域采用不同的垃圾收集策略，以提高垃圾收集的效率。**
  5. **增量收集（Incremental Collection）**：
     - 不是一次性回收所有的垃圾，而是分多次小步骤进行，减少程序的停顿时间。

  ### 垃圾回收器类型：

  - **串行回收器（Serial GC）**：
    - 对于单线程环境，适用于小型数据处理。
  - **并行回收器（Parallel GC）**：
    - 利用多个CPU核心同时进行垃圾回收，减少停顿时间，适用于多核服务器。
  - **并发标记清除（CMS GC）**：
    - 最小化程序停顿，适用于那些对响应时间有很高要求的应用。
  - **G1回收器（G1 GC）**：
    - 针对具有大内存空间的多处理器机器，以高概率满足垃圾收集的暂停时间目标（Pause Time Goal）。
  - **ZGC和Shenandoah GC**（较新）：
    - 目标是为了进一步减少暂停时间，并且适用于大堆内存。

  ### 重要概念：

  - **停顿时间（Pause Time）**：

    - 收集垃圾时程序的执行会被暂停，优化垃圾收集的一个关键点就是减少这种停顿。

  - **内存泄漏（Memory Leak）**：

    - 即使有自动垃圾回收，不当的编码实践仍然可能导致**内存泄漏**，这些通常是由于长生命周期对象持有短生命周期对象的引用造成的。

      

### 内存泄漏

**内存泄漏（Memory Leak）**是一个编程问题，出现在**一个程序分配了内存但未能释放，即使它不再使用这些内存。这会导致程序运行时占用越来越多的内存资源，可能最终导致系统资源枯竭**，程序崩溃或性能下降。以下是内存泄漏的一些主要特点和影响：

**主要特点：**

1. **持续增长**: 内存泄漏通常导致程序的内存使用持续增长。
2. **难以检测**: 尤其在大型、复杂的程序中，内存泄漏可能很难发现。
3. **长时间运行问题**: 在短时间内，内存泄漏可能不会立即导致问题，但在长时间运行的程序（如服务器）中，它们可以成为一个严重问题。

**影响：**

1. **性能下降**: 随着内存使用量的增加，操作系统可能需要使用虚拟内存（硬盘），从而导致性能下降。
2. **资源枯竭**: 在极端情况下，内存泄漏可能导致可用内存完全耗尽，从而导致其他程序或整个系统崩溃。
3. **系统不稳定**: 由于资源的不断耗尽，可能导致系统运行不稳定。

**如何检测：**

1. **手动检查代码**: 通过仔细阅读和理解代码来识别潜在的内存泄漏。
2. **静态代码分析**: 使用静态代码分析工具来识别常见的模式和潜在的内存泄漏。
3. **动态分析工具**: 如 Valgrind、Instruments 或专用的内存分析库。
4. **运行时监控**: 使用性能监控工具来观察程序的内存使用情况。

**如何解决：**

1. **垃圾回收**: 在支持自动垃圾回收的编程语言（如 Java, Python）中，内存泄漏通常较少出现，但仍然可能。
2. **手动内存管理**: 在需要手动管理内存的编程语言（如 C/C++）中，开发者需要更加谨慎地分配和释放内存。
3. **使用智能指针**: 在C++11及以后版本中，可以使用智能指针（如 `std::unique_ptr` 和 `std::shared_ptr`）来自动管理内存。
4. **代码重构**: 识别和修改导致内存泄漏的代码部分。



### 动态分配与静态分配

#### 动态分配

**动态分配（Dynamic Allocation）**是一种在程序运行时（而非编译时）分配内存空间的方法。这与静态分配相对，**静态分配是在程序编译时就确定了内存的大小。**动态分配的主要优点是它允许程序更灵活地使用内存，适应不同的数据规模和运行环境。

**为什么需要动态分配？**

在很多情况下，你可能无法预先知道需要多少内存。例如：

1. 当你从文件或网络中读取数据时，数据的大小可能是不确定的。
2. 当你实现数据结构（如链表、树、图等）时，元素的数量可能会动态变化。

在这些情况下，动态分配允许你根据需要分配或释放内存，使得内存使用更为高效。

**如何进行动态分配？**

不同的编程语言提供了不同的机制来进行动态内存分配。

1. C/C++: 使用 

   ```
   malloc()
   ```

   , 

   ```
   calloc()
   ```

   , 

   ```
   realloc()
   ```

    和 

   ```
   free()
   ```

    等函数进行内存的动态分配和释放。

   ```
   int *arr = (int*) malloc(10 * sizeof(int)); // 分配一个大小为 10 的整数数组
   free(arr); // 释放内存
   ```

2. Java: 使用 

   ```
   new
   ```

    关键字进行对象的动态分配。

   ```
   int[] arr = new int[10]; // 分配一个大小为 10 的整数数组
   ```

3. Python: 动态分配是自动进行的，你只需创建新的对象即可。

   ```
   arr = [None] * 10  # 分配一个大小为 10 的列表
   ```

4. JavaScript: 同样自动进行，通常通过字面量或构造函数来创建对象。

   ```
   const arr = new Array(10);  // 分配一个大小为 10 的数组
   ```

**内存管理和泄漏**

动态分配的内存必须谨慎管理。在一些低级语言（如 C/C++）中，你需要手动释放不再使用的内存，否则会导致内存泄漏。而在一些高级语言（如 Java、Python）中，垃圾回收机制会自动释放不再使用的内存。

#### 静态分配

静态分配是在编译时分配内存的一种方式。这意味着当程序被编译时，内存的大小和位置就已经确定了，无法在程序运行时改变。下面是几个静态分配的例子：

**C/C++ 中的静态数组**

```
int arr[10]; // 分配一个大小为 10 的整数数组，其大小在编译时确定。
```

**Java 中的基础数据类型**

```
int a; // 在栈上分配一个整数变量，大小和位置在编译时确定。
```

**Python 中的不可变数据类型**

虽然 Python 主要依赖动态分配，但不可变数据类型（如元组和字符串）一旦创建就不能更改，因此可以看作是静态分配的一种。

```
t = (1, 2, 3)  # 元组一旦创建，其大小和内容就不能更改。
```

**全局和静态变量**

**全局变量和静态变量**（在 C/C++ 中使用 **`static`** 关键字定义）也是静态分配的例子。它们在程序的生命周期内一直存在，不会被动态地创建或销毁。

```
static int x;  // 静态变量，其生命周期在整个程序执行期间。
```

**常量**

常量是在编译时就确定其值的变量，因此它们也是静态分配的。

```
final int MAX_VALUE = 100;  // 常量，其值在编译时就确定。
```

**结构体和类的静态成员（C++）**

在 C++ 中，类或结构体的静态成员变量也是静态分配的。

```
class MyClass {
public:
    static int staticVar;  // 静态成员变量，其生命周期在整个程序执行期间。
};
```



## Java多线程

在Java中，多线程主要可以通过以下几种方式实现：

**1. 继承 `Thread` 类**

你可以创建一个新类，继承自 `Thread` 类在Java中，**`this`** 是一个引用变量，指向当前对象。这个关键字在几种不同的上下文中使用，但是它主要被用来：

1. **区分实例变量和参数**：当方法参数与类的实例变量同名时，可以使用 `this` 来解决命名冲突。
2. **在构造器中调用另一个构造器**：可以用 `this()` 调用同一个类中的另一个构造器。
3. **传递当前对象**：可以传递当前对象给方法或者构造器。
4. **返回当前类的实例**：可以从方法中返回当前类的实例。



下面是 `this` 关键字使用的示例：

```java
public class MyClass {
    private int value;

    public MyClass(int value) {
        // 使用 this 关键字区分实例变量和参数
        this.value = value;
    }

    public void setValue(int value) {
        // 再次使用 this 关键字区分实例变量和参数
        this.value = value;
    }

    public void print() {
        // 使用 this 传递当前对象
        printValue(this);
    }

    public void printValue(MyClass obj) {
        System.out.println(obj.value);
    }
}
```

，并重写 `run()` 方法。然后通过创建该类的实例并调用其 `start()` 方法来创建并启动新线程。

```java
class MyThread extends Thread {
    public void run() {
        // 代码逻辑
    }
}

public class Main {
    public static void main(String[] args) {
        MyThread myThread = new MyThread();
        myThread.start();
    }
}
```



**2. 实现 `Runnable` 接口**

你也可以通过**实现 `Runnable` 接口来创建多线程**。这种方法更为灵活，因为Java**不支持多重继承**，所以实现接口是一种更好的选择。

```java
class MyRunnable implements Runnable {
    public void run() {
        // 代码逻辑
    }
}

public class Main {
    public static void main(String[] args) {
        Thread thread = new Thread(new MyRunnable());
        thread.start();
    }
}
```



**3. 使用 线程池`Executor` 框架**

Java还提供了线程池管理机制，可以通过 `Executors` 类和 `ExecutorService` 接口来创建线程池，以便更有效地管理线程资源。

```java
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Main {
    public static void main(String[] args) {
        ExecutorService executor = Executors.newFixedThreadPool(5);
        
        for (int i = 0; i < 10; i++) {
            Runnable worker = new MyRunnable();
            executor.execute(worker);
        }
        
        executor.shutdown(); // 终止线程池
    }
}
```

在上面的例子中，我们创建了一个固定大小为5的线程池，并提交了10个任务。线程池内部管理着线程的创建、执行和回收。



**4. 使用 `Callable` 和 `Future`**

如果你需要获取线程执行完毕后的结果，可以使用 `Callable` 接口和 `Future` 类。

```java
import java.util.concurrent.Callable;
import java.util.concurrent.FutureTask;

public class Main {
    public static void main(String[] args) throws Exception {
        FutureTask<String> futureTask = new FutureTask<>(new Callable<String>() {
            @Override
            public String call() throws Exception {
                return "Hello, world!";
            }
        });

        new Thread(futureTask).start();
        
        String result = futureTask.get();
        System.out.println(result);
    }
}
```

注意事项：

1. **线程安全**：当多个线程共享资源时，需要注意线程安全问题。**可以使用`synchronized`关键字或其他并发工具类进行同步。**
2. **死锁**：避免**多个线程相互等待资源，导致程序卡住。**
3. **线程间通信**：`wait()`, `notify()`, `notifyAll()` 等方法可用于线程间的基本通信。

多线程编程通常涉及更多复杂的概念，例如线程局部存储、线程优先级、守护线程等。但上述几种方法是最基本和最常用的多线程实现方式。



### 守护线程和非守护线程

守护线程（Daemon Thread）和非守护线程（Non-daemon Thread）是编程中**多线程概念**的一部分，特别是在Java和Python这样的编程语言中比较常见。**这两种线程的主要区别在于程序是否等待它们执行完成。**

**守护线程（Daemon Thread）**

1. **生命周期**：守护线程是一种在后台运行的线程，**主要用于执行那些不应阻止程序退出的任务。**
2. **程序退出**：**一旦程序中所有的非守护线程都结束了，守护线程将被自动终止，即使它们没有完成执行。**
3. **用例**：常见的例子包括垃圾回收、日志服务等。

**非守护线程（Non-daemon Thread）** **-用户线程**

1. **生命周期**：非守护线程是程序的主要工作线程，用于执行核心任务。

2. **程序退出**：程序会等待所有的非守护线程执行完毕才会退出。

3. **用例**：主程序逻辑、用户交互等。

   

### 常见问题

**1、为什么要使用多线程?**
参考解答：

生活中很多事情就是「看起来」在同时进行的，计算机也是类似的。如果全都串行执行，程序的效率就会异常慢，并且也浪费了系统的资源；
更好地利用多核 CPU，更多的 CPU 就可以帮我们处理更多任务。

**2、使用多线程可能带来什么问题?**
参考解答：

多线程是重要的基础知识，是一门学习成本较高的技术。在步入工作的初期很可能不会接触到多线程编程，因此我们需要在工作学习之余，温故而知新地去学习和理解多线程编程，以备将来不时之需。

**线程安全问题**，由于 CPU 执行线程具有随机性。如果我们不太熟悉多线程的知识，不能利用好编程语言提供的工具类，很可能会得到错误的结果；
**可能产生竞态条件**：竞态条件指的是多个线程在访问和修改共享的变量或资源时，由于执行顺序的不确定性而导致程序结果的不确定性。具体来说，**如果多个线程同时读取和修改一个共享变量，那么就可能出现竞态条件。**
**可能产生死锁问题**：死锁（**Deadlock**）是指两个或多个线程在等待另一个线程持有的资源时被阻塞的状态，从而导致它们无法继续执行。为避免死锁，在编程的时候应该避免持有多个锁，以相同的顺序获取锁，或者使用超时机制来避免长时间等待等。

**3、并发与并行的区别是什么？**

参考解答：

并发：是指在 同一时间段内 **交替执行 多个线程，交替是随机的**。在并发编程中，线程之间共享同一个 CPU 的**时间片**，每个线程都可以在同一时间内执行一部分代码；
并行：是指 同时 执行多个线程。**这些线程在不同的 CPU 核心或处理器上同时执行任务，从而实现同时处理多个任务。**

**4、同步和异步的区别？**

参考解答：

同步 ： 同步不是生活中的「同步走、一起走」，而是「排队等待执行」的意思。后面的任务必须等待前面的任务完成以后才能执行。类似于接力赛中，第 2 棒的选手必须等待，拿到第 1 棒的选手的接力棒以后才能跑起来。
异步 ：前面的执行任务还没有返回，后面的任务就可以执行了。类似于接力赛中，第 2 棒的选手无须等待第 1 棒的选手的接力棒就可以跑起来，这只是一个比喻，没有这样的接力比赛。

**5、创建线程的两个方法「实现 Runnable」 和「继承 Thread」用哪个好？**

参考解答：

如果想要更灵活和可重用的并发代码，建议实现 Runnable接口。但是，如果只需要编写简单的并发代码，可以考虑继承 Thread 类；

通常来说实现 Runnable接口更好一点：实现 Runnable接口这种方式创建并发代码更加灵活。这是因为在 Java 中，如果选择继承 Thread 类，就无法继承任何其它类。Java 没有多继承，但是可以实现多个接口。

另外，实现 Runnable 接口可以更好地实现代码的重用性。如果有多个任务需要在不同的线程中运行，我们可以创建多个 Runnable 实例，并将它们传递给多个Thread对象的构造方法。但是如果继承 Thread 类，就需要为每个任务创建一个新的Thread子类。



### 注解是给代码加上的标记

我们最早接触的注解可能是 **@Override** ，它修饰在方法上，被注解 **@Override** 修饰的方法表示：**方法覆盖了父类（或者父类的父类）的某个方法。**有了 @Override 注解，如果父类的方法名、参数个数、参数类型、返回值类型和当前方法不一致，编译器就会报错。所以注解在这里有两个作用：

- 给人看：父类也有这个方法，在子类被重写了；
- 给编译器看：帮我检查一下，我是不是重写对了。

因此，注解是给代码加上的标记，是对代码内容的说明。设计注解是为了设计更通用的功能，我们先来看看注解有什么用。

**注解有什么作用**

- 增强语义：上面说了，注解有一部分功能是写给人看的，向看代码的人说明这个方法不是当前类就有的，而是父类就有的，在我这里我重新定义了。有人说，注释是代码的一部分。因此注解更是代码的一部分，也起到了自解释的功能；
- 增强功能：在任何需要的地方加上一个 标记，增强原有的功能。我们在学习 Java 框架的时候会遇到大量的注解，使用这些注解大大简化了我们的开发；




# 异常

在Java中，异常（Exception）和错误（Error）都是继承自`Throwable`类的对象。`Throwable`类是所有异常和错误的“根类”，并且只有`Throwable`或其子类的对象才可以被抛出（`throw`）或捕获（`catch`）。这里是Java异常类型的一个概览：

### Throwable

- **Throwable**: 是所有异常和错误的父类。它有两个主要的子类，分别是`Error`和`Exception`。

### Error

- **Error**

  : 表示严重的问题，通常是JVM或系统级别的。程序一般不应尝试捕获这类问题。常见的例子包括：

  - **VirtualMachineError**: 如`OutOfMemoryError`、`StackOverflowError`等。
  - **AssertionError**: 当断言失败时抛出。

### Exception

- **Exception**: 是应用级异常的基类。根据是否需要强制捕获，`Exception`又可分为受检异常和非受检异常。

  #### 受检异常（Checked Exceptions）

  - 这些异常在编译时需要处理（即必须使用`try-catch`块捕获，或者在方法签名中使用`throws`关键字声明）。
  - **IOException**: 输入输出异常，例如`FileNotFoundException`。
  - **SQLException**: 数据库访问异常。
  - **ClassNotFoundException**: 找不到指定的类。

  #### 非受检异常（Unchecked Exceptions）

  - 这些异常继承自`RuntimeException`，编译器不强制要求处理它们。
  - **NullPointerException**: 当访问`null`对象的方法或字段时抛出。
  - **IndexOutOfBoundsException**: 如`ArrayIndexOutOfBoundsException`，访问数组或列表的非法索引。
  - **ArithmeticException**: 如除以零。

### 自定义异常

- 除了Java内建的异常类型，你还可以创建自定义异常。通常，自定义异常继承自`Exception`类（受检）或`RuntimeException`类（非受检）。

### 示例代码

```java
try {
    // 可能会抛出异常的代码
} catch (FileNotFoundException e) {
    // 处理FileNotFoundException
} catch (IOException e) {
    // 处理其他IOException
} catch (Exception e) {
    // 处理其他Exception
} finally {
    // 无论是否发生异常，都会执行此块代码
}
```



### JVM处理异常的方式

**1.打印错误信息**

a.异常的类名

b.异常信息

c.异常的位置

d.错误的行号



**2.将程序停止**

JVM处理异常的方式不能够满足我们的需求,因为我们想要对异常处理之后，程序还能够继续运行下去，所以需要自己来处理异常

我们处理异常的方式
**1.try…catch…finally**

**2.throws**

try…catch…finally异常处理方法
try…catch…finally异常处理的格式:

**try {**
**可能出现问题的代码;**
**} catch(异常类名 异常对象) {**
**异常处理的代码**
**} finally {**
**释放未关闭的资源** 
**}**

try…catch…finally执行流程：

1.程序执行到错误代码的地方,系统会抛出一个异常对象

ArithmeticException ae = new ArithmeticException("/by zero");

throw ae;

2.程序转入catch块进行逐个匹配

3.匹配成功,程序执行 catch代码

4.匹配失败,程序还给JVM处理



# 相关选择题

<img src="C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231102234302907.png" alt="image-20231102234302907" style="zoom: 67%;" />

机器语言、汇编语言和高级语言是不同级别的计算机编程语言，它们各有特点和应用场景。

**机器语言：**

机器语言是最低级别的编程语言，也是计算机硬件能够直接理解和执行的指令集。它由一系列的二进制代码组成，每个代码都直接对应处理器的指令。机器语言指令通常由一系列的0和1表示，这些指令非常依赖于具体的硬件架构。

**例子**：`10110000 01100001` 可能表示在x86架构上将字母 `a`（其ASCII码为 97，二进制表示为 01100001）加载到寄存器AL中的指令。

**汇编语言：**

汇编语言是低级语言，但它使用符号代替了机器语言中的二进制代码。这些符号称为助记符，它们与机器指令一一对应，更易于程序员理解和记忆。每条汇编语言的指令通常代表一条机器语言指令。汇编语言同样依赖于具体的硬件架构。它需要通过汇编器（Assembler）转换成机器语言才能被计算机执行。

**例子**：在x86架构上，`mov al, 61h` 代表将十六进制值61（ASCII码中的 `=` 符号）移动到寄存器AL中，它与上面的机器语言指令等价。

**高级语言：**

高级语言是更接近人类语言的编程语言，它抽象了底层的硬件细节。高级语言使得编程更加容易，因为它们不需要程序员管理内存地址或者考虑CPU指令。这些语言通常是跨平台的，也就是说，相同的高级语言代码可以在不同的硬件和操作系统上运行，只要有适当的编译器或解释器。高级语言代码需要通过编译器（Compiler）转换成机器语言，或通过解释器（Interpreter）在运行时转换，以便计算机执行。

**例子**：

- **C语言**（编译语言）：`int a = 5;`
- **Python**（解释语言）：`a = 5`
- **Java**（既需要编译也需要解释执行）：`int a = 5;`

这些高级语言的代码示例都实现了一个基本的操作，即声明一个整数变量 `a` 并将其赋值为5，但它们隐藏了将该值存储到内存中具体地址的细节。

总结一下，机器语言是处理器可以直接执行的指令集，汇编语言是这些指令的符号表示，而高级语言则提供了更高层次的抽象，使得编程更加容易，同时使得程序更具有可移植性。

<img src="C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231102234736491.png" alt="image-20231102234736491" style="zoom: 67%;" />



<img src="C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231103001447546.png" alt="image-20231103001447546" style="zoom:67%;" />

在Java中，比较两个字符串时主要使用 `equals()` 方法和 `compareTo()` 方法。

- ### `equals()` 方法

`equals()` 方法用于比较字符串的内容是否相等。这个方法比较的是字符串的值，而不是引用。

```
javaCopy codeString str1 = "Hello";
String str2 = "Hello";
String str3 = "hello";

boolean result1 = str1.equals(str2); // 返回 true，因为内容完全相同
boolean result2 = str1.equals(str3); // 返回 false，因为大小写不同
```

如果你想要忽略大小写进行比较，你可以使用 `equalsIgnoreCase()` 方法：

```

boolean result3 = str1.equalsIgnoreCase(str3); // 返回 true，因为这里忽略了大小写
```

- ### `compareTo()` 方法

`compareTo()` 方法比较字符串的字典顺序。它返回一个整数，该整数表示调用者字符串和参数字符串在字典顺序上的差异。

- 如果两个字符串相等，`compareTo()` 返回 `0`。
- 如果调用者字符串在字典顺序上排在参数字符串之前，返回一个负数。
- 如果调用者字符串在字典顺序上排在参数字符串之后，返回一个正数。

```
javaCopy codeint result4 = str1.compareTo(str2); // 返回 0，因为两个字符串相等
int result5 = str1.compareTo(str3); // 返回一个正数，因为"Hello"字典顺序上排在"hello"之前
```

与 `equalsIgnoreCase()` 方法类似，如果你想在比较时忽略大小写，可以使用 `compareToIgnoreCase()` 方法：

```

int result6 = str1.compareToIgnoreCase(str3); // 返回 0，因为忽略大小写后两者相等
```

- ### 总结

- 使用 `equals()` 或 `equalsIgnoreCase()` 来检查两个字符串是否相等。
- 使用 `compareTo()` 或 `compareToIgnoreCase()` 来比较两个字符串的字典顺序。

不要使用 `==` 操作符来比较字符串，因为 `==` 比较的是对象引用是否指向堆内存中的同一位置，而不是比较字符串的内容。



- ### Python和Java的数据比较不同

在Python和Java中，比较不同数据类型的变量的方法和规则有所不同，因为这两种语言在类型系统和类型转换方面的设计哲学不同。

- #### Python中的比较方法：

Python是动态类型语言，它允许你比较不同类型的变量。比较操作通常是基于一组规则的，例如数字和字符串之间的比较，或者在Python 2中，不同类型的比较通常会考虑它们的类型名（但这在Python 3中已经不再允许，会引发TypeError）。

```python
pythonCopy code# 在Python 3.x中，直接比较不同类型将会引发错误
1 < '2'  # TypeError: '<' not supported between instances of 'int' and 'str'

# 如果有逻辑上的比较方式，比如不同类型的数字，Python将正常比较
1 < 2.5  # True，因为这两个可以按数值比较

# 对于完全不同的类型，你通常会将它们转换为共同类型
str(1) < '2'  # True，因为这里都是字符串的比较
```

在Python中，推荐在进行比较之前明确地将变量转换为相同类型，除非比较的是同一类型的不同实例。

- #### Java中的比较方法：

Java是静态类型语言，类型在编译时就已确定，你不能直接比较不兼容的类型。如果尝试这样做，编译器会报错。

```java
javaCopy codeint a = 1;
String b = "2";

// a < b; // 编译错误：不兼容的类型

// 必须先将int转换为String，或者将String转换为int
boolean result = Integer.toString(a).compareTo(b) < 0; // 将int转换为String再比较
// 或者
boolean result = a < Integer.parseInt(b); // 将String转换为int再比较
```

在Java中，如果想要比较不同类型的变量，你必须先进行显式类型转换或者调用适当的方法，将变量转换为可以比较的类型。对于原始数据类型，可以进行类型提升（例如，将`int`转换为`double`再进行比较）。对于对象，可以调用相应的方法，例如比较字符串和数字时，可以使用字符串的 `compareTo()` 方法或将字符串解析为一个数字。

类型的转换和比较必须是有意义的，你不能将一个字符串转换为数字进行比较，除非字符串确实表示一个数字。

总结一下，在Python中，尽管可以直接比较不同类型，但推荐转换为相同类型进行比较。在Java中，你必须将不同类型的变量转换为相同类型才能进行比较，否则会有编译时错误。

<img src="C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231103005000468.png" alt="image-20231103005000468" style="zoom:67%;" />

要避免在 `while` 循环中产生无限循环，你需要确保循环最终能够达到其结束条件。这通常涉及到以下几个方面：

A - **初始化循环控制变量**：你需要在循环开始前正确设置循环控制变量的初始值，这样它才能在测试表达式中被正确评估。

B - **循环控制变量需要在 while-loop 语句中进行测试**：`while` 循环的条件检查必须能够因循环控制变量的改变而最终评估为 `false`，以便退出循环。

C - **循环控制变量需要在循环主体内部更新**：确保循环体内有代码能改变循环控制变量的值，这样条件检查最终就能失败，循环就会停止。

D - **改成其他的循环形式**：虽然改变循环的形式可能帮助逻辑更清晰，但它本身并不直接阻止无限循环。无论使用哪种循环形式（`for`，`while`，`do-while`），都必须确保满足上述A、B和C点以避免无限循环。



<img src="C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231103005150622.png" alt="image-20231103005150622" style="zoom: 67%;" />

在编程中，**方法签名**定义了方法的名称和参数列表。对于不同的编程语言，方法签名的定义有细微的差别，但一般情况下，以下部分被认为构成了方法签名：

1. **方法名称**: 方法的名字是其标识，是调用方法时使用的标识符。
2. **参数列表**: 包括参数的类型、顺序、数量和参数名（在某些语言中）。这是方法签名非常重要的一部分，因为即使两个方法具有相同的名字，只要它们的参数列表不同，它们也是不同的方法。

不属于方法签名的部分包括方法的返回类型、访问修饰符（如 `public`、`private` 等）和抛出的异常（在某些语言中）。

- ##### 例如，在Java中：

```
javaCopy codepublic int add(int a, int b) {
    return a + b;
}
```

在这个例子中，方法签名是 `add(int, int)`。它由方法名称 `add` 和参数列表 `int a, int b` 组成。注意，虽然Java的方法重载考虑参数列表，但不考虑返回类型。

- ##### 另一个例子，在Python中：

```
pythonCopy codedef add(a, b):
    return a + b
```

在Python中，方法签名通常只考虑方法名称 `add` 和参数列表 `(a, b)`。Python不支持传统意义上的重载，因此参数名和类型不像在Java中那样被严格考虑为方法签名的一部分。然而，参数的数量和顺序确实很重要。



<img src="C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231103005453320.png" alt="image-20231103005453320" style="zoom:67%;" />

以下是基于Java的语法：

A - `int 1_Number=1` 变量名不能以数字开头。因此，这个声明是错误的。

B - `boolean answer="false"` 在Java中，布尔值应该是没有引号的 `true` 或 `false`，而不是字符串。因此，这个声明也是错误的。

C - `char answer="Y"` 在Java中，字符字面量应该用单引号 `'` 而不是双引号 `"`。双引号用于字符串字面量。因此，这个声明也是错误的。正确的声明应该是 `char answer='Y';`。

D - `int number$copies=10` 在Java中，变量名中可以包含美元符号（`$`），尽管这不是最佳实践。因此，这个声明是正确的。



<img src="C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231103013107465.png" alt="image-20231103013107465" style="zoom:67%;" />

A - **可以创建多个随机数生成器**： 确实，使用 `Random` 类，你可以创建多个随机数生成器实例，每个实例都有自己的种子和状态。这对于需要在不同的上下文中生成不同随机数序列的场景很有用。例如，在多线程应用程序中，每个线程可以有自己的 `Random` 实例，以避免竞争条件。

B - **随机中的生成器比 Math.random 中的生成器更有效**： 这个说法通常是不成立的。`Math.random()` 内部也使用了 `Random` 类的实例（静态实例），所以它们的效率是相似的。实际效率取决于具体实现，但并没有根本性的差异。

C - **可以在一个范围内生成随机整数、浮点数和整数**： `Random` 类提供了多种方法来生成不同类型和范围的随机数，比如 `nextInt()`, `nextFloat()`, `nextDouble()`, `nextLong()` 等，可以指定范围。而 `Math.random()` 只能生成一个在0.0到1.0之间的随机 `double` 值，如果你想要其他类型或者范围，需要进行额外的计算。

D - **可以初始化和重新初始化随机生成器**： `Random` 类允许你在创建随机数生成器实例时指定种子，也可以通过 `setSeed()` 方法重新设置种子。这允许你在需要时重现一个随机数序列。`Math.random()` 没有提供直接的方法来设置种子，因为它使用的是静态 `Random` 实例。

综上，正确答案是：

- A：正确，`Random` 类允许创建多个随机数生成器实例。
- B：错误，效率大致相当，并没有明显优势。
- C：正确，`Random` 类提供了更多方法来生成不同类型和范围的随机数。
- D：正确，`Random` 类允许初始化和重新初始化随机数生成器的种子。







**在 Java 中，如果在初始化变量之前尝试使用该变量，会发生什么情况？**

在Java中，如果你在初始化一个变量之前尝试使用它，那么会发生编译时错误。Java编译器要求变量在使用之前必须被初始化，否则编译器将无法编译代码，并会给出一个错误消息，如“变量可能尚未初始化”。

这种规则适用于局部变量。对于局部变量，编译器不会给它们赋予默认值，所以你必须在使用它们之前明确地初始化它们：

```java
int value;
System.out.println(value); // 错误：变量 value 可能尚未初始化
```

但是，类的成员变量（字段）和数组的情况有所不同。如果你声明一个类的成员变量但没有显式初始化它，那么它会被自动初始化为该类型的默认值（例如，数值类型的默认值是0，布尔类型的默认值是false，对象类型的默认值是null）。例如：

```java
public class MyClass {
    private int value; // 自动初始化为0

    public void printValue() {
        System.out.println(value); // 将打印出0，没有编译错误
    }
}
```

同样地，数组也会在创建时自动被初始化为它们各自类型的默认值：

```java
int[] array = new int[5]; // 所有元素自动初始化为0
System.out.println(array[0]); // 将打印出0，没有编译错误
```

总结一下，如果在初始化变量之前尝试使用局部变量，Java编译器会报错。对于类的字段和数组，Java会自动将它们初始化为默认值。





<img src="C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231103013450097.png" alt="image-20231103013450097" style="zoom: 67%;" />

在Java中，点运算符（`.`）主要用于访问对象的成员，无论是字段（属性）、方法还是内部类。它用于引用变量和后面的属性或方法。因此，以下是点运算符的功能：

A - 错误。点运算符不是用来分隔浮点数的整数部分与小数部分的。这是小数点的功能。

B - 正确。点运算符允许通过对象引用来访问对象内的数据成员（字段或属性）。

C - 正确。点运算符同样允许通过对象引用来调用对象内的方法。

D - 错误。点运算符不是用来终止命令的；在Java中，命令（语句）通常以分号（`;`）终止。



