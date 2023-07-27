import pyautogui
import webbrowser
from time import sleep
import random

class Bot():
    
    def abrir_web(site):
        webbrowser.open(site)
        sleep(2)
    
    def login(usuario, senha):
        # usuario
        login_usuario = pyautogui.locateCenterOnScreen('usuario.png')
        if login_usuario == None:
            pyautogui.click(1397,328, duration=0.2)
        else:
            pyautogui.click(login_usuario[0],login_usuario[1], duration=0.4)

        sleep(0.4)
        pyautogui.typewrite(usuario)
        # senha
        pyautogui.press('tab')
        sleep(0.1)
        pyautogui.typewrite(senha)
        entrar = pyautogui.locateCenterOnScreen('entrar.png')
        pyautogui.click(entrar[0],entrar[1], duration=0.4)
        sleep(4)
        
        # nao salvar info de login
    def info_login():
        sleep(1)
        
        info_login = pyautogui.locateCenterOnScreen('salvar_info.png')
        
        if info_login != None:
            pyautogui.click(info_login[0],info_login[1], duration=0.4)
        else: 
            pass
        
        sleep(2)

    def pesquisar_perfil(perfil):
        sleep(2)
        pyautogui.click(999,279, duration=0.2)
        sleep(0.3)
        pyautogui.typewrite(perfil)
        
        
        nike = pyautogui.locateCenterOnScreen('nike.png')
        if nike == None:
            sleep(0.2)
            pyautogui.press('tab')
            sleep(0.3)
            pyautogui.press('tab')
            sleep(0.3)
            pyautogui.press('enter')
        else:
            pyautogui.click(nike[0],nike[1], duration=0.4)
    sleep(4)
    
    def curtir_comentar_3_em_3(quantidade):
        
        # scroll
        sleep(3)
        pyautogui.scroll(-60)

        for i in range(quantidade):
           
             # imagem coluna 1            
            for x in range(1):
                sleep(0.4)
                pyautogui.click(1178,711, duration=0.4)
                sleep(2)

                comentarios =  ['simplesmente lindo','amei!','otimo','eu gostei','muito bem feito','incrivel','muito legal','hahaha','parabens','ai sim!', 'que lindo','sonho!']
                comentarios_random = random.choice(comentarios)

                # procura coracao pra dar like e comentar
                coracao = pyautogui.locateCenterOnScreen('coracao.png')
                if coracao != None:
                    pyautogui.click(coracao[0],coracao[1],duration=0.4)
                    pyautogui.press('c')
                    sleep(1)
                    pyautogui.write(comentarios_random, interval=0.15)
                    pyautogui.press('enter')
                    sleep(2)
                    pyautogui.click(1821,105, duration=0.4)
                else:
                    pyautogui.click(1821,105, duration=0.4)
                
            for y in range(1):
                # imagem coluna 2
                sleep(1)
                pyautogui.click(1436,711,duration=0.4)
                sleep(2)

                comentarios =  ['simplesmente lindo','amei!','otimo','eu gostei','muito bem feito','incrivel','muito legal','hahaha','parabens','ai sim!', 'que lindo','sonho!']
                comentarios_random = random.choice(comentarios)

                # procura coracao pra dar like e comentar
                coracao = pyautogui.locateCenterOnScreen('coracao.png')
                if coracao != None:
                    pyautogui.click(coracao[0],coracao[1],duration=0.4)
                    pyautogui.press('c')
                    sleep(1)
                    pyautogui.write(comentarios_random, interval=0.15)
                    pyautogui.press('enter')
                    sleep(2)
                    pyautogui.click(1821,105, duration=0.4)
                else:
                    pyautogui.click(1821,105, duration=0.4)

            for z in range(1):
                # imagem coluna 3
                sleep(1)
                pyautogui.click(1715,711,duration=0.4)
                sleep(2)

                comentarios =  ['simplesmente lindo','amei!','otimo','eu gostei','muito bem feito','incrivel','muito legal','hahaha','parabens','ai sim!', 'que lindo','sonho!']
                comentarios_random = random.choice(comentarios)

                # procura coracao pra dar like e comentar
                coracao = pyautogui.locateCenterOnScreen('coracao.png')
                if coracao != None:
                    pyautogui.click(coracao[0],coracao[1],duration=0.4)
                    pyautogui.press('c')
                    sleep(1)
                    pyautogui.write(comentarios_random, interval=0.15)
                    pyautogui.press('enter')
                    sleep(2)    
                    pyautogui.click(1821,105, duration=0.4)
                else:
                    pyautogui.click(1821,105, duration=0.4)

            
            # abaixar tela scroll loop
            sleep(1)
            for i in range(1):
                pyautogui.scroll(-219)
                sleep(2)


Bot.abrir_web('https://www.instagram.com/accounts/login/?source=auth_switcher')
Bot.login(usuario='',senha='') # somente nome, sem email ou numero
Bot.info_login() # salvar informacoes de login no navegador ? se nao aparecer a pergunta no site, pode desconsiderar esta funcao
Bot.pesquisar_perfil(perfil='') # selecionar perfil
Bot.curtir_comentar_3_em_3(quantidade='') # selecionar quantidade de vezes para repetir (apenas numeros inteiros)
