import pyautogui
import time

def wait_for_image(image_path, confidence=0.7, delay=5):
    while True:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=confidence)
            if location is not None:
                return location
            print(f"Image not detected : {image_path}. New try in {delay} sec.")
            time.sleep(delay)
        except Exception as e:
            print(f"Searching image : {e}")
            time.sleep(delay)

def click_image(image_location):
    pyautogui.click(image_location)
    print(f"Image clicked : {image_location}")



times = int(input("How many times do you want the script to clear the prime event? "))
auto_stamina = input("Enable auto stamina? (Y/N): ")

auto_stamina = auto_stamina.lower() == "y"

time.sleep(5)
print('Searching Start button...')   
bouton_start_location = wait_for_image('./Assets/PRIME_START.PNG')
click_image(bouton_start_location)

for i in range(times):

    time.sleep(5)
    print("Recherche du bouton restart...")
    restart_button = wait_for_image('./Assets/RESTART.PNG')
    click_image(restart_button)
    time.sleep(1)
    pyautogui.click(x=1060, y=640)

    if auto_stamina == 'y':
        try:
            print("Searching Stamina...")
        
            sta_meat_location = wait_for_image('./Assets/STA.PNG')
        
            if sta_meat_location is not None:
                sta_positions = [(1085, 640), (1060, 710), (1085, 640)]
            
                for pos in sta_positions:
                    pyautogui.click(x=pos[0], y=pos[1])
                    print(f"Clicked stamina {pos}")
                    time.sleep(1)  
        except Exception as e:
            print(f"Error while searching stamina : {e}")
            pass


    time.sleep(5)
    print('Searching Start button...')   
    bouton_start_location = wait_for_image('./Assets/PRIME_START.PNG')
    click_image(bouton_start_location)
