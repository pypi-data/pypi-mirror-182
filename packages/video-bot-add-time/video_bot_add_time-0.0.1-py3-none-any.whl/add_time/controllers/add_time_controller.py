from add_time.services.base_service import BaseService

from add_time.models.request import Request
from add_time.controllers.base_controller import BaseController


class AddTimeController(BaseController):

    def __init__(self, request: Request, service: BaseService):
        super().__init__(request, service)

    def handle(self):
        if (self.service):
            if (self.request.route == '/'):
                return self.service.execute()
            elif (self.request.route == '/section'):
                section = self.request.body['script_config']['config']['section']
                return self.service.get_time_to_section(section, get_time_from_sentence_before = True)
            elif (self.request.route == '/sentence'):
                sentence = self.request.body['script_config']['config']['sentence']
                return self.service.get_time_to_sentence(sentence)                
            else:
                return self.service.execute()



        

    
    