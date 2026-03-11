+ 在当前目录中查找所有文件内容是否包含特定内容xxx(深度为1)
```bash
$ find . -maxdepth 1 -type f -exec grep -l "xxx" {} \;
```
