#!/bin/bash

base_dir=/data/mysql-1
$base_dir/bin/mysqld --defaults-file=$base_dir/my.cnf --basedir=$base_dir --datadir=$base_dir/data --plugin-dir=$base_dir/lib/plugin --user=mysql --log-error=$base_dir/data/SHUBEI-1-100.err --pid-file=$base_dir/data/SHUBEI-1-100.pid --socket=$base_dir/data/mysql.sock &
