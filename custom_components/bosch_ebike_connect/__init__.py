import logging
from .api import BoschApi

LOGGER = logging.getLogger(__name__)

DOMAIN = "bosch_ebike_connect"


async def async_setup(hass, config):
	hass.data.setdefault(DOMAIN, {})
	return True


async def async_setup_entry(hass, entry):

	LOGGER.warning("Bosch setup started")

	email = entry.data["email"]
	password = entry.data["password"]

	api = BoschApi(email, password)

	await api.login()

	LOGGER.warning("Bosch login success")

	devices = await api.get_devices()

	LOGGER.warning("Bosch devices loaded")
	LOGGER.warning(f"Bosch devices: {devices}")

	bike = devices["my_ebikes"][0]

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

	LOGGER.warning("Bosch sensors created")

	hass.data[DOMAIN][entry.entry_id] = {
		"api": api,
		"devices": devices
	}

	return True


async def async_unload_entry(hass, entry):

	hass.data[DOMAIN].pop(entry.entry_id, None)

	return True