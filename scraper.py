import csv
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

# Open the csv file and write the header row
with open('recruits.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['ranking', 'name', 'high_school', 'position', 'height_weight', 'stars', 'composite_score',
                     'college', 'year'])

    # For loop that accesses the url for years 2008-2023
    for year in range(2008, 2024):
        url = f'https://247sports.com/Season/{year}-Football/CompositeRecruitRankings/?InstitutionGroup=HighSchool/'
        print(url)
        driver.get(url)

        # Click 'Load More' button until the top 500 recruits are in view
        for _ in range(10):
            time.sleep(2)
            button = driver.find_element(By.CSS_SELECTOR, '.rankings-page__showmore > a')
            ActionChains(driver).move_to_element(button).click(button).perform()

        # Find all recruit elements on the page
        players = driver.find_elements(By.CLASS_NAME, 'rankings-page__list-item')

        # Loop through each element and assign the data to variables
        for player in players:
            ranking = player.find_element(By.CLASS_NAME, 'primary').text.strip()
            name = player.find_element(By.CLASS_NAME, 'rankings-page__name-link').text.strip()
            high_school = player.find_element(By.CSS_SELECTOR, '.recruit > span').text.strip()
            position = player.find_element(By.CLASS_NAME, 'position').text.strip()
            height_weight = player.find_element(By.CLASS_NAME, 'metrics').text.strip()
            rating = player.find_elements(By.CLASS_NAME, 'icon-starsolid.yellow')
            stars = len(rating)
            composite_score = player.find_element(By.CLASS_NAME, 'score').text.strip()
            try:
                college_img = player.find_element(By.CSS_SELECTOR, '.img-link > img')
                college = college_img.get_attribute('alt')
            except NoSuchElementException as err:
                college = 'None'

            # Create new recruit
            recruit = [ranking, name, high_school, position, height_weight, stars, composite_score, college, year]

            # Write the new recruit to csv file
            writer.writerow(recruit)

            # The loop will run until all 4 and 5 stars have been saved
            if stars > 3:
                print(recruit)
            else:
                break
