from homeassistant.components.sensor import SensorEntity


class BoschBikeTestSensor(SensorEntity):
	_attr_name = "Bosch Bike Test"
	_attr_native_value = "Connected"