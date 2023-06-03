CXX = g++
STD = -std=c++17
CFLAG = -Wall -Werror -Wextra
DEBUG_FLAG = -g3 #-fsanitize=address
GTEST_LIBS := -lgtest -lpthread #`pkg-config --libs gtest

all: compile run

install: compile
	@mkdir SmartCalc
	@cp smartCalc_v2 SmartCalc/smartCalc_v2
	@rm smartCalc_v2

uninstall:
	rm -rf SmartCalc

dvi:
	texi2dvi foo.texi

dist: install
	tar --create --file SmartCalc_v2.tar.gzip SmartCalc

tests: clean
	$(CXX) $(STD) $(CFLAG) $(DEBUG_FLAG) -o tests.out -I app/. tests.cpp app/model.cpp -lgcov $(GTEST_LIBS) --coverage
	@./tests.out

compile: clean build
	cd build ; qmake smartCalc_v2.pro; make
	cp ./build/smartCalc_v2.app/Contents/MacOS/smartCalc_v2 .

run:
	./smartCalc_v2

gcov_report: tests
	@lcov --directory . -t "smartcalc_tests" -o gcovreport.info -c  --no-external
	@lcov -q --remove gcovreport.info "`pwd`/tests/*" -o gcovreport.info --rc lcov_function_coverage=0
	@genhtml -o $@ gcovreport.info
	@echo opening report `pwd`/gcov_report/index.html
	@open ./gcov_report/index.html

build:
	mkdir build
	cp app/smartCalc_v2.pro ./build/
	cp app/main.cpp ./build/
	cp -R app/ ./build/

clean:
	@rm -rf build gcov_report SmartCalc
	@rm -f smartCalc_v2 a.out tests.out
	@rm -f *.gcda *.gcno
	@rm -f .clang-format
	@rm -f *.info *.gzip SmartCalc *.aux *.dvi *.log *.toc

style:
	cp ../materials/linters/.clang-format .
	cd app ; clang-format -n controller.* model.* main.cpp graph.h graph.cpp smartcalcview.cpp smartcalcview.h xprocessdialog.cpp xprocessdialog.h

valgrind:
	valgrind --tool=memcheck --leak-check=full --track-origins=yes ./tests.out

leaks:
	leaks -atExit -- ./tests.out 
