from add_time.controllers.base_controller import BaseController
from add_time.services.base_service import BaseService

from add_time.models.request import Request

from add_time.factories.base_factory import BaseFactory

#Infra
from add_time.infra.add_time import AddTime


#Services
from add_time.services.add_time_service import AddTimeService

#Controllers
from add_time.controllers.add_time_controller import  AddTimeController

from add_time.utils.helpers import *


class Factory(BaseFactory):
   
  
    def __init__(self, request: Request, logger = None):
        super().__init__(request, logger)                                      

       

    
    def make_script(self, script_name, general_config, script_config):
        return AddTime(script_config, self.logger)
        
        
  
    def make_service(self, script_name, general_config, script_config) -> BaseService:
        
        script_config = script_config['config']

        generator = self.make_script(script_name, general_config, script_config)
        
        script_config = { **script_config, 'script_name': script_name}

        return AddTimeService(script_config, generator = generator)

        

    def make_controller(self) -> BaseController:
        
        route = self.request.route
        script_name = self.get_script_name(route)
        service = self.make_service(script_name, self.general_config, self.script_config)
        
        controller = AddTimeController(self.request, service)

        return controller     



        

    
    