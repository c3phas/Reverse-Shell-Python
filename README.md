### Script name: reverse_shell
#### Description:
* Gain access to a remote machine using reverse shell in python
* The server.py file should be installed on the attacker
machine while the client.py runs on the target(victim) machine

* Note:The server.py contains your IP address while the client.py <br>
contains the ip address of the server</b>

#### Testing
The scripts have been tested on  kali linux as the attacker and <br><b>windows 10</b> machine as the victim
### Requirements
```
Python3 should be installed on both machines
Download all the libraries used in the script:
	1.pyautogui - used for screenshots
	2.subprocess - used for executing commands on the shell
	3.socket     - used to communicate over the network
	
To install the libraries
pip3 install pyautogui
````
#### Installation

##### To run the scripts extract the files/clone this repo to your machine
* Edit the two files to set the servers ip
* you can leave the port as it is
```$python3 server.py```:This runs the server which now listens<br>
for any incoming connections
To run the windows side you can convert the client.py to an executable<br>file or simply run it through an IDE of your choice for testing purpose
##### Available options
when your run```python3 server.py```the server waits for 
a connection from a victim
Once a connection is established we get a shell which we can <br> run
commands as if we are physically on the victims machine
**To run other commands such as download files from victim
and to take a screenshot from the victims screen
we only need to specify on the shell ie:
```
 $download file.pdf This downloads the file.pdf to your attackers machine with same name
 $screen This will take a screenshot of the victims screen
and save it on the attackers machine with current time as the file name
```
##### This script is for education purpose only am not liable for any damages

##### contribution
Any contributions or changes are highly welcomed<br>Folk the repo and perform the changes you deem necessary then do a pull requests 
and your changes will be incorporated.<br>Any issues raised will also be looked into
##### AUTHOR
peter-macharia
