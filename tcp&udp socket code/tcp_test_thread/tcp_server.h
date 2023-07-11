#pragma once

// 多线程

#include <iostream>
#include <sys/socket.h>
#include <cstring>
#include <unistd.h>
#include <sys/types.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/fcntl.h>
#include <sys/wait.h>
#include <pthread.h>

#define DEFALUT 8080
#define BACKLOG 5

// 用于传递fd、ip和port给对应线程
// 应该也可以使用结构体
class Prama
{ // 存储参数
public:
	std::string ip;
	int port;
	int sock;

public:
	Prama(std::string _ip, int _port, int _sock)
		: ip(_ip), port(_port), sock(_sock)
	{
	}

	~Prama()
	{
	}
};

class TcpServer
{
private:
	int port;
	int lsock; // listen socket

public:
	TcpServer(int _port = DEFALUT) : port(_port), lsock(-1)
	{
	}
	~TcpServer()
	{
		if (lsock >= 0)
			close(lsock);
	}

public:
	void InitTcpServer()
	{
		lsock = socket(AF_INET, SOCK_STREAM, 0);
		if (lsock < 0)
		{
			std::cerr << "socket error!" << std::endl;
			exit(1);
		}

		struct sockaddr_in local;
		memset(&local, 0, sizeof(local));
		local.sin_family = AF_INET;
		local.sin_port = htons(port);
		local.sin_addr.s_addr = htonl(INADDR_ANY);

		if (bind(lsock, (struct sockaddr *)&local, sizeof(local)) < 0)
		{
			std::cerr << "bind error!" << std::endl;
			exit(2);
		}

		if (listen(lsock, BACKLOG) < 0)
		{
			std::cerr << "listen error!" << std::endl;
			exit(3);
		}
	}

	// 静态成员函数
	static void *routine(void *arg)
	{
		Prama *p = (Prama *)arg;
		pthread_detach(pthread_self());

		Service(p->sock, p->ip, p->port);
		close(p->port);
		delete p;

		return nullptr;
	}

	void Start()
	{
		struct sockaddr_in peer;
		for (;;)
		{
			socklen_t len = sizeof(peer);
			int sock = accept(lsock, (struct sockaddr *)&peer, &len);
			if (sock < 0)
			{
				std::cout << "accept error ,continue next" << std::endl;
				continue;
			}

			pthread_t tid;
			std::string _ip = inet_ntoa(peer.sin_addr);
			int _port = ntohs(peer.sin_port);

			Prama *p = new Prama(_ip, _port, sock);
			pthread_create(&tid, nullptr, routine, (void *)p);
		}
	}

	// 静态成员函数
	static void Service(int sock, std::string ip, int port)
	{
		char buffer[1024];
		while (true)
		{
			ssize_t size = read(sock, buffer, sizeof(buffer) - 1);
			if (size > 0)
			{
				buffer[size] = 0;
				std::cout << ip << ":" << port << "# " << buffer << std::endl;

				write(sock, buffer, size);
			}
			else if (size == 0)
			{
				std::cout << ip << ":" << port << " close!" << std::endl;
				break;
			}
			else
			{
				std::cerr << sock << " read error " << std::endl;
				break;
			}
		}

		close(sock); // fd也是一种资源是有限的
		std::cout << "service done!" << std::endl;
	}
};