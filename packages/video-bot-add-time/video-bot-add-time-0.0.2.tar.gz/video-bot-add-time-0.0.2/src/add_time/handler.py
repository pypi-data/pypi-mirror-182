from logger import Logger
from add_time.utils.lambda_helpers  import * 
from add_time.models.request import Request
from add_time.factories.factory import Factory

def handler(event, context):

    request = Request(event)
    logger = Logger()
    factory = Factory(request, logger)
    controller = factory.make_controller()
    result = controller.handle()

    json_str = get_json(result)
    
    print(json_str)
    
    return json_str