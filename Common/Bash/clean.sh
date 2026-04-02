#!/bin/bash
# 递归删除指定目录下的编译文件
# 若命令行无参数则默认删除当前目录下的编译文件

set -e  # 遇到错误立即终止

# 定义删除模式
declare -a patterns=("*.o" "*.so" "*.ko" "*.exe" "*.a" "*.out")

# 默认路径为当前目录
path="."

# 检查是否有参数，如果有则使用第一个参数作为路径
if [ $# -ne 0 ]; then
    path="$1"
fi

# 递归删除匹配文件
for p in "${patterns[@]}"; do
    find $path -type f -name "$p" -exec rm -f {} \;
done

# 删除构建目录build
find $path -type d -name "build" -exec rm -rf {} +

# 递归查找当前目录及子目录下的ELF文件并删除
find $path -type f -print0 | while IFS= read -r -d '' file; do
    # 使用file命令检测文件类型，判断是否为ELF文件
    if file --brief "$file" | grep -q 'ELF'; then
        echo "正在删除ELF文件: $file"
        rm -- "$file"    # 删除文件（--防止文件名以-开头导致误判）
    fi
done

echo "所有编译文件已清除"