# apmgr-scripts
Some quick scripts to add or amend APs from FortiManager AP Manager

WARNING: Never use device manager or device manager CLI scripts to manipulate APs in FortiManager, only ever use AP Manager

These scripts utilise the same API calls as the AP Manager Web UI

### DEPENDENCIES
Most python environments will only require 'pip install python-dotenv' in addition to defaults

import requests
import json
import time
import os 
import json
from dotenv import load_dotenv


### ADDING APs
- Define environmental variables (URL, api username, api password, FortiGate/WLC) in apscript.env
- Define APs in addaplist.json
- Run add-aps-to-fmg.py
- Install the change (this script does not perform device installation)

### EDIT APs
- Define environmental variables (URL, api username, api password, FortiGate/WLC) in apscript.env
- Define APs in editaplist.json
- From quick testing, most entries can be removed if not relevant / used (i.e. left on defaults or not being altered), full schema is provided as example
- Run edit-aps.py - note this applies an over-ride to the AP profile
- Install the change (this script does not perform device installation)

### ENVIRONMENT VARIABLES
FMGURL="https:/'your FMG'/jsonrpc" 
  
FMGUSERNAME='your FMG API user with JSON API permissions'
  
FMGPASSWORD='your FMG API user password'
  
FMGWLC='your FortiGate'
  
