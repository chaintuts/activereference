# This file contains a make script for the ActiveReference application
#
# Author: Josh McIntyre
#

# This block defines makefile variables
SRC_FILES=src/core/*.py
TEMPLATE_FILES=src/templates/*.html
RES_FILES=res/*.json

BUILD_DIR=bin/activereference
TEMPLATE_DIR=templates
RES_DIR=res

# This rule builds the application
build: $(SRC_FILES) $(DATA_FILES)
	mkdir -p $(BUILD_DIR)
	mkdir -p $(BUILD_DIR)/$(TEMPLATE_DIR)
	mkdir -p $(BUILD_DIR)/$(RES_DIR)
	cp $(SRC_FILES) $(BUILD_DIR)
	cp $(TEMPLATE_FILES) $(BUILD_DIR)/$(TEMPLATE_DIR)
	cp $(RES_FILES) $(BUILD_DIR)/$(RES_DIR)

# This rule cleans the build directory
clean: $(BUILD_DIR)
	rm -r $(BUILD_DIR)/*
	rmdir $(BUILD_DIR)
