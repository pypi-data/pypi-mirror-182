import math
from gcscanner import output
from print2 import PPrint


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0 B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


def size_by_class(
    bucket,
    indent,
    level,
    bucket_uniform_access: bool = True,
    display_size=False,
    display_file_access=False,
):
    blobs = bucket.list_blobs()
    pp = PPrint(prefix="", indent=indent, level=level)

    size_multi_regional = (
        size_regional
    ) = size_nearline = size_coldline = size_standard = 0
    count_files = 0
    _bucket_access = {}
    for blob in blobs:
        count_files = count_files + 1
        if not bucket_uniform_access and display_file_access:
            pp.print(blob.name)
            policy = blob.get_iam_policy(requested_policy_version=3)
            _bucket_access = output.display_policy(policy, "\t", level + 1)
            if (
                "bucket_public_access" in _bucket_access
                and _bucket_access["bucket_public_access"]
            ):
                pp.print(f"Publicly readable", "red")

            elif (
                "bucket_authenticated_readable" in _bucket_access
                and _bucket_access["bucket_authenticated_readable"]
            ):
                pp.print(f"Readable for anyone signed", "magenta")

            else:
                pp.print(f"Not publicly and authenticated readable", "green")
        if blob.storage_class == "MULTI_REGIONAL":
            size_multi_regional = size_multi_regional + blob.size
        if blob.storage_class == "REGIONAL":
            size_regional = size_regional + blob.size
        if blob.storage_class == "NEARLINE":
            size_nearline = size_nearline + blob.size
        if blob.storage_class == "COLDLINE":
            size_coldline = size_coldline + blob.size
        if blob.storage_class == "STANDARD":
            size_standard = size_standard + blob.size

    if display_size:
        if size_multi_regional:
            pp.print("MULTI_REGIONAL: " + str(convert_size(size_multi_regional)))
        if size_regional:
            pp.print("REGIONAL: " + str(convert_size(size_regional)))
        if size_nearline:
            pp.print("NEARLINE: " + str(convert_size(size_nearline)))
        if size_coldline:
            pp.print("COLDLINE: " + str(convert_size(size_coldline)))
        if size_standard:
            pp.print("STANDARD: " + str(convert_size(size_standard)))

        size_total = (
            size_multi_regional
            + size_regional
            + size_nearline
            + size_coldline
            + size_standard
        )
        pp.print("TOTAL= " + str(convert_size(size_total)))
    pp.print("FILES = " + str(count_files))
