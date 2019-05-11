import re
import subprocess
import sys

CMD_TESTBED = "/usr/bin/testbed"


def get_instance_name(testbed=0):
    """
    Gets testbed instance by its index
    TODO
    >>>
    """
    result = subprocess.run([CMD_TESTBED], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        if len(result.stderr) != 0:
            sys.stderr.write(result.stderr)
        return None

    return re.split(r'\W+', result.stdout.splitlines()[1:][testbed])[0]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
