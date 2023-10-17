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
**描述**

- OpenCVfacetracking.py是一个基于OpenCV实现的人脸追踪模块程序，它可以通过树莓派连接的摄像头实时检测视频流中的人脸，并对其进行追踪。该模块可以被集成到树莓派小车的代码中，以增强小车的感知能力和自主导航能力

**环境**

- OpenCV
- NumPy

**使用方法**
- 确保已在树莓派安装好所需的环境
- 下载OpenCVfacetracking.py，并将其复制到小车代码目录下
- 调试参数并运行此代码

**代码段**
```py
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import cv2
import numpy as np
from LOBOROBOT import LOBOROBOT # 载入机器人库
import  RPi.GPIO as GPIO
import time  
"""
* @par Copyright (C): 2010-2020, hunan CLB Tech
* @file         OpencvFaceTracking
* @version      V2.0
* @details
* @par History

@author: zhulin
"""

# 按键及LED初始化
BtnPin  = 19
Gpin    = 5
Rpin    = 6

# 从网络摄像头获取输入
cap = cv2.VideoCapture(0)
clbrobot = LOBOROBOT()  # 实例化机器人对象

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096
# Helper function to make setting a servo pulse width simpler.
# 频率设置为50hz，适用于舵机系统。
clbrobot.set_servo_angle(5,90)  #底座舵机
clbrobot.set_servo_angle(4,75)  #顶部舵机

time.sleep(0.5)

# 将视频尺寸减小到320x240，这样rpi处理速度就会更快
cap.set(3,320)
cap.set(4,240)

#引入分类器
face_cascade = cv2.CascadeClassifier( 'face1.xml' )

# 键盘控制函数         
def keysacn():
    val = GPIO.input(BtnPin)
    while GPIO.input(BtnPin) == False:
        val = GPIO.input(BtnPin)
    while GPIO.input(BtnPin) == True:
        time.sleep(0.01)
        val = GPIO.input(BtnPin)
        if val == True:
            GPIO.output(Rpin,1)
            while GPIO.input(BtnPin) == False:
                GPIO.output(Rpin,0)
        else:
            GPIO.output(Rpin,0)

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
GPIO.setup(Gpin, GPIO.OUT)     # 设置绿色Led引脚模式输出
GPIO.setup(Rpin, GPIO.OUT)     # 设置红色Led引脚模式输出
GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # 设置输入BtnPin模式，拉高至高电平(3.3V) 

# 键盘控制函数 
keysacn()

while True:   
    ret,frame = cap.read()
    gray= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #对灰度图进行.detectMultiScale()
    faces=face_cascade.detectMultiScale(gray)   
    clbrobot.t_stop(0) # 机器人停止
    if len(faces)>0:
        print('face found!')
        (x,y,w,h) = faces[0]
        cv2.rectangle(frame,(x,y),(x+h,y+w),(0,255,0),2)
        result=(x,y,w,h)
        x=result[0]+w/2
        y=result[1]+h/2
        facebool = True 
        
        for(x,y,w,h) in faces:
            #找到矩形的中心位置
            cv2.rectangle(frame,(x,y),(x+h,y+w),(0,255,0),2)
            result=(x,y,w,h)
            x=result[0]+w/2
            y=result[1]+h/2 
            x_p = int(round(x))
            print x_p
        # 设定一个范围
        x_Lower = 150
        x_Upper = 180
        # 判断X方向范围来判断机器人的运动
        if x_p > x_Lower and x_p < x_Upper:
            clbrobot.t_up(50,0)            # 机器人前进
        elif x_p < x_Lower:
            clbrobot.turnLeft(50,0)       # 机器人左转
        elif x_p > x_Upper:
            clbrobot.turnRight(50,0)     # 机器人右转                
        else:
                clbrobot.t_stop(0)      # 机器人停止
    # 显示窗口画面        
    cv2.imshow("capture", frame)        
    if cv2.waitKey(1) & 0xFF == ord('q'):
            clbrobot.t_stop(0) # 机器人停止
            cap.release()
            GPIO.cleanup()
            cv2.destroyAllWindows() 
            break
        
clbrobot.t_stop(0) # 机器人停止
cap.release()
cv2.destroyAllWindows()       
```

描述
这是一个使用 OpenCV 进行人脸追踪从而控制小车运动的项目，可以实现在摄像头捕获的视频重实时追踪人脸并进行标记。

## 11.robot_servo_ball.py
**描述**

- robot_servo_ball.pyrobot_servo_ball.py 是一个用于控制二维舵机云台的水平和垂直方向旋转控制的代码模块。该模块可以通过 PWM 方式控制舵机的旋转角度，从而实现对二维舵机云台的精准控制


**环境**

- RPi.GPIO


**使用方法**
- 确保已在树莓派安装好所需的环境
- 下载robot_servo_ball.py，并将其复制到小车代码目录下
- 调试参数并运行此代码
  

**代码段**
```py
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
    * @par Copyright (C): 2010-2020, Hunan CLB Tech
    * @file        robot_sevo_ball
    * @version      V1.0
    * @details
    * @par History
    @author: zhulin
"""
from __future__ import division
import cv2
import time  
import numpy as np
from LOBOROBOT import LOBOROBOT,PCA9685 # 载入机器人库
import threading
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# 实例化机器人对象
clbrobot = PCA9685(0x40, debug=False)  # 实例化机器人对象
clbrobot.setPWMFreq(50)

# 设置舵机初始值，可以根据自己的要求调试
clbrobot.setPWM(10,0,350)  # 底座舵机
clbrobot.setPWM(9,0,370)  # 倾斜舵机
time.sleep(1)

#初始化摄像头并设置阙值
usb_cap = cv2.VideoCapture(0)

# 设置球体追踪的HSV值，上下限值
ball_yellow_lower=np.array([9,135,231])
ball_yellow_upper=np.array([31,255,255])

# 设置显示的分辨率，设置为320×240 px
usb_cap.set(3, 320)
usb_cap.set(4, 240)

#舵机云台的每个自由度需要4个变量
pid_thisError_x=500       #当前误差值
pid_lastError_x=100       #上一次误差值
pid_thisError_y=500
pid_lastError_y=100

pid_x=0
pid_y=0

# 舵机的转动角度
pid_Y_P = 280
pid_X_P = 300           #转动角度
pid_flag=0


# 机器人舵机旋转
def Robot_servo(X_P,Y_P):
    clbrobot.setPWM(10,0,650-pid_X_P)
    clbrobot.setPWM(9,0,650-pid_Y_P)
      

# 循环函数
while True:    
    ret,frame = usb_cap.read()

    #高斯模糊处理
    frame=cv2.GaussianBlur(frame,(5,5),0)
    hsv= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #ROI及找到形态学找到小球进行处理
    mask=cv2.inRange(hsv,ball_yellow_lower,ball_yellow_upper) # 掩膜处理
    mask=cv2.erode(mask,None,iterations=2)
    mask=cv2.dilate(mask,None,iterations=2)
    mask=cv2.GaussianBlur(mask,(3,3),0)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    cnts=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]  #发现小球
    #当找到小球处理
    if len(cnts)>0:
        cap_cnt=max(cnts,key=cv2.contourArea)
        (pid_x,pid_y),radius=cv2.minEnclosingCircle(cap_cnt)
        cv2.circle(frame,(int(pid_x),int(pid_y)),int(radius),(255,0,255),2)

        # 误差值处理
        pid_thisError_x=pid_x-160
        pid_thisError_y=pid_y-120

        #PID控制参数
        pwm_x = pid_thisError_x*3+1*(pid_thisError_x-pid_lastError_x)
        pwm_y = pid_thisError_y*3+1*(pid_thisError_y-pid_lastError_y)

        #迭代误差值操作
        pid_lastError_x = pid_thisError_x
        pid_lastError_y = pid_thisError_y

        pid_XP=pwm_x/100
        pid_YP=pwm_y/100
        
        # pid_X_P pid_Y_P 为最终PID值
        pid_X_P=pid_X_P-int(pid_XP)
        pid_Y_P=pid_Y_P-int(pid_YP)

        #限值舵机在一定的范围之内
        if pid_X_P>670:
            pid_X_P=650
        if pid_X_P<0:
            pid_X_P=0
        if pid_Y_P>650:
            pid_Y_P=650
        if pid_X_P<0:
            pid_Y_p=0

    servo_tid=threading.Thread(target=Robot_servo,args=(pid_X_P,pid_Y_P))  # 多线程
    servo_tid.setDaemon(True)
    servo_tid.start()   # 开启线程
    
    cv2.imshow("MAKEROBO Robot", frame)  # 显示图像
    if cv2.waitKey(1)==119:
        break
    
usb_cap.release()
cv2.destroyAllWindows()
```
## 12.robot_servo_face.py
**描述**

- robot_servo_ball.py 的机器人人脸控制程序。该程序可以实时检测摄像头中的人脸，并根据人脸移动和表情变化来控制机器人的舵机云台运动


**环境**

- OpenCV


**使用方法**
- 确保已在树莓派安装好所需的环境
- 下载robot_servo_face.py，并将其复制到小车代码目录下
- 调试参数并运行此代码
  

**代码段**
```py
!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
    * @par Copyright (C): 2010-2020, Hunan CLB Tech
    * @file        robot_sevo_face
    * @version      V1.0
    * @details
    * @par History
    @author: zhulin
"""
from __future__ import division
import cv2
import time  
import numpy as np
#from LOBOROBOT import PCA9685 # 载入机器人库
import Adafruit_PCA9685
import threading
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 实例化机器人对象
#clbrobot = PCA9685(0x40, debug=False)  # 实例化机器人对象
#clbrobot.setPWMFreq(50)
#初始化PCA9685和舵机
servo_pwm = Adafruit_PCA9685.PCA9685() # 实例话舵机云台
servo_pwm.set_pwm_freq(50)

# 设置舵机初始值，可以根据自己的要求调试
servo_pwm.set_pwm(10,0,350) # 底座舵机
servo_pwm.set_pwm(9,0,300) # 倾斜舵机  420
time.sleep(1)

#初始化摄像头并设置阙值
usb_cap = cv2.VideoCapture(0)

# 设置显示的分辨率，设置为320×240 px
usb_cap.set(3, 320)
usb_cap.set(4, 240)

#引入分类器
makerobo_face_cascade = cv2.CascadeClassifier('face1.xml')

pid_x=0
pid_y=0
pid_w=0
pid_h=0

#舵机云台的每个自由度需要4个变量
pid_thisError_x=0   #当前误差值
pid_lastError_x=0   #上一次误差值
pid_thisError_y=0
pid_lastError_y=0

# 舵机的转动角度
pid_X_P = 325
pid_Y_P = 350   #转动角度 420

pid_flag=0
makerobo_facebool = False

# 机器人舵机旋转
def Robot_servo():
    while True:
        servo_pwm.set_pwm(10,0,650-pid_X_P)
        servo_pwm.set_pwm(9,0,650-pid_Y_P)


servo_tid=threading.Thread(target=Robot_servo)  # 多线程
servo_tid.setDaemon(True)
servo_tid.start()                               # 开启线程

# 循环函数  
while True:   
    ret,frame = usb_cap.read()       # 加载图像
    gray= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #对灰度图进行.detectMultiScale()
    faces=makerobo_face_cascade.detectMultiScale(gray)
    max_face=0
    value_x=0
    
    # 找到人脸画矩形
    if len(faces)>0:
        (pid_x,pid_y,pid_w,pid_h) = faces[0]
        cv2.rectangle(frame,(pid_x,pid_y),(pid_x+pid_h,pid_y+pid_w),(0,255,0),2)
        result=(pid_x,pid_y,pid_w,pid_h)
        pid_x=result[0]+pid_w/2
        pid_y=result[1]+pid_h/2
        makerobo_facebool = True      

         # 误差值处理
        pid_thisError_x=pid_x-160
        pid_thisError_y=pid_y-120

        #自行对P和D两个值进行调整，检测两个值的变化对舵机稳定性的影响
        pwm_x = pid_thisError_x*5+1*(pid_thisError_x-pid_lastError_x)
        pwm_y = pid_thisError_y*5+1*(pid_thisError_y-pid_lastError_y)
        
        #迭代误差值操作
        pid_lastError_x = pid_thisError_x
        pid_lastError_y = pid_thisError_y
        
        pid_XP=pwm_x/100
        pid_YP=pwm_y/100
        
        # pid_X_P pid_Y_P 为最终PID值
        pid_X_P=pid_X_P-int(pid_XP)
        pid_Y_P=pid_Y_P-int(pid_YP)

        #限值舵机在一定的范围之内
        if pid_X_P>670:
            pid_X_P=650
        if pid_X_P<0:
            pid_X_P=0
        if pid_Y_P>650:
            pid_Y_P=650
        if pid_X_P<0:
            pid_Y_p=0
    # 显示图像
    cv2.imshow("MAKEROBO Robot", frame)
    if cv2.waitKey(1)==119:
        break
    
usb_cap.release()
cv2.destroyAllWindows()
```

## 13.Robot_QR_navigation.py
**描述**
二维码
**环境**

- 


**使用方法**
- 确保已在树莓派安装好所需的环境
- 下载robot_servo_ball.py，并将其复制到小车代码目录下
- 调试参数并运行此代码
  

**代码段**
```py
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
* @par Copyright (C): 2010-2020, hunan CLB Tech
* @file         13.robot_QR_navigatoin.py
* @version      V2.0
* @details
* @par History

@author: zhulin
"""
import cv2
import numpy as np
import zbar
from PIL import Image
from LOBOROBOT import LOBOROBOT # 载入机器人库
from aip import AipSpeech
import pygame
import  RPi.GPIO as GPIO 
import sys 

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    
clbrobot=LOBOROBOT()  #  载入机器人库
    
#这里需要填你自己的id和密钥
APP_ID='16226519'
API_KEY='5KVxQVES4LSja0u2G4y8m1O9'
SECRET_KEY='KhaXYwGLSmQYgnwHkuXKpV9MO2ta0bQ8'

aipSpeech=AipSpeech(APP_ID,API_KEY,SECRET_KEY)

def robot_speech(content):
    text=content
    result = aipSpeech.synthesis(text = text, 
                             options={'spd':5,'vol':9,'per':0,})
    if not isinstance(result,dict):
        with open('makerobo.mp3','wb') as f:
            f.write(result)  
    else:print(result)
    #我们利用树莓派自带的pygame
    pygame.mixer.init()
    pygame.mixer.music.load('/home/pi/CLBROBOT/makerobo.mp3')
    pygame.mixer.music.play()


# 智能机器人运动状态
enStop = 0
enRun = 1
enBack = 2
enLeft = 3
enRight = 4
car_State = 0
symbolPos = []

last_qr_data = 'no qrcode'
global qr_data

def draw_rect(img, pos, color, width):
    cv2.line(img, pos[0], pos[1], color, width)
    cv2.line(img, pos[0], pos[3], color, width)
    cv2.line(img, pos[2], pos[1], color, width)
    cv2.line(img, pos[2], pos[3], color, width)

def qr_scan_decode(img):
    global qr_data
    global last_qr_data
    pil= Image.fromarray(img).convert('L')  # gray
    width, height = pil.size
    raw = pil.tobytes()
    zarimage = zbar.Image(width, height, 'Y800', raw)
    scanner_Flag = scanner.scan(zarimage)
    if scanner_Flag == 1:
        for symbol in zarimage:
            if not symbol.count:
                print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data
                symbolPos = symbol.location
                draw_rect(img, symbolPos, (0,255,0), 3)
                qr_data = str(symbol.data)
            else:
                qr_data = 'no qrcode'
    else:
        qr_data = 'no qrcode'
    if last_qr_data != qr_data:       
        command_resolve(qr_data)
    last_qr_data = qr_data

def command_resolve(command):
    last_car_state = 0
    if command.find("Run",0,len(command)) != -1 :
        command.zfill(len(command))
        car_state = 1
    elif command.find("Back",0,len(command)) != -1 :
        command.zfill(len(command))
        car_state = 2
    elif command.find("Left",0,len(command)) != -1 :
        command.zfill(len(command))
        car_state = 3
    elif command.find("Right",0,len(command)) != -1:
        command.zfill(len(command))
        car_state = 4
    elif command.find("Stop",0,len(command)) != -1:            
        command.zfill(len(command))
        car_state = 0
    else:
        car_state = 5
        command.zfill(len(command))
    #print car_state
   
    if last_car_state != car_state :
        car_control(car_state)
    last_car_state = car_state

def car_control(car_state):
    
    if car_state == enRun:
        content='机器人前进'
        robot_speech(content)
        clbrobot.t_up(50,1)         # 前进
    elif car_state == enBack :
        content='机器人后退'
        robot_speech(content)
        clbrobot.t_down(50,1)      # 后退
    elif car_state == enLeft :
        content='机器人左转'
        robot_speech(content)        
        clbrobot.turnLeft(50,1)    # 左转
    elif car_state == enRight :
        content='机器人右转'
        robot_speech(content) 
        clbrobot.turnRight(50,1)   # 右转
    elif car_state == enStop:
        content='机器人停止'
        robot_speech(content) 
        clbrobot.t_stop(0)        # 停止
    else:
        content='机器人停止'
        robot_speech(content) 
        clbrobot.t_stop(0)       # 停止

if __name__ == '__main__':
    # 创建一个QR
    scanner = zbar.ImageScanner()
    # 配置QR
    scanner.parse_config('enable')
    font = cv2.FONT_HERSHEY_SIMPLEX
    # 设置Camera
    cap = cv2.VideoCapture(0)
    if cap.isOpened()==0 :
        print("camera iserror")
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

    while(True):
        grabbed, frame = cap.read()
        if not grabbed:
            break
        qr_scan_decode(frame)
    
    #cv2.putText(frame,symbol.data,(20,100),font,1,(0,255,0),4)
    #print car_state

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == 27: # 按ESC键退出
            clbrobot.t_stop(0)
            break
# 释放Camera和GPIO
    GPIO.release()
    clbrobot.t_stop(0)
    cap.release()
    cv2.destroyAllWindows()
```

## 14.gesture.py
<<<<<<< HEAD
**描述**

- 


**环境**

- 


**使用方法**
- 确保已在树莓派安装好所需的环境
- 下载robot_servo_ball.py，并将其复制到小车代码目录下
- 调试参数并运行此代码
  

**代码段**
```py
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
* @par Copyright (C): 2010-2019, hunan CLB Tech
* @file         11.gesture.py
* @version      V1.0
* @details
* @par History

@author: zhulin
"""
import cv2
import numpy as np
import math

cap = cv2.VideoCapture(0)

# 将视频尺寸减小到300x300，这样rpi处理速度就会更快
cap.set(3,320)
cap.set(4,320)
    
while(1):
        
    try:  # 如果它在窗口中找不到任何东西，因为找不到最大面积的轮廓，就会出现错误
          # 因此，此try错误语句
          
        ret, frame = cap.read()
        frame=cv2.flip(frame,1)
        kernel = np.ones((3,3),np.uint8)
        
        # 定义感兴趣的区域
        roi=frame[0:300, 0:300]
        
        
        cv2.rectangle(frame,(0,0),(300,300),(0,255,0),0)    
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        
        
         
    # 定义HSV中肤色的范围
        lower_skin = np.array([0,20,70], dtype=np.uint8)
        upper_skin = np.array([20,255,255], dtype=np.uint8)
        
     # 提取肤色图像 
        mask = cv2.inRange(hsv, lower_skin, upper_skin)
        
   
        
    # 外推手以填补其中的黑点
        mask = cv2.dilate(mask,kernel,iterations = 4)
        
    # 高斯模糊
        mask = cv2.GaussianBlur(mask,(5,5),100) 
        
        
        
    # 找到轮廓
        _,contours,hierarchy= cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
   # 找到最大面积的轮廓（手）
        cnt = max(contours, key = lambda x: cv2.contourArea(x))
        
    # 大概轮廓
        epsilon = 0.0005*cv2.arcLength(cnt,True)
        approx= cv2.approxPolyDP(cnt,epsilon,True)
       
        
    # 围绕手做凸包
        hull = cv2.convexHull(cnt)
        
     #define area of hull and area of hand
        areahull = cv2.contourArea(hull)
        areacnt = cv2.contourArea(cnt)
      
    # 查找凸包中未被手覆盖的区域的百分比
        arearatio=((areahull-areacnt)/areacnt)*100
    
     # 发现凸包相对于手的缺陷
        hull = cv2.convexHull(approx, returnPoints=False)
        defects = cv2.convexityDefects(approx, hull)
        
    # l = no. of defects
        l=0
        
    # 查找编号的代码 手指造成的缺陷
        for i in range(defects.shape[0]):
            s,e,f,d = defects[i,0]
            start = tuple(approx[s][0])
            end = tuple(approx[e][0])
            far = tuple(approx[f][0])
            pt= (100,180)
            
            
            # 求出三角形所有边的长度
            a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
            b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
            c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
            s = (a+b+c)/2
            ar = math.sqrt(s*(s-a)*(s-b)*(s-c))
            
            # 点与凸包之间的距离
            d=(2*ar)/a
            
            # 在这里应用余弦规则
            angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57
            
        
            # 忽略大于90度的角度并忽略非常靠近凸包的点（它们通常是由于噪声而来）
            if angle <= 90 and d>30:
                l += 1
                cv2.circle(roi, far, 3, [255,0,0], -1)
            
            # 在手周围画线
            cv2.line(roi,start, end, [0,255,0], 2)
            
            
        l+=1
        
        # 打印范围内的相应手势
        font = cv2.FONT_HERSHEY_SIMPLEX
        if l==1:
            if areacnt<2000:
                cv2.putText(frame,'Put hand in the box',(0,50), font, 1, (0,0,255), 3, cv2.LINE_AA)
            else:
                if arearatio<12:
                    cv2.putText(frame,'0',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
                elif arearatio<17.5:
                    cv2.putText(frame,'Best of luck',(0,50), font, 1, (0,0,255), 3, cv2.LINE_AA)
                   
                else:
                    cv2.putText(frame,'1',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
                    
        elif l==2:
            cv2.putText(frame,'2',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
            
        elif l==3:
         
              if arearatio<27:
                    cv2.putText(frame,'3',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
              else:
                    cv2.putText(frame,'ok',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
                    
        elif l==4:
            cv2.putText(frame,'4',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
            
        elif l==5:
            cv2.putText(frame,'5',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
            
        elif l==6:
            cv2.putText(frame,'reposition',(0,50), font, 1, (0,0,255), 3, cv2.LINE_AA)
            
        else :
            cv2.putText(frame,'reposition',(10,50), font, 1, (0,0,255), 3, cv2.LINE_AA)
            
        # 显示窗户
        cv2.imshow('mask',mask)
        cv2.imshow('frame',frame)
    except:
        pass
        
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    
cv2.destroyAllWindows()
cap.release()    
```
=======

## 15.Control_from_PC&Phone

## 16.MQTT_control
>>>>>>> 1db36bfe1d5d8922cc21b052dbd2160ee38566be
