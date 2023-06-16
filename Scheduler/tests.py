from celery.result import AsyncResult
from Scheduler.tasks import check_interview

# submit the task and get the task ID
task = check_interview.delay(request)
task_id = task.id

# poll the result backend for the task result
result = None
while result is None:
    result = AsyncResult(task_id).get()

# process the task result
if result.success:
    data = result.result["data"]
    logger.info(data)
    print(data)
else:
    error = result.result["error"]
    logger.error(error)
    print(error)