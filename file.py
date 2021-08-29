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
    route = input("Ingresa la ruta de tu archivo \n")
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
            terrain = Terrain(name,xi,yi,xf,yf,get_matrix(positions,row,col),row,col,get_matrix(positions,row,col),0)
            intances.terrain_handler.new_element(terrain)
            counter+=data
        return("archivo cargado con éxito!")
    except:
        return("ruta invalida , volviendo al inicio...")



def create_file():
    intances.terrain_handler.print_terrains_by_name()
    terrain = input("\nIngresa el número de terreno a generar \n") 
    # try:
    terrain_data = intances.terrain_handler.get_terrain_output_data(int(terrain))
    name = terrain_data[0]
    xi = terrain_data[1]
    yi = terrain_data[2]
    xf = terrain_data[3]
    yf = terrain_data[4]
    gas = terrain_data[5]
    matrix = terrain_data[6]
    route = input("Ingresa la ruta y nombre de archivo \n")
    output_file = open(route, "w")
    output_file.write(f'''<terreno nombre="{name}">
    <posicioninicio>
        <x>{str(xi)}</x>
        <y>{str(yi)}</y>
    </posicioninicio>
    <posicionfin>
        <x>{str(xf)}</x>
        <y>{str(yf)}</y>
    </posicionfin>
    <combustible>{str(gas)}</posicionfin>''')
    for row_index, row in enumerate(matrix):
        for col_index,col in enumerate(row):
            if (matrix[row_index][col_index]) == 1:
                output_file.write(f''' 
    <posicion x="{str(row_index + 1)}" y="{str(col_index + 1)}"> {str(matrix[row_index][col_index])} </posicion>''')
    output_file.write('''
</terreno>''')

