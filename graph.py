import graphviz
import intances

map = [ [1,1,5,3,2],
        [4,1,4,2,6],
        [3,1,1,3,3],
        [5,2,3,1,2],
        [2,1,1,1,1]]

def print_terrains():
    intances.terrain_handler.print_terrains_by_name()
    terrain = input("\nIngresa el número de terreno a graficar \n") 
    try:
        generate_graphic(intances.terrain_handler.get_terrain_map(int(terrain)),intances.terrain_handler.get_terrain_name(int(terrain)))
        return
    except:
        print("Ingresa un terreno válido o cierre la la gráfica anterior")
    print_terrains()
def generate_graphic(matrix,name):
    h = graphviz.Graph('html_table')
    html=""
    html+=f"<TR><TD colspan='{len(matrix)}'>{name}</TD></TR>"
    for row in matrix:
        html+="<TR>"
        for col in row:
            html+=f"<TD>{col}</TD>"    
        html+="</TR>"
    h.node('tab', label=f'''<<TABLE>{html}</TABLE>>''')
    h.render(f'graph.gv', view=True)
