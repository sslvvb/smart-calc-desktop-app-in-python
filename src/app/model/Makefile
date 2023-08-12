.PHONY: compile_arm64 rebuild clean

rebuild-macos-intel:
	g++ -shared -o model.so cpp_dynamic_lib/model.cpp cpp_dynamic_lib/parser.cpp cpp_dynamic_lib/wrapper.cpp

rebuild-macos-arm:
	g++-12 -arch arm64 -shared -o cpp_dynamic_lib/model.so cpp_dynamic_lib/model.cpp cpp_dynamic_lib/parser.cpp cpp_dynamic_lib/wrapper.cpp

clean:
	rm -f model.so
