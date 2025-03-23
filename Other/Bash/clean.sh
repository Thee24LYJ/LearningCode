#!/bin/bash
# 递归删除当前目录及子目录的编译文件

set -e  # 遇到错误立即终止

# 定义删除模式
declare -a patterns=("*.o" "*.so" "*.ko" "*.exe" "*.a")

# 递归删除匹配文件
for p in "${patterns[@]}"; do
    find . -type f -name "$p" -exec rm -f {} \;
done

# 删除构建目录build
find . -type d -name "build" -exec rm -rf {} +

# 递归查找当前目录及子目录下的ELF文件并删除
find . -type f -print0 | while IFS= read -r -d '' file; do
    # 使用file命令检测文件类型，判断是否为ELF文件
    if file --brief "$file" | grep -q 'ELF'; then
        echo "正在删除ELF文件: $file"
        rm -- "$file"    # 删除文件（--防止文件名以-开头导致误判）
    fi
done

echo "所有编译文件已清除"