import aiohttp


class BoschApi:

	def __init__(self, email, password):
		self.email = email
		self.password = password
		self.session = None

	async def login(self):

		async with aiohttp.ClientSession() as session:

			payload = {
				"mobile_id": "C5A16D86-3AC4-48B1-A851-63BAD39EAEC5",
				"username": self.email,
				"password": self.password
			}

			headers = {
				"accept": "application/vnd.ebike-connect.com.v4+json, application/json",
				"content-type": "application/json",
				"protect-from": "CSRF",
				"user-agent": "oea_ios/4.8.1"
			}

			async with session.post(
				"https://www.ebike-connect.com/ebikeconnect/api/app/token/public",
				json=payload,
				headers=headers
			) as response:

				data = await response.json()

				self.session = data

				return data

	async def get_devices(self):

		token = (
			f"{self.session['token_value']}:"
			f"{self.session['mobile_id']}"
		)

		headers = {
			"x-authorization": token,
			"accept": "application/json"
		}

		async with aiohttp.ClientSession() as session:

			async with session.get(
				"https://www.ebike-connect.com/ebikeconnect/api/app/devices/my_ebikes",
				headers=headers
			) as response:

				return await response.json()
				
	async def get_trips(self):
	
	token = (
		f"{self.session['token_value']}:"
		f"{self.session['mobile_id']}"
	)
	
	headers = {
		"x-authorization": token,
		"accept": "application/json"
	}
	
	async with aiohttp.ClientSession() as session:
	
		async with session.get(
			"https://www.ebike-connect.com/ebikeconnect/api/app/activities/trip/headers?max=10&offset=0",
			headers=headers
		) as response:
	
			return await response.json()