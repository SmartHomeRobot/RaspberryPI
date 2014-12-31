# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

# BOARD编号方式，基于插座引脚编号
pins = [11,12,13,15,16,18]

def setup():
    # BOARD MODE
    GPIO.setmode(GPIO.BOARD
    # 输出模式
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

def forward():
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(15, GPIO.LOW)

def backward():
    GPIO.output(11, GPIO.LOW)
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(15, GPIO.HIGH)
    time.sleep(1)

def halt():
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(15, GPIO.HIGH)
    time.sleep(0.5)

def turn_left():
    GPIO.output(11, GPIO.LOW)
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(15, GPIO.LOW)
    time.sleep(1)
    halt()

def turn_right():
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(15, GPIO.HIGH)
    time.sleep(1)
    halt()

def loop():
    while True:
    forward()

def destroy():
    for pin in pins:
        GPIO.output(pin, GPIO.LOW)
        GPIO.setup(pin, GPIO.IN)

if __name__ == '__main__':
    # 初始化GPIO
    setup()
    try:
        loop()
    except KeyboardInterrupt:
    # 恢复GPIO口状态
        destroy()
