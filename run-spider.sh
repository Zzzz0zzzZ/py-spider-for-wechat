echo "-------------------------------get_urls-------------------------------"
python ./getAllUrls.py
wait

echo "--------------------------get_content_by_urls--------------------------"
python ./getContentsByUrls-MultiThread.py
wait

echo "---------------------------convert time-stamp--------------------------"
python ./getRealTimeByTimeStamp.py
wait

echo "-------------------------------selecting-------------------------------"
python ./getTitleByKeywords.py

echo "---------------------------------done----------------------------------"
read -n 1
