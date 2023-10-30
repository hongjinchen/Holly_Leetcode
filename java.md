### Java 数据类型

Java 的数据类型可以分为两大类：基本数据类型（Primitive Data Types）和引用数据类型（Reference Data Types）。

**基本数据类型**

1. **byte**: 8 位整型数，范围从 -128 到 127。
2. **short**: 16 位整型数，范围从 -32,768 到 32,767。
3. **int**: 32 位整型数，范围从 -2^31 到 2^31 - 1。
4. **long**: 64 位整型数，范围从 -2^63 到 2^63 - 1。
5. **float**: 32 位浮点数。
6. **double**: 64 位浮点数。
7. **char**: 16 位 Unicode 字符。
8. **boolean**: 布尔类型，只有两个取值：`true` 和 `false`。

**引用数据类型**

1. **对象（Object）**: 任何继承自 `Object` 类的类型。
2. **数组（Array）**: 一个存储同类型数据的连续空间。
3. **枚举（Enum）**: 一种特殊的类，它可以有一组预定义的常量。
4. **接口（Interface）**: 一种定义方法但不实现的类型。

**字符串（String）**

虽然 `String` 类型在 Java 中实际上是一个对象，但由于其在 Java 中的特殊地位和常用性，有时它被视为一个单独的数据类型。



#### **Java的回收机制（Garbage Collection）**

Java 使用垃圾回收机制自动管理内存，主要目标是识别并回收不再使用的对象。Java中的垃圾收集器通常是后台运行的，它自动地查找不再被引用的对象并释放其占用的内存。

**引用计数（Reference Counting）**



#### **java多态**

多态（Polymorphism）是面向对象编程中的一个重要概念，**它允许你使用一个接口来表示多种数据类型**。在 Java 中，多态主要通过**接口、继承和方法重载来实现**。下面我会详细解释这个概念。

**主要类型：**

1. **编译时多态（静态多态）**：主要是通过方法重载实现的。
2. **运行时多态（动态多态）**：主要是通过继承和接口实现的。

**编译时多态**

方法重载是一种编译时多态。同一个类中可以有多个同名但参数列表不同的方法。

```
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

   ```
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

   ```
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

多态是面向对象编程的四大基本特性之一（封装、继承、多态和抽象）。正确地使用多态可以使代码更灵活、可扩展和易于维护。



#### Java继承

在 Java 中，继承是一种允许我们重用代码和建立类之间关系的机制。通过继承，一个类（称为子类或派生类）可以获得另一个类（称为父类或基类）的字段（变量）和方法。下面详细介绍 Java 中继承的各个方面。

**基础语法**

要创建一个子类，您可以使用 `extends` 关键字：

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



**方法覆盖（Method Overriding）**

子类可以提供父类已有方法的特定实现。这被称为方法覆盖。

```java
public class Dog extends Animal {
    @Override
    public void makeSound() {
        System.out.println("Woof woof");
    }
}
```

现在，如果您创建一个 `Dog` 对象并调用 `makeSound` 方法，将输出 "Woof woof"，而不是 "Some generic animal sound"。



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



**访问修饰符和继承**

- `private` 成员不会被继承。
- `public` 和 `protected` 成员会被继承，并且在子类中是可访问的。
- 默认（package-private）成员会被继承，但只在同一个包中的子类中是可访问的。



**final 关键字**

如果一个类用 `final` 关键字标记，那么它不能被继承。

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



#### Java多线程的实现

在Java中，多线程主要可以通过以下几种方式实现：

**1. 继承 `Thread` 类**

你可以创建一个新类，继承自 `Thread` 类，并重写 `run()` 方法。然后通过创建该类的实例并调用其 `start()` 方法来创建并启动新线程。

```
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

你也可以通过实现 `Runnable` 接口来创建多线程。这种方法更为灵活，因为Java不支持多重继承，所以实现接口是一种更好的选择。

```
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

**3. 使用 `Executor` 框架**

Java的 `java.util.concurrent` 包提供了更高级的多线程支持，包括线程池。

```
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Main {
    public static void main(String[] args) {
        ExecutorService executorService = Executors.newFixedThreadPool(10);

        executorService.execute(new MyRunnable());
        
        executorService.shutdown();
    }
}
```

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

1. **线程安全**：当多个线程共享资源时，需要注意线程安全问题。可以使用`synchronized`关键字或其他并发工具类进行同步。
2. **死锁**：避免多个线程相互等待资源，导致程序卡住。
3. **线程间通信**：`wait()`, `notify()`, `notifyAll()` 等方法可用于线程间的基本通信。

多线程编程通常涉及更多复杂的概念，例如线程局部存储、线程优先级、守护线程等。但上述几种方法是最基本和最常用的多线程实现方式。



#### 覆盖（Override）和重载（Overload）

`覆盖（Override）` 和 `重载（Overload）` 是 Java 中两个非常重要的概念，它们在形式和目的上有明显的不同。下面详细解释它们之间的主要区别。

**覆盖（Override）**

1. **定义**: 子类提供了一个与父类方法签名（方法名和参数类型）完全相同的方法。

2. **目的**: 为了改变继承自父类的同名方法的行为。

3. **修饰符**: 必须与父类方法的修饰符相同或更为宽松。例如，如果父类方法是 `protected`，则子类覆盖的方法可以是 `protected` 或 `public`。

4. **返回类型**: 必须与父类方法的返回类型相同或是其子类型。

5. **抛出异常**: 子类覆盖的方法所抛出的异常应该是被父类抛出异常的子集。

6. **运行时行为**: Java 使用运行时多态性来选择要执行的方法版本，即它执行的是对象实际类的方法版本。

   ```
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



**重载（Overload）**

1. **定义**: 在同一个类中定义一个与已有方法名相同但参数列表不同的方法。

2. **目的**: 让同一个方法可以有不同类型或数量的参数。

3. **修饰符**: 可以与已有的重载方法有不同的访问修饰符。

4. **返回类型**: 可以与已有的重载方法有不同的返回类型。

5. **抛出异常**: 可以与已有的重载方法有不同的异常抛出列表。

6. **编译时行为**: Java 使用编译时多态性来解析应该调用哪个方法。

   ```
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



#### 守护线程和非守护线程

守护线程（Daemon Thread）和非守护线程（Non-daemon Thread）是编程中多线程概念的一部分，特别是在Java和Python这样的编程语言中比较常见。这两种线程的主要区别在于程序是否等待它们执行完成。

**守护线程（Daemon Thread）**

1. **生命周期**：守护线程是一种在后台运行的线程，主要用于执行那些不应阻止程序退出的任务。
2. **程序退出**：一旦程序中所有的非守护线程都结束了，守护线程将被自动终止，即使它们没有完成执行。
3. **用例**：常见的例子包括垃圾回收、日志服务等。

**非守护线程（Non-daemon Thread）**

1. **生命周期**：非守护线程是程序的主要工作线程，用于执行核心任务。
2. **程序退出**：程序会等待所有的非守护线程执行完毕才会退出。
3. **用例**：主程序逻辑、用户交互等。



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