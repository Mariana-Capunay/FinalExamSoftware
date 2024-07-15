from main import Task, create_task, get_tasks, get_task_by_id
import pytest


def test_main():
    response = get_tasks()
    assert response["message"] == "Tasks fetched successfully"
    assert response["data"] == []

@pytest.mark.parametrize(
    "task", #parameter value
    [
            (Task(id=1, name="Task 1", description="This is task 1", completed=False, date="2021-09-01")),
            (Task(id=2, name="Task 2", description="This is task 2", completed=True, date="2021-09-02"))
    ]
)
def test_add_task(task:Task):
    response = create_task(task)
    assert response["message"] == "Task created successfully"
    """ 
    // to be more specific
    assert response["data"]["id"] == 1
    assert response["data"]["name"] == "Task 1"
    assert response["data"]["description"] == "This is task 1"
    assert response["data"]["completed"] == False
    assert response["data"]["date"] == "2021-09-01"
    """



@pytest.mark.parametrize(
    "id", #parameter value
    [
        (1)
    ]
)
def test_get_task_by_id(id:int):
    response = get_task_by_id(id)
    assert response["message"] == "Task fetched successfully"
    """
    assert response["data"]["name"] == "Task 1"
    assert response["data"]["description"] == "This is task 1"
    assert response["data"]["completed"] == False
    assert response["data"]["date"] == "2021-09-01"
    """
   

def test_exists_task():
    assert get_task_by_id(1)["message"] == "Task fetched successfully"