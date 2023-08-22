#include "parser.h"

namespace s21 {

std::list<std::pair<double, Type>> Parser::ParseNodes(const char* str) {
  while (*str) {
    GetType(&str);
  }
  Type last_type = GetPrevType();
  if ((last_type >= kBasicPlus && last_type <= kOpenBrckt) || brckt_flag_) {
    throw std::invalid_argument("Error in expression");
  }
  list result_list = parser_nodes_;
  parser_nodes_.clear();
  return result_list;
}

void Parser::GetType(const char** token) {
  if (**token >= 48 && **token <= 57) {
    NumberProcess(token);
  } else if (**token == '.') {
    throw std::out_of_range("Error in expression");
  } else if (**token == 'e') {
    throw std::out_of_range("Error in expression");
  } else if (**token == 'x') {
    XProcess(token);
  } else if (**token == '-' || **token == '+') {
    PlusAndMinusProcess(token);
  } else if (**token == '*' || **token == '/' || **token == '^') {
    OperatorProcess(token);
  } else if (**token == '(') {
    OpenBrcktProcess(token);
  } else if (**token == ')') {
    CloseBrcktProcess(token);
  } else if (**token == 'm') {
    ModProcess(token);
  } else if (**token == 'l') {
    LnLogProcess(token);
  } else if (**token == 's') {
    SqrtSinProcess(token);
  } else if (**token == 'a') {
    AProcess(token);
  } else if (**token == 'c' || **token == 't') {
    CosTanProcess(token);
  } else {
    throw std::out_of_range("Error in expression");
  }
}

void Parser::NumberProcess(const char** token) {
  Type prev_type = GetPrevType();
  if (prev_type == kNumber || prev_type == kSymbolX ||
      prev_type == kCloseBrckt) {
    throw std::invalid_argument("Error in expression");
  }
  char* ptr_end = nullptr;
  double number = strtod(*token, &ptr_end);
  pair node(number, kNumber);
  parser_nodes_.push_back(node);
  *token = ptr_end;
}

void Parser::XProcess(const char** token) {
  Type prev_type = GetPrevType();
  if (prev_type == kNumber || prev_type == kSymbolX ||
      prev_type == kCloseBrckt) {
    throw std::invalid_argument("Error in expression");
  }
  pair node{};
  node.second = kSymbolX;
  parser_nodes_.push_back(node);
  *token += 1;
}

void Parser::PlusAndMinusProcess(const char** token) {
  Type prev_type = GetPrevType();
  pair node{};
  if (prev_type >= kBasicPlus && prev_type <= kDiv) {
    throw std::invalid_argument("Error in expression");
  } else if (prev_type == kZeroType || prev_type == kPower ||
             prev_type == kOpenBrckt) {
    node.second = kNumber;
    parser_nodes_.push_back(node);
  }
  if (**token == '+') {
    node.second = kBasicPlus;
  } else {
    node.second = kBasicMinus;
  }
  parser_nodes_.push_back(node);
  *token += 1;
}

void Parser::OperatorProcess(const char** token) {
  Type prev_type = GetPrevType();
  pair node{};
  if (prev_type == kZeroType ||
      (prev_type >= kBasicPlus && prev_type <= kOpenBrckt)) {
    throw std::invalid_argument("Error in expression");
  }
  if (**token == '*') {
    node.second = kMul;
  } else if (**token == '/') {
    node.second = kDiv;
  } else {
    node.second = kPower;
  }
  parser_nodes_.push_back(node);
  *token += 1;
}

void Parser::OpenBrcktProcess(const char** token) {
  Type prev_type = GetPrevType();
  if (prev_type == kNumber || prev_type == kSymbolX ||
      prev_type == kCloseBrckt) {
    throw std::invalid_argument("Error in expression");
  }
  pair node{};
  node.second = kOpenBrckt;
  parser_nodes_.push_back(node);
  brckt_flag_ += 1;
  *token += 1;
}

void Parser::CloseBrcktProcess(const char** token) {
  Type prev_type = GetPrevType();
  if (!brckt_flag_ || prev_type == kZeroType ||
      (prev_type >= kBasicPlus && prev_type <= kPower)) {
    throw std::invalid_argument("Error in expression");
  }
  pair node{};
  node.second = kCloseBrckt;
  parser_nodes_.push_back(node);
  brckt_flag_ -= 1;
  *token += 1;
}

void Parser::ModProcess(const char** token) {
  Type prev_type = GetPrevType();
  if (prev_type == kZeroType ||
      (prev_type >= kBasicPlus && prev_type <= kOpenBrckt)) {
    throw std::invalid_argument("Error in expression");
  }
  pair node{};
  node.second = kMod;
  parser_nodes_.push_back(node);
  node.second = kOpenBrckt;
  parser_nodes_.push_back(node);
  *token += 4;
  brckt_flag_ += 1;
}

void Parser::LnLogProcess(const char** token) {
  CheckFooValid();
  *token += 1;
  pair node{};
  if (**token == 'n') {
    node.second = kLn;
    parser_nodes_.push_back(node);
    *token += 2;
  } else {
    node.second = kLog;
    parser_nodes_.push_back(node);
    *token += 3;
  }
  node.second = kOpenBrckt;
  parser_nodes_.push_back(node);
  brckt_flag_ += 1;
}

void Parser::SqrtSinProcess(const char** token) {
  CheckFooValid();
  *token += 1;
  pair node{};
  if (**token == 'q') {
    node.second = kSqrt;
    parser_nodes_.push_back(node);
    *token += 4;
  } else {
    node.second = kSin;
    parser_nodes_.push_back(node);
    *token += 3;
  }
  node.second = kOpenBrckt;
  parser_nodes_.push_back(node);
  brckt_flag_ += 1;
}

void Parser::AProcess(const char** token) {
  CheckFooValid();
  *token += 1;
  pair node{};
  if (**token == 's') {
    node.second = kAsin;
    parser_nodes_.push_back(node);
  } else if (**token == 'c') {
    node.second = kAcos;
    parser_nodes_.push_back(node);
  } else {
    node.second = kAtan;
    parser_nodes_.push_back(node);
  }
  node.second = kOpenBrckt;
  parser_nodes_.push_back(node);
  *token += 4;
  brckt_flag_ += 1;
}

void Parser::CosTanProcess(const char** token) {
  CheckFooValid();
  pair node{};
  if (**token == 'c') {
    node.second = kCos;
    parser_nodes_.push_back(node);
  } else {
    node.second = kTan;
    parser_nodes_.push_back(node);
  }
  node.second = kOpenBrckt;
  parser_nodes_.push_back(node);
  *token += 4;
  brckt_flag_ += 1;
}

Type Parser::GetPrevType() {
  Type result = kZeroType;
  if (parser_nodes_.size()) {
    result = parser_nodes_.back().second;
  }
  return result;
}

void Parser::CheckFooValid() {
  Type prev_type = GetPrevType();
  if (prev_type == kNumber || prev_type == kSymbolX ||
      prev_type == kCloseBrckt) {
    throw std::invalid_argument("Error in expression");
  }
}

}  // namespace s21
