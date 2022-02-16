from authenticate import Authenticate
from requester import build_path, call

class LOTR:

    def __init__(self, auth="no_auth"):
        self.auth = auth

    def get_book(self, id=None, chapter=False):
        path = build_path("book", id, chapter)
        return call(path)
    
    @Authenticate.verify
    def get_movie(self, id=None, quote=False):
        path = build_path("movie", id, quote)
        return call(path, self.auth)
    
    @Authenticate.verify
    def get_character(self, id=None, quote=False):
        path = build_path("character", id, quote)
        return call(path, self.auth)
    
    @Authenticate.verify
    def get_quote(self, id=None):
        path = build_path("quote", id)
        return call(path, self.auth)
    
    @Authenticate.verify
    def get_chapter(self, id=None):
        path = build_path("chapter", id)
        return call(path, self.auth)