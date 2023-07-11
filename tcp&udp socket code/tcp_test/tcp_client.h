#pragma once

#include <iostream>
#include <cstring>
#include <string>
#include <unistd.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <sys/types.h>

class TcpClient
{
private:
	std::string svr_ip;
	int svr_port;
	int sock;

public:
	TcpClient(std::string ip, int port) : svr_ip(ip), svr_port(port), sock(-1)
	{
	}

	TcpClient()
	{
		if (sock >= 0)
			close(sock);
	}

public:
	void InitTcpClient()
	{
		sock = socket(AF_INET, SOCK_STREAM, 0);
		if (sock < 0)
		{
			std::cerr << "socket error" << std::endl;
			exit(2);
		}
	}

	void Start()
	{
		struct sockaddr_in peer;
		memset(&peer, 0, sizeof(peer));

		peer.sin_family = AF_INET;
		peer.sin_port = htons(svr_port);
		peer.sin_addr.s_addr = inet_addr(svr_ip.c_str());

		// 发送连接请求
		if (connect(sock, (struct sockaddr *)&peer, sizeof(peer)) == 0)
		{
			// success
			std::cout << "connect success ..." << std::endl;
			Request(sock);
		}
		else
		{
			// faild
			std::cout << "connect failed ..." << std::endl;
		}
	}

	void Request(int sock)
	{
		std::string message;
		char buffer[1024];
		while (true)
		{
			std::cout << "Please Enter# ";
			std::cin >> message;

			write(sock, message.c_str(), message.size());

			ssize_t size = read(sock, buffer, sizeof(buffer) - 1);
			if (size > 0)
			{
				buffer[size] = 0;
			}

			std::cout << "server echo# " << buffer << std::endl;
		}
	}
};