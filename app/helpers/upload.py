import os
import uuid
from flask import current_app

def get_real_path():
    return os.path.join(os.path.realpath('.'), current_app.config['FILES_FOLDER'])

def upload_pdf(filedata):
    if filedata.filename != '':
        filename = str(uuid.uuid1()) + '.pdf'
        fullname = os.path.join(get_real_path(),filename)
        filedata.save(fullname)
        return fullname
