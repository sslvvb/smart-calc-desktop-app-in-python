#ifndef SMARTCALC_APP_GRAPH_H_
#define SMARTCALC_APP_GRAPH_H_

#include <QDialog>
#include <QVector>

namespace Ui {
class Graph;
}

namespace s21 {

class Graph : public QDialog {
  Q_OBJECT

 public:
  explicit Graph(std::pair<QVector<double>, QVector<double>> pair,
                 QVector<double> x_y_asix, QWidget *parent = nullptr);
  ~Graph();

 private:
  Ui::Graph *ui_;
  std::pair<QVector<double>, QVector<double>> pair_;
  QVector<double> x_y_asix_;

  void DrawGraph();
};

}  // namespace s21

#endif  // SMARTCALC_APP_GRAPH_H_
