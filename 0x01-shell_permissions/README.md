# Project: 0x01. Shell, permissions

## Resources
**Read or watch:**

- [Permissions](http://linuxcommand.org/lc3_lts0090.php)  

**man or help:**

- `chmod`
- `sudo`
- `su`
- `chown`
- `chgrp`
- `id`
- `groups`
- `whoami`
- `adduser`
- `useradd`
- `addgroup`
# Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/?fbclid=IwAR2K5_BGPVo0QjJXkOIIqNsqcXK4lTskPWJvA0asKQIGtCPWaQBdKmj1Ztg), **without the help of Google:**
## Permissions
- What do the commands `chmod`, `sudo`, `su`, `chown`, `chgrp` do
- Linux file permissions
- How to represent each of the three sets of permissions (owner, group, and other) as a single digit
- How to change permissions, owner and group of a file
- Why can’t a normal user `chown` a file
- How to run a command with root privileges
# Other Man Pages
- How to create a user
- How to create a group
- How to print real and effective user and group IDs
- How to print the groups a user is in
- How to print the effective userid
# Requirements
## General
- Allowed editors: `vi`, `vim`, `emacs`  
- All your scripts will be tested on Ubuntu 20.04 LTS    
- All your scripts should be exactly two lines long (`$ wc -l file` should print 2)   
- All your files should end with a new line (`why?`)    
- The first line of all your files should be exactly `#!/bin/bash`    
- A `README.md` file, at the root of the folder of project, describing what each script is doing  
- You are not allowed to use backticks, `&&`, `||` or `;`  
- All your scripts must be executable
# Quiz questions
 
  
  ### Question #0  
  Which command should I use for changing a file permission?
  - [ ] su
  - [x] chmod 
  - [ ] chown  
  - [ ] chgrp 
  
  ### Question #1
  Which command should I use for changing a file owner?
  - [ ] su
  - [ ] chmod 
  - [x] chown  
  - [ ] chgrp
  
  ### Question #2
  What is the permission value for a file without any restriction?
  - [ ] 600
  - [ ] 644
  - [x] 777
  
  ### Question #3
  What is the permission value for a file read only for the group owner?
  - [x] 040
  - [ ] 050
  - [ ] 060
  - [ ] 070
    
  ### Question #4
  What is the numerical value for the rwx------ permission?
  - [ ] 600
  - [ ] 621
  - [ ] 704
  - [x] 700
    
  ### Question #5
  What is the numerical value for the r-xr--r-- permission?
  - [ ] 522
  - [x] 544
  - [ ] 644
  - [ ] 411
    
  ### Question #6
  What is the numerical value for the ----w---x permission?
  - [ ] 123
  - [ ] 121
  - [ ] 221
  - [x] 021   
    
