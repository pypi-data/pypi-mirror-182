from gcscanner import project_manager, bucket_manager


def get_projects_scope(project: str):
    if project:
        project = project_manager.get_project(project)
        return [project]

    return project_manager.get_list_projects()


def get_buckets_scope(project_id: str, bucket: str = None):
    if bucket:
        bucket = bucket_manager.get_bucket(project_id, bucket)
        return [bucket]

    return bucket_manager.list_buckets(
        project_id,
    )
