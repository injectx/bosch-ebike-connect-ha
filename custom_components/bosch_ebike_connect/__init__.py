import logging
from .api import BoschApi

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

	LOGGER.warning(f"Bosch devices: {devices}")

	hass.data[DOMAIN][entry.entry_id] = {
		"api": api,
		"devices": devices
	}
	
	await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])

	return True


async def async_unload_entry(hass, entry):
	hass.data[DOMAIN].pop(entry.entry_id)
	return True