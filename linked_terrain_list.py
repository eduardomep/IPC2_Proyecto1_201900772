from node import Node
class Linked_terrain_list:
    def __init__(self):
        self.first = None
    def new_element(self,terrain):
        if self.first == None:
            self.first = Node(terrain = terrain)
            return
        #apuntador
        current = self.first
        #si el primero ya apunta
        while current.next:
            #apuntador le asigno el apuntador que viene
            current = current.next
        #Apunta al que viene
        current.next = Node(terrain=terrain)
    def print_terrains(self):
        current = self.first
        while current != None:
            print(current.terrain.name+" - "+str(current.terrain.grid))
            current = current.next
    def print_terrains_by_name(self):
        counter=1
        current = self.first
        while current != None:
            print(f'{counter} - {current.terrain.name}')
            counter+=1
            current = current.next
    def get_terrain_map(self,id):
        counter=1
        current = self.first
        while current != None:
            if(counter==id):
                return current.terrain.grid
            counter+=1
            current = current.next
        return False