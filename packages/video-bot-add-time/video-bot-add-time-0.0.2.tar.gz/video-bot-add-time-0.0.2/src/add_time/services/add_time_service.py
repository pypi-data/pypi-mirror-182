
import time
from os import path, makedirs

from add_time.services.base_service import BaseService
from add_time.utils.helpers import generate_id, get_attr, set_attr


DEFAULT_TEMPORARY_DIRECTORY='/tmp'
NO_SECTIONS = "No sections"

class AddTimeService(BaseService):
    
    def __init__(self, config, generator, downloader = None):

        self.config = config

        self.data = get_attr(self.config, 'data', None)
        self.sentence = get_attr(self.config, 'sentence', None)
        self.section = get_attr(self.config, 'section', None)
        
      
        #workers
        self.generator = generator
        self.downloader = downloader
       
        self.script_name = get_attr(self.config, 'script_name', 'all')

        self.temp_directory =   get_attr(self.config,  'temp_directory', DEFAULT_TEMPORARY_DIRECTORY)
        

    def get_time_to_sentence(self, sentence):

        #if speech exists and file is remote, download it before:
        speech = get_attr(sentence, 'speech', None)
        if (speech != None):
            source = get_attr(speech, 'source', None)
            if (source != None):
                source_bucket = source['bucket_name']
                directory = path.dirname(source['file_path'])
                file = source['file_id']
                download_source = {'source_bucket' : source_bucket, "sources": [{ "directory": directory, "objects": [file] }]}
                self.downloader.reset_sources()
                self.downloader.add_source(download_source)
                self.downloader.run()
        

        return self.generator.get_time_to_sentence(sentence)

    def get_time_to_title_sentence(self, sentence):
        return self.generator.get_time_to_title_sentence(sentence)   

    def get_time_to_section(self, section, get_time_from_sentence_before = False):
        return self.generator.get_time_to_section(section, get_time_from_sentence_before)   
         

    def execute(self):
        
        sections = get_attr(self.data, 'sections', [])
        
        if len(sections) == 0:
            raise Exception(NO_SECTIONS)

        sections = self.generator.get_time_to_sentences(sections)
        sections = self.generator.get_time_to_sections(sections)

        sections = self.generator.get_time_to_images_by_section(sections)
        sections = self.generator.get_time_to_videos_by_section(sections)

        sections = self.generator.get_time_to_images(sections)
        sections = self.generator.get_time_to_videos(sections)    

        return sections