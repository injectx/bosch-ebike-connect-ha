import aiohttp
import time
import logging

_LOGGER = logging.getLogger(__name__)


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

				self.session = await response.json()
				return self.session


	async def get_devices(self):

		token = f"{self.session['token_value']}:{self.session['mobile_id']}"

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

		token = f"{self.session['token_value']}:{self.session['mobile_id']}"

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


	async def get_trip_detail(self, trip_id):

		token = f"{self.session['token_value']}:{self.session['mobile_id']}"

		headers = {
			"accept": "application/json",
			"protect-from": "CSRF",
			"user-agent": "oea_ios/4.8.1",
			"x-authorization": token
		}

		async with aiohttp.ClientSession() as session:

			async with session.get(
				f"https://www.ebike-connect.com/ebikeconnect/api/activities/trip/details/{trip_id}",
				headers=headers
			) as response:

				data = await response.json()
				
				_LOGGER.warning(
					"ASSIST DATA: %s",
					data.get("significant_assistance_level_percentages")
				)
				
				_LOGGER.warning(
					"POWER DATA: %s",
					{
						"driver": data.get("total_driver_consumption_percentage"),
						"battery": data.get("total_battery_consumption_percentage"),
						"driver_power": data.get("average_driver_power")
					}
				)
				
				_LOGGER.warning(
					"TRIP DETAIL KEYS: %s",
					list(data.keys())
				)
				
				return data


	async def get_statistics(self):

		token = f"{self.session['token_value']}:{self.session['mobile_id']}"

		headers = {
			"accept": "application/json",
			"protect-from": "CSRF",
			"user-agent": "oea_ios/4.8.1",
			"x-authorization": token
		}

		async with aiohttp.ClientSession() as session:

			async with session.get(
				"https://www.ebike-connect.com/ebikeconnect/api/portal/statistics/all_statistics",
				headers=headers
			) as response:

				_LOGGER.warning(
					"STATISTICS STATUS: %s",
					response.status
				)

				return await response.json()