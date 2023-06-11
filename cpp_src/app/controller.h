#ifndef SMARTCALC_APP_CONTROLLER_H_
#define SMARTCALC_APP_CONTROLLER_H_

#include <QVector>

#include "model.h"

namespace s21 {

class Controller {
 public:
  Controller() = default;
  Controller(const Controller& other) = default;
  Controller(Controller&& other) = delete;
  Controller& operator=(const Controller& other) = default;
  Controller& operator=(Controller&& other) = delete;
  ~Controller() = default;

  double GetResult(const char* str);
  double GetResult(const char* str, double x_value);
  std::pair<QVector<double>, QVector<double>> GetResultForGraph(const char* str,
                                                                double x_min,
                                                                double x_max);

 private:
  Model model_;
};

}  // namespace s21

#endif  // SMARTCALC_APP_CONTROLLER_H_
