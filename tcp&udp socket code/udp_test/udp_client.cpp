#include "udp_client.h"

int main(int argc, char *argv[])
{
	if (argc != 3)
	{
		std::cout << "Usage: " << argv[0] << " ip port " << std::endl;
		return 1;
	}

	std::string ip = argv[1];
	int port = atoi(argv[2]);

	UdpClient *ucli = new UdpClient(ip, port);
	ucli->InitUdpClient();

	ucli->Start();
}