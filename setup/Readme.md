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
# So that, after next login, you won't need to `sudo docker` anymore (after you log out/log in)
sudo usermod -aG docker $USER
```

