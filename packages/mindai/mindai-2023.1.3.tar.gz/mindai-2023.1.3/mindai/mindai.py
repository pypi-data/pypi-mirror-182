import requests,os
# See and Enjoy ;)
# Apis are public to use.

class Ai:

    def __init__(self):
        self.main_api = "https://reback.ml/v1/api/make/"
        self.main_api2 = "https://reback.ml/"
    def text_to_anime(self,prompt=None):
        """
        Make Anime arts from Prompt!
        :param prompt:
        """
        try:
            r = requests.get(self.main_api2+"art",params={"prompt":prompt}).json()
            if r['success']:
                a = r['url']
                return {"success":True,"url":a}
            else:
                return {"success":False,"message":r['message']}

        except Exception as e:
            return {"success":False,"message":e}
    def prompt_extend(self,prompt=None):
        """
        This tool can make A prompt and add more description for your prompt
        :param prompt:
        """
        try:
            r = requests.get(self.main_api2+"prompt-extend",params={"short":prompt}).json()
            if r['success']:
                a = r['text']
                return {"success":True,"text":a}
            else:
                return {"success":False,"message":r['message']}

        except Exception as e:
            return {"success":False,"message":e}
    def complete_setnece(self,setnece=None):
        """
        This Tool complete your word just add ( * ) in place you want to complete.
        :param setnece:
        """
        try:
            r = requests.get(self.main_api2+"complete",params={"words":setnece}).json()
            if r['success']:
                a = r['setneces']
                return {"success":True,"setneces":a}
            else:
                return {"success":False,"message":r['message']}

        except Exception as e:
            return {"success":False,"message":e}
    def get_verbs(self,setnece=None):
        """
        This tool Get Who talk name and Orgs name and His location, if found in setneces.
        :param setnece:
        """
        try:
            r = requests.get(self.main_api2+"get-verbs",params={"words":setnece}).json()
            if r['success']:
                a = r['verbs']
                return {"success":True,"verbs":a}
            else:
                return {"success":False,"message":r['message']}

        except Exception as e:
            return {"success":False,"message":e}
    def dalle_2(self,prompt=None):
        """
        Use Dalle-2 Model!
        :param prompt:
        """
        try:
            r = requests.get(self.main_api2+"dalle-2",params={"prompt":prompt}).json()
            if r['success']:
                a = r['url']
                return {"success":True,"url":a}
            else:
                return {"success":False,"message":r['message']}

        except Exception as e:
            return {"success":False,"message":e}
    def image_to_text(self,url=None):
        """
        You can get text in image, only URLS!
        :param url:
        :return: JSon response
        """
        try:
            r = requests.get(self.main_api2+"as",params={"url":url,})
            if r.status_code ==200:
                self.code = r.json()['text']
                return {"error":None,"text":self.code}
            else:
                self.error = r.json()['message']
                return {"error":True,"message":self.error}
        except Exception as e:
            self.error = r.json()['message']
            return {"error":True,"message":self.error}
    def word_mean(self,word=None):
        """
        Get word meaning and get example to use it.
        :param word: 
        :return: JSon response
        """
        try:
            r = requests.get(self.main_api2+"mean",params={"word":word})
            if r.status_code ==200:
                self.code = r.json()['examples']
                return {"error":None,"mean":self.code}
            else:
                self.error = r.json()['message']
                return {"error":True,"message":self.error}
        except Exception as e:
            self.error = r.json()['message']
            return {"error":True,"message":self.error}
    def chat(self,message=None):
        """
        Chat with an ai.
        :param message:
        :return Json response
        """
        try:
            r = requests.get(self.main_api2+"chat",params={"message":message})
            if r.status_code ==200:
                self.code = r.json()['reply']
                return {"error":None,"reply":self.code}
            else:
                self.error = r.json()['message']
                return {"error":True,"message":self.error}
        except Exception as e:
            self.error = r.json()['message']
            return {"error":True,"message":self.error}
    def audio_to_text(self,url=None):
        """
        Search for image was maked by ai,
        :param query:
        """
        try:
            r = requests.get(self.main_api2+"stt",params={"url":url})
            if r.status_code ==200:
               
                self.textt = r.json()['text']

                self.confidence = (r.json()['confidence'])
                return {"error":None,"text":self.textt,"success_percentg":self.confidence}
            else:
                self.error = r.json()['message']
                return {"error":True,"message":error}
        except Exception as e:
            self.error = r.json()
            
            return {"error":True,"message":self.error['message']}
    def explain_code(self,code=None,lang=None):
        """
        This defition explain your code.
        :param code:
        :param lang:
        """
        try:
            r = requests.get(self.main_api2+"explain",params={"code":code})
            if r.status_code ==200:
                if lang == "english" or lang == "en" or lang == None:
                    self.textt = r.json()['explain']
                    return {"error":None,"explained":self.textt,}
                elif lang == "arabic" or lang == "ar":
                    self.textt = r.json()['explain']
                    c = requests.get(self.main_api2+"trans",params={"text":self.textt})
                    self.translated = c.json()['text']
                    return {"error":None,"explained":self.translated,}
                else:
                    return {"error":None,"explained":self.textt,}
            else:
                self.error = r.json()['message']
                return {"error":True,"message":error}
        except Exception as e:
            self.error = r.json()
            return {"error":True,"message":self.error['message']}
    def image_search(self,query=None):
        """
        Search for image was maked by ai,
        :param query:
        """
        try:
            r = requests.get(self.main_api2+"sai",params={"word":query})
            if r.status_code ==200:
                self.code = r.json()['imgs']
                self.count = len(r.json()['imgs'])
                return {"error":None,"images":self.code,"count":self.count}
            else:
                self.error = r.json()['message']
                return {"error":True,"message":self.error}
        except Exception as e:
            self.error = r.json()['message']
            return {"error":True,"message":self.error}
    def code_gen(self,prompt=None,lang=None):
        """
        Prompt to Code, (code generateor).
        :param prompt: 
        :param lang: 
        :return: JSon response
        """
        try:
            r = requests.get(self.main_api,params={"prompt":prompt,"lang":lang,})
            if r.status_code ==200:
                self.code = r.json()['code']
                return {"error":None,"code":self.code}
            else:
                self.error = r.json()['message']
                return {"error":True,"message":self.error}
        except Exception as e:
            self.error = r.json()['message']
            return {"error":True,"message":self.error}
