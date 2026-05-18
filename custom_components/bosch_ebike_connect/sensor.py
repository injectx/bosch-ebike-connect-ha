from homeassistant.components.sensor import SensorEntity


async def async_setup_entry(hass, entry, async_add_entities):

	data = hass.data["bosch_ebike_connect"][entry.entry_id]
	devices = data["devices"]

	bike = devices["my_ebikes"][0]

	entities = [
		BoschSensor(
			"bike_name",
			"Bosch Bike Name",
			bike["drive_unit"]["device_name"],
			"mdi:bike"
		),
		BoschSensor(
			"motor",
			"Bosch Motor",
			bike["drive_unit"]["product_line_name"],
			"mdi:engine"
		),
		BoschSensor(
			"display",
			"Bosch Display",
			bike["buis"][0]["device_name"],
			"mdi:monitor-dashboard"
		),
		BoschSensor(
			"battery",
			"Bosch Battery",
			bike["batteries"][0]["device_name"],
			"mdi:battery"
		)
	]

	async_add_entities(entities)


class BoschSensor(SensorEntity):

	def __init__(self, unique_id, name, value, icon):

		self._attr_unique_id = unique_id
		self._attr_name = name
		self._attr_native_value = value
		self._attr_icon = icon

		self._attr_device_info = {
			"identifiers": {
				("bosch_ebike_connect", "focus_jam2")
			},
			"name": "Focus JAM² 6.8",
			"manufacturer": "Focus",
			"model": "JAM² 6.8",
		}