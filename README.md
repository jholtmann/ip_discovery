ip_discovery

These python programs can be used to find a server on your local LAN when you don't know its IP address.

On the server:
'''
python ip_disc_server.py &
'''

On the client machine:
'''
python ip_disc_client.py
'''

The server will now listen for UDP broadcasts on port 9434. The client sends UDP packets to 255.255.255.255, which are broadcast across the network. The server then responds to the client, allowing the client to deduce the server's ip.