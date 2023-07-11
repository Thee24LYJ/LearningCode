#include "tcp_server.h"

int main(int argc, char *argv[])
{
	if (argc != 2)
	{
		std::cout << "Usage: " << argv[0] << " port" << std::endl;
		return 1;
	}

	int port = atoi(argv[1]);

	TcpServer *tsv = new TcpServer(port);
	tsv->InitTcpServer();
	tsv->Start();

	delete tsv;
	return 0;
}