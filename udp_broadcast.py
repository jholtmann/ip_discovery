from socket import *
import sys
import time

# Create a UDP socket
sock = socket(AF_INET, SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
sock.settimeout(5)

server_address = ('255.255.255.255', 9434)
message = 'pfg_ip_broadcast_cl'

try:
	while True:
		# Send data
		print('sending: ' + message)
		sent = sock.sendto(message.encode(), server_address)

		# Receive response
		print('waiting to receive')
		data, server = sock.recvfrom(4096)
		if data.decode('UTF-8') == 'pfg_ip_response_serv':
			print('Received confirmation')
			print('Server ip: ' + str(server[0]) )
			break
		else:
			print('Verification failed')
		
		print('Trying again...')
	
	
finally:	
	sock.close()