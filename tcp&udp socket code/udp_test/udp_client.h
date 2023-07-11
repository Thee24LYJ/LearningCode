#pragma once

#include <iostream>
#include <string>
#include <sys/types.h>
#include <arpa/inet.h>
#include <cstring>

class UdpClient
{
private:
	std::string ip;
	int port;
	int sockfd;

public:
	UdpClient(std::string _ip, int _port) : ip(_ip), port(_port)
	{
	}

	~UdpClient()
	{
	}

public:
	bool InitUdpClient()
	{
		sockfd = socket(AF_INET, SOCK_DGRAM, 0);
		if (sockfd < 0)
		{
			std::cerr << "socket error!" << std::endl;
			return false;
		}

		// 客户端不需要port? 客户端不需要绑定?
		return true;
	}

	void Start()
	{
		struct sockaddr_in peer; // 往哪发
		memset(&peer, 0, sizeof(peer));

		peer.sin_family = AF_INET;
		peer.sin_port = htons(port);
		// peer.sin_addr.s_addr = inet_addr(ip.c_str()); // 点分十进制转整形
		peer.sin_addr.s_addr = INADDR_ANY; // 接收任意IP发来的消息

		std::string msg;
		for (;;)
		{
			std::cout << "Please Enter# ";
			std::cin >> msg;
			sendto(sockfd, msg.c_str(), msg.size(), 0, (struct sockaddr *)&peer, sizeof(peer));

			char buffer[128];
			struct sockaddr_in temp;
			socklen_t len = sizeof(temp);
			ssize_t size = recvfrom(sockfd, buffer, sizeof(buffer) - 1, 0, (struct sockaddr *)&temp, &len);
			if (size > 0)
			{
				buffer[size] = 0;
				std::string _ip = inet_ntoa(temp.sin_addr);
				int _port = ntohs(temp.sin_port);
				std::cout << _ip << ":" << _port << "# " << buffer << std::endl;
			}
		}
	}
};