class myCredentials:
    '''
    This is a class of my Credentials to 
    import various credentials for use with LexisNexis APIs
    '''
    
    def __init__(self):
        import json
        f=self.getJsonFile()
        dict = json.load(f)
        self.__dict__.update(dict)
    def setKey(self,myDict):
        import json
        self.__dict__.update(myDict)
        print(self.__dict__)
        f=self.getJsonFile('w')
        with f as outfile:
            json.dump(self.__dict__, outfile, indent=4)
    def getJsonFile(self,permission ='r'):
        import json
        import os
        path = os.path.dirname(os.path.abspath(__file__))
        json_file_name = 'myCredentials.json'
        json_file = open(os.path.join(path,json_file_name), permission)
        return json_file
    def getCredentials(self):
        import pprint as pp
        pp.pprint(self.__dict__)
        