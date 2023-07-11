CC=g++
 
.PHONY:all
all:server client
 
server:udp_server.cpp
		$(CC) -o $@ $^ -std=c++11
 
client:udp_client.cpp
		$(CC) -o $@ $^ -std=c++11
 
.PHONY:clean
clean:
		rm -f server client