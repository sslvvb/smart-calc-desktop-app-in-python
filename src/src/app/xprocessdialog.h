#ifndef SMARTCALC_APP_XPROCESSDIALOG_H_
#define SMARTCALC_APP_XPROCESSDIALOG_H_

#include <QDialog>
#include <QMessageBox>

#include "controller.h"
#include "graph.h"

namespace Ui {
class XProcessDialog;
}

namespace s21 {

class XProcessDialog : public QDialog {
  Q_OBJECT

 public:
  explicit XProcessDialog(Controller controller, const char* str,
                          QWidget* parent = nullptr);
  ~XProcessDialog();

  QString get_answer();

 private:
  Ui::XProcessDialog* ui_;
  Controller controller_;
  QString answer_string_;
  const char* str_;
  bool collect_valid_;
  QVector<double> x_y_asix_;

  void CalculateExpression();
  void GoGraph();
  std::pair<QVector<double>, QVector<double>> CollectVectorsPair();

  bool CheckValid(QString x_value);

 private slots:
  void CalculatePressed();
};

}  // namespace s21

#endif  // SMARTCALC_APP_XPROCESSDIALOG_H_
