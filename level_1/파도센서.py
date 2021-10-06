# 입력한 물결파의 좌표와 유효사거리에 따라 5개의 센서 중 몇개의 센서가 물결파를 감지했는지 출력하는 프로그램

import math

wave_x, wave_y, wave_radius = map(int, input().split(' ')) # 첫 줄에 파도가 일어난 좌표와 파도의 유효 반지름을 입력
x1, y1 = map(int, input().split(' ')) # 첫 번째 센서 좌표를 입력
x2, y2 = map(int, input().split(' ')) # 두 번째 센서 좌표를 입력
x3, y3 = map(int, input().split(' ')) # 셋 번째 센서 좌표를 입력
x4, y4 = map(int, input().split(' ')) # 넷 번째 센서 좌표를 입력
x5, y5 = map(int, input().split(' ')) # 다섯 번째 센서 좌표를 입력
