.PHONY: build clean create_executable

env:
	python3 -m venv env_name
	source env_name/bin/activate
	pip3 install -r requirements.txt

tmp:
	npm install
	npm install --save-dev electron-builder
	npx electron-builder build --mac

build:
	npx electron-builder build --mac

open:
	cd /opt/goinfre/hjerilyn/projects/python_calc_3/git_rep_python_calc/electron_test/dist/mac/electron_test.app/Contents/MacOS/ ; ./electron_test

clean:
	rm -rf dist/ build/ app_exe
	rm -f model.spec reverse_text.spec

rebuild: clean build open

create_executable:
	pyinstaller --distpath ./build/app_exe -F app/model/reverse_text.py

kill_port:
	npx kill-port 5000
