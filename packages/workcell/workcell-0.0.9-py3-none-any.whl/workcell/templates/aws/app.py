import os
import json
from workcell.core import Workcell
from workcell.api import create_api
from mangum import Mangum


# get stage & workcell_fqdn from environment
# stage = os.environ.get('STAGE', None)
# workcell_fqdn = os.environ.get('WORKCELL_FQDN', None)

# get stage & workcell_fqdn from workcell_config.json
workcell_config = json.load(open("workcell_config.json"))
stage = workcell_config.get("workcell_version", None)
workcell_fqdn = workcell_config.get("workcell_fqdn", None)
openapi_prefix = f"/{stage}" if stage else "/"

# generate workcell from workcell_fqdn
app = create_api(Workcell(workcell_fqdn)) # Here is the magic
app.root_path = openapi_prefix

# create lambda handler
handler = Mangum(app)
