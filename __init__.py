from modloader import modast, modinfo
from modloader.modclass import Mod, loadable_mod
import jz_magmalink as ml
import renpy.ast as ast
import renpy.parser as parser

@loadable_mod
class sqbremy(Mod):
    name = "Horny Remy Mod"
    version = "0.1"
    author = "squarebells"
    dependencies = ["MagmaLink","CRAP", "BangOk"]
    nsfw = True
    
    @classmethod
    def mod_load(cls):
         sqb1remy(ml)
         
    @staticmethod
    def mod_complete():
        pass
          
def sqb1remy(ml):
    
      ml.find_label("remyoffmenu") \
          .search_menu("Rummage through his trash.").branch() \
          .hook_to("sqb_remy_m1_trash", condition='persistent.nsfwtoggle == True') \
          
      ml.find_label("remyoffmenu") \
          .search_menu("Look at his computer.").branch() \
          .search_say("(I wonder if their computers") \
          .hook_to("sqb_remy_m1_start", condition='persistent.nsfwtoggle == True and bangok_four_playerhasdick == None or False') \
          .search_scene("black") \
          .link_from("sqb_remy_m1_end") \
          .search_say("When I have to work late", depth=400) \
          .link_from("sqb_remy_m1_fail")