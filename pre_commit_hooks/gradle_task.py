from __future__ import print_function

import argparse
from typing import Optional
from typing import Sequence

from pre_commit_hooks.util import cmd_output, run_gradle_wrapper_task, run_gradle_task


def main(argv=None):  # type: (Optional[Sequence[str]]) -> int
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '-w', '--wrapper', action='store_true',
        help='Runs commands using gradlew. Requires gradle wrapper configuration within the project.'
    )
    group.add_argument(
        '-p', '--wrapper-path', action='store',
        help='Specifies the path where the gradle wrapper script and the build.gradle is.'
    )
    parser.add_argument(
        '-o', '--output', action='store_true',
        help='Prints the output of all executed gradle commands.'
    )
    parser.add_argument('tasks', nargs='*', help='gradle tasks to run')
    args = parser.parse_args(argv)

    if args.wrapper or args.wrapper_path is not None:
        wrapper = args.wrapper_path if args.wrapper_path is not None else '.'
        return run_gradle_wrapper_task(wrapper,args.output, *args.tasks)
    else:
        return run_gradle_task(args.output, *args.tasks)


if __name__ == '__main__':
    exit(main())
