#!/bin/bash

ID_LIST=$(cat fund-id.txt) 

TODAY=$(date +"%Y-%m-%d")
START=$(date -j -v-10y -f "%Y-%m-%d" $TODAY "+%Y-%m-%d")

OUTPUT_DIR=data/hist

mkdir -p $OUTPUT_DIR

for ID in $ID_LIST 
do
	echo "Processing fund: $ID"
	curl -s "http://vip.fundxy.com/fundxy/Curve/ClientCurveService.asmx/GetCurveDayVar?FundID=${ID}&CurveType=1&Width=540&Height=320&StartDate=${START}&EndDate=${TODAY}" > $OUTPUT_DIR/$ID.txt
done

echo "See more in ${OUTPUT_DIR}"