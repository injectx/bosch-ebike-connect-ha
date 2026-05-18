from homeassistant.components.sensor import SensorEntity


async def async_setup_entry(hass, entry, async_add_entities):

	data = hass.data["bosch_ebike_connect"][entry.entry_id]

	devices = data["devices"]

	bike = devices["my_ebikes"][0]

	sensors = [

		BoschSensor(
			"Bike Name",
			bike["drive_unit"]["device_name"]
		),

		BoschSensor(
			"Motor",
			bike["drive_unit"]["product_line_name"]
		),

		BoschSensor(
			"Display",
			bike["buis"][0]["device_name"]
		),

		BoschSensor(
			"Battery",
			bike["batteries"][0]["device_name"]
		)
	]

	async_add_entities(sensors)


class BoschSensor(SensorEntity):

	def __init__(self, name, value):
		self._attr_name = f"Bosch {name}"
		self._attr_native_value = value