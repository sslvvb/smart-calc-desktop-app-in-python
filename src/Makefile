.PHONY: all installer test lint clean_all

UNAME := $(shell uname)
ARCH := $(shell arch)

ifeq ($(UNAME), Darwin)
    ifeq ($(ARCH), x86_64)
        REBUILD_TARGET := rebuild-macos-intel
    endif
    ifeq ($(ARCH), arm64)
        REBUILD_TARGET := rebuild-macos-arm
    endif
endif

###############################################################
#                            MAIN                             #
###############################################################

all: run_app

env:
	python3 -m venv env_sslvvb
	source env_sslvvb/bin/activate
	pip3 install --upgrade pip
	pip3 install -r requirements.txt

run_app: build_cpp
	python3 app/main.py

installer:
	python3 setup.py py2app
	hdiutil create -format UDBZ -srcfolder dist/main.app SmartCalc.dmg

###############################################################
#                            BUILD                            #
###############################################################

build_cpp:
	make $(REBUILD_TARGET)

rebuild-macos-intel:
	g++ -shared -o app/model/cpp_dynamic_lib/model.so app/model/cpp_dynamic_lib/source/model.cpp app/model/cpp_dynamic_lib/source/parser.cpp app/model/cpp_dynamic_lib/source/wrapper.cpp

rebuild-macos-arm:
	g++-12 -arch arm64 -shared -o app/model/cpp_dynamic_lib/model.so app/model/cpp_dynamic_lib/source/model.cpp app/model/cpp_dynamic_lib/source/parser.cpp app/model/cpp_dynamic_lib/source/wrapper.cpp

###############################################################
#                            TESTS                            #
###############################################################

coverage: build_cpp
	cd app/model; python3 -m coverage run --source=. -m unittest
	cd app/model; coverage html
	open app/model/htmlcov/index.html

lint:
	pylint --rcfile pylintrc app/main.py app/view/*.py app/presenter/*.py app/model/*.py

###############################################################
#                            CLEAN                            #
###############################################################

clean:
	rm -rf build dist app/model/htmlcov
	rm -f SmartCalc.dmg app/model/.coverage

clean_all: clean
	rm -rf env_sslvvb
	rm -f app/model/cpp_dynamic_lib/model.so
	# deactivate
