<h2>Script name: reverse_shell</h2>
<h4>Description:</h4>
<p>Gain access to a remote machine using reverse shell in python</P>
<p>The server.py file should be installed on the attacker<br>
machine while the client.py runs on the target(victim) machine</p>
<br>
<b>Note:The server.py contains your IP address while the client.py <br>
contains the ip address of the server</b>

<h5>Testing</h5>
<p>The scripts have been tested on <b>kali linux</b> as the attacker and <br><b>windows 10</b> machine as the victim</p>
<h4>Requirements</h4>
<pre>Python3 should be installed on both machines
Download all the libraries used in the script:
	1.pyautogui - used for screenshots
	2.subprocess - used for executing commands on the shell
	3.socket     - used to communicate over the network
</pre>	
<b>To install the libraries</b>
<i>pip3 install pyautogui</i>

<h4>Installation</h4>
<pre><p>
To run the scripts extract the files/clone this repo to your machine
<b>Edit the two files to set the servers ip</b>
<p>you can leave the port as it is</p>
<p><b>python3 server.py</b>This runs the server which now listens<br>
for any incoming connections</p>
<p>To run the windows side you can convert the client.py to an executable<br>file or simply run it through an IDE of your choice for testing purpose</p>
<p><b>Available options</b></p>
<p>when your run <b>python3 server.py</b> the server waits for <br>
a connection from a victim</p>
<p>Once a connection is established we get a shell which we can <br> run
commands as if we are physically on the victims machine<p>
<p>To run other commands such as <b>download</b> files from victim<br>
and to take a <b>screenshot</b> from the victims screen <br>
we only need to specify on the shell ie:
<pre> #download file.pdf</pre><p>This downloads the file.pdf to your attackers machine with same name</p>
<pre> #screen </pre><p>This will take a screenshot of the victims screen<br>
and save it on the attackers machine with <b>current time</b> as the file name</p>

<h4><b>This script is for education purpose only am not liable for any damages</b></h4>

<h5>contribution</h5>
<p>Any contributions or changes are highly welcomed<br>Folk the repo and perform the changes you deem necessary then do a pull requests <br>
and your changes will be incorporated.<br>Any issues raised will also be looked into</p>
<h5>AUTHOR</h5>
<p>peter-macharia</p>
