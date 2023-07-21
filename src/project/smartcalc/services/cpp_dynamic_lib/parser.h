#ifndef SMARTCALC_PARSER_H_
#define SMARTCALC_PARSER_H_

#include <list>
#include <stdexcept>

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

class Parser {
 public:
  using list = std::list<std::pair<double, Type>>;
  using pair = std::pair<double, Type>;

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

}  // namespace s21

#endif  // SMARTCALC_PARSER_H_
