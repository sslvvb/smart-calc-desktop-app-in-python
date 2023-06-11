#include "model.h"

namespace s21 {

double Model::GetResult(const char* str) {
  nodes_ = parser_.ParseNodes(str);
  ConvertToRPN();
  double result = Calculate(&nodes_in_rpn_);
  return result;
}

double Model::GetResult(const char* str, double x_value) {
  nodes_ = parser_.ParseNodes(str);
  ConvertToRPN();
  XToNumberReplace(&nodes_in_rpn_, x_value);
  double result = Calculate(&nodes_in_rpn_);
  return result;
}

std::pair<std::vector<double>, std::vector<double>> Model::GetResultForGraph(
    const char* str, double x_min, double x_max) {
  nodes_ = parser_.ParseNodes(str);
  ConvertToRPN();
  std::vector<double> scope_x;
  std::vector<double> scope_y;
  double step = (x_max - x_min) / 1e5;
  for (double x = x_min; x <= (x_max + step); x += step) {
    list tmp = nodes_in_rpn_;
    XToNumberReplace(&tmp, x);
    scope_x.push_back(x);
    scope_y.push_back(Calculate(&tmp));
  }
  return std::make_pair(scope_x, scope_y);
}

void Model::XToNumberReplace(list* list_nodes, double x_value) {
  for (auto it = list_nodes->begin(); it != list_nodes->end(); ++it) {
    auto tmp = *it;
    if (tmp.second == kSymbolX) {
      pair node(x_value, kNumber);
      list_nodes->insert(it, node);
      it = list_nodes->erase(it);
      --it;
    }
  }
}

std::list<std::pair<double, Type>> Model::Parser::ParseNodes(const char* str) {
  while (*str) {
    GetType(&str);
  }
  Type last_type = GetPrevType();
  if ((last_type >= kBasicPlus && last_type <= kOpenBrckt) || brckt_flag_) {
    throw std::invalid_argument("ERROR");
  }
  list result_list = parser_nodes_;
  parser_nodes_.clear();
  return result_list;
}

void Model::Parser::GetType(const char** token) {
  if (**token >= 48 && **token <= 57) {
    NumberProcess(token);
  } else if (**token == '.') {
    throw std::out_of_range("ERROR");
  } else if (**token == 'e') {
    throw std::out_of_range("ERROR");
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
  }
}

void Model::Parser::NumberProcess(const char** token) {
  Type prev_type = GetPrevType();
  if (prev_type == kNumber || prev_type == kSymbolX ||
      prev_type == kCloseBrckt) {
    throw std::invalid_argument("ERROR");
  }
  char* ptr_end = nullptr;
  double number = strtod(*token, &ptr_end);
  pair node(number, kNumber);
  parser_nodes_.push_back(node);
  *token = ptr_end;
}

void Model::Parser::XProcess(const char** token) {
  Type prev_type = GetPrevType();
  if (prev_type == kNumber || prev_type == kSymbolX ||
      prev_type == kCloseBrckt) {
    throw std::invalid_argument("ERROR");
  }
  pair node{};
  node.second = kSymbolX;
  parser_nodes_.push_back(node);
  *token += 1;
}

void Model::Parser::PlusAndMinusProcess(const char** token) {
  Type prev_type = GetPrevType();
  pair node{};
  if (prev_type >= kBasicPlus && prev_type <= kDiv) {
    throw std::invalid_argument("ERROR");
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

void Model::Parser::OperatorProcess(const char** token) {
  Type prev_type = GetPrevType();
  pair node{};
  if (prev_type == kZeroType ||
      (prev_type >= kBasicPlus && prev_type <= kOpenBrckt)) {
    throw std::invalid_argument("ERROR");
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

void Model::Parser::OpenBrcktProcess(const char** token) {
  Type prev_type = GetPrevType();
  if (prev_type == kNumber || prev_type == kSymbolX ||
      prev_type == kCloseBrckt) {
    throw std::invalid_argument("ERROR");
  }
  pair node{};
  node.second = kOpenBrckt;
  parser_nodes_.push_back(node);
  brckt_flag_ += 1;
  *token += 1;
}

void Model::Parser::CloseBrcktProcess(const char** token) {
  Type prev_type = GetPrevType();
  if (!brckt_flag_ || prev_type == kZeroType ||
      (prev_type >= kBasicPlus && prev_type <= kPower)) {
    throw std::invalid_argument("ERROR");
  }
  pair node{};
  node.second = kCloseBrckt;
  parser_nodes_.push_back(node);
  brckt_flag_ -= 1;
  *token += 1;
}

void Model::Parser::ModProcess(const char** token) {
  Type prev_type = GetPrevType();
  if (prev_type == kZeroType ||
      (prev_type >= kBasicPlus && prev_type <= kOpenBrckt)) {
    throw std::invalid_argument("ERROR");
  }
  pair node{};
  node.second = kMod;
  parser_nodes_.push_back(node);
  node.second = kOpenBrckt;
  parser_nodes_.push_back(node);
  *token += 4;
  brckt_flag_ += 1;
}

void Model::Parser::LnLogProcess(const char** token) {
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

void Model::Parser::SqrtSinProcess(const char** token) {
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

void Model::Parser::AProcess(const char** token) {
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

void Model::Parser::CosTanProcess(const char** token) {
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

Type Model::Parser::GetPrevType() {
  Type result = kZeroType;
  if (parser_nodes_.size()) {
    result = parser_nodes_.back().second;
  }
  return result;
}

void Model::Parser::CheckFooValid() {
  Type prev_type = GetPrevType();
  if (prev_type == kNumber || prev_type == kSymbolX ||
      prev_type == kCloseBrckt) {
    throw std::invalid_argument("ERROR");
  }
}

void Model::ConvertToRPN() {
  stack tmp{};
  size_t list_size = nodes_.size();
  for (size_t i = 0; i != list_size; ++i) {
    pair node = nodes_.front();
    if (node.second == kNumber || node.second == kSymbolX) {
      nodes_in_rpn_.push_back(node);
    } else if ((node.second >= kBasicPlus && node.second <= kPower) ||
               node.second == kMod) {
      OperatorConvert(&tmp, node);
    } else if (node.second == kOpenBrckt) {
      tmp.push(node);
    } else if (node.second == kCloseBrckt) {
      while (tmp.top().second != kOpenBrckt) {
        nodes_in_rpn_.push_back(tmp.top());
        tmp.pop();
      }
      tmp.pop();
    } else {
      tmp.push(node);
    }
    nodes_.pop_front();
  }
  while (tmp.size()) {
    nodes_in_rpn_.push_back(tmp.top());
    tmp.pop();
  }
}

void Model::OperatorConvert(stack* tmp, pair node) {
  if (tmp->size()) {
    int sort_flag = 0;
    while (!sort_flag) {
      int tmp_priority = GetProirity(tmp->top().second);
      int input_proirity = GetProirity(nodes_.front().second);
      if (tmp_priority > input_proirity ||
          (tmp_priority == input_proirity && input_proirity != 3)) {
        nodes_in_rpn_.push_back(tmp->top());
        tmp->pop();
      } else {
        sort_flag = 1;
      }
      if (!tmp->size()) {
        sort_flag = 1;
      }
    }
  }
  tmp->push(node);
}

int Model::GetProirity(Type type) {
  int result{};
  if (type == kOpenBrckt || type == kCloseBrckt) {
    result = -1;
  } else if (type == kNumber || type == kSymbolX) {
    result = 0;
  } else if (type == kBasicPlus || type == kBasicMinus) {
    result = 1;
  } else if (type == kMul || type == kDiv || type == kMod) {
    result = 2;
  } else if (type == kPower) {
    result = 3;
  } else {
    result = 4;
  }
  return result;
}

double Model::Calculate(list* list_nodes_) {
  list tmp;
  while (list_nodes_->size()) {
    int act_flag = 0;
    Type type = list_nodes_->front().second;
    if (type == kNumber) {
      tmp.push_back(list_nodes_->front());
      list_nodes_->pop_front();
    } else if ((type >= kLn && type <= kAtan)) {
      pair node(FooCalculate(type, tmp.back().first), kNumber);
      list_nodes_->pop_front();
      tmp.pop_back();
      list_nodes_->push_front(node);
      act_flag = 1;
    } else {
      double num1 = tmp.back().first;
      tmp.pop_back();
      double num2 = tmp.back().first;
      tmp.pop_back();
      pair node(OperatorCalculate(type, num1, num2), kNumber);
      list_nodes_->pop_front();
      tmp.push_back(node);
      act_flag = 1;
    }
    if (act_flag) {
      while (tmp.size()) {
        list_nodes_->push_front(tmp.back());
        tmp.pop_back();
      }
    }
  }
  double result = tmp.back().first;
  return result;
}

double Model::OperatorCalculate(Type type, double num1, double num2) {
  double result{};
  if (type == kBasicPlus) {
    result = num2 + num1;
  } else if (type == kBasicMinus) {
    result = num2 - num1;
  } else if (type == kMul) {
    result = num2 * num1;
  } else if (type == kDiv) {
    result = num2 / num1;
  } else if (type == kPower) {
    result = pow(num2, num1);
  } else if (type == kMod) {
    result = ModCalculate(num2, num1);
  }
  return result;
}

double Model::ModCalculate(double num1, double num2) {
  double result{};
  if ((num1 < 0 && num2 < 0) || (num1 > 0 && num2 > 0)) {
    result = fmod(num1, num2);
  } else if (num1 > 0 && num2 < 0) {
    if (num1 <= fabs(num2)) {
      result = num2 + num1;
    } else {
      double tmp = num1 + num2;
      while (tmp > fabs(num2)) {
        tmp = tmp + num2;
      }
      result = num2 + tmp;
    }
  } else if (num1 < 0 && num2 > 0) {
    if (fabs(num1) <= num2) {
      result = num2 + num1;
    } else {
      double tmp = num1 + num2;
      while (fabs(tmp) > num2) {
        tmp = tmp + num2;
      }
      result = num2 + tmp;
    }
  }
  return result;
}

double Model::FooCalculate(Type type, double num) {
  double result{};
  if (type == kLn) {
    result = log(num);
  } else if (type == kLog) {
    result = log10(num);
  } else if (type == kSqrt) {
    result = sqrt(num);
  } else if (type == kSin) {
    result = sin(num);
  } else if (type == kAsin) {
    result = asin(num);
  } else if (type == kCos) {
    result = cos(num);
  } else if (type == kAcos) {
    result = acos(num);
  } else if (type == kTan) {
    result = tan(num);
  } else if (type == kAtan) {
    result = atan(num);
  }
  return result;
}

}  // namespace s21
