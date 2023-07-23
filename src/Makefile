ifeq ($(OS),Windows_NT)
    ARCH := $(PROCESSOR_ARCHITECTURE)
else
    UNAME := $(shell uname)
    ARCH := $(shell arch)
endif

# Set default target
# .DEFAULT_GOAL := run_app

# Directories
MODEL_DIR := app/project/smartcalc/services
PROJECT_DIR := app/project

# Platform-specific targets
# ifeq ($(UNAME), Linux)
#     REBUILD_TARGET := rebuild-linux
# endif
ifeq ($(UNAME), Darwin)
    ifeq ($(ARCH), x86_64)
        REBUILD_TARGET := rebuild-macos-intel
    endif
    ifeq ($(ARCH), arm64)
        REBUILD_TARGET := rebuild-macos-arm
    endif
endif
# ifeq ($(OS),Windows_NT)
#     ifeq ($(ARCH), AMD64)
#         REBUILD_TARGET := rebuild-windows-64
#     endif
#     ifeq ($(ARCH), x86)
#         REBUILD_TARGET := rebuild-windows-32
#     endif
# endif

# all: run_app

cpp_lib:
	cd $(MODEL_DIR) && make $(REBUILD_TARGET)

executable:
	cd $(PROJECT_DIR) && pyinstaller smart_calc.spec
    # Add commands for creating the executable based on the platform

tmp: cpp_lib executable
	cd app && electron .


installation_file:
    # Add commands for creating the installation file based on the platform

run_app: cpp_lib executable installation_file
    # Add commands to run the application

clean:
	cd $(PROJECT_DIR) && rm -rf build dist
# Add commands to clean the build artifacts
# rm -f package-lock.json
# rm -rf dist

test:
    # Add commands for running tests

pokritie_wtf:

lint:
    # Add commands for linting the code

.PHONY: cpp_lib executable installation_file run_app clean test lint

exe:
	pyinstaller smart_calc.spec
	./dist/smart_calc/smart_calc runserver localhost:8000 --noreload
