import os

def recon(subdomain):
    os.system(f"nmap -A -p- -Pn {subdomain} -v")
    protocol = input("is target domain using http or https: ")
    print("NMAP SCAN IS COMPLETED!!!.. NOW GOING TO BRUTE FORCE DIRECTORIES...")
    if protocol == "https":
      os.system(f"dirb https://{subdomain}")
    else:
      os.system(f"dirb http://{subdomain}")
    print("DIRECTORY BRUTE FORCING COMPLETED!!!.. NOW GOING TO CRAWL URLS...")
    if protocol == "https":
        os.system(f"katana -u https://{subdomain} -o {subdomain}-katana-output.txt")
    else:
        os.system(f"katana -u http://{subdomain} -o {subdomain}-katana-output.txt")
    print("URLS HAVE BEEN CRAWLED AND SAVED USING KATANA!!!.. NOW GOING TO ANALYZE THE URLS ARE DEAD OR NOT...")
    os.system(f"cat {subdomain}-katana-output.txt | httpx-toolkit -sc | tee {subdomain}-httpx-toolkit-result.txt ")

recon(input("Enter the subdomain name to scan: "))
