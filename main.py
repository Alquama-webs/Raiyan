import qrcode
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivymd.uix.navigationdrawer import MDNavigationDrawer, MDNavigationDrawerItem
from kivymd.uix.textfield import MDTextField



KV = '''
MDScreen:
    MDNavigationLayout:

        ScreenManager:
            id: screen_manager

            MDScreen:
                name: 'home'

                MDTopAppBar:
                    title: "{SR} QR Code Genrator"
                    elevation: 4
                    pos_hint: {"top": 1}
                    left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]

                MDLabel:
                    text: "Welcome QR Code Genrator!"
                    pos_hint:{'center_x':0.5,'center_y':0.85}
                    font_size:"25sp"
                    font_style:"H4"

                MDTextField:
                    id:img_name
                    hint_text: "Enter Your QR Code Image Name"
                    pos_hint:{'center_x':0.5,'center_y':0.6}
                    size_hint_x: None
                    width: "250dp"


                MDTextField:
                    id:qr_link
                    hint_text: "Enter your link"
                    pos_hint:{'center_x':0.5,'center_y':0.53}
                    size_hint_x: None
                    width: "250dp"


                MDFlatButton:
                    text:'Genrate QR'
                    md_bg_color:"#4169E1"
                    pos_hint:{'center_x':0.5,'center_y':0.45}
                    on_release: app.print_text()

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)

            ContentNavigationDrawer:
'''

class ContentNavigationDrawer(MDBoxLayout):
    pass

class SRQRCodeGenrator(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Dark" 
        return Builder.load_string(KV)

    def print_text(self):
        img = self.root.ids.img_name.text
        link = self.root.ids.qr_link.text
        qr = qrcode.QRCode(version=1, box_size=15, border=5, error_correction=qrcode.constants.ERROR_CORRECT_H)
        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill_color="green",back_color="white")
        img.save(f"{img}.png")

if __name__ == "__main__":
    SRQRCodeGenrator().run()


