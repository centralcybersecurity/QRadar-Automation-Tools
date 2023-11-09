import api

bad_ips = ["1.1.1.1", "2.2.2.2"] 

refset = api.get_ref_set("Bad IP Addresses")
refset["data"] = bad_ips

api.update_ref_set("Bad IP Addresses", refset)