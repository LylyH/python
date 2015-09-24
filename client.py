#!/usr/bin/python3
# coding: utf-8
 
from gi.repository import Gtk
import socket

class ConnectWindow(Gtk.Window):

    def __init__(self):
        self.connectServer()
        self.store = Gtk.ListStore(int, str)
        for i in range(5):
            name = "Channel #%d" % i
            self.store.append([i, name])

        self.builder = Gtk.Builder()
        self.builder.add_from_file("glade/connect_create.glade")
        self.window = self.builder.get_object("connect_create")
        self.scroll = self.builder.get_object("scrolledwindow")
        self.list = Gtk.TreeView(self.store)
        
        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Channel Id", renderer, text=0)
        self.list.append_column(column)

        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Name", renderer, text=1)
        self.list.append_column(column)

        self.scroll.add(self.list);
        self.scroll.set_min_content_width(400)
        self.scroll.set_min_content_height(400)
        # for i in range(5):
        #     buffer = "ListItemContainer with Label #%d" % i
        #     self.populateChannel(buffer)

        # for row in self.store:
        #     # Print values of all columns
            # self.populateChannel(row[:])

        handlers = {
            "onDeleteWindow": Gtk.main_quit,
            }
        self.builder.connect_signals(handlers)
        self.window.show_all()

    def connectBtn(self, widget):
        self.builder.get_object("label_channel").set_text('Vous avez cliqué !')

    def populateListChannel(self, content):
        label = Gtk.Label(content)
        label.show()
        row = Gtk.ListBoxRow()
        row.add(label)
        self.listchannel.add(row)

    def connectServer(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("10.41.176.208", 1234))
        coucou = "Je suis un utilisateur qui lance le client.py"

        s.send(bytes(coucou, encoding='utf-8'))

ConnectWindow = ConnectWindow()
Gtk.main()