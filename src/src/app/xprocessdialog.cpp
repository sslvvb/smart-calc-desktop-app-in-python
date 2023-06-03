#include "xprocessdialog.h"

#include "ui_xprocessdialog.h"

namespace s21 {

XProcessDialog::XProcessDialog(Controller controller, const char* str,
                               QWidget* parent)
    : QDialog(parent),
      ui_(new Ui::XProcessDialog),
      controller_(controller),
      str_(str) {
  ui_->setupUi(this);
  connect(ui_->calculate, SIGNAL(clicked()), this, SLOT(CalculatePressed()));
}

XProcessDialog::~XProcessDialog() { delete ui_; }

void XProcessDialog::CalculatePressed() {
  if (ui_->radio_expression->isChecked()) {
    CalculateExpression();
  } else if (ui_->radio_graph->isChecked()) {
    GoGraph();
  }
  close();
}

void XProcessDialog::CalculateExpression() {
  if (!ui_->line_x_expression->text().isEmpty()) {
    try {
      QString x_value = ui_->line_x_expression->text();
      if (CheckValid(x_value)) {
        double x_double = x_value.toDouble();
        double result = controller_.GetResult(str_, x_double);
        answer_string_ = QString::number(result);
      } else {
        QMessageBox::warning(this, "Werror", "X value incorrect");
      }
    } catch (const std::exception& ex) {
      QMessageBox::warning(this, "Werror", " Expression incorrect");
    }
  }
}

void XProcessDialog::GoGraph() {
  auto pair = CollectVectorsPair();
  if (collect_valid_) {
    Graph graph_window(pair, x_y_asix_);
    graph_window.setWindowTitle(str_);
    graph_window.exec();
  }
}

std::pair<QVector<double>, QVector<double>>
XProcessDialog::CollectVectorsPair() {
  std::pair<QVector<double>, QVector<double>> pair;
  try {
    QString x_min_str = ui_->line_x_min->text();
    QString x_max_str = ui_->line_x_max->text();
    QString y_min_str = ui_->line_y_min->text();
    QString y_max_str = ui_->line_y_max->text();

    x_y_asix_.push_back(x_min_str.toDouble());
    x_y_asix_.push_back(x_max_str.toDouble());
    x_y_asix_.push_back(y_min_str.toDouble());
    x_y_asix_.push_back(y_max_str.toDouble());

    if (CheckValid(x_min_str) && CheckValid(x_max_str) &&
        CheckValid(y_min_str) && CheckValid(y_max_str) &&
        x_y_asix_[0] < x_y_asix_[1] && x_y_asix_[2] < x_y_asix_[3]) {
      collect_valid_ = true;
      return controller_.GetResultForGraph(str_, x_y_asix_[0], x_y_asix_[1]);
    } else {
      QMessageBox::warning(this, "Werror", "Coordinate values incorrect");
      collect_valid_ = false;
    }
  } catch (const std::exception& ex) {
    QMessageBox::warning(this, "Werror", " Expression incorrect");
    collect_valid_ = false;
  }
  return pair;
}

bool XProcessDialog::CheckValid(QString x_value) {
  bool result = false;
  x_value.toDouble(&result);
  return result;
}

QString XProcessDialog::get_answer() { return answer_string_; }

}  // namespace s21
