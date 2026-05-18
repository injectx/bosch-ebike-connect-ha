from homeassistant import config_entries
import voluptuous as vol

DOMAIN = "bosch_ebike_connect"

CONF_EMAIL = "email"
CONF_PASSWORD = "password"


class BoschFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
	VERSION = 1

	async def async_step_user(self, user_input=None):
		if user_input is not None:
			return self.async_create_entry(
				title="Bosch eBike Connect",
				data=user_input
			)

		schema = vol.Schema(
			{
				vol.Required(CONF_EMAIL): str,
				vol.Required(CONF_PASSWORD): str,
			}
		)

		return self.async_show_form(
			step_id="user",
			data_schema=schema
		)