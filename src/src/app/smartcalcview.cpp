#include "smartcalcview.h"

#include "ui_smartcalcview.h"

namespace s21 {

SmartCalcView::SmartCalcView(QWidget* parent)
    : QMainWindow(parent), ui_(new Ui::SmartCalcView) {
  ui_->setupUi(this);
  connect(ui_->num_0, SIGNAL(clicked()), this, SLOT(NumberPressed()));
  connect(ui_->num_1, SIGNAL(clicked()), this, SLOT(NumberPressed()));
  connect(ui_->num_2, SIGNAL(clicked()), this, SLOT(NumberPressed()));
  connect(ui_->num_3, SIGNAL(clicked()), this, SLOT(NumberPressed()));
  connect(ui_->num_4, SIGNAL(clicked()), this, SLOT(NumberPressed()));
  connect(ui_->num_5, SIGNAL(clicked()), this, SLOT(NumberPressed()));
  connect(ui_->num_6, SIGNAL(clicked()), this, SLOT(NumberPressed()));
  connect(ui_->num_7, SIGNAL(clicked()), this, SLOT(NumberPressed()));
  connect(ui_->num_8, SIGNAL(clicked()), this, SLOT(NumberPressed()));
  connect(ui_->num_9, SIGNAL(clicked()), this, SLOT(NumberPressed()));
  connect(ui_->add, SIGNAL(clicked()), this, SLOT(NumberPressed()));
  connect(ui_->sub, SIGNAL(clicked()), this, SLOT(NumberPressed()));
  connect(ui_->mul, SIGNAL(clicked()), this, SLOT(NumberPressed()));
  connect(ui_->div, SIGNAL(clicked()), this, SLOT(NumberPressed()));
  connect(ui_->pow, SIGNAL(clicked()), this, SLOT(NumberPressed()));
  connect(ui_->x_symbol, SIGNAL(clicked()), this, SLOT(NumberPressed()));
  connect(ui_->e_symbol, SIGNAL(clicked()), this, SLOT(NumberPressed()));
  connect(ui_->dot, SIGNAL(clicked()), this, SLOT(NumberPressed()));
  connect(ui_->open_brckt, SIGNAL(clicked()), this, SLOT(NumberPressed()));
  connect(ui_->close_brckt, SIGNAL(clicked()), this, SLOT(NumberPressed()));
  connect(ui_->sin, SIGNAL(clicked()), this, SLOT(FooPressed()));
  connect(ui_->asin, SIGNAL(clicked()), this, SLOT(FooPressed()));
  connect(ui_->cos, SIGNAL(clicked()), this, SLOT(FooPressed()));
  connect(ui_->acos, SIGNAL(clicked()), this, SLOT(FooPressed()));
  connect(ui_->tan, SIGNAL(clicked()), this, SLOT(FooPressed()));
  connect(ui_->atan, SIGNAL(clicked()), this, SLOT(FooPressed()));
  connect(ui_->mod, SIGNAL(clicked()), this, SLOT(FooPressed()));
  connect(ui_->ln, SIGNAL(clicked()), this, SLOT(FooPressed()));
  connect(ui_->sqrt, SIGNAL(clicked()), this, SLOT(FooPressed()));
  connect(ui_->log, SIGNAL(clicked()), this, SLOT(FooPressed()));
  connect(ui_->clean, SIGNAL(clicked()), this, SLOT(CleanPressed()));
  connect(ui_->equals, SIGNAL(clicked()), this, SLOT(EqualPressed()));
}

SmartCalcView::~SmartCalcView() { delete ui_; }

void SmartCalcView::NumberPressed() {
  ui_->answer_line->clear();
  QPushButton* button = (QPushButton*)sender();
  QString text = ui_->text_line->text() + button->text();
  if (text.size() <= 255) ui_->text_line->setText(text);
}

void SmartCalcView::FooPressed() {
  ui_->answer_line->clear();
  QPushButton* button = (QPushButton*)sender();
  QString text = ui_->text_line->text() + button->text() + "(";
  if (text.size() <= 255) ui_->text_line->setText(text);
}

void SmartCalcView::CleanPressed() {
  ui_->text_line->clear();
  ui_->answer_line->clear();
}

void SmartCalcView::EqualPressed() {
  QString qstr = ui_->text_line->text();
  QByteArray expression = qstr.toLocal8Bit();
  if (expression.size() > 0) {
    const char* str = expression.constData();
    if (expression.contains("x")) {
      CalculateGraphOrExpression(str);
    } else {
      CalculateExpression(str);
    }
  }
}

void SmartCalcView::CalculateExpression(const char* str) {
  try {
    double result = controller_.GetResult(str);
    QString result_string = QString::number(result);
    ui_->answer_line->setText(result_string);
  } catch (const std::exception& ex) {
    ui_->answer_line->setText(ex.what());
  }
  ui_->text_line->clear();
}

void SmartCalcView::CalculateGraphOrExpression(const char* str) {
  XProcessDialog dialog(controller_, str);
  dialog.setWindowTitle("X process ...");
  dialog.exec();
  ui_->answer_line->setText(dialog.get_answer());
  ui_->text_line->clear();
}

}  // namespace s21
