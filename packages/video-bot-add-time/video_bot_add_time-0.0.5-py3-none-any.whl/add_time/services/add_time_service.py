
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
        

    def download_file_when_necessary(self, sentence):
        download_required = False
        downloaded_files = []

        #if speech exists and file is remote, download it before:
        speech = get_attr(sentence, 'speech', {})
        if (speech != None):
            source = get_attr(speech, 'source', {})
            if (source != None):
                source_bucket = get_attr(source, 'bucket_name',None)
                if (source_bucket != None): 
                    directory = path.dirname(source['file_path'])
                    file = source['file_id']
                    download_source = {'source_bucket' : source_bucket, "sources": [{ "directory": directory, "objects": [file] }]}
                    self.downloader.reset_sources()
                    self.downloader.add_sources(download_source)
                    download_results, downloaded_files = self.downloader.run()
                    download_required = True
                    if (len(downloaded_files) == 0):
                        raise Exception('download is required,but could not download files from s3 bucket')
                else:
                    download_required = False
                    downloaded_files = []    
            else:
                download_required = False
                downloaded_files = []  

        else:
            download_required = False
            downloaded_files = []

        return (download_required, downloaded_files)                

    def get_time_to_sentence(self, sentence):

        download_required, downloaded_files = self.download_file_when_necessary(sentence)
        if (download_required):
            set_attr(sentence['speech'], 'file', downloaded_files[0] )
                    
        new_sentence_with_time = self.generator.get_time_to_sentence(sentence)
        return new_sentence_with_time

    def get_time_to_title_sentence(self, sentence):

        download_required, downloaded_files = self.download_file_when_necessary(sentence)
        if (download_required):
            set_attr(sentence['speech'], 'file', downloaded_files[0] )
                    
        new_sentence_with_time = self.generator.get_time_to_title_sentence(sentence)
        return new_sentence_with_time

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