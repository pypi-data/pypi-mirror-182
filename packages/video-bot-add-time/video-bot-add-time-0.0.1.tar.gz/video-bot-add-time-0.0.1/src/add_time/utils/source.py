from add_time.utils.helpers import get_attr
from add_time.utils.object_factory import generate_source

DEFAULT_MONGO_FILES_TABLE = 'fs.files'
DEFAULT_MONGO_DATABASE_NAME = 'filesdb'



def generate_source_mongo(result, config):

        mongo_files_table = get_attr(config ,'mongo_files_table', DEFAULT_MONGO_FILES_TABLE)
        mongo_database_name = get_attr(config ,'mongo_database_name', DEFAULT_MONGO_DATABASE_NAME)
            
        source = generate_source(file_id = str(result['mongo_file_id']), 
                                     file_path = result['file'], 
                                     repository_id = result['repository_id'], 
                                     database_uri = config['mongo_uri'], 
                                     database_table_name = mongo_files_table,
                                     database_name = mongo_database_name)

        return source



def generate_source_s3(result, config):
        source = generate_source(file_id=result['target'], 
                                 file_path=result['target'], 
                                 bucket_name=config['target_bucket'])    
        return source



def generate_source_fs(result, config):
        source = generate_source(file_id=result['target'], 
                                 file_path=result['target'])    
        return source    



def build_source_object(result, config ):

        if (config['type'] == 'mongo'):
            source = generate_source_mongo(result, config)
        elif (config['type']  == 's3'):
            source = generate_source_s3(result, config)    
        elif (config['type']  == 'local'):    
            source = generate_source_fs(result, config)    
        else:
            raise Exception('config type not available')    

        return source
