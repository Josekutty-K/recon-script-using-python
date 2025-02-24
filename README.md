# recon-script-using-python
I have been learning python for the last couple of days and I created a python script that can automate some basic steps in the recon phase in web app penetration testing...

\nWHAT WILL THIS SCRIPT DO ???
The script will get the subdomain which is the target then it will do a nmap port scan with -A flag after the nmap scan the script will ask if web need to brute force directories using http or https protocol after the user mentions the protocol the script will do a directory brute-forcing using dirb, after that the script will crawl urls using katana and save the result in the current location, after that the script will run httpx-toolkit and find the status codes of the URLs gathered using katana and save the result in the current location.....


PLEASE MAKE SURE YOU HAVE THESE TOOLS AVAILABLE AND THEY SHOULD BE ACCESSIBLE FROM THE LOCATION IN WHICH YOU ARE RUNNING THE PYTHON SCRIPT
Nmap, Dirb, Katana, httpx-toolkit

If you don't have these tools I will give steps to install these on kali:

1️⃣ Install Nmap
Nmap is pre-installed in Kali Linux, but if it's missing or needs updating, run:
sudo apt update && sudo apt install nmap -y

✅ Verify Installation:
nmap --version

2️⃣ Install Dirb
Dirb is used for directory brute-forcing.
sudo apt install dirb -y

✅ Verify Installation:
dirb

3️⃣ Install Katana (Web Crawler)
Katana is not in Kali’s default repositories, so we clone and install it manually:
CGO_ENABLED=1 go install github.com/projectdiscovery/katana/cmd/katana@latest

✅ Verify Installation:
katana -h

4️⃣ Install HTTPX-Toolkit
sudo apt install httpx-toolkit

✅ Verify Installation:
httpx-toolkit -h

INSTALLATION OF THE TOOL:

1, Git clone https://github.com/Josekutty-K/recon-script-using-python.git

2, cd recon-script-using-python

3, chmod +x recon-script.py

4, python recon-script.py

THAT'S IT, ENTER YOUR SUBDOMAIN TO ENUMERATE AND THE TOOL WILL TAKE CARE THE REST OF THE HEADACHE...

