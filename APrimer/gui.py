import pygtk
pygtk.require("2.0")
import gtk
window = gtk.Window()
window.connect("delete-event", gtk.main_quit)
window.set_border_width(10)
button = gtk.Button("Hello World")

def on_button_clicked(button):
    print "Hello World"

button.connect("clicked", on_button_clicked)
window.add(button)
window.show_all()
gtk.main()
