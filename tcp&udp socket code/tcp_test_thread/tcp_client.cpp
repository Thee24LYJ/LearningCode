#include "tcp_client.h"

int main(int argc, char *argv[])
{
	if (argc != 3)
	{
		std::cerr << "Usage: " << argv[0] << "ip  port " << std::endl;
		exit(1);
	}

	std::string ip = argv[1];
	int port = atoi(argv[2]);

	TcpClient *tcl = new TcpClient(ip, port);
	tcl->InitTcpClient();
	tcl->Start();

	delete tcl;
	return 0;
}