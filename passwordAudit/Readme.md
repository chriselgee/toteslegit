## Password Auditing

In a Windows environment, organizations should consider occasional password audits.
In this type of engagement, we retrieve hashes from the environment and check how many might be cracked easily.

### Impacket

[Impacket](https://github.com/fortra/impacket) is a suite of AD-focused tools.
Some highlights are:
* secretsdump.py: Pull passwords and hashes from a target machine.  Also great for turning ntds.dit and the SYSTEM hive into hashes for a password audit!
* Get-GPPPassword.py: Look for old Group Policy Preference files - and local admin credentials stored within

#### Install

As a Python package, Impacket installs with `pipx`:

```bash
sudo apt install pipx
python3 -m pipx install impacket
pipx ensurepath
```

#### Use

As a quick check, use Get-GPPPassword to see if you have any local admin creds hanging out in a group policy preference file:

```bash
Get-GPPPassword.py 'toteslegit.local'/'USER':'PASSWORD'@'DOMAIN_CONTROLLER'
```

Or, for a password audit, first get all the hashes from the domain controller:

```cmd.exe
vssadmin create shadow /for=c:
copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\windows\ntds\ntds.dit c:\ntds.dit
reg save hklm\system c:\system /y
```

Move them to your testing machine - and be sure to delete the copies in the root of `c:\`!

```bash
secretsdump.py -ntds ./ntds.dit -system ./system -outputfile /tmp/hashes.txt LOCAL
```

### Responder

Responder listens for misconfigured name resolution broadcasts.
Run Responder on a well-populated network segment and just wait for hashes!

#### Install

```bash
docker pull chriselgee/responder
```

#### Usage

```bash
docker run --rm -it --net=host --privileged chriselgee/responder:latest -I ens33
```

### Hashcat

#### Install

```bash
wget https://hashcat.net/files/hashcat-7.0.0.7z
7z x hashcat-7.0.0.7z
sudo ln -s $PWD/hashcat-7.0.0/hashcat.bin /usr/bin/hashcat
```

#### Usage

-m5600
-NT
