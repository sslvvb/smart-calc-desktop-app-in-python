#ifndef SMARTCALC_APP_MODEL_H_
#define SMARTCALC_APP_MODEL_H_

#include <clocale>
#include <cmath>
#include <list>
#include <stack>
#include <stdexcept>
#include <vector>

// из этого собираю динамическую библиотеку с тремя публичными функциями наружу
// подключить ее к питону
// фронт разделить на кнопки и собирать оттуда строку и х если он есть, подумать как это сделать красиво

namespace s21 {

enum Type {
  kZeroType,
  kNumber,
  kSymbolX,

  kBasicPlus,
  kBasicMinus,
  kMul,
  kDiv,
  kPower,

  kOpenBrckt,
  kCloseBrckt,

  kMod,
  kLn,
  kLog,
  kSqrt,
  kSin,
  kAsin,
  kCos,
  kAcos,
  kTan,
  kAtan,
};

class Model {
 public:
  using list = std::list<std::pair<double, Type>>;
  using stack = std::stack<std::pair<double, Type>>;
  using pair = std::pair<double, Type>;
  using vector = std::vector<double>;

  Model() { setlocale(LC_ALL, "C"); };
  Model(const Model& other) = default;
  Model(Model&& other) = delete;
  Model& operator=(const Model& other) = default;
  Model& operator=(Model&& other) = delete;
  ~Model() = default;

  double GetResult(const char* str);
  double GetResult(const char* str, double x_value);
  std::pair<std::vector<double>, std::vector<double>> GetResultForGraph(
      const char* str, double x_min, double x_max);

 private:
  class Parser { // композиция-наследование почему вообще это внутри ???
   public:
    list ParseNodes(const char* str);

   private:
    list parser_nodes_;
    int brckt_flag_{};

    void GetType(const char** str);
    Type GetPrevType();
    void NumberProcess(const char** token);
    void XProcess(const char** token);
    void PlusAndMinusProcess(const char** token);
    void OperatorProcess(const char** token);
    void OpenBrcktProcess(const char** token);
    void CloseBrcktProcess(const char** token);
    void ModProcess(const char** token);
    void LnLogProcess(const char** token);
    void SqrtSinProcess(const char** token);
    void AProcess(const char** token);
    void CosTanProcess(const char** token);
    void CheckFooValid();
  };

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

#endif  // SMARTCALC_APP_MODEL_H_
