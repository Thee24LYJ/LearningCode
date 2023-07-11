CC=g++
 
.PHONY:all
all:server client
 
server:tcp_server.cpp
		$(CC) -o $@ $^ -std=c++11 -l pthread
 
client:tcp_client.cpp
		$(CC) -o $@ $^ -std=c++11 -l pthread
 
.PHONY:clean
clean:
		rm -f server client