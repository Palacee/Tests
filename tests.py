import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
'''
def list_reverse(arr,size):
 
    #if only one element present, then return the array
    if(size==1):
        return arr
     
    #if only two elements present, then swap both the numbers.
    elif(size==2):
        arr[0],arr[1],=arr[1],arr[0]
        return arr
     
    #if more than two elements presents, then swap first and last numbers.
    else:
        i=0
        while(i<size//2):
 
    #swap present and preceding numbers at time and jump to second element after swap
            arr[i],arr[size-i-1]=arr[size-i-1],arr[i]
       
    #skip if present and preceding numbers indexes are same
            if((i!=i+1 and size-i-1 != size-i-2) and (i!=size-i-2 and size-i-1!=i+1)):
                arr[i+1],arr[size-i-2]=arr[size-i-2],arr[i+1]
            i+=2
        return arr
 
a=[]
n=int(input("Number of elements in array:"))
for i in range(0,n):
   l=int(input())
   a.append(l)


print('Original list: ',a)
print("Reversed list: ",list_reverse(a,n))
'''

url = "https://www.google.com/search?q=1"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(0.2)
driver.get(url)


try:
    driver.find_element(By.CLASS_NAME, "logo")
    print("Logo Encontrado")
except:
    print("Elemento no encontrado")


try:
    query = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')

except:
    print("TextArea no encontrada")

query.click()
query.clear()

search_query = "youtube"

query.send_keys(search_query)
query.send_keys(Keys.RETURN)

validation = driver.find_element(By.XPATH, '//*[@id="APjFqb"]').text

if validation == search_query:
    print("Validado el texto")

