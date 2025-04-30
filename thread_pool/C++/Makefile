# 添加自定义变量
CC=g++
# 使用函数搜索当前目录下的源文件 .cpp
src=$(wildcard *.cpp)
# 将源文件的后缀替换为 .o
obj=$(patsubst %.cpp, %.o, $(src))

target=main

$(target):$(obj)
	$(CC) $(obj) -o $(target)

%.o:%.cpp
	$(CC) $< -c

# 添加规则, 删除生成文件 *.o 可执行程序
# 声明clean为伪文件
.PHONY:clean
clean:
    # shell命令前的 - 表示强制这个指令执行, 如果执行失败也不会终止
	-rm $(obj) $(target)