"""
Copyright (c) 2012 Anant Bhardwaj

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from abc import ABCMeta, abstractmethod
from google_voice.main import GoogleVoice
from africa_talking.main import AfricaTalking
import config

'''
@author: anant bhardwaj
@date: Oct 4, 2012

VoiceX public APIs
'''	

class VoiceX:
	def __init__(self, client=config.GV):
		__metaclass__ = ABCMeta
		if(client == config.GV):
			self.client = GoogleVoice(config.GV['username'], config.GV['password'], d = False)
		elif(client == config.AT):
			self.client = AfricaTalking(config.AP['username'], config.GV['api_key'])
		else:
			raise
	
	@abstractmethod	
	def set_callback(self, callback):
		self.client.set_callback(callback)

	@abstractmethod
	def sms(self, to, text):
		self.client.sms(to, text)

	@abstractmethod
	def mark_read(self, msg):
		self.client.mark_read(msg)

	@abstractmethod
	def mark_unread(self, msg):
		self.client.mark_unread(msg)

	@abstractmethod
	def delete(self, msg):
		self.client.delete(msg)

	@abstractmethod
	def fetch_unread_sms():
		self.client.fetch_unread_sms()

	@abstractmethod
	def fetch_all_sms(self):
		self.client.fetch_all_sms()

class Test():
	def __init__(self):		
		self.client = VoiceX()
		self.client.set_callback(callback = self.msg_new)

	def msg_new(self, msg):
		print "Got text [ %s ] from [%s]." %(msg['text'], msg['from'])
		print self.client.mark_read(msg)
		print self.client.sms(msg['from'], "Ack :" + msg['text'])
		print self.client.delete(msg)

def main():	
	Test()



if __name__ == "__main__":
	main()
