

# MySQL

## **数据库事务的特性**

**原子性（Atomicity）**

原子性确保事务被视为一个单一的“不可分割”的工作单位，即事务内的操作要么全部完成，要么全部不做。如果事务中的一部分操作失败，整个事务将被回滚（撤销），以保证数据库状态的一致性。

例如，假设一个事务涉及将一个银行账户的资金转移到另一个账户。这个操作包含两个步骤：从第一个账户扣款和向第二个账户存款。原子性会确保这两个操作要么都完成，要么都不做。

**一致性（Consistency）**

一致性确保事务从一个一致的状态导致另一个一致的状态。一致性不仅仅是原子性的问题，它还包括确保数据的完整性约束（例如，唯一性、外键约束等）得到满足。

在事务开始和结束时，数据库应处于一致状态。这意味着所有规则和约束必须得到满足。继续上面的银行账户示例，一致性会确保转账后两个账户的总金额与转账前相同。

**隔离性（Isolation）**

多个事务可能会并发地执行。隔离性确保每个事务在执行时，其操作对其他事务是不可见的，即一个事务的中间状态不应该被其他事务看到。这是通过各种锁机制和时间戳来实现的。

数据库系统通常提供不同级别的隔离，包括读未提交（Read Uncommitted）、读已提交（Read Committed）、可重复读（Repeatable Read）和串行化（Serializable）。

> **1. 读未提交（Read Uncommitted）**
>
> - **定义**：在这个级别中，一个事务可以读取另一个未提交事务的数据。
> - **问题**：这是最低的隔离级别，会导致很多问题，如脏读（Dirty Reads），即一个事务读取到另一个未完成事务的数据。
> - **应用场景**：几乎不用，除非在特定场景下，对数据一致性的要求极低。
>
> **2. 读已提交（Read Committed）**
>
> - **定义**：在这个级别中，一个事务只能读取已经被其他事务提交的数据。
> - **问题**：虽然解决了脏读的问题，但是还是有其它问题，比如不可重复读（Non-repeatable Reads），即在同一个事务里，多次读取同一数据返回的结果有可能不同。
> - **应用场景**：适用于对数据一致性要求不是很高，但又不希望出现脏读的情况。
>
> **3. 可重复读（Repeatable Read）**
>
> - **定义**：这个级别确保在同一个事务中多次读取同一数据会得到相同的结果。
> - **问题**：这个级别解决了不可重复读的问题，但是还可能出现幻读（Phantom Reads），即在一个事务内读取某个范围内的记录时，另一个事务插入了一个新的记录，使得同一查询产生不同结果。
> - **应用场景**：适用于业务逻辑复杂，需要多次读取同一数据的情况。
>
> **4. 串行化（Serializable）**
>
> - **定义**：这是最高的隔离级别。在这个级别，事务序列化顺序执行，不能并发执行。
> - **问题**：由于事务不能并发执行，因此会对系统性能造成很大影响。
> - **应用场景**：只有在对数据一致性要求极高的系统中才需要使用这个级别。



**持久性（Durability）**

持久性确保一旦事务被提交，其对数据库的更改就是永久性的，即使在系统崩溃或故障后也不会丢失。

通常，这是通过将事务日志持久化到磁盘来实现的。在系统恢复后，这些日志用于将数据库恢复到一致的状态。



## SQL 语法

### 数据库

**1. 查看现有数据库**

```text
SHOW DATABASES;
```

**2. 新建数据库**

```text
CREATE DATABASE <数据库名>;
```

**3. 选择数据库**

```text
USE <数据库名>;
```

**4. 从`.sql`文件引入SQL语句**

```text
SOURCE <.sql文件路径>;
```

**5. 删除数据库**

```text
DROP DATABASE <数据库名>;
```

### 表

**6. 查看当前数据库中的表**

```text
SHOW TABLES;
```

![img](https://pic4.zhimg.com/80/v2-d7ddbd8950efe4a2a320f4684fa03c6f_1440w.webp)

**7. 创建新表**

```text
CREATE TABLE <表名> (
    <列名1> <列类型1>,
    <列名2> <列类型2>,
    <列名3> <列类型3>,
    PRIMARY KEY (<列名1>),
    FOREIGN KEY (<列名2>) REFERENCES <表名2>(<列名2>)
);
```

主键（`PRIMARY KEY`）用来标识一条记录（一行），所以每条记录的主键值必须是唯一的。主键可以定义在多列上，这称为**联合主键（composite primary key）**。

如果我们把表视作具有某种结构的数组（例如，C语言中的struct），那么外键（`FOREIGN KEY`）可以视作指针。

例子：

```text
CREATE TABLE instructor (
    ID CHAR(5),
    name VARCHAR(20) NOT NULL,
    dept_name VARCHAR(20),
    salary NUMERIC(8,2), 
    PRIMARY KEY (ID),
    FOREIGN KEY (dept_name) REFERENCES department(dept_name));
```

在上面的例子中，我们创建了一个教员（`instructor`）表，该表的主键是ID，外键是教员所在的部门名称（`dept_name`），关联部门（`department`）表。此外，教员表还包括姓名（`name`）、薪水（`salary`）。其中，姓名有约束`NOT NULL`，表示姓名这一项不能为空。

**8. 概述表中的列**

使用如下语句查看表中的列的基本信息：

```text
DESCRIBE <表名>;
```

下图显示了一些例子：

![img](https://pic2.zhimg.com/80/v2-23727505d367e44a9c4d56d8df1f7509_1440w.webp)

**9. 在表中插入新纪录**

```text
INSERT INTO <表名> (<列名1>, <列名2>, <列名3>, …)
    VALUES (<值1>, <值2>, <值3>, …);
```

也可以省略列名（依序在所有列上插入新值）：

```text
INSERT INTO <表名>
    VALUES (<值1>, <值2>, <值3>, …);
```

**10. 在表中更新记录**

```text
UPDATE <表名>
    SET <列名1> = <值1>, <列名2> = <值2>, ...
    WHERE <条件>;
```

**11. 清空表**

```text
DELETE FROM <表名>;
```

**12. 删除表**

```text
DROP TABLE <表名>;
```



### 查询

**13. SELECT**

**SELECT**语句可以从表中选择数据：

```text
SELECT <列名1>, <列名2>, …
    FROM <表名>;
```

以下语句选择所有内容：

```text
SELECT * FROM <表名>;
```

![img](https://pic3.zhimg.com/80/v2-7c3f80ef110ed423ae4fdbe53efe2726_1440w.webp)

选中department表和course表中的所有内容

**14. SELECT DISTINCT**

**SELECT DISTINCT**过滤掉了重复的值：

```text
SELECT DISTINCT <列名1>, <列名2>, …
    FROM <表名>;
```

![img](https://pic2.zhimg.com/80/v2-637855a8cc50ae2ca4c52b90e537cde1_1440w.webp)

**15. WHERE**

我们之前在更新记录时已经用到了**WHERE**关键字，用来指明条件。这里我们稍微详细一点地介绍下**WHERE**。

**WHERE**的条件通常是：

- 比较**文本（text）**
- 比较**数字（numbers）**
- **AND**、**OR**、**NOT**等逻辑运算

让我们来看一些例子：

```text
SELECT * FROM course WHERE dept_name='Comp. Sci.';
SELECT * FROM course WHERE credits>3;
SELECT * FROM course WHERE dept_name='Comp. Sci.' AND credits>3;
```

![img](https://pic4.zhimg.com/80/v2-ba65cae91c8a07113428dc700a77350b_1440w.webp)

**16. GROUP BY**

**GROUP BY**语句可以分组结果，常用于**COUNT**、**MAX**、**MIN**、**SUM**、**AVG**等**聚合函数（aggregate functions）**。

```text
SELECT <列名1>, <列名2>, …
    FROM <表名>
    GROUP BY <列名>;
```

让我们来看一个例子，列出每个部门的课程数量：

```text
SELECT COUNT(course_id), dept_name 
     FROM course 
     GROUP BY dept_name;
```

![img](https://pic2.zhimg.com/80/v2-b98b02a2e727819e0bb393dd39ea6609_1440w.webp)

**17. HAVING**

乍看起来，**HAVING**和**WHERE**很像：

```text
SELECT <列名1>, <列名2>, …
    FROM <表名>
    GROUP BY <列名x>
    HAVING <条件>;
```

那么，**HAVING**和**WHERE**有什么不同呢？让我们先来看一个例子，列出开了不止一门课程的部门开设的课程数：

```text
SELECT COUNT(course_id), dept_name 
    FROM course 
    GROUP BY dept_name 
    HAVING COUNT(course_id)>1;
```

这里**HAVING**不能换成**WHERE**，因为**WHERE**直接针对行操作，且在**GROUP BY**之前运行（即先通过**WHERE**筛选行，之后再将筛选出的行通过**GROUP BY**分组）。假设SQL中不存在**HAVING**语句，那么我们只能先新建一张表，将`COUNT(course_id)`作为新表的列，然后在新表上再通过**WHERE**进行筛选（当然，实际上SQL提供了派生表、CTE等机制，并不用真的手工建新表）。

![img](https://pic4.zhimg.com/80/v2-9822a7cdbae57d65986b8760be362e63_1440w.webp)

**18. ORDER BY**

**ORDER BY**可以对结果进行排序，在没有明确指定**ASC**（升序）或**DESC**（降序）的情况下，默认按升序排列。

```text
SELECT <列名1>, <列名2>, …
FROM <表名>
ORDER BY <列名1>, <列名2>, …, ASC|DESC;
```

例子：

```text
SELECT * FROM course ORDER BY credits;
SELECT * FROM course ORDER BY credits DESC;
```

![img](https://pic2.zhimg.com/80/v2-6671d510a7597957436428001436d695_1440w.webp)

**19. BETWEEN**

**BETWEEN**语句用于**指定区间**。

```text
SELECT <列名1>, <列名2>, …
    FROM <表名>
    WHERE <列名x> BETWEEN <值1> AND <值2>;
```

其中“值”可能是数字，文本，乃至日期等。

例如，列出薪资在50000和100000之间的教员：

```text
SELECT * FROM instructor 
    WHERE salary BETWEEN 50000 AND 100000;
```

![img](https://pic2.zhimg.com/80/v2-67fd4e97bdbac7493f10d0cea8270ba1_1440w.webp)

**20. LIKE**

**LIKE**用于匹配**文本中的特定模式**。

```text
SELECT <列名1>, <列名2>, …
    FROM <表名>
    WHERE <列名x> LIKE <模式>;
```

模式中可以使用以下两个通配符：

- `%` （零个、一个或多个字符）
- `_` （单个字符）

例子：列出课程名中包含“to”的课程，以及课程ID以“CS-”开头的课程。

```text
SELECT * FROM course WHERE title LIKE '%to%';
SELECT * FROM course WHERE course_id LIKE 'CS-___';
```

![img](https://pic4.zhimg.com/80/v2-b79387e250a3df16e27e6046e4256b6b_1440w.webp)

**21. IN**

**IN**语句表示值属于某个集合。

```text
SELECT <列名1>, <列名2>, …
    FROM <表名>
    WHERE <列名n> IN (<值1>, <值2>, …);
```

例子：列出计算机科学、物理、电子工程部门的学生。

```text
SELECT * FROM student 
    WHERE dept_name IN ('Comp. Sci.', 'Physics', 'Elec. Eng.');
```

![img](https://pic4.zhimg.com/80/v2-e3aa7ceab577f85e8f1b0676f2ec45af_1440w.webp)

**22. JOIN**

**JOIN**用来组合两张以上表中的值。下图展示了**JOIN**的三种类型：



![img](https://pic3.zhimg.com/80/v2-f3f027a8b81ed884d5e77a4e989cb44e_1440w.webp)

```text
SELECT <列名1>, <列名2>, …
    FROM <表名1>
    JOIN <表名2>
    ON <表名1.列名x> = <表名2.列名x>
```

让我们来看三个例子，分别对应三种**JOIN**的类型。

第一个例子，列出课程时包含开设课程的部门详情：

```text
SELECT * FROM course 
    JOIN department 
    ON course.dept_name=department.dept_name;
```

![img](https://pic4.zhimg.com/80/v2-29c046ddedee80e2fc617ff411e68503_1440w.webp)

第二个例子，列出所有具有前置课程的课程的详情：

```text
SELECT prereq.course_id, title, dept_name, credits, prereq_id 
    FROM prereq 
    LEFT OUTER JOIN course 
    ON prereq.course_id=course.course_id;
```

![img](https://pic3.zhimg.com/80/v2-8b5cca57797228d0cd5d132bc66aa2fa_1440w.webp)

最后一个例子，列出所有课程的详情，不管是否具有前置课程：

```text
SELECT course.course_id, title, dept_name, credits, prereq_id 
    FROM prereq 
    RIGHT OUTER JOIN course 
    ON prereq.course_id=course.course_id;
```

![img](https://pic3.zhimg.com/80/v2-4ca21be6eb7f2009ab3789554d4026ca_1440w.webp)

**23. 视图**

视图（view）是虚拟的SQL表。它包含行和列，和一般的SQL表格很类似。视图总是显示数据库中的最新数据。

**CREATE VIEW**

创建视图：

```text
CREATE VIEW <视图名> AS
    SELECT <列名1>, <列名2>, …
    FROM <表名>
    WHERE <条件>;
```

**DROP VIEW**

删除视图：

```text
DROP VIEW <视图名>;
```

例如，创建3学分的课程视图：

```text
CREATE VIEW my_view AS
    SELECT * FROM course
    WHERE credits=3;
```

![img](https://pic4.zhimg.com/80/v2-3581a7722415db9e97590892ef8452af_1440w.webp)

**24. 聚合函数**

我们之前已经提到聚合函数，这里列出最常用的一些聚合函数：

- **COUNT(列名)** 返回行数

- **SUM(列名)** 返回指定列的值之和

- **AVG(列名)** 返回指定列的平均值

- **MIN(列名)** 返回指定列的最小值

- **MAX(列名)** 返回指定列的最大值

  

**25. 嵌套子查询**

在SQL请求中，可以嵌套**SELECT-FROM-WHERE**表达式，称为**嵌套子查询（nested subqueries）**。

例如，查找2009年秋、2010年春都开的课程：

```text
SELECT DISTINCT course_id 
    FROM section 
    WHERE semester = ‘Fall’ AND year= 2009 AND course_id IN (
        SELECT course_id 
            FROM section 
            WHERE semester = ‘Spring’ AND year= 2010
    );
```

![img](https://pic1.zhimg.com/80/v2-e70916f1c617bafc28d1f2ab68e936a4_1440w.webp)

https://www.runoob.com/sql/sql-select.html



### **数据库左连接和右连接的区别**

**左连接（LEFT JOIN）**

- **基本思路**：左连接会返回左表（left table）中的所有记录和右表（right table）中匹配的记录。如果没有找到匹配的记录，则右表中的列会包含`NULL`。

**右连接（RIGHT JOIN）**

- **基本思路**：右连接会返回右表（right table）中的所有记录和左表（left table）中匹配的记录。如果没有找到匹配的记录，则左表的列会包含`NULL`。

  

**SQL，“在一列数据中，找出存在重复的数据”**

```
SELECT my_column, COUNT(*)
FROM my_table
GROUP BY my_column
HAVING COUNT(*) > 1;
```



### 优化 MySQL 指令

优化 MySQL 指令（SQL 语句）是数据库性能优化的一个重要环节。优化的目标主要是减少查询时间、减少系统负载以及提高并发处理能力。下面列举了一些常见的优化手段：

#### 索引优化

1. **使用合适的索引**：根据查询模式选择合适的列来创建索引。
2. **避免全表扫描**：尽量让查询走索引而非进行全表扫描。

#### SQL 语句优化

1. **选择适当的字段**：仅查询你需要的字段，避免 `SELECT *`。
2. **减少子查询和临时表的使用**：尽可能使用 JOIN 操作。
3. **使用 LIMIT**：如果只需要部分数据，使用 LIMIT 来限制返回结果的数量。

#### 数据库设计优化

1. **数据规范化**：避免数据冗余。
2. **合理的数据类型**：例如，如果一个字段存储年龄，使用 TINYINT 类型而非 INT。

#### 查询优化

1. **使用 `EXPLAIN` 分析查询**：通过解释计划来查看 MySQL 是如何执行查询的，以找出需要优化的地方。
2. **避免使用 `LIKE` 的前置通配符**：这样会导致 MySQL 不能有效地使用索引。

#### 其他优化

1. **批量插入**：一次插入多行数据，减少单次操作的开销。
2. **避免使用锁表操作**：例如，尽量使用 InnoDB 存储引擎以支持行级锁定。
3. **调整配置参数**：例如，可以调整缓存大小以适应工作负载。



#### 示例

假设有一个查询，原始版本如下：

```
SELECT * FROM employees WHERE age > 25 AND age < 50;
```

优化后：

```
SELECT id, name, age FROM employees WHERE age BETWEEN 26 AND 49;
```

在这个简单的例子中，我们只选择了需要的字段，并且使用 `BETWEEN` 代替了两个逻辑操作，这样可以更有效地使用索引（如果有的话）。



#### **Index**

在 MySQL 中，索引（Index）是一种数据结构，用于提高数据检索的速度。索引可以被认为是一种“快速查找表”，它包含一个指向数据表中每一行数据的指针。使用索引可以大大减少数据查找所需的时间，尤其是在大型数据集中。

**常见类型的索引**

1. **单列索引**：一个索引覆盖单个列。
2. **复合索引**：一个索引覆盖多个列。
3. **唯一索引**：不允许索引列中有重复值。
4. **主键索引**：是一种特殊的唯一索引，不允许有 NULL 值。
5. **全文索引**：用于全文搜索。
6. **空间索引**：用于地理数据存储。



**如何创建索引**

创建表时添加索引

```sql
CREATE TABLE students (
    id INT NOT NULL,
    name VARCHAR(50),
    age INT,
    PRIMARY KEY (id),
    INDEX (name)
);
```

在这个例子中，`id` 列是主键索引，`name` 列有一个单列索引。



**在已存在的表上添加索引**

1. **添加单列索引**

   ```sql
   ALTER TABLE students ADD INDEX index_name (name);
   ```

   或者

   ```sql
   CREATE INDEX index_name ON students(name);
   ```

2. **添加复合索引**

   ```
   ALTER TABLE students ADD INDEX index_name (name, age);
   ```

   或者

   ```
   CREATE INDEX index_name ON students(name, age);
   ```

3. **添加唯一索引**

   ```
   ALTER TABLE students ADD UNIQUE (email);
   ```

   或者

   ```
   CREATE UNIQUE INDEX index_name ON students(email);
   ```

4. **添加全文索引**

   ```
   ALTER TABLE articles ADD FULLTEXT (title, content);
   ```

   或者

   ```
   CREATE FULLTEXT INDEX index_name ON articles(title, content);
   ```

**注意事项**

1. **性能**：虽然索引可以加快检索速度，但创建和维护索引也需要时间和存储空间。每当你插入、更新或删除一行，索引也需要更新。

2. **选择性**：具有高选择性（唯一值多）的列通常是创建索引的好候选。

3. **查询优化**：需要根据实际的查询需求来设计索引，例如，WHERE 子句中经常用到的列，排序操作中使用的列等。

4. **复合索引的列顺序**：在复合索引中，列的顺序会影响到索引的效率。

5. **索引覆盖**：如果一个查询只用到了索引中的信息，而没有去访问数据行，它可以直接从索引中获取信息，这通常会更快。

   

**索引的结构，为什么用B+树不用B树**

索引是数据库中用于提高数据检索效率的数据结构。在很多现代数据库管理系统（DBMS）中，B+树是最常用的索引结构。尽管B+树和B树有很多相似之处，但还是有几个关键差异使得B+树更适合作为数据库索引。

**B树与B+树的结构特点：**

**B树：**

1. **多路搜索树**: B树是一种自平衡的多路搜索树。
2. **所有节点存储键值**: 在B树中，所有的节点（包括内部节点和叶子节点）都可以存储数据（键和可能的相关值）。
3. **递归分割**: 节点分裂是递归进行的，也就是说，如果一个节点分裂并导致其父节点也需要分裂，则该过程会一直递归进行，直到不再需要分裂。

**B+树：**

1. **多路搜索树**: B+树也是一种自平衡的多路搜索树。
2. **仅叶子节点存储数据**: 在B+树中，所有的数据都存储在叶子节点，内部节点仅用于路由。
3. **所有叶子节点通过指针相连**: 这一点有助于范围查询。

**为什么使用B+树而不是B树？**

1. **范围查询更高效**: 因为所有叶子节点都是通过指针相互连接的，所以范围查询可以更快地执行。在B树中执行范围查询则需要更多的磁盘I/O操作。

2. **更少的磁盘I/O**: 在B+树中，内部节点不存储数据，这意味着每个内部节点可以存储更多的键，从而减少了树的高度，进一步减少了磁盘I/O。

3. **数据访问更加均匀**: 因为B+树的所有数据都存储在叶子节点，数据访问（尤其是随机访问）更加均匀，没有“热点”问题。

4. **插入和删除简化**: 在B+树中，插入和删除只会影响叶子节点，因此算法相对更简单。而在B树中，插入和删除可能需要更多的节点变动和数据移动。

5. **更适合磁盘或持久存储**: B+树通常更高（因为每个节点有更多的子节点），这意味着需要更少的磁盘读操作，这在大多数数据库应用场景中是一个优势。

   

#### 关系型数据库（RDBMS）

1. **表格存储**：数据存储在表中，表和表之间可能有关系。常见的关系型数据库包括MySQL, PostgreSQL, SQLite, Oracle等。

#### 非关系型数据库（NoSQL）

1. **键值存储（Key-Value）**：如Redis, Amazon DynamoDB。适用于需要快速查找的简单数据。
2. **文档存储（Document-Oriented）**：如MongoDB, Couchbase。适用于JSON、XML等文档型的数据存储。
3. **列式存储（Column-Family Stores）**：如Cassandra, HBase。适用于大数据和实时分析。
4. **图形数据库（Graph Databases）**：如Neo4j, Amazon Neptune。适用于存储网络、社交网络、组织结构等复杂关系的数据。

**其他**

1. **对象存储**：用于存储复杂对象和其关系，例如Java的对象数据库。

2. **文件存储（File-based storage）**：例如CSV, XML文件，通常用于简单的应用或数据交换。

3. **内存数据库（In-memory databases）**：如Redis、Memcached，用于需要高速读写的场景。

4. **分布式数据库**：如CockroachDB、Google Spanner，用于确保数据分布在多个地点或集群上。

   

## 真题

**SQL中，下面对于数据定义语言DDL描述正确的是（）**

A DDL关心的是数据库中的数据

B 联盟链

C 控制对数据库的访问

D 定义数据库的结构



D

（1）**数据定义**（SQL **DDL**）用于定义SQL模式、基本表、视图和索引的创建和撤消操作。

数据定义一般涉及到数据库模式的创建、修改和删除。在SQL中，常用的数据定义语言（DDL）指令包括 `CREATE`, `ALTER`, 和 `DROP`。

（2）**数据操纵**（SQL **DML**）数据操纵分成数据查询和数据更新两类。数据更新又分成插入、删除、和修改三种操作。

数据操纵主要涉及数据的增加、删除、修改和查询。在SQL中，常用的数据操纵语言（DML）指令包括 `INSERT`, `DELETE`, `UPDATE`, 和 `SELECT`。

（3）**数据控制**（DCL）包括对基本表和视图的授权，完整性规则的描述，事务控制等内容。

数据控制涉及权限和数据安全性的管理。在SQL中，常用的数据控制语言（DCL）指令包括 `GRANT` 和 `REVOKE`。

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



**DROP**

`DROP` 是一种数据定义语言（DDL）命令，用于永久删除数据库对象（如表、索引、视图、序列等）。一旦执行 `DROP` 命令，被删除的对象以及其中的所有数据将无法恢复。

- **删除表**

  ```
  sqlCopy code
  DROP TABLE Students;
  ```

- **删除索引**

  ```
  sqlCopy code
  DROP INDEX index_name;
  ```

**TRUNCATE**

`TRUNCATE` 也是一种DDL命令，用于删除表中的所有行，但不删除表本身或其结构。与 `DELETE` 命令不同，`TRUNCATE` 通常不能被回滚（取决于数据库系统），并且不会触发任何 DELETE 触发器。

- **清空表中的所有数据**

  ```
  sqlCopy code
  TRUNCATE TABLE Students;
  ```

**DELETE**

`DELETE` 是一种数据操纵语言（DML）命令，用于从表中删除数据。与 `TRUNCATE` 命令不同，`DELETE` 命令可以有条件地删除数据，并且可以触发 DELETE 触发器。执行 `DELETE` 命令后，可以使用 `ROLLBACK` 命令来撤销删除。

- **删除所有数据**

  ```
  sqlCopy code
  DELETE FROM Students;
  ```

- **有条件地删除数据**

  ```
  sqlCopy code
  DELETE FROM Students WHERE Age < 18;
  ```

**对比**

- **DROP**: 永久删除整个数据库对象。

- **TRUNCATE**: 删除表中的所有数据，但保留表结构。

- **DELETE**: 可以有条件地删除表中的数据。

  

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

- EmployeeID→Name
- EmployeeID→Department
- EmployeeID→Salary

**属性：**

1. **自反性**: 如果 B 是 A 的子集，那么 *A*→*B*。

2. **增广性**: 如果 *A*→*B*，那么 *A*∪*C*→*B*∪*C*，其中 C 是任意属性集。

3. **传递性**: 如果 *A*→*B* 和 *B*→*C*，那么 *A*→*C*。

   

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

通常分为6个阶段 

1：[需求分析](https://www.baidu.com/s?wd=需求分析&tn=SE_PcZhidaonwhc_ngpagmjz&rsv_dl=gh_pc_zhidao)：分析用户的需求，包括数据、功能和性能需求； 

2：概念结构设计：主要采用[E-R模型](https://www.baidu.com/s?wd=E-R模型&tn=SE_PcZhidaonwhc_ngpagmjz&rsv_dl=gh_pc_zhidao)进行设计，包括画E-R图； 

3：[逻辑结构设计](https://www.baidu.com/s?wd=逻辑结构设计&tn=SE_PcZhidaonwhc_ngpagmjz&rsv_dl=gh_pc_zhidao)：通过将E-R图转换成表，实现从[E-R模型](https://www.baidu.com/s?wd=E-R模型&tn=SE_PcZhidaonwhc_ngpagmjz&rsv_dl=gh_pc_zhidao)到[关系模型](https://www.baidu.com/s?wd=关系模型&tn=SE_PcZhidaonwhc_ngpagmjz&rsv_dl=gh_pc_zhidao)的转换； 

4：[数据库物理设计](https://www.baidu.com/s?wd=数据库物理设计&tn=SE_PcZhidaonwhc_ngpagmjz&rsv_dl=gh_pc_zhidao)：主要是为所设计的数据库选择合适的[存储结构](https://www.baidu.com/s?wd=存储结构&tn=SE_PcZhidaonwhc_ngpagmjz&rsv_dl=gh_pc_zhidao)和存取路径； 

5：数据库的实施：包括编程、测试和试运行； 

6：数据库运行与维护：系统的运行与数据库的日常维护。） 主要讨论其中的第3个阶段,即[逻辑设计](https://www.baidu.com/s?wd=逻辑设计&tn=SE_PcZhidaonwhc_ngpagmjz&rsv_dl=gh_pc_zhidao)。 逻辑设计主要是建立数据库的逻辑模型，也就是关系数据模型。



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



![image-20231021162138764](C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231021162138764.png)

数据库中的封锁机制主要是为了实现并发控制。当多个用户或者进程同时访问数据库时，封锁机制确保了数据的一致性和完整性。通过对数据项加锁，系统可以防止多个事务同时修改同一数据项，从而避免数据不一致的问题。

并发控制机制通常包括两类锁：

1. 共享锁（Shared Lock）：允许多个事务读取同一数据项但不允许任何事务进行写操作。
2. 排他锁（Exclusive Lock）：允许一个事务对数据项进行读取和写入，但不允许其他任何事务访问该数据项。

![image-20231021162256481](C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231021162256481.png)

在Microsoft Access数据库中，"向导"（Wizard）不是通常认为的Access对象。常见的Access对象包括：

1. 表（Tables）：存储数据的主要结构。
2. 查询（Queries）：用于从表中检索数据。
3. 窗体（Forms）：用于数据输入和显示。
4. 报表（Reports）：用于数据的打印和展示。
5. 宏（Macros）和模块（Modules）：用于编写自动化代码。

向导是一种用户界面工具，用于帮助用户完成特定任务，如创建表、查询、窗体等，但它们自身不存储在数据库中作为一个“对象”。



![image-20231021162813302](C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231021162813302.png)

数据独立性是指应用程序与数据之间的解耦，即应用程序不需要直接和数据的物理结构或存储细节打交道。这样，当底层数据发生变化时，上层的应用程序不需要做相应的修改。在数据库系统中，数据独立性主要通过三级模式结构来实现。

**三级模式结构**

1. **外模式（用户视图）**: 针对特定用户或应用程序的数据视图。
2. **概念模式（全局视图）**: 数据库的整体逻辑视图，独立于任何具体的物理细节。
3. **内模式（物理模式）**: 描述数据在存储介质中如何存储的细节。

应用程序主要与外模式和概念模式交互，而不是直接与内模式交互。这样，即使底层的数据存储细节发生变化（例如，表的物理结构，存储方式等），应用程序也无需修改。



![image-20231021163043550](C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231021163043550.png)



<img src="C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231021164524171.png" alt="image-20231021164524171" style="zoom: 50%;" />

R 表有一个 A 列，S 表有一个 D 列。S 表中的 A 列有一个外键约束，它引用 R 表中的 A 列，并带有 "ON DELETE NO ACTION" 选项。

"ON DELETE NO ACTION" 意味着，如果你尝试删除主键表（在这种情况下是 R 表）中的一行，并且该行的主键值被另一个表（S 表）的外键值引用，则将阻止删除操作。

现在，我们评估每一个 SQL 语句：

A) DELETE FROM R WHERE A=2: 这会尝试删除 R 表中 A=2 的行。查看 S 表，有一行其 D 列的值为 e1 且 A 列的值为 2。由于 "ON DELETE NO ACTION" 约束，因为 S 表引用了该值，所以这个删除操作将被阻止。

B) DELETE FROM R WHERE A=3: 这会尝试删除 R 表中 A=3 的行。在 S 表中没有任何行引用这个 A 列的值。因此，此操作将成功。

C) DELETE FROM S WHERE A=1: 这将删除 S 表中 A 列值为 1 的行。这不违反任何约束，操作将成功。

D) DELETE FROM S WHERE A=2: 这将删除 S 表中 A 列值为 2 的行。这不违反任何约束，操作将成功。



![image-20231021164737373](C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231021164737373.png)

A) RDBMS: 关系数据库管理系统，例如 MySQL, PostgreSQL, Oracle 等。

B) NoSQL: 非关系型数据库，例如 MongoDB, Redis, Cassandra 等。

D) NewSQL: 是一种新型的关系数据库管理系统，旨在提供传统 RDBMS 所提供的 ACID 兼容性，同时还能实现NoSQL 样式的水平可扩展性。

F) HBase: 是一个开源的、分布式的、版本化的、非关系型的数据库。



![image-20231021182243642](C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231021182243642.png)

1. **层次模型**（Hierarchical Model）: 这种模型将数据组织成树形结构，其中每个记录只有一个父记录，但可以有多个子记录。IBM的 IMS 数据库是基于这种模型的一个例子。

2. **网状模型**（Network Model）: 这种模型允许每个记录有多个父记录和多个子记录，形成一个图形结构。CODASYL DBTG（Database Task Group）定义了这种模型。

3. **关系模型**（Relational Model）: 在这种模型中，数据被组织成表（或称为关系），每个表由行（记录）和列（字段）组成。这种模型的主要特点是它的数学基础和简洁性。现在大多数商业数据库（如 Oracle, MySQL, PostgreSQL）都基于关系模型。

4. **实体-关系模型**（Entity-Relationship Model，ER Model）: 这是一种高级数据模型，用于数据库的设计阶段。它使用实体、属性和关系来描述现实世界中的数据。

5. **面向对象数据模型**（Object-Oriented Model）: 这种模型将数据看作对象，对象中可以包含数据（属性）和方法（函数）。面向对象的数据库如 ObjectStore 和 O2 是基于这种模型的。

6. **对象关系模型**（Object-Relational Model）: 这种模型结合了关系模型和面向对象模型的特点，允许在表中存储对象和引用其他对象。例如，PostgreSQL 就支持一些对象关系特性。

7. **NoSQL模型**：这是一组不同的数据模型，不同于传统的关系模型。其中包括键-值存储、列式存储、文档存储和图形数据库等。

   

![image-20231021182345621](C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231021182345621.png)

 数据库设计通常分为6个阶段 

  1需求分析：分析用户的需求，包括数据、功能和性能需求； 

  2概念结构设计：主要采用E-R模型进行设计，包括画E-R图； 

  3逻辑结构设计：通过将E-R图转换成表，实现从E-R模型到关系模型的转换； 

  4数据库物理设计：主要是为所设计的数据库选择合适的存储结构和存取路径； 

  5数据库的实施：包括编程、测试和试运行；6数据库运行与维护：系统的运行与数据库的日常维护。



![image-20231021182425177](C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231021182425177.png)

这个问题是关于两个表 `R` 和 `S` 的自然连接（natural join）。自然连接基于两个表中所有具有相同名称的列进行连接操作。

让我们逐步分析这两个表的自然连接：

1. 表 `R` 和 `S` 都有列 `A`, `B`, 和 `C`，因此我们将基于这三个列进行自然连接。

2. 对于 `R` 表中的每一行，我们将查找 `S` 表中具有相同 `A`, `B`, 和 `C` 列值的行。

   a. 对于 `R` 的第一行 (a1, b2, c1)，在 `S` 中找不到匹配的行。 b. 对于 `R` 的第二行 (a2, b2, c2)，在 `S` 中有一个匹配的行，即 (a2, b2, c2, g)。 c. 对于 `R` 的第三行 (a3, b1, c1)，在 `S` 中也找不到匹配的行。

所以，根据上述分析，`R` 和 `S` 的自然连接结果只有1行。因此，正确答案是 **D) 1**。



![image-20231021182559281](C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231021182559281.png)



![image-20231021230921133](C:\Users\hongj\AppData\Roaming\Typora\typora-user-images\image-20231021230921133.png)



# 关系模型（Relational Model）

![img](https://pic3.zhimg.com/v2-a2200fb58d53cb486e0f16f8be624f0e_r.jpg)

关系模型（Relational Model）是一种用于管理和组织数据的高级抽象模型。

**DBMS 采用某种数据模型进行建模**，提供了在计算机中表示数据的方式，其包括，**数据结构、数据操作、数据完整性**三部分。在关系模型中**，通过关系表示实体与实体之间的联系**，然后**基于关系数据集合进行数据的查询、更新以及控制**等操作同时**对数据的更新操作进行实体完整性、参照完整性、用户自定义完整性约束**。而在前期，通过关系代数和逻辑方式（关系演算）表示对关系操作的能力，而后出现了 **SQL 语言**，其吸纳了关系代数的概念，和关系演算的逻辑思想

## 基本概念 

**Relation（关系）**

在关系模型中，一个关系（或称为表）是数据的基础单位。关系是由一系列有相同属性（Attribute）的元组（Tuple）组成的。这里的“元组”就是数据库表中的一行，而“属性”则是表中的一列。

例如，考虑一个简单的“学生”关系，其中可能有如下元组：

- (1, 'Alice', 20)
- (2, 'Bob', 21)
- (3, 'Charlie', 22)

每个元组表示一个学生的信息：学号、姓名和年龄。

**Attribute（属性）**

属性是用来描述元组特性的列。在上面的“学生”关系例子中，“学号”、“姓名”和“年龄”就是属性。每个属性都有一个预定义的数据类型（如整数、字符串等）。

**Tuple（元组）**

元组（或记录）是关系中的一个实例。在“学生”关系中，每个元组都是一个特定的学生。一个元组的每个属性都有一个值，这个值是从该属性的域（Domain）中选取的。

**Domain（域）**

域是一个属性可能取值的集合。例如，在上面的“学生”关系中，“学号”的域可能是所有正整数，“姓名”的域可能是所有有效的字符串，“年龄”的域可能是 0 到 150 的整数。

在数据库实现中，域的定义通常涉及到数据类型和可能的约束。例如，一个年龄属性可能被定义为非负整数，且不能超过 150。

**Key（键）**

键是用于唯一标识元组的属性集合。在关系模型中，有多种类型的键：

- **主键（Primary Key）**: 是唯一标识一个元组的属性集合。一个关系只能有一个主键。例如，在“学生”关系中，“学号”可以是主键。
- **候选键（Candidate Key）**: 除了主键之外，还可以唯一标识元组的其他键。
- **外键（Foreign Key）**: 是在一个关系中用于引用另一个关系的主键或候选键的属性集合。外键用于建立关系之间的连接。
- **复合键（Composite Key）**: 是由两个或更多的属性组成的键。

## 实体之间的关系

**一对一（1:1）关系**

在一对一关系中，一个实体A的每一个实例与实体B的一个实例相关，反之亦然。例如，在一个人口数据库中，“身份证”和“人”之间就可能有一对一的关系。

**一对多（1:N）关系**

在一对多关系中，实体A的一个实例可以与实体B的多个实例相关，但实体B的一个实例只能与实体A的一个实例相关。例如，在一个学校数据库中，“老师”和“课程”之间就可能有一对多的关系。

**多对多（M:N）关系**

在多对多关系中，实体A的一个实例可以与实体B的多个实例相关，反之亦然。例如，在一个图书馆数据库中，“读者”和“书籍”之间就可能有多对多的关系。

在关系数据库中，这些不同类型的实体关系通常通过使用“外键”（Foreign Key）来实现。外键是一个或多个字段（即属性或列），它用于在一个表（关系）中引用另一个表（关系）的主键（Primary Key）。

**关系表示例：**

以“学生”和“课程”为例，他们之间可能存在多对多的关系，通常可以通过一个中间表（也称为“连接表”或“关系表”）来表示。

- 学生表（Student）
  - StudentID（主键）
  - Name
- 课程表（Course）
  - CourseID（主键）
  - CourseName
- 学生-课程关系表（Student_Course）
  - StudentID（外键）
  - CourseID（外键）

这样，一个学生可以选多门课，而一门课也可以被多个学生选。关系表中的每一行都表示一个学生与一门课之间的关系。