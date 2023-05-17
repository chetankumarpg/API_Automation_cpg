echo "Case:1"
echo "Test the remoteddnszone structure"

echo "Command : curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/networkview -d '{"name": "Testing","remote_forward_zones": [{"fqdn": "asm123.com","gss_tsig_dns_principal": "saklfjlk","gss_tsig_domain": "AD-21.LOCAL","key_type": "GSS-TSIG","server_address": "10.39.39.45"}]}' -X POST"

echo -e "\n\n Result"

curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/networkview -d '{"name": "Testing","remote_forward_zones": [{"fqdn": "asm123.com","gss_tsig_dns_principal": "saklfjlk","gss_tsig_domain": "AD-21.LOCAL","key_type": "GSS-TSIG","server_address": "10.39.39.45"}]}' -X POST
echo -e "\n\n"


echo "Case:2"
echo " Test the fqdn field in remoteddnszone structure "
echo "Command : curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/networkview -d '{"name": "Infoblox","remote_forward_zones": [{"gss_tsig_dns_principal": "test","gss_tsig_domain": "AD-21.LOCAL","key_type": "GSS-TSIG","server_address": "10.0.0.2"}]}' -X POST"

echo -e "\n\n Result"

curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/networkview -d '{"name": "Infoblox","remote_forward_zones": [{"gss_tsig_dns_principal": "test","gss_tsig_domain": "AD-21.LOCAL","key_type": "GSS-TSIG","server_address": "10.0.0.2"}]}' -X POST
echo -e "\n\n"


echo "Case:3"
echo "Test the gss_tsig_dns_principal field in remoteddnszon structure"
echo " Command: curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/networkview -d '{"name": "Infoblox","remote_forward_zones": [{"fqdn": "infoblox.com","gss_tsig_dns_principal": 123 ,"gss_tsig_domain": "AD-21.LOCAL","key_type": "GSS-TSIG","server_address": "10.0.0.2"}]}' -X POST"

echo -e "\n\n Result"

curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/networkview -d '{"name": "Infoblox","remote_forward_zones": [{"fqdn": "infoblox.com","gss_tsig_dns_principal": 123 ,"gss_tsig_domain": "AD-21.LOCAL","key_type": "GSS-TSIG","server_address": "10.0.0.2"}]}' -X POST
echo -e "\n\n"


echo "Case:4"
echo "Test the gss_tsig_domain field in remoteddnszon structure "

echo "curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/networkview -d '{"name": "Infoblox","remote_forward_zones": [{"fqdn": "infoblox.com","gss_tsig_dns_principal": "test","gss_tsig_domain": 1234,"key_type": "GSS-TSIG","server_address": "10.0.0.2"}]}' -X POST"

echo -e "\n\n Result"

curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/networkview -d '{"name": "Infoblox","remote_forward_zones": [{"fqdn": "infoblox.com","gss_tsig_dns_principal": "test","gss_tsig_domain": 1234,"key_type": "GSS-TSIG","server_address": "10.0.0.2"}]}' -X POST
echo -e "\n\n"

echo "Case:5"
echo "Test the key_type field in remoteddnszon structure"
echo "Command: curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/networkview -d '{"name": "Infoblox","remote_forward_zones": [{"fqdn": "infoblox.com","gss_tsig_dns_principal": "test","gss_tsig_domain": "AD-21.LOCAL","key_type": "ASM","server_address": "10.0.0.2"}]}' -X POST"

echo -e "\n\n Result"

curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/networkview -d '{"name": "Infoblox","remote_forward_zones": [{"fqdn": "infoblox.com","gss_tsig_dns_principal": "test","gss_tsig_domain": "AD-21.LOCAL","key_type": "ASM","server_address": "10.0.0.2"}]}' -X POST
echo -e "\n\n"

echo "Case:6"
echo " Test the server_address field in remoteddnszon structure"

echo "Command: curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/networkview -d '{"name": "Infoblox","remote_forward_zones": [{"fqdn": "infoblox.com","gss_tsig_dns_principal": "test","gss_tsig_domain": "AD-21.LOCAL","key_type": "GSS-TSIG"}]}' -X POST"

echo -e "\n\n Result"

curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/networkview -d '{"name": "Infoblox","remote_forward_zones": [{"fqdn": "infoblox.com","gss_tsig_dns_principal": "test","gss_tsig_domain": "AD-21.LOCAL","key_type": "GSS-TSIG"}]}' -X POST
echo -e "\n\n"

echo "Case:7"
echo " Test the server_address field in remoteddnszon structure"

echo "Command :curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/networkview -d '{"name": "Infoblox","remote_forward_zones": [{"fqdn": "infoblox.com","gss_tsig_dns_principal": "test","gss_tsig_domain": "AD-21.LOCAL","key_type": "GSS-TSIG","server_address": "10.0.A.2"}]}' -X POST"

echo -e "\n\n Result"

curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/networkview -d '{"name": "Infoblox","remote_forward_zones": [{"fqdn": "infoblox.com","gss_tsig_dns_principal": "test","gss_tsig_domain": "AD-21.LOCAL","key_type": "GSS-TSIG","server_address": "10.0.A.2"}]}' -X POST
echo -e "\n\n"


echo "Case:8"
echo " Test the tsig_key field in remoteddnszon structure"

echo "Command : curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/networkview -d '{"name": "Infoblox","remote_forward_zones": [{"fqdn": "infoblox.com","gss_tsig_dns_principal": "test","gss_tsig_domain": "AD-21.LOCAL","key_type": "TSIG","server_address": "10.0.0.2","tsig_key": 1234,"tsig_key_alg": "HMAC-MD5","tsig_key_name": "test"}]}' -X POST"

echo -e "\n\n Result"

curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/networkview -d '{"name": "Infoblox","remote_forward_zones": [{"fqdn": "infoblox.com","gss_tsig_dns_principal": "test","gss_tsig_domain": "AD-21.LOCAL","key_type": "TSIG","server_address": "10.0.0.2","tsig_key": 1234,"tsig_key_alg": "HMAC-MD5","tsig_key_name": "test"}]}' -X POST
echo -e "\n\n"


echo "Case:9"
echo "Test the tsig_key_alg field in remoteddnszon structure"

echo "Command : curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/networkview -d '{"name": "Infoblox","remote_forward_zones": [{"fqdn": "infoblox.com","gss_tsig_dns_principal": "test","gss_tsig_domain": "AD-21.LOCAL","key_type": "TSIG","server_address": "10.0.0.2","tsig_key": "lDenNrBKS7JMqodB0I703ldthZloYcwMycdS4vqWiOY=","tsig_key_alg": true,"tsig_key_name": "test"}]}' -X POST"

echo -e "\n\n Result"

curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/networkview -d '{"name": "Infoblox","remote_forward_zones": [{"fqdn": "infoblox.com","gss_tsig_dns_principal": "test","gss_tsig_domain": "AD-21.LOCAL","key_type": "TSIG","server_address": "10.0.0.2","tsig_key": "lDenNrBKS7JMqodB0I703ldthZloYcwMycdS4vqWiOY=","tsig_key_alg": true,"tsig_key_name": "test"}]}' -X POST

echo -e "\n\n"

echo "Case:10"
echo "Test the tsig_key_name field in remoteddnszon structure"
	
echo "Command : curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/networkview -d '{"name": "Infoblox","remote_forward_zones": [{"fqdn": "infoblox.com","gss_tsig_dns_principal": "test","gss_tsig_domain": "AD-21.LOCAL","key_type": "TSIG","server_address": "10.0.0.2","tsig_key": "lDenNrBKS7JMqodB0I703ldthZloYcwMycdS4vqWiOY=","tsig_key_alg": "HMAC-MD5","tsig_key_name": true}]}' -X POST"

echo -e "\n\n Result"	

curl -H "Content-Type: application/json" -k1 -w 'Response code:%{http_code}' -u admin:infoblox https://10.35.118.15/wapi/v2.7/networkview -d '{"name": "Infoblox","remote_forward_zones": [{"fqdn": "infoblox.com","gss_tsig_dns_principal": "test","gss_tsig_domain": "AD-21.LOCAL","key_type": "TSIG","server_address": "10.0.0.2","tsig_key": "lDenNrBKS7JMqodB0I703ldthZloYcwMycdS4vqWiOY=","tsig_key_alg": "HMAC-MD5","tsig_key_name": true}]}' -X POST	

echo -e "\n\n"
