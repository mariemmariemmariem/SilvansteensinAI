from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *

def choisir(plant_type, weather, sunlight, coastal_inland, soil, rainfall, winds, pests_diseases):
    suggested_species = []

    if plant_type == "Trees":
        if weather == "Hot and dry" and sunlight == "Mostly sunny" and coastal_inland == "Inland" and soil == "Sandy" and rainfall == "Periods of drought" and winds == "No prevailing winds" and pests_diseases == "No":
            suggested_species = ["Mesquite", "Acacia"]
        elif weather == "Mild and rainy" and sunlight == "Partially shaded" and coastal_inland == "Inland" and soil == "Loamy" and rainfall == "Consistent rainfall" and winds == "Gentle breezes" and pests_diseases == "No":
            suggested_species = ["Maple", "Oak"]
        elif weather == "Cold and snowy" and sunlight == "Mostly shaded" and coastal_inland == "Coastal" and soil == "Clay-like" and rainfall == "Both" and winds == "Strong coastal winds" and pests_diseases == "No":
            suggested_species = ["Pine", "Spruce"]



    elif plant_type == "Shrubs":
        if weather == "Hot and dry" and sunlight == "Mostly sunny" and coastal_inland == "Inland" and soil == "Sandy" and rainfall == "Periods of drought" and winds == "No prevailing winds" and pests_diseases == "No":
            suggested_species = ["Lavender", "Rosemary"]
        elif weather == "Mild and rainy" and sunlight == "Partially shaded" and coastal_inland == "Inland" and soil == "Loamy" and rainfall == "Consistent rainfall" and winds == "Gentle breezes" and pests_diseases == "No":
            suggested_species = ["Azalea", "Camellia"]
        elif weather == "Cold and snowy" and sunlight == "Mostly shaded" and coastal_inland == "Coastal" and soil == "Clay-like" and rainfall == "Both" and winds == "Strong coastal winds" and pests_diseases == "No":
            suggested_species = ["Boxwood", "Juniper"]


    elif plant_type == "vegetables" :
        if weather == "Hot and dry" and sunlight == "Mostly sunny" and coastal_inland == "Inland" and soil == "Sandy" and rainfall == "Periods of drought" and winds == "No prevailing winds" and pests_diseases == "No":
            suggested_species = ["Tomato", "Pepper"]
        elif weather == "Mild and rainy" and sunlight == "Partially shaded" and coastal_inland == "Inland" and soil == "Loamy" and rainfall == "Consistent rainfall" and winds == "Gentle breezes" and pests_diseases == "No":
            suggested_species = ["Cucumber", "Lettuce"]
        elif weather == "Cold and snowy" and sunlight == "Mostly shaded" and coastal_inland == "Coastal" and soil == "Clay-like" and rainfall == "Both" and winds == "Strong coastal winds" and pests_diseases == "No":
            suggested_species = ["Carrot", "Broccoli"]


    elif plant_type =="fruits":
        if weather == "Hot and dry" and sunlight == "Mostly sunny" and coastal_inland == "Inland" and soil == "Sandy" and rainfall == "Periods of drought" and winds == "No prevailing winds" and pests_diseases == "No":
            suggested_species = ["Cactus Pear", "Pomegranate"]
        elif weather == "Mild and rainy" and sunlight == "Partially shaded" and coastal_inland == "Inland" and soil == "Loamy" and rainfall == "Consistent rainfall" and winds == "Gentle breezes" and pests_diseases == "No":
            suggested_species = ["Apple", "Cherry"]
        elif weather == "Cold and snowy" and sunlight == "Mostly shaded" and coastal_inland == "Coastal" and soil == "Clay-like" and rainfall == "Both" and winds == "Strong coastal winds" and pests_diseases == "No":
            suggested_species = ["Blueberry", "Blackberry"]
            
    elif plant_type =="herbs":
        if weather == "Hot and dry" and sunlight == "Mostly sunny" and coastal_inland == "Inland" and soil == "Sandy" and rainfall == "Periods of drought" and winds == "No prevailing winds" and pests_diseases == "No":
            suggested_species = ["Basil", "Thyme"]
        elif weather == "Mild and rainy" and sunlight == "Partially shaded" and coastal_inland == "Inland" and soil == "Loamy" and rainfall == "Consistent rainfall" and winds == "Gentle breezes" and pests_diseases == "No":
            suggested_species = ["Parsley", "Mint"]
        elif weather == "Cold and snowy" and sunlight == "Mostly shaded" and coastal_inland == "Coastal" and soil == "Clay-like" and rainfall == "Both" and winds == "Strong coastal winds" and pests_diseases == "No":
            suggested_species = ["Rosemary", "Lavender"]
            
    elif plant_type =="flowers" :
        if weather == "Hot and dry" and sunlight == "Mostly sunny" and coastal_inland == "Inland" and soil == "Sandy" and rainfall == "Periods of drought" and winds == "No prevailing winds" and pests_diseases == "No":
            suggested_species = ["Sunflower", "Zinnia"]
        elif weather == "Mild and rainy" and sunlight == "Partially shaded" and coastal_inland == "Inland" and soil == "Loamy" and rainfall == "Consistent rainfall" and winds == "Gentle breezes" and pests_diseases == "No":
            suggested_species = ["Daisy", "Tulip"]
        elif weather == "Cold and snowy" and sunlight == "Mostly shaded" and coastal_inland == "Coastal" and soil == "Clay-like" and rainfall == "Both" and winds == "Strong coastal winds" and pests_diseases == "No":
            suggested_species = ["Pansy", "Lily"]
    # Display the suggested species to the user

        return(suggested_species)

def play ():
        # Initialize variables
    weather = ""
    sunlight = ""
    coastal_inland = ""
    soil = ""
    rainfall = ""
    winds = ""
    pests_diseases = ""
    plant_type = ""
    
    if windows.hotanddry.isChecked():
        weather = "Hot and dry"
    elif windows.mildandrainy.isChecked():
        weather == "Mild and rainy"
    elif windows.coldandsnowy.isChecked():
        weather == "Cold and snowy"

    
    if windows.mostlysunny.isChecked():
        sunlight = "Mostly sunny"
    elif windows.partiallyshaded.isChecked():
        sunlight == "Partially shaded"
    elif windows.mostlyshaded.isChecked():
        sunlight == "Mostly shaded"
        
    if windows.inland.isChecked():
        coastal_inland = "inland"
    elif windows.coastal.isChecked():
        coastal_inland == "Coastal"

        
    if windows.sundy.isChecked():   
        soil = "Sandy"
    elif windows.loamy.isChecked():
        soil == "Loamy"
    elif windows.claylike.isChecked():
        soil == "Clay-like"
    
    if windows.periodsofdrought.isChecked():    
        rainfall = "Periods of drought"
    elif windows.constitentrainfall.isChecked():
        rainfall == "Consistent rainfall"
    elif windows.mostlyshaded.isChecked():
        rainfall == "Both"
        
    if windows.noprevailingwind.isChecked():    
        winds = "No prevailing winds"
    elif windows.gentlebreezes.isChecked():
        winds == "Gentle breezes"
    if windows.strongandcoastalwinds.isChecked():     
        winds == "Strong coastal winds"
    
    if windows.comboBox.currentText()=="trees" :
        plant_type = "Trees"
    elif windows.comboBox.currentText()=="shrubs" :
        plant_type = "Shrubs"
    elif windows.comboBox.currentText()=="vegetables" :
        plant_type = "vegetables"
    elif windows.comboBox.currentText()=="fruits" :
        plant_type = "fruits"
    elif windows.comboBox.currentText()=="herbs" :
        plant_type = "herbs"
    else :
        plant_type =="flowers" 
    
    # Call the choisir() function to get the suggested species
    result = choisir(plant_type, weather, sunlight, coastal_inland, soil, rainfall, winds, pests_diseases)

    # Check if the result is not None (no suggestion for the selected criteria)
    if result is not None:
        # Unpack the tuple and format it into a single string
        suggestion_text = "{}\n{}".format(result[0], ", ".join(result[1]))
        windows.res.setText(suggestion_text)
    else:
        windows.res.setText("No suggestion for the selected criteria.")
app = QApplication([])
windows = loadUi("userinterface.ui")
windows.show()
windows.bouton.clicked.connect(play)
app.exec_()