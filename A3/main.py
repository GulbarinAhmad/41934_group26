from pathlib import Path
import ifcopenshell

modelname = "LLYN - ARK - REV00"

try:
    dir_path = Path(__file__).parent
    model_url = Path.joinpath(dir_path, 'model', modelname).with_suffix('.ifc')
    model = ifcopenshell.open(model_url)
except OSError:
    try:
        import bpy
        model_url = Path.joinpath(Path(bpy.context.space_data.text.filepath).parent, 'model', modelname).with_suffix('.ifc')
        model = ifcopenshell.open(model_url)
    except OSError:
        print(f"ERROR: please check your model folder : {model_url} does not exist")

# Your script goes here

import ifcopenshell
file = ifcopenshell.open('/Users/ahmetondertektas/Desktop/Advanced_BIM/model/LLYN - ARK - REV00.ifc')
file.by_type('IfcProject')
file.by_type('IfcProject')[0]

project = file.by_type('IfcProject')[0]

project.IsDecomposedBy
project.IsDecomposedBy[0]
project.IsDecomposedBy[0].RelatedObjects
project.IsDecomposedBy[0].RelatedObjects[0]

site = project.IsDecomposedBy[0].RelatedObjects[0]


site.IsDecomposedBy[0].RelatedObjects[0]

building = site.IsDecomposedBy[0].RelatedObjects[0]

building.IsDecomposedBy[0]
building.IsDecomposedBy[0].RelatedObjects

building_storeys = building.IsDecomposedBy[0].RelatedObjects
for building_storey in building_storeys:
    print(building_storey)

print('-------------------------------------------------------------------------------')

### Material Properties
### Building Storey (Ground Floor) = [KL_Kælder]
    
building_storeys[0]
KL_Kælder = building_storeys[0]

KL_Kælder.get_info()
KL_Kælder.ContainsElements
KL_Kælder.ContainsElements[0]

rel_contained_in_structure = KL_Kælder.ContainsElements[0]
rel_contained_in_structure.RelatedElements

for element in rel_contained_in_structure.RelatedElements:
    print(element)
    
print('-------------------------------------------------------------------------------')

####################################################################

### Material Properties
### Building Storey (Ground Floor) [ES_Stue]
   
building_storeys[0]
ES_Stue = building_storeys[1]

ES_Stue.get_info()
ES_Stue.ContainsElements
ES_Stue.ContainsElements[0]

rel_contained_in_structure = ES_Stue.ContainsElements[0]
rel_contained_in_structure.RelatedElements

for element in rel_contained_in_structure.RelatedElements:
    print(element)

print('-------------------------------------------------------------------------------')

####################################################################
'''
### Material Properties
### Building Storey (1st Floor) [E1_1]

building_storeys[0]
E1_1 = building_storeys[2]

E1_1.get_info()
E1_1.ContainsElements
E1_1.ContainsElements[0]

rel_contained_in_structure = E1_1.ContainsElements[0]
rel_contained_in_structure.RelatedElements

for element in rel_contained_in_structure.RelatedElements:
    print(element)

print('-------------------------------------------------------------------------------')
    
####################################################################

### Material Properties
### Building Storey (2nd Floor) [E2_2]

building_storeys[0]
E2_2 = building_storeys[3]

E2_2.get_info()
E2_2.ContainsElements
E2_2.ContainsElements[0]

rel_contained_in_structure = E2_2.ContainsElements[0]
rel_contained_in_structure.RelatedElements

for element in rel_contained_in_structure.RelatedElements:
    print(element)
    
print('-------------------------------------------------------------------------------')
####################################################################

### Material Properties
### Building Storey (3th Floor) [E3_3]

building_storeys[0]
E3_3 = building_storeys[4]

E3_3.get_info()
E3_3.ContainsElements
E3_3.ContainsElements[0]

rel_contained_in_structure = E3_3.ContainsElements[0]
rel_contained_in_structure.RelatedElements

for element in rel_contained_in_structure.RelatedElements:
    print(element)


    
print('-------------------------------------------------------------------------------')

### Material Properties
### Building Storey (4th Floor) [E4_4]

building_storeys[0]
E4_4 = building_storeys[5]

E4_4.get_info()
E4_4.ContainsElements
E4_4.ContainsElements[0]

rel_contained_in_structure = E4_4.ContainsElements[0]
rel_contained_in_structure.RelatedElements

for element in rel_contained_in_structure.RelatedElements:
    print(element)
'''
############################################################

