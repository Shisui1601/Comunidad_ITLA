from azureml.core import Workspace

ws = Workspace.from_config()
print(ws.name, ws.resource_group, ws.location, ws.subscription_id, sep='\n')

from azureml.core import Datastore, Dataset

# Obtener el DataStore predeterminado
datastore = ws.get_default_datastore()

# Subir el archivo CSV al DataStore
datastore.upload_files(files=['client_data.csv'],
                       target_path='client_data/',
                       overwrite=True,
                       show_progress=True)

# Crear un Dataset a partir del archivo CSV en el DataStore
dataset = Dataset.Tabular.from_delimited_files(path=(datastore, 'client_data/client_data.csv'))

# Registrar el Dataset en el Workspace
dataset = dataset.register(workspace=ws, name='client_data')
