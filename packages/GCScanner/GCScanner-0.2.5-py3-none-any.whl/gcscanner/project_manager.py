from google.cloud import resourcemanager_v3
from typing import List


def display_projects(projects: List):
    # Iterate
    for project in projects:
        print(project.project_id)


def get_list_projects() -> List:
    """Lists all projects from an account."""
    resource_manager_client = resourcemanager_v3.ProjectsClient()
    projects = resource_manager_client.search_projects()
    return projects


def get_project(project_id: str) -> List:
    """Get a project."""
    resource_manager_client = resourcemanager_v3.ProjectsClient()

    project = resource_manager_client.get_project(name=f"projects/{project_id}")
    return project
