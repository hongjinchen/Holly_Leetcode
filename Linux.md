# Linux系统结构和基础

## 了解Unix/Linux哲学

1. **什么是Linux**：Linux 是一个开源的 Unix-like 操作系统内核。它由 Linus Torvalds 在1991年首次发布。Linux 的优点包括稳定性、性能、多用户支持、多任务、强大的网络功能以及硬件支持。

2. **与Unix的关系**：Linux 是 Unix 的一个克隆版本，旨在提供与 Unix 相似的功能和兼容性，但它并不是由 Unix 代码库派生出来的。Linux 继承了 Unix 的设计哲学和部分用户空间的接口。

3. **与其他操作系统的关系**：与像 Windows 这样的商业操作系统相比，Linux 更加开放和自由。它的源代码可以被任何人查看、修改和重新分发。

4. **基本哲学**：Unix 和 Linux 都遵循“做一件事，做好”的哲学。这意味着每个程序或命令应当只完成一个特定的任务，但要做得尽可能好。

   

## 文件系统和目录结构

在 Linux 中，所有的内容都是以文件的形式组织的，这些文件按照一个预定的目录结构进行排列。

1. **`/`（根目录）**：这是文件系统的起点，所有的目录和文件都是从这里开始的。
2. **`/home`**：这个目录通常用于存放用户数据。每个用户都有一个在 `/home` 下的子目录，通常名为 `/home/username`。
3. **`/etc`**：这个目录用于存放系统范围内的配置文件和子目录。这里的文件主要由系统管理员进行编辑。
4. **`/usr`**：这个目录用于存放用户可用的标准应用程序和文件。例如，`/usr/bin` 包含了大量的二进制文件（命令），`/usr/lib` 包含库文件。

其他常见目录：

- **`/bin`**：存放基本命令二进制文件，这些命令在单用户模式下也需要使用。
- **`/sbin`**：存放一些只有系统管理员通常会用到的命令。
- **`/var`**：用于存放经常变化的文件，如日志文件和数据库。
- **`/tmp`**：用于存放临时文件，这些文件在系统重启时通常会被删除。



## 常见操作

1. **Shell使用**：熟悉命令行界面，学习使用基础的shell命令。

2. **文件操作**：`ls`, `cd`, `cp`, `mv`, `rm`, `mkdir`等。

3. **文本操作**：`cat`, `echo`, `grep`, `sed`, `awk`等。

4. **权限和所有权**：`chmod`, `chown`, `sudo`等。

   

### 文件和目录操作

1. **`ls`**:

   - 功能：列出目录中的文件和子目录。
  ![alt text](image-54.png)

   - **常用选项**：

     - `ls -l`: 列出文件和目录的详细信息，包括权限、所有者、大小和最后修改日期。

     - `ls -a`: 列出所有文件和目录，包括隐藏文件（以`.`开头）。

     - `ls -h`: 以易读的格式显示文件大小（例如，`K`, `M`, `G`）。

     - `ls -S`: 按文件大小对输出进行排序。

     - `ls -t`: 按修改时间对输出进行排序，最近修改ls的文件将排在最前面。

       

   - 例子：`ls -la` 会以长格式列出所有文件，包括隐藏文件。

     - ls - al

       ```
       drwxr-xr-x  10 user  user  4096 Oct 19 09:00 .
       drwxr-xr-x  12 user  user  4096 Oct 18 12:34 ..
       -rw-------   1 user  user     5 Oct 19 09:00 .bash_history
       -rw-r--r--   1 user  user   220 Oct 17 13:39 .bash_logout
       ```

     在Linux和Unix系统中，`drwxr-xr-x` 用于描述文件类型和文件权限。

     - **第一个字符代表文件类型**：
       - `d` 表示这是一个目录。
       - `-` 表示这是一个普通文件。
       - 其他可能的字符包括 `l`（符号链接）、`s`（套接字）、`p`（命名管道）等。
     - **接下来的9个字符代表文件权限**，这9个字符被分为三组，每组3个字符：
       - 第一组（字符2-4）：拥有者权限
         - `rwx` 分别代表读（Read）、写（Write）、执行（Execute）权限。
       - 第二组（字符5-7）：组权限
         - `r-x` 表示该组用户具有读和执行权限，但没有写权限。
       - 第三组（字符8-10）：其他用户权限
         - `r-x` 表示其他用户具有读和执行权限，但没有写权限。

     每一组中的 `r`、`w` 和 `x` 可以分别被替换为 `-`，代表相应的权限没有被赋予。例如，`rw-` 表示具有读和写权限，但没有执行权限。

     综合以上信息，`drwxr-xr-x` 表示：

     - 这是一个目录（`d`）。
     
     - 文件/目录拥有者有读、写和执行权限（`rwx`）。
     
     - 与文件/目录关联的组只有读和执行权限（`r-x`）。
     
     - 所有其他用户也只有读和执行权限（`r-x`）。
     
       

2. **`cd`**:

   - 功能：更改当前工作目录。

   - 例子：`cd Documents` 会切换到当前用户目录下的 `Documents` 文件夹。

     

3. **`pwd`**:

   - 功能：显示当前工作目录的完整路径。
![alt text](image-55.png)
     

4. **`cp`**:

   - 功能：复制文件或目录。

   - 常用选项：`-r`（递归复制目录和其内容）。

   - 例子：`cp -r source_folder destination_folder`。

     

5. **`mv`**:

   - 功能：移动或重命名文件或目录。

   - 例子：`mv old_name new_name` 会将 `old_name` 重命名为 `new_name`。

     

6. **`rm`**:

   - 功能：删除文件或目录。

   - 常用选项：`-r`（递归删除目录和其内容）。

   - 例子：`rm -r folder_name` 会删除 `folder_name` 及其所有内容。

     

7. **`mkdir`**:

   - 功能：创建新目录。

   - 例子：`mkdir new_folder` 会在当前目录下创建一个名为 `new_folder` 的新目录。

     

8. **`rmdir`**:

   - 功能：删除空目录。
   
   - 例子：`rmdir folder_name` 会删除一个名为 `folder_name` 的空目录。
   
     

### 文本操作

1. **`cat`**:

   - 功能：显示文件的全部内容。

   - 例子：`cat file.txt` 会输出 `file.txt` 的所有内容。

     

2. **`echo`**:

   - 功能：输出文本或变量。

   - 例子：`echo "Hello, World!"` 会输出 "Hello, World!"。

     

3. **`more` 和 `less`**:

   - 功能：分页查看文件内容。

   - 在 `more` 或 `less` 界面，可以使用 `space` 翻页，`q` 退出。

   - 语法

     - `more [options] [file]`
     - `less [options] [file]`

     例子

     - `more file.txt`：分页显示`file.txt`的内容。
     - `less file.txt`：以可滚动的方式分页显示`file.txt`的内容。

   

4. **`grep`**:

   - 功能：搜索特定模式。

   - 常用选项：`-i`（忽略大小写），`-r`（递归搜索）。

   - 例子：`grep -i "hello" file.txt` 会在 `file.txt` 中进行不区分大小写的搜索。

     

5. **`sed`**:

   - 功能：流编辑器。

   - 例子：`sed 's/apple/orange/g' file.txt` 会将 `file.txt` 中的所有“apple”替换为“orange”。

     

6. **`awk`**:

   - 功能：文本和数据提取和报告工具。

   - 例子：`awk '{print $1}' file.txt` 会打印 `file.txt` 中的每一行的第一个字段。

     

### 权限和所有权

1. **`chmod`**:

   - 功能：更改文件权限。

   - ```
     chmod [options] mode[,mode] file1 [file2 ...]
     ```

   - 例子：`chmod 755 file.txt` 会设置 `file.txt` 的权限为 `755`（即 `rwxr-xr-x`）。

     假如您运行 `chmod 755 file.txt`：

     - 这会将 `file.txt` 的权限设置为 `755`。

     - 在**八进制表示法**中，

       ```
       755
       ```

        对应于 

       ```
       rwxr-xr-x
       ```

       。

       - `r`（读）的数值是 4
       - `w`（写）的数值是 2
       - `x`（执行）的数值是 1

     - 所以 

       ```
       755
       ```

        表示：

       - 所有者（Owner）拥有读、写、执行（`rwx`，即 `7`）的权限。
       - 所属组（Group）拥有读和执行（`r-x`，即 `5`）的权限。
       - 其他人（Others）拥有读和执行（`r-x`，即 `5`）的权限。

   

2. **`chown`**:

   - 功能：更改文件或目录的所有者和组。

   - ```
     chown [options] [owner][:group] file1 [file2 ...]
     ```

   - 例子：`chown username:groupname file.txt`。

     假如您运行 `chown username:groupname file.txt`：

     这会将 `file.txt` 的所有者更改为 `username`，并将所属组更改为 `groupname`。

   

3. **`sudo`**:

   - 功能：以超级用户（root）权限运行命令。

   - ```
     sudo [options] command [arguments ...]
     ```

   - 例子：`sudo apt update` 会以超级用户权限更新软件包列表。



### 系统和进程信息

1. **`ps`**:

   - 该命令**列出当前系统中运行的进程，并显示一些关于这些进程的信息。**
![alt text](image-56.png)
     **详细解释**

     - `PID`：进程ID。
     - `TTY`：终端类型。
     - `TIME`：该进程占用的CPU时间。
     - `CMD`：该进程正在运行的命令。

     **常用选项**

     - `-e`：列出所有进程。
     
     - `-f`：全格式列表。
     
       

2. **`top`**:

   - 该命令提供一个**动态的视图**，展示**系统的整体状态**，包括**CPU使用率、内存使用情况、正在运行的进程等**。
  ![alt text](image-57.png)

     **详细解释**

     - CPU使用率：你会看到一个按CPU核心分割的列表，显示每个核心的使用百分比。
     - 内存使用：这里会显示物理内存（RAM）和交换空间（swap）的使用情况。
     - 进程：`top`命令下方列出了正在运行的进程，按照CPU或内存使用量排序。

     **常用选项**

     - `-u [username]`：仅显示指定用户运行的进程。
     
       

1. **`df`**:

   - 该命令显示**所有挂载的文件系统及其磁盘使用情况**。

![alt text](image-58.png)
     **详细解释**

     - `Filesystem`：文件系统的名称。
     - `1K-blocks`：文件系统的总容量（以1K块为单位）。
     - `Used`：已使用的空间（以1K块为单位）。

     **常用选项**

     - `-h`：以易读的方式（G, M, K）显示信息。
     
       

4. **`du`**:

   - 功能：**估算和显示文件和目录的磁盘使用空间**。

   - 常用选项：`-h`，`--max-depth=1`。
![alt text](image-59.png)
     

5. **`free`**:

   - 功能：**显示内存使用情况**。

   - 常用选项：`-m`（以 MB 为单位显示）。

     

6. **`uptime`**:

   - #### 功能

     该命令显示系统已经运行了多长时间，以及系统的负载等。

     #### 详细解释

     - 输出格式一般为：`当前时间，系统运行时间，当前用户数，负载`
     
       

## 系统管理

1. **进程管理**：了解`ps`, `top`, `kill`等命令。
2. **软件包管理**：如何使用`apt`, `yum`或其他包管理器安装、更新、删除软件。
3. **系统服务管理**：了解`systemd`或`init.d`，使用`systemctl`等命令来管理服务。

 

### 进程管理

`ps`

列出当前运行的进程及其相关信息。

- `ps`命令会展示**各个进程的进程ID（PID）**、父进程ID（PPID）、CPU使用时间、运行状态等信息。

常用选项

- `ps -e`: 列出所有进程。

- `ps -u [username]`: 列出指定用户的所有进程。

  

`top`

动态展示系统状态，包括运行中的进程、CPU和内存使用情况等。

- `top`命令提供一个实时更新的界面，显示所有重要的系统统计信息。

- `top -u [username]`: 仅显示指定用户的进程。

  

`kill`

用于**终止或发送信号到一个进程。**

- 使用`kill`命令，你可以根据进程ID（**PID**）来停止进程。

- `kill -9 [PID]`: 强制终止指定PID的进程。

  

### 软件包管理

**`apt`**

Debian和Ubuntu等基于Debian的系统的软件包管理工具。

- `sudo apt update`: 更新软件包列表。

- `sudo apt install [package_name]`: 安装软件包。

- `sudo apt remove [package_name]`: 卸载软件包。

  

**`yum`**

Red Hat, CentOS等基于RPM的系统的软件包管理工具。

- `sudo yum update`: 更新所有软件包。

- `sudo yum install [package_name]`: 安装软件包。

- `sudo yum remove [package_name]`: 卸载软件包。

  

### 系统服务管理

`systemd`

现代Linux发行版中用于初始化系统和管理系统服务的工具。

**`systemctl` 常用命令**

- `sudo systemctl start [service_name]`: 启动服务。

- `sudo systemctl stop [service_name]`: 停止服务。

- `sudo systemctl enable [service_name]`: 开机自启动服务。

- `sudo systemctl disable [service_name]`: 禁止开机自启动服务。

  

`init.d`

早期的Linux发行版使用的系统和服务管理工具。

- `/etc/init.d/[service_name] start`: 启动服务。

- `/etc/init.d/[service_name] stop`: 停止服务。

  

## 网络操作

1. **基础网络命令**：`ping`, `ssh`, `scp`, `curl`等。
2. **防火墙和端口**：了解`iptables`或`ufw`等。

| 命令         | 功能                   | 详细解释                            | 常用选项                         |
| ------------ | ---------------------- | ----------------------------------- | -------------------------------- |
| **ping**     | 测试与网络主机的连通性 | 发送ICMP回显请求到目标主机          | `ping -c [count] [hostname]`     |
| **ssh**      | 远程登录到另一台计算机 | 通过安全的网络协议访问另一台主机    | `ssh [username]@[hostname]`      |
| **scp**      | 安全地传输文件         | 使用SSH协议进行安全的数据传输       | `scp [source] [destination]`     |
| **curl**     | 通过URL协议传输数据    | 支持多种类型的协议，包括HTTP、FTP等 | `curl -O [URL]`                  |
| **iptables** | 配置Linux内核防火墙    | 定义防火墙规则，控制进出的网络流量  | `iptables -L`                    |
| **ufw**      | 友好的防火墙配置工具   | 简化`iptables`的配置                | `ufw enable`, `ufw allow [port]` |


## 查看系统信息

uname: 显示系统信息。
![alt text](image-60.png)

lscpu: 显示CPU架构信息，如CPU类型、核数、架构等。
![alt text](image-61.png)

free: 显示内存使用情况。
![alt text](image-62.png)

vmstat: 报告虚拟内存统计。
![alt text](image-63.png)

iostat: 监视系统输入输出设备和CPU的使用情况。


# 操作系统

### 批处理操作系统（Batch Processing Operating System）

**主要特点：**

- 高效率：优化 CPU 和 I/O 操作

- 无用户交互：作业自动执行

- 作业调度：使用调度算法选择待执行作业

  

**应用场景：**

- 数据分析

- 文件转换

- 后端处理（如数据库备份）

  

**示例：**

- 早期的 IBM OS/360

- UNIX 系统中的 batch commands

  

批处理操作系统（Batch Processing Operating System）是一种用于执行批处理任务的操作系统。在这种系统中，作业（也称为任务或程序）通常被组织成一个队列，并按照一定的顺序一一执行。这种方式尤其适用于需要长时间运行并且不需要用户交互的作业。

主要特点：

1. **无需用户交互**：一旦作业被提交到队列，系统会自动进行处理，不需要用户干预。
2. **高效率**：由于作业是批量执行的，所以可以优化 CPU 和 I/O 操作，以提高系统的总体效率。
3. **作业调度**：批处理系统通常具有复杂的作业调度算法，以确定何时和如何执行队列中的作业。
4. **资源优化**：系统可以根据需要来优化资源分配，例如，通过将需要相似资源的作业组织在一起执行。

工作流程：

1. **作业提交**：用户或其他系统将作业提交到一个作业队列。
2. **作业调度**：操作系统的调度器从队列中选取作业进行执行。
3. **执行**：选中的作业被加载到内存中并执行。
4. **输出处理**：作业执行完成后，输出结果通常会被保存到存储设备中。
5. **作业完成**：一旦所有作业都被执行完，批处理操作通常就会结束。

示例应用场景：

1. **数据分析**：大规模数据集的分析通常不需要实时交互，可以通过批处理进行。
2. **文件转换**：将一种文件格式批量转换为另一种文件格式。
3. **后端处理**：如数据库的备份和恢复，日志分析等。
4. **科学计算**：进行大量计算而不需要用户交互的场景。
5. **打印作业**：在早期的计算机系统中，批处理操作系统常用于管理打印队列。

由于没有实时用户交互，批处理操作系统通常不具备图形用户界面（GUI），而是通过命令行接口（CLI）或通过其他系统进行操作。



#### 单道批处理 (Single-Stream Batch Processing)

在单道批处理系统中，一次只执行一个作业或任务。系统将完成一个作业后才开始执行下一个作业。这种方式简单易理解，但由于任何时候都只有一个作业在执行，系统资源（如CPU、内存等）的利用率相对较低。

#### 多道批处理 (Multi-Stream Batch Processing)

多道批处理系统是单道批处理系统的扩展，它允许多个作业同时在系统中处于不同的执行阶段（例如，一个作业在执行，另一个作业在等待磁盘I/O，另一个作业在等待CPU等）。这样，当一个作业等待I/O操作完成时，CPU可以被另一个作业使用，从而提高系统资源的利用率。



### 分时操作系统（Time-Sharing Operating System）

**主要特点：**

- 多用户支持：支持多终端并发访问
- 交互式：用户可以实时与系统交互
- 资源共享：CPU、内存和其他资源被多个用户共享

**应用场景：**

- 在线编程
- 数据库查询
- 多用户应用和游戏

**示例：**

- UNIX

- Early versions of Multics

  

分时操作系统（Time-Sharing Operating System）是一种多用户操作系统，它允许多个用户通过终端同时访问和使用计算机资源。这是通过将 CPU 时间和其他系统资源分割成非常短的时间片段，并将这些时间片段轮流分配给各个用户或任务，从而实现多用户或多任务的并发执行。

**主要特点：**

1. **多用户支持**：分时操作系统支持多个用户通过不同的终端设备进行并发访问。
2. **响应时间**：系统旨在提供足够短的响应时间，即使在多用户环境下也能给用户一种“实时”使用的感觉。
3. **资源共享**：多个用户或任务可以共享相同的计算机资源，如 CPU、内存、存储和输入/输出设备。
4. **交互式使用**：与批处理系统不同，分时操作系统通常具有交互式用户界面，允许用户实时输入命令并接收反馈。
5. **作业调度和多任务**：通过复杂的调度算法，系统能够合理地分配 CPU 时间和其他资源。
6. **优先级和配额**：系统通常支持为不同的用户或任务设置不同的优先级和资源配额。

**工作原理：**

1. **任务调度**：操作系统的调度器使用某种算法（如轮转调度、优先级调度等）来决定哪个用户或任务应当获得 CPU 时间。
2. **上下文切换**：当一个任务的时间片用完或被其他更高优先级的任务抢占时，系统会保存当前任务的状态，并加载下一个任务的状态，以便在稍后恢复执行。
3. **用户交互**：用户通过终端与系统进行交互，输入命令并获取输出结果。
4. **资源管理**：分时操作系统会跟踪和管理系统资源的使用，以确保公平和高效地分配给各个用户和任务。

**示例应用场景：**

1. **在线编辑和编程**：多个程序员可以通过分时操作系统同时访问同一个系统进行开发。
2. **数据库系统**：多个用户可以同时查询和修改数据库。
3. **多用户游戏和应用**：分时操作系统可以支持多用户在线游戏或其他交互应用。
4. **远程访问和维护**：系统管理员可以远程登录到分时操作系统进行维护。



### 实时操作系统（Real-Time Operating System, RTOS）

**主要特点：**

- 确定性：能在预定时间内完成特定任务
- 可靠性：对系统响应时间有严格要求
- 任务调度：使用实时调度算法

**应用场景：**

- 嵌入式系统
- 工业自动化
- 航空航天

**示例：**

- QNX

- VxWorks

- FreeRTOS

  

### 分布式操作系统（Distributed Operating System）

**主要特点：**

- 资源共享：多台机器的资源能够被共享
- 扩展性：可以容易地添加更多的机器
- 高可用性：一个节点的故障通常不会导致整个系统崩溃

**应用场景：**

- 大规模数据处理
- 网络服务
- 高性能计算

**示例：**

- Apache Hadoop

- Google's Borg

  

### 移动操作系统（Mobile Operating System）

**主要特点：**

- 用户友好：触摸屏操作，易用界面
- 资源受限：对 CPU、内存和电池有限制
- 应用生态：拥有大量第三方应用

**应用场景：**

- 智能手机
- 平板电脑

**示例：**

- Android
- iOS



# Git

### 初始化和配置

1. **`git init`**：在当前目录下初始化一个新的 Git 仓库。
2. **`git config`**: 用于设置 Git 配置信息。

### 克隆和远程操作

1. **`git clone [url]`**：克隆（复制）一个远程仓库到本地。
2. **`git remote`**: 用于管理远程仓库。
3. **`git fetch`**: 获取远程仓库的最新版本，但不合并。
4. **`git pull`**: 获取并合并远程仓库的最新版本。

### 文件和状态操作

1. **`git status`**: 显示工作目录和暂存区的状态。
2. **`git add [file]`**: 将文件添加到暂存区。
3. **`git rm [file]`**: 从版本控制中移除文件。

### 提交和历史

1. **`git commit`**: 提交暂存区的文件。
2. **`git log`**: 查看提交历史。
3. **`git revert`**: 回滚到之前的提交。

### 分支和标签

1. **`git branch`**: 列出、创建或删除分支。
2. **`git checkout [branch]`**: 切换到指定分支。
3. **`git merge [branch]`**: 将指定分支合并到当前分支。
4. **`git tag`**: 用于操作标签。

### 其他

1. **`git stash`**: 临时保存当前的修改。
2. **`git reset`**: 重置当前分支到某个状态。
3. **`git diff`**: 查看文件差异。

