# Web Stack Debugging #0

## Description

The purpose of this project is to learn how to debug a web stack. In this case, we are debugging a web server that is not working properly.
The web server is running Apache and the server is not returning the correct page.

## Observations

On my Ubuntu 22.04 LTS, I received the error `curl: (56) Recv failure: Connection reset by peer`
when trying to access the server. This error is caused by the server not returning the correct page.

## Solution

The solution to this problem is to start the Apache server. To do this, run the following command:

```bash
sudo service apache2 start
```
