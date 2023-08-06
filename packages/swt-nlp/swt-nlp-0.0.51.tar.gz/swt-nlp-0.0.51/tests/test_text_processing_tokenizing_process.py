from   swt.nlp.basis import text_processing
import re

# =========================================
# FOCUSING ON DEFAULT TOKENIZING PROCESSES 
# =========================================
def test_default_preprocesses():
    text = 'สวัสดีวันจันทร์ MONDAY อังคาร '
    tp   = text_processing()

    processed_text = tp.preprocesses(text)
    assert processed_text == 'สวัสดีวันจันทร์ monday อังคาร'


def test_default_tokenizer():
    text       = 'สวัสดีวันจันทร์'
    tp         = text_processing()
    
    result     = tp._tokenizer(text)
    assert len(result) == 3
    assert result      == ['สวัสดี', 'วัน', 'จันทร์']


def test_default_postprocesses():
    token      = ['สวัสดี', 'วัน', 'จันทร์']
    tp         = text_processing()
    
    result     = tp.postprocesses(token)
    assert tp._postprocesses == []
    assert len(result)       == 3
    assert result            == ['สวัสดี', 'วัน', 'จันทร์']


def test_text_processing_tokenize_with_defult_processes_combined():
    text   = 'สวัสดีวันจันทร์ MONDAY อังคาร '
    tp     = text_processing()

    result = tp.tokenize(text)
    assert result == ['สวัสดี', 'วัน', 'จันทร์', 'monday', 'อังคาร']


# =========================================
# FOCUSING ON CUSTOM TOKENIZING PROCESSES 
# =========================================
def test_preprocessing_text_custom_preprocess_with_lower_case():
    text   = 'สวัสดีวันจันทร์ MONDAY อังคาร '
    pre    = lambda t: t.lower()

    tp     = text_processing(pre)
    result = tp.preprocesses(text)
    assert result == 'สวัสดีวันจันทร์ monday อังคาร '


def test_preprocessing_text_custom_preprocess_with_adding_remove_special_chars():
    # prebuilt with lower_case preprocessing
    text   = 'เมล์กลับมาที่ SOME_ONE-NO-REPLY@EMAIL.COM #TESTING '
    preset = lambda t: t.lower()
    tp     = text_processing(preset)
    # adding remove_special_char preprocessing
    chars  = r'[^ก-์a-zA-Z0-9 @#-._]'
    remove = lambda t: re.sub(chars, '', t)
    tp.add_preprocess(remove)
    # processing
    result = tp.preprocesses(text)
    # assertation
    assert result == 'เมล์กลับมาที่ some_one-no-reply@email.com #testing '


def test_text_processing_custom_postprocess():
    text   = 'สวัสดีวันจันทร์ MONDAY อังคาร '
    # adding 2 post processes
    post   = [lambda arr: '_'.join(arr), lambda t: f'hello_{t}']
    # init class
    tp     = text_processing(postprocesses=post)
    # tokenize with preprocess and postprocess
    result = tp.tokenize(text)
    # assertation
    assert result == 'hello_สวัสดี_วัน_จันทร์_monday_อังคาร'

