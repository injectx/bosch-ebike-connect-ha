from homeassistant import config_entries
import voluptuous as vol


class BoschFlowHandler(config_entries.ConfigFlow, domain="bosch_ebike_connect"):
	VERSION = 1

	async def async_step_user(self, user_input=None):
		return self.async_create_entry(
			title="Bosch eBike Connect",
			data={}
		)