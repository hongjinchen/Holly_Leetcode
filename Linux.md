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

   - 常用选项：

     - `ls -l`: 列出文件和目录的详细信息，包括权限、所有者、大小和最后修改日期。

     - `ls -a`: 列出所有文件和目录，包括隐藏文件（以`.`开头）。
     - `ls -h`: 以易读的格式显示文件大小（例如，`K`, `M`, `G`）。
     - `ls -S`: 按文件大小对输出进行排序。
     - `ls -t`: 按修改时间对输出进行排序，最近修改的文件将排在最前面。

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

   - 该命令列出当前系统中运行的进程，并显示一些关于这些进程的信息。

     **详细解释**

     - `PID`：进程ID。
     - `TTY`：终端类型。
     - `TIME`：该进程占用的CPU时间。
     - `CMD`：该进程正在运行的命令。

     **常用选项**

     - `-e`：列出所有进程。
     - `-f`：全格式列表。

2. **`top`**:

   - 该命令提供一个动态的视图，展示系统的整体状态，包括CPU使用率、内存使用情况、正在运行的进程等。

     **详细解释**

     - CPU使用率：你会看到一个按CPU核心分割的列表，显示每个核心的使用百分比。
     - 内存使用：这里会显示物理内存（RAM）和交换空间（swap）的使用情况。
     - 进程：`top`命令下方列出了正在运行的进程，按照CPU或内存使用量排序。

     **常用选项**

     - `-u [username]`：仅显示指定用户运行的进程。

3. **`df`**:

   - 该命令显示所有挂载的文件系统及其磁盘使用情况。

     **详细解释**

     - `Filesystem`：文件系统的名称。
     - `1K-blocks`：文件系统的总容量（以1K块为单位）。
     - `Used`：已使用的空间（以1K块为单位）。

     **常用选项**

     - `-h`：以易读的方式（G, M, K）显示信息。

4. **`du`**:

   - 功能：估算和显示文件和目录的磁盘使用空间。
   - 常用选项：`-h`，`--max-depth=1`。

5. **`free`**:

   - 功能：显示内存使用情况。
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

- `ps`命令会展示各个进程的进程ID（PID）、父进程ID（PPID）、CPU使用时间、运行状态等信息。

常用选项

- `ps -e`: 列出所有进程。

- `ps -u [username]`: 列出指定用户的所有进程。

  

`top`

动态展示系统状态，包括运行中的进程、CPU和内存使用情况等。

- `top`命令提供一个实时更新的界面，显示所有重要的系统统计信息。

- `top -u [username]`: 仅显示指定用户的进程。

  

`kill`

用于终止或发送信号到一个进程。

- 使用`kill`命令，你可以根据进程ID（PID）来停止进程。

- `kill -9 [PID]`: 强制终止指定PID的进程。

  

### 软件包管理

`apt`

Debian和Ubuntu等基于Debian的系统的软件包管理工具。

- `sudo apt update`: 更新软件包列表。

- `sudo apt install [package_name]`: 安装软件包。

- `sudo apt remove [package_name]`: 卸载软件包。

  

`yum`

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



