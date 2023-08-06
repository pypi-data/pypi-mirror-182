import readtime

def get_text_duration(text):
    result = readtime.of_text(text)
    return result.seconds


def read_from_file(file):
   with open(file) as f:
      return f.read()

def save_file(filename, content):
      f = open(filename, 'w')
      f.write(content)
      f.close()  
      return filename
