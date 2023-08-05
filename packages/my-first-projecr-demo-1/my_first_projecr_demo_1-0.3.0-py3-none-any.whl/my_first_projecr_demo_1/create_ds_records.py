import time
from google.cloud import datastore


datastore_client = datastore.Client()
def create_record_in_datastore():
    kind = "Task"
    id = "6789012"
    task_key = datastore_client.key(kind, id)
    task = datastore.Entity(key=task_key)
    task["description"] = "Test 1 record"
    datastore_client.put(task)

    print(f"Saved {task.key.name}: {task['description']}")


def update_records():
    kind = "Task"
    # id="sampletask1"
    id = 5644004762845184
    with datastore_client.transaction():
        task_key = datastore_client.key(kind, id)
        record_id = datastore_client.get(task_key)
        record_id.update({'description':"Add new description via python code to test."})
        datastore_client.put(record_id)
    

def delete_records():
    kind = "Task"
    id = "54321"
    task_key = datastore_client.key(kind, id)
    datastore_client.delete(task_key)


def create_multi_records():
    kind = "Employee_table"

    task_key1 = datastore_client.key(kind, 1)
    task1 = datastore.Entity(task_key1)
    task1.update({
        'emp_name': "Shyam",
        'age': 30,
        'gender': "Male",
        'designation': "PM",
        'address': "Pune"
    })


    task_key2 = datastore_client.key(kind, 3)
    task2 = datastore.Entity(task_key2)

    task2.update({
        'emp_name': "Advait",
        'age': 30,
        'gender': "Male",
        'designation': "CEO",
        'address': "USA"
    })


    datastore_client.put_multi([task1, task2])


def delete_multi_records():
    kind = "Employee_table"
    task_key1 = datastore_client.key(kind, 1)
    task_key2 = datastore_client.key(kind, 3)

    datastore_client.delete_multi([task_key1, task_key2])
