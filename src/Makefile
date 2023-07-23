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
    # Add commands for creating the executable based on the platform
    # Replace this comment with actual commands

installation_file:
    # Add commands for creating the installation file based on the platform
    # Replace this comment with actual commands

run_app: cpp_lib executable installation_file
    # Add commands to run the application
    # Replace this comment with actual commands

clean:
    # Add commands to clean the build artifacts
    # Replace this comment with actual commands
# rm -f package-lock.json
# rm -rf dist
# rm -rf duild dist
# rm -f manage.spec

test:
    # Add commands for running tests
    # Replace this comment with actual commands

pokritie_wtf:

lint:
    # Add commands for linting the code
    # Replace this comment with actual commands

.PHONY: cpp_lib executable installation_file run_app clean test lint

exe:
	pyinstaller smart_calc.spec
	./dist/smart_calc/smart_calc runserver localhost:8000 --noreload
