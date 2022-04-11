# Project: 0x03. Shell, init files, variables and expansions

## Resources
**Read or watch:**

- [Expansions](http://linuxcommand.org/lc3_lts0080.php)  
- [Shell Arithmetic](https://www.gnu.org/software/bash/manual/html_node/Shell-Arithmetic.html)
- [Variables](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_02.html)  
- [Shell initialization files](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_01.html)
- [The alias Commands](http://www.linfo.org/alias.html)  
- [Technical Writing](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2021/6/9112669886fd446a2aa3113c31319d1f468dc160.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220411%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220411T203924Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a39d23430a0ee2f7dc371f2e02d77b3a04c132d3706f54f17be336de9bd82e10) 

**man or help:**

- `printenv`
- `set`
- `unset`
- `export`
- `alias`
- `unalias`
- `.`
- `source`
- `printf`
# Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/?fbclid=IwAR2K5_BGPVo0QjJXkOIIqNsqcXK4lTskPWJvA0asKQIGtCPWaQBdKmj1Ztg), **without the help of Google:**
## General
- What happens when you type `$ ls -l *.txt`
## Shell Initialization Files
- What are the `/etc/profile` file and the /etc/profile.d directory
- What is the `~/.bashrc` file
# Variables
- What is the difference between a local and a global variable
- What is a reserved variable
- How to create, update and delete shell variables
- What are the roles of the following reserved variables: HOME, PATH, PS1
- What are special parameters
- What is the special parameter `$?`?
# Expansions
- What is expansion and how to use them
- What is the difference between single and double quotes and how to use them properly
- How to do command substitution with `$()` and backticks
# Shell Arithmetic
- How to perform arithmetic operations with the shell
# The `alias` Command
- How to create an alias
- How to list aliases
- How to temporarily disable an alias
# Other `help` pages
How to execute commands from a file in the current shell

# Requirements
## General
- Allowed editors: `vi`, `vim`, `emacs`  
- All your scripts will be tested on Ubuntu 20.04 LTS    
- All your scripts should be exactly two lines long (`$ wc -l file` should print 2)   
- All your files should end with a new line (`why?`)    
- The first line of all your files should be exactly `#!/bin/bash`    
- A `README.md` file, at the root of the folder of project, describing what each script is doing  
- You are not allowed to use backticks, `&&`, `||` or `;`  
- You are not allowed to use `bc`, `sed` or `awk`
- All your files must be executable

# More Info
Read your `/etc/profile`, `/etc/inputrc` and `~/.bashrc` files.

Look at some files in the `/etc/profile.d` directory.

Note: You do not have to learn about `awk`, `tar`, `bzip2`, `date`, `scp`, `ulimit`, `mask`, or shell scripting, yet.

# Quiz questions
 
  
  ### Question #0
  Which symbol should I use to redirect the standard output to a file (overwrite the file)?
  - [ ] >>
  - [ ] 2> 
  - [x] >  
  - [ ] &
  
  ### Question #1  
  Which symbol should I use to redirect the standard output to a file (appending to the file)?
  - [x] >>
  - [ ] 2> 
  - [ ] >  
  - [ ] &
  
  ### Question #2
  Which symbol should I use to redirect the error output to the standard output?
  - [x] 2>&1
  - [ ] 2> 
  - [ ] 1>&2  
  
  ### Question #3
  Which symbol should I use to start a comment?
  - [ ] &
  - [ ] !
  - [ ] //
  - [X] #
    
  ### Question #4
  Which command should I use to display the entire file content?
  - [ ] grep
  - [x] cat
  - [ ] head
  - [ ] tail
    
  ### Question #5
  Which command should I use to display the last 11 lines of a file?
  - [ ] head -n 11 my_file
  - [ ] head 11 my_file
  - [x] tail -n 11 my_file
  - [ ] tail 11 my_file

  ### Question #6
 Which symbol should I use to escape a special character?
 - [x] \
 - [ ] !
 - [ ] $
 - [ ] #   
    
