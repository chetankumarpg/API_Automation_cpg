Need to Execute using below Command.
Eg :
python run.py -m 10.35.119.4:10.35.119.8:10.35.119.6 -v 2.6

10.35.119.4 - Grid Master.
10.35.119.8 - Grid Member 1.
10.35.119.6 - Grid Member 2.

2.6 - WAPI Version
It will change based on the Build.

run.py will do addkeys, automatically changing the Grid IP's inside the config.py and it will start executing pytest file for both licensing and profiling automation.

For licensing automation it will create licensing.log
For Profiling automation it will create profiling.log

How to Execute py.test file 
py.test WAPI82_Automation/test_grid_filedistribution.py -vv

If you need html Report then need to execute in following method
py.test WAPI82_Automation/test_grid_filedistribution.py --tb=long --html=profiling_report.html --junit-xml=profiling_results.xml -vv

At now for manually set the grid ip in config.py file ( config.py is available in FR folder )
