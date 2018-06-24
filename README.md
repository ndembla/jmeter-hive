Steps:
1. Download Apache Jmeter. 
2. Copy the *jar files from /usr/hdp/current/hive-server2-hive2/lib (your relevant dir) into jmeter/lib and jmeter/lib/ext directories.
3. Download hive-jdbc-2.1.0-SNAPSHOT-standalone.jar. Save it to a directory and add that directory to the Jmeter class path in your jmx file

Example:
      <stringProp name="TestPlan.user_define_classpath">./jdbc-binaries/hive-jdbc-2.1.0-SNAPSHOT-standalone.jar,/home/ndembla/jmeter/lib</stringProp>
      
4. Change the following in the jmx file based on your setup

	Add your jdbc url to this property
 	<stringProp name="dbUrl">jdbc:hive2://localhost:10007/tpcds_bin_partitioned_orc_10000?hive.exec.orc.split.strategy=BI</stringProp> 
5. Set Jmeter heapsize to prevent jmeter crashing on queries returning large resultsets
export _JAVA_OPTIONS="-Djava.awt.headless=true -Xmx8192m"
6. Run jmeter -n -t llap-test.jmx. Look at jmeter.log for any errors reported.
7. Run "python report_2.py  raw_llap_1468573258.xml > results.csv" to get a csv format of queries and 4 runs of runtimes.
