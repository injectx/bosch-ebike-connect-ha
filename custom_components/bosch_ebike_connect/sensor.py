import logging
from homeassistant.components.sensor import SensorEntity

LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass, entry, async_add_entities):

	LOGGER.warning("Sensor setup started")

	data = hass.data["bosch_ebike_connect"][entry.entry_id]
	devices = data["devices"]

	bike = devices["my_ebikes"][0]

	entities = [
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

	LOGGER.warning(f"Adding {len(entities)} sensors")

	async_add_entities(entities, True)


class BoschSensor(SensorEntity):

	def __init__(self, unique_id, name, value):
		self._attr_unique_id = unique_id
		self._attr_name = name
		self._attr_native_value = value