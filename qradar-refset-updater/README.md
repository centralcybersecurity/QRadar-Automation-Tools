# QRadar Reference Set Updater

This script updates QRadar reference sets from external data sources.

QRadar reference sets are essentially customizable lists or datasets that can be used to enrich and categorize events within QRadar.

# Some common uses of QRadar reference sets include:

Blacklists - Lists of IP addresses, domains, hashes etc. that are considered suspicious or malicious. Events containing these can be flagged.

Whitelists - Lists of approved IP addresses, users, applications etc. Used to reduce false positives.

Asset profiles - Can map events to human-readable names or business attributes like locations, departments etc.

Vulnerabilities - Map events to known vulnerabilities like CVE IDs for vulnerability management.

Custom categories - Categorize events using custom labels like "PCI Events", "Ransomware" etc.

Reference sets allow security teams to customize how events are processed in QRadar. Instead of just relying on predefined rules, sets provide flexibility to tailor QRadar to an organization's needs.

They can be populated manually or from external data feeds. The reference set updater script allows automating this population from any external data source.

# Uses of this tool

The QRadar reference set updater script allows automatically updating reference sets in QRadar using external data sources.

Here's a quick explanation of what it does:

api.py contains reusable functions for getting and updating QRadar reference sets via the REST API.

get_ref_set() retrieves the existing set data from QRadar.

update_ref_set() updates the set by sending the modified JSON payload.

refsets.py is where the actual reference set update logic goes. It:

Defines some external data, like a list of bad IP addresses.

Gets the existing "Bad IP Addresses" reference set from QRadar using get_ref_set().

Updates the data field of the reference set with the external list.

Sends the updated set back to QRadar via update_ref_set()

This allows dynamically updating QRadar reference sets like bad IPs, usernames, domains etc. from any external data source. The script can be scheduled to run automatically to sync the data on a regular basis.

## Usage

1. Update `src/refsets.py` with reference set details
2. Run `pip install -r requirements.txt`
3. Run `python src/refsets.py` 
4. Reference sets will be updated in QRadar