#!/usr/bin/python3
# coding: utf-8
 
from gi.repository import Gtk
import socket

class ConnectWindow(Gtk.Window):

    def __init__(self):
        self.connectServer()
        self.store = Gtk.ListStore(int, str)
        
        # Generate default channel | TO_REMOVE
        for i in range(40):
            name = "Channel #%d" % i
            self.store.append([i, name])

        # Use GTK for create a window
        self.builder = Gtk.Builder()
        self.builder.add_from_file("glade/connect_create.glade")
        self.window = self.builder.get_object("connect_create")
        self.scroll = self.builder.get_object("scrolledwindow")

        # Create a trewView
        self.list = Gtk.TreeView(self.store)
        
        # Create column Channel Id
        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Channel Id", renderer, text=0)
        self.list.append_column(column)

        # Create column Name
        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Name", renderer, text=1)
        self.list.append_column(column)

        # Find the Gtk.TreeSelection object, and execute on_tree_selection_changed method
        select = self.list.get_selection()
        select.connect("changed", self.on_tree_selection_changed)

        # Add scroll
        self.scroll.add(self.list);
        self.scroll.set_min_content_width(400)
        self.scroll.set_min_content_height(325)

        handlers = {
            "onDeleteWindow": Gtk.main_quit,
            "onClickBtnConnect": self.connectBtn,
            "onClickCreateChannel": self.createChannel,
            }
        self.builder.connect_signals(handlers)
        self.window.show_all()

    def on_tree_selection_changed(self, selection):
        model, treeiter = selection.get_selected()
        if treeiter != None:
            print("You selected : " + str(model[treeiter][0]) + " -> " + str(model[treeiter][1]))
            self.channel_selected = treeiter

    def connectBtn(self, widget):
        print("Connection to : " + str(self.store[self.channel_selected][0]) + " -> " + str(self.store[self.channel_selected][1]))

    def createChannel(self, widget):
        channel_name = self.builder.get_object("create_input").get_text()
        self.store.append([len(self.store) + 1, channel_name])

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