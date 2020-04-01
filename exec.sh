#!/bin/bash
chmod +x $1
cat $1 | sudo mysql -hlocalhost -uroot -pa $2