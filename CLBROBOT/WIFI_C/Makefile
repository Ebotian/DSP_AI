INCLUDEPATH=/home/pi/CLBROBOT/wifi_c/
CFLAGS=-lwiringPi \
-lwiringPiDev \
-lm \
-Wall -Og\
-I$(INCLUDEPATH)

car_server: LOBOROBOT.o car_server.o
	gcc $(CFLAGS) -o car_server car_server.o LOBOROBOT.o

car_server.o: car_server.c LOBOROBOT.h globals.h
	gcc $(CFLAGS) -c car_server.c

LOBOROBOT.o: LOBOROBOT.c LOBOROBOT.h globals.h
	gcc $(CFLAG) -c LOBOROBOT.c
