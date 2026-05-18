DOMAIN = "bosch_ebike_connect"


async def async_setup(hass, config):
	hass.data.setdefault(DOMAIN, {})
	return True


async def async_setup_entry(hass, entry):
	hass.data[DOMAIN][entry.entry_id] = entry.data
	return True


async def async_unload_entry(hass, entry):
	hass.data[DOMAIN].pop(entry.entry_id)
	return True