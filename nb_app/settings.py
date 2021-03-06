import os
# WARNING:
# We do our best effort to keep sensible information private
# but in the scenario of an intrusion into the network or machines
# where agents or servers that represents a risk for the information
# stored in that machines.

# Main settings
PROJECTID = "voF17Gg7"
PROJECT_NAME = "nbwf-demo2"

WORKFLOW_SERVICE = os.getenv("NB_WORKFLOW_SERVICE", "http://localhost:8000")

# Theese information is used to run workloads in the workers.
# Don't modify at least you know what you are doing.
# Log
LOGLEVEL = "INFO"
detailed_format = "[%(asctime)s] - %(name)s - %(levelname)s - %(message)s"
LOGFORMAT = detailed_format