# 只保留文件前1000行的内容
```bash
# 删除第1001行到文件末尾的所有内容
$ sed -i '1001,$ d'
```
# 递归查找特定后缀且大于100MB的文件
```bash
$ find . -type f -name "*.后缀" -size +100M
# 使用-ls显示对应文件的详细信息
$ find . -type f -name "*.后缀" -size +100M -ls
```
