#include "graph.h"

#include "ui_graph.h"

namespace s21 {

Graph::Graph(std::pair<QVector<double>, QVector<double>> pair,
             QVector<double> x_y_asix, QWidget *parent)
    : QDialog(parent), ui_(new Ui::Graph), pair_(pair), x_y_asix_(x_y_asix) {
  ui_->setupUi(this);
  DrawGraph();
}

Graph::~Graph() { delete ui_; }

void Graph::DrawGraph() {
  ui_->widget->xAxis->setRange(x_y_asix_[0], x_y_asix_[1]);
  ui_->widget->yAxis->setRange(x_y_asix_[2], x_y_asix_[3]);
  ui_->widget->setInteraction(QCP::iRangeZoom, true);
  ui_->widget->setInteraction(QCP::iRangeDrag, true);
  QPen pen;
  pen.setColor(QColor(250, 214, 230));
  ui_->widget->addGraph()->setPen(pen);
  ui_->widget->graph(0)->setLineStyle(QCPGraph::lsNone);
  ui_->widget->graph(0)->setScatterStyle(
      QCPScatterStyle(QCPScatterStyle::ssDisc, 3));
  ui_->widget->graph(0)->addData(pair_.first, pair_.second);
  ui_->widget->replot();
}

}  // namespace s21
