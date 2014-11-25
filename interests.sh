#!/bin/sh
# interests.sh - find USHL members with particular interests
# injection !!!!

if [ $# -ne 1 ]; 
then
	echo 'please specify one keyword';
	exit;
fi

mysql -t --protocol=tcp -P3308 -u root -p  sampdb <<QUERY_INPUT
select last_name, first_name, email, interests from member
where interests like '%$1%'
order by last_name, first_name;
QUERY_INPUT
