1. copy data manually from http://www.fundxy.com/newvalue.asp to list-of-fund.txt
2. replace all tabs with spaces in a text editor
3. awk '{print $3;}' list-of-fund.txt > fund-id.txt
4. run ./fetch_hist_value.sh
