from tkinter import E
from random import choice, randint, random
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By  
from time import sleep
import random
import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)

class InstaGlowUpBot:
    def __init__(self, user, passw):
        self.username = user
        self.password = passw
        user_agent_list = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36/8mqULwuL-67", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36/8mqPtVuL-9", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Agency/90.8.1597.98", "Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4870.181 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36/8mqEpSuL-47", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36/0cqIF4Ef-13", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4859.172 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0. 4844.82 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4864.133 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/0ADF80FA", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2700.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2696.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4698.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36 GLS/97.10.6229.30", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Config/95.2.8641.42", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 AtContent/93.5.2274.75", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Config/96.2.9111.12", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36 GLS/95.10.1539.40", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36/8mqXoXuL-32", "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.114 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36(KHTML,likeGecko) Chrome/98.0.4758.82 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.9 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4753.0 Safari/537.36"]
        user_agent = random.choice(user_agent_list)
        options = webdriver.ChromeOptions()
        # specify the desired user agent
        options.add_argument(f'user-agent={user_agent}')
        self.driver = webdriver.Chrome(chrome_options=options)
       
    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        sleep(randint(3, 8))

        usuário = driver.find_element(By.XPATH, "//input[@name='username']")
        usuário.click() # Clica em usuário.
        usuário.clear() # Limpa a caixa de usuário.
        usuário.send_keys(self.username) # Digita o usuário informada.

        senha = driver.find_element(By.XPATH, "//input[@name='password']")
        senha.click() # Clica em senha
        senha.clear() # Limpa a caixa de senha
        senha.send_keys(self.password) # Digita a senha.
        sleep(randint(1, 4))
        senha.send_keys(Keys.RETURN) # "Enter".
        sleep(randint(1, 6)) # Tempo para iniciar a pŕixima etapa. 

        self.CommentPost()   

    def more_comment(self):
        driver = self.driver
        mais_comentarios = int(input('Digite (1) se deseja comentar mais vezes e (2) para encerrar. ')) # Define se encerra ou reinicia o programa.
        if (int(mais_comentarios == 1)):
            self.escolha()
        elif (int(mais_comentarios == 2)):
            print ('Encerrando programa...')
            driver.close()
            exit()
            
    @staticmethod
    def digitação(frase, coment1): # Digita letra por letra
        for letra in frase:
            coment1.send_keys(letra)
            sleep(randint(4, 8) / 30)
            
    def CommentPost(self):
        driver = self.driver
        sleep(randint(2, 4))
        link_postagem = str(input('Insira o link da postagem: '))
        driver.get(f'{link_postagem}') # Link da postagem receberá os comentarios. 
       
        self.escolha()

    def escolha(self):
        driver = self.driver
        sleep(randint(3, 4))    
        comentários = ['comentario1','comentario2','comentario3'] # Lista de comentários
        num_comentários = int(input('Digite o número de comentários que deseja realizar: ')) 
        num_pessoas = int(input('Digite o número pessoas a serem marcadas por comentário (1) ou (2): '))
        print ('\n\n')
        print ('Iniciando Comentários...')      
        pessoas = int(num_pessoas) 

    
        if (int(pessoas == 1)):
            for u in range(1, num_comentários + 1): # numero de comentarios a ser realizados 
                driver.find_element(By.CLASS_NAME, "_ablz._aaoc").click() # Clica em "Comentário"
                comentario = driver.find_element(By.CLASS_NAME, "_ablz._aaoc")
                sleep(randint(2, 6))

                self.digitação(choice(comentários), comentario) # Digita o comentário no campo
                sleep(randint(3, 9))

                driver.find_element(By.CLASS_NAME, "_aacl._aaco._aacw._aad0._aad6._aade").click() # Publica a postagem.
                sleep(randint(1, 2))
                try: 
                    driver.find_element(By.XPATH, "//p[@class='_abmp']") # Procura possivel bloqueio
                    print('Possivel bloqueio detectado.')
                    encerrar = int(input('Deseja tentar novamente? (1)Sim (2)Não: '))
                    if (encerrar == 1):
                        driver.find_element(By.CLASS_NAME, "_aacl._aaco._aacw._aad0._aad6._aade").click() # Publica a postagem.
                        sleep(randint(1, 2))
                        try: 
                            driver.find_element(By.XPATH, "//p[@class='_abmp']") # Procura possivel bloqueio novamente após tentar novamente publicar.
                            print('Bloqueio detectado!\nEncerrando programa!') # Se encotrado bloqueio após segunda tentativa, encerra o programa.
                            driver.close()
                            exit()
                        except NoSuchElementException:
                            print(f'Comentários postados: {u}')
                    else:
                        print ('Encerrando programa!')   
                        driver.close()
                        exit()
                except NoSuchElementException: 
                    print(f'Comentários postados: {u}')

                if (int(u != num_comentários)):
                    sleep(randint(30, 60))
                else: 
                    print(f'Todos os comentários foram realizados.\n\n')
                    self.more_comment()          
        
        elif (int(pessoas == 2)):
                
            for u in range(1, num_comentários + 1): # numero de comentarios 
                driver.find_element(By.CLASS_NAME, "_ablz._aaoc").click() # Clica em "Comentário"
                comentario = driver.find_element(By.CLASS_NAME, "_ablz._aaoc")
                sleep(randint(4, 9))

                self.digitação(choice(comentários), comentario) # Digita o comentário no campo
                sleep(randint(3, 8))
                self.digitação((" "), comentario) # Digita espaco no campo
                sleep(randint(1, 3))
                self.digitação(choice(comentários), comentario) # Digita o comentário no campo
                sleep(randint(4, 10)) 
                
                driver.find_element(By.CLASS_NAME, "_aacl._aaco._aacw._aad0._aad6._aade").click() # Publica a postagem.
                sleep(randint(1, 2))
                try: 
                    driver.find_element(By.XPATH, "//p[@class='_abmp']")
                    print('Possivel bloqueio detectado.\n Encerrando programa!')
                    encerrar = int(input('Deseja tentar novamente? (1)Sim (2)Não: '))
                    if (encerrar == 1):
                        driver.find_element(By.CLASS_NAME, "_aacl._aaco._aacw._aad0._aad6._aade").click() # Publica a postagem.
                        sleep(randint(1, 2))
                        try: 
                            driver.find_element(By.XPATH, "//p[@class='_abmp']") # Procura possivel bloqueio após tentar novamente.
                            print('Bloqueio detectado!\nEncerrando programa!') # Se encotrado bloqueio após segunda tentativa, encerra o programa.
                            driver.close()
                            exit()
                        except NoSuchElementException:
                            print(f'Comentários postados: {u}')                            
                    else:
                        print ('Encerrando programa!')                          
                        driver.close()
                        exit()
                except NoSuchElementException: 
                    print(f'Comentários postados: {u}')

                if (int(u != num_comentários)):
                    sleep(randint(25, 62))
                else: 
                    print(f'Todos os comentários foram realizados.\n\n')
                    self.more_comment()
                
                                    
        else:
            print ('Ainda não temos essa funcionalidade. Em breve!')
            print ('Redirecionando...')
            self.escolha()
     
InstaGlowUpBot = InstaGlowUpBot('usuario', 'senha') # Adicione aqui o seu usuário e senha.
InstaGlowUpBot.login()
