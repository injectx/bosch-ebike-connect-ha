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
	
	trips = await api.get_trips()
	
	LOGGER.warning(f"Bosch trips: {trips}")

	LOGGER.warning("Bosch devices loaded")

	hass.data[DOMAIN][entry.entry_id] = {
		"api": api,
		"devices": devices
	}

	await hass.config_entries.async_forward_entry_setups(
		entry,
		["sensor"]
	)

	return True


async def async_unload_entry(hass, entry):

	hass.data[DOMAIN].pop(entry.entry_id, None)

	return True