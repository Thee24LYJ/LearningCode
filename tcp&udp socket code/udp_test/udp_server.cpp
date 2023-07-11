#include "udp_server.h"

int main(int argc, char *argv[])
{
	if (argc != 2)
	{
		std::cout << "Usage: " << argv[0] << " port " << std::endl;
		return 1;
	}

	std::string ip = "127.0.0.1";
	int port = atoi(argv[1]); // 字符串转化为整数

	UdpServer *svr = new UdpServer(ip, port);
	svr->InitUdpServer();
	svr->Start();

	return 0;
}