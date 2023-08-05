from gcscanner import output


def list_buckets_publicly_readable(_buckets_publicly_readable) -> None:
    if _buckets_publicly_readable == []:
        print()
        output.pretty_print(text="0 bucket publicly readable", color="green")
        return
    print()
    output.pretty_print(text="Bucket(s) publicly readable :", color="red")
    for bucket in _buckets_publicly_readable:
        output.display_bucket(bucket, "\t")


def list_buckets_authenticated_readable(_buckets_authenticated_readable) -> None:
    if _buckets_authenticated_readable == []:
        print()
        output.pretty_print(text="0 bucket readable for anyone signed", color="green")
        return
    print()
    output.pretty_print(text="Bucket(s) readable for anyone signed:", color="magenta")
    for bucket in _buckets_authenticated_readable:
        output.display_bucket(bucket, "\t")
