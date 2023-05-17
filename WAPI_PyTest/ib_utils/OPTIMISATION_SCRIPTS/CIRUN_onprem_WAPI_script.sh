#!/bin/bash

# args = [Master1_IP]
######## [${args[0]}]
args=("$@")

All_Master_IP=${args[0]}

client_ip=$(echo "$NODE_NAME" | cut -d- -f3)
echo $client_ip

set +x
set -x
###################### Add keys ######################
count=0
IFS=':' #setting space as delimiter
read -ra IP <<<"$All_Master_IP" #reading str as an array as tokens separated by IFS

for i in "${IP[@]}"; #accessing each element of array
do
echo ">> Performing addkeys for $i <<"
addkeys $i

count=$((count+1))
done

echo ">> End of addkeys <<"
echo "TOTAL GRID MASTERS = "$count

Master_IP=${IP[0]}
##################### End of Addkeys ###################

sleep 20

wapi_version=`/import/qaddi/sramanathan/IBQACI/get_wapi_version $Master_IP`
export PYTHONPATH=$PYTHONPATH:$WORKSPACE/API_Automation/WAPI_PyTest
echo $PYTHONPATH

cd $WORKSPACE/API_Automation/WAPI_PyTest/suites/$SUITE_NAME

######################## Configuration Generator ################################
#### Generating Configuration.xml ####
c=1
file_exec="${WORKSPACE}/API_Automation/WAPI_PyTest/ib_utils/OPTIMISATION_SCRIPTS/grid_configuration_generator.py file=${POOL_DIR}/GRID_1.xml"

while [ $c -lt $count ]
do
    # increment the value
    c=`expr $c + 1`

    # Print the values
    echo "c=$c and count=$count"

    # Concatinating xml file

    file_exec="$file_exec,${POOL_DIR}/GRID_$c.xml"
done

echo $file_exec
eval "python $file_exec"

#### Generating config.py using Configuration.xml ####
echo ">> Printing custom_config.yaml below <<"
cat custom_config.yaml

python ${WORKSPACE}/API_Automation/WAPI_PyTest/ib_utils/OPTIMISATION_SCRIPTS/generate_wapi_configs.py

echo -e "wapi_version=\"${wapi_version}\"" >> config.py
echo -e "grid_vip=\"${Master_IP}\"" >> config.py
echo -e "client_ip=\"${client_ip}\"" >> config.py
echo -e "client_user=\"${NODE_USER}\"" >> config.py

cat config.py
################################ End of Configuration Generator ##########################################


pytest ${SUITE_NAME}.py -vss -rP -rF --html=${SUITE_NAME}_report.html --junit-xml=${SUITE_NAME}_results.xml -vv || true

sed -i 's/="pytest"/="$SUITE_NAME_results"/g' $SUITE_NAME_results.xml


cp -rf ${SUITE_NAME}_results.xml SUMMARY_reporting_portal_junit.xml

python /import/qaddi/sramanathan/IBQACI/remove_timestamp_junit.py SUMMARY_reporting_portal_junit.xml


echo "JOB_OWNER: '${JOB_OWNER}'"
echo "nios_version: '${nios_version}'"
zip "${JOB_NAME}_${JOB_OWNER}_${nios_version}.zip" SUMMARY_reporting_portal_junit.xml
cp SUMMARY_reporting_portal_junit.xml $WORKSPACE/

Reporting_portal_Access_token_id=$(python /import/qaddi/API_Automation/aws_scripts_automation/reporting_portal_details_onprem.py rp_token_id)
Reporting_portal_ip=$(python /import/qaddi/API_Automation/aws_scripts_automation/reporting_portal_details_onprem.py rp_ip)
Reporting_portal_project_name=$(python /import/qaddi/API_Automation/aws_scripts_automation/reporting_portal_details_onprem.py rp_project_name)

curl -X POST --header 'Content-Type: multipart/form-data' --header 'Accept: application/json' --header "Authorization: $Reporting_portal_Access_token_id" -F file=@"${JOB_NAME}_${JOB_OWNER}_${nios_version}.zip" "$Reporting_portal_ip$Reporting_portal_project_name"



##########Core and log vaildation,capture support bundle,email notification to owner and release appliances script added here ######################
client_ip=$(echo "$NODE_NAME" | cut -d- -f3)
echo $client_ip


python /import/qaddi/API_Automation/aws_scripts_automation/validate_logs_core_files_onprem.py $Master_IP ${JOB_NAME} $client_ip ${NODE_USER} infoblox ${nios_version} $USER ${Email_List}

############# Releasing the grids ##############

if [ $RELEASE_GRIDS == "NO" ]
then
  echo "Saving VMs for debugging - GRIDS ARE NOT RELEASED!"
else
  n=0
  while [ $n -lt $count ]
  do
    # increment the value
    n=`expr $n + 1`

    # Print the values
    echo "n=$n and count=$count"

    # Releasing Grids
    release="/import/tools/qa/bin/release_grid -P $POOL_DIR -T GRID_$n"
    echo $release
    eval $release
 done
 echo ">> Removing the folders... <<"
 eval "rm -rf ~/API_Automation"
 eval "rm -rf ${POOL_DIR}"
 eval "find ${WORKSPACE} -type f -not -name SUMMARY_reporting_portal_junit.xml -delete"

fi



