#!/bin/bash

#判断是否有参数
if [ x$1 != x ] #带参数
then
        source_dir=$1   #源文件夹
        backup_dir=$2   #备份文件夹
else    #没有参数
        source_dir="/home/lyj/TG_ERQI_230227LYJ"
        backup_dir="/home/lyj/backup"
fi

temp="/home/lyj/backup_folder"

#创建一个临时文件（要保存备份的路径）
mkdir -p $temp

#备份数据到backup_folder目录下，先将数据拷过来
cp -r $source_dir $temp

#删除项目编译文件
rm -rf $temp/TG_ERQI_230227LYJ/ZLToolKit-master/linux_build

#备份文件名
backup_file="$backup_dir/TG_ERQI_LYJ_$(date +%Y%m%d).tar.gz"

#将数据所在文件夹backup_folder打包
tar -zcPvf $backup_file  $temp/$source_dir > $backup_dir/backup.log 2>&1

#删除临时文件内容
rm -rf $temp

#输出备份完成的消息
echo "Backup complete:$backup_file"

#删除该文件夹下超过30天的文件
#find ./ -mtime +30 -name "*.tar.gz" -exec rm -rf {} ;