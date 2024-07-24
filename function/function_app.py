import azure.functions as func
import logging

def test(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    name = "Sanjana"
    query_name = req.params.get('name')
    logging.info(f'Query string name: {query_name}')

    if query_name:
        name = query_name
    else:
        try:
            req_body = req.get_json()
            req_body_name = req_body.get('name')
            logging.info(f'Request body name: {req_body_name}')
           
            if req_body_name:
                name = req_body_name
        except ValueError:
            pass

    return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")

# Create a Function App instance and specify the route
app = func.FunctionApp()
app.route(route="test")(test)
