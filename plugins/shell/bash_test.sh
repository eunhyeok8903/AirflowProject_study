VAR=$1
if [ $VAR == test1 ];then
	echo "--TEST1--"
elif [ $VAR == test2 ];then
	echo "--TEST2--"
else
	echo "--TEST--"
fi
