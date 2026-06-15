#!/bin/csh

# 参考：https://yb.tencent.com/s/Vv5sjDa2qaGP
# 这个脚本演示了如何获取当前路径的basename（最后一部分）。
# 如果在执行过程中遇到"basename: Command not found"的错误，可以取消注释掉设置PATH的行，以确保系统能够找到basename命令。

# 如果执行报错：basename: Command not found.的问题，取消下面这行注释
# setenv PATH "/bin:/usr/bin:/usr/local/bin:$PATH"
# 或者直接使用绝对路径调用basename命令，例如：/usr/bin/basename

### 获取路径的basename
set cur_path = $PWD
echo "cur_path: $cur_path"

# 方法1：使用basename命令
set last_part = `basename $cur_path`
echo "basename (method 1): $last_part"

# 方法2：使用字符串操作
set last_part2 = `echo $cur_path | awk -F/ '{print $NF}'`
echo "basename (method 2): $last_part2"

# 方法3：使用参数扩展
set last_part3 = ${cur_path:t}
echo "basename (method 3): $last_part3"