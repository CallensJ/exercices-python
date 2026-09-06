


#fonction Écrire une fonction qui valide un dossier de destination fourni sous forme de chemin (`str` ou `Path`), et retourne un résultat clair indiquant si ce dossier peut être utilisé.


#DEBUT algorithme validate_destination_dir

#CREER new_error_list []
#READ dest_folder
#IF NOT dest_folder exist , THEN
    #ADD message " le dossier XXX n'existe pas " INTO new_error_list
#ENDIF
#IF NOT dest_folder is folder, THEN
    #ADD message " Ce n'est pas un dossier valide" INTO new
#ENDIF


#FIN algorithme validate_destination_dir
from pathlib import Path



def validate_destination_dir(folder_path):
    new_errors_list = []
    path = Path(folder_path)

    if not path.exists():
        new_errors_list.append(f"Le dossier '{folder_path}' n'existe pas")
        return new_errors_list

    if not path.is_dir():
        new_errors_list.append(f"'{folder_path}' n'est pas un dossier")
        return new_errors_list

    return new_errors_list
