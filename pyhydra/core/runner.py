import subprocess
from .command import HydraCommandBuilder
from .parsing import check_output

def bruteforce(command_builder: HydraCommandBuilder, found_callback, exit_callback=None, error_callback=None) -> None:
    print(" ".join(command_builder.build()))
    process = subprocess.Popen(command_builder.build(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while True:
        try:
            output = process.stdout.readline()
            if process.poll() is not None:
                break
            if output:
                # parse
                check_output(output.decode("utf-8"))
        except KeyboardInterrupt:
            if exit_callback:
                exit_callback()
            process.kill()
            print("Keyboard interrupt")
            break
    rc = process.poll()
    if rc != 0:
        if error_callback:
            error_callback()
        raise Exception("Error has occured")
    return rc