from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

driver = webdriver.Firefox()
driver.get("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

# Login no Sistema
email_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@name='email']"))
)
email_field.click()
email_field.send_keys("dias@gmail")

password_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@name='password']"))
)
password_field.click()
password_field.send_keys("senha")

submit_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
)
submit_btn.click()

# Cadastro de produtos
table = pd.read_csv('produtos.csv')

for index, row in table.iterrows():

    code_field = driver.find_element(By.XPATH, "//input[@name='codigo']")
    code_field.send_keys(row['codigo'])

    product_brand_field = driver.find_element(By.XPATH, "//input[@name='marca']")
    product_brand_field.send_keys(row['marca'])

    product_type_field = driver.find_element(By.XPATH, "//input[@name='tipo']")
    product_type_field.send_keys(row['tipo'])

    product_category_field = driver.find_element(By.XPATH, "//input[@name='categoria']")
    product_category_field.send_keys(row['categoria'])

    unit_price_field = driver.find_element(By.XPATH, "//input[@name='preco_unitario']")
    unit_price_field.send_keys(row['preco_unitario'])

    product_cost_field = driver.find_element(By.XPATH, "//input[@name='custo']")
    product_cost_field.send_keys(row['custo'])

    if not pd.isna(row['obs']):
        obs_field = driver.find_element(By.XPATH, "//input[@name='obs']")
        obs_field.send_keys(row['obs'])
    
    submit_btn_form = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_btn_form.click()
