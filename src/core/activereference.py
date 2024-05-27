# This file contains code for transforming JSON activity data into an HTML-formatted webpage
#
# Author: Josh McIntyre
#
import flask
import jinja2
import json

# App constants
APP_NAME = "activereference"
ROUTE_BODYWEIGHT_MOVEMENTS = "/bodyweight_movements"
ROUTE_FREEWEIGHT_MOVEMENTS = "/freeweight_movements"
ROUTE_PROGRAM_TEMPLATES = "/program_templates"
ROUTE_PREMADE_PROGRAMS = "/premade_programs"

RES_DIR="res/"
TEMPLATE_DIR="templates/"

DATA_BODYWEIGHT_MOVEMENTS = "bodyweight_movements.json"
TEMPLATE_BODYWEIGHT_MOVEMENTS = "bodyweight_movements_template.html"
DATA_FREEWEIGHT_MOVEMENTS = "freeweight_movements.json"
TEMPLATE_FREEWEIGHT_MOVEMENTS = "freeweight_movements_template.html"
DATA_PROGRAM_TEMPLATES = "program_templates.json"
TEMPLATE_PROGRAM_TEMPLATES = "program_templates_template.html"
DATA_PREMADE_PROGRAMS = "premade_programs.json"
TEMPLATE_PREMADE_PROGRAMS = "premade_programs_template.html"

# Create the main application
app = flask.Flask(APP_NAME)

def render_data(datafile, template):

    # Init
    environment = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))

    # Generate
    template = environment.get_template(template)
    
    with open(f"{RES_DIR}{datafile}") as f:
        data = json.load(f)

    template_html = ""
    for item in data:
        template_html += template.render(item)
 
    return template_html
        
# Define application routes
@app.route(ROUTE_BODYWEIGHT_MOVEMENTS)
def bodyweight_movements():
    return render_data(DATA_BODYWEIGHT_MOVEMENTS, TEMPLATE_BODYWEIGHT_MOVEMENTS)
    
@app.route(ROUTE_FREEWEIGHT_MOVEMENTS)
def freeweight_movements():
    return render_data(DATA_FREEWEIGHT_MOVEMENTS, TEMPLATE_FREEWEIGHT_MOVEMENTS)

@app.route(ROUTE_PROGRAM_TEMPLATES)
def program_templates():
    return render_data(DATA_PROGRAM_TEMPLATES, TEMPLATE_PROGRAM_TEMPLATES)

@app.route(ROUTE_PREMADE_PROGRAMS)
def premade_programs():
    return render_data(DATA_PREMADE_PROGRAMS, TEMPLATE_PREMADE_PROGRAMS)
