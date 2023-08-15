# class EventHandler:
#     def __init__(self, view, history):
#         self.view = view
#         self.history = history  # зачем ?
#
#     # def init(self):
#     #
#     #
#     #     self.view.bind_history_menu_callback(self._history_menu_callback)
#     #     self.view.bind_graph_button_callback(self.graph_button_callback)
#
#     # def on_button_click(self, button_text):
#     #     # Handle button click events
#     #     pass
#     #
#     # def graph_button_callback(self):
#     #     # Handle graph button click event
#     #     pass
#     #
#     # def _show_error_message(self, message: str):
#     #     # Show error message
#     #     pass
#     #
#     # def check_coordinates(self):
#     #     # Check coordinates for graphing
#     #     pass
#     #
#     # def _history_menu_callback(self, choice):
#     #     # Handle history menu selection
#     #     pass
#     #
#     # def update_history(self, history: list):
#     #     # Update history menu
#     #     pass
#
# # event_handler.py
#
#     def on_button_click(self, button_text):
#         # if button_text == "GRAPH":
#         #     self.graph_button_callback()
#         # elif button_text == "AC":
#         #     self.expression_var.set('')
#         # elif button_text == "=":
#         #     self.presenter.handle_expression_result(self.expression_var.get(), str(self.x_var.get()))
#         # elif button_text == "Delete history":
#         #     self.presenter.handle_delete_history()
#         # elif button_text == "About app":
#         #     if self.about_window is None or not self.about_window.winfo_exists():
#         #         self.about_window = About(self, background=self.get_code_bg_color(self.background))
#         #     else:
#         #         self.about_window.focus()
#         # else:
#         #     self.append_to_expression(button_text)
#
#         if button_text == "GRAPH":
#             # self.graph_button_callback()
#             pass
#         elif button_text == "AC":
#             self.view.expression_var.set('')
#         elif button_text == "=":
#             self.view.presenter.handle_expression_result(self.view.expression_var.get(), self.view.x_var.get())
#         elif button_text == "Delete history":
#             pass
#             # self.presenter.handle_delete_history()
#         elif button_text == "About app":
#             pass
#             # self.show_about_window()
#         else:
#             self.append_to_expression(button_text)
#
#     def graph_button_callback(self):
#         if self.check_coordinates():
#             self.view.presenter.handle_graphic_result(
#                 self.view.get_expression_var(),
#                 self.view.get_x_min_var(),
#                 self.view.get_x_max_var()
#             )
#         else:
#             self._show_error_message('Error in expression or coordinate values.')
#
#     def _show_error_message(self, message: str):
#         if not self.view.error_window_exists():
#             self.view.create_error_window(message)
#         else:
#             self.view.focus_error_window()
#
#     def show_about_window(self):
#         if not self.view.about_window_exists():
#             self.view.create_about_window()
#         else:
#             self.view.focus_about_window()
#
#     def check_coordinates(self):
#         if (
#             self.view.get_expression_var() != ''
#             and self.view.get_x_min_var() != ''
#             and self.view.get_x_max_var() != ''
#             and self.view.get_y_min_var() != ''
#             and self.view.get_y_max_var() != ''
#         ):
#             if (
#                 float(self.view.get_x_min_var()) < float(self.view.get_x_max_var())
#                 and float(self.view.get_y_min_var()) < float(self.view.get_y_max_var())
#             ):
#                 return True
#         return False
#
#     def _history_menu_callback(self, choice):
#         if choice != 'No History':
#             history_item = choice.rstrip()
#             split_lines = history_item.split('=')
#             self.view.set_expression_var(split_lines[0])
#             self.view.set_x_var(split_lines[2])
#
#     def update_history(self, history: list):
#         self.history = history
#         self.view.update_history_menu(self._history_menu_values())
#         if self.history:
#             self.view.set_history_menu(self.history[0])
#         else:
#             self.view.set_history_menu('No History')
#
#
#
#     def append_to_expression(self, text):
#         current_expression = self.view.expression_var.get()
#         if len(current_expression) + len(text) <= 255:
#             new_expression = current_expression + text
#             self.view.expression_var.set(new_expression)
#
#
#
#
# # # event_handler.py
# #
# # class EventHandler:
# #     def __init__(self, view, presenter):
# #         self.view = view
# #         self.presenter = presenter
# #
# #     def bind_events(self):
# #         # Bind events to UI elements here
# #         self.view.expression_var.trace_add('write', self.expression_var_changed)
# #         for button in self.view.buttons:
# #             button.configure(command=lambda b=button: self.on_button_click(b.cget('text')))
# #
# #     def on_button_click(self, button_text):
# #         if button_text == "GRAPH":
# #             self.graph_button_clicked()
# #         elif button_text == "AC":
# #             self.view.expression_var.set('')
# #         elif button_text == "=":
# #             self.presenter.handle_expression_result(self.view.expression_var.get(), str(self.view.x_var.get()))
# #         # Handle other button clicks here...
# #
# #     def graph_button_clicked(self):
# #         if self.view.check_coordinates():
# #             self.presenter.handle_graphic_result(
# #                 self.view.expression_var.get(),
# #                 self.view.x_min_var.get(),
# #                 self.view.x_max_var.get()
# #             )
# #         else:
# #             self.view.show_error_message('Error in expression or coordinate values.')
# #
# #     def expression_var_changed(self, *args):
# #         # Handle expression variable changes, if needed
# #         pass
# #
# #     # Add more event handlers as needed...
