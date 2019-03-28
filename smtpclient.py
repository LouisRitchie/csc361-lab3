from socket import *

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "smtp.uvic.ca"

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 25))

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv0 = clientSocket.recv(1024).decode()
print(recv0)
if recv0[:3] != '250':
    print('250 reply not received from server.')
    
# Send MAIL FROM command and print server response.
mailCommand = 'MAIL from: louisr@uvic.ca\r\n'
clientSocket.send(mailCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command and print server response. 
rcptCommand = 'RCPT to: louisr@uvic.ca\r\n'
clientSocket.send(rcptCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
    print('250 reply not received from server.')

# Send DATA command and print server response. 
dataCommand = "DATA\r\n"
clientSocket.send(dataCommand.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '354':
    print('354 reply not received from server.')

# Send message data.
dataBody = "I love computer networks!\r\n.\r\n"
clientSocket.send(dataBody.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '250':
    print('250 reply not received from server.')

# Send QUIT command and get server response.
quitCommand = "QUIT\r\n"
clientSocket.send(quitCommand.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)
if recv5[:3] != '221':
    print('221 reply not received from server.')
