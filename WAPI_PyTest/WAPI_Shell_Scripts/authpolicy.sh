echo -e "\n\n============================"

echo "Test Case:1"
echo "Create A new authpolicy"

echo "Command : curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/authpolicy -d '{"admin_groups": "admin-group","auth_services":["localuser:authservice/Li5sb2NhbF91c2VyX2F1dGhfc2VydmljZSRk:Local%20Admin"],"default_group":"cloud-api-only","usage_type": "FULL"}' -X POST"

echo -e "\n\n Result"

curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/authpolicy -d '{"admin_groups": "admin-group","auth_services":["localuser:authservice/Li5sb2NhbF91c2VyX2F1dGhfc2VydmljZSRk:Local%20Admin"],"default_group":"cloud-api-only","usage_type": "FULL"}' -X POST

echo -e "\n\n============================"



echo "Test Case:2"
echo "Test the format of authpolicy object"

echo "Command : curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/authpolicy"

echo -e "\n\n Result"

curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/authpolicy

echo -e "\n\n============================"



echo "Test Case:3"
echo "Test the restriction for the authentication policy object - CSV Export"

echo "Command : curl -k1 -u admin:infoblox -H 'content-type:application/json' -X POST -w 'Response code:%
{http_code}' https://10.35.118.15/wapi/v2.7/authpolicy?_function=csv_export"

echo -e "\n\n Result"

curl -k1 -u admin:infoblox -H 'content-type:application/json' -X POST -w 'Response code:%{http_code}' https://10.35.118.15/wapi/v2.7/authpolicy?_function=csv_export


echo -e "\n\n============================"



echo "Test Case:4"
echo "Test the restriction for the authentication policy object - Scheduling"

echo "Command : curl -k1 -u admin:infoblox -H 'content-type:application/json' -X POST -w 'Response code:%{http_code}' https://10.35.118.15/wapi/v2.7/authpolicy?_schedinfo.scheduled_time=1496390800"

echo -e "\n\n Result"

curl -k1 -u admin:infoblox -H 'content-type:application/json' -X POST -w 'Response code:%{http_code}' https://10.35.118.15/wapi/v2.7/authpolicy?_schedinfo.scheduled_time=1496390800

echo -e "\n\n============================"



echo "Test Case:5"
echo "Test the restriction for the authentication policy object - Global search"

echo "Command : curl -k1 -u admin:infoblox -H 'content-type:application/json' -w 'Response code:%{http_code}' https://10.35.118.15//wapi/v2.7/search?search_string=admin-group -X GET"

echo -e "\n\n Result"

curl -k1 -u admin:infoblox -H 'content-type:application/json' -w 'Response code:%{http_code}' https://10.35.118.15//wapi/v2.7/search?search_string=admin-group -X GET

echo -e "\n\n============================"



echo "Test Case:6"
echo "Test the _return_fields for default values in authentication policy object"

echo "Command : curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/authpolicy"

echo -e "\n\n Result"

curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/authpolicy

echo -e "\n\n============================"





echo "Test Case:7"
echo "Test the admin_groups field in authentication policy object"

echo "Command : curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/authpolicy?_return_fields=admin_groups"

echo -e "\n\n Result"

curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/authpolicy?_return_fields=admin_groups

echo -e "\n\n============================"





echo "Test Case:8"
echo "Check the admin_groups field with different type of search modifiers-1"

echo "Command : curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/authpolicy?admin_groups="admin-group""

echo -e "\n\n Result"

curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/authpolicy?admin_groups="admin-group"

echo -e "\n\n============================"




echo "Test Case:9"
echo "Check the admin_groups field with different type of search modifiers-2"

echo "Command : curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/authpolicy?admin_groups:="admin-group""

echo -e "\n\n Result"

curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/authpolicy?admin_groups:="admin-group"

echo -e "\n\n============================"





echo "Test Case:10"
echo "Check the admin_groups field with different type of search modifiers -3"

echo "Command : curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/authpolicy?admin_groups~="admin-group""

echo -e "\n\n Result"

curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/authpolicy?admin_groups~="admin-group"

echo -e "\n\n============================"





echo "Test Case:11"
echo "Test the default_group field in authentication policy object"

echo "Command : curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/authpolicy?_return_fields=default_group"

echo -e "\n\n Result"

curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/authpolicy?_return_fields=default_group

echo -e "\n\n============================"




echo "Test Case:12"
echo "Test the default_group field in authentication policy object"

echo "Command : curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/authpolicy?_return_fields=default_group"

echo -e "\n\n Result"

curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/authpolicy?_return_fields=default_group

echo -e "\n\n============================"


echo "Test Case:13"
echo "Check the default_group field with different search modifiers-1"

echo "Command : curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/authpolicy?default_group="cloud-api-only""

echo -e "\n\n Result"

curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/authpolicy?default_group="cloud-api-only"

echo -e "\n\n============================"



echo "Test Case:14"
echo "Check the default_group field with different search modifiers-2"

echo "Command : curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/authpolicy?default_group:="cloud-api-only""

echo -e "\n\n Result"

curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/authpolicy?default_group:="cloud-api-only"

echo -e "\n\n============================"



echo "Test Case:15"
echo "Check the default_group field with different search modifiers-3"
echo "Command : curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/authpolicy?default_group~="cloud-api-only""
echo -e "\n\n Result"
curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/authpolicy?default_group~="cloud-api-only"

echo -e "\n\n============================"




echo "Test Case:16"
echo "Test the usage_type field in authentication policy object"

echo "Command : curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/authpolicy?_return_fields=usage_type"
echo -e "\n\n Result"
curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/authpolicy?_return_fields=usage_type

echo -e "\n\n============================"




echo "Test Case:17"
echo "Test the usage_type field in authentication policy object"

echo "Command : curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/authpolicy?_return_fields=usage_type"
echo -e "\n\n Result"
curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/authpolicy?_return_fields=usage_type

echo -e "\n\n============================"




echo "Test Case:18"
echo "Check the usage_type field with different search modifiers-1"

echo "Command : curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/authpolicy?usage_type="FULL""
echo -e "\n\n Result"
curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/authpolicy?usage_type="FULL"

echo -e "\n\n============================"


echo "Test Case:19"
echo "Check the usage_type field with different search modifiers-2"

echo "Command : curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/authpolicy?usage_type:="FULL""
echo -e "\n\n Result"
curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/authpolicy?usage_type:="FULL"

echo -e "\n\n============================"


echo "Test Case:20"
echo "Check the usage_type field with different search modifiers-3"

echo "Command : curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/authpolicy?usage_type~="FULL""
echo -e "\n\n Result"
curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox -X GET https://10.35.118.15/wapi/v2.7/authpolicy?usage_type~="FULL"

echo -e "\n\n============================"









