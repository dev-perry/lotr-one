class Authenticate:
    def verify(func):
        def inner(self):
            if self.auth == "no_auth":
                raise Exception("This method cannot be called without passing an authentication key. Visit https://the-one-api.dev/ to create one")
            else:
                func(self)
        return inner