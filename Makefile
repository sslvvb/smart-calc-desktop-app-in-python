.PHONY: all install build rebuild-macos-intel rebuild-macos-arm run installer coverage lint clean

VENV_NAME = venv

REQUIREMENTS_FILE = requirements.txt

ARCH := $(shell uname -m)

CPP_LIBRARY = src/app/model/cpp_dynamic_lib/model.so

.PHONY: all install clean run

all: install

install: $(VENV_NAME)
	@echo "Installing dependencies..."
	@source $(VENV_NAME)/bin/activate; \
	pip install -r $(REQUIREMENTS_FILE)
	@echo "Building the C++ dynamic library..."
	@make build
	@echo "Running the app..."
	@make run

$(VENV_NAME):
	python3 -m venv $(VENV_NAME)

build:
	@echo "Building the C++ dynamic library..."
ifeq ($(ARCH),x86_64)
	@echo "Building for Intel architecture (x86_64)..."
	make rebuild-macos-intel
else ifeq ($(ARCH),arm64)
	@echo "Building for ARM architecture (arm64)..."
	make rebuild-macos-arm
else
	@echo "Unsupported architecture: $(ARCH)"
endif

rebuild-macos-intel:
	g++ -shared -o $(CPP_LIBRARY) src/app/model/cpp_dynamic_lib/source/model.cpp src/app/model/cpp_dynamic_lib/source/parser.cpp src/app/model/cpp_dynamic_lib/source/wrapper.cpp

rebuild-macos-arm:
	g++ -arch arm64 -shared -o $(CPP_LIBRARY) src/app/model/cpp_dynamic_lib/source/model.cpp src/app/model/cpp_dynamic_lib/source/parser.cpp src/app/model/cpp_dynamic_lib/source/wrapper.cpp

run:
	@echo "Running the app..."
	source $(VENV_NAME)/bin/activate; \
	python3 src/app/main.py


###############################################################
#                          INSTALLER                          #
###############################################################

installer:
	python3 setup.py py2app
	hdiutil create -format UDBZ -srcfolder dist/main.app SmartCalc.dmg

###############################################################
#                            TESTS                            #
###############################################################

coverage: build
	cd src/app/model; python3 -m coverage run --source=. -m unittest
	cd src/app/model; coverage html
	open src/app/model/htmlcov/index.html

lint:
	pylint --rcfile materials/pylintrc src/app/main.py src/app/view/*.py src/app/presenter/*.py src/app/model/*.py

###############################################################
#                            CLEAN                            #
###############################################################

clean:
	@echo "Cleaning up..."
	rm -rf $(VENV_NAME) $(CPP_LIBRARY) .eggs build dist src/app/model/htmlcov src/app/model/.coverage SmartCalc.dmg
