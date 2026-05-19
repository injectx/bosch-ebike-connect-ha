import aiohttp
import time


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
			"accept": "application/vnd.ebike-connect.com.v4+json, application/json",
			"protect-from": "CSRF",
			"user-agent": "oea_ios/4.8.1",
			"x-authorization": token
		}

		timestamp = int(time.time() * 1000)

		async with aiohttp.ClientSession() as session:

			async with session.get(
				f"https://www.ebike-connect.com/ebikeconnect/api/app/activities/trip/headers?max=10&offset={timestamp}",
				headers=headers
			) as response:

				return await response.json()


	async def get_trip_detail(self, ride_id):

		token = (
			f"{self.session['token_value']}:"
			f"{self.session['mobile_id']}"
		)

		headers = {
			"accept": "application/vnd.ebike-connect.com.v4+json, application/json",
			"protect-from": "CSRF",
			"user-agent": "oea_ios/4.8.1",
			"x-authorization": token
		}

		async with aiohttp.ClientSession() as session:

			async with session.get(
				f"https://www.ebike-connect.com/ebikeconnect/api/activities/trip/details/{ride_id}",
				headers=headers
			) as response:

				return await response.json()


	async def get_statistics(self):

		token = (
			f"{self.session['token_value']}:"
			f"{self.session['mobile_id']}"
		)

		headers = {
			"accept": "application/vnd.ebike-connect.com.v4+json, application/json",
			"protect-from": "CSRF",
			"user-agent": "oea_ios/4.8.1",
			"x-authorization": token
		}

		async with aiohttp.ClientSession() as session:

			async with session.get(
				"https://www.ebike-connect.com/ebikeconnect/api/dashboard/all_statistics",
				headers=headers
			) as response:

				print("STATISTICS STATUS:", response.status)

				text = await response.text()

				print("STATISTICS RESPONSE:")
				print(text[:1000])

				return await response.json()