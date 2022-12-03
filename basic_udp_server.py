import socket
import ctypes
import struct
 
UDP_IP = "127.0.0.1"
UDP_PORT = 20777 
sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
sock.settimeout(20)

while True:
    rawData, addr = sock.recvfrom(2048) # buffer size is 2048 bytes
    #print("Count: %s" % count)
    
    print("Byte Value: %s" % rawData[0:27])
    validValues = 0
    data = bytearray()
    for i in range(0,len(rawData)):
        
        if rawData[i:i+1]:
            validValues += 1
            data.append(rawData[i])
        else:
            print("Is Ascii: %s" % rawData[i:i+1])
            continue
                

        if validValues >= 27:
            break
    print("Byte Values: %s" % data)
    m_packet_format = int.from_bytes(data[0:2], "little")
    m_game_major_version = int.from_bytes(data[2:3], "little")
    m_game_minor_version = int.from_bytes(data[3:4], "little")
    m_packet_version = int.from_bytes(data[4:5], "little")
    m_packet_id = int.from_bytes(data[5:6], "little")
    m_session_uid = int.from_bytes(data[6:15], "little")
    print(data[15:20])
    # m_session_time = struct.unpack('<f', data[15:20])
    m_frame_identifier = int.from_bytes(data[20:25], "little")
    m_player_car_index = int.from_bytes(data[25:26], "little")
    m_secondary_player_car_index = int.from_bytes(data[26:27], "little")
    print("\n ---- New Data Received ----")
    print("Session UID: %s" % m_session_uid)
    print("Packet ID: %s" % m_packet_id)
    # print("Session Time: %s" % m_session_time)
    print("Frame Identifier: %s" % m_frame_identifier)