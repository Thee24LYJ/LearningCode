#pragma once

#include <iostream>
#include <sys/socket.h>
#include <cstring>
#include <unistd.h>
#include <sys/types.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/fcntl.h>
#include "threadpool.h"
#include "task.h"

#define DEFALUT 8080
#define BACKLOG 5 // 全连接的最大数量

class TcpServer
{
private:
	int port;
	int listen_sock;
	ThreadPool<Task> *tp;

public:
	TcpServer(int _port = DEFALUT) : port(_port), listen_sock(-1), tp(nullptr)
	{
	}
	~TcpServer()
	{
		if (listen_sock >= 0)
			close(listen_sock);
		delete tp;
	}

public:
	void InitTcpServer()
	{
		listen_sock = socket(AF_INET, SOCK_STREAM, 0);
		if (listen_sock < 0)
		{
			std::cerr << "socket error" << std::endl;
			exit(2);
		}

		struct sockaddr_in local;
		memset(&local, 0, sizeof(local));
		local.sin_family = AF_INET;
		local.sin_port = htons(port);
		local.sin_addr.s_addr = INADDR_ANY;

		if (bind(listen_sock, (struct sockaddr *)&local, sizeof(local)) < 0)
		{
			std::cerr << "bind error" << std::endl;
			exit(3);
		}

		if (listen(listen_sock, BACKLOG) < 0)
		{
			std::cerr << "listen error" << std::endl;
			exit(4);
		}

		tp = new ThreadPool<Task>();
	}

	void Start()
	{
		tp->InitTheadPool();
		struct sockaddr_in peer;
		for (;;)
		{
			socklen_t len = sizeof(peer);
			int sock = accept(listen_sock, (struct sockaddr *)&peer, &len);
			if (sock < 0)
			{
				std::cout << "accept error, continue next" << std::endl;
				continue;
			}
			std::string ip = inet_ntoa(peer.sin_addr);
			int port = ntohs(peer.sin_port);
			Task t(sock, ip, port);
			tp->Push(t);
		}
	}
};