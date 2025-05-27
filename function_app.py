import azure.functions as func
import logging
from azure.functions.decorators.core import DataType
import uuid

# Initialize the FunctionApp
app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# Function 1: Queue Output Binding (Part 1)
@app.route(route="HttpExample")
@app.queue_output(arg_name="msg", queue_name="outqueue", connection="AzureWebJobsStorage")
def HttpExample(req: func.HttpRequest, msg: func.Out[func.QueueMessage]) -> func.HttpResponse:
    logging.info('Processing HTTP request for queue output.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
            name = req_body.get('name')
        except ValueError:
            pass

    if name:
        msg.set(name)
        return func.HttpResponse(f"Hello, {name}. Message added to queue.")
    else:
        return func.HttpResponse(
            "Please pass a name in query or request body.",
            status_code=400
        )

# Function 2: SQL Output Binding (Part 2)
@app.function_name(name="HttpTrigger1")
@app.route(route="hello", auth_level=func.AuthLevel.ANONYMOUS)
@app.generic_output_binding(
    arg_name="toDoItems",
    type="sql",
    CommandText="dbo.ToDo",
    ConnectionStringSetting="SqlConnectionString",
    data_type=DataType.STRING
)
def test_function(req: func.HttpRequest, toDoItems: func.Out[func.SqlRow]) -> func.HttpResponse:
    logging.info('Processing HTTP request for SQL output.')

    try:
        name = req.get_json().get('name')
    except ValueError:
        name = None

    if name:
        toDoItems.set(func.SqlRow({
            "Id": str(uuid.uuid4()),
            "title": name,
            "completed": False,
            "url": ""
        }))
        return func.HttpResponse(f"Hello {name}! Added to SQL table.")
    else:
        return func.HttpResponse("Please pass a name in the request body", status_code=400)
