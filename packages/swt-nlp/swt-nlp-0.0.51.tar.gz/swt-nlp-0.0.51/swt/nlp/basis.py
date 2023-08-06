import pandas as pd
import muuusiiik.util as msk
import re
from   itertools import product
from   marisa_trie import Trie
from   pythainlp.tokenize import word_tokenize
from   pythainlp.corpus import thai_words, thai_stopwords
#from   sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer



        
        

class base_processing:
    TEXT_PATTERN   = r'[^ก-์a-zA-Z0-9 ]'
    THAI_WORDS     = thai_words
    THAI_STOPWORDS = thai_stopwords

    def preprocess(text, text_pattern=None) -> str:
        """ set preprocess method such as lower, filter some char out
        """
        try:
            text_pattern = text_pattern if text_pattern else base_processing.TEXT_PATTERN
            text = text.lower()
            text = re.sub(text_pattern, ' ', text)
            text = re.sub(r'\s+', ' ', text)
            text = text.strip()
            return text 
        
        except Exception as e:
            print(f' > preprocessing() error: {str(e)}')
            print(f'   text: {text}')
            return ''
        

    def default_tokenizer(trie_vocab:Trie=None, keep_whitespace:bool=False):
        """ assign default tokenizer using custom dict
        """
        if trie_vocab is None: trie_vocab = Trie(base_processing.THAI_WORDS())
        if type(trie_vocab) == list: trie_vocab = Trie(trie_vocab)
        tokenizer = lambda text: word_tokenize(text, keep_whitespace=keep_whitespace, custom_dict=trie_vocab)
        return tokenizer



class text_processing:
    """ objective: doing these followings
        * preprocessing  - e.g., lower case, remove special chars, normalize term, etc
        * tokenizing     - segmentation
        * postprocessing - e.g., weighting, combine tokens, etc
    """
    def __init__(self, preprocesses=None, tokenizer=None, postprocesses=None, verbose:bool=False, **kwargs):
        self._verbose = verbose
        self.reset()
        self.load(preprocesses, tokenizer, postprocesses, **kwargs)


    def reset(self):
        self._preprocesses   = []
        self._tokenizer      = None
        self._postprocesses  = []


    # ref https://tutorial.eyehunts.com/python/constructor-overloading-in-python-example-code/
    @classmethod
    def from_configure(cls, f_configure, verbose:bool=True):
        try:
            # load configure
            configure = msk.configure_loader(f_configure)
            # handling tokenizer
            f_vocab_list    = configure.get('vocab')
            vocab_list      = msk.data.load_file_list(f_vocab_list, verbose=verbose)
            tokenizer       = base_processing.default_tokenizer(vocab_list)
            return cls(tokenizer=tokenizer, verbose=verbose)

        except FileNotFoundError as e:
            raise e

        except TypeError as e:
            raise e

        except Exception as e:
            raise e


    def _validate_process(self, process, default_process):
        """ validate if the given process is set
            return default_process if None is given
            return nothing if empty list is given
        """
        # case of something is assigned
        if process: return process
        # case of None or [] is assigned
        else: return default_process if process is None else None
        

    def load(self, preprocesses=None, tokenizer=None, postprocesses=None, **kwargs):
        """ assign preprocess, tokenizer and postprocess
        """
        # validate content
        preprocesses  = self._validate_process(preprocesses,  base_processing.preprocess)
        tokenizer     = self._validate_process(tokenizer,     base_processing.default_tokenizer())
        postprocesses = self._validate_process(postprocesses, [])

        # ASSIGN PREPROCESS
        if preprocesses:  self.add_preprocess(preprocesses)

        # ASSIGN TOKENIZER
        if tokenizer:   self._tokenizer = tokenizer

        # ASSIGN POSTPROCESS
        if postprocesses: self.add_postprocess(postprocesses)





    # ---------------------------------
    # text_processing: adding processes
    # ---------------------------------
    def _add_single_preprocess(self, fnc):
        try:
            if callable(fnc):   self._preprocesses.append(fnc)
            else:               raise TypeError('obj {fnc} is not callable')

        except Exception as e:
            raise e


    def _add_single_postprocess(self, fnc):
        try:
            if callable(fnc):   self._postprocesses.append(fnc)
            else:               raise TypeError('obj {fnc} is not callable')

        except Exception as e:
            raise e


    def add_preprocess(self, fnc):
        if type(fnc) == list: [self._add_single_preprocess(f) for f in fnc]
        #    for f in fnc: 
        #        self._add_single_preprocess(f)
        else:                 self._add_single_preprocess(fnc)


    def add_postprocess(self, fnc):
        if type(fnc) == list: [self._add_single_postprocess(f) for f in fnc]
        #    for f in fnc: 
        #        self._add_single_postprocess(f)
        else:                 self._add_single_postprocess(fnc)


    # ------------------------
    # text_processing: actions 
    # ------------------------
    def preprocesses(self, text:str) -> str:
        """ preprocess is a module that input is str and output is str """
        try:
            for idx, process in enumerate(self._preprocesses):
                text = process(text)
            return text

        except Exception as e:
            if self._verbose: print(f'> preprocess() no.{idx} error - {type(e)} - {str(e)}')
            raise e


    def postprocesses(self, tokens):
        """ postprocess is a module that input is tokens (list of str)  and output is any type designed """
        try:
            for idx, process in enumerate(self._postprocesses):
                tokens = process(tokens)
            return tokens

        except Exception as e:
            if self._verbose: print(f'> postprocess() no.{idx} error - {type(e)} - {str(e)}')
            raise e

        
    def tokenize(self, text:str, **kwargs):
        # do preprocessing
        text   = self.preprocesses(text)
        # do tokenizing
        tokens = self._tokenizer(text)
        # do postprocessing
        result = self.postprocesses(tokens)
        return result


        
class _text_processing:
    """ mainly, consisting of 
        * module preprocess - for remove special chars, lower case, etc
        * module tokenizer  - for tokenization task
    """
    def __init__(self, verbose:bool=False):
        self._preprocess = None
        self._tokenizer  = None
        #self._tfidf     = None
        self._vocabs    = []
        self._stopwords = []
        self._whitelist = []
        self._blacklist = []
        #self._tf_params = {}
        self._verbose   = verbose

        self.load()
        
    def load(self, **kwargs):
        self.set_vocabs()
        self.set_preprocess()
        #self.set_tokenizer()
        ## self.__set_tfidf_params()
        #self.set_tfidf()
        
    def set_preprocess(self, preprocess=None):
        if preprocess: self._preprocess = preprocess
        else:          self._preprocess = base_processing.preprocess
        
    def set_tokenizer(self, tokenizer=None, vocab=None, keep_whitespace:bool=False):
        """ if tokenizer is not None, set tokenizer by ignoring other params
        """
        if tokenizer: self._tokenizer = tokenizer
        else:
            if vocab: vocab = vocab if type(vocab) is Trie else Trie(vocab)
            self._vocabs    = vocab
            self._tokenizer = base_processing.default_tokenizer(vocab, keep_whitespace)


    def set_vocabs(self, vocabs=None, stopwords=None, whitelist=None, blacklist=None, is_append:bool=True, verbose:bool=None):
        verbose = verbose if verbose is not None else self._verbose
        try:
            # default vocab setting
            if all([vocabs is None, stopwords is None, whitelist is None, blacklist is None]):
                self._vocabs    = Trie( base_processing.thai_words() )
                self._stopwords = Trie( base_processing.thai_stopwords() )
                self._blacklist = []
                self._whitelist = []
                if verbose: print(f'set default vocab set: {len(self._vocabs)} vocabs')
                return
            # process assigned dict
            #vocabs    = vocabs    if vocabs    else []   if vocabs    == [] else None
            #stopwords = stopwords if stopwords else None if stopwords == [] else None
            #whitelist = whitelist if whitelist else None if whitelist == [] else None
            #blacklist = blacklist if blacklist else None if blacklist == [] else None

            new_vocab = []
            if vocabs:    new_vocab += vocabs 
            if stopwords: new_vocab += stopwords 
            if whitelist: new_vocab += whitelist 
            if blacklist: new_vocab += blacklist

            if is_append:
                # adding assigned dict to original
                if new_vocab: self._vocabs    = Trie(list(self._vocabs)    + new_vocab)
                if stopwords: self._stopwords = Trie(list(self._stopwords) + stopwords)
                if whitelist: self._whitelist = Trie(list(self._whitelist) + whitelist)
                if blacklist: self._blacklist = Trie(list(self._blacklist) + blacklist)
                if verbose: print(f'append new vocabs: {len(self._vocabs)} vocabs')
            else:
                # set new assigned dict
                if new_vocab == []: new_vocab = [' ']  # error prevention
                if vocabs    is not None: self._vocabs    = Trie(new_vocab)
                else:                     self._vocabs    = Trie(list(self._vocabs) + new_vocab)
                if stopwords is not None: self._stopwords = Trie(stopwords)
                if whitelist is not None: self._whitelist = Trie(whitelist)
                if blacklist is not None: self._blacklist = Trie(blacklist)
                if verbose: print(f'set new vocabs: {len(self._vocabs)} vocabs')

        except Exception as e:
            raise(e)

        finally:
            self.update_setting()


#    def set_tfidf(self, tfidf:TfidfVectorizer=None, **kwargs):
#        """ if tfidf is set, ignore the kwargs
#        """
#        try:
#            if tfidf: self._tfidf = tfidf
#            else:     
#                if kwargs: self.__set_tfidf_params(**kwargs)
#                self._tfidf = TfidfVectorizer(**self._tf_params)
#        except Exception as e:
#            raise e
            

#    def __set_tfidf_params(self, is_update:bool=True, **kwargs):
#        if kwargs: 
#            if is_update: self._tf_params.update(kwargs)
#            else:         self._tf_params = kwargs
#        else:      self._tf_params = {'ngram_range':(1,2), 'max_df': 0.9, 'min_df': 20, 
#                                      'max_features': 8_000, 
#                                      'preprocessor': self.preprocess, 
#                                      'tokenizer': self._tokenizer,
#                                      'stop_words': list(self._stopwords)
#                                     }

    def update_setting(self):
        """ after update vocab set, should be update tokenizer & tfidf as well
            ISSUES: this setting focus on using default tokenizer 
        """
        self.set_tokenizer(tokenizer=None, vocab=self._vocabs)
#        self.set_tfidf(preprocessor=self.preprocess, tokenizer=self._tokenizer, stop_words=self._stopwords)
            
            
    def tokenize(self, text, do_preprocess:bool=True, mode='token') -> list:
        if do_preprocess: text = self.preprocess(text)
        token_sent = self._tokenizer(text)
        if mode == 'token':
            return token_sent
        else:
            return ' '.join([re.sub(' ', '_', token) for token in token_sent])
            # return ' '.join(['_'.join(token.split()) for token in token_sent])
  


    
    
