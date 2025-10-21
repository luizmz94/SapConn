""" SAP connection module """
import os
import glob
from os import path
import time
from threading import Thread
from connection.abstract_connection_type import AbstractConnectionType

class SapConnection(AbstractConnectionType):
    """ SAP connection class """

    KEY_CONN = "conn"
    KEY_CLNT = "clnt"
    KEY_USER = "user"
    KEY_LANG = "lang"
    KEY_GUI = "gui"
    FILE_NAME = "login.sapc"

    open_thread = ''
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    file_path = path.join(desktop, FILE_NAME)
    gui_version = None  # Armazena qual versão usar para essa conexão

    @property
    def args_template(self) -> dict:
        """ Returns a template for setup """
        return {
            SapConnection.KEY_CONN: "",
            SapConnection.KEY_CLNT: "",
            SapConnection.KEY_USER: "",
            SapConnection.KEY_LANG: "",
            SapConnection.KEY_GUI: "",  # Opcional: "7.8", "8.10", etc. Se vazio, usa padrão do Mac
        }

    def connect(self, args: dict, credential: str, account: str):
        """ Opens a connection to the system """
        # Armazena a versão especificada do SAP GUI (se houver)
        if SapConnection.KEY_GUI in args and args[SapConnection.KEY_GUI].strip():
            SapConnection.gui_version = args[SapConnection.KEY_GUI].strip()
        else:
            SapConnection.gui_version = None
            
        file_content = "conn=" + args[SapConnection.KEY_CONN]
        file_content += "&clnt=" + args[SapConnection.KEY_CLNT]
        file_content += "&user=" + account
        #file_content += "&user=" + args[SapConnection.KEY_USER]
        file_content += "&lang=" + args[SapConnection.KEY_LANG]
        file_content += "&expert=true&pass=" + credential

        
        #file_path = '/Users/luizcarloszanellamartins/Documents/SAPConn/kutapada-desktop/login.sapc'
        #file_path = path.join(os.getcwd(), SapConnection.FILE_NAME)
        with open(SapConnection.file_path, "w") as tmp_file:
           tmp_file.write(file_content)

        SapConnection.open_thread = Thread(target=self._open_connection_file)
        SapConnection.open_thread.start()

    def _find_sap_gui_by_version(self, version: str) -> str:
        """ Busca o caminho do SAP GUI pela versão especificada """
        base_path = "/Applications/SAP Clients"
        
        # Padrão de busca: SAPGUI seguido da versão
        search_pattern = f"{base_path}/SAPGUI {version}*"
        
        # Busca diretórios que começam com a versão especificada
        matching_dirs = glob.glob(search_pattern)
        
        if matching_dirs:
            # Pega o primeiro diretório encontrado e ordena (rev mais alto primeiro)
            matching_dirs.sort(reverse=True)
            sap_dir = matching_dirs[0]
            
            # Busca o arquivo .app dentro do diretório
            app_pattern = f"{sap_dir}/SAPGUI*.app"
            app_files = glob.glob(app_pattern)
            
            if app_files:
                return app_files[0]
        
        return None

    def _open_connection_file(self):
        #file_path = path.join(os.getcwd(), SapConnection.FILE_NAME)
        #file_path = '/Users/luizcarloszanellamartins/Documents/SAPConn/kutapada-desktop/login.sapc'
        try:
            # Se foi especificada uma versão, busca por ela
            if SapConnection.gui_version:
                sap_gui_path = self._find_sap_gui_by_version(SapConnection.gui_version)
                
                if sap_gui_path:
                    # Usa a versão específica encontrada
                    os.system(f'open -a "{sap_gui_path}" "{SapConnection.file_path}"')
                else:
                    # Se não encontrou a versão, usa o padrão e mostra aviso
                    print(f"Versão SAP GUI {SapConnection.gui_version} não encontrada. Usando padrão do sistema.")
                    os.system(f'open "{SapConnection.file_path}"')
            else:
                # Se não especificou versão, usa a versão padrão do sistema
                os.system(f'open "{SapConnection.file_path}"')
            
            time.sleep(10)
        finally:
            os.remove(SapConnection.file_path)
