
from .defined import defined_payloads


def parse(msg):
	type_id = msg.type_id
	payload = msg.payload
	specified_payload = defined_payloads[type_id]
	parsed_params = payload.split(',')
	assert specified_payload['id'] == type_id
	result_dict = {}
	for i, param in enumerate(specified_payload['parameters']):
		name = param[0]
		param_type = param[1]
		result_dict[name] = param_type(parsed_params[i])
	return result_dict