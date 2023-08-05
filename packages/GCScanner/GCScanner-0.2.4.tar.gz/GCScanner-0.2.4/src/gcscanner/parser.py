import argparse
from typing import List
from gcscanner.logger import LOGGER
from gcscanner import output, main, scope, utils
from print2 import PPrint, pprint


def display_project(project, options):
    _bucket_access = []
    pp = PPrint(indent="\t", level=0)
    # if project state is on DELETE_REQUESTED state (2)
    if project.state == 2:
        pprint(f"{project.display_name}", indent="", level=0, color="red")
        pprint(f"id = {project.project_id}", indent="\t", level=1, color="red")
        return []

    pp.print(f"{project.display_name}", "green")
    # pp.inc_level()
    pp.print(f"id = {project.project_id}")
    buckets = scope.get_buckets_scope(project.project_id, options.bucket)
    buckets = list(buckets)
    if not buckets:
        return
    pp.print(f"buckets =")
    for bucket in buckets:
        output.display_bucket(bucket, "\t", 1, options.details)
        utils.size_by_class(
            bucket,
            "\t",
            2,
            bucket.iam_configuration.uniform_bucket_level_access_enabled,
            display_size=options.size,
            display_file_access=options.files_access,
        )
        policy = bucket.get_iam_policy(requested_policy_version=3)
        _bucket_access = output.display_policy(
            policy,
            "\t",
            2,
            options.policy,
        )

        pp.set_level(2)
        if options.policy:
            pp.inc_level()

        if (
            "bucket_public_access" in _bucket_access
            and _bucket_access["bucket_public_access"]
        ):

            pp.print(f"Bucket publicly readable", "red")
            main._buckets_publicly_readable.append(bucket)

        elif (
            "bucket_authenticated_readable" in _bucket_access
            and _bucket_access["bucket_authenticated_readable"]
        ):
            pp.print(f"Bucket readable for anyone signed", "magenta")
            main._buckets_authenticated_readable.append(bucket)

        else:
            pp.print(
                f"Bucket not publicly and authenticated readable",
                "green",
                output=not options.only_public,
            )


def args(argv: List[str] = None) -> bool:

    if argv is None:
        import sys

        argv = sys.argv[1:]

    parser = argparse.ArgumentParser(description="What the program does")

    parser.add_argument(
        "-log", "--log", default="warning", help="Provide logging level. "
    )

    parser.add_argument(
        "-a",
        "--bucket-authenticated",
        action="store_true",
        help="Check access bucket authenticated",
    )

    parser.add_argument(
        "-o",
        "--only-public",
        action="store_true",
        help="Show only publicly readable or authenticated bucket",
    )

    parser.add_argument(
        "-f",
        "--files-access",
        action="store_true",
        help="Check access for files publicly or authenticated readable",
    )

    parser.add_argument(
        "-s",
        "--size",
        action="store_true",
        help="Show total size of bucket",
    )

    parser.add_argument(
        "-r",
        "--resume",
        action="store_true",
        help="Resume publicly readable or authenticated bucket",
    )

    parser.add_argument(
        "-p",
        "--project",
        default="",
        help="Only search in this project",
    )

    parser.add_argument(
        "-b",
        "--bucket",
        default="",
        help="Only search in this bucket",
    )

    parser.add_argument(
        "-d",
        "--details",
        action="store_true",
        help="Get details about buckets",
    )

    parser.add_argument(
        "-po",
        "--policy",
        action="store_true",
        help="Display policy",
    )

    options = parser.parse_args(argv)

    levels = {
        "critical": 50,
        "error": 40,
        "warn": 30,
        "warning": 30,
        "info": 20,
        "debug": 10,
    }
    level = levels.get(options.log.lower())

    if not level:
        raise ValueError(
            f"log level given: {options.log}"
            f" -- must be one of: {' | '.join(levels.keys())}"
        )

    LOGGER.setLevel(level)

    main.scan_projects(options)
