import socket
import time
import math

# User and Game Server Information
NICKNAME = '대전_1반_이연재'
HOST = '127.0.0.1'
PORT = 1447 # Do not modify

# predefined variables(Do not modify these values)
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 5
HOLES = [ [0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127] ]

class Conn:
    def __init__(self):
        self.sock = socket.socket()
        print('Trying to Connect: ' + HOST + ':' + str(PORT))
        self.sock.connect((HOST, PORT))
        print('Connected: ' + HOST + ':' + str(PORT))
        send_data = '9901/' + NICKNAME
        self.sock.send(send_data.encode('utf-8'))
        print('Ready to play.\n--------------------')
    def request(self):
        self.sock.send('9902/9902'.encode())
        print('Received Data has been curruted, Resend Requested.')
    def receive(self):
        recv_data = (self.sock.recv(1024)).decode()
        print('Data Received: ' + recv_data)
        return recv_data
    def send(self, angle, power):
        merged_data = '%d/%d' % (angle, power)
        self.sock.send(merged_data.encode('utf-8'))
        print('Data Sent: ' + merged_data)
    def close(self):
        self.sock.close()

class GameData:
    def __init__(self):
        self.reset()
    def reset(self):
        self.balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]
    def read(self, conn):
        recv_data = conn.receive()
        split_data = recv_data.split('/')
        idx = 0    
        try:
            for i in range(NUMBER_OF_BALLS):
                for j in range(2):
                    self.balls[i][j] = int(split_data[idx])
                    idx += 1
        except:
            self.reset()
            conn.request()
            self.read(conn)
    def show(self):
        print('=== Arrays ===')
        for i in range(NUMBER_OF_BALLS):
            print('Ball%d: %d, %d' % (i, self.balls[i][0], self.balls[i][1]))
        print()

# 자신의 차례가 되어 게임을 진행해야 할 때 호출되는 Method
def play(conn, gameData):
    angle = 0
    power = 0
    ######################################################################################
    one = gameData.balls[0]

    for i in range(1, len(gameData.balls)):
        if gameData.balls[i][0] != -1:
            height = abs(one[1] - gameData.balls[i][1])
            base = abs(one[0] - gameData.balls[i][0])
            tan = height / base
            atan = math.atan(tan)
            result = 0
            if gameData.balls[0][0] < gameData.balls[i][0] and gameData.balls[i][1] > gameData.balls[0][1]:
                result = math.degrees(atan)
            elif gameData.balls[0][0] < gameData.balls[i][0] and gameData.balls[i][1] < gameData.balls[0][1]:
                result = math.degrees(atan) + 90
            elif gameData.balls[i][0] < gameData.balls[0][0] and gameData.balls[i][1] < gameData.balls[0][1]:
                result = math.degrees(atan) + 180
            elif gameData.balls[i][0] < gameData.balls[0][0] and gameData.balls[i][1] > gameData.balls[0][1]:
                result = math.degrees(atan) + 270

            angle = result
            power = math.sqrt((gameData.balls[0][0] - gameData.balls[i][0])**2 + (gameData.balls[0][1] - gameData.balls[i][1])**2) - 35
            if power <= 15:
                power = 15
            print('각도는: ', result)
            print('파워는: ', power)
            break


    ######################################################################################
    conn.send(angle, power)
    time.sleep(3)



def main():
    conn = Conn()
    gameData = GameData()
    while True:
        gameData.read(conn)
        gameData.show()
        if gameData.balls[0][0] == 9909:
            break
        play(conn, gameData)        
    conn.close()
    print('Connection Closed')

if __name__ == '__main__':
    main()
