# BlackCoffer-AWS
To Access the model:
http://44.208.20.218:8080/

# Steps to follow

Create AWS account (free, but takes 24Hrs for account verification)
https://aws.amazon.com/

create EC2 instance (I used UBUNTU OS image), private key will get downloaded

download Putty & Puttygen (Download Putty will include Puttygen too)
https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html
 

download wincp
https://winscp.net/eng/download.php

Open Puttygen -> load private key (use downloaed key)

wincp -> copy all files(only those which has our code) to Ubuntu server

Putty --> connect through Putty & install all libraries, use these commands

sudo apt-get update && sudo apt-get install python3-pip 
pip3 install -r requirements.txt 
python3 main-app.py

edit host and port in flask app:
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)
