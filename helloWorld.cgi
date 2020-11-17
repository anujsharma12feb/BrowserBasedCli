#!/bin/bash
echo "Content-type: text/html"
echo ""
echo "<html><head><title>Browser based CLI over CGI"
echo "</title></head><body>"

echo "<h1>Hello world</h1>"
echo "<p>"
echo "<center><h2>"
echo "User's OS is: "
uname -o
echo "</center></h2>"
echo "<p>"
echo "Enjoy using CLI by just adding your desired commands in *.cgi file!!"

echo "</body></html>"
