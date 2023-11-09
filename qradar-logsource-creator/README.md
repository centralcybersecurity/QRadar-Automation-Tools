# QRadar Log Source Creator

This script creates QRadar log sources from templates.

 QRadar log sources are used to ingest and analyze log data from different IT assets and systems in an organization. 

Some common uses and types of QRadar log sources include:

- Network devices - Routers, switches, firewalls etc. Logs from these devices provide visibility into network activity.

- Operating systems - Windows, Linux, UNIX etc. OS logs record events happening across servers and endpoints. 

- Applications - Databases, web servers, ERP systems. Application logs provide insight into app performance and usage.

- Security devices - IDS/IPS, proxies, antivirus. These logs are critical for security monitoring and threat detection.

- Cloud/SaaS - AWS CloudTrail, O365 audit logs. Cloud service logs extend visibility beyond on-prem infrastructure.

- Custom logs - Log files from custom applications or formats can be ingested via syslog or log file protocols. 


## Usage

1. Update templates in `src/templates.py`
2. Run `pip install -r requirements.txt` 
3. Run `python src/logsources.py`
4. Generated log sources will be in `logsources/` directory