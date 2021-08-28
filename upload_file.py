from xml.dom import minidom
from Terrain import Terrain
import intances
counter = 0

def get_matrix(positions,row,col):
    row = int(row)
    col = int(col)
    terrain_grid = []
    for position in positions:
        terrain_grid = [*terrain_grid,position.firstChild.data]
    terrain_grid=[terrain_grid[col*i: col*(i+1)] for i in range(row)]
    return terrain_grid

def get_file():
    global counter
    route = 'entry.xml'
    #route = input("Ingresa la ruta de tu archivo \n")
    try:
        xml_file = minidom.parse(route)
        terrains = xml_file.getElementsByTagName('TERRENO')
        for terrain in terrains:
            terrain_grid = []
            name= terrain.attributes["nombre"].value
            row = terrain.getElementsByTagName("m")[0].childNodes[0].data
            col = terrain.getElementsByTagName("n")[0].childNodes[0].data 
            init_coodernades = xml_file.getElementsByTagName('posicioninicio')
            end_coodernades = xml_file.getElementsByTagName('posicionfin')
            xi = init_coodernades[0].getElementsByTagName("x")[0].childNodes[0].data
            yi= init_coodernades[0].getElementsByTagName("y")[0].childNodes[0].data
            xf= end_coodernades[0].getElementsByTagName("x")[0].childNodes[0].data
            yf= end_coodernades[0].getElementsByTagName("y")[0].childNodes[0].data
            data = int(row)*int(col)
            positions = xml_file.getElementsByTagName('posicion')[counter: data+counter]
            terrain = Terrain(name,xi,yi,xf,yf,get_matrix(positions,row,col),row,col)
            intances.terrain_handler.new_element(terrain)
            counter+=data
        return("archivo cargado con éxito!")
    except:
        return("ruta invalida , volviendo al inicio...")


