# Project: 0x02. Shell, I/O Redirections and filters

## Resources
**Read or watch:**

- [Shell, I/O Redirection](http://linuxcommand.org/lc3_lts0070.php)  
- [Special Characters](http://mywiki.wooledge.org/BashGuide/SpecialCharacters)

**man or help:**

- `echo`
- `cat`
- `head`
- `tail`
- `find`
- `wc`
- `sort`
- `uniq`
- `grep`
- `tr`
- `rev`
- `cut`
- `passwd (5)` (_i.e._ _`man 5 passwd`_)
# Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/?fbclid=IwAR2K5_BGPVo0QjJXkOIIqNsqcXK4lTskPWJvA0asKQIGtCPWaQBdKmj1Ztg), **without the help of Google:**
## Shell, I/O Redirection
- What do the commands `head`, `tail`, `find`, `wc`, `sort`, `uniq`, `grep`, `tr` do
- How to redirect standard output to a file
- How to get standard input from a file instead of the keyboard
- How to send the output from one program to the input of another program
- How to combine commands and filters with redirections
# Special Characters
- What are special characters
- Understand what do the white spaces, single quotes, double quotes, backslash, comment, pipe, command separator, tilde and how and when to use them
# Other Man Pages
- How to display a line of text
- How to concatenate files and print on the standard output
- How to reverse a string
- How to remove sections from each line of files
- What is the `/etc/passwd` file and what is its format
- What is the `/etc/shadow` file and what is its format
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
- You are not allowed to use `sed` or `awk`

# More Info
Read your `/etc/passwd` and `/etc/shadow` files.

Note: You do not have to learn about `fmt`, `pr`, `du`, `gzip`, `tar`, `lpr`, `sed` and `awk` yet.

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
    
