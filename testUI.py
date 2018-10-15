import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from main import main
import imaplib
builder = Gtk.Builder()
builder.add_from_file("login.glade")
window = builder.get_object("window")
window.connect("delete-event", Gtk.main_quit)

entry_email = builder.get_object("email")
entry_pass = builder.get_object("pass")

btn_login = builder.get_object("login")
btn_forget = builder.get_object("forget")


def login(button):

    imap = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    try:
        username = entry_email.get_text()
        password = entry_pass.get_text()


        imap.login(entry_email.get_text(), entry_pass.get_text())
        # TODO: login dialog
        window.destroy()
        builder2 = Gtk.Builder()
        builder2.add_from_file("success.glade")
        window2 = builder2.get_object("Success")
        window2.connect("delete-event", Gtk.main_quit)
        #btn_ok = builder2.get_object("OK")
        #btn_ok.connect("clicked", Gtk.main_quit)
        window2.show_all()

        # TODO: destroy all windows
        main(username, password)
    except Exception as e:
        #Todo: login unsuccessful dialog
        pass


btn_login.connect("clicked", login)


window.show_all()
Gtk.main()
