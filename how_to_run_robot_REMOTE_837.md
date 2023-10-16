# Work Record

Although all codes were given, and video tutorial was fine, running them still could be a challenge for us. Here i will record some of the problems i met and how i solved them. I will follow the order of the given codes.

## 1.passive_buzzer.py

Running this code is easy, but the environment is not. I didn't follow the video tutorial to install virtual machine on a windows laptop but instead using my own arch linux laptop all the way.

To connect to the raspberry pi, i used this command:

```bash
ip a # to find the ip address of the laptop
```

expect out put:

```bash
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host noprefixroute
       valid_lft forever preferred_lft forever
2: enp7s0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc fq_codel state DOWN group default qlen 1000
    link/ether f8:75:a4:64:ea:8a brd ff:ff:ff:ff:ff:ff
3: wlp0s20f3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether c8:09:a8:6e:ba:13 brd ff:ff:ff:ff:ff:ff
    inet 192.168.201.180/24 brd 192.168.201.255 scope global dynamic noprefixroute wlp0s20f3
       valid_lft 3252sec preferred_lft 3252sec
    inet6 2409:8924:e50:2ebb:977c:42f3:3b20:5223/64 scope global dynamic noprefixroute
       valid_lft 3497sec preferred_lft 3497sec
    inet6 fe80::64aa:8d28:e5c7:1b1a/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
```

so my laptop ip address is 192.168.201.180
then use this to detect raspberry pi's ip:(notice the first three numbers are the same as my laptop's ip address)

```bash
sudo nmap -T4 -O 192.168.201.0/24
```

expect output:

```bash
[sudo] password for ebotian:
Starting Nmap 7.94 ( https://nmap.org ) at 2023-10-13 15:40 HKT
Nmap scan report for 192.168.201.168
Host is up (0.011s latency).
Not shown: 997 filtered tcp ports (no-response)
PORT      STATE SERVICE
1042/tcp  open  afrog
1043/tcp  open  boinc
10001/tcp open  scp-config
MAC Address: 48:E7:DA:AA:22:D3 (AzureWave Technology)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running (JUST GUESSING): Microsoft Windows 11|10 (90%), FreeBSD 6.X (90%)
OS CPE: cpe:/o:freebsd:freebsd:6.2 cpe:/o:microsoft:windows_10
Aggressive OS guesses: Microsoft Windows 11 21H2 (90%), FreeBSD 6.2-RELEASE (90%), Microsoft Windows 10 (85%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 1 hop

Nmap scan report for 192.168.201.205
Host is up (0.011s latency).
Not shown: 995 filtered tcp ports (no-response)
PORT     STATE SERVICE
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
903/tcp  open  iss-console-mgr
5357/tcp open  wsdapi
MAC Address: 14:5A:FC:20:CC:77 (Liteon Technology)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running (JUST GUESSING): Microsoft Windows 2019|10|XP (90%)
OS CPE: cpe:/o:microsoft:windows_10 cpe:/o:microsoft:windows_xp::sp3
Aggressive OS guesses: Microsoft Windows Server 2019 (90%), Microsoft Windows 10 1909 (88%), Microsoft Windows XP SP3 (85%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 1 hop

Nmap scan report for 192.168.201.220
Host is up (0.019s latency).
Not shown: 998 closed tcp ports (reset)
PORT     STATE SERVICE
22/tcp   open  ssh
5900/tcp open  vnc
MAC Address: D8:3A:DD:4B:68:3A (Unknown)
Device type: general purpose
Running: Linux 4.X|5.X
OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5
OS details: Linux 4.15 - 5.8
Network Distance: 1 hop

Nmap scan report for 192.168.201.251
Host is up (0.010s latency).
Not shown: 999 closed tcp ports (reset)
PORT   STATE SERVICE
53/tcp open  domain
MAC Address: 96:90:FA:C1:93:95 (Unknown)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.94%E=4%D=10/13%OT=53%CT=1%CU=32623%PV=Y%DS=1%DC=D%G=Y%M=9690FA%
OS:TM=6528F495%P=x86_64-pc-linux-gnu)SEQ(SP=104%GCD=1%ISR=10C%TI=Z%CI=Z%II=
OS:I%TS=A)OPS(O1=M5B4ST11NW9%O2=M5B4ST11NW9%O3=M5B4NNT11NW9%O4=M5B4ST11NW9%
OS:O5=M5B4ST11NW9%O6=M5B4ST11)WIN(W1=FFFF%W2=FFFF%W3=FFFF%W4=FFFF%W5=FFFF%W
OS:6=FFFF)ECN(R=Y%DF=Y%T=40%W=FFFF%O=M5B4NNSNW9%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=
OS:O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD
OS:=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0
OS:%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1
OS:(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI
OS:=N%T=40%CD=S)

Network Distance: 1 hop

Nmap scan report for 192.168.201.180
Host is up (0.000019s latency).
Not shown: 999 closed tcp ports (reset)
PORT     STATE SERVICE
9090/tcp open  zeus-admin
Device type: general purpose
Running: Linux 2.6.X
OS CPE: cpe:/o:linux:linux_kernel:2.6.32
OS details: Linux 2.6.32
Network Distance: 0 hops

OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 256 IP addresses (5 hosts up) scanned in 30.98 seconds
```

and ip of raspberry pi is 192.168.201.220
then use this command to connect to the raspberry pi:

```bash
ssh pi@192.168.201.220
```

for the first connect, it will ask you whether connect it or not, just type `yes` and press enter, then it will ask you for the password, the default password is `raspberry`

then you can enter the shell of raspberry pi.
our pi is brand new, which have nothing installed, so we need to install some packages:

```bash
sudo apt install zsh neovim #note it could config the mirror first, just follow the steps the shell given if you haven't config the mirror
# and change the passwd also
passwd pi
#enter passwd here, i chose just `111`
```

and back to my laptop, i use this command to copy the code to raspberry pi:

```bash
scp robo.tar.gz pi@192.168.201.220:~
#my cmd setting:(alias ip to pi's)
scp .zshrc pi@ip:~
scp .dotfiles/.oh-my-zsh pi@ip:~
```

back to pi, extract it:

```bash
tar xvz robo.tar.gz
```

Done! Basic environment setting should enable us to run the code now.
in pi:

```bash
cd clb[tab]
sudo apt install dos2unix
dos2unix *.py
sudo chmod -R +x *.py
```

then we can run the code now:

```bash
./1.[tab]
```

expect output:robot start singing(playing music)

## 2.button.py

```bash
./2.[tab]
```

expect output:when press button, light change its color

## 3.Basic movement.py

notice if you don't run `dos2unix *.py` before, you will get this error:

```bash
/usr/bin/env: 'python2\r': No such file or directory
```

```bash
./3.[tab]
```

expect output:robot start moving

## 4.infrared_avoid.py

notice if you don't run `dos2unix *.py` before, you will get this error:

```bash
': [Errno 2] No such file or directory
```

```bash
./4.[tab]
```

expect output:

1. robot do nothing until button pressed
2. robot start moving, when it detect obstacle, it will stop and turn around

## 5.openCVLineFollowingRobot.py

## 6.speech-compound.py

我是杨威

or the first connect, it will ask you whether connect it or not, just type `yes` and press enter, then it will ask you for the password, the default password is `raspberry`

then you can enter the shell of raspberry pi.
our pi is brand new, which have nothing installed, so we need to install some packages:

## 7.Robot-speech.py

## 8.OpencvBallTracking.py

## 9.face_recognition.py

## 10.OpencvFaceTracking.py

描述
这是一个使用 OpenCV 进行人脸追踪从而控制小车运动的项目，可以实现在摄像头捕获的视频重实时追踪人脸并进行标记。

## 11.robot_servo_ball.py

## 12.robot_servo_face.py

## 13.Robot_QR_navigation.py

## 14.gesture.py

## 15.Control_from_PC&Phone

## 16.MQTT_control
