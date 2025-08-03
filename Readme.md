# Go Pentest Yourself!

This repository covers instructions for completing basic penetration testing on your own environment.
While this is not a recommended replacement for quality, third-party pentesting, it's a great first step.
Also, if you knock this out before your pentesters arrive, that'll force them to work harder and find deeper vulnerabilities!

## How To Use This Repo

Start with the steps in the `setup/` folder.
This will help you get tools set up and, more importantly, start thinking about what is in scope.

After that, a sensible order to go in might be:
1. attackSurface
2. cloud
3. activeDirectory

## Repo Layout

* Readme.md: This file describes the flow of the workshop
* activeDirectory/: Tools for testing Active Directory
* attackSurface/: Tools for scanning and otherwise discovering attack surface
* cloud/: Tools for measuring cloud risk
* firewall-app/: A vibe-coded fake firewall app used in part of the demo
* setup/: Common setup steps for testing
