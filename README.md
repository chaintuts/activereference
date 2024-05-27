## General
____________

### Author
* Josh McIntyre

### Website
* jmcintyre.net

### Overview
* ActiveReference is a web application for transforming and viewing training data

## Development
________________

### Git Workflow
* master for releases (merge development)
* development for bugfixes and new features

### Building
* make build
Build the application
* make load
Load the database
* make clean
Clean the build and data directories

### Features
* Takes compact JSON data and formats as HTML for easy viewing using Jinja templating

### Requirements
* Requires Python

### Platforms
* Windows
* Linux
* MacOSX

## Usage
____________

### Browser Usage
* Run the application using the built-in Flask server or another server configuration
* Navigate to collections via URL

### Available data
* `/bodyweight_movements` for bodyweight training progressions
* `/freeweight_movements` for barbell/dumbell free weight training variations
* `/program_templates` for customizable training program template information
* `/premade_programs` for pre-made training programs

