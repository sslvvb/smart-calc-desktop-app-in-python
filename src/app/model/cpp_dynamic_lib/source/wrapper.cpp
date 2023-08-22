#include "model.h"

#ifdef __cplusplus
extern "C" {
#endif

bool GetResult(const char* expression, double& result) {
  s21::Model model;
  return model.GetResult(expression, result);
}

bool GetResultForGraph(const char* expression, double x_min, double x_max,
                       int number_of_steps, double* x_buf_values,
                       double* y_buf_values) {
  s21::Model model;
  std::vector<double> x_buf, y_buf;
  bool result = model.GetResultForGraph(expression, x_min, x_max,
                                        number_of_steps, x_buf, y_buf);
  if (!result) {
    return false;
  } else {
    for (size_t i = 0; i < number_of_steps; i++) {
      x_buf_values[i] = x_buf[i];
      y_buf_values[i] = y_buf[i];
    }
  }
  return true;
}

#ifdef __cplusplus
}
#endif
