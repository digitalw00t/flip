Project Description
-------------------

`flip` is a Python-based command-line tool designed to invert the last two arguments of a specified command before executing it. This utility is particularly useful for commands like `grep`, where you may want to search different strings in the same file multiple times.

### Features

*   Inverts the last two arguments of a given command.
*   Supports debug mode, activated with `-d` or `--debug`, to print the executed command.

Installation
------------

1.  Clone the repository:
    
    bashCopy code
    
    `git clone https://github.com/digitalw00t/flip.git`
    
2.  Navigate to the project directory:
    
    bashCopy code
    
    `cd flip`
    
3.  Make the script executable:
    
    bashCopy code
    
    `chmod +x flip.py`
    

Usage
-----

General usage:

bashCopy code

`./flip.py [OPTIONS] COMMAND -- [ARGUMENTS]`

### Options

*   `-d`, `--debug`: Enable debug mode to print the command that will be executed.

### Arguments

*   `COMMAND`: The command you want to run.
*   `ARGUMENTS`: The arguments for the command.

**Note**: Use `--` before specifying the arguments to ensure that any special characters like wildcards are handled correctly.

Examples
--------

1.  Basic Usage:
    
    bashCopy code
    
    `./flip.py grep -- -ir file string`
    
    This will run: `grep -ir string file`
    
2.  With Debug Mode:
    
    bashCopy code
    
    `./flip.py -d grep -- -ir file string`
    
    Output:
    
    bashCopy code
    
    `Executing command: grep -ir string file`
    
    And then it will run the actual command.
    

Contributing
------------

Feel free to open issues or submit pull requests to improve the tool.

License
-------

This project is open-sourced under the MIT License.

* * *

### See also

*   📘 [Markdown Guide](https://www.google.com/search?q=Markdown+guide) to get more familiar with Markdown syntax.
*   🛠️ [Creating a README.md](https://www.google.com/search?q=how+to+create+a+README.md) for more tips on writing README files.

### You may also enjoy

*   📝 [Technical Writing](https://www.google.com/search?q=technical+writing+tutorials) to improve your documentation skills.
*   🐍 [Python CLI Projects](https://www.google.com/search?q=Python+CLI+projects) for more examples of Python command-line tools.
