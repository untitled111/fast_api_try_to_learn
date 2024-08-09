from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import List


class Project(BaseModel):
    id: int
    name: str
    description: str


class Task(BaseModel):
    id: int
    title: str
    description: str
    project_id: int


app = FastAPI()
projects = []
tasks = []


@app.get('/projects/', response_model=List[Project])
def get_list_projects():
    return projects


@app.get('/projects/{project_id}')
def get_project_by_id(project_id: int):
    return [project for project in projects if project.id == project_id]


@app.post('/projects/add_project')
def add_project(project: Project):
    projects.append(project)
    return {
        'projects': projects,
    }


@app.post('/add_task/')
def add_task(task: Task):
    tasks.append(task)
    return {
        'tasks': tasks,
    }


@app.get('/tasks_by_project/')
def get_tasks(project_id: int):
    return [task for task in tasks if task.project_id == project_id]


if __name__ == '__main__':
    uvicorn.run("main:app")
