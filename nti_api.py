#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import json
import sys

class handle_api():
	def __init__(self):
		self.authkey="1c61551026d8a985a3e0e23a862a2b426f9867ea63e08ef2d84eea6e5e38b379"
		self.api1="https://nti.nsfocus.com/api/v1/search/queryString/?"
		pass

	def send(self,tab,argvs):
		if tab=="1":
			parems=""
			for i in argvs:
				parems=parems+i+"&"
		
		url=self.api1+parems
		print url
		request=urllib2.Request(
			url,
			'',
			{'Content-Type':'application/json',"NS-NTI-KEY":self.authkey}
			)
		response = urllib2.urlopen(request)
		data = json.loads(response.read())
		return data

		pass
if __name__ == '__main__':
	api=handle_api()
	argvs=['index=v','query="cve-2017-8890"','startTime=2017-06-14','size=10','endTime=2017-06-18','page=1']
	data=api.send("1",argvs)
	print json.dumps(data, indent=4, sort_keys=False, ensure_ascii=False)