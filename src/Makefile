.PHONY: cpp_lib executable installation_file run_app clean test lint

all: run_app

cpp_lib:
	cd app/project/smartcalc/services && g++ -shared -o model.so cpp_dynamic_lib/model.cpp cpp_dynamic_lib/parser.cpp cpp_dynamic_lib/wrapper.cpp

executable:

installation_file:

run_app: cpp_lib executable

clean:

test:

pokritie_wtf:

lint:
