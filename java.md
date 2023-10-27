

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