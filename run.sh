#export PATH=/home/ec2-user/apache-jmeter-5.2.1/bin:$PATH
export _JAVA_OPTIONS="-Djava.awt.headless=true -Xmx8192m"
/home/ec2-user/apache-jmeter-5.2.1/bin/jmeter -n -t llap-test.jmx
