## Active Directory

### Bloodhound

[Bloodhound](https://github.com/SpecterOps/BloodHound.git) helps us analyze 

```bash
wget https://github.com/SpecterOps/bloodhound-cli/releases/latest/download/bloodhound-cli-linux-amd64.tar.gz
tar -xvzf bloodhound-cli-linux-amd64.tar.gz
./bloodhound-cli install
# Note the URL and credentials!
./bloodhound-cli up
# Browse to localhost:8080
```

### Impacket

```bash
sudo apt install pipx
python3 -m pipx install impacket
pipx ensurepath
```

### Certipy

```bash
git clone https://github.com/ly4k/Certipy.git
cd Certipy
python3 -m venv certipy-venv
source certipy-venv/bin/activate
pip install certipy-ad
```

https://github.com/ly4k/Certipy.git

### Share Finders
