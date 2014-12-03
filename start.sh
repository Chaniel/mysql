#!/bin/bash

base_dir=/data/mysql-1
$base_dir/bin/mysqld --defaults-file=$base_dir/my.cnf --basedir=$base_dir --datadir=$base_dir/data --plugin-dir=$base_dir/lib/plugin --user=mysql --log-error=$base_dir/data/SHUBEI-1-100.err --pid-file=$base_dir/data/SHUBEI-1-100.pid --socket=$base_dir/data/mysql.sock &


#/bin/sh bin/mysqld_safe --defaults-file=my.cnf

#Restart them with the --skip-slave-start option so that they do not connect to the master. Perform any table repair or rebuilding operations needed to re-create database objects, 
#use the --skip-networking option when you restart the master.
# --skip-grant-tables 
# for upgrade mysql replication.
