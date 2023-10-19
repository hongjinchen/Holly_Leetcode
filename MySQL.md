

# MySQL



## 真题


**SQL中，下面对于数据定义语言DDL描述正确的是（）**

A DDL关心的是数据库中的数据

B 联盟链

C 控制对数据库的访问

D 定义数据库的结构



D

（1）数据定义（SQL **DDL**）用于定义SQL模式、基本表、视图和索引的创建和撤消操作。
（2）数据操纵（SQL **DML**）数据操纵分成数据查询和数据更新两类。数据更新又分成插入、删除、和修改三种操作。
（3）数据控制（DCL）包括对基本表和视图的授权，完整性规则的描述，事务控制等内容。

（4）嵌入式SQL的使用规定（TCL）涉及到SQL语句嵌入在宿主语言程序中使用的规则。




**下面哪个不是sql的合法标识符**

A 22d

B sd1

C #id

D sut@



A

- **A: `22d`**: 以数字 `22` 开头，所以这不是一个合法的 SQL 标识符。

- **B: `sd1`**: 以字母 `s` 开头，后面跟着字母和数字，这是一个合法的标识符。

- **C: `#id`**: 虽然一些数据库（如 SQL Server）可能允许在标识符中使用 `#` 符号，但这通常是特定于数据库的。基于标准 SQL 的规则，这通常不是一个合法的标识符。然而，根据问题的设定，它与选项 A 相比更可能是合法的，因为它以字母开头。

- **D: `sut@`**: 和选项 C 类似，`@` 符号通常不是一个合法的字符，但在某些数据库系统中可能是允许的。与选项 A 相比，它更可能是合法的，因为它以字母开头。

  

在 SQL 中，合法标识符（也称为合法名称或合法对象名称）用于识别数据库、表、列、索引、触发器等数据库对象。虽然不同的数据库管理系统（DBMS）可能有一些特定的规则和限制，但通常，合法标识符遵循以下基本规则：

### 基础规则：

1. **首字符**: 标识符的第一个字符通常必须是字母（A-Z 或 a-z）或下划线（_）。
2. **其他字符**: 除首字符外，标识符还可以包含字母、数字和下划线。
3. **大小写敏感性**: 在一些 DBMS（如 PostgreSQL）中，标识符是大小写敏感的。在其他 DBMS（如 MySQL 的默认设置）中，标识符是大小写不敏感的。
4. **长度限制**: 大多数 DBMS 都有关于标识符长度的限制。例如，在 SQL Server 中，标识符最多可以有 128 个字符，而在 MySQL 中，这个限制是 64 个字符。
5. **保留字**: 通常，保留字不能用作标识符，除非你使用了特定的引用符号来括起它。

### 特殊字符和引用

如果你需要在标识符中使用特殊字符或保留字，你通常需要使用一种引用机制，这依赖于特定的 DBMS。例如：

- 在 SQL Server 中，你可以使用方括号（`[...]`）。
- 在 MySQL 和 PostgreSQL 中，你可以使用反引号（``...``）或双引号（`"..."`）。

### 示例：

- 合法的标识符： `username`, `_username`, `user123`, `User_Name`
- 非法的标识符： `123user` (以数字开头), `user-name` (包含非法字符 `-`)





**Mysql中表student_table(id,name,birth,sex)，插入如下记录：**

('1004' , '张三' ,'2000-08-06' , '男');
('1009' , '李四', '2000-01-01', '男');
('1010' , '李四', '2001-01-01', '男');
('1006' , '王五', '2000-08-06' , '女');
('1008' , '张三', '2002-12-01', '女');
('1012' , '张三', '2001-12-01', '女');
('1011' , '李四', '2002-08-06' , '女');

执行

select t1.*,t2.*
from (
select * from student_table where sex = '男' ) t1 
left join 
(select * from student_table where sex = '女')t2 
on t1.name = t2.name ; 
的结果行数是（）？



要解决这个问题，我们需要考虑两个从 `student_table` 中选取的子集：一个只包含 "男" 性别，另一个只包含 "女" 性别。

1. "男" 性别的子集包含以下记录：
   - ('1004', '张三', '2000-08-06', '男')
   - ('1009', '李四', '2000-01-01', '男')
   - ('1010', '李四', '2001-01-01', '男')
2. "女" 性别的子集包含以下记录：
   - ('1006', '王五', '2000-08-06', '女')
   - ('1008', '张三', '2002-12-01', '女')
   - ('1012', '张三', '2001-12-01', '女')
   - ('1011', '李四', '2002-08-06', '女')

然后，我们执行一个左连接（left join），其中 "男" 性别的子集是左表（t1），"女" 性别的子集是右表（t2）。连接条件是 `t1.name = t2.name`。

对于左表中的每一行，我们都会找到所有与之匹配的右表中的行。如果没有匹配项，那么结果将显示左表中的行和右表中的空值。

下面是每一行的匹配情况：

1. ('1004', '张三', '2000-08-06', '男') 匹配两行：
   - ('1008', '张三', '2002-12-01', '女')
   - ('1012', '张三', '2001-12-01', '女')
2. ('1009', '李四', '2000-01-01', '男') 匹配一行：
   - ('1011', '李四', '2002-08-06', '女')
3. ('1010', '李四', '2001-01-01', '男') 也匹配一行：
   - ('1011', '李四', '2002-08-06', '女')

所以，在结果中我们有：

- 2 行对应于 '张三'
- 1 行对应于第一条 '李四'
- 1 行对应于第二条 '李四'

一共是 2 + 1 + 1 = 4 行。





![image-20231019164227359](C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231019164227359.png)

存储过程（Stored Procedure）是一种在数据库中预编译的 SQL 代码块。你可以将一组为了达到特定目的而逻辑地组织在一起的 SQL 语句保存为一个存储过程，然后通过一个单一的存储过程调用来执行这组语句。

存储过程有以下几个主要优点：

### 1. 性能优化：

- **预编译：** 存储过程在第一次运行时会被编译，并将编译后的版本存储在数据库中，这样再次运行相同的存储过程时就不需要重新编译。
- **减少网络流量：** 只需发送存储过程的名称和参数（如果有）即可，而不是一长串复杂的 SQL 代码。

### 2. 代码重用和一致性：

由于存储过程是一次创建，多次使用，因此它们有助于代码重用。同时，因为多个应用可以共享同一个存储过程，所以也更容易保证结果的一致性。

### 3. 维护性：

如果需要更改 SQL 逻辑，只需要更改存储过程即可，而不需要修改所有使用这段逻辑的应用程序代码。

### 4. 安全性：

- 可以限制用户只能执行某些预定义的存储过程，而不能执行任意 SQL 代码。
- 也可通过存储过程来设置更复杂的业务逻辑和验证，从而提高数据库的安全性。

存储过程的基本语法因数据库系统而异。例如，在 SQL Server 中，创建存储过程的基本语法可能如下：

```
sqlCopy codeCREATE PROCEDURE ProcedureName
    @param1 datatype,
    @param2 datatype,
    ...
AS
BEGIN
    -- SQL statements here
END;
```

调用存储过程也很简单，通常像这样：

```
sqlCopy code
EXEC ProcedureName @param1=value1, @param2=value2, ...;
```

这样，你就可以通过一个简单的调用来执行一组预定义的 SQL 语句，而不需要每次都写出所有的 SQL 代码。



![image-20231019164851872](C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231019164851872.png)

A选项的操作会将该字段所在的列中所有数据替换成别名



![image-20231019165032437](C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231019165032437.png)

1：处理效率：drop>trustcate>delete

2：删除范围：drop删除整个表（结构和数据一起删除）；trustcate删除全部记录，但不删除表结构；delete只删除数据

3：高水位线：delete不影响自增ID值，高水线保持原位置不动；trustcate会将高水线复位，自增ID变为1。



![image-20231019171613624](C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231019171613624.png)

需要行转列按日期分组并对列求和，因此需要group by Date， sum(...胜/负)。

A中无sum，错；

B中无group by，错；

C中case when ... then ... else ... end用法不正确，错；



在 SQL 中，`CASE WHEN ... THEN ... ELSE ... END` 是一种条件表达式，用于根据一个或多个条件来选择不同的输出结果。这个结构类似于其他编程语言中的 `if-else` 或 `switch-case` 语句。

### 基本语法

```
sqlCopy codeCASE 
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    ...
    ELSE resultN
END
```

- **CASE**: 开始一个 `CASE` 表达式。
- **WHEN condition1 THEN result1**: 如果 `condition1` 为 `TRUE`，则返回 `result1`。
- **ELSE resultN**: 如果没有任何条件为 `TRUE`，则返回 `resultN`。
- **END**: 结束 `CASE` 表达式。

### 举例说明

考虑一个名为 `employees` 的表，其中有一个名为 `salary` 的列。

```
sqlCopy codeSELECT name, 
       CASE 
           WHEN salary < 50000 THEN 'Low'
           WHEN salary >= 50000 AND salary < 100000 THEN 'Medium'
           ELSE 'High'
       END AS salary_category
FROM employees;
```

这个查询会返回员工的名字和他们的薪水类别（Low、Medium 或 High）。

- 如果 `salary` 小于 50,000，`salary_category` 将为 'Low'。
- 如果 `salary` 在 50,000 和 100,000 之间，`salary_category` 将为 'Medium'。
- 否则，`salary_category` 将为 'High'。

### 另一种形式：简化的 CASE 表达式

SQL 还支持另一种简化的 `CASE` 表达式形式，其中你可以直接与一个表达式（通常是一个列名）进行比较。

```
sqlCopy codeCASE expression
    WHEN value1 THEN result1
    WHEN value2 THEN result2
    ...
    ELSE resultN
END
```

例如：

```
sqlCopy codeSELECT name,
       CASE job_title
           WHEN 'Manager' THEN 'Management'
           WHEN 'Developer' THEN 'Engineering'
           ELSE 'Other'
       END AS department
FROM employees;
```

这个查询会返回员工的名字和他们所在的部门（Management、Engineering 或 Other）。



![image-20231019172015951](C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231019172015951.png)

INSERT INTO 语句用于向一张表中插入新的行。

SELECT INTO 语句从一张表中选取数据插入到另一张表中。



![image-20231019173418660](C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231019173418660.png)

A选项，聚集函数不能直接出现在WHERE子句中；B选项，商品id既不是聚集函数，也没有在GROUP BY子句后出现，该选项语句错误；C选项，所检索的结果是每一个商品的最高销量，不符题意。



![image-20231019175125575](C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231019175125575.png)


count(name) 时不包括null值，所以结果是3；

插入时null与NULL的意思一样都是NULL。



![image-20231019175156731](C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231019175156731.png)

- A. 视图数据查询：你可以查询视图，就像查询普通的数据库表一样。
- B. 更新视图数据：在某些情况下，你也可以更新视图的数据。但这取决于该视图是如何定义的以及它涉及的底层表结构。例如，如果视图是由多个表联接而成或包含聚合函数，更新可能就不可行。
- C. 在视图中定义新的基本表：这是不可能的。视图本质上是一个或多个表的查询结果，你不能在视图中定义新的基本表。
- D. 在视图中定义新视图：是可行的。你可以基于一个现有的视图定义另一个新的视图。