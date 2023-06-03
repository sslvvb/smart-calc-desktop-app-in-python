#include <QApplication>

#include "smartcalcview.h"

int main(int argc, char *argv[]) {
  QApplication a(argc, argv);
  s21::SmartCalcView window;
  window.show();
  return a.exec();
}
