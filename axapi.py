import json
import requests
requests.packages.urllib3.disable_warnings()
from getpass import getpass

class A10(object):
	version = 3
	def __init__(self,hostname):
		self.hostname = hostname
		self.base_url = f'https://{hostname}/axapi/v{self.version}'
		self.session = requests.Session()
		self.token = ''
		return

	def authenticate(self,username,password=''):
		url = f'{self.base_url}/auth'
		data = {
			'credentials':  {
				'username':     username,
				'password':     '',
			}
		}
		if password:
			data['credentials']['password'] = password
		else:
			data['credentials']['password'] = getpass('Password: ')
		response = self.session.post(url, json=data, verify=False)
		if response.status_code == 200:
			print('[I] Logon successful')
			token_raw = json.loads(response.text)
			self.token = token_raw['authresponse']['signature']
			headers = {
				'Authorization':	f'A10 {self.token}',
			}
			self.session.headers.update(headers)
		else:
			print('[E] Login failed')
		return

	def set_active_partition(self, partition):
		url = f'{self.base_url}/active-partition/{partition}'
		data = {
			'active-partition': {
				'curr-part-name':       partition,
			}
		}
		response = self.session.post(url, json=data, verify=False)
		if response.status_code == 200:
			print(f'[I] Active Partition : {partition}')
		else:
			print(f'[W] Failed to change Active Partition')
		return

	def get_slb_server_list(self):
		# TODO
		return

	def get_slb_server_stats(self, server):
		url = f'{self.base_url}/slb/server/{server}/stats'
		response = self.session.get(url, verify=False)
		output = response.text
		return output

	def logoff(self):
		url = f'{self.base_url}/logoff/'
		response = self.session.get(url)
		if response.status_code == 200:
			print('[I] Logoff successful')
		else:
			print('[W] Logoff failed')
		return

if __name__ == '__main__':
	#host = 'sga10-01'
	un = 'jack_sparrow'
	partition = 'INSIDE'
	server = 'server_APRDAPPVM046.oesc.ca'
	a = A10(host)
	a.authenticate(un)
	a.set_active_partition('INSIDE')
	stats = a.get_slb_server_stats(server)
	print(stats)
	a.logoff()