import subprocess
from .command import HydraCommandBuilder
from .parsing import get_line_type, LineType

def bruteforce(command_builder: HydraCommandBuilder, line_handler, exit_callback=None, error_callback=None) -> None:
    process = subprocess.Popen(command_builder.build(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while True:
        try:
            output = process.stdout.readline()
            if process.poll() is not None:
                break
            if output:
                if get_line_type(output.decode("utf-8")) == LineType.FINISHED:
                    if exit_callback:
                        exit_callback()
                    process.kill()
                    break
                line_handler(output.decode("utf-8"))
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
        raise Exception("Hydra exited with code " + str(rc))
    return rc