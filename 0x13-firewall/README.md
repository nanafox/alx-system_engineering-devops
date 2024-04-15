# Firewall

This project is on configuring a firewall on my linux web servers. The firewall
is configured using `ufw`.

Only the following ports are allowed:
- 22 (SSH)
- 80 (HTTP)
- 443 (HTTPS)

The firewall is configured to deny all incoming and outgoing traffic by default.

Port forwarding is configured to forward traffic from port 8080 to port 80.
