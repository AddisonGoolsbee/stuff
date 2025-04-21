from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

minerals = [
    "quartz",
    "microcline",
    "sanidine",
    "orthoclase",
    "plagioclase",
    "sodalite",
    "nepheline",
    "scapolite",
    "leucite",
    "zeolite",
    "olivine",
    "garnet",
    "kyanite",
    "sillimanite",
    "andalusite",
    "staurolite",
    "zircon",
    "sphene",
    "topaz",
    "orthopyroxene",
    "clinopyroxene",
    "omphacite",
    "wollastonite",
    "actinolite",
    "glaucophane",
    "hornblende",
    "tremolite",
    "anthophyllite",
    "muscovite",
    "biotite",
    "serpentine",
    "talc",
    "margarite",
    "chlorite",
    "lepidolite",
    "lawsonite",
    "clinozoisite-epidote",
    "zoisite",
    "beryl",
    "tourmaline",
    "cordierite",
    "graphite",
    "diamond",
    "gold",
    "silver",
    "copper",
    "sulfur",
    "iron",
    "pyrite",
    "marcasite",
    "chalcopyrite",
    "sphalerite",
    "galena",
    "rutile",
    "corundum",
    "magnetite",
    "hematite",
    "goethite",
    "halite",
    "fluorite",
    "apatite",
    "calcite",
    "aragonite",
    "dolomite",
    "siderite",
    "rhodochrosite",
    "malachite",
    "azurite",
    "gypsum",
    "barite",
]

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


for mineral in minerals:
    query = f"mindat {mineral} gallery"
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get("https://www.google.com")
    time.sleep(1)

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query + Keys.RETURN)
    time.sleep(2)

    results = driver.find_elements(By.CSS_SELECTOR, "a h3")
    if results:
        results[0].click()
    time.sleep(2)

# Optional: Keep browser open
input("Press Enter to close all tabs...")
driver.quit()
