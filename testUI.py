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
        imap.login(entry_email.get_text(), entry_pass.get_text())
        # TODO: login dialog
        # TODO: destroy all windows
        main(entry_email.get_text(), entry_pass.get_text())
    except Exception as e:
        #Todo: login unsuccessful dialog
        pass


btn_login.connect("clicked", login)


window.show_all()
Gtk.main()
