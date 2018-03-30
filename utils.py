import urllib.request, json 

def get_json_from_url(link):
	req = urllib.request.Request(link, headers={'User-Agent' : "Magic Browser"}) 
	data = {}
	with urllib.request.urlopen(req) as url:
		data = json.loads(sanitize_json_chars(url.read().decode()))
	return data

def sanitize_json_chars(json):
	return json.replace('\r', '').replace('\n', '')

# BEGIN FETCHING DATA

# Using WF Mobile API
def fetch_warframes_and_archwings():
	data = get_json_from_url("http://content.warframe.com/MobileExport/Manifest/ExportWarframes.json")["ExportWarframes"]
	temp = [item['name'].title() for item in data]
	warframes = []
	archwings = []
	for item in temp:
		if item.split()[0] == "<Archwing>":
			archwings.append(item.replace("<Archwing> ", ""))
		else:
			warframes.append(item)
	return sorted(warframes), sorted(archwings)

def fetch_weapons():
	data = get_json_from_url("http://content.warframe.com/MobileExport/Manifest/ExportWeapons.json")["ExportWeapons"]
	weapons = [item['name'].title() for item in data]
	return sorted(weapons)


def fetch_companions():
	print("Not implemented")


# Using Framedex API
def fetch_all(framedex_user="792962eb1e06dd8b0f76601758ba983bda569912"):
	unmastered_link = "http://framedex-api-env.fnejsgued2.eu-west-2.elasticbeanstalk.com/getUnleveled?id=" + framedex_user
	data = get_json_from_url(unmastered_link)
	mastered_link = "http://framedex-api-env.fnejsgued2.eu-west-2.elasticbeanstalk.com/getLeveled?id=" + framedex_user
	data += get_json_from_url(mastered_link)

	primaries, secondaries, melees, warframes = [], [], [], []
	kubrows, kavats, helminths, amps, zaws = [], [], [], [], []
	archwings, aw_primaries, aw_melees, sentinels, sentinel_weapons = [], [], [], [], []
	for item in data:
		name = item["name"]
		eq_type = item["eq_type"]
		# Traitional Weapons
		if eq_type == "primary":
			primaries.append(name)
		elif eq_type == "secondary":
			secondaries.append(name)
		elif eq_type == "melee":
			melees.append(name)
		# Frames
		elif eq_type == "warframe":
			warframes.append(name)
		# Amps/Zaws
		elif eq_type == "amp":
			amps.append(name)
		elif eq_type == "zaw":
			zaws.append(name)
		# AW and weapons
		elif eq_type == "aw":
			archwings.append(name)
		elif eq_type == "aw_primaries":
			aw_primaries.append(name)
		elif eq_type == "aw_melee":
			aw_melees.append(name)
		# Companions and Weapons
		elif eq_type == "kubrow":
			kubrows.append(name)
		elif eq_type == "kavat":
			kavats.append(name)
		elif eq_type == "helminth":
			helminths.append(name)
		elif eq_type == "sentinel":
			sentinels.append(name)
		elif eq_type == "sentinel_weapons":
			sentinel_weapons.append(name)
		else:
			print(name,"is not of a valid category! Please check it.")

	data_dict = {"primaries" : sorted(primaries), 
				 "secondaries" : sorted(secondaries), 
				 "melees" : sorted(melees), 
				 "warframes" : sorted(warframes),
				 "kubrows" : sorted(kubrows),
				 "kavats" : sorted(kavats),
				 "helminths" : sorted(helminths),
				 "amps" : sorted(amps),
				 "zaws" : sorted(zaws),
				 "archwings" : sorted(archwings),
				 "aw_primaries" : sorted(aw_primaries),
				 "aw_melees" : sorted(aw_melees),
				 "sentinels" : sorted(sentinels),
				 "sentinel_weapons" : sorted(sentinel_weapons)}
	return data_dict

# BEGIN TESTING

def test():
	data = fetch_all()
	print(data)






