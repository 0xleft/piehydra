# A python wrapper for hydra (bruteforce tool)

## Description

Scripts = easy profit. Scripts + hydra = more profit.

Repository also includes a simple server to test the script on.

## Usage

```python
from piehydra import HydraCommandBuilder, bruteforce, parse, LineType

command_builder = HydraCommandBuilder()
command_builder.set_target("localhost")
command_builder.set_method("ssh")
command_builder.set_passwords("wordlist.txt")
command_builder.set_usernames("test", list=False)
command_builder.exit_on_found()

def line_handler(line: str):
    parsed_line = parse(line)
    if parsed_line.type == LineType.FOUND:
        print("Found: " + parsed_line.username + ":" + parsed_line.password)
    elif parsed_line.type == LineType.ATTEMPT:
        print("Attempt: " + parsed_line.username + ":" + parsed_line.password)

# main method
bruteforce(command_builder, line_handler)
```

Output:
```bash
...
Attempt: test:s1aut11111
Attempt: test:111111!@
Found: test:test
```

## Install

Note you must have hydra installed for this to work.

`sudo apt install hydra`

Note that hydra itself is licensed under AGPL which can be found [here](https://github.com/vanhauser-thc/thc-hydra/blob/master/LICENSE)

```bash
pip install piehydra
```