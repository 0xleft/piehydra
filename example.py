from piehydra import HydraCommandBuilder, bruteforce, parse, LineType

# build the command
command_builder = HydraCommandBuilder()
command_builder.set_target("localhost")
# we are bruteforcing ssh logins
command_builder.set_method("ssh")
# path to the wordlist
command_builder.set_passwords("wordlist.txt")
# path to usernames or just one username
command_builder.set_usernames("test", list=False)
# we want to exit when we find the password
command_builder.exit_on_found()

def line_handler(line: str):
    # parse the line
    parsed_line = parse(line)
    if parsed_line.type == LineType.FOUND:
        # we found a valid login
        print("Found: " + parsed_line.username + ":" + parsed_line.password)
    elif parsed_line.type == LineType.ATTEMPT:
        print("Attempt: " + parsed_line.username + ":" + parsed_line.password)

# main method
bruteforce(command_builder, line_handler)