from .api import BoschApi

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

	print(devices)

	hass.data[DOMAIN][entry.entry_id] = {
		"api": api,
		"devices": devices
	}

	return True


async def async_unload_entry(hass, entry):
	hass.data[DOMAIN].pop(entry.entry_id)
	return True