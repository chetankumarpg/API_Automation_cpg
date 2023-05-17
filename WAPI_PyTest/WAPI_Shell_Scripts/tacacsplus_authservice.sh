echo -e "\n\n============================"
echo "============Object Name tacacsplus:authservice============"
echo "Test Case:1"
echo "Test the format of tacacsplus:authservice object."
echo "Command Used:"
echo "Command: curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infobloxhttps://10.35.118.15/wapi/v2.7/tacacsplus:authservice?_return_fields=name,servers"
echo -e "\n\n Result"
curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?_return_fields=name,servers
echo -e "\n\n============================"


echo "Test Case:2"
echo "Test the restriction for the tacacsplus:authservice object -Scheduling"
echo "Command Used:"
echo "curl -k1 -u admin:infoblox -X POST https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?_schedinfo.scheduled_time=1924223800"
echo -e "\n\n Result"
curl -k1 -u admin:infoblox -X POST https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?_schedinfo.scheduled_time=1924223800
echo -e "\n\n============================"


echo "Test Case:3"
echo "Test the restriction for the tacacsplus:authservice object - CSV Export"
echo "Command Used:"
echo "curl -k1 -u admin:infoblox -H 'content-type:application/json' -X POST -w 'Response code:%{http_code}' https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?_function=csv_export"
echo -e "\n\n Result"
curl -k1 -u admin:infoblox -H 'content-type:application/json' -X POST -w 'Response code:%{http_code}' https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?_function=csv_export
echo -e "\n\n============================"


echo "Test Case:4"
echo "Test the _return_fields for default values in tacacsplus:authservice  object"
echo "Command Used:"
echo "curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice -X GET"
echo -e "\n\n Result"
curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice -X GET
echo -e "\n\n============================"


echo "Test Case:5"
echo "Peform CREATE operation on tacacsplus object"
echo "Command Used:"
echo "curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice -d '{"name": "admin","servers": [{"address": "10.39.39.45","shared_secret":"hello"}]}' -X POST"
echo -e "\n\n Result"
curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice -d '{"name": "admin","servers": [{"address": "10.39.39.45","shared_secret":"hello"}]}' -X POST
echo -e "\n\n============================"



echo "Test Case:6"
echo "Test the fields are required to create this object -1"
echo "Command Used:"
echo "curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice -d '{"servers": [{"address": "10.39.39.45","shared_secret":"hello"}]}' -X POST"
echo -e "\n\n Result"
curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice -d '{"servers": [{"address": "10.39.39.45","shared_secret":"hello"}]}' -X POST
echo -e "\n\n============================"



echo "Test Case:7"
echo "Test the fields are required to create this object -2"
echo "Command Used:"
echo "curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice -d '{"name": "admin"}' -X POST"
echo -e "\n\n Result"
curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice -d '{"name": "admin"}' -X POST
echo -e "\n\n============================"



echo "Test Case:8"
echo "Test the acct_retries field in tacacsplus:authservice object"
echo "Command Used:"
echo "curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?_return_fields=acct_retries"
echo -e "\n\n Result"
curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?_return_fields=acct_retries
echo -e "\n\n============================"



echo "Test Case:9"
echo "perform search for acct_retries field with different type of search modifiers-1"
echo "Command Used:"
echo "curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?acct_timeout=1000"
echo -e "\n\n Result"
curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?acct_timeout=1000
echo -e "\n\n============================"




echo "Test Case:10"
echo "perform search for acct_retries field with different type of search modifiers-2"
echo "Command Used:"
echo "curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?acct_timeout:=1000"
echo -e "\n\n Result"
curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?acct_timeout:=1000
echo -e "\n\n============================"


echo "Test Case:11"
echo "perform search for acct_retries field with different type of search modifiers-3"
echo "Command Used:"
echo "curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?acct_timeout~=1000"
echo -e "\n\n Result"
curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?acct_timeout~=1000
echo -e "\n\n============================"


echo "Test Case:12"
echo "Test the acct_timeout field in tacacsplus:authservice object"
echo "Command Used:"
echo "curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?_return_fields=acct_timeout"
echo -e "\n\n Result"
curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?_return_fields=acct_timeout
echo -e "\n\n============================"



echo "Test Case:13"
echo "perform search for acct_timeout field with different type of search modifiers-1"
echo "Command Used:"
echo "curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?acct_timeout=1000"
echo -e "\n\n Result"
curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?acct_timeout=1000
echo -e "\n\n============================"


echo "Test Case:14"
echo "perform search for acct_timeout field with different type of search modifiers-2"
echo "Command Used:"
echo "curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?acct_timeout:=1000"
echo -e "\n\n Result"
curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?acct_timeout:=1000
echo -e "\n\n============================"



echo "Test Case:15"
echo "perform search for acct_timeout field with different type of search modifiers-3"
echo "Command Used:"
echo "curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?acct_timeout~=1000"
echo -e "\n\n Result"
curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?acct_timeout~=1000
echo -e "\n\n============================"



echo "Test Case:16"
echo "Test the auth_retries field in tacacsplus:authservice object"
echo "Command Used:"
echo "curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?_return_fields=auth_retries"
echo -e "\n\n Result"
curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?_return_fields=auth_retries
echo -e "\n\n============================"




echo "Test Case:17"
echo "perform search for auth_retries field with different type of search modifiers-1"
echo "Command Used:"
echo "curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?auth_retries=0"
echo -e "\n\n Result"
curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?auth_retries=0
echo -e "\n\n============================"




echo "Test Case:18"
echo "perform search for auth_retries field with different type of search modifiers-2"
echo "Command Used:"
echo "curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?auth_retries:=0"
echo -e "\n\n Result"
curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?auth_retries:=0
echo -e "\n\n============================"


echo "Test Case:19"
echo "perform search for auth_retries field with different type of search modifiers-3"
echo "Command Used:"
echo "curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?auth_retries~=0"
echo -e "\n\n Result"
curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?auth_retries~=0
echo -e "\n\n============================"


echo "Test Case:20"
echo "Test the auth_timeout field in tacacsplus:authservice object"
echo "Command Used:"
echo "curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?_return_fields=auth_timeout"
echo -e "\n\n Result"
curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?_return_fields=auth_timeout
echo -e "\n\n============================"


echo "Test Case:21"
echo "perform search for auth_timeout field with different type of search modifiers-1"
echo "Command Used:"
echo "curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?auth_timeout=5000"
echo -e "\n\n Result"
curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?auth_timeout=5000
echo -e "\n\n============================"


echo "Test Case:22"
echo "perform search for auth_timeout field with different type of search modifiers-2"
echo "Command Used:"
echo "curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?auth_timeout:=5000"
echo -e "\n\n Result"
curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?auth_timeout:=5000
echo -e "\n\n============================"


echo "Test Case:23"
echo "perform search for auth_timeout field with different type of search modifiers-3"
echo "Command Used:"
echo "curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?auth_timeout~=5000"
echo -e "\n\n Result"
curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?auth_timeout~=5000
echo -e "\n\n============================"


echo "Test Case:24"
echo "Test the comment field in tacacsplus:authservice object"
echo "Command Used:"
echo "curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?_return_fields=comment"
echo -e "\n\n Result"
curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?_return_fields=comment
echo -e "\n\n============================"


echo "Test Case:25"
echo "perform search for comment field with different type of search modifiers-1"
echo "Command Used:"
echo "curl -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/tacacsplus:authservice -d comment="QA_Testing""
echo -e "\n\n Result"
curl -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/tacacsplus:authservice -d comment="QA_Testing"
echo -e "\n\n============================"


echo "Test Case:26"
echo "perform search for comment field with different type of search modifiers-2"
echo "Command Used:"
echo "curl -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/tacacsplus:authservice -d comment:="qA_Testing""
echo -e "\n\n Result"
curl -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/tacacsplus:authservice -d comment:="qA_Testing"
echo -e "\n\n============================"


echo "Test Case:27"
echo "perform search for comment field with different type of search modifiers-3"
echo "Command Used:"
echo "curl -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/tacacsplus:authservice -d comment:="qA_Testing""
echo -e "\n\n Result"
curl -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/tacacsplus:authservice -d comment:="qA_Testing"
echo -e "\n\n============================"


echo "Test Case:28"
echo "Determines whether the TACACS+ authentication service object is disabled"
echo "Command Used:"
echo "curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?_return_fields=disable"
echo -e "\n\n Result"
curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?_return_fields=disable
echo -e "\n\n============================"


echo "Test Case:29"
echo "perform search for disable field with different type of search modifiers-1"
echo "Command Used:"
echo "curl -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/tacacsplus:authservice -d disable=false"
echo -e "\n\n Result"
curl -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/tacacsplus:authservice -d disable=false
echo -e "\n\n============================"



echo "Test Case:30"
echo "perform search for disable field with different type of search modifiers-2"
echo "Command Used:"
echo "curl -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/tacacsplus:authservice -d disable:=false"
echo -e "\n\n Result"
curl -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/tacacsplus:authservice -d disable:=false
echo -e "\n\n============================"



echo "Test Case:31"
echo "perform search for disable field with different type of search modifiers-3"
echo "Command Used:"
echo "curl -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/tacacsplus:authservice -d disable~=false"
echo -e "\n\n Result"
curl -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/tacacsplus:authservice -d disable~=false
echo -e "\n\n============================"


echo "Test Case:32"
echo "Test the name field in tacacsplus:authservice object"
echo "Command Used:"
echo "curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?_return_fields=name"
echo -e "\n\n Result"
curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?_return_fields=name
echo -e "\n\n============================"


echo "Test Case:33"
echo "perform search for name field with different type of search modifiers-1"
echo "Command Used:"
echo "curl -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/tacacsplus:authservice -d name=admin"
echo -e "\n\n Result"
curl -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/tacacsplus:authservice -d name=admin
echo -e "\n\n============================"



echo "Test Case:34"
echo "perform search for name field with different type of search modifiers-2"
echo "Command Used:"
echo "curl -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/tacacsplus:authservice -d name:=ADmin"
echo -e "\n\n Result"
curl -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/tacacsplus:authservice -d name:=ADmin
echo -e "\n\n============================"


echo "Test Case:35"
echo "perform search for name field with different type of search modifiers-3"
echo "Command Used:"
echo "curl -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/tacacsplus:authservice -d name~=adm*"
echo -e "\n\n Result"
curl -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/tacacsplus:authservice -d name~=adm*
echo -e "\n\n============================"


echo "Test Case:36"
echo "Test the servers field in tacacsplus:authservice object"
echo "Command Used:"
echo "curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?_return_fields=servers"
echo -e "\n\n Result"
curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/tacacsplus:authservice?_return_fields=servers
echo -e "\n\n============================"


echo "Test Case:37"
echo "perform search for servers field with different type of search modifiers-1"
echo "Command Used:"
echo "curl -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/tacacsplus:authservice -d servers=10.35.118.15"
echo -e "\n\n Result"
curl -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/tacacsplus:authservice -d servers=10.35.118.15
echo -e "\n\n============================"


echo "Test Case:38"
echo "perform search for servers field with different type of search modifiers-2"
echo "Command Used:"
echo "curl -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/tacacsplus:authservice -d servers:=10.35.118.15"
echo -e "\n\n Result"
curl -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/tacacsplus:authservice -d servers:=10.35.118.15
echo -e "\n\n============================"


echo "Test Case:39"
echo "perform search for servers field with different type of search modifiers-3"
echo "Command Used:"
echo "curl -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/tacacsplus:authservice -d servers~=10.35.118.15"
echo -e "\n\n Result"
curl -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/tacacsplus:authservice -d servers~=10.35.118.15
echo -e "\n\n============================"













