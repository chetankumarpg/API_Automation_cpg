echo -e "\n\n============================"
echo "============Struct Name tacacsplus:server============"
echo "Test Case:1"
echo "Create a new tacacsplus:server"
echo "Command Used:"
echo "curl -k1 -u admin:infoblox -H content-type:application/json https://10.35.118.15/wapi/v2.7/tacacsplus:authservice -d '{"name": "admin","servers": [{"address": "10.39.39.45","auth_type": "CHAP","disable": false,"port": 49,"use_accounting": false,"use_mgmt_port": false,"shared_secret": "test"}]}' -X POST"
echo -e "\n\n Result"
curl -k1 -u admin:infoblox -H content-type:application/json https://10.35.118.15/wapi/v2.7/tacacsplus:authservice -d '{"name": "admin","servers": [{"address": "10.39.39.45","auth_type": "CHAP","disable": false,"port": 49,"use_accounting": false,"use_mgmt_port": false,"shared_secret": "test"}]}' -X POST
echo -e "\n\n============================"
