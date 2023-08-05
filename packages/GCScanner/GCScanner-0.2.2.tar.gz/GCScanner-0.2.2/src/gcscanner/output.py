from print2 import PPrint

"""
def pretty_print(
    text: str, indent: str = "\t", prefix: str = "", level: int = 0, color: str = ""
):
    if is_multiline(text):
        for line in text.splitlines():
            pretty_print(
                text=line, prefix=prefix, indent=indent, level=level, color=color
            )
        return
    if not color:
        print(f"{indent*level}{prefix}{text}")
        return
    print(colored(f"{indent*level}{prefix}{text}", color))
    return


def is_multiline(text):
    if "\n" in text:
        return True
    return False


class PrettyPrint:

    prefix = ""
    indent = "\t"
    level = 0

    def __init__(
        self, prefix: str = "", indent: str = "\t", level: int = 0, output: int = True
    ):
        self.prefix = prefix
        self.indent = indent
        self.level = level
        self.output = output
        self.level_tmp = 0

    def set_prefix(self, prefix: str) -> None:
        self.prefix = prefix

    def get_prefix(self) -> str:
        return self.prefix

    def set_indent(self, indent: str) -> None:
        self.indent = indent

    def get_indent(self) -> str:
        return self.indent

    def set_output(self, output: bool = True) -> None:
        self.output = output

    def get_output(self) -> bool:
        return self.output

    def set_level(self, level: int) -> None:
        self.level = level

    def set_tmp_level(self, level: int) -> None:
        self.level_tmp = level

    def inc_level(self) -> None:
        self.level = self.level + 1

    def get_level(self) -> int:
        return self.level

    def print(self, text, color: str = "", output: bool = None):
        if (self.output and output is not False) or output:
            if self.level_tmp:
                pretty_print(
                    text=text,
                    prefix=self.prefix,
                    indent=self.indent,
                    level=self.level_tmp,
                    color=color,
                )
                self.level_tmp = 0
                return
            pretty_print(
                text=text,
                prefix=self.prefix,
                indent=self.indent,
                level=self.level,
                color=color,
            )
        return
"""


def display_bucket(bucket, indent, level: str = 1, output: bool = True):
    pp = PPrint(indent=indent, level=level, output=output)
    pp.print(f"{bucket.name}", output=1)
    pp.inc_level()
    time_created = str(bucket.time_created)
    pp.print(f"Created = {time_created[:10]}")
    pp.print(
        f"Uniform Bucket Level Access = {bucket.iam_configuration.uniform_bucket_level_access_enabled}"
    )
    if bucket.owner is not None:
        pp.print(f"Owner = {bucket.owner}", prefix=indent, level=level)
    pp.print(f"Location = {bucket.location} ({bucket.location_type})")
    pp.print(f"Versioning = {bucket.versioning_enabled}")
    pp.print(f"Storage class = {bucket.storage_class}")


def display_policy(policy, indent, level=0, output: bool = True) -> dict:
    _bucket_public_access = False
    _bucket_authenticated_readable = False
    pp = PPrint(indent=indent, level=level, output=output)
    pp.print("policy =")
    pp.inc_level()
    pp.print(f"version = {policy.version}")
    for binding in policy.bindings:
        pp.print(f"role = {binding['role']}")
        pp.print("member(s)=")
        for member in binding["members"]:
            pp.set_tmp_level(pp.get_level() + 1)
            pp.print(f"{member}")
            if member == "allUsers":
                _bucket_public_access = True
            if member == "allAuthenticatedUsers":
                _bucket_authenticated_readable = True
    return {
        "bucket_public_access": _bucket_public_access,
        "bucket_authenticated_readable": _bucket_authenticated_readable,
    }
