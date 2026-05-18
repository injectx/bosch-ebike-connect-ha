import logging
from .api import BoschApi
from .sensor import BoschSensor

LOGGER = logging.getLogger(__name__)

DOMAIN = "bosch_ebike_connect"


async def async_setup(hass, config):
	hass.data.setdefault(DOMAIN, {})
	return True


async def async_setup_entry(hass, entry):

	email = entry.data["email"]
	password = entry.data["password"]

	api = BoschApi(email, password)

	await api.login()

	devices = await api.get_devices()

	bike = devices["my_ebikes"][0]

	sensors = [
		BoschSensor(
			"bike_name",
			"Bosch Bike Name",
			bike["drive_unit"]["device_name"]
		),
		BoschSensor(
			"motor",
			"Bosch Motor",
			bike["drive_unit"]["product_line_name"]
		),
		BoschSensor(
			"display",
			"Bosch Display",
			bike["buis"][0]["device_name"]
		),
		BoschSensor(
			"battery",
			"Bosch Battery",
			bike["batteries"][0]["device_name"]
		)
	]

	hass.states.async_set(
		"sensor.bosch_bike_name",
		bike["drive_unit"]["device_name"]
	)

	hass.states.async_set(
		"sensor.bosch_motor",
		bike["drive_unit"]["product_line_name"]
	)

	hass.states.async_set(
		"sensor.bosch_display",
		bike["buis"][0]["device_name"]
	)

	hass.states.async_set(
		"sensor.bosch_battery",
		bike["batteries"][0]["device_name"]
	)

	return True


async def async_unload_entry(hass, entry):
	return True