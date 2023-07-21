.PHONY: compile_arm64 rebuild

rebuild:
    rm -f model.so && g++ -shared -o model.so cpp_dynamic_lib/model.cpp cpp_dynamic_lib/parser.cpp cpp_dynamic_lib/wrapper.cpp
#	python3 calculator.py

run:
	python3 calculator.py

compile_arm64:
    g++-12 -arch arm64 -shared -o model.so cpp_dynamic_lib/model.cpp cpp_dynamic_lib/parser.cpp cpp_dynamic_lib/wrapper.cpp

bind_lib:
    g++ -shared -o model.so -fPIC `python3 -m pybind11 --includes` cpp_dynamic_lib/model.cpp cpp_dynamic_lib/model_bind.cpp
