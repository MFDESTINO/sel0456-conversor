#!/usr/bin/env python

import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

class Conversor:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("conversor.glade")
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("window1")
        self.mode = 0
        self.res = 0
        self.input_num_widget = self.builder.get_object('input_num')
        self.output_num_widget = self.builder.get_object('output_num')
        self.window.show()

    def on_window1_destroy(self, object, data=None):
        Gtk.main_quit()
    
    def on_button1_clicked(self, button):
        self.input_num = float(self.input_num_widget.get_text())
        if self.mode == 0:
            self.res = self.input_num * 0.393701
        elif self.mode == 1:
            self.res = self.input_num * 2.54
        elif self.mode == 2:
            self.res = self.input_num * 9/5 + 32
        elif self.mode == 3:
            self.res = (self.input_num - 32) * 5/9
        self.output_num_widget.set_text(str(self.res))

    def button_toggle(self, widget):
        if widget.get_active():
        # if the active widget name is equal to 'rb1': then set the label text
            if Gtk.Buildable.get_name(widget)=='rb1':self.mode = 0
            if Gtk.Buildable.get_name(widget)=='rb2':self.mode = 1
            if Gtk.Buildable.get_name(widget)=='rb3':self.mode = 2
            if Gtk.Buildable.get_name(widget)=='rb4':self.mode = 3

if __name__ == "__main__":
    main = Conversor()
    Gtk.main()