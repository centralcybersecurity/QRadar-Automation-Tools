# QRadar DSM Parser

This script parses QRadar DSM configuration files (.dsm) to validate syntax.

DSM stands for "Data Source Module" in QRadar.

QRadar uses DSMs to integrate with external data sources and normalize events into a common schema.

Each DSM consists of a configuration file with a .dsm extension that defines:

- Name and description
- Log source type
- Supported event types
- Mappings to normalize and categorize events
- When a DSM is installed, QRadar can receive and parse logs from that data source based on the configuration.

## Usage

1. Place .dsm files in the `dsms/` directory
2. Run `pip install -r requirements.txt`
3. Run `python src/parser.py`
4. Output will indicate valid or invalid DSM configs