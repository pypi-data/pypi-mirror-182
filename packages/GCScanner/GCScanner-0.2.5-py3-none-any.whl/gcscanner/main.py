from gcscanner import parser, check, scope

_buckets_publicly_readable = []
_buckets_authenticated_readable = []


def scan_projects(options):
    projects = scope.get_projects_scope(options.project)

    # Iterate on projects
    for project in projects:

        parser.display_project(project, options)

    resume(options.resume)


def resume(resume):
    if resume:
        check.list_buckets_authenticated_readable(_buckets_authenticated_readable)
        check.list_buckets_publicly_readable(_buckets_publicly_readable)


if __name__ == "__main__":
    # Execute when the module is not initialized from an import statement.
    parser.args()
