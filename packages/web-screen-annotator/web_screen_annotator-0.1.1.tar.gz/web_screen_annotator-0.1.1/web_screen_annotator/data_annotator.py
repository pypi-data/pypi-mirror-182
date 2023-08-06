from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import json
from PIL import Image
from .dom_element import DomElement
from .dom_extractor import dom_extractor
from webdriver_manager.chrome import ChromeDriverManager
from PIL import  ImageDraw
import time

colors = {
        "button" : "green",
        "input"  : "blue",
        "img"    : "orange",
        "other"  : "red"
    }

class DataAnnotator():

    def __init__(self,urls,depth = 0):
        self.site_urls  = urls
        self.depth = depth

    def tag_class_mapper(tag):
        if "button" in tag or tag == "a":
            return "button"
        if "input" in tag:
            return "input"
        if "img" in tag:
            return "img"
        return "other"

    def get_element_list(element,list_of_elements):
        for child in element.children:
            DataAnnotator.get_element_list(child,list_of_elements)
        tag = element.tag
        if tag not in ["div", "form","section","body"]:
            bboxe = (element.left, element.top, element.left + element.width, element.top + element.height)
            item = {}
            item["tag"] = DataAnnotator.tag_class_mapper(tag)
            item["bb"] = bboxe
            item["id"] = element.id
            list_of_elements.append(item)
        return list_of_elements

    def draw_elements(list_of_elements,image_path):
        image = Image.open(image_path)
        for item in list_of_elements:
            tag = item["tag"]
            outline = colors[tag]
            imdraw = ImageDraw.Draw(image)
            imdraw.rectangle(item["bb"], outline = outline)
        return image

    def get_dom_and_screenshot(site_url,path):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(site_url)
        time.sleep(1)
        raw_dom = driver.execute_script(dom_extractor)
        dom = DomElement(raw_dom)
        image_path = os.path.join(path,"image.png")
        driver.save_screenshot(image_path)
        driver.close()
        return dom , image_path
    

    def execute(self,viz = False):
        cwd = os.getcwd()
        data_path = os.path.join(cwd,"data") 
        try :
            os.mkdir(data_path)
        except:
            print("some data may be overrided.")
        for i in range(len(self.site_urls)):
            site_url = self.site_urls[i]
            path = os.path.join(data_path,"site_nb_"+str(i))
            try :
                os.mkdir(path)
            except:
                print("overriding data for site number",i)
            
            dom, image_path= DataAnnotator.get_dom_and_screenshot(site_url,path)
            list_of_elements = []
            list_of_elements = DataAnnotator.get_element_list(dom,list_of_elements)

            # vizualization
            if viz :
                image = DataAnnotator.draw_elements(list_of_elements,image_path)
                image.save(os.path.join(path,"bboxes.png"))
            #save json for bounding boxes  
            with open(os.path.join(path,"bboxes.json"), "w") as outfile:
                json.dump(list_of_elements, outfile)
        print("completed")