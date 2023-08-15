.PHONY: clean, app

clean:
	rm -rf build dist



# ifeq ($(OS),Windows_NT)
#     ARCH := $(PROCESSOR_ARCHITECTURE)
# else
#     UNAME := $(shell uname)
#     ARCH := $(shell arch)
# endif
#
# # Directories
# MODEL_DIR := app/model
# PROJECT_DIR := app/project
# APP_DIR := app
#
# # Platform-specific targets
# # ifeq ($(UNAME), Linux)
# #     REBUILD_TARGET := rebuild-linux
# # endif
# ifeq ($(UNAME), Darwin)
#     ifeq ($(ARCH), x86_64)
#         REBUILD_TARGET := rebuild-macos-intel
#     endif
#     ifeq ($(ARCH), arm64)
#         REBUILD_TARGET := rebuild-macos-arm
#     endif
# endif
# # ifeq ($(OS),Windows_NT)
# #     ifeq ($(ARCH), AMD64)
# #         REBUILD_TARGET := rebuild-windows-64
# #     endif
# #     ifeq ($(ARCH), x86)
# #         REBUILD_TARGET := rebuild-windows-32
# #     endif
# # endif
#
# all: build run_app
#
# make_env:
# # add
#
# cpp_lib:
# 	cd $(MODEL_DIR) && make $(REBUILD_TARGET)
#
# python_executable:
# 	cd $(PROJECT_DIR) && pyinstaller smart_calc.spec
#
# build: cpp_lib python_executable
#
# run_app:
# 	cd $(APP_DIR) && npm run start
#
# installer:
# 	cd $(APP_DIR) && npm run digital
#
# clean:
# 	cd $(PROJECT_DIR) && rm -rf build dist
# 	cd $(APP_DIR) && rm -rf dist
#
# all_clean:
# # rm -f package-lock.json
# # rm -rf node_modules
#
# test:
# 	PYTHONPATH=.:$$PYTHONPATH pytest tests/
# # Add commands for running tests
#
# pokritie_wtf:
# # add
#
# lint:
# # Add commands for linting the code
# # cpp & python
#
# .PHONY: cpp_lib executable installation_file run_app clean test lint
#
#
#
#
#
# tmp:
# 	pkgbuild --identifier com.sample.pkg.app --root /Users/sslvvb/Documents/S21/Projects/Python/python_calc_3/my_git_rep_python_calc/src/app/project/dist/gui Sample.pkg
#
#
#
#
setup:
	py2applet --make-setup app/main.py

app:
	python3 setup.py py2app -A
# 	hdiutil create -volname "YourAppName" -srcfolder dist/main.app/ -ov -format UDZO YourAppName.dmg
