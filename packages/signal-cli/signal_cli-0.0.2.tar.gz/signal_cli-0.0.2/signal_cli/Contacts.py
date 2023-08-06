## @package signal_cli

import requests, json, os, pathlib
from typing import Union

## @brief Class holding the collection of functions from the Contacts section
# @details This class handles a collection of all functions that are listed in the Contacts section in the documentation of the signal-cli-rest-api
# @author Felix Hune
# @version 1.0
# @date 2022-12-18
class Contacts:
	
	def __init__(self):
		with open(os.path.join(pathlib.Path(__file__).parent.resolve(), "config.json"), "r") as f:
			config = json.load(f)
		self.address = config["address"]
		self.port = str(config["port"])
		self.number = config["number"]
		
	## @brief Update contact
	# @details Calls the API to update the details of an existing contact or, if not existing, creating a new contact with the given information
	# @param	expiration	The time for messages to self-destruct, set 0 for never self-destruct
	# @param	name		The name of the contact
	# @param	recipient	The phone number of the contact, in international format
	# @return Either a @p dict in json format or a @p str
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-18
	def update_contact(self, expiration: int, name: str, recipient: str) -> Union[dict, str]:
		
		payload = {"expiration_in_seconds": expiration, "name": name, "recipient": recipient}
		r = requests.put(f"{self.address}:{self.port}/v1/contacts/{self.number}", headers={"Content-Type": "application/json"}, data=json.dumps(payload))
		
		try:
			r = r.json()
		except:
			r = r.text
		return r
