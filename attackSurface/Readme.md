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
sudo nmap -iL ips-dedup.txt -sV -oA quickscan
sudo nmap -iL ips-dedup.txt -p0- -sV -oA thoroughscan
sudo nmap -iL ips-dedup.txt -sU --top-ports=20 -oA udpscan
```

### GoWitness

```bash
# Use your nmap output like this:
docker run --rm -v $(pwd):/data leonjza/gowitness gowitness scan nmap -f thoroughscan.xml --open-only --service-contains http --write-db
# Or if you have a good idea of what the web hosts are
docker run --rm -v $(pwd):/data leonjza/gowitness gowitness scan file -f webhosts.txt --write-db
docker run --rm -v $(pwd):/data -p127.0.0.1:7171:7171 leonjza/gowitness gowitness report server --host 0.0.0.0
```
