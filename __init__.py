import os
from cudatext import *

INI = app_path(APP_DIR_SETTINGS)+os.sep+'cuda_focus_mode.ini'

if app_api_version()<'1.0.196':
    msg_box('Focus Mode plugin needs newer CudaText >= 1.16.2', MB_OK+MB_ICONERROR)

class Command:
    def __init__(self):
        self.load_opt()

    def load_opt(self):
        self.lexers = ini_read(INI, 'op', 'lexers', 'Fountain,SomeOtherLexer')
        self.dim_value = int(ini_read(INI, 'op', 'dim_value', '150'))

    def save_opt(self):
        ini_write(INI, 'op', 'lexers', self.lexers)
        ini_write(INI, 'op', 'dim_value', str(self.dim_value))

    def config(self):
        self.save_opt()
        file_open(INI)

    def on_caret(self, ed_self):
        self.work()

    def on_lexer(self, ed_self):
        self.work()

    def work(self):
        ed.dim(DIM_DELETE_ALL)

        lexer = ed.get_prop(PROP_LEXER_FILE, '')
        if ','+lexer+',' not in ','+self.lexers+',':
            return

        x, y, x2, y2 = ed.get_carets()[0]
        s = ed.get_text_line(y)
        if not s:
            return

        y1 = y
        while y1>0 and bool(ed.get_text_line(y1-1)): y1-=1
        y2 = y
        max_y = ed.get_line_count()-1
        while y2<max_y and bool(ed.get_text_line(y2+1)): y2+=1

        #print('para', y1, y2)
        if y1>0:
            ed.dim(DIM_ADD, 0, y1-1, self.dim_value)
        ed.dim(DIM_ADD, y2+1, max_y, self.dim_value)
