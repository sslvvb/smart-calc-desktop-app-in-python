#ifndef SMARTCALC_MODEL_H_
#define SMARTCALC_MODEL_H_

#include <clocale>
#include <cmath>
#include <stack>
#include <vector>

#include "parser.h"

namespace s21 {

class Model {
 public:
  using stack = std::stack<std::pair<double, Type>>;
  using list = std::list<std::pair<double, Type>>;
  using pair = std::pair<double, Type>;

  Model() { setlocale(LC_ALL, "C"); };
  Model(const Model& other) = default;
  Model(Model&& other) = delete;
  Model& operator=(const Model& other) = default;
  Model& operator=(Model&& other) = delete;
  ~Model() = default;

  bool GetResult(const char* str, double& result_buf);
  bool GetResult(const char* str, double x_value, double& result_buf);
  bool GetResultForGraph(const char* str, double x_min, double x_max,
                         int number_of_steps,
                         std::vector<double>& x_results_buf,
                         std::vector<double>& y_results_buf);

 private:
  Parser parser_;
  list nodes_;
  list nodes_in_rpn_;

  void ConvertToRPN();
  void OperatorConvert(stack* tmp, pair node);
  int GetProirity(Type type);

  void XToNumberReplace(list* list_nodes_, double x_value);

  double Calculate(list* list_nodes_);
  double FooCalculate(Type type, double num);
  double OperatorCalculate(Type type, double num1, double num2);
  double ModCalculate(double num1, double num2);
};

}  // namespace s21

#endif  // SMARTCALC_MODEL_H_
