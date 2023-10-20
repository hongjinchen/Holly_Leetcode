

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
CREATE PROCEDURE ProcedureName
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
CASE 
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
SELECT name, 
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
CASE expression
    WHEN value1 THEN result1
    WHEN value2 THEN result2
    ...
    ELSE resultN
END
```

例如：

```
SELECT name,
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



![image-20231020154644847](C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231020154644847.png)

【解析】范式是符合某一种级别的关系模式的集合。关系数据库中的关系必须满足一定的要求，满足不同程度要求的为不同范式。目前关系数据库有六种范式：第一范式（ 1NF ）、第二范式（ 2NF ）、第三范式（ 3NF ）、 Boyce-Codd 范式（ BCNF ）、第四范式（ 4NF ）和第五范式（ 5NF ）。满足最低要求的范式是第一范式（ 1NF ）。在第一范式的基础上进一步满足更多要求的称为第二范式（ 2NF ），其余范式以次类推。一般说来，数据库只需满足第三范式（ 3NF ）就行了。 第一范式：主属性（主键）不为空且不重复，字段不可再分（存在非主属性对主属性的部分依赖）。 第二范式：如果关系模式是第一范式，每个非主属性都没有对主键的部分依赖。 第三范式：如果关系模式是第二范式，没有非主属性对主键的传递依赖和部分依赖。 BCNF 范式：所有属性都不传递依赖于关系的任何候选键。 题目中关系模式没有非主属性对主键的传递依赖和部分依赖，满足第三范式，但不满足 BCNF 范式。故本题答案为 A 选项。

数据库范式（Normal Forms）是用于评估数据库表结构质量的一组规则和准则。下面是不同范式的简要介绍：

1. **第一范式（1NF）**: 数据库表的每一列都是不可分割的基本数据项，同时每一行都有一个唯一标识，称为主键。简单来说，表是规范化的，没有重复组或数组。
2. **第二范式（2NF）**: 满足第一范式，并且所有非主键列都完全依赖于整个主键。这意味着没有部分依赖，即非主键字段依赖的不仅仅是主键中的一部分。
3. **第三范式（3NF）**: 满足第二范式，并且所有非主键列都只依赖于主键，不依赖于其他非主键列。这消除了传递依赖。
4. **BCNF范式（Boyd-Codd Normal Form）**: 是第三范式的一个特例。满足BCNF意味着，对于所有的决定性依赖 X -> Y，X 都必须是一个超键（超键是一个特殊类型的键，不仅能唯一标识记录，还可能包含更多的字段）。

根据给定的关系模式 S、C 和 SC，我们可以观察：

- S 表：主键是 S#，其他列（Sn, Sd, SA）完全依赖于主键。
- C 表：主键是 C#，其他列（Cn, P#）完全依赖于主键。
- SC 表：主键可能是 (S#, C#) 组合，G 完全依赖于这个主键。

所有这些表都符合第一范式（所有字段都是不可分割的），第二范式（所有非主键字段完全依赖于整个主键）以及第三范式（没有非主键字段依赖于另一个非主键字段）。

A决定B，B决定C, 但是C不能决定B,B不能决定A,那么存在A到C的依赖传递，BCNF范式是不能有依赖传递的。题中学号，姓名，年龄就是一种依赖传递的关系。那么肯定不是BCNF。



**函数依赖 (Functional Dependency)**

函数依赖是用来表达一种约束，即在一个关系模式中，某一集合的属性值（记作A）能够唯一确定另一集合的属性值（记作B）。这被表示为A*→*B。

**例子：**

假设有一个员工表，其结构如下：

| EmployeeID | Name  | Department | Salary |
| ---------- | ----- | ---------- | ------ |
| 1          | Alice | HR         | 50000  |
| 2          | Bob   | Sales      | 60000  |
| 3          | Carol | HR         | 70000  |

在这个例子中，EmployeeID 唯一确定了 Name、Department 和 Salary。因此，我们可以说：

- EmployeeID→NameEmployeeID→Name
- EmployeeID→DepartmentEmployeeID→Department
- EmployeeID→SalaryEmployeeID→Salary

**属性：**

1. **自反性**: 如果 B 是 A 的子集，那么 �→�*A*→*B*。

2. **增广性**: 如果 �→�*A*→*B*，那么 �∪�→�∪�*A*∪*C*→*B*∪*C*，其中 C 是任意属性集。

3. **传递性**: 如果 �→�*A*→*B* 和 �→�*B*→*C*，那么 �→�*A*→*C*。

   

**部分依赖 (Partial Dependency)**

部分依赖是一种特殊类型的函数依赖，它出现在具有复合主键（由两个或多个属性组成）的关系模式中。

**例子：**

考虑一个学生选课表：

| StudentID | CourseID | Grade | Professor |
| --------- | -------- | ----- | --------- |
| 1         | 101      | A     | Dr. Smith |
| 1         | 102      | B     | Dr. Jones |
| 2         | 101      | C     | Dr. Smith |

在这个表中，复合主键是 (StudentID, CourseID)。

- Grade 是由 (StudentID, CourseID) 唯一确定的，因此它没有部分依赖。

- 但是，Professor 只由 CourseID 确定，这就是一个部分依赖。

  

![image-20231020155155767](C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231020155155767.png)

![img](https://uploadfiles.nowcoder.com/images/20180827/283950953_1535337015759_51B3875ECF358403950EB543513B2F00)

在MySQL中，延时注入通常使用`SLEEP()`函数来实施。`SLEEP()`函数让数据库“睡眠”一段指定的时间（以秒为单位），这样做的目的是检测应用程序是否容易受到SQL注入攻击。如果应用程序也延迟响应，说明注入可能成功。

一个简单的延时注入示例：

```
sqlCopy code
SELECT * FROM users WHERE username = '' OR 1=SLEEP(5) -- ' AND password = 'password';
```

在这个例子中，假设该SQL语句是用于从`users`表中查找与给定`username`和`password`匹配的用户。攻击者通过插入`OR 1=SLEEP(5)`，尝试让数据库暂停5秒钟。如果应用程序的响应也延迟了5秒，那么攻击者可能会认为应用程序容易受到SQL注入攻击。

这种类型的攻击是危险的，应该避免。预防SQL注入的最佳做法是使用预处理语句、参数化查询或者使用ORM（对象关系映射）工具。



![image-20231020155905412](C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231020155905412.png)

关系代数表达式由关系代数操作组合而成。操作中，以笛卡尔积和连接操作最费时 间，并生成大量的中间结果。如果直接按表达式书写的顺序执行，必将花费很多时间，并生 成大量的中间结果，效率较低。 

**MySQL各种操作的时间开销**

1. **SELECT Queries（选择查询）**: 这些通常是最快的操作之一，尤其是当对表进行了适当的索引。但如果需要全表扫描，则可能非常慢。

2. **INSERT Queries（插入查询）**: 插入操作的速度依赖于多种因素，包括是否有触发器、是否有复杂的约束检查等。

3. **UPDATE Queries（更新查询）**: 更新操作通常比插入和选择要慢，因为它们可能涉及更多的磁盘I/O和锁定。

4. **DELETE Queries（删除查询）**: 删除操作可能非常慢，特别是当涉及到大量数据和/或触发器和外键约束时。

5. **JOIN Operations（连接操作）**: 连接操作的效率取决于表的大小和是否进行了适当的索引。INNER JOIN通常比OUTER JOIN快。

6. **Aggregate Functions（聚合函数）**: COUNT、SUM、AVG等聚合函数通常比较快，但如果在没有索引的列上进行，可能会很慢。

7. **Sorting（排序）**: ORDER BY子句会增加查询时间，特别是当排序列没有被索引或者数据量很大时。

8. **Subqueries（子查询）**: 子查询可能会降低查询性能，特别是如果它们嵌套得很深或在循环中使用。

9. **Full-text Search（全文搜索）**: 这通常是一个相对慢的操作，但MySQL的全文搜索引擎已经进行了优化，以提供更快的搜索速度。

   

![image-20231020160024288](C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231020160024288.png)

[数据库设计](https://www.baidu.com/s?wd=数据库设计&tn=SE_PcZhidaonwhc_ngpagmjz&rsv_dl=gh_pc_zhidao)通常分为6个阶段 1：[需求分析](https://www.baidu.com/s?wd=需求分析&tn=SE_PcZhidaonwhc_ngpagmjz&rsv_dl=gh_pc_zhidao)：分析用户的需求，包括数据、功能和性能需求； 2：概念结构设计：主要采用[E-R模型](https://www.baidu.com/s?wd=E-R模型&tn=SE_PcZhidaonwhc_ngpagmjz&rsv_dl=gh_pc_zhidao)进行设计，包括画E-R图； 3：[逻辑结构设计](https://www.baidu.com/s?wd=逻辑结构设计&tn=SE_PcZhidaonwhc_ngpagmjz&rsv_dl=gh_pc_zhidao)：通过将E-R图转换成表，实现从[E-R模型](https://www.baidu.com/s?wd=E-R模型&tn=SE_PcZhidaonwhc_ngpagmjz&rsv_dl=gh_pc_zhidao)到[关系模型](https://www.baidu.com/s?wd=关系模型&tn=SE_PcZhidaonwhc_ngpagmjz&rsv_dl=gh_pc_zhidao)的转换； 4：[数据库物理设计](https://www.baidu.com/s?wd=数据库物理设计&tn=SE_PcZhidaonwhc_ngpagmjz&rsv_dl=gh_pc_zhidao)：主要是为所设计的数据库选择合适的[存储结构](https://www.baidu.com/s?wd=存储结构&tn=SE_PcZhidaonwhc_ngpagmjz&rsv_dl=gh_pc_zhidao)和存取路径； 5：数据库的实施：包括编程、测试和试运行； 6：数据库运行与维护：系统的运行与数据库的日常维护。） 主要讨论其中的第3个阶段,即[逻辑设计](https://www.baidu.com/s?wd=逻辑设计&tn=SE_PcZhidaonwhc_ngpagmjz&rsv_dl=gh_pc_zhidao)。 逻辑设计主要是建立数据库的逻辑模型，也就是关系数据模型。



![image-20231020160243528](C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231020160243528.png)

A 1.主索引是候选索引的特例，能唯一标识一条记录，只能由一个字段组成。一个表只能建立一个主索引。 2.候选索引也能唯一标识一条记录，但不一定只由一个字段组成，可以由两个或两个以上字段组成，一个表可以建立多个候选索引。 3.普通索引就没有任何限制了，不能唯一标识一条记录，可以任意建立，数量不限。建立普通索引的主要目的是为了加快查询速度和建立表之间的联系。 4.唯一索引已经淘汰不用了，它的唯一性是指索引项的唯一而不是字段值的唯一。



1. **普通索引（Regular Index）**

   - **作用**: 主要用于提高查询速度。
   - **优点**: 因为没有额外的约束，所以创建和维护相对容易。
   - **缺点**: 耗费存储空间，对于插入、删除和更新操作有一定的性能开销。

   2. **唯一索引（Unique Index）**

   - **作用**: 不仅提高查询速度，还保证索引列的唯一性。
   - **优点**: 可以避免重复的记录。
   - **缺点**: 对于插入、删除和更新操作，需要额外检查唯一性，可能有一定性能开销。

   3. **候选索引（Candidate Index）**

   - **作用**: 实质上是唯一索引的一种，但它不是表的主键。也用于提高查询性能和保证数据唯一性。
   - **优点**: 除了查询优化，还为实现某些业务逻辑提供了便利。
   - **缺点**: 类似于唯一索引，需要维护其唯一性，这可能引入额外的性能开销。

   **4. 主索引/主键（Primary Index/Primary Key）**

   - **作用**: 是唯一标识表中每个记录的索引，通常是一个唯一索引，并且不能有NULL值。
   - **优点**: 除了提供高速的随机访问，还可作为其他表（通过外键）与该表关联的逻辑和物理连接点。
   - **缺点**: 由于其唯一性和非NULL的约束，对插入、更新和删除操作有一定的性能开销。