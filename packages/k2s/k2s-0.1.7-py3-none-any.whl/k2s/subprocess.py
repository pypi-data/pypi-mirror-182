import sys
from os import environ
from subprocess import Popen, PIPE

from k2s.exceptions import CLIError
from k2s.spinner import Spinner

DEBUG_MODE = bool(environ.get("K2S_DEBUG", False))


def _run_command(cmd):
    process = Popen(cmd, stdout=PIPE, stderr=PIPE)

    last_length = 0

    with Spinner():
        while True:
            # TODO: this wont work if the output is larger than the terminal
            # size
            output = process.stdout.readline().decode()

            if output == '' and process.poll() is not None:
                break

            if output:
                line = output.strip() + '  '

                if DEBUG_MODE:
                    print(line)
                else:
                    out = ('\r' + ' ' * last_length + '\r' + line)
                    sys.stdout.write(out)
                    sys.stdout.flush()
                    last_length = len(line)

    print('\n', end='')

    return_code = process.poll()

    if return_code:
        raise CLIError(
            'An error happened:\n\n'
            f'{process.stderr.read().decode()}\nFor help, share this error '
            'in the #ask-anything channel in '
            'our community: https://ploomber.io/community')
