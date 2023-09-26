class HydraCommandBuilder:
    def __init__(self):
        # I = do not restore, -V verbosity so we can catch output
        self.args = ["-I", "-V"]
        self.target = None
        self.method = None
        self.extra_input = None
        
    def set_target(self, target):
        self.target = target

    def set_method(self, method):
        self.method = method

    def set_extra_input(self, extra_input):
        self.extra_input = extra_input

    def set_usernames(self, usernames, list=True):
        if list:
            self.args.append("-L")
        else:
            self.args.append("-l")
        self.args.append(usernames)
    
    def set_passwords(self, passwords, list=True):
        if list:
            self.args.append("-P")
        else:
            self.args.append("-p")
        self.args.append(passwords)

    def set_port(self, port):
        self.args.append("-s")
        self.args.append(str(port))

    def set_tasks(self, tasks):
        self.args.append("-t")
        self.args.append(str(tasks))

    def exit_on_found(self):
        self.args.append("-f")

    def build(self):
        if self.target is None:
            raise Exception("Target not set")
        if self.method is None:
            raise Exception("Method not set")
        if self.extra_input is None and self.method == "http-form-post":
            raise Exception("Extra input not set")
        
        return ["hydra"] + self.args + [self.target, self.method, self.extra_input or ""]