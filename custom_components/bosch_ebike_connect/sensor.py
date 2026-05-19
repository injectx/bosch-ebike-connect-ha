from homeassistant.components.sensor import SensorEntity


async def async_setup_entry(hass, entry, async_add_entities):

	data = hass.data["bosch_ebike_connect"][entry.entry_id]

	devices = data["devices"]
	trips = data["trips"]

	bike = devices["my_ebikes"][0]

	entities = []

	# Bike info

	entities.extend([
		BoschSensor(
			"bike_name",
			"Bosch Bike Name",
			bike["drive_unit"]["device_name"],
			"mdi:bike",
			"bike"
		),
		BoschSensor(
			"motor",
			"Bosch Motor",
			bike["drive_unit"]["product_line_name"],
			"mdi:engine-outline",
			"bike"
		),
		BoschSensor(
			"display",
			"Bosch Display",
			bike["buis"][0]["device_name"],
			"mdi:monitor-dashboard",
			"bike"
		),
		BoschSensor(
			"battery",
			"Bosch Battery",
			bike["batteries"][0]["device_name"],
			"mdi:battery",
			"bike"
		)
	])

	# Last ride
	
	if trips:
	
		rides = trips[0]["ride_headers"]
		
		distance = round(
			sum(float(r["total_distance"]) for r in rides) / 1000,
			1
		)
		
		duration = round(
			sum(int(r["driving_time"]) for r in rides) / 60000
		)
		
		calories = round(
			sum(float(r["calories"]) for r in rides)
		)
		
		max_speed = max(
			float(r["max_speed"]) for r in rides
		)
		
		avg_speed = round(
			sum(
				float(r["avg_speed"]) *
				float(r["total_distance"])
				for r in rides
			) /
			sum(
				float(r["total_distance"])
				for r in rides
			),
			1
		)
		
		location = rides[-1].get(
			"title",
			"Unknown"
		)
	
		distance = round(float(ride["total_distance"]) / 1000, 1)
		duration = round(int(ride["driving_time"]) / 60000)
	
		entities.extend([
	
			BoschSensor(
				"last_distance",
				"Last Ride Distance",
				distance,
				"mdi:map-marker-distance",
				"ride",
				"km"
			),
	
			BoschSensor(
				"last_duration",
				"Last Ride Duration",
				duration,
				"mdi:timer-outline",
				"ride",
				"min"
			),
	
			BoschSensor(
				"last_avg_speed",
				"Last Ride Average Speed",
				float(ride["avg_speed"]),
				"mdi:speedometer",
				"ride",
				"km/h"
			),
	
			BoschSensor(
				"last_max_speed",
				"Last Ride Max Speed",
				float(ride["max_speed"]),
				"mdi:rocket-launch-outline",
				"ride",
				"km/h"
			),
	
			BoschSensor(
				"last_calories",
				"Last Ride Calories",
				round(float(ride["calories"])),
				"mdi:fire",
				"ride",
				"kcal"
			),
	
			BoschSensor(
				"last_location",
				"Last Ride Location",
				ride["title"],
				"mdi:map-marker",
				"ride"
			)
		])

	async_add_entities(entities)


class BoschSensor(SensorEntity):

	def __init__(
		self,
		unique_id,
		name,
		value,
		icon,
		device_type,
		unit=None
	):

		self._attr_unique_id = unique_id
		self._attr_name = name
		self._attr_native_value = value
		self._attr_icon = icon
		self._attr_native_unit_of_measurement = unit

		if device_type == "ride":

			self._attr_device_info = {
				"identifiers": {
					("bosch_ebike_connect", "last_ride")
				},
				"name": "Focus JAM² Last Ride",
				"manufacturer": "Bosch",
				"model": "Ride Statistics",
			}

		else:

			self._attr_device_info = {
				"identifiers": {
					("bosch_ebike_connect", "focus_jam2")
				},
				"name": "Focus JAM² 6.8",
				"manufacturer": "Focus",
				"model": "JAM² 6.8",
			}