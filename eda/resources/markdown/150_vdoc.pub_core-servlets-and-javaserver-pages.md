## 17.7 Bypassing the HTTP Server

## 17.7 Bypassing the HTTP Server

Although applets can only open network connections to the same machine they were loaded from, they need not necessarily connect on the same port (e.g.,  80,  the  HTTP  port).  So,  applets  are  permitted  to  use  raw  sockets, JDBC, or RMI to communicate with custom clients running on the server host.

Applets do these operations in exactly the same manner as do normal Java programs, so you can use whatever approaches to socket, JDBC, and RMI programming that you are already familiar with, provided that the network server is on the same host as the Web server that delivered the applet.