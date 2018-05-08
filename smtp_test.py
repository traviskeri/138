#Travis Keri
#PLab 2a: SMTP Client

from socket import*

msg = b"\r\n I love computer networks!\r\n"
endmsg = b"r\r\n.\r\n"

mailserver = 'smtp.csus.edu'
mailport = 25

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, mailport))
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')

heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
	print('250 reply not received from server')

# Send MAIL FROM command and print server response.
print("Sending MAIL FROM Command")
clientSocket.send(b'MAIL FROM:<travis.j.keri@gmail.com>\r\n')
recv2 = clientSocket.recv(1024)
print(recv2)
if recv2[:3] != '250':
	print('250 reply not received from sever.')

# Send RCPT TO command and print server response.
print("Sending RCPT TO Command")
clientSocket.send(b"RCPT TO: <travis.j.keri@gmail.com>\r\n")
recv2 = clientSocket.recv(1024)
print(recv2)
if recv2[:3] != '250':
	print('250 reply not received from sever.')


# Send DATA command and print server response.
print("Sending DATA Command")
clientSocket.send(b"DATA\r\n")
recv2 = clientSocket.recv(1024)
print(recv2)
if recv2[:3] != '354':
	print('250 reply not received from sever.')


#Send message data.
print("Sending msg Command")
clientSocket.send("\r\n SMTP Mail Client Test\nI love computer networkin!\r\n.\r\n")
recv2 = clientSocket.recv(1024)
print(recv2)
if recv2[:3] != '250':
	print('250 reply not received from sever.')


#Message ends with a single period.
#print("Sending endmsg Command")
#clientSocket.send(endmsg)
#recv2 = clientSocket.recv(1024)
#print(recv2)
#if recv2[:3] != '250':
#	print('250 reply not received from sever.')


# Send QUIT command and get server response.
print("Sending QUIT")
clientSocket.send(b"QUIT\r\n")
recv2 = clientSocket.recv(1024)
print(recv2)
if recv2[:3] != '250':
	print('250 reply not received from sever.')


print("Mail Sent")