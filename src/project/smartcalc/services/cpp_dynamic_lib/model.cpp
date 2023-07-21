#include "model.h"

namespace s21 {

bool Model::GetResult(const char* str, double& result_buf) {
  try {
    nodes_ = parser_.ParseNodes(str);
    ConvertToRPN();
    result_buf = Calculate(&nodes_in_rpn_);
  } catch (const std::exception&) {
    return false;
  }
  return true;
}

bool Model::GetResult(const char* str, double x_value, double& result_buf) {
  try {
    nodes_ = parser_.ParseNodes(str);
    ConvertToRPN();
    XToNumberReplace(&nodes_in_rpn_, x_value);
    result_buf = Calculate(&nodes_in_rpn_);
  } catch (const std::exception&) {
    return false;
  }
  return true;
}

bool Model::GetResultForGraph(const char* str, double x_min, double x_max,
                              int number_of_steps,
                              std::vector<double>& x_results_buf,
                              std::vector<double>& y_results_buf) {
  try {
    x_results_buf.clear();
    y_results_buf.clear();
    nodes_ = parser_.ParseNodes(str);
    ConvertToRPN();
    double step = (x_max - x_min) / number_of_steps;
    for (double x = x_min; x <= (x_max + step); x += step) {
      list tmp = nodes_in_rpn_;
      XToNumberReplace(&tmp, x);
      x_results_buf.push_back(x);
      y_results_buf.push_back(Calculate(&tmp));
    }
  } catch (const std::exception&) {
    return false;
  }
  return true;
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
