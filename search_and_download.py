from selenium import webdriver
import os
from get_image_links import DRIVER_PATH
from get_image_links import fetch_image_urls
from links_to_directory import persist_image


def search_and_download(search_term: str, number_images=1):
    target_folder = "C:/Users/canad/Documents/iPhoneDataSets/iPhone5"

    if not os.path.exists(target_folder):
        print("Exception: No such file path")
        return

    with webdriver.Chrome(executable_path=DRIVER_PATH) as wd:
        res = fetch_image_urls(search_term, number_images, wd=wd)

    for elem in res:
        persist_image(target_folder, elem)


search_and_download('iphone 5 back')
