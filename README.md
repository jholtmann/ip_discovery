Python UDP broadcast IP discovery

These python scripts can be used to find a server on your local LAN when you don't know its IP address.

On the server:
```
python3 ip_disc_server.py & echo $! > ip_disc_server.pid
```

On the client machine:
```
python3 ip_disc_client.py
```

The server will now listen for UDP broadcasts on port 9434. The client sends UDP packets to 255.255.255.255, which are broadcast across the network. The server then responds to the client, allowing the client to deduce the server's IP address.

The .bat file can be used to run the server discovery script on windows systems. Please note that Python 3.x must be installed and the script must be run with administrator privileges.


To run the server on boot on a Linux server do:
```
sudo crontab -e
```
and add:
```
@reboot python3 /[PATH TO SCRIPT DIRECTORY]/ip_disc_server.py & echo $! > /[PATH TO SCRIPT DIRECTORY]/ip_disc_server.pid
```
to the bottom of the file.
