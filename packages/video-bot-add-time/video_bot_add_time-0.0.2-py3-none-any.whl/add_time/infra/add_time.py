from add_time.utils.helpers import get_attr, set_attr
from add_time.infra.script import Script
from add_time.utils.audio import get_audio_duration
from add_time.utils.text import get_text_duration

SCRIPT_NAME = 'Add times'
ERROR_MESSAGE = 'could not add times'
TO_BE_IMPLEMENTED_MESSAGE = 'add times to be implemented'

DEFAULT_TITLE_TIME = 5.0
DEFAULT_ADD_SECONDS_TO_DURATION = 0.0
DEFAULT_TEMPORARY_DIRECTORY = './tmp'
DEFAULT_USE_NARRATION = False

TIME_ROBOT_NO_VIDEOS_BY_SECTION="No Videos for keyword ###keyword###"
TIME_ROBOT_NO_IMAGES_BY_SECTION="No Images for keyword ###keyword###"
TIME_ROBOT_NO_IMAGES="No Images for keyword ###keyword###"
TIME_ROBOT_NO_VIDEOS="No Videos for keyword ###keyword###"

class AddTime(Script):
   
    def __init__(self, config, logger = None):
        
        
        super().__init__(config, logger)

        self.config = config

        self.on_lambda = get_attr(self.config, 'on_lambda', False)
        self.temp_directory = get_attr(self.config, 'temp_directory', DEFAULT_TEMPORARY_DIRECTORY)

        self.add_seconds_to_duration = get_attr(self.config, 'add_seconds_to_duration', DEFAULT_ADD_SECONDS_TO_DURATION)
        self.title_time = get_attr(self.config, 'title_time', DEFAULT_TITLE_TIME)
        self.use_narration = get_attr(self.config, 'use_narration', DEFAULT_USE_NARRATION)

        
    def validate(self):
        pass
    
    def add_duration(self, time):
        return time + self.add_seconds_to_duration   

    def get_time_to_section(self, section, get_time_from_sentences_before = False):

        if (not hasattr(section, 'time')):
                set_attr(section,'time', 0)

        section_time = get_attr(section, 'time', None)    
        if (section_time == None):
            set_attr(section, 'time', 0)  

        is_ad = get_attr(section, 'is_ad', False)    
        if (is_ad == True):
            keywords = get_attr(section, 'keywords', [])    
            for keyword in keywords:
                keyword_videos = get_attr(keyword, 'videos', [])    
                for video in keyword_videos:
                    video_time  =get_attr(video, 'time', 0)
                    set_attr(section, 'time', section_time  + video_time )
                    section_time = get_attr(section, 'time', 0)
                    

        else:
            sentences = get_attr(section, 'sentences', [])    
            for sentence in sentences:
                if (get_time_from_sentences_before):
                    sentence = self.get_time_to_sentence(sentence)
                sentence_time  =get_attr(sentence, 'time', 0)
                
                set_attr(section, 'time', section_time  + sentence_time )
                section_time = get_attr(section, 'time', 0)

        return section 


    def get_time_to_sections(self, sections):
        
        for section in sections:
            section = self.get_time_to_section(section)
            
        return sections
    
    def get_number_of_images(self, keywords):
        count = 0
        for keyword in keywords:
            keyword_images = get_attr(keyword, 'images', [])
            count = count + len(keyword_images)
        return count

    def get_number_of_videos(self, keywords):
        count = 0
        for keyword in keywords:
            keyword_videos = get_attr(keyword, 'videos', [])
            count = count + len(keyword_videos)
        return count


    def get_time_to_images(self, sections):
        for section in sections:
            sentences = get_attr(section, 'sentences', [])

            for sentence in sentences:

                sentences_keywords = get_attr(sentence, 'keywords', [])

                number_of_images = self.get_number_of_images(sentences_keywords)
                for keyword in sentences_keywords:
                    if (number_of_images > 0):
                        time = get_attr(sentence, 'time', 0)
                        image_time = time  / number_of_images 
                        keyword_images = get_attr(keyword, 'images', [])
                        for image in keyword_images:
                            set_attr(image, time, image_time)
                    else:
                        keyword_text = get_attr(keyword, 'text', '')
                        self.logger.warning(str(TIME_ROBOT_NO_IMAGES).replace('###keyword###', keyword_text))        
        return sections


    def get_time_to_images_by_section(self, sections):
        for section in sections:
                section_keywords = get_attr(section, 'keywords', [])
                number_of_images = self.get_number_of_images(section_keywords)
                for keyword in section_keywords:
                    if (number_of_images > 0):
                        section_time = get_attr(section, 'time', 0)
                        image_time = section_time  / number_of_images 
                        keyword_images = get_attr(keyword, 'images', [])
                        for image in keyword_images:
                            set_attr(image, 'time', image_time)
                    else:
                        keyword_text = get_attr(keyword, 'text', '')
                        self.logger.warning(str(TIME_ROBOT_NO_IMAGES_BY_SECTION).replace('###keyword###', keyword_text))        
        return sections


    def get_time_to_videos(self, sections):
        for section in sections:
            sentences = get_attr( section, 'sentences', [])

            for sentence in sentences:

                sentences_keywords = get_attr(sentence, 'keywords', [])
                number_of_videos = self.get_number_of_videos(sentences_keywords)

                for keyword in sentences_keywords:
                    if (number_of_videos > 0):
                        sentence_time = get_attr(sentence, 'time', 0)
                        video_time = sentence_time  / number_of_videos 
                        keyword_videos = get_attr(keyword, 'videos', [])
                        for video in keyword_videos:
                            set_attr(video, 'time', video_time)
                    else:
                        keyword_text = get_attr(keyword, 'text', '')
                        self.logger.warning(str(TIME_ROBOT_NO_VIDEOS).replace('###keyword###', keyword_text))        
        return sections


    def get_time_to_videos_by_section(self, sections):

        for section in sections:
                section_keywords = get_attr(section, 'keywords', [])
                number_of_videos = self.get_number_of_videos(section_keywords)
                for keyword in section_keywords:
                    if (number_of_videos > 0):
                        section_time = get_attr(section, 'time', 0)
                        video_time = section_time  / number_of_videos 
                        keyword_videos = get_attr(keyword, 'videos', [])
                        for video in keyword_videos:
                            set_attr(video, 'time', video_time)
                    else:
                        keyword_text = get_attr(keyword, 'text', '')
                        self.logger.warning(str(TIME_ROBOT_NO_VIDEOS_BY_SECTION).replace('###keyword###', keyword_text))        
        return sections


    

    def get_time_to_title_sentence(self, sentence):
        
        sentence_speech = None

        if (self.use_narration == True):

            sentence_speech = get_attr(sentence, 'speech', None)

            if (sentence_speech != None):
                speech_file = get_attr(sentence_speech, 'file', None)

            if (speech_file != None and speech_file != ''):

                duration = get_audio_duration(speech_file)
                added_time = self.add_duration(duration) 
                set_attr(sentence_speech, 'time', added_time)
                set_attr(sentence, 'time', self.title_time )

            else:
                set_attr(sentence, 'time', self.title_time )
                
                if (sentence_speech != None):
                    set_attr(sentence_speech, 'time', 0)

        else:
            set_attr(sentence, 'time', self.title_time )
            
            if (sentence_speech != None):
                set_attr(sentence_speech, 'time', 0)
                sentence.speech.time = 0 

        sentence_subtitles = get_attr(sentence, 'subtitles', [])
        for subtitle in sentence_subtitles:
            set_attr(subtitle, 'time', self.title_time)


        return sentence     


    def get_time_to_sentence(self, sentence):
        
        text = get_attr(sentence, 'text', '')
        sentence_speech = None

        if (self.use_narration == True):
            sentence_speech = get_attr(sentence, 'speech', None)
            speech_file = get_attr(sentence_speech, 'file', None)
            
            if (speech_file != None and speech_file != ''):
                duration = get_audio_duration(speech_file)
                added_time = self.add_duration(duration) 
                set_attr(sentence_speech, 'time', added_time)
                set_attr(sentence, 'time', added_time)
            else:
                duration = get_text_duration(text)
                added_time = self.add_duration(duration) 
                set_attr(sentence, 'time', added_time)
                
                if (sentence_speech != None):
                    set_attr(sentence_speech, 'time', 0)

        else:
            duration = get_text_duration(text)
            added_time = self.add_duration(duration) 
            set_attr(sentence, 'time', added_time)

            if (sentence_speech != None):
                 set_attr(sentence_speech, 'time', 0)


        subtitles = get_attr(sentence, 'subtitles', [])
        for subtitle in subtitles:
            subtitle_text = get_attr(subtitle, 'text', '')
            duration = get_text_duration(subtitle_text)
            set_attr(subtitle, 'time', duration)


        return sentence    

    
       

    def get_time_to_sentences(self, sections):
        
        for section in sections:

            is_title  =  get_attr(section, 'is_title', False)
            sentences =  get_attr(section, 'sentences', [])

            for sentence in sentences:

                if (is_title == False):
                    sentence = self.get_time_to_sentence(sentence)
                else:
                    sentence = self.get_time_to_title_sentence(sentence)

        return sections


    
    def get_time(self, items, field):
        total_time = 0
        _time = 0
        if (items !=None):
            for item in items:
                if (item != None):
                    _time = get_attr(item, field)
                    if (_time != None):
                        total_time = total_time + _time
            return total_time
        else:
            return 0

    def get_total_time(self, content, total_content_time):
        
        total_time = 0

        logo_intro_time = self.get_time([get_attr(content,'logointro', None)], 'video_time')
        disclaimers_time = self.get_time(get_attr(content,'disclaimers', None), 'time')
        ads_time = 0 #TODO - ads time #await self.get_time(content.ads, 'ad_video_time')
        intro_time = self.get_time([get_attr(content,'intro', None)], 'video_time')
        credits_time = self.get_time([get_attr(content,'credits', None)], 'video_time')

        total_time = logo_intro_time + disclaimers_time +  intro_time + credits_time + ads_time

        return total_content_time + total_time

    def run(self, data):

      result = None

      try:

        self.start()
        self.validate()
        
        sections = data
        result = self.get_times(sections)

      except Exception as err:
          print(ERROR_MESSAGE)
          print(str(err))
          pass
      finally:
          self.end()      
        
         
      return result




    












    
    

         
