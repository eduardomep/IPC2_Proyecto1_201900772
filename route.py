import intances

def print_terrains():
    intances.terrain_handler.print_terrains_by_name()
    terrain = input("\nIngresa el número de terreno a procesar \n") 
    print("\nCalculando la ruta...")
    print("Calculando combustible...")
    grid_traveled = matrix_to_zero(intances.terrain_handler.get_terrain_map_traveled(int(terrain))) 
    #print_matrix(grid_traveled)
    terrain_positions = intances.terrain_handler.get_terrain_positions(int(terrain))
    print(f"""
Ruta: ({terrain_positions[0]},{terrain_positions[1]}) -> ({terrain_positions[2]},{terrain_positions[3]})    """)
    xi= terrain_positions[0] - 1
    yi= terrain_positions[1] - 1
    xf= terrain_positions[2] - 1
    yf= terrain_positions[3] - 1
    grid = intances.terrain_handler.get_terrain_map(int(terrain))
    print("\nterreno original")
    print_matrix(grid)
    try:
        validate_space(xi,yi,xf,yf,grid,grid_traveled)
    except:
        print("\nNo se pudo completar el recorrido\n")
    print("\nterreno recorrido")
    print_matrix(grid_traveled)
    intances.terrain_handler.update_gas(int(terrain),total_gas)
    
    # try:

    #     #validate_space(0,0,4,4,grid,grid_traveled)
    #     return
    # except:
    #     print("Ingresa un terreno válido")
    # print_terrains()




grid = [ [1,1,5,3,2],
        [4,1,4,2,6],
        [3,1,1,3,3],
        [5,2,3,1,2],
        [2,1,1,1,1]]



grid_traveled = [ [1,1,5,3,2],
        [4,1,4,2,6],
        [3,1,1,3,3],
        [5,2,3,1,2],
        [2,1,1,1,1]]


# xi = 1
# yi = 1

def matrix_to_zero(matrix):
    for row_index, row in enumerate(matrix):
        for col_index, col in enumerate(row):
            matrix[row_index][col_index] = 0
    return matrix


row_global = 5
col_global = 5

def print_matrix(matrix):
    for row_index, row in enumerate(matrix):
        numbers = ""
        for col_index, col in enumerate(row):
            numbers = str(numbers) + str(matrix[row_index][col_index]) + " |"
        print(str(numbers))

        



total_gas=0
oldx = None
oldy = None
index = 0



def validate_space(row,col,xf,yf,matrix,road_traveled):
    global oldx, oldy
    global total_gas 
    xf_original = xf + 1
    yf_original = yf + 1
    xtemp = oldx
    ytemp = oldy
    #print("-----------inicia-------------")
    global index
    if(oldx is None):
        oldx = row
        oldy = col
    else:
        oldx = row
        oldy = col
    #print(f"posicion anterior:  {xtemp} - {ytemp} ******************")
    #print(f'posicion actual: {row+1} - {col+1}')
    road_traveled[row][col] = 1
    total_gas += int(matrix[row][col])
    # validaondo si no llegamos al final del matrixa  
    if(row != xf or col != yf ):
        #abuelo es row,col una posicion inicla (primetro parametro)
        #variable para guardar el valor del paso siguiente y su total de gasolina
        temp_movement=[0,0,0]
        #papas
        aroundItems = validate_around(row,col,matrix,xf_original,yf_original)
        #por cada uno de los papás
        
        for aroundItem in aroundItems:
            #verificamos que exista la poisición
            if(aroundItem[0] >=0):
                if(aroundItem[0] == xf and aroundItem[1] == yf):
                    print(f"\n llegamos al final en {xf+1} -{yf+1}")
                    road_traveled[xf][xf] = 1
                    total_gas+=matrix[xf][yf]
                    print(total_gas)
                    print_matrix(matrix)
                    print("\n")
                    print_matrix(road_traveled)
                    return False
                aroundTotals=[0,0,0,0]
                #hijos
                aroundJuniors =  validate_around(aroundItem[0],aroundItem[1],matrix,xf_original,yf_original)
                i=0
                for aroundJunior in aroundJuniors:
                    if(aroundItem[0] != xtemp or aroundItem[1] != ytemp):
                        #if(aroundJunior[0]==xf and aroundJunior[1]==yf):
                        #    print("faltan dos pasos***********")                            
                        if((aroundJunior[0] >= 0) and (row != aroundJunior[0] or col != aroundJunior[1])):
                            aroundTotals[i] =  aroundItem[2] + aroundJunior[2]
                            if int(temp_movement[2]) == 0 :
                                #X papa
                                temp_movement[0] = aroundItem[0] 
                                #y papa
                                temp_movement[1] = aroundItem[1] 
                                #suma total de hijo con papa
                                temp_movement[2] = aroundTotals[i] 
                            else:
                                if(int(temp_movement[2]) >= int(aroundTotals[i])):
                                    #X papa
                                    temp_movement[0] = aroundItem[0] 
                                    #y papa
                                    temp_movement[1] = aroundItem[1] 
                                    #suma total de hijo con papa
                                    temp_movement[2] = aroundTotals[i] 
                                    #print(f'posicion actual {temp_movement[0]} - {temp_movement[1]}')
                            #print(f'Ganó la suma de gasolina en: {temp_movement[2]}')
                        else:
                            aroundTotals[i] = -1
                        #print(temp_movement[0],temp_movement[1])
                    i+=1
                #print(f'{aroundTotals} el menor es {temp_movement[2]}')
                


        validate_space(int(temp_movement[0]),int(temp_movement[1]),xf,yf,matrix,road_traveled)

    


    
def validate_around(row,col,matrix,xf,yf):
    #[x,y,gas]
    around = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
    try:
        #top
        if(matrix[row][col] and (row-1)>=0 and (row-1)<=(xf-1)):
            around[0][0]=row-1
            around[0][1]=col
            around[0][2]=matrix[row-1][col]
        #right
        if(matrix[row][col] and (col+1)>=0 and (col+1)<=(yf-1)):
            around[1][0]=row
            around[1][1]=col+1
            around[1][2]=matrix[row][col+1]
        #bottom
        if(matrix[row][col] and (row+1)>=0 and (row+1)<=(xf-1)):
            around[2][0]=row+1
            around[2][1]=col
            around[2][2]=matrix[row+1][col]
        #left
        if(matrix[row][col] and (col-1)>=0 and (col-1)<=(yf-1)):
            around[3][0]=row
            around[3][1]=col-1
            around[3][2]=matrix[row][col-1]
    except:
        #return print("coordenada inexistente")
        return
    return around







# matrix_to_zero(grid_traveled) 
# validate_space(0,0,4,4,grid,grid_traveled)
# print("")
# print_matrix(grid)
# print("M")
# print_matrix(grid_traveled)