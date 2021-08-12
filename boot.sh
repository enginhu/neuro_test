#!/bin/bash
source venv/bin/activate
exec gunicorn -b :3000 --access-logfile - --error-logfile - neuro_app:app