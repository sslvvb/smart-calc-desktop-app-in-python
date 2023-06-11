#include "controller.h"

namespace s21 {

double Controller::GetResult(const char* str) { return model_.GetResult(str); }

double Controller::GetResult(const char* str, double x_value) {
  return model_.GetResult(str, x_value);
}

std::pair<QVector<double>, QVector<double>> Controller::GetResultForGraph(
    const char* str, double x_min, double x_max) {
  auto pair = model_.GetResultForGraph(str, x_min, x_max);
  QVector<double> x_qvector(pair.first.begin(), pair.first.end());
  QVector<double> y_qvector(pair.second.begin(), pair.second.end());
  return std::make_pair(x_qvector, y_qvector);
}

}  // namespace s21
