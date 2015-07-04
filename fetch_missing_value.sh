#!/bin/bash

ID_LIST=$(cat fund-id.txt) 

TODAY=$(cat data/hist/last)
START=$(date -j -v-10y -f "%Y-%m-%d" $TODAY "+%Y-%m-%d")

OUTPUT_DIR=data/hist

#for ID in $ID_LIST 
#do
#	length=$(wc -l $OUTPUT_DIR/${ID}.txt | awk '{print $1;}')
#	if [ $length -eq 0 ]
#	then
#		echo "$ID" >> /tmp/missing
#	fi
#
#done

wc /tmp/missing
ID_LIST=$(cat /tmp/missing) 
max=500
init=0
for ID in $ID_LIST 
do
	    init=$((init+1))
	    if [ $init -gt $max ]
	    then
	    	break
	    fi
		echo "Processing missing fund: $ID"
	    curl -s "http://vip.fundxy.com/fundxy/Curve/ClientCurveService.asmx/GetCurveDayVar?FundID=${ID}&CurveType=1&Width=540&Height=320&StartDate=${START}&EndDate=${TODAY}" > $OUTPUT_DIR/$ID.txt &
done
echo "$init jobs sent to the background. Run 'ps | grep curl | wc -l' for status"