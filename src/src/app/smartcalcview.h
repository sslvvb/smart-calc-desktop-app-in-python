#ifndef SMARTCALC_APP_SMARTCALCVIEW_H_
#define SMARTCALC_APP_SMARTCALCVIEW_H_

#include <QMainWindow>

#include "controller.h"
#include "xprocessdialog.h"

QT_BEGIN_NAMESPACE
namespace Ui {
class SmartCalcView;
}
QT_END_NAMESPACE

namespace s21 {

class SmartCalcView : public QMainWindow {
  Q_OBJECT

 public:
  SmartCalcView(QWidget *parent = nullptr);
  ~SmartCalcView();

 private slots:
  void NumberPressed();
  void FooPressed();
  void CleanPressed();
  void EqualPressed();

 private:
  Ui::SmartCalcView *ui_;
  Controller controller_;

  void CalculateExpression(const char *str);
  void CalculateGraphOrExpression(const char *str);
};

}  // namespace s21

#endif  // SMARTCALC_APP_SMARTCALCVIEW_H_
