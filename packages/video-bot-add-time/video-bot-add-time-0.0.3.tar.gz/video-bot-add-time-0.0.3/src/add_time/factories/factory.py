from add_time.controllers.base_controller import BaseController
from add_time.services.base_service import BaseService

from add_time.models.request import Request

from add_time.factories.base_factory import BaseFactory

#Infra
from add_time.infra.add_time import AddTime

#Downloader
from file_transfer.infra.s3_downloader.s3_downloader import S3Downloader
from file_saver.infra.mongo_downloader.mongo_downloader import MongoDownloader

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

    def make_downloader(self, script_name, general_config, script_config):
        
            if ('downloader' not in script_config):
                return None

            downloader_type = script_config['downloader']['type']

            script_config['downloader'] = { **script_config['downloader'], 'temp_directory': get_attr(script_config,'temp_directory','/tmp') }

            if (downloader_type == 's3'):
                return S3Downloader(script_config['downloader'])
            elif (downloader_type == 'mongo'):
                return MongoDownloader(script_config['downloader'])      
            else:
                raise Exception(f'Downloader type not implemented: {downloader_type}')    

  
        
        
  
    def make_service(self, script_name, general_config, script_config) -> BaseService:
        
        script_config = script_config['config']

        generator = self.make_script(script_name, general_config, script_config)
        downloader = self.make_downloader(script_name, general_config, script_config)
        
        script_config = { **script_config, 'script_name': script_name}

        return AddTimeService(script_config, generator = generator, downloader = downloader)

        

    def make_controller(self) -> BaseController:
        
        route = self.request.route
        script_name = self.get_script_name(route)
        service = self.make_service(script_name, self.general_config, self.script_config)
        
        controller = AddTimeController(self.request, service)

        return controller     



        

    
    