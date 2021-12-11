import os
import webbrowser
from tkinter import Tk, Button, E, LabelFrame, messagebox, Label, Menu
from tkinter.ttk import Combobox
from PIL import Image, ImageTk

# window
ROOT = Tk()
ROOT.title('World Soccer Predictor')
ROOT.geometry('325x280')
ROOT.resizable(False, False)

# logo
FRAME2 = LabelFrame(ROOT)
FRAME2.grid(padx=5, pady=5)
IMAGEx = Image.open('Pic/soccerball.png')
PHOTOx = ImageTk.PhotoImage(IMAGEx)
LABELx = Label(FRAME2, image=PHOTOx)
LABELx.IMAGEx = PHOTOx
LABELx.grid(padx=0, pady=0, row=0, column=0)

def about_menu():
    '''about program'''
    messagebox.showinfo('Program Information', 'World Soccer Predictor\n'  \
                        'For Fall Semester, 2019\n\n'  \
                        'Created by\n\n'  \
                        'Bryce Bilodeau\n'  \
                        'Evan Barth\n'  \
                        'Hubert Oberhauser')


# drop-down menu.
MENU_BAR = Menu(ROOT)
FILE_MENU = Menu(MENU_BAR, tearoff=0)
MENU_BAR.add_cascade(label='Menu', menu=FILE_MENU)
FILE_MENU.add_command(label='About', command=about_menu)
FILE_MENU.add_command(label='Exit', command=ROOT.destroy)
ROOT.config(menu=MENU_BAR)

# dictionary; team,weight pulled from 'Teams.py'
team = {
    'Abkhazia': 3, 'Afghanistan': 1, 'Albania': 3, 'Alderney': 3, 'Algeria': 0, 'American Samoa': 3, 'Andalusia': 3,
     'Andorra': 0, 'Angola': 4, 'Anguilla': 2, 'Antigua and Barbuda': 0, 'Arameans Suryoye': 4, 'Argentina': 3,
     'Armenia': 3, 'Artsakh': 3, 'Aruba': 3, 'Australia': 2, 'Austria': 3, 'Azerbaijan': 4, 'Bahamas': 0, 'Bahrain': 4,
     'Bangladesh': 4, 'Barawa': 4, 'Barbados': 3, 'Basque Country': 3, 'Belarus': 0, 'Belgium': 3, 'Belize': 4,
     'Benin': 3, 'Bermuda': 1, 'Bhutan': 0, 'Bolivia': 0, 'Bonaire': 4, 'Bosnia and Herzegovina': 3, 'Botswana': 0,
     'Brazil': 3, 'British Virgin Islands': 3, 'Brittany': 3, 'Brunei': 1, 'Bulgaria': 3, 'Burkina Faso': 4, 'Burma': 1,
     'Burundi': 2, 'Cambodia': 2, 'Cameroon': 1, 'Canada': 1, 'Canary Islands': 3, 'Cape Verde': 4, 'Cascadia': 3,
     'Catalonia': 3, 'Cayman Islands': 4, 'Central African Republic': 3, 'Central Spain': 4, 'Chad': 2,
     'Chagos Islands': 2, 'Chameria': 4, 'Chile': 4, 'China PR': 1, 'Chinese Taipei': 0, 'Colombia': 3, 'Comoros': 0,
     'Congo': 2, 'Cook Islands': 4, 'Corsica': 4, 'Costa Rica': 2, 'County of Nice': 2, 'Crimea': 3, 'Croatia': 1,
     'Cuba': 3, 'Curacao': 2, 'Curaçao': 4, 'Cyprus': 1, 'Czech Republic': 1, 'Czechoslovakia': 3, 'DR Congo': 3,
     'Darfur': 4, 'Denmark': 1, 'Djibouti': 3, 'Dominica': 1, 'Dominican Republic': 3, 'East Timor': 3, 'Ecuador': 3,
     'Egypt': 1, 'El Salvador': 1, 'Ellan Vannin': 4, 'England': 2, 'Equatorial Guinea': 4, 'Eritrea': 3, 'Estonia': 3,
     'Eswatini': 1, 'Ethiopia': 1, 'Falkland Islands': 0, 'Faroe Islands': 3, 'Felvidék': 4, 'Fiji': 4, 'Finland': 4,
     'France': 1, 'French Guiana': 3, 'Frøya': 0, 'Gabon': 2, 'Galicia': 3, 'Gambia': 2, 'Georgia': 0, 'German DR': 0,
     'Germany': 0, 'Ghana': 0, 'Gibraltar': 2, 'Gotland': 4, 'Gozo': 2, 'Grand Total': 2, 'Greece': 0, 'Greenland': 2,
     'Grenada': 1, 'Guadeloupe': 4, 'Guam': 2, 'Guatemala': 4, 'Guernsey': 3, 'Guinea': 4, 'Guinea-Bissau': 1,
     'Guyana': 1, 'Găgăuzia': 3, 'Haiti': 2, 'Hitra': 4, 'Honduras': 3, 'Hong Kong': 2, 'Hungary': 3, 'Iceland': 3,
     'India': 0, 'Indonesia': 3, 'Iran': 1, 'Iraq': 3, 'Iraqi Kurdistan': 0, 'Isle of Man': 0, 'Isle of Wight': 4,
     'Israel': 2, 'Italy': 2, 'Ivory Coast': 1, 'Jamaica': 2, 'Japan': 4, 'Jersey': 0, 'Jordan': 1, 'Kabylia': 4,
     'Kazakhstan': 3, 'Kenya': 2, 'Kernow': 0, 'Kiribati': 3, 'Kosovo': 1, 'Kuwait': 0, 'Kyrgyzstan': 4,
     'Kárpátalja': 0, 'Laos': 2, 'Latvia': 2, 'Lebanon': 3, 'Lesotho': 2, 'Liberia': 3, 'Libya': 3, 'Liechtenstein': 3,
     'Lithuania': 0, 'Luxembourg': 1, 'Macau': 0, 'Madagascar': 0, 'Madrid': 2, 'Malawi': 4, 'Malaysia': 4,
     'Maldives': 1, 'Mali': 0, 'Malta': 0, 'Manchukuo': 3, 'Martinique': 3, 'Matabeleland': 0, 'Mauritania': 0,
     'Mauritius': 3, 'Mayotte': 2, 'Menorca': 2, 'Mexico': 2, 'Micronesia': 1, 'Moldova': 0, 'Monaco': 2, 'Mongolia': 4,
     'Montenegro': 1, 'Montserrat': 4, 'Morocco': 1, 'Mozambique': 3, 'Myanmar': 2, 'Namibia': 0, 'Nepal': 3,
     'Netherlands': 2, 'New Caledonia': 3, 'New Zealand': 3, 'Nicaragua': 3, 'Niger': 0, 'Nigeria': 1, 'Niue': 4,
     'North Korea': 4, 'North Macedonia': 1, 'North Vietnam': 4, 'Northern Cyprus': 2, 'Northern Ireland': 3,
     'Northern Mariana Islands': 3, 'Norway': 3, 'Occitania': 4, 'Oman': 4, 'Orkney': 3, 'Padania': 3, 'Pakistan': 2,
     'Palau': 1, 'Palestine': 1, 'Panama': 1, 'Panjab': 3, 'Papua New Guinea': 1, 'Paraguay': 3,
     'Parishes of Jersey': 4, 'Peru': 3, 'Philippines': 1, 'Poland': 3, 'Portugal': 0, 'Provence': 1, 'Puerto Rico': 3,
     'Qatar': 4, 'Raetia': 3, 'Republic of Ireland': 3, 'Republic of St. Pauli': 0, 'Rhodes': 4, 'Romani people': 1,
     'Romania': 0, 'Row Labels': 2, 'Russia': 1, 'Rwanda': 2, 'Réunion': 1, 'Saare County': 3, 'Saarland': 4,
     'Saint Helena': 4, 'Saint Kitts and Nevis': 4, 'Saint Lucia': 0, 'Saint Martin': 2,
     'Saint Vincent and the Grenadines': 2, 'Samoa': 3, 'San Marino': 3, 'Sark': 3, 'Saudi Arabia': 1, 'Scotland': 0,
     'Senegal': 1, 'Serbia': 2, 'Seychelles': 4, 'Shetland': 2, 'Sierra Leone': 2, 'Silesia': 1, 'Singapore': 2,
     'Sint Maarten': 0, 'Slovakia': 0, 'Slovenia': 1, 'Solomon Islands': 0, 'Somalia': 1, 'Somaliland': 2,
     'South Africa': 2, 'South Korea': 0, 'South Ossetia': 2, 'South Sudan': 0, 'Spain': 4, 'Sri Lanka': 3,
     'St Kitts and Nevis': 2, 'St Vincent and the Grenadines': 2, 'St. Pierre & Miquelon': 2, 'Sudan': 2, 'Suriname': 1,
     'Sweden': 0, 'Switzerland': 1, 'Syria': 0, 'Székely Land': 4, 'Sápmi': 0, 'São Tomé and Príncipe': 0, 'Tahiti': 3,
     'Tajikistan': 0, 'Tamil Eelam': 4, 'Tanzania': 3, 'Thailand': 3, 'Tibet': 1, 'Timor-Leste': 3, 'Togo': 4,
     'Tonga': 1, 'Trinidad and Tobago': 4, 'Tunisia': 4, 'Turkey': 4, 'Turkmenistan': 2, 'Turks and Caicos Islands': 2,
     'Tuvalu': 1, 'U.S. Virgin Islands': 0, 'Uganda': 0, 'Ukraine': 2, 'United Arab Emirates': 0,
     'United Koreans in Japan': 1, 'United States': 4, 'Uruguay': 3, 'Uzbekistan': 1, 'Vanuatu': 2, 'Vatican City': 0,
     'Venezuela': 1, 'Vietnam': 2, 'Vietnam Republic': 2, 'Wales': 4, 'Wallis Islands and Futuna': 2,
     'Western Armenia': 3, 'Western Isles': 2, 'Western Sahara': 4, 'Yemen': 0, 'Yemen DPR': 4, 'Ynys Môn': 0,
     'Yorkshire': 3, 'Yugoslavia': 0, 'Zambia': 2, 'Zanzibar': 4, 'Zimbabwe': 1, 'Åland Islands': 3}


def prediction():
    '''display dodgy prediction'''
    home_team = COMBO1.get()
    away_team = COMBO2.get()

    if away_team == home_team:
        messagebox.showinfo('Error', 'Please select two different teams!')
        return

    htw = team[home_team]
    htw += 1 #home adv
    atw = team[away_team]

    if htw == atw:
        result = "A Draw"
    if htw > atw:
        result = "Home Win"
    if htw < atw:
        result = "Away Win"

    messagebox.showinfo('World Soccer Predictor', 'You Selected:\n'  \
                        +str(home_team)+' V '+str(away_team)+'\n'  \
                        +'My prediction is:\n\n'+str(result))

#dict to lists
team_list = (list(team.keys()))
team_values = (list(team.values()))

#label texts
FRAME0 = LabelFrame(ROOT)
FRAME0.grid(padx=8, pady=8)
LAB1 = Label(FRAME0, bg='red', text='Home Team')
LAB1.grid()
LAB2 = Label(FRAME0, bg='royalblue', text='Away Team')
LAB2.grid(row=0, column=1)

#combo boxes
COMBO1 = Combobox(FRAME0)
COMBO1['values'] = (team_list)
COMBO1.current(16)
COMBO1.grid(padx=5, pady=5)

COMBO2 = Combobox(FRAME0)
COMBO2['values'] = (team_list)
COMBO2.current(1)
COMBO2.grid(padx=5, pady=5, row=1, column=1)

# predict button
FRAME1 = LabelFrame(ROOT)
FRAME1.grid(padx=8, pady=8)
BTN = Button(FRAME1, bg='green', text='Predict Game', command=prediction)
BTN.grid(sticky=E, padx=5, pady=5)

ROOT.mainloop()

