# Go Pentest Yourself!

This repository covers instructions for completing basic penetration testing on your own environment.
While this is not a recommended replacement for quality, third-party pentesting, it's a great first step.
Also, if you knock this out before your pentesters arrive, that'll force them to work harder and find deeper vulnerabilities!

## Repo Layout

* Readme.md: This file describes the flow of the workshop
* firewall-app/: A vibe-coded fake firewall app used in part of the demo

## Setup

Ideally, these steps are done from an external cloud instance and an internal testing machine.
I like to use the latest Debian distributions for these, but anything that can install the tools needed is _probably_ fine!

### Scope

We need to begin with some kind of scope.
This may be in the form of IP ranges, IP addresses, or network names.
I recommend putting them in files like:

`ips.txt`
```
10.2.3.4
172.16.32.32
192.168.121.0/24
```

`hostnames.txt`
```
example.toteslegit.us
mail.toteslegit.us
www.toteslegit.us
```

### Install Packages

Install a few essentials:

```bash
sudo apt update
sudo apt install nmap curl ca-certificates jq
```

### Add Docker

To simplify tool installation, we use [Docker](https://docs.docker.com/get-started/docker-overview/) heavily.
This allows us to run tools without going crazy over libraries and dependencies.
[Install Docker](https://docs.docker.com/engine/install/debian/) in your testing machines.

Cheat sheet as of publication:
```bash
# Set up to add Docker's repos
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
# Fetch updates and install Docker
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
# Check that it works!
sudo docker run hello-world
# So that, after next login, you won't need to `sudo docker` anymore
sudo usermod -aG docker $USER
```

## Asset Discovery

In many modern organizations, discovering and tracking system inventory (the first [CIS Critical Critical Security Control](https://www.cisecurity.org/controls)®!) is a full-time job.
Note that tools like [RunZero](https://www.runzero.com/) (free to a point) can help with asset discovery.

### Discovering Hostnames With Certificate Transparency

Along with whatever we've collected from our own records, we can often find additional, forgotten hostnames with certificate transparency logs.

```bash
curl -s 'https://crt.sh/?q=toteslegit.us&output=json' | jq -r '.[].name_value' | grep -v '*' | sort -u >> certs.txt
```

### Converting Host Names to IP Addresses

Now let's take all the hostnames, deduplicate them, turn them into IP addresses, and deduplicate those:

```bash
cat certs.txt hostnames.txt | sort -u > names-dedup.txt
while read f; do dig A $f +short; done < names-dedup.txt >> ips.txt
cat ips.txt | sort -Vu > ips-dedup.txt
```

### Scanning

Scan your external IP space from an external host.
There are plenty of options here.
Uses one or more of these:

```bash
sudo nmap -iL -sV ips-dedup.txt -oA quickscan
sudo nmap -iL -p0- -sV ips-dedup.txt -oA thoroughscan
sudo nmap -iL ips-dedup.txt -sU --top-ports=20 -oA udpscan
```

nmap -f nmap.xml --open --service-contains http

### GoWitness

```bash
# Use your nmap output like this:
docker run --rm -v $(pwd):/data leonjza/gowitness gowitness nmap -f thoroughscan.xml --open --service-contains http --write-db
# Or if you have a good idea of what the web hosts are
docker run --rm -v $(pwd):/data leonjza/gowitness gowitness scan file -f webhosts.txt --write-db
docker run --rm -v $(pwd):/data -p127.0.0.1:7171:7171 leonjza/gowitness gowitness report server --host 0.0.0.0
```

## Active Directory

### Bloodhound

https://github.com/SpecterOps/BloodHound.git

### Impacket

Maybe do a chriselgee/impacket

* GetPPPassword.py
* GetUserSPNs.py
* Certipy.py 

### Certipy

https://github.com/ly4k/Certipy.git

### Share Finders

## Cloud Assets

### Scoutsuite

https://github.com/nccgroup/ScoutSuite.git

### CSP Dashboards

