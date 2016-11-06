import logging
import json

from my_pokemon_api import *
from db_accessor import *

from django.shortcuts import render

from django.http import HttpResponse

logger = logging.getLogger("worker")

class Config:
	pass

# Create your views here.
def add_crawl_point(request):
	logger.info("I'm in add_crawl_point")
	# Crawl pokemon data

	# 1. Get cell id from request
	request_obj = json.loads(request.body)
	cell_id = request_obj["cell_id"]
	
	# 2. Call my search api
	config = Config()
	config.auth_service = "ptc"
	config.username = "ppgo0001"
	config.password = "123456"
	config.proxy = "socks5://127.0.0.1:9050"
	api = init_api(config)
	search_response = search_point(cell_id, api)
	result = parse_pokemon(search_response)

	logger.info("Crawl result: {0}".format(json.dumps(result, indent=2)))

	# 3. Store search result into database
	# encounter_id, expire, pokemon_id, latitude, longitude

	for pokemon in result:
		add_pokemon_to_db(pokemon["encounter_id"],
						  pokemon["expiration_timestamp_ms"],
						  pokemon["pokemon_id"],
						  pokemon["latitude"],
						  pokemon["longitude"])

	return HttpResponse("Result")
