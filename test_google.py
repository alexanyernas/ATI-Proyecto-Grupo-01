from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Creamos una nueva sesion en Chrome
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.maximize_window()

# Navegamos a la pagina principal de Google
driver.get("http://www.google.com")

# Obtenemos el id del cuadro de busqueda y lo limpiamos
search_field = driver.find_element_by_id("lst-ib")
search_field.clear()

# Realizamos una busqueda
search_field.send_keys("Realizando una busqueda desde Google :D")
search_field.submit()

# Obtenemos la lista de elementos cuya clase posee este nombre (enlaces)
lists = driver.find_elements_by_class_name("rc")

# Imprimimos el numero de elementos encontrados
print ("Encontradas " + str(len(lists)) + " busquedas:")

# Iteramos sobre cada elemento e imprimimos su valor
i = 0
for listitem in lists:
	print ("Item "+str(i))
	print (listitem.text)
	i = i+1
	if(i>10):
		break
driver.implicitly_wait(100)
# close the browser window
driver.quit()