from contextlib import contextmanager
import re


class VerbosePrintHandler:
    def __init__(self, start_msg, verbose=False):
        self.verbose = verbose
        if verbose:
            print(start_msg)
        self.exists_previous_message = False

    @contextmanager
    def print_msg(self, msg):
        if self.verbose:
            if self.exists_previous_message:
                print(f"\r├─ ")
            print(f"└─ {msg}...", end="")
        yield msg
        if self.verbose:
            print("DONE", end="")
            self.exists_previous_message = True


def clean_name(name):
    for c in ["\ufeff", "\uFEFF", '"', "$", "\n", "\r", "\t"]:
        name = name.replace(c, "")
    name = re.sub("\W", "_", name)

    if name and re.match("\d", name[0]):
        name = f"letter_{name}"
    return name.lower()
