1. copy data manually from http://www.fundxy.com/newvalue.asp to list-of-fund.txt
2. replace all tabs with spaces in a text editor
3. awk '{print $3;}' list-of-fund.txt > fund-id.txt
4. run ./fetch_hist_value.sh
5. run python xml_to_yml.py
6. run ./fetch_missing_value.sh
Repeat step 5-6 if there is still any misssing data