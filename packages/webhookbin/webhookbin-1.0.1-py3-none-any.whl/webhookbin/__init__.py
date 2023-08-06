
import requests

class WebhookBin():
    def __init__(
        self,
        url:str='https://webhookbin.net/v1/',
        binid:str=None,
        token:str=None):

        self.url = url
        self.binid = binid
        self.token = token

    def makebin(self,private:str=None):
        header = {}
        header['private'] = str(private)
        mkbinres = requests.get(self.url+'makebin',headers=header)
        self.binid = mkbinres.json().get('binid')
        self.token = mkbinres.json().get('token')
        return mkbinres
    
    def post(
        self,
        data:dict,
        binid:str=None,
        header:dict=None,
        token:str=None):

        if header is None:
            header = {}
        header['Binauth'] = self._gettoken(token)

        if binid is None:
            binid = self.binid

        return requests.post(self.url+'bin/'+self._getbinid(binid),json=data,headers=header)
    
    def get(
        self,
        binid:str=None,
        token:str=None,
        orderby:str=None,
        delete:bool=True):

        header = {}
        header['Binauth'] = self._gettoken(token)
        header['orderby'] = orderby
        header['delete'] = str(delete)
        
        return requests.get(self.url+'bin/'+self._getbinid(binid),headers=header)
    
    def patch(self,binid:str=None):
        return requests.patch(self.url+'bin/'+self._getbinid(binid))

    def _getbinid(self,binid:str):
        if binid is None:
            binid = self.binid
        return binid
    
    def _gettoken(self,token:str):
        if token is None:
            token = self.token
        return token

webbin = WebhookBin()

def makebin(private:str=None):
    """
    private:\n
    \t both: token needed to read and write\n
    \t post: token only needed to write\n
    \t get: token only needed to read\n\n
    
    returns a requests response\n
    response.json()\n
    response.text\n
    """
    return webbin.makebin(private=private)

def post(
    data:dict,
    binid:str=None,
    headers:dict=None,
    token:str=None):
    """
    data: dict form will be sent as json\n
    binid: set binid if None will use binid from makebin\n
    headers: custom headers as dict\n
    token: set token if None will use token from makebin\n\n

    returns a requests response\n
    response.json()\n
    response.text\n
    """
    return webbin.post(data=data,binid=binid,header=headers,token=token)

def get(
    binid:str=None,
    token:str=None,
    orderby:str=None,
    delete:bool=True):
    """
    binid: set binid if None will use binid from makebin\n
    token: set token if None will use token from makebin\n
    orderby: acending (oldest first) or decending\n
    delete: true or false if message should be deleted\n\n

    returns a requests response\n
    response.json()\n
    response.text\n
    """
    return webbin.get(binid=binid,token=token,orderby=orderby,delete=delete)

def patch(binid:str=None):
    """
    binid: set binid if None will use binid from makebin\n\n

    returns a requests response\n
    response.json()\n
    response.text\m
    """
    return webbin.patch(binid=binid)
