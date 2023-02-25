from itertools import count
from random import choice, randint
from selenium.webdriver.common.keys import Keys
import keyboard, os, warnings, pwinput
from selenium import webdriver as wd
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By  
from time import sleep
with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)

class InstaGiario_bot:
    # Inicializa
    def __init__(self, user, passw):
        self.username = user
        self.password = passw
        chromeOptions = wd.ChromeOptions()
        chromeOptions.add_argument('--user-data-dir=C:\\Users\\lanin\\OneDrive\\Documentos\\Google Chrome Profile ') #Adicione a pasta do perfil do chrome
        chromeOptions.add_argument('--profile-directory=Profile 3') # Especifique o perfil    
        chromeOptions.add_argument('--disable-gpu')
        self.driver = wd.Chrome(options = chromeOptions)
    # Faz Login
    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        print (f'Bot:', self.driver.execute_script('return navigator.webdriver'))
        sleep(randint(4, 8))
        try:
            driver.find_element(By.XPATH, "//input[@name='username']")
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
            sleep(randint(1, 6)) # Tempo para iniciar a pŕoxima etapa. 

            self.Comment_Post()
        except NoSuchElementException:
            self.Comment_Post()    
    # Cronometro para bloqueios    
    def countdown_block(self):   
        t = (randint(1200, 2400))
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            if keyboard.is_pressed("esc"):           
                print ('Contador interrompido!')
                break
            else:
                print("Bloqueado, aguarde: " + timer, "           ", end="\r")
                sleep(1)
                t -= 1
    # Cronometro para comentários
    def comment_countdown(self):
    
        t = (randint(10,45))
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print("Comentando em: " + timer, "           ", end="\r")
            sleep(1)
            t -= 1    
    # Contador de bloqueios
    def blocks_count(self, a):
        global count
        if (a == 0):
            count += 1
            return count
        elif (a == 1):
            count -= 1
            return count  
    # Verifica se a conta foi bloqueada ou não
    def block_or_not(self, u, quem):
        global count
        driver = self.driver
        print('Bloqueio detectado.', end ="\r")
        if (count == 5):
            self.countdown_block(3600, 7200)
            count = int(4) 
        else:
            self.countdown_block(600, 1800)
        driver.find_element(By.CLASS_NAME, "_aacl._aaco._aacw._aad0._aad6._aade").click() # Publica a postagem. 
        sleep(1) 
        try: # Procura Bloqueios
            driver.find_element(By.XPATH, "//p[@class='_abmp' and contains(text(),'Não foi possível publicar o comentário')]") # Procura possivel bloqueio  
            print('Possivel bloqueio detectado!', end ="\r")
            sleep (1)
            if (driver.find_element(By.CLASS_NAME, "_acan._acao._acas").is_enabled() == True):
                self.blocks_count(0)
                print ('-----------Bloqueio - 1-----------')      
                self.block_or_not(u, quem)  
            else:   
                print("Conta liberada!             ")
                self.blocks_count(1)                
                print(f'Comentários postados: {u} ({quem})              ')  
        except NoSuchElementException:        
            try:    
                driver.find_element(By.CLASS_NAME, "_a9-v") # Procura possivel bloqueio                                  
                sleep(1)
                driver.find_element(By.CLASS_NAME, "_a9--._a9_0").click() # Relata problema de bloqueio                          
                self.blocks_count(0)
                print ('-----------Bloqueio - 2-----------')                
                self.block_or_not(u, quem)
            except NoSuchElementException:
                print("Conta liberada!             ")
                self.blocks_count(1)
                print(f'Comentários postados: {u} ({quem})              ')
    # Verifica se deseja comentar mais vezes
    def more_comment(self, pessoas, lista_comentários_2):
        driver = self.driver
        mais_input_comentarios = int(input('Digite (1) se deseja comentar mais vezes e (2) para encerrar: ')) # Define se encerra ou reinicia o programa.
        if (int(mais_input_comentarios == 1)):
            num_comentários = int(input('Digite o número de comentários que deseja realizar: '))
            self.commenting(num_comentários, pessoas, lista_comentários_2) 
        elif (int(mais_input_comentarios == 2)):
            print ('Encerrando programa...')
            driver.close()
            exit()
    # Digita letra por letra      
    @staticmethod
    def digitação(frase, coment1): 
        for letra in frase:
            coment1.send_keys(letra)
            sleep(randint(4, 8) / 30)
    # Recebe o link da postagem             
    def Comment_Post(self):
        driver = self.driver
        os.system('cls') 
        print (logo)
        link_postagem = str(input('Insira o link da postagem: '))
        driver.get(f'{link_postagem}') # Link da postagem que receberá os input_comentarios.
        self.comment_choice()
    # Escolhe os comentários da lista
    def comment_choice(self):
        sleep(randint(3, 4))
        os.system('cls')
        print (logo)
        print (f'Fez login como: @{self.username}') 
        print(f'Comentando em: {self.driver.title}') 
        lista_comentários = ['Comentário1', 'Comentário2', 'Comentário3', 'Comentário4', 'Comentário5']        
        num_comentários = int(input('Digite o número de comentários que deseja realizar: '))
        num_pessoas = int(input('Digite o número pessoas a serem marcadas por comentário: '))
        print ('Iniciando Comentários...')      
        pessoas = int(num_pessoas)
        lista_comentários_2 = lista_comentários 
        self.commenting(num_comentários, pessoas, lista_comentários_2) 
    # Efetua os comentários    
    def commenting(self, num_comentários, pessoas, lista_comentários_2):
        driver = self.driver
        for u in range(1, num_comentários + 1): # numero de comentários 
            driver.find_element(By.XPATH, "//*[name()='textarea' and @aria-label='Adicione um comentário...']").click() # Clica em "Comentário"
            input_comentario = driver.find_element(By.XPATH, "//*[name()='textarea' and @aria-label='Adicione um comentário...']")          
            submit_comment_selector = ("x1i10hfl.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x1lku1pv.x1a2a7pz.x6s0dn4.xjyslct.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x9f619.x1ypdohk.x1i0vuye.xwhw2v2.xl56j7k.x17ydfre.x1f6kntn.x2b8uid.xlyipyv.x87ps6o.x14atkfc.x1d5wrs8.x972fbf.xcfux6l.x1qhh985.xm0m39n.xm3z3ea.x1x8b98j.x131883w.x16mih1h.xt0psk2.xt7dq6l.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.xjbqb8w.x1n5bzlp.x173jzuc.x1yc6y37")
            submit_button = driver.find_element(By.CLASS_NAME, submit_comment_selector)

            sleep(1)
            input_comentario.send_keys(Keys.CONTROL + "a") # Seleciona texto da caixa "Comentários"
            input_comentario.send_keys(Keys.DELETE) # Limpa a caixa "Comentários"
            sleep(randint(1, 3))
            print("Comentando agora!               ", end="\r")
                
            for i in range(1, pessoas + 1 ):                
                if len(lista_comentários_2) != 0:
                    quem = (choice(lista_comentários_2))
                    self.digitação(quem, input_comentario) # Digita o comentário no campo
                    self.digitação((" "), input_comentario) # Digita o comentário no campo
                    lista_comentários_2.remove(quem) #Remove possível repeticão
                    if len(lista_comentários_2) == 0: 
                        driver.find_element(By.XPATH, "//*[name()='textarea' and @aria-label='Adicione um comentário...']").send_keys(Keys.ENTER)
                        new_list = str(input('Nova Lista aqui:')) # Lista deve ser colocada com espacos separando os comentários
                        comentários_3 = new_list.split()  #Testar com lista_comentários_2 = new_list.split()
                        for u in range(pessoas - i): #Apagar se o teste validar
                            if len(comentários_3) != 0:
                                quem = (choice(comentários_3))
                                self.digitação(quem, input_comentario) # Digita o comentário no campo
                                self.digitação((" "), input_comentario) # Digita o comentário no campo
                                comentários_3.remove(quem) #Remove possível repeticão da nova lista
                            else:
                                break

            sleep(randint(1, 6))
            submit_button.click()
            print("Publicando agora!               ", end="\r")
            sleep(randint(1, 2))
            try: # Procura Bloqueios
                driver.find_element(By.XPATH, "//p[@class='_abmp' and contains(text(),'Não foi possível publicar o comentário')]") # Procura possivel bloqueio  
                print('Possivel bloqueio detectado!', end ="\r")            
                if (driver.find_element(By.CLASS_NAME, "_acan._acao._acas").is_enabled() == True):
                    self.blocks_count(0)
                    print ('-----------Bloqueio - 1-----------')
                    self.block_or_not(u, quem)  
                else:   
                    print("Conta liberada!             ")
                    self.blocks_count(1)
                    print(f'Comentários postados: {u} ({quem})              ')                                         
            except NoSuchElementException: 
                try: 
                    driver.find_element(By.CLASS_NAME, "_a9-v") # Procura possivel bloqueio                                  
                    sleep(1)
                    driver.find_element(By.CLASS_NAME, "_a9--._a9_0").click() # Relata problema de bloqueio
                    self.blocks_count(0)
                    print ('-----------Bloqueio - 2-----------')
                    self.block_or_not(u, quem)                                        
                except NoSuchElementException:                            
                    print(f'Comentários postados: {u} ({quem})              ')
                   
                if (int(u != num_comentários)):
                    self.comment_countdown()               
                else: 
                    print(f'Todos os comentários foram realizados.\n')
                    self.more_comment(pessoas, lista_comentários_2)          
                                               
os.system('cls')
logo = (r"""
  _____           _         _____ _   __       _       
 |_   _|         | |       / ____(_) /_/      (_)      
   | |  _ __  ___| |_ __ _| |  __ _  __ _ _ __ _  ___  
   | | | '_ \/ __| __/ _` | | |_ | |/ _` | '__| |/ _ \ 
  _| |_| | | \__ \ || (_| | |__| | | (_| | |  | | (_) |
 |_____|_| |_|___/\__\__,_|\_____|_|\__,_|_|  |_|\___/ 
                                                       
""")
print (logo)
usuario = (input('Digite o Usuário: '))
senha = pwinput.pwinput(prompt = 'Digite sua senha: ')   
count = int(0)
InstaGiario_bot = InstaGiario_bot(usuario, senha) 
InstaGiario_bot.login()

#Bloqueio 1 - Tarja preta
#Bloqueio 2 - Informado pelo intagram
