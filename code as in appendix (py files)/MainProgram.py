from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.listview import ListItemButton
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager
from DNS_Server import Server
from NetworkHashTable import HashTable
import NetworkHashTable as netHashRef

server = Server()
newHash = HashTable()


class TabbedMenu(TabbedPanel):
    pass


class TaskBar(GridLayout):
    pass


class ListResult(ListItemButton):
    pass


class AppGridLayout(GridLayout):

    def create_domain(self, entry):
        if entry:
            try:
                netHashRef.popuptext(server.create_domain(entry))
            except (AttributeError, FileNotFoundError):
                pass

    def list_domains(self, entry):
        if entry:
            try:
                netHashRef.popuptext(server.print_directory(entry))
            except (AttributeError, FileNotFoundError, ValueError):
                if ValueError:
                    pass
                else:
                    netHashRef.popuptext("Error or No List Found")

    def generate_domains(self):
            try:
                server.print_domains(self)
            except (AttributeError, FileNotFoundError, ValueError):
                if ValueError:
                    pass
                else:
                    netHashRef.popuptext("Error or No List Found")

    def delete_domain_server(self, entry):
        if entry:
            try:
                netHashRef.popuptext(server.delete_domain(entry))
            except (AttributeError, FileNotFoundError, ValueError):
                if ValueError:
                    pass
                else:
                    netHashRef.popuptext("Error,Can't Delete Domain or doesn't exist")

    def insert_new(self, domain, ip_add):
        if domain and ip_add:
            try:
                netHashRef.popuptext(newHash.insert(domain, ip_add))
            except (AttributeError, FileNotFoundError, ValueError):
                if ValueError:
                    pass
                else:
                    netHashRef.popuptext("Error,Can't insert new entry")

    def search_by_name(self, entry):
        if entry:
            try:
                newHash.search(entry)
            except (AttributeError, FileNotFoundError):
                netHashRef.popuptext("Error or Not Found")

    def search_by_address(self, entry):
        if entry:
            try:
                netHashRef.popuptext(newHash.search(entry))
            except (AttributeError, FileNotFoundError):
                netHashRef.popuptext("Error or Not Found")

    def delete_domain_name(self, entry):
        if entry:
            try:
                netHashRef.popuptext(newHash.delete_address(entry))
            except (AttributeError, FileNotFoundError, ValueError):
                if Exception is ValueError:
                    netHashRef.popuptext("No Value Captured")
                else:
                    pass

    def close_window(self):
        Main.stop(App)

    def list_of_domains(self):
        pass

    def delete_entire_dns_domain(self):
        pass

    def about_popup(self):
        str_text = ''
        file = open("about.txt", 'r')
        about_text = file.readlines()
        for text in about_text:
            str_text += text
        popup = Popup(title='About',
                      content=Label(
                          text=str_text),
                      size_hint=(None, None), size=(700, 500))
        popup.open()

    def help_popup(self):
        str_text = ''
        file = open("help.txt", 'r')
        about_text = file.readlines()
        for text in about_text:
            str_text += text
        popup = Popup(title='HELP',
                      content=Label(text=str_text),
                      size_hint=(None, None), size=(800, 600))
        popup.open()
        file.close()


class AppBoxLayout(BoxLayout):
    pass


class RootScreen(ScreenManager):
    pass


class MainApp(App):
    App.title = "DNS SERVER SYSTEM"
    App.icon = "UI_files/icon.ico"

    def build(self):
        return AppGridLayout()


Main = MainApp()

if __name__ == "__main__":
    Main.run()
