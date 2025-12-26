#!/bin/bash
export PYTHONPATH=$PYTHONPATH:/app

# Generate config from template using Python/Jinja2 (simple substitution script)
cat <<EOF > /app/generate_config.py
import os
import sys
from jinja2 import Template

with open('/app/homeserver.yaml', 'r') as f:
    template = Template(f.read())

config = template.render(os.environ)

with open('/app/homeserver.generated.yaml', 'w') as f:
    f.write(config)
EOF

echo "Generating configuration..."
python3 /app/generate_config.py

# Copy Element config
if [ -d "/app/element-web" ]; then
    echo "Configuring Element Web..."
    cp /app/element-config.json /app/element-web/config.json
fi

echo "Starting Synapse..."
exec python3 -m synapse.app.homeserver --config-path /app/homeserver.generated.yaml
