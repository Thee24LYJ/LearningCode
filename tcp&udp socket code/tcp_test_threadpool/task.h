#pragma once

#include <iostream>
#include <string>
#include <unistd.h>
#include <unordered_map>

class Handler
{
public:
	Handler() {}
	void operator()(int sock, std::string ip, int port)
	{
		// for test
		std::unordered_map<std::string, std::string> dict;
		dict.insert({"apple", "苹果"});
		dict.insert({"banana", "香蕉"});
		dict.insert({"boy", "男孩"});
		dict.insert({"MIUI", "小米"});

		char buffer[1024];
		std::string value;
		while (true)
		{
			ssize_t size = read(sock, buffer, sizeof(buffer) - 1);
			if (size > 0)
			{
				buffer[size] = 0;
				std::cout << ip << ":" << port << "# " << buffer << std::endl;

				std::string key = buffer;
				auto iter = dict.find(key);
				if (iter != dict.end())
				{
					value = iter->second;
				}
				else
				{
					value = buffer;
				}

				write(sock, value.c_str(), value.size());
			}
			else if (size == 0)
			{
				std::cout << ip << ":" << port << " close!" << std::endl;
				break;
			}
			else
			{
				std::cerr << sock << " read error" << std::endl;
				break;
			}
		}
		std::cout << "service done" << std::endl;
		close(sock);
	}
	~Handler() {}
};

class Task
{
private:
	int sock;
	std::string ip;
	int port;
	Handler handler;

public:
	Task() {}
	Task(int _sock, std::string _ip, int _port)
		: sock(_sock), ip(_ip), port(_port)
	{
	}
	void Run()
	{
		handler(sock, ip, port);
	}

	~Task()
	{
	}
};