#!/bin/bash

# 指定WiFi名称
wifi_name="UESTC-WiFi"
# 获取所有WiFi信息
wifi_info=`nmcli dev wifi`

#echo $wifi_info

result=$(echo $wifi_info | grep "${wifi_name}")
if [[ "$result" != "" ]]
then	# 存在该WiFi则进行连接，否则报错
	echo `nmcli dev wifi connect $wifi_name`
else
	echo "$wifi_name does not exist!"
fi
