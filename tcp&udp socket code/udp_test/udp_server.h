#pragma once

#include <iostream>
#include <string>
#include <sys/socket.h>
#include <cstring>
#include <sys/types.h>
#include <arpa/inet.h>

#define DEFAULT 8080
#define SIZE 128

class UdpServer
{
private:
	std::string ip;
	int port;
	int sockfd;

public:
	UdpServer(std::string _ip, int _port = DEFAULT) : ip(_ip), port(_port)
	{
	}

	~UdpServer()
	{
	}

public:
	bool InitUdpServer()
	{
		sockfd = socket(AF_INET, SOCK_DGRAM, 0);
		if (sockfd < 0)
		{
			std::cerr << "socket error" << std::endl;
			return false;
		}

		std::cout << "socket create success, sockfd: " << sockfd << std::endl;

		struct sockaddr_in local; // 创建变量初始化
		memset(&local, '\0', sizeof(local));

		local.sin_family = AF_INET;
		local.sin_port = htons(port); // 主机序列转网络序列 port为端口号
		// local.sin_addr.s_addr = inet_addr(ip.c_str()); // 将点分十进制的IP转化为 整数ip
		local.sin_addr.s_addr = INADDR_ANY; // 接收任意IP发来的消息

		if (bind(sockfd, (struct sockaddr *)&local, sizeof(local)) < 0)
		{
			std::cerr << "bind error" << std::endl;
			return false;
		}
		std::cout << "bind success " << std::endl;

		return true;
	}

	void Start()
	{
		char buffer[SIZE];
		for (;;)
		{
			struct sockaddr_in peer; // 哪一端发送的数据
			socklen_t len = sizeof(peer);
			ssize_t size = recvfrom(sockfd, buffer, sizeof(buffer) - 1, 0, (struct sockaddr *)&peer, &len);

			if (size > 0)
			{
				buffer[size] = 0;
				int _port = ntohs(peer.sin_port);
				std::string _ip = inet_ntoa(peer.sin_addr);
				std::cout << _ip << ":" << _port << "# " << buffer << std::endl;

				std::string echo_msg = "server get -> ";
				echo_msg += buffer;
				sendto(sockfd, echo_msg.c_str(), echo_msg.size(), 0, (struct sockaddr *)&peer, len);
			}
			else
			{
				std::cerr << "recvfrom error!" << std::endl;
			}
		}
	}
};