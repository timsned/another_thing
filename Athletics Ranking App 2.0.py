from ARS import db

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.label import MDLabel
from kivymd.toast import toast
from kivy.properties import ObjectProperty
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField, MDTextFieldRound, MDTextFieldRect
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.list import ILeftBody, IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.list import OneLineAvatarListItem
from kivymd.icon_definitions import md_icons
from kivy.properties import StringProperty, AliasProperty
from kivymd.uix.gridlayout import GridLayout
from kivy.factory import Factory
from kivy.uix.image import Image
from kivymd.uix.navigationdrawer import NavigationLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemeManager
from kivymd.color_definitions import text_colors


def get_male_category():
    gender_category = []
    for event in db.fetch_category():
        if event[0] not in gender_category:
            gender_category.append(event[0])
    return gender_category  

def get_female_category():
    gender_category = []
    for event in db.fetch_category():
        if event[0] not in gender_category:
            gender_category.append(event[1])
    return gender_category

def get_mshr():
    discipline = []
    for event in db.fetch_discipline():
        if event[0] not in discipline:
            discipline.append(event[0])        
    return discipline
    
def get_mmd():
    discipline = []
    for event in db.fetch_discipline():
        if event[0] not in discipline:
            discipline.append(event[1])
    return discipline

def get_mlds():
    discipline = []
    for event in db.fetch_discipline():
        if event[0] not in discipline:
            discipline.append(event[2])
    return discipline

def get_mrr():
    discipline = []
    for event in db.fetch_discipline():
        if event[0] not in discipline:
            discipline.append(event[3])
    return discipline

def get_mrw():
    discipline = []
    for event in db.fetch_discipline():
        if event[0] not in discipline:
            discipline.append(event[4])
    return discipline

def get_mjtc():
    discipline = []
    for event in db.fetch_discipline():
        if event[0] not in discipline:
            discipline.append(event[5])
    return discipline

def get_wshr():
    discipline = []
    for event in db.fetch_discipline():
        if event[0] not in discipline:
            discipline.append(event[6])
    return discipline

def get_wmd():
    discipline = []
    for event in db.fetch_discipline():
        if event[0] not in discipline:
            discipline.append(event[7])
    return discipline

def get_wlds():
    discipline = []
    for event in db.fetch_discipline():
        if event[0] not in discipline:
            discipline.append(event[8])
    return discipline

def get_wrr():
    discipline = []
    for event in db.fetch_discipline():
        if event[0] not in discipline:
            discipline.append(event[9])
    return discipline

def get_wrw():
    discipline = []
    for event in db.fetch_discipline():
        if event[0] not in discipline:
            discipline.append(event[10])
    return discipline

def get_wjtc():
    discipline = []
    for event in db.fetch_discipline():
        if event[0] not in discipline:
            discipline.append(event[11])
    return discipline

def get_event_level():
    return [item[0] for item in db.fetch_event_level()]
    
def get_events():
    return [item[0] for item in db.fetch_event()]

event_ow = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', 
'9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th']
event_df = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', 
'9th', '10th', '11th', '12th'] 
event_gw = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', 
'9th', '10th', '11th', '12th']
event_gl = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', 
'9th', '10th', '11th', '12th']
event_a = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th']
event_b = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th']
event_c = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th']
event_d = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th']
event_e = ['1st', '2nd', '3rd', '4th', '5th', '6th']
event_f = ['1st', '2nd', '3rd']

class MainApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "HPSNZ OptoTrack"
        self.theme_cls = ThemeManager()

        self.genders = ['Male', 'Female']
        
        self.category_list = []
        self.male_events = get_male_category() 
        self.female_events = get_female_category()

        self.discipline_list = []
        self.mshr = get_mshr()
        self.mmd = get_mmd()
        self.mlds = get_mlds()
        self.mrr = get_mrr()
        self.mrw = get_mrw()
        self.mjtc = get_mjtc()
        self.wshr = get_wshr()
        self.wmd = get_wmd()
        self.wlds = get_wlds()
        self.wrr = get_wrr()
        self.wrw = get_wrw()
        self.wjtc = get_wjtc()

        self.event_level = get_event_level()

        self.placing_list = []
        self.ow = event_ow
        self.df = event_df
        self.gw = event_gw
        self.gl = event_gl
        self.a = event_a
        self.b = event_b
        self.c = event_c
        self.d = event_d
        self.e = event_e
        self.f = event_f

        self.event_selected = None
        self.placing_selected = None
        self.placing_points = None

        self.category = None
        self.discipline = None
        self.result = None 
        self.result_score = None
        self.wind = ''
        self.wind_modification = None

        self.events = get_events()
        self.matching_events = []

        super().__init__(**kwargs)

    def on_start(self):
        self.root.ids.event_screen.populate_event_list()
        build_nav_drawer(self)
        
    '''
    def get_result_points(self):
        result = db.fetch_result_score(self.category, str(self.discipline), self.result)
        discipline = result[0]
        return discipline[0]
    '''
    def get_placing_points(self):
        result = db.fetch_placing_score(str(self.event_selected))
        event = result[0]
        points = event[int(self.placing_selected)]
        self.placing_points = points   

    def get_wind_modification(self):
        result = db.fetch_wind_modification(self.wind)
        wind = result[0]
        points = wind[int()]
        self.wind_modification = points

    def get_result_category(self):
        result = db.fetch_result_list(self.category)
        return result
#-------------------------------------Login----------------------------------------------
class LoginScreen(Screen):
    pass

#-------------------------------------Nav Drawer-----------------------------------------
class ContentNavigationDrawer(BoxLayout):
    """Base Widget for Navigation Drawer"""
    pass

class FirstNavItem(OneLineAvatarListItem):
    """Item in Nav Drawer callback to First screen"""
    icon = StringProperty()
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        super().__init__(**kwargs)

    def callback(self):
        ###################################################
        #functions for populating and going to your screen go here
        ###################################################
        self.app.root.ids.MainScreenManager.current = 'screen1'
        self.app.root.ids.nav_drawer.set_state('toggle')

class SecondNavItem(OneLineAvatarListItem):
    """Item in Nav Drawer callback to Second screen"""
    icon = StringProperty()
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        super().__init__(**kwargs)

    def callback(self):
        ###################################################
        #functions for populating and going to your screen go here
        ###################################################
        self.app.root.ids.MainScreenManager.current = 'screen2'
        self.app.root.ids.nav_drawer.set_state('toggle')
    
class ThirdNavItem(OneLineAvatarListItem):
    """Item in Nav Drawer callback to Third screen"""
    icon = StringProperty()
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        super().__init__(**kwargs)

    def callback(self):
        ###################################################
        #functions for populating and going to your screen go here
        ###################################################
        self.app.root.ids.MainScreenManager.current = 'screen3'
        self.app.root.ids.nav_drawer.set_state('toggle')  

class FourthNavItem(OneLineAvatarListItem):
    """Item in Nav Drawer callback to Fourth screen"""
    icon = StringProperty()
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        super().__init__(**kwargs)

    def callback(self):
        ###################################################
        #functions for populating and going to your screen go here
        ###################################################
        self.app.root.ids.MainScreenManager.current = 'screen4'
        self.app.root.ids.nav_drawer.set_state('toggle') 

class FifthNavItem(OneLineAvatarListItem):
    """Item in Nav Drawer callback to Fourth screen"""
    icon = StringProperty()
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        super().__init__(**kwargs)

    def callback(self):
        ###################################################
        #functions for populating and going to your screen go here
        ###################################################
        self.app.root.ids.MainScreenManager.current = 'screen5'
        self.app.root.ids.nav_drawer.set_state('toggle') 

def build_nav_drawer(running_app):
    running_app.root.ids.content_drawer.ids.box_item.clear_widgets()
    running_app.root.ids.content_drawer.ids.box_item.add_widget(FirstNavItem(icon="run", text="Performance"))
    running_app.root.ids.content_drawer.ids.box_item.add_widget(SecondNavItem(icon="medal-outline", text="Placing"))
    running_app.root.ids.content_drawer.ids.box_item.add_widget(ThirdNavItem(icon="weather-windy", text="Wind"))
    running_app.root.ids.content_drawer.ids.box_item.add_widget(FourthNavItem(icon="account-search", text="Events"))
    running_app.root.ids.content_drawer.ids.box_item.add_widget(FifthNavItem(icon="weather-windy", text="Tracking"))
    


class ListItemWithCheckbox(OneLineAvatarIconListItem):
    '''Custom list item.'''
    icon = StringProperty("android")

class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''Custom right container.'''
#------------------------------------Genders-------------------------------------------------------------
class GenderDropDown(MDRaisedButton):
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        super().__init__(**kwargs)

    def generate_genders(self):
        menu_items = [
            {
                "viewclass": "MDMenuItem",
                "text": item,
            }
            for item in self.app.genders
        ]
        return menu_items


    def open_gender_dropdown(self):
        built_items = self.generate_genders()
        MDDropdownMenu(callback=self.gender_callback, caller=self, items=built_items, width_mult=3).open()
        
    def gender_callback(self, instance):
        gender = instance.text
        if gender == 'Male':
            self.app.category_list = self.app.male_events   
        if gender == 'Female':
            self.app.category_list = self.app.female_events
        return
#--------------------------------------Category-----------------------------------------------------------
class CategoryDropDown(MDRaisedButton):
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        super().__init__(**kwargs)

    def generate_category(self):
        menu_items = [
            {
                "viewclass": "MDMenuItem",
                "text": item,
            }
            for item in self.app.category_list
        ]
        return menu_items

    def open_category_dropdown(self):
        
        built_items = self.generate_category()
        MDDropdownMenu(callback=self.category_callback, caller=self, items=built_items, width_mult=6).open()

    def category_callback(self, instance):
        category_selected = instance.text
        if category_selected == 'Mens Sprints, Hurdles & Relays':
            self.app.discipline_list = self.app.mshr
            self.app.category = 'Mens_Sprints_Hurdles_Relays'
        if category_selected == 'Mens Middle Distances':
            self.app.discipline_list = self.app.mmd
            self.app.category = 'Mens_Middle_Distances'
        if category_selected == 'Mens Long Distances & Steeple':
            self.app.discipline_list = self.app.mlds
            self.app.category = 'Mens_Long_Distances_Steeple'
        if category_selected == 'Mens Road Running':
            self.app.discipline_list = self.app.mrr
            self.app.category = 'Mens_Road_Running'
        if category_selected == 'Mens Race Walking':
            self.app.discipline_list = self.app.mrw
            self.app.category = 'Mens_Race_Walking'
        if category_selected == 'Mens Jumps, Throws & Combined':
            self.app.discipline_list = self.app.mjtc
            self.app.category = 'Mens_Jumps_Throws_Combined'
        if category_selected == 'Womens Sprints, Hurdles & Relays':
            self.app.discipline_list = self.app.wshr
            self.app.category = 'Womens_Sprints_Hurdles_Relays'
        if category_selected == 'Womens Middle Distances':
            self.app.discipline_list = self.app.wmd
            self.app.category = 'Womens_Middle_Distances'
        if category_selected == 'Womens Long Distances & Steeple':
            self.app.discipline_list = self.app.wlds
            self.app.category = 'Womens_Long_Distances_Steeple'
        if category_selected == 'Womens Road Running':
            self.app.discipline_list = self.app.wrr
            self.app.category = 'Womens_Road_Running'
        if category_selected == 'Womens Race Walking':
            self.app.discipline_list = self.app.wrw
            self.app.category = 'Womens_Race_Walking'
        if category_selected == 'Womens Jumps, Throws & Combined':
            self.app.discipline_list = self.app.wjtc
            self.app.category = 'Womens_Jumps_Throws_Combined'
        
#-------------------------------------Disciplines------------------------------------------------------------
class DisciplineDropDown(MDRaisedButton):
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        super().__init__(**kwargs)

    def generate_discipline(self):
        for item in self.app.discipline_list:
            if item == None:
                self.app.discipline_list.remove(None) 
        
        if None in self.app.discipline_list:
            self.app.discipline_list.remove(None)
        
        menu_items = [
            {
                "viewclass": "MDMenuItem",
                "text": item,
            }
            for item in self.app.discipline_list
        ]
        return menu_items
        
    def open_discipline_dropdown(self):
        built_items = self.generate_discipline()
        MDDropdownMenu(callback=self.discipline_callback, caller=self, items=built_items, width_mult=5).open()

    def discipline_callback(self, instance):
        discipline_selected = instance.text
        if discipline_selected == '100m':
            self.app.discipline = '_100m'
        if discipline_selected == '110mH':
            self.app.discipline = '_110mH'
        if discipline_selected == '100mH':
            self.app.discipline = '_100mH'    
        if discipline_selected == '200m':
            self.app.discipline = '_200m'
        if discipline_selected == '300m':
            self.app.discipline = '_300m'
        if discipline_selected == '400m':
            self.app.discipline = '_400m'
        if discipline_selected == '400mH':
            self.app.discipline = '_400mH'
        if discipline_selected == '4x100m':
            self.app.discipline = '_4x100m'
        if discipline_selected == '4x200m':
            self.app.discipline = '_4x200m'
        if discipline_selected == '4x400m':
            self.app.discipline = '_4x400m'
        if discipline_selected == '600m':
            self.app.discipline = '_600m'
        if discipline_selected == '800m':
            self.app.discipline = '_800m'
        if discipline_selected == '1000m':
            self.app.discipline = '_1000m'
        if discipline_selected == '1500m':
            self.app.discipline = '_1500m'
        if discipline_selected == 'Mile':
            self.app.discipline = '_Mile'
        if discipline_selected == '2000m':
            self.app.discipline = '_2000m'
        if discipline_selected == '2000m SC':
            self.app.discipline = '_2000m_SC'
        if discipline_selected == '3000m':
            self.app.discipline = '_3000m'       
        if discipline_selected == '3000m SC':
            self.app.discipline = '_3000m_SC'
        if discipline_selected == '2 Miles':
            self.app.discipline = '_2_Miles'
        if discipline_selected == '5000m':
            self.app.discipline = '_5000m'
        if discipline_selected == '10000m':
            self.app.discipline = '_10000m'
        if discipline_selected == '10 km':
            self.app.discipline = '_10_km' 
        if discipline_selected == '15 km':
            self.app.discipline = '_15_km'       
        if discipline_selected == '10 Miles':
            self.app.discipline = '_10_Miles'
        if discipline_selected == '20 km':
            self.app.discipline = '_20_km'
        if discipline_selected == 'Half Marathon':
            self.app.discipline = '_Half_Marathon'
        if discipline_selected == '25 km':
            self.app.discipline = '_25_km'
        if discipline_selected == '30 km':
            self.app.discipline = '_30_km'
        if discipline_selected == 'Marathon':
            self.app.discipline = '_Marathon'
        if discipline_selected == '100 km':
            self.app.discipline = '_100_km' 
        if discipline_selected == '3km W':
            self.app.discipline = '_3km_W'       
        if discipline_selected == '5km W':
            self.app.discipline = '_5km_W'
        if discipline_selected == '10km W':
            self.app.discipline = '_10km_W'
        if discipline_selected == '20km W':
            self.app.discipline = '_20km_W'
        if discipline_selected == '30km W':
            self.app.discipline = '_30km_W'
        if discipline_selected == '35km W':
            self.app.discipline = '_35km_W'
        if discipline_selected == '50km W':
            self.app.discipline = '_50km_W'
        if discipline_selected == 'High Jump':
            self.app.discipline = '_High_Jump'
        if discipline_selected == 'Pole Vault':
            self.app.discipline = '_Pole_Vault'
        if discipline_selected == 'Long Jump':
            self.app.discipline = '_Long_Jump'
        if discipline_selected == 'Triple Jump':
            self.app.discipline = '_Triple_Jump'
        if discipline_selected == 'Shot Put':
            self.app.discipline = '_Shot_Put'
        if discipline_selected == 'Discus Throw':
            self.app.discipline = '_Discus_Throw'
        if discipline_selected == 'Hammer Throw':
            self.app.discipline = '_Hammer_Throw'
        if discipline_selected == 'Javelin Throw':
            self.app.discipline = '_Javelin_Throw' 
        if discipline_selected == 'Decathlon':
            self.app.discipline = '_Decathlon'  
        if discipline_selected == 'Heptathlon':
            self.app.discipline = '_Heptathlon' 
#-------------------------------------Result------------------------------------------------------------

class ResultTextField(MDTextField):
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        super().__init__(**kwargs)

class ResultEntry(MDRaisedButton):
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        super().__init__(**kwargs)

    def result_entry(self):
        result_entered = self.app.root.ids.resulttextfield.text
        if result_entered == '':
            return None
             
        else:
            result = result_entered.replace(':', '') 
            self.app.result = result
            
#-------------------------------------Result Score------------------------------------------------------------
class ResultScoreButton(MDRaisedButton):
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        super().__init__(**kwargs)

    #def print_result_score(self):
        #print(self.app.get_result_points())     

    def find_discipline(self):
        discipline_selected = self.app.discipline
        if discipline_selected == '_100m':
            position = 1 	
        if discipline_selected == '_600m':
            position = 1 
        if discipline_selected == '_2000m_SC':
            position = 1 
        if discipline_selected == '_10_km':
            position = 1                   
        if discipline_selected == '_3km_W':
            position = 1 	
        if discipline_selected == '_High_Jump':
            position = 1 
        if discipline_selected == '_100mH':
            position = 2 
        if discipline_selected == '_110mH':
            position = 2
        if discipline_selected == '_3000m':
            position = 2 	
        if discipline_selected == '_15_km':
            position = 2 
        if discipline_selected == '_5km_W':
            position = 2 
        if discipline_selected == '_Pole_Vault':
            position = 2
        if discipline_selected == '_200m':
            position = 3 	
        if discipline_selected == '_1000m':
            position = 3 
        if discipline_selected == '_3000m_SC':
            position = 3 
        if discipline_selected == '_10_Miles':
            position = 3
        if discipline_selected == '_10km_W':
            position = 3 	
        if discipline_selected == '_Long_Jump':
            position = 3 
        if discipline_selected == '_300m':
            position = 4 
        if discipline_selected == '_1500m':
            position = 4
        if discipline_selected == '_2_Miles':
            position = 4 	
        if discipline_selected == '_20_km':
            position = 4 
        if discipline_selected == '_20km_W':
            position = 4 
        if discipline_selected == '_Triple_Jump':
            position = 4
        if discipline_selected == '_400m':
            position = 5 	
        if discipline_selected == '_Mile':
            position = 5 
        if discipline_selected == '_5000m':
            position = 5 
        if discipline_selected == '_Half_Marathon':
            position = 5
        if discipline_selected == '_30km_W':
            position = 5 	
        if discipline_selected == '_Shot_Put':
            position = 5 
        if discipline_selected == '_400mH':
            position = 6 
        if discipline_selected == '_2000m': 
            position = 6
        if discipline_selected == '_10000m':
            position = 6 	
        if discipline_selected == '_25_km':
            position = 6 
        if discipline_selected == '_50km_W':
            position = 6 
        if discipline_selected == '_Discus_Throw':
            position = 6
        if discipline_selected == '_4x100m':
            position = 7 	
        if discipline_selected == '_30_km':
            position = 7 
        if discipline_selected == '_Hammer_Throw':
            position = 7 
        if discipline_selected == '_4x200m':
            position = 8
        if discipline_selected == '_Marathon':
            position = 8 	
        if discipline_selected == '_Javelin_Throw':
            position = 8 
        if discipline_selected == '_4x400m':
            position = 9 
        if discipline_selected == '_100_km':
            position = 9
        if discipline_selected == '_Decathlon':
            position = 9 
        if discipline_selected == '_Heptathlon':
            position = 9
        return position

    def get_result_category(self):
        result = db.fetch_result_list(self.app.category)
        return result

    def get_result_list(self): 
        result_list = [item[self.find_discipline()] for item in self.get_result_category()]
        #print(self.app.result)
        closest_num = min(result_list, key=lambda x:abs(x-float(self.app.result)))
        return closest_num

    def get_result_score(self):
        if self.app.category == None:
            return None
        if self.app.discipline == None:
            return None
        if self.app.result == None:
            return None
        else:
            result = db.fetch_result_score(self.app.category, str(self.app.discipline), self.get_result_list())
            discipline = result[0]
            self.app.result_score = discipline[0] 
            print(self.app.result_score)

class DisplayResultScore(MDLabel):
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        super().__init__(**kwargs)

    def display_result_score(self):
        return self.app.result_score
#-------------------------------------Event Level------------------------------------------------------------
class EventLevelDropDown(MDRaisedButton):
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        super().__init__(**kwargs)
    
    def generate_event_level(self):
        menu_items = [
            {
                "viewclass": "MDMenuItem",
                "text": item,
            }
            for item in self.app.event_level
        ]
        return menu_items

    def open_event_level_dropdown(self):
        
        built_items = self.generate_event_level()
        MDDropdownMenu(callback=self.event_level_callback, caller=self, items=built_items, width_mult=3).open()

    def event_level_callback(self, instance):
        event_level = instance.text
        if event_level == 'OW':
            self.app.event_selected = 'OW'
            self.app.placing_list = self.app.ow
        if event_level == 'DF':
            self.app.event_selected = 'DF'
            self.app.placing_list = self.app.df
        if event_level == 'GW':
            self.app.event_selected = 'GW'
            self.app.placing_list = self.app.gw
        if event_level == 'GL':
            self.app.event_selected = 'GL'
            self.app.placing_list = self.app.gl
        if event_level == 'A':
            self.app.event_selected = 'A'
            self.app.placing_list = self.app.a
        if event_level == 'B':
            self.app.event_selected = 'B'
            self.app.placing_list = self.app.b
        if event_level == 'C':
            self.app.event_selected = 'C'
            self.app.placing_list = self.app.c
        if event_level == 'D':
            self.app.event_selected = 'D'
            self.app.placing_list = self.app.d
        if event_level == 'E':
            self.app.event_selected = 'E'
            self.app.placing_list = self.app.e
        if event_level == 'F':
            self.app.event_selected = 'F' 
            self.app.placing_list = self.app.f   
#-------------------------------------Placing------------------------------------------------------------
class PlacingDropDown(MDRaisedButton):
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        super().__init__(**kwargs)
    
    def generate_placing(self):
        menu_items = [
            {
                "viewclass": "MDMenuItem",
                "text": item,
            }
            for item in self.app.placing_list
        ]
        return menu_items

    def open_placing_dropdown(self):
        
        built_items = self.generate_placing()
        MDDropdownMenu(callback=self.placing_callback, caller=self, items=built_items, width_mult=3).open()

    def placing_callback(self, instance):
        placing = instance.text
        if placing == '1st':
            self.app.placing_selected = 1
        if placing == '2nd':
            self.app.placing_selected = 2
        if placing == '3rd':
            self.app.placing_selected = 3
        if placing == '4th':
            self.app.placing_selected = 4
        if placing == '5th':
            self.app.placing_selected = 5
        if placing == '6th':
            self.app.placing_selected = 6
        if placing == '7th':
            self.app.placing_selected = 7
        if placing == '8th':
            self.app.placing_selected = 8
        if placing == '9th':
            self.app.placing_selected = 9
        if placing == '10th':
            self.app.placing_selected = 10
        if placing == '11th':
            self.app.placing_selected = 11
        if placing == '12th':
            self.app.placing_selected = 12
        if placing == '13th':
            self.app.placing_selected = 13
        if placing == '14th':
            self.app.placing_selected = 14
        if placing == '15th':
            self.app.placing_selected = 15
        if placing == '16th':
            self.app.placing_selected = 16
        
class PlacingScore(MDRaisedButton):
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        super().__init__(**kwargs)
    
    def print_event(self):
        if self.app.event_selected == None:
            return None
        if self.app.placing_selected == None:
            return None
        else:
            self.app.get_placing_points()
            print(self.app.placing_points) 

class WindTextField(MDTextField):
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        super().__init__(**kwargs)

class EnterWind(MDRaisedButton):
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        super().__init__(**kwargs)

    def wind(self):
        wind_entered = self.app.root.ids.windtextfield.text
        if wind_entered == '':
            return None
        else:
            self.app.wind = wind_entered
            self.app.get_wind_modification()

class WindMod(MDRaisedButton):
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        super().__init__(**kwargs) 

    def print_wind_mod(self):
        if self.app.wind == '':
            return None
        else:
            print(self.app.wind_modification)

class PerformanceScore(MDRaisedButton):
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        super().__init__(**kwargs)
    
    def display_performance_score(self):
        if self.app.result_score == None:
            return None
        if self.app.placing_points == None:
            return None
        if self.app.wind_modification == None:
            score = (self.app.result_score + self.app.placing_points)
            print(score)
        else:
            score = (self.app.result_score + self.app.placing_points + self.app.wind_modification)
            print(score)

class MyCheckbox(IRightBodyTouch, MDCheckbox):
    pass


class MyAvatar(ILeftBody, Image):
    pass

class EventTextSearch(MDTextField):
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        super().__init__(**kwargs)

    def repopulate_event_list(self):
        if len(self.app.root.ids.event_search.text) == 0:
            return None
        else:
            events = self.app.events
            event_sel = self.app.root.ids.event_search.text
            matching_events = [i for i in events if event_sel in i]
            self.app.root.ids.MainScreenManager.screens[3].children[1].ids.scroll.clear_widgets()
            if event_sel == "":
                for event in events:
                    self.app.root.ids.MainScreenManager.screens[3].children[1].ids.scroll.add_widget(Factory.ListItemWithCheckbox(text=event))
            else:
                for event in matching_events:
                    self.app.root.ids.MainScreenManager.screens[3].children[1].ids.scroll.add_widget(Factory.ListItemWithCheckbox(text=event))
            
            
class EventListScreen(BoxLayout):
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        super().__init__(**kwargs)
        
    def populate_event_list(self):
        events = self.app.events
        for event in events:
            self.ids.scroll.add_widget(Factory.ListItemWithCheckbox(text=event))

class TrackingScreen(Screen):
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        super().__init__(**kwargs)

        

if __name__ == "__main__":
    my_app = MainApp()
    my_app.run()
    
    
    
    