from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1500.bin",                # FileName
        "c1500",                    # MapName
        "c1500",                    # Location
        0x00AA,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\n',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 170, 0, 11, 0, 12],
    )

    BuildStringList((
        "c1500",                  # 0
        "Kanning police officer",           # 1
        "Martin policing",         # 2
        "Tajik",                 # 3
        "Policeman",                   # 4
        "Policeman",                   # 5
        "Policeman",                   # 6
        "Policeman",                   # 7
        "City official staff",             # 8
        "City official staff",             # 9
        "Lieutenant Mireille",           # 10
        "Citizen",                   # 11
        "girl",                 # 12
        "tourist",                 # 13
        "tourist",                 # 14
        "tourist",                 # 15
        "tourist",                 # 16
        "tourist",                 # 17
        "tourist",                 # 18
        "Kindoor",             # 19
        "Ryu",                 # 20
        "Henry",                 # 21
        "peach",                   # 22
        "Singh",                   # 23
        "Reporter Noticia",         # 24
        "Nielsen",             # 25
        "Douglas deputy command",         # 26
        "McDowell",         # 27
        "Sergey Manager",           # 28
        "Broken support car",         # 29
        "New armored car",             # 30
        "New armored car",             # 31
        "Prime Minister Osborne",         # 32
        "Lector clerk",         # 33
        "Prince Oliver",       # 34
        "Major Muller",           # 35
        "Claudia Hime",         # 36
        "Assistant Julia",             # 37
        "Prince Albert",         # 38
        "President Lock Smith",     # 39
        "Assistant Kirika",           # 40
        "Mayor of Dieter",         # 41
        "Marybele",             # 42
        "Mushroute Scott",         # 43
        "Wrestler Wenzel",     # 44
        "Zookoist Rin",             # 45
        "Friend Aolia",         # 46
        "Secretary of Defense Arios",       # 47
        "Dudley investigator",         # 48
        "Raymond investigator",       # 49
        "Emma investigator",             # 50
        "Mr. Joe Ridge",       # 51
        "Kate patrol head",           # 52
        "Police investigation",           # 53
        "Voice of Lloyd's",         # 54
        "Event monster",   # 55
        "Event monster",   # 56
        "Event monster",   # 57
        "Event monster",   # 58
        "Event monster",   # 59
        "Event monster",   # 60
        "Event monster",   # 61
        "Event monster",   # 62
        "Event monster",   # 63
        "Sonya Command",           # 64
        "Policeman",                   # 65
        "Policeman",                   # 66
        "Policeman",                   # 67
        "Policeman",                   # 68
        "Policeman",                   # 69
        "Policeman",                   # 70
        "Policeman",                   # 71
        "Policeman",                   # 72
        "Policeman",                   # 73
        "Policeman",                   # 74
        "The guard",                 # 75
        "The guard",                 # 76
        "The guard",                 # 77
        "The guard",                 # 78
        "The guard",                 # 79
        "The guard",                 # 80
        "The guard",                 # 81
        "The guard",                 # 82
        "A secretary",                   # 83
        "Butler",                   # 84
        "Imperial Army officer",             # 85
        "Imperial Army officer",             # 86
        "Republican army officer",           # 87
        "Republican army officer",           # 88
        "The gentleman",                 # 89
        "The gentleman",                 # 90
        "Soldier Carter",           # 91
        "Defense Forces soldier · man",         # 92
        "Defense Forces soldier · man",         # 93
        "Defense Forces soldier · man",         # 94
        "Defense Forces soldier · man",         # 95
        "Defense Forces soldier / woman",         # 96
        "Defense Forces soldier / woman",         # 97
        "Defense Forces soldier / woman",         # 98
        "Defense Forces Officer",             # 99
        "Grace",               # 100
        "Raines",               # 101
        "A reporter",                   # 102
        "A reporter",                   # 103
        "A reporter",                   # 104
        "A reporter",                   # 105
        "car",                     # 106
        "car",                     # 107
        "car",                     # 108
        "car",                     # 109
        "New armored vehicle (A)",       # 110
        "New armored vehicle (B)",       # 111
        "Moon ring",                 # 112
        "Moon ring",                 # 113
        "SE control",                 # 114
        "Central square",               # 115
        "Nishi dori",                 # 116
        "Administrative district",                 # 117
        "Residential area",                 # 118
        "Entertainment district",                 # 119
        "East Street",                 # 120
        "old Town",                 # 121
        "Harbor district",                 # 122
        "IBC",                 # 123
        "Beside the station",               # 124
        "Back street",                 # 125
        "Ursula interchange",           # 126
        "East Crossbell Highway",       # 127
        "West Crossbell Highway",       # 128
        "Mainz Mountain Road",           # 129
        "Orchis Tower",         # 130
    ))

    AddCharChip((
        "chr/ch30000.itc",                   # 00
        "chr/ch28100.itc",                   # 01
        "chr/ch27700.itc",                   # 02
        "chr/ch27800.itc",                   # 03
        "chr/ch32600.itc",                   # 04
        "chr/ch20302.itc",                   # 05
        "chr/ch22300.itc",                   # 06
        "chr/ch24400.itc",                   # 07
        "chr/ch44200.itc",                   # 08
        "chr/ch34300.itc",                   # 09
        "chr/ch44200.itc",                   # 0A
        "chr/ch20600.itc",                   # 0B
        "chr/ch22200.itc",                   # 0C
        "chr/ch20700.itc",                   # 0D
        "chr/ch45000.itc",                   # 0E
        "chr/ch47900.itc",                   # 0F
        "chr/ch45102.itc",                   # 10
        "chr/ch49200.itc",                   # 11
        "chr/ch49000.itc",                   # 12
        "chr/ch05800.itc",                   # 13
        "chr/ch02500.itc",                   # 14
        "chr/ch44700.itc",                   # 15
        "chr/ch21800.itc",                   # 16
    ))

    DeclNpc(2759,    0,       26000,   180,  257,  0x0, 0,   0,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(4294964537, 0,       26000,   180,  257,  0x0, 0,   0,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(2859,    0,       4294963517, 0,    385,  0x0, 0,   1,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(2759,    0,       4294948276, 180,  385,  0x0, 0,   0,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(4294964316, 0,       4294948286, 180,  385,  0x0, 0,   0,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(10069,   300,     4294954876, 0,    385,  0x0, 0,   0,   0,   0,   1,   0,   24,  255,  0)
    DeclNpc(4294956467, 0,       5320,    180,  385,  0x0, 0,   0,   0,   0,   2,   0,   25,  255,  0)
    DeclNpc(4294961816, 250,     7909,    270,  385,  0x0, 0,   2,   0,   0,   0,   0,   26,  255,  0)
    DeclNpc(4294959816, 250,     7909,    90,   385,  0x0, 0,   3,   0,   0,   0,   0,   27,  255,  0)
    DeclNpc(7230,    250,     7760,    225,  385,  0x0, 0,   4,   0,   0,   0,   0,   28,  255,  0)
    DeclNpc(13539,   449,     4294953956, 315,  389,  0x0, 0,   5,   0,   0,   0,   0,   34,  255,  0)
    DeclNpc(13539,   300,     4294956296, 0,    385,  0x0, 0,   6,   0,   0,   3,   0,   35,  255,  0)
    DeclNpc(4294956696, 289,     4294952876, 0,    385,  0x0, 0,   7,   0,   0,   0,   0,   36,  255,  0)
    DeclNpc(4294957546, 289,     4294952597, 0,    385,  0x0, 0,   8,   0,   0,   0,   0,   37,  255,  0)
    DeclNpc(4294949596, 0,       7489,    0,    385,  0x0, 0,   9,   0,   0,   0,   0,   38,  255,  0)
    DeclNpc(4294948596, 0,       7489,    0,    385,  0x0, 0,   10,  0,   0,   0,   0,   39,  255,  0)
    DeclNpc(4294966696, 100,     6090,    0,    385,  0x0, 0,   17,  0,   0,   0,   0,   40,  255,  0)
    DeclNpc(600,     100,     6090,    0,    385,  0x0, 0,   18,  0,   0,   0,   0,   41,  255,  0)
    DeclNpc(4294956666, 0,       11239,   45,   385,  0x0, 0,   22,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(4294966397, 100,     7260,    135,  389,  0x0, 0,   11,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(2220,    100,     5559,    270,  389,  0x0, 0,   12,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(4294965267, 100,     5559,    90,   389,  0x0, 0,   13,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(1620,    100,     7010,    225,  389,  0x0, 0,   14,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(6829,    250,     5150,    0,    389,  0x0, 0,   15,  0,   0,   0,   0,   42,  255,  0)
    DeclNpc(4294944407, 400,     4294961277, 90,   389,  0x0, 0,   16,  0,   255, 255, 0,   43,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   21,  0,   0,   0,   0,   32,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   19,  0,   255, 255, 0,   29,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   20,  0,   255, 255, 0,   31,  255,  0)
    DeclNpc(4294957126, 0,       19069,   0,    132,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(3430,    100,     8590,    0,    132,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(10510,   0,       6289,    0,    132,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    452,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    452,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 59,  0.0,                   29.0,                  -0.75,                 225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -9.666666984558105,    0.15000000596046448,   1.0])
    DeclEvent(0x0000, 0, 57,  0.0,                   29.0,                  -0.75,                 225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -9.666666984558105,    0.15000000596046448,   1.0])

    DeclActor(4294957126, 0,       18070,   2500,    4294957126, 2500,    18070,   0x007C, 0,  33, 0x0000)

    PlaceName(-20.690000534057617, 0.0, -334.95001220703125, 0x0000, 0x0000, "Central square")
    PlaceName(-176.4499969482422, 0.0, -343.79998779296875, 0x0000, 0x0000, "Nishi dori")
    PlaceName(21.639999389648438, 0.0, -191.3000030517578, 0x0000, 0x0000, "Administrative district")
    PlaceName(-276.45001220703125, 0.0, -223.8000030517578, 0x0000, 0x0000, "Residential area")
    PlaceName(-142.5, 0.0, -222.60000610351562, 0x0000, 0x0000, "Entertainment district")
    PlaceName(113.25, 0.0, -400.5, 0x0000, 0x0000, "East Street")
    PlaceName(183.5800018310547, 0.0, -513.25, 0x0000, 0x0000, "old Town")
    PlaceName(154.9499969482422, 0.0, -274.3999938964844, 0x0000, 0x0000, "Harbor district")
    PlaceName(126.94999694824219, 0.0, -96.5, 0x0000, 0x0000, "IBC")
    PlaceName(-17.75, 0.0, -493.6000061035156, 0x0000, 0x0000, "Beside the station")
    PlaceName(-101.80000305175781, 0.0, -283.20001220703125, 0x0000, 0x0000, "Back street")
    PlaceName(-21.200000762939453, 0.0, -548.0499877929688, 0x0000, 0x0000, "Ursula interchange")
    PlaceName(234.85000610351562, 0.0, -384.6000061035156, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-264.95001220703125, 0.0, -340.3999938964844, 0x0000, 0x0000, "West Crossbell Highway")
    PlaceName(-254.0500030517578, 0.0, -165.39999389648438, 0x0000, 0x0000, "Mainz Mountain Road")
    PlaceName(0.0, 0.0, 55.5, 0x0000, 0x0000, "Orchis Tower")
    PlaceName(-75.98999786376953, 0.0, -390.8500061035156, 0x0000, 0x0051, "")
    PlaceName(26.18000030517578, 0.0, -340.75, 0x0000, 0x0054, "")
    PlaceName(-30.809999465942383, 0.0, -400.6499938964844, 0x0000, 0x0057, "")
    PlaceName(-76.8499984741211, 0.0, -336.20001220703125, 0x0000, 0x0053, "")
    PlaceName(-33.279998779296875, 0.0, -289.79998779296875, 0x0000, 0x0053, "")
    PlaceName(-155.63999938964844, 0.0, -302.45001220703125, 0x0000, 0x0053, "")
    PlaceName(-99.7300033569336, 0.0, -266.6000061035156, 0x0000, 0x0053, "")
    PlaceName(-110.25, 0.0, -240.39999389648438, 0x0000, 0x0052, "")
    PlaceName(128.3000030517578, 0.0, -543.5800170898438, 0x0000, 0x0053, "")
    PlaceName(-85.7300033569336, 0.0, -280.67999267578125, 0x0000, 0x0053, "")
    PlaceName(-26.950000762939453, 0.0, -144.3300018310547, 0x0000, 0x0051, "")
    PlaceName(181.85000610351562, 0.0, -410.5, 0x0000, 0x0052, "")
    PlaceName(128.3000030517578, 0.0, -543.5800170898438, 0x0000, 0x0053, "")
    PlaceName(158.64999389648438, 0.0, -582.2999877929688, 0x0000, 0x0053, "")

    ChipFrameInfo(4864, 0)                                       # 0

    ScpFunction((
        "Function_0_1300",         # 00, 0
        "Function_1_13B0",         # 01, 1
        "Function_2_1445",         # 02, 2
        "Function_3_14DA",         # 03, 3
        "Function_4_1505",         # 04, 4
        "Function_5_159A",         # 05, 5
        "Function_6_15ED",         # 06, 6
        "Function_7_1640",         # 07, 7
        "Function_8_1733",         # 08, 8
        "Function_9_1752",         # 09, 9
        "Function_10_176F",        # 0A, 10
        "Function_11_1832",        # 0B, 11
        "Function_12_1D3D",        # 0C, 12
        "Function_13_204C",        # 0D, 13
        "Function_14_299C",        # 0E, 14
        "Function_15_335A",        # 0F, 15
        "Function_16_3CD4",        # 10, 16
        "Function_17_3E1A",        # 11, 17
        "Function_18_3E9D",        # 12, 18
        "Function_19_3F3C",        # 13, 19
        "Function_20_3FCD",        # 14, 20
        "Function_21_4067",        # 15, 21
        "Function_22_475B",        # 16, 22
        "Function_23_4873",        # 17, 23
        "Function_24_4973",        # 18, 24
        "Function_25_49AF",        # 19, 25
        "Function_26_4A16",        # 1A, 26
        "Function_27_4ABD",        # 1B, 27
        "Function_28_4B26",        # 1C, 28
        "Function_29_4FBF",        # 1D, 29
        "Function_30_5471",        # 1E, 30
        "Function_31_591D",        # 1F, 31
        "Function_32_5E43",        # 20, 32
        "Function_33_6330",        # 21, 33
        "Function_34_659E",        # 22, 34
        "Function_35_6911",        # 23, 35
        "Function_36_6B78",        # 24, 36
        "Function_37_6BD8",        # 25, 37
        "Function_38_6C30",        # 26, 38
        "Function_39_6E33",        # 27, 39
        "Function_40_6FB4",        # 28, 40
        "Function_41_6FF8",        # 29, 41
        "Function_42_7046",        # 2A, 42
        "Function_43_70BD",        # 2B, 43
        "Function_44_7180",        # 2C, 44
        "Function_45_8186",        # 2D, 45
        "Function_46_87F9",        # 2E, 46
        "Function_47_8D68",        # 2F, 47
        "Function_48_8DB5",        # 30, 48
        "Function_49_8E02",        # 31, 49
        "Function_50_8E4F",        # 32, 50
        "Function_51_8E9C",        # 33, 51
        "Function_52_AA19",        # 34, 52
        "Function_53_AAD2",        # 35, 53
        "Function_54_AC50",        # 36, 54
        "Function_55_AC76",        # 37, 55
        "Function_56_ACD1",        # 38, 56
        "Function_57_B12A",        # 39, 57
        "Function_58_B1C8",        # 3A, 58
        "Function_59_BA8D",        # 3B, 59
        "Function_60_BF06",        # 3C, 60
        "Function_61_C1A8",        # 3D, 61
        "Function_62_CF44",        # 3E, 62
        "Function_63_D003",        # 3F, 63
        "Function_64_D124",        # 40, 64
        "Function_65_D865",        # 41, 65
        "Function_66_D91E",        # 42, 66
        "Function_67_E4A6",        # 43, 67
        "Function_68_E4C2",        # 44, 68
        "Function_69_E4EB",        # 45, 69
        "Function_70_E5F9",        # 46, 70
        "Function_71_FF58",        # 47, 71
        "Function_72_FFC1",        # 48, 72
        "Function_73_10024",       # 49, 73
        "Function_74_10087",       # 4A, 74
        "Function_75_100EA",       # 4B, 75
        "Function_76_1015D",       # 4C, 76
        "Function_77_101C6",       # 4D, 77
        "Function_78_1021B",       # 4E, 78
        "Function_79_1028B",       # 4F, 79
        "Function_80_102FC",       # 50, 80
        "Function_81_104A3",       # 51, 81
        "Function_82_1064D",       # 52, 82
        "Function_83_107F4",       # 53, 83
        "Function_84_1083F",       # 54, 84
        "Function_85_1088E",       # 55, 85
        "Function_86_108F1",       # 56, 86
        "Function_87_10954",       # 57, 87
        "Function_88_109B7",       # 58, 88
        "Function_89_10A15",       # 59, 89
        "Function_90_10AA2",       # 5A, 90
        "Function_91_10C78",       # 5B, 91
        "Function_92_10CFB",       # 5C, 92
        "Function_93_10D7E",       # 5D, 93
        "Function_94_10E01",       # 5E, 94
        "Function_95_11145",       # 5F, 95
        "Function_96_1119B",       # 60, 96
        "Function_97_112BA",       # 61, 97
        "Function_98_11302",       # 62, 98
        "Function_99_115FA",       # 63, 99
        "Function_100_11688",      # 64, 100
        "Function_101_11796",      # 65, 101
        "Function_102_117C5",      # 66, 102
        "Function_103_1187E",      # 67, 103
        "Function_104_1198B",      # 68, 104
        "Function_105_11B02",      # 69, 105
        "Function_106_11B3B",      # 6A, 106
        "Function_107_1217B",      # 6B, 107
        "Function_108_12187",      # 6C, 108
        "Function_109_121AA",      # 6D, 109
        "Function_110_123F5",      # 6E, 110
        "Function_111_1248F",      # 6F, 111
        "Function_112_124F2",      # 70, 112
        "Function_113_12691",      # 71, 113
        "Function_114_126DC",      # 72, 114
        "Function_115_12776",      # 73, 115
        "Function_116_127DC",      # 74, 116
        "Function_117_12868",      # 75, 117
        "Function_118_12887",      # 76, 118
        "Function_119_12969",      # 77, 119
        "Function_120_12A3C",      # 78, 120
        "Function_121_12B71",      # 79, 121
        "Function_122_12B99",      # 7A, 122
        "Function_123_12C3A",      # 7B, 123
        "Function_124_12C90",      # 7C, 124
        "Function_125_12D63",      # 7D, 125
        "Function_126_12D82",      # 7E, 126
        "Function_127_12E2C",      # 7F, 127
        "Function_128_12E46",      # 80, 128
        "Function_129_12E60",      # 81, 129
        "Function_130_12E7A",      # 82, 130
        "Function_131_12EC1",      # 83, 131
        "Function_132_12F08",      # 84, 132
        "Function_133_12F25",      # 85, 133
        "Function_134_12F50",      # 86, 134
        "Function_135_12F9F",      # 87, 135
        "Function_136_12FD8",      # 88, 136
        "Function_137_1300A",      # 89, 137
        "Function_138_1303C",      # 8A, 138
        "Function_139_13092",      # 8B, 139
        "Function_140_130E8",      # 8C, 140
        "Function_141_1313E",      # 8D, 141
        "Function_142_13194",      # 8E, 142
        "Function_143_138C9",      # 8F, 143
        "Function_144_13938",      # 90, 144
        "Function_145_1399E",      # 91, 145
        "Function_146_13A04",      # 92, 146
        "Function_147_13A6A",      # 93, 147
        "Function_148_13AD0",      # 94, 148
        "Function_149_13B36",      # 95, 149
        "Function_150_13DF7",      # 96, 150
    ))


    def Function_0_1300(): pass

    label("Function_0_1300")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1338"),
        (1, "loc_1344"),
        (2, "loc_1350"),
        (3, "loc_135C"),
        (4, "loc_1368"),
        (5, "loc_1374"),
        (6, "loc_1380"),
        (SWITCH_DEFAULT, "loc_138C"),
    )


    label("loc_1338")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1398")

    label("loc_1344")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1398")

    label("loc_1350")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1398")

    label("loc_135C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1398")

    label("loc_1368")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1398")

    label("loc_1374")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1398")

    label("loc_1380")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1398")

    label("loc_138C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1398")

    label("loc_1398")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13AF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1398")

    label("loc_13AF")

    Return()

    # Function_0_1300 end

    def Function_1_13B0(): pass

    label("Function_1_13B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1444")
    OP_95(0xFE, 10070, 0, 6000, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(300)
    OP_95(0xFE, 21680, 300, 6000, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(300)
    OP_95(0xFE, 21680, 300, -6750, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(300)
    OP_95(0xFE, 10070, 300, -12420, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    Jump("Function_1_13B0")

    label("loc_1444")

    Return()

    # Function_1_13B0 end

    def Function_2_1445(): pass

    label("Function_2_1445")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_14D9")
    OP_95(0xFE, -10830, 300, -12520, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -21560, 300, -6130, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -21560, 300, 5320, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -10830, 0, 5320, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(300)
    Jump("Function_2_1445")

    label("loc_14D9")

    Return()

    # Function_2_1445 end

    def Function_3_14DA(): pass

    label("Function_3_14DA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1504")
    OP_94(0xFE, 0x2AEE, 0xFFFFD800, 0x3E30, 0xFFFFD382, 0x3E8)
    Sleep(300)
    Jump("Function_3_14DA")

    label("loc_1504")

    Return()

    # Function_3_14DA end

    def Function_4_1505(): pass

    label("Function_4_1505")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1599")
    OP_95(0xFE, -5600, 250, 3020, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -10570, 0, 3180, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -5330, 0, -3700, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -10720, 0, -3700, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(300)
    Jump("Function_4_1505")

    label("loc_1599")

    Return()

    # Function_4_1505 end

    def Function_5_159A(): pass

    label("Function_5_159A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_15EC")
    OP_95(0xFE, -21660, 300, 20300, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -21660, 300, -7500, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    Jump("Function_5_159A")

    label("loc_15EC")

    Return()

    # Function_5_159A end

    def Function_6_15ED(): pass

    label("Function_6_15ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_163F")
    OP_95(0xFE, 21300, 300, -9300, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    OP_95(0xFE, 21300, 300, 21000, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(300)
    Jump("Function_6_15ED")

    label("loc_163F")

    Return()

    # Function_6_15ED end

    def Function_7_1640(): pass

    label("Function_7_1640")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1732")
    OP_95(0xFE, 14560, 0, 5730, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(1000)
    OP_95(0xFE, 8390, 250, 4070, 2000, 0x0)
    OP_95(0xFE, 6130, 250, 4070, 2000, 0x0)
    OP_95(0xFE, 140, 100, 4000, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(300)
    OP_95(0xFE, 6130, 250, 4070, 2000, 0x0)
    OP_95(0xFE, 8390, 250, 4070, 2000, 0x0)
    Jump("Function_7_1640")

    label("loc_1732")

    Return()

    # Function_7_1640 end

    def Function_8_1733(): pass

    label("Function_8_1733")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1751")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_8_1733")

    label("loc_1751")

    Return()

    # Function_8_1733 end

    def Function_9_1752(): pass

    label("Function_9_1752")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_176E")
    OP_A1(0xFE, 0x2BC, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_9_1752")

    label("loc_176E")

    Return()

    # Function_9_1752 end

    def Function_10_176F(): pass

    label("Function_10_176F")

    SetMapObjFlags(0x10, 0x2000000)
    SetMapObjFlags(0x11, 0x2000000)
    SetMapObjFlags(0x12, 0x2000000)
    SetMapObjFlags(0x13, 0x2000000)
    SetMapObjFlags(0x16, 0x2000000)
    SetMapObjFlags(0x14, 0x2000000)
    SetMapObjFlags(0x15, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_17CA")
    ClearMapObjFlags(0x10, 0x2000000)
    ClearMapObjFlags(0x11, 0x2000000)
    SetMapObjFlags(0xA, 0x2000000)
    SetMapObjFlags(0xB, 0x2000000)
    SetMapObjFlags(0xC, 0x2000000)
    SetMapObjFlags(0xE, 0x2000000)

    label("loc_17CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_180D")
    ClearMapObjFlags(0x12, 0x2000000)
    ClearMapObjFlags(0x13, 0x2000000)
    ClearMapObjFlags(0x16, 0x2000000)
    ClearMapObjFlags(0x14, 0x2000000)
    ClearMapObjFlags(0x15, 0x2000000)
    SetMapObjFlags(0xA, 0x2000000)
    SetMapObjFlags(0xB, 0x2000000)
    SetMapObjFlags(0xC, 0x2000000)
    SetMapObjFlags(0xE, 0x2000000)

    label("loc_180D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_END)), "loc_1822")
    ClearMapObjFlags(0x12, 0x2000000)
    ClearMapObjFlags(0x13, 0x2000000)

    label("loc_1822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 2)), scpexpr(EXPR_END)), "loc_1831")
    ClearMapObjFlags(0x13, 0x2000000)

    label("loc_1831")

    Return()

    # Function_10_176F end

    def Function_11_1832(): pass

    label("Function_11_1832")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_190F")
    SetChrPos(0x0, 0, -4930, -40200, 0)
    SetChrPos(0x1, 0, -4930, -40200, 0)
    SetChrPos(0x2, 0, -4930, -40200, 0)
    SetChrPos(0x3, 0, -4930, -40200, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18B9")
    SetChrPos(0x4, 0, -4930, -40200, 0)
    SetChrPos(0x5, 0, -4930, -40200, 0)
    Jump("loc_18D8")

    label("loc_18B9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18D8")
    SetChrPos(0x4, 0, -4930, -40200, 0)

    label("loc_18D8")

    OP_68(0, -2430, -40200, 0)
    MoveCamera(0, 2, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(19000, 0)
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_190F")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_19C8")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 12310, 300, -14690, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x22, 0x40)
    ClearChrFlags(0x23, 0x40)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1973")
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0x21, 0x10)
    SetChrFlags(0x22, 0x10)
    SetChrFlags(0x23, 0x10)

    label("loc_1973")

    BeginChrThread(0x22, 0, 0, 0)
    BeginChrThread(0x23, 0, 0, 0)
    SetChrPos(0x11, 4840, 250, 3840, 45)
    SetChrPos(0x21, 5390, 250, 6320, 135)
    SetChrPos(0x22, 7580, 250, 5850, 225)
    SetChrPos(0x23, 8310, 250, 4150, 315)
    Jump("loc_1C02")

    label("loc_19C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_19E0")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_1C02")

    label("loc_19E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_19F8")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_1C02")

    label("loc_19F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1A3C")
    ClearChrFlags(0x20, 0x80)
    SetChrChipByIndex(0x20, 0x10)
    SetChrSubChip(0x20, 0x0)
    EndChrThread(0x20, 0x0)
    SetChrBattleFlags(0x20, 0x4)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x12, 0x5)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    Jump("loc_1C02")

    label("loc_1A3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1A87")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x12, 0x5)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    OP_93(0x16, 0x5A, 0x0)
    OP_93(0x17, 0x5A, 0x0)
    Jump("loc_1C02")

    label("loc_1A87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1A9F")
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jump("loc_1C02")

    label("loc_1A9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1AD7")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x12, 0x5)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_1C02")

    label("loc_1AD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1B0F")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x12, 0x5)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_1C02")

    label("loc_1B0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1B47")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x12, 0x5)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_1C02")

    label("loc_1B47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1B82")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x1F, 0x80)
    Jump("loc_1C02")

    label("loc_1B82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1BDD")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x12, 0x5)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jump("loc_1C02")

    label("loc_1BDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1BEB")
    Jump("loc_1C02")

    label("loc_1BEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1BF9")
    Jump("loc_1C02")

    label("loc_1BF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1C02")

    label("loc_1C02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1C19")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 7)
    Event(0, 46)
    Jump("loc_1CE2")

    label("loc_1C19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_1C2D")
    ClearScenarioFlags(0x22, 1)
    Event(0, 51)
    Jump("loc_1CE2")

    label("loc_1C2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1C44")
    ClearScenarioFlags(0x22, 2)
    SetScenarioFlags(0x0, 7)
    Event(0, 60)
    Jump("loc_1CE2")

    label("loc_1C44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_1C58")
    ClearScenarioFlags(0x22, 3)
    Event(0, 61)
    Jump("loc_1CE2")

    label("loc_1C58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_1C6F")
    ClearScenarioFlags(0x22, 4)
    SetScenarioFlags(0x0, 7)
    Event(0, 64)
    Jump("loc_1CE2")

    label("loc_1C6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_1C83")
    ClearScenarioFlags(0x22, 5)
    Event(0, 66)
    Jump("loc_1CE2")

    label("loc_1C83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_1C97")
    ClearScenarioFlags(0x22, 6)
    Event(0, 69)
    Jump("loc_1CE2")

    label("loc_1C97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 7)), scpexpr(EXPR_END)), "loc_1CAB")
    ClearScenarioFlags(0x22, 7)
    Event(0, 70)
    Jump("loc_1CE2")

    label("loc_1CAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_END)), "loc_1CBF")
    ClearScenarioFlags(0x23, 0)
    Event(0, 142)
    Jump("loc_1CE2")

    label("loc_1CBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_END)), "loc_1CD3")
    ClearScenarioFlags(0x23, 1)
    Event(0, 149)
    Jump("loc_1CE2")

    label("loc_1CD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 2)), scpexpr(EXPR_END)), "loc_1CE2")
    ClearScenarioFlags(0x23, 2)
    Event(0, 150)

    label("loc_1CE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D06")
    SetMapFlags(0x10000000)
    Event(0, 44)
    Jump("loc_1D3C")

    label("loc_1D06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D21")
    SetMapFlags(0x10000000)
    Event(0, 58)
    Jump("loc_1D3C")

    label("loc_1D21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D3C")
    SetMapFlags(0x10000000)
    Event(0, 56)

    label("loc_1D3C")

    Return()

    # Function_11_1832 end

    def Function_12_1D3D(): pass

    label("Function_12_1D3D")

    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF032877), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0x1C2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1D5F")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 7)

    label("loc_1D5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D78")
    OP_10(0x0, 0x0)
    OP_10(0x2, 0x1)
    Jump("loc_1D7E")

    label("loc_1D78")

    OP_10(0x0, 0x1)
    OP_10(0x2, 0x0)

    label("loc_1D7E")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D96")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1D96")

    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2_add", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1ECC")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x1F4, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Sound(128, 1, 100, 0)

    label("loc_1ECC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1F4E")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x1E, 0x276, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)

    label("loc_1F4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_END)), "loc_1F5D")
    SetMapObjFlags(0x9, 0x4)

    label("loc_1F5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F85")
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x2)
    SetMapObjFrame(0xC, "mark01", 0x0, 0x1)

    label("loc_1F85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2022")
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x25, 0x4)
    OP_78(0xC, 0x25)
    SetMapObjFlags(0xC, 0x1000)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x2)
    OP_D5(0x25, 0x0, 0x36EE8, 0x0, 0x0)
    SetMapObjFrame(0xC, "mark00", 0x0, 0x1)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x26, 0x4)
    OP_78(0xE, 0x26)
    SetMapObjFlags(0xE, 0x1000)
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x2)
    OP_D5(0x26, 0x0, 0x27100, 0x0, 0x0)
    SetMapObjFrame(0xE, "mark00", 0x0, 0x1)
    SetMapObjFlags(0xF, 0x1000)
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xF, 0x2)

    label("loc_2022")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2033")
    OP_66(0x0, 0x1)

    label("loc_2033")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_204B")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_204B")

    Return()

    # Function_12_1D3D end

    def Function_13_204C(): pass

    label("Function_13_204C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_20DF")

    ChrTalk(
        0xFE,
        (
            "Defense Forces soldiers also withdrew in general,\x01",
            "We guard department again\x01",
            "It was decided to be deployed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's a hard situation, but let's keep up with each other.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2998")

    label("loc_20DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_20ED")
    Jump("loc_2998")

    label("loc_20ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_20FB")
    Jump("loc_2998")

    label("loc_20FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_22D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2219")

    ChrTalk(
        0xFE,
        (
            "Battle in front of the Orkis Tower ……\x01",
            "It was a very fighting battle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honestly without Arios,\x01",
            "Like IBC here ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Well done.\x01",
            "Tell me yourself\x01",
            "Something's getting horrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyhow, it was safe here.\x01",
            "There is no point in thinking any further.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_22CE")

    label("loc_2219")


    ChrTalk(
        0xFE,
        (
            "However, Mr. Dudley is also awesome … …\x01",
            "To Arios-san, with us\x01",
            "It was as if the strength was different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dynamism to the sword speed which can be said as a supernatural work … …\x01",
            "I said well as \"the sword of the wind\".\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22CE")

    Jump("loc_2998")

    label("loc_22D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2381")

    ChrTalk(
        0xFE,
        (
            "Occupied case in Mainz, or …\x01",
            "Cuddly, also ridiculous things\x01",
            "It happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems pretty rugged,\x01",
            "Anything in the guard\x01",
            "I hope you have a step.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2998")

    label("loc_2381")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_240B")

    ChrTalk(
        0xFE,
        (
            "On a rainy day,\x01",
            "Popular also in this square#4ROne person#It will not run out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it is such a wide place,\x01",
            "Somehow I feel sadness alone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2998")

    label("loc_240B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_24AE")

    ChrTalk(
        0xFE,
        (
            "I heard it at the reception earlier,\x01",
            "Everything seems that the train derailed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Investigations 2 and the guard already have\x01",
            "She seems to have gone to the survey … …\x01",
            "I wonder how much damage it is.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2998")

    label("loc_24AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_25C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2561")

    ChrTalk(
        0xFE,
        (
            "Also the square in front of this tower\x01",
            "As a place for citizens to relax,\x01",
            "It seems that it has become established.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am playing with friends\x01",
            "While watching something with my family,\x01",
            "I am feeling heartwarming.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_25C3")

    label("loc_2561")


    ChrTalk(
        0xFE,
        (
            "With sunny sunshine,\x01",
            "A mumberful family ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, so much\x01",
            "There is no picture of a warm heart.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25C3")

    Jump("loc_2998")

    label("loc_25C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2785")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26FB")

    ChrTalk(
        0xFE,
        (
            "Since the trade meeting has ended,\x01",
            "It's already been more than a month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The attacks of terrorists as well\x01",
            "Of course it was a major incident,\x01",
            "Immediately after the independent advocacy was done ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, really this year\x01",
            "Great incidents and incidents in rapid succession\x01",
            "It will happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Somehow, freshness\x01",
            "I feel the date in no time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2780")

    label("loc_26FB")


    ChrTalk(
        0xFE,
        (
            "Anyway, really this year\x01",
            "Great incidents and incidents in rapid succession\x01",
            "It will happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Somehow, freshness\x01",
            "I feel the date in no time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2780")

    Jump("loc_2998")

    label("loc_2785")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2881")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_281F")

    ChrTalk(
        0xFE,
        "It seems that it is a special support department.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You guard against the trade council\x01",
            "I am listening to participate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, please come inside.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_287C")

    label("loc_281F")


    ChrTalk(
        0xFE,
        (
            "You guard against the trade council\x01",
            "I am listening to participate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, please come inside.\x02",
    )

    CloseMessageWindow()

    label("loc_287C")

    Jump("loc_2998")

    label("loc_2881")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2998")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_292C")

    ChrTalk(
        0xFE,
        "Oh, you guys are special affairs support department.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Orkis Tower\x01",
            "We are in charge of the security department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, mutual police,\x01",
            "When something happens I will ask you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2998")

    label("loc_292C")


    ChrTalk(
        0xFE,
        (
            "The Orkis Tower\x01",
            "We are in charge of the security department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, mutual police,\x01",
            "When something happens I will ask you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2998")

    TalkEnd(0xFE)
    Return()

    # Function_13_204C end

    def Function_14_299C(): pass

    label("Function_14_299C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2A3C")

    ChrTalk(
        0xFE,
        (
            "President Dieter,\x01",
            "It is bound by 36F.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No way, the country where we live\x01",
            "It is supposed to detain the top.\x01",
            "…… I do not feel good.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3356")

    label("loc_2A3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2A4A")
    Jump("loc_3356")

    label("loc_2A4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2A58")
    Jump("loc_3356")

    label("loc_2A58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2B8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B22")

    ChrTalk(
        0xFE,
        (
            "\"Red constellation\" ……\x01",
            "…… It was a really scary guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Individual battle techniques as well as,\x01",
            "The difference in arms is also evident ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If there is an army in the crossbell,\x01",
            "The situation was supposed to be different … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B88")

    label("loc_2B22")


    ChrTalk(
        0xFE,
        (
            "\"Red constellation\" ……\x01",
            "…… It was a really scary guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But if\x01",
            "If there is an army on the crossbell ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B88")

    Jump("loc_3356")

    label("loc_2B8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2D51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CA0")

    ChrTalk(
        0xFE,
        (
            "Because it is such a situation time\x01",
            "We police are dignified for citizens\x01",
            "I have to set it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Like guards, we are daily\x01",
            "I am training for that\x01",
            "That's it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "\"Always a citizen's example\"\x01",
            "Again reckon this word\x01",
            "Let's scream each other.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2D4C")

    label("loc_2CA0")


    ChrTalk(
        0xFE,
        (
            "Because it is such a situation time\x01",
            "We police are dignified for citizens\x01",
            "I have to set it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "\"Always a citizen's example\"\x01",
            "Again reckon this word\x01",
            "Let's scream each other.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D4C")

    Jump("loc_3356")

    label("loc_2D51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2E11")

    ChrTalk(
        0xFE,
        (
            "For the transcontinental railroad, with the success of the guard\x01",
            "Somehow within yesterday\x01",
            "It is said that it was able to recover.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it had been raining this day,\x01",
            "I think that there were various troublesome … …\x01",
            "Respect for rapid response.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3356")

    label("loc_2E11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2EA4")

    ChrTalk(
        0xFE,
        (
            "On the West Crossbell Highway\x01",
            "Does the guiding train derail? …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With this crossbell\x01",
            "Although it is a rare accident,\x01",
            "What on earth was happening?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3356")

    label("loc_2EA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2F69")

    ChrTalk(
        0xFE,
        (
            "The operation of the Orkis Tower is more\x01",
            "If you get into full swing, people in this square will also come in and out\x01",
            "You will be more active.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If that happens, even if work gets busy\x01",
            "I am pleased as one crossbell person.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3356")

    label("loc_2F69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3166")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30C3")

    ChrTalk(
        0xFE,
        (
            "It seems to steam it,\x01",
            "In the terrorist case of the trade council\x01",
            "It was truly a misunderstanding taken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our police force is defending against us,\x01",
            "Ultimately the two major powers will\x01",
            "As a result of relying on the military equipped ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And also this time security\x01",
            "It is a story that it was taken by the other way … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a matter of course further crisis management,\x01",
            "We also increase consciousness\x01",
            "It is necessary.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3161")

    label("loc_30C3")


    ChrTalk(
        0xFE,
        (
            "It is also stretched to double and triple,\x01",
            "A defense line that should have had a trust\x01",
            "Oh well too … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a matter of course further crisis management,\x01",
            "We also increase consciousness\x01",
            "It is necessary.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3161")

    Jump("loc_3356")

    label("loc_3166")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_31D7")

    ChrTalk(
        0xFE,
        "Good work today, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To ensure that the trade meeting ends safely,\x01",
            "Let's do our best with each other.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3356")

    label("loc_31D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3356")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32A6")

    ChrTalk(
        0xFE,
        (
            "Kanning patrol with me this time,\x01",
            "As a security guard at the Orkis Tower\x01",
            "It was decided to be assigned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not to mention the trade meeting,\x01",
            "Since I plan to pack this place after that\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3356")

    label("loc_32A6")


    ChrTalk(
        0xFE,
        (
            "Gather attention in the continents,\x01",
            "You can work in this Orkis Tower\x01",
            "I am very honored.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The state-of-the-art\x01",
            "Without compromising on security,\x01",
            "I am willing to fulfill my duty.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3356")

    TalkEnd(0xFE)
    Return()

    # Function_14_299C end

    def Function_15_335A(): pass

    label("Function_15_335A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_33EE")

    ChrTalk(
        0xFE,
        (
            "When the president came to such a thing,\x01",
            "Crossbell will be in the future\x01",
            "I wonder what's going on ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… Well, as possible only\x01",
            "Well, I guess.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CD0")

    label("loc_33EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_33FC")
    Jump("loc_3CD0")

    label("loc_33FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_340A")
    Jump("loc_3CD0")

    label("loc_340A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_35A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_351E")

    ChrTalk(
        0xFE,
        (
            "At the time of the raid, I was on the finance section floor\x01",
            "It was decided to evacuate to the basement … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone all elevators\x01",
            "I will not go using it,\x01",
            "The young men used the stairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way,\x01",
            "The finance section is at 31F.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… At that time\x01",
            "I was about to die because of shortness of breath.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_359C")

    label("loc_351E")


    ChrTalk(
        0xFE,
        (
            "No way, I took this high-rise building on the stairs\x01",
            "I did not expect to run down, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Somehow, from daily\x01",
            "It is important that you make physical strength.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_359C")

    Jump("loc_3CD0")

    label("loc_35A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_36E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3669")

    ChrTalk(
        0xFE,
        "Is the hunting corps and the guard engaged in battle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Also, although extra expenses are likely to increase … …\x01",
            "What a thing\x01",
            "It is not a case to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, as soon as possible\x01",
            "I pray the goddess of the convergence of the situation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_36DF")

    label("loc_3669")


    ChrTalk(
        0xFE,
        (
            "It was a big case recently\x01",
            "I will come down to the least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, as soon as possible\x01",
            "I pray the goddess of the convergence of the situation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36DF")

    Jump("loc_3CD0")

    label("loc_36E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_36F2")
    Jump("loc_3CD0")

    label("loc_36F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_385F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37D4")

    ChrTalk(
        0xFE,
        (
            "I do not understand something,\x01",
            "The train is stopped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Continental economic aorta outage … …\x01",
            "How serious I can not laugh It is a joke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not want you to be recovered early,\x01",
            "You will quickly become a big problem.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_385A")

    label("loc_37D4")


    ChrTalk(
        0xFE,
        (
            "Continental economic aorta outage … …\x01",
            "How serious I can not laugh It is a joke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not want you to be recovered early,\x01",
            "You will quickly become a big problem.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_385A")

    Jump("loc_3CD0")

    label("loc_385F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3917")

    ChrTalk(
        0xFE,
        (
            "Mayor Dieter said,\x01",
            "Without paying public expenses for entertainment expenses and travel expenses\x01",
            "I'm paying all on my own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is it the president of IBC?\x01",
            "In the case of that person, the area of fat\x01",
            "It is exceeding well beyond.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CD0")

    label("loc_3917")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3B3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A93")

    ChrTalk(
        0xFE,
        (
            "Crossbell to the state, … ….\x01",
            "Mayor Croise mayor\x01",
            "I do not think he was a bold person so far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because I am also in the finance section\x01",
            "The tax revenue transfer system hurts my head\x01",
            "I know that it is a problem … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anything related to subordinate countries is anyway\x01",
            "Even putting it out was a taboo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The two major powers are already obvious\x01",
            "I have a negative statement … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How both countries will move in the future,\x01",
            "I do not worry about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3B37")

    label("loc_3A93")


    ChrTalk(
        0xFE,
        (
            "Referendums are essential\x01",
            "Citizen's will to independence\x01",
            "Although it is said that it is a question … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Either way the two major powers\x01",
            "You can not have a good face.\x01",
            "I'm worried about the future of both countries' mobilization.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B37")

    Jump("loc_3CD0")

    label("loc_3B3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3B4A")
    Jump("loc_3CD0")

    label("loc_3B4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3CD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C38")

    ChrTalk(
        0xFE,
        (
            "Well, no doubt the Orkis Tower\x01",
            "I honestly will be completed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Spare the capital of IBC\x01",
            "Put in public works\x01",
            "Mayor Dieter's spirit ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just to fertilize my stomach\x01",
            "Dedicated members who are enthusiastic\x01",
            "Actors are different.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3CD0")

    label("loc_3C38")


    ChrTalk(
        0xFE,
        (
            "Spare the capital of IBC\x01",
            "Put in public works\x01",
            "Mayor Dieter's spirit ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just to fertilize my stomach\x01",
            "Dedicated members who are enthusiastic\x01",
            "Actors are different.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CD0")

    TalkEnd(0xFE)
    Return()

    # Function_15_335A end

    def Function_16_3CD4(): pass

    label("Function_16_3CD4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3E0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DA6")

    ChrTalk(
        0xFE,
        (
            "Finally \"Orchis Tower\"\x01",
            "To its citizens … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This prospect that also reaches the sky,\x01",
            "And it was based on blue and white\x01",
            "The appearance is really beautiful …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Again, undertaking the design\x01",
            "It is very nice……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3E08")

    label("loc_3DA6")


    ChrTalk(
        0xFE,
        (
            "The design of the 40th floor building above ground\x01",
            "It was extremely difficult … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Umm …\x01",
            "Do not get your eyes getting hot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E08")

    Jump("loc_3E16")

    label("loc_3E0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3E16")

    label("loc_3E16")

    TalkEnd(0xFE)
    Return()

    # Function_16_3CD4 end

    def Function_17_3E1A(): pass

    label("Function_17_3E1A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E2F")
    Call(0, 21)
    Jump("loc_3E99")

    label("loc_3E2F")


    ChrTalk(
        0xFE,
        (
            "By the way, Kea - chan,\x01",
            "is it OK……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On the roof of a department store,\x01",
            "It looked kinda like hen … ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E99")

    TalkEnd(0xFE)
    Return()

    # Function_17_3E1A end

    def Function_18_3E9D(): pass

    label("Function_18_3E9D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EB2")
    Call(0, 21)
    Jump("loc_3F38")

    label("loc_3EB2")


    ChrTalk(
        0xFE,
        (
            "Singh, language is erotic though\x01",
            "Roots are like good fellows.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard he will return tomorrow,\x01",
            "I have to play a cup at the moment.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F38")

    TalkEnd(0xFE)
    Return()

    # Function_18_3E9D end

    def Function_19_3F3C(): pass

    label("Function_19_3F3C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F51")
    Call(0, 21)
    Jump("loc_3FC9")

    label("loc_3F51")


    ChrTalk(
        0xFE,
        (
            "Anyway, the Orchise Tower ……\x01",
            "Than I imagined\x01",
            "It was a cool building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'd love to go inside as long as I can.\x02",
    )

    CloseMessageWindow()

    label("loc_3FC9")

    TalkEnd(0xFE)
    Return()

    # Function_19_3F3C end

    def Function_20_3FCD(): pass

    label("Function_20_3FCD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FE2")
    Call(0, 21)
    Jump("loc_4063")

    label("loc_3FE2")


    ChrTalk(
        0xFE,
        (
            "Fun\x01",
            "Because Bonzoku is this, I am in trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyways……\x01",
            "For my brighter future as well,\x01",
            "I have to sit well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4063")

    TalkEnd(0xFE)
    Return()

    # Function_20_3FCD end

    def Function_21_4067(): pass

    label("Function_21_4067")

    OP_4B(0x1E, 0xFF)
    OP_4B(0x1B, 0xFF)
    OP_4B(0x1C, 0xFF)
    OP_4B(0x1D, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_41FB")

    ChrTalk(
        0x101,
        "#00005FWell, is not it?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x101, 500)

    ChrTalk(
        0x1E,
        (
            "Ah……\x01",
            "You guys were yesterday!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x102, 500)

    ChrTalk(
        0x1E,
        "Hello, older sister! It is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FHuhu, Hello,\x01",
            "You were with Ryu guys?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Well, that's right.\x01",
            "I guess they do not do it\x01",
            "Since it says it's useless … …\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x1E, 500)

    ChrTalk(
        0x1B,
        "You do not have to tell me ~ ~?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Ka'a and Shizuku got home\x01",
            "Because I looked sad,\x01",
            "You put it in a group.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45CF")

    label("loc_41FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4447")

    ChrTalk(
        0x101,
        "#00005FWell, you sure are … Shin?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x101, 500)

    ChrTalk(
        0x1E,
        (
            "Ah……\x01",
            "You guys were yesterday!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Without accepting my guidance,\x01",
            "What were you doing! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FSorry, Shin.\x01",
            "Well we too\x01",
            "I can not take my hand …\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x102, 500)

    ChrTalk(
        0x1E,
        (
            "Oooh … well, that.\x01",
            "I took up my older sister … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "…… Hun, oh well.\x01",
            "The guidance of the subordinates was not interesting,\x01",
            "I could do sightseeings of the city all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FEven today, today\x01",
            "It was with the shoguns.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x104, 500)

    ChrTalk(
        0x1B,
        (
            "Oh, on the roof of a department store\x01",
            "Together with the unveiling ceremony,\x01",
            "It is playing as it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Somehow it seemed to be alone for one person\x01",
            "You put it in a group.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45CF")

    label("loc_4447")


    ChrTalk(
        0x101,
        (
            "#00002FHey, are not they Ryuu?\x02\x03",
            "#00005F… …. that, what is that?\x01",
            "You have an unfamiliar child?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x0, 500)

    ChrTalk(
        0x1E,
        (
            "What are you guys.\x01",
            "Do you know Ryu?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "OK, this is black ──\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x0, 500)

    ChrTalk(
        0x1B,
        (
            "Well, I do not quite understand it\x01",
            "It seems like a traveler from the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "On the roof of a department store\x01",
            "Because I was watching the unveiling ceremony together,\x01",
            "It is playing as it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Somehow it seemed to be alone for one person\x01",
            "You put it in a group.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45CF")

    TurnDirection(0x1E, 0x1B, 500)

    ChrTalk(
        0x1E,
        (
            "But, who was lonely ……\x01",
            "Let's stop saying words!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Oh, you did it!\x01",
            "Hey, Momo, were you doing?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x1D, 500)

    ChrTalk(
        0x1D,
        "Uh, um, that … …\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x1B, 500)

    ChrTalk(
        0x1C,
        (
            "Wait a minute,\x01",
            "Please do not tease!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_46FA")

    ChrTalk(
        0x101,
        (
            "#00002F(Hello, what is it?\x01",
            "It seems familiar. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_472B")

    label("loc_46FA")


    ChrTalk(
        0x101,
        "#00002F(Hey, you seem to be playing with each other.\x02",
    )

    CloseMessageWindow()

    label("loc_472B")

    OP_93(0x1E, 0xE1, 0x0)
    OP_93(0x1B, 0x87, 0x0)
    OP_93(0x1C, 0x10E, 0x0)
    OP_93(0x1D, 0x5A, 0x0)
    OP_4C(0x1E, 0xFF)
    OP_4C(0x1B, 0xFF)
    OP_4C(0x1C, 0xFF)
    OP_4C(0x1D, 0xFF)
    SetScenarioFlags(0x159, 2)
    Return()

    # Function_21_4067 end

    def Function_22_475B(): pass

    label("Function_22_475B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_47F4")

    ChrTalk(
        0xFE,
        (
            "For now, the signs of terrorists\x01",
            "I do not feel it here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can not imagine coming from the front to drift … …\x01",
            "Anyway continue to keep alert.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_486F")

    label("loc_47F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_486F")

    ChrTalk(
        0xFE,
        (
            "Hi, Hello.\x01",
            "Is this place a very nice place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the new sights of Crossbell\x01",
            "There is no mistake.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_486F")

    TalkEnd(0xFE)
    Return()

    # Function_22_475B end

    def Function_23_4873(): pass

    label("Function_23_4873")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4903")

    ChrTalk(
        0xFE,
        (
            "Today Orkis Tower is full,\x01",
            "Access other than stakeholders\x01",
            "I restrict it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You guys are mission support department.\x01",
            "Please come along.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_496F")

    label("loc_4903")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_496F")

    ChrTalk(
        0xFE,
        "Welcome to Orkis Tower.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As entering and leaving the square is free\x01",
            "Please drop by if you do not mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_496F")

    TalkEnd(0xFE)
    Return()

    # Function_23_4873 end

    def Function_24_4973(): pass

    label("Function_24_4973")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Good work everyone.\x01",
            "There is no abnormality in the square.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_4973 end

    def Function_25_49AF(): pass

    label("Function_25_49AF")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Finally, finally\x01",
            "The plenary session will be held.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was a bit nervous … …\x01",
            "I have to relax.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_49AF end

    def Function_26_4A16(): pass

    label("Function_26_4A16")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Good, the leaders\x01",
            "Please give me a smile when you greet me\x01",
            "Do not be rude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it should be coarse\x01",
            "If it works you can not have our head\x01",
            "It will blow away in a moment.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_4A16 end

    def Function_27_4ABD(): pass

    label("Function_27_4ABD")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Director, manager,\x01",
            "I know that way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Pressure badly\x01",
            "Please do not put it.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_4ABD end

    def Function_28_4B26(): pass

    label("Function_28_4B26")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4F28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B44")
    Call(0, 30)
    Jump("loc_4F23")

    label("loc_4B44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E93")

    ChrTalk(
        0x11,
        "#07902FEveryone …… And Randy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FYeah, Mireille.\x01",
            "It seems that the unit was able to recover safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#07904FWell, thanks to you.\x02\x03",
            "#07902FWe leave the corps with discipline,\x01",
            "The commander greeted me well.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4CB2")

    ChrTalk(
        0x109,
        (
            "#10100FHuhu, if you are Sonya commander\x01",
            "I think that it is a matter of course.\x02\x03",
            "Excellent people like the three lieutenant Mireille\x01",
            "It would be the situation I want even one person … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D30")

    label("loc_4CB2")


    ChrTalk(
        0x103,
        (
            "#00204FUnique to Sonya command\x01",
            "It is flexible correspondence.\x02\x03",
            "#00202FExcellent people like the three lieutenant Mireille\x01",
            "It would be the situation I want even one person … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D30")


    ChrTalk(
        0x11,
        (
            "#07904FHehe, whether it is excellent\x01",
            "I do not know but …\x02\x03",
            "#07902FAs I returned,\x01",
            "I will do my best.\x02\x03",
            "Before being a defense army or guard,\x01",
            "Having a mission to protect the crossbell\x01",
            "As a human being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FGo for it, Mireille.\x02\x03",
            "#00309FWell, it's too tight\x01",
            "Do not run around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#07906FNo, I do not even have to tell you!\x01",
            "…… Ridiculous idiot!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AE, 2)
    Jump("loc_4F23")

    label("loc_4E93")


    ChrTalk(
        0x11,
        (
            "#07902FAs I returned,\x01",
            "I will do my best.\x02\x03",
            "Before being a defense army or guard,\x01",
            "Having a mission to protect the crossbell\x01",
            "As a human being.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F23")

    Jump("loc_4FBB")

    label("loc_4F28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4FBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F43")
    Call(0, 45)
    Jump("loc_4FBB")

    label("loc_4F43")


    ChrTalk(
        0x11,
        (
            "#07903FWe also organized troops\x01",
            "I am sure to come running from there.\x02\x03",
            "#07901FSo everyone ……\x01",
            "Please do as you please that foolish thing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FBB")

    TalkEnd(0xFE)
    Return()

    # Function_28_4B26 end

    def Function_29_4FBF(): pass

    label("Function_29_4FBF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FD4")
    Call(0, 30)
    Jump("loc_546D")

    label("loc_4FD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52CE")

    ChrTalk(
        0x22,
        (
            "#02501FThe influence that Dieter had been restrained,\x01",
            "It will spread to domestic and overseas soon.\x02\x03",
            "Even if we take this situation,\x01",
            "From now on, to crossbell\x01",
            "A lot of hardships will be waiting.\x02\x03",
            "#02503F…… I think, to Dieter\x01",
            "Crubel's burden of the future\x01",
            "Perhaps it was overdressed.\x02\x03",
            "As one of the autonomous state representatives,\x01",
            "Was it something you managed to do before this happened …?\x01",
            "I do not feel my powerlessness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108FGrandpa …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F…… Regarding this matter,\x01",
            "That's the whole crossbell\x01",
            "I think that was a problem.\x02\x03",
            "#00000FWhat are you going to do …?\x01",
            "That is important, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "#02503F…… Well, that's right.\x02\x03",
            "#02500FAnyway, now the problem in front of me\x01",
            "Let's say we solve each one.\x02\x03",
            "To young you guys\x01",
            "I will make a hard time but … ….\x01",
            "Please lend me your power for a while.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AE, 3)
    Jump("loc_546D")

    label("loc_52CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53CA")

    ChrTalk(
        0x22,
        (
            "#02503FAnyway, now the problem in front of me\x01",
            "Let's say we solve each one.\x02\x03",
            "#02500FAs a representative of the cross-bell autonomous state,\x01",
            "I have to settle this situation at all costs.\x02\x03",
            "To young you guys\x01",
            "I will make a hard time but … ….\x01",
            "Please lend me your power for a while.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_546D")

    label("loc_53CA")


    ChrTalk(
        0x22,
        (
            "#02503FAnyway, now the problem in front of me\x01",
            "Let's say we solve each one.\x02\x03",
            "#02500FTo young you guys\x01",
            "I will make a hard time but … ….\x01",
            "Please lend me your power for a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_546D")

    TalkEnd(0xFE)
    Return()

    # Function_29_4FBF end

    def Function_30_5471(): pass

    label("Function_30_5471")

    OP_4B(0x22, 0xFF)
    OP_4B(0x21, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_4B(0x23, 0xFF)

    ChrTalk(
        0x22,
        (
            "#02503FThe rumor that the president was detained\x01",
            "It seems that it already spreads both inside and outside.\x02\x03",
            "#02500FWe are also wary of two major powers\x01",
            "I can not neglect it … but …\x01",
            "…… What is the situation in each place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "Again, to the emergence of that \"Taiki\"\x01",
            "There is confusion in every direction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "Also, due to the effect that barrier disappeared\x01",
            "Citizens who wish to go to Ursula hospital\x01",
            "It seems that many people are out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "With regard to that, Mr. Mireille to three\x01",
            "We have instructed correspondence ahead of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#07903FRegarding the visits to and from the city\x01",
            "Put a platoon into each road\x01",
            "We are increasing the escorts of moving vehicles.\x02\x03",
            "#07900FCurrently under the President's restriction\x01",
            "Transportation of citizens several times is possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "#02503FHmm, thank you for your prompt response.\x02\x03",
            "#02500FI am the chairman of the autonomous state legislature\x01",
            "On the public place, on President's detention\x01",
            "You will need to explain.\x02\x03",
            "Already towards the city hall\x01",
            "I prepared arrangements for the press conference … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "#01002FRegarding that, the President prepared\x01",
            "Screen cars will also be available.\x02\x03",
            "You should share it with the police in the city\x01",
            "Shall I prepare?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "#02503FI'm sorry, I will ask for your kindness.\x02\x03",
            "#02501FWe can not neglect warning to two major powers … …\x01",
            "Please be careful enough for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F(McDowell's chairman\x01",
            "To respond to each direction\x01",
            "It looks like I'm being chased. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(Here for the grandparents\x01",
            "It will be okay to leave it. )\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x22, 0xFF)
    OP_4C(0x21, 0xFF)
    OP_4C(0x11, 0xFF)
    OP_4C(0x23, 0xFF)
    ClearChrFlags(0x11, 0x10)
    ClearChrFlags(0x21, 0x10)
    ClearChrFlags(0x22, 0x10)
    ClearChrFlags(0x23, 0x10)
    SetScenarioFlags(0x1AE, 1)
    Return()

    # Function_30_5471 end

    def Function_31_591D(): pass

    label("Function_31_591D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5932")
    Call(0, 30)
    Jump("loc_5E3F")

    label("loc_5932")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C9C")

    ChrTalk(
        0x23,
        (
            "#01002FAre you …?\x01",
            "What happened, what happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FNo, this situation is\x01",
            "I wondered what was going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "#01003FWell, as you can see\x01",
            "We are in talks with each other in the future.\x02\x03",
            "#01001FI also as a liaison by the police\x01",
            "I am going to go over here.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A7B")

    ChrTalk(
        0x10A,
        (
            "#00604FHM……\x01",
            "Sergei's would be a good candidate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AAA")

    label("loc_5A7B")


    ChrTalk(
        0x103,
        "#00204FIndeed, it seems that the section chief is qualified.\x02",
    )

    CloseMessageWindow()

    label("loc_5AAA")


    ChrTalk(
        0x104,
        (
            "#00300FThat's right ……\x01",
            "Is the support section getting rattled?\x01",
            "Is not there a request or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "#01002FRequests made from various places from here\x01",
            "Although it contains a lot, they are\x01",
            "I decided to leave it to the guild.\x02\x03",
            "#01004FYou guys are asking\x01",
            "There is no need to worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FOh really……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FIf you can leave it to the guild\x01",
            "We are safe too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "#01004FAnyway, you guys are\x01",
            "Come until you are satisfied.\x02\x03",
            "#01002FAs a \"mission support section\" ……\x01",
            "Above all, you as yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FYes……!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AE, 4)
    Jump("loc_5E3F")

    label("loc_5C9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DAB")

    ChrTalk(
        0x23,
        (
            "#01003F…… By the way,\x01",
            "In a room of Tower 36 F\x01",
            "I am in a state of detention.\x02\x03",
            "Current situation, evacuation is also postponed.\x01",
            "I do not seem to intend to resist,\x01",
            "I only have a minimum watch.\x02\x03",
            "#01002FWell, if you feel like it, you should visit us.\x01",
            "There will be stories that I can hear again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5E3F")

    label("loc_5DAB")


    ChrTalk(
        0x23,
        (
            "#01003FThe president is in a room of Tower 36F\x01",
            "I am in a state of detention.\x02\x03",
            "#01002FWell, if you feel like it, you should visit us.\x01",
            "There will be stories that I can hear again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E3F")

    TalkEnd(0xFE)
    Return()

    # Function_31_591D end

    def Function_32_5E43(): pass

    label("Function_32_5E43")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E58")
    Call(0, 30)
    Jump("loc_632C")

    label("loc_5E58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6198")

    ChrTalk(
        0x104,
        (
            "#00300FDouglas's Osan,\x01",
            "You came here.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5ECD")

    ChrTalk(
        0x109,
        "#10100FGood job, deputy commander!\x02",
    )

    CloseMessageWindow()

    label("loc_5ECD")


    ChrTalk(
        0xFE,
        (
            "You guys.\x01",
            "Haha, it's been a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Asked by Sonja Command,\x01",
            "As a representative of the Defense Forces side\x01",
            "I'm coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FIs that so.\x02\x03",
            "#00000FAnyway, that uniform ……\x01",
            "It is the first time for a defense army to appear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha ha, compared with the time of the guard\x01",
            "It will seem a little cramped … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Until a certain amount of corrections are made\x01",
            "It will be to act as it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F…. Again, the situation is pleasant\x01",
            "It does not seem to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh … … The barrier that wrapped the city and\x01",
            "As long as that \"god machine\" was also lost,\x01",
            "We should watch out for the two major powers strictly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Well, immediate invasion\x01",
            "It will not start,\x01",
            "Leave this to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You guys are only with you\x01",
            "Do what you can not do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah ….\x01",
            "Thank you for your consideration.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AE, 5)
    Jump("loc_632C")

    label("loc_6198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6297")

    ChrTalk(
        0xFE,
        (
            "Since the report of the president's detention arrived,\x01",
            "Command is kind of like to think occasionally\x01",
            "Show it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… She is a person with a strong sense of responsibility.\x01",
            "Perhaps including your own advances,\x01",
            "It seems that they are making various thoughts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a deputy commander, now firmly\x01",
            "I should support it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_632C")

    label("loc_6297")


    ChrTalk(
        0xFE,
        (
            "Soon the invasion of the two major powers\x01",
            "It will not start,\x01",
            "Leave this to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You guys are only with you\x01",
            "Do what you can not do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_632C")

    TalkEnd(0xFE)
    Return()

    # Function_32_5E43 end

    def Function_33_6330(): pass

    label("Function_33_6330")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64C7")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_63A1")

    ChrTalk(
        0x109,
        "#10105FAh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FCar used by support section ……\x01",
            "Have you been moved here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63E3")

    label("loc_63A1")


    ChrTalk(
        0x101,
        (
            "#00005FAh……\x02\x03",
            "Car used by support section ……\x01",
            "Have you been moved here?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63E3")


    ChrTalk(
        0x102,
        (
            "#00106FI'm sorry but ……\x01",
            "Leave this state for a while\x01",
            "It seems to be left alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWell, it's like this\x01",
            "Wait a minute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FOnce you arrive one by one,\x01",
            "I'm sure to fix it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, yes.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AE, 6)
    Jump("loc_659A")

    label("loc_64C7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6541")

    ChrTalk(
        0x109,
        (
            "#10100FWhen the case is over,\x01",
            "I'm sure to fix it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004FAh … … for now, good job.\x02",
    )

    CloseMessageWindow()
    Jump("loc_659A")

    label("loc_6541")


    ChrTalk(
        0x101,
        (
            "#00000FWhen the case is over,\x01",
            "I'm sure to repair it.\x02\x03",
            "#00004F… …. Good morning, good work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_659A")

    TalkEnd(0xFF)
    Return()

    # Function_33_6330 end

    def Function_34_659E(): pass

    label("Function_34_659E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_65AF")
    Jump("loc_690D")

    label("loc_65AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_669B")

    ChrTalk(
        0xFE,
        (
            "Me and my daughter, also during the raid\x01",
            "I was in this square … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When you are instructed to evacuate the building\x01",
            "I really did not feel alive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You guarded this guardian\x01",
            "To Arios and everyone else\x01",
            "I can not thank you enough.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_690D")

    label("loc_669B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6723")

    ChrTalk(
        0xFE,
        (
            "Today is also fine weather,\x01",
            "It is sad that it is an occupation case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why, this is\x01",
            "I wonder what will happen …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_690D")

    label("loc_6723")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6731")
    Jump("loc_690D")

    label("loc_6731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6790")

    ChrTalk(
        0xFE,
        "Well, it 's about time for lunch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even at the sandwich we brought\x01",
            "I should eat it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_690D")

    label("loc_6790")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_67EB")

    ChrTalk(
        0xFE,
        "Hehe, it's fine weather today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Orkis Tower in the clear sky\x01",
            "It shines well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_690D")

    label("loc_67EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6865")

    ChrTalk(
        0xFE,
        (
            "Huhu, after all\x01",
            "This square is a nice place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is a bit far from downtown,\x01",
            "I will definitely go there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_690D")

    label("loc_6865")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6873")
    Jump("loc_690D")

    label("loc_6873")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_690D")

    ChrTalk(
        0xFE,
        (
            "Huhu, whatever the unveiling ceremony here\x01",
            "I do not think I just had it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Such a wonderful place\x01",
            "I will release you from the first day\x01",
            "Mayor Dieter is also a big boy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_690D")

    TalkEnd(0xFE)
    Return()

    # Function_34_659E end

    def Function_35_6911(): pass

    label("Function_35_6911")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6922")
    Jump("loc_6B74")

    label("loc_6922")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_69A6")

    ChrTalk(
        0xFE,
        (
            "Arios is a person\x01",
            "People of Cassatsuto\x01",
            "You guarded me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Many things, Kansha ♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_6B74")

    label("loc_69A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6A04")

    ChrTalk(
        0xFE,
        (
            "Today is Mom, what?\x01",
            "I have a difficult face.\x01",
            "I want you to play GENKI … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B74")

    label("loc_6A04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6A12")
    Jump("loc_6B74")

    label("loc_6A12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6A46")

    ChrTalk(
        0xFE,
        "Gohan, gohan, duh gohan ♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_6B74")

    label("loc_6A46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6A97")

    ChrTalk(
        0xFE,
        (
            "Tenki, tenki, yi ten key ♪\x01",
            "Ame Ame's Furui, Ame Furu Nah ♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B74")

    label("loc_6A97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6AEB")

    ChrTalk(
        0xFE,
        (
            "Eh, today with mum\x01",
            "I came here so much.\x01",
            "Ruururu ♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B74")

    label("loc_6AEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6AF9")
    Jump("loc_6B74")

    label("loc_6AF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6B74")

    ChrTalk(
        0xFE,
        (
            "I'm excited.\x01",
            "When trying to see Choshi\x01",
            "The fish is it Itatata.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ita Tata, Tata, Tattatter ♪\x02",
    )

    CloseMessageWindow()

    label("loc_6B74")

    TalkEnd(0xFE)
    Return()

    # Function_35_6911 end

    def Function_36_6B78(): pass

    label("Function_36_6B78")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "………………………………\x01",
            "Huh ~~~~~~~~~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……… Only sighs came out.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_36_6B78 end

    def Function_37_6BD8(): pass

    label("Function_37_6BD8")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Well, indeed\x01",
            "It may not be possible to express.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Just being stunned.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_37_6BD8 end

    def Function_38_6C30(): pass

    label("Function_38_6C30")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6CD8")

    ChrTalk(
        0xFE,
        (
            "Something, the place of Mainz\x01",
            "It's become a serious thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not know well … ….\x01",
            "Without being caught quickly\x01",
            "You may as well go home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E2F")

    label("loc_6CD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6CE6")
    Jump("loc_6E2F")

    label("loc_6CE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6D35")

    ChrTalk(
        0xFE,
        (
            "Well, well, I ate for lunch.\x01",
            "I wonder if I should return to the city soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E2F")

    label("loc_6D35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6DAF")

    ChrTalk(
        0xFE,
        (
            "The rooftop of Orkis Tower\x01",
            "It is still not open to the public.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, sorry.\x01",
            "I have to come back again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E2F")

    label("loc_6DAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6E2F")

    ChrTalk(
        0xFE,
        (
            "Rumored Orchis Tower\x01",
            "I came to see … ….\x01",
            "It is more amazing than I imagined.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell\x01",
            "How rich is he?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E2F")

    TalkEnd(0xFE)
    Return()

    # Function_38_6C30 end

    def Function_39_6E33(): pass

    label("Function_39_6E33")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6EB1")

    ChrTalk(
        0xFE,
        "Well, you're a cross-border guard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is quite beautiful, but ……\x01",
            "Does that person fight with weapons as well?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6FB0")

    label("loc_6EB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6EBF")
    Jump("loc_6FB0")

    label("loc_6EBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6F30")

    ChrTalk(
        0xFE,
        "By the way, I am hungry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, if you are in this place\x01",
            "I will forget about a moment.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6FB0")

    label("loc_6F30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6F68")

    ChrTalk(
        0xFE,
        "Oh, ah, can I see the scenery from the rooftop?\x02",
    )

    CloseMessageWindow()
    Jump("loc_6FB0")

    label("loc_6F68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6FB0")

    ChrTalk(
        0xFE,
        (
            "Fluffy, after all from far away\x01",
            "The power is completely different from viewing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FB0")

    TalkEnd(0xFE)
    Return()

    # Function_39_6E33 end

    def Function_40_6FB4(): pass

    label("Function_40_6FB4")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Well, this is rainy.\x01",
            "Teppen is not clearly seen.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_40_6FB4 end

    def Function_41_6FF8(): pass

    label("Function_41_6FF8")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Even though I came all the way, I'm bored.\x01",
            "I wonder how it will rain anymore!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_41_6FF8 end

    def Function_42_7046(): pass

    label("Function_42_7046")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Huhu, even if I look at it again\x01",
            "It is really a terrible building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is not a thing to compare,\x01",
            "It is not the ratio of \"four tower tower\".\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_42_7046 end

    def Function_43_70BD(): pass

    label("Function_43_70BD")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The presence of Orkis Tower is\x01",
            "Being able to feel without seeing\x01",
            "It is overwhelming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was destroyed 嘥 BC,\x01",
            "A new symbol of the protected city … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, this result is\x01",
            "Is it a coincidence product …?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_43_70BD end

    def Function_44_7180(): pass

    label("Function_44_7180")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    SetChrPos(0x101, 650, 0, -19420, 0)
    SetChrPos(0x104, -650, 0, -19720, 0)
    SetChrPos(0x102, -1790, 0, -20140, 0)
    SetChrPos(0x103, 1630, 0, -20020, 0)
    OP_68(-1230, 2770, -21620, 0)
    MoveCamera(29, 31, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(10240, 0)
    LoadChrToIndex("chr/ch41400.itc", 0x1E)
    LoadChrToIndex("chr/ch41500.itc", 0x1F)
    LoadChrToIndex("chr/ch41800.itc", 0x20)
    SetChrChipByIndex(0x62, 0x1E)
    SetChrChipByIndex(0x63, 0x1F)
    SetChrChipByIndex(0x64, 0x1F)
    SetChrChipByIndex(0x65, 0x1E)
    SetChrChipByIndex(0x66, 0x20)
    SetChrChipByIndex(0x67, 0x1E)
    SetChrChipByIndex(0x68, 0x1F)
    SetChrChipByIndex(0x69, 0x1E)
    SetChrChipByIndex(0x6A, 0x1F)
    SetChrPos(0x62, -3160, 0, -12800, 180)
    SetChrPos(0x63, 3160, 0, -12800, 180)
    SetChrPos(0x64, -3140, 0, 25000, 180)
    SetChrPos(0x65, 2740, 0, 25240, 180)
    SetChrPos(0x66, -10520, 0, 3070, 180)
    SetChrPos(0x67, 5320, 250, 6840, 180)
    SetChrPos(0x68, -21660, 300, -7560, 180)
    SetChrPos(0x69, 21300, 300, 21000, 180)
    SetChrPos(0x6A, 14560, 0, 5730, 180)
    ClearChrFlags(0x62, 0x80)
    ClearChrFlags(0x63, 0x80)
    ClearChrFlags(0x64, 0x80)
    ClearChrFlags(0x65, 0x80)
    ClearChrFlags(0x66, 0x80)
    ClearChrFlags(0x67, 0x80)
    ClearChrFlags(0x68, 0x80)
    ClearChrFlags(0x69, 0x80)
    ClearChrFlags(0x6A, 0x80)
    ClearChrFlags(0x66, 0x4)
    ClearChrFlags(0x68, 0x4)
    ClearChrFlags(0x69, 0x4)
    ClearChrFlags(0x6A, 0x4)
    SetChrFlags(0x62, 0x8000)
    SetChrFlags(0x63, 0x8000)
    SetChrFlags(0x64, 0x8000)
    SetChrFlags(0x65, 0x8000)
    SetChrFlags(0x66, 0x8000)
    SetChrFlags(0x67, 0x8000)
    SetChrFlags(0x68, 0x8000)
    SetChrFlags(0x69, 0x8000)
    SetChrFlags(0x6A, 0x8000)
    BeginChrThread(0x62, 1, 0, 0)
    BeginChrThread(0x63, 1, 0, 0)
    BeginChrThread(0x64, 1, 0, 0)
    BeginChrThread(0x65, 1, 0, 0)
    BeginChrThread(0x66, 1, 0, 4)
    BeginChrThread(0x67, 1, 0, 0)
    BeginChrThread(0x68, 1, 0, 5)
    BeginChrThread(0x69, 1, 0, 6)
    BeginChrThread(0x6A, 1, 0, 7)
    ClearChrFlags(0x75, 0x80)
    ClearChrFlags(0x75, 0x4)
    OP_78(0xC, 0x75)
    SetChrPos(0x75, 7330, 250, 8180, 225)
    SetMapObjFlags(0xC, 0x1000)
    ClearMapObjFlags(0xC, 0x4)
    OP_D5(0x75, 0x0, 0x20F58, 0x0, 0x0)
    SetMapObjFrame(0xC, "mark00", 0x0, 0x1)
    ClearChrFlags(0x76, 0x80)
    ClearChrFlags(0x76, 0x4)
    OP_78(0xE, 0x76)
    SetChrPos(0x76, -7220, 250, 8270, 135)
    SetMapObjFlags(0xE, 0x1000)
    ClearMapObjFlags(0xE, 0x4)
    OP_D5(0x76, 0x0, 0x36EE8, 0x0, 0x0)
    SetMapObjFrame(0xE, "mark00", 0x0, 0x1)
    FadeToBright(2000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00005Fthis is……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(0, 3400, 30670, 0)
    MoveCamera(0, 9, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(19000, 0)
    Fade(1000)
    OP_68(0, 3400, 1770, 8000)
    MoveCamera(0, 9, 0, 8000)
    OP_6E(1000, 8000)
    SetCameraDistance(19000, 8000)
    Sleep(8000)
    OP_68(-3770, 2500, 3480, 0)
    MoveCamera(60, 30, 0, 0)
    OP_6E(990, 0)
    SetCameraDistance(19000, 0)
    Fade(1000)
    OP_68(3510, 2500, 3790, 6000)
    MoveCamera(300, 30, 0, 6000)
    OP_6E(990, 6000)
    SetCameraDistance(19000, 6000)
    Sleep(6000)
    OP_68(0, 3400, -6240, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(19000, 0)
    Fade(1000)
    OP_68(-1230, 2770, -21620, 4000)
    MoveCamera(29, 31, 0, 4000)
    OP_6E(750, 4000)
    SetCameraDistance(10240, 4000)
    Sleep(4500)

    ChrTalk(
        0x104,
        (
            "#12P#00301FIn front of Orkis Tower\x01",
            "Those of the \"Defense Army\"\x01",
            "Do not try hardening ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108FIt is the place where the uncle's independence was declared,\x01",
            "I guess this alert is natural.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_63(0x62, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_4B(0x62, 0x1)

    ChrTalk(
        0x62,
        (
            "Oh, you …\x01",
            "Is not Randy?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_95(0x62, -1340, 0, -17100, 2000, 0x0)
    OP_93(0x101, 0x13B, 0x1F4)
    OP_93(0x103, 0x13B, 0x1F4)

    ChrTalk(
        0x104,
        (
            "#00305F#12PMaybe Carter?\x02\x03",
            "#00302FBecause it is such a white uniform\x01",
            "I did not notice.\x02\x03",
            "You, at the Belgard gate\x01",
            "Was not it deployed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x62,
        (
            "Oh, in accordance with the President's speech\x01",
            "Some people from the border gate\x01",
            "It is called security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x62,
        (
            "With loggins too\x01",
            "I'm patrolling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00302F#12PHaha, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#12P(this person is……)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#6P(Randy's Guardian era\x01",
            "It looks like a coworker. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x62,
        (
            "No, but\x01",
            "It was a serious thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x62,
        (
            "We also suddenly\x01",
            "Given such military uniforms,\x01",
            "At first I was surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12POh, suddenly too\x01",
            "I do not understand the translation …\x02\x03",
            "#00300FThink about it, military uniform and good\x01",
            "Do not feel like you are preparing too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x62,
        (
            "The president must have been from before\x01",
            "I wonder what he was preparing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x62,
        (
            "Defense army equipments will be strengthened\x01",
            "There seems to be promises\x01",
            "I have to tighten my mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F#12POh, ah ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#12P(… … soldiers of the Defense Army,\x01",
            "Favorably like this reorganization\x01",
            "You seem to have received it. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6P(Compared to the regular army of other countries\x01",
            "Because there was no doubt that it was incompatible,\x01",
            "I feel like I understand my feelings … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x62,
        (
            "By the way, to become a defense army\x01",
            "We like usual troops\x01",
            "The class name was to be used.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x62,
        (
            "I was called the first lieutenant, the second lieutenant, the third captain\x01",
            "Captain, lieutenant, you are so lucky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x62,
        (
            "If you make a mistake when calling an officer,\x01",
            "It is reasonably rude, so be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F#12POh, that's your advice.\x02\x03",
            "#00303FThing is that the Mireille guy is\x01",
            "Because it was \"Sanja\" … …\x01",
            "Will it be \"lieutenant\" from now on?\x02\x03",
            "#00309FHahaha, I got a bit of teasing story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#12PCome on … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x62,
        (
            "Let me see……\x01",
            "Well, I wonder if that will happen.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#00305F#12PWhat is it that,\x01",
            "Do not boil me Reply … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F#12PAs a way to call\x01",
            "It should not be a mistake, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x62,
        "No, it's not like that … …\x02",
    )

    CloseMessageWindow()
    OP_63(0x62, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x62)

    ChrTalk(
        0x62,
        (
            "Wait, Randy.\x01",
            "In fact\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x6A, 0x1)
    TurnDirection(0x6A, 0x62, 500)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Voice of Defense Force Officer")

    ChrTalk(
        0x6A,
        (
            "#4S… … Carter! It is!\x01",
            "Please refrain from talking about security while I am guarding! It is!#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x62, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)
    OP_93(0x62, 0x2D, 0x1F4)

    ChrTalk(
        0x62,
        "……, Hah! It is!\x02",
    )

    CloseMessageWindow()
    OP_4C(0x6A, 0x1)
    TurnDirection(0x62, 0x104, 300)

    ChrTalk(
        0x62,
        (
            "… … Bad, Randy.\x01",
            "I will tell you the details next time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F#12PI do not know well …\x01",
            "It was bad this time to speak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x62,
        "Haha, do not mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x62,
        (
            "Oh yeah, you police also\x01",
            "You are going to be incorporated into the Defense Forces, do not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x62,
        (
            "From now on I am a colleague again.\x01",
            "I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x62, -3160, 0, -12800, 2000, 0x0)
    OP_93(0x62, 0xB4, 0x12C)
    OP_4C(0x62, 0x1)

    ChrTalk(
        0x104,
        (
            "#00306F#12PWhew ……\x01",
            "Saying only what you care about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#12PFor the moment it is better to turn back here\x01",
            "Is not it okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#12POh, let's go.\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_68(0, 2770, -13870, 5000)
    MoveCamera(0, 7, 0, 5000)
    OP_6E(750, 5000)
    SetCameraDistance(19000, 5000)

    def lambda_80E5():

        label("loc_80E5")

        TurnDirection(0x62, 0x104, 500)
        Yield()
        Jump("loc_80E5")

    QueueWorkItem2(0x62, 2, lambda_80E5)
    OP_93(0x101, 0xB4, 0x1F4)

    def lambda_80FE():

        label("loc_80FE")

        OP_9B(0x0, 0x101, 0x0, 0x2710, 0x7D0, 0x0)
        Yield()
        Jump("loc_80FE")

    QueueWorkItem2(0x101, 1, lambda_80FE)
    OP_93(0x104, 0xB4, 0x1F4)

    def lambda_811F():

        label("loc_811F")

        OP_9B(0x0, 0x104, 0x0, 0x2710, 0x7D0, 0x0)
        Yield()
        Jump("loc_811F")

    QueueWorkItem2(0x104, 1, lambda_811F)
    OP_93(0x103, 0xB4, 0x1F4)

    def lambda_8140():

        label("loc_8140")

        OP_9B(0x0, 0x103, 0x0, 0x2710, 0x7D0, 0x0)
        Yield()
        Jump("loc_8140")

    QueueWorkItem2(0x103, 1, lambda_8140)
    OP_93(0x102, 0xB4, 0x1F4)

    def lambda_8161():

        label("loc_8161")

        OP_9B(0x0, 0x102, 0x0, 0x2710, 0x7D0, 0x0)
        Yield()
        Jump("loc_8161")

    QueueWorkItem2(0x102, 1, lambda_8161)
    OP_0D()
    SetScenarioFlags(0x191, 4)
    EventEnd(0x6)
    NewScene("c1100", 108, 0, 0)
    IdleLoop()
    Return()

    # Function_44_7180 end

    def Function_45_8186(): pass

    label("Function_45_8186")

    EventBegin(0x0)
    OP_4B(0x11, 0xFF)
    Fade(500)
    OP_68(6100, 2500, 4460, 0)
    MoveCamera(0, 27, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(8570, 0)
    OP_93(0x11, 0xE1, 0x0)
    SetChrSubChip(0x11, 0x0)
    SetChrPos(0x101, 5260, 250, 6290, 43)
    SetChrPos(0x102, 4290, 130, 6800, 45)
    SetChrPos(0x103, 5340, 250, 4840, 43)
    SetChrPos(0x109, 3390, 100, 5970, 43)
    SetChrPos(0x105, 4400, 190, 5200, 43)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#6P#00001FSan Miireiu … …\x01",
            "I was in town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#07903FYes, I just got it.\x02\x03",
            "#07900FI still have a meeting here\x01",
            "I am waiting for command and deputy commander.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FThe section chief also from last night\x01",
            "It was a meeting I attended …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00201FGuard commanders are left\x01",
            "That means …\x01",
            "Is the measure also difficult?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x11)

    ChrTalk(
        0x11,
        (
            "#07901F……you.\x01",
            "This morning, from the section manager\x01",
            "It is a matter of inquiries … …\x02\x03",
            "Randy goes\x01",
            "Did you say it was crazy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F……Yes.\x02\x03",
            "#00001FProbably …\x01",
            "Heading towards Mainz Mountain Road\x01",
            "It seems to be a situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#07908F……so……………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x11)

    ChrTalk(
        0x105,
        "#6P#10300F……Are you okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#07903F…… Yes, I am fine.\x01",
            "More than that …\x02\x03",
            "#07901FRandy disappeared,\x01",
            "His past is involved …\x01",
            "Is not it so?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00008FWell, that is ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#07908F…. Although it's mild,\x01",
            "I told Randy's past,\x01",
            "I do not know much about it.\x02\x03",
            "Until now in actual warfare training\x01",
            "The reason why the rifle could not be used,\x01",
            "I do not understand.\x02\x03",
            "#07901FBut … this time this time,\x01",
            "Make a lot of worries for everyone\x01",
            "I know that it's really a stupid act.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10108FSan Miireiu … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00203F…… Certainly, it is a big idiot beyond idiots.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#07903F…… The guard was also hit hard.\x01",
            "From now on by the commanders, once again\x01",
            "I think we will organize rescue troops.\x02\x03",
            "We can not move until then … …\x01",
            "Randy exercise for one person\x01",
            "It can not be quick.\x02\x03",
            "#07900FSo everyone ……\x01",
            "Please do as you please that foolish thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000F……Let me take care of that.\x01",
            "Randy surely, we, … !.!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_4C(0x11, 0xFF)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x16F, 4)
    EventEnd(0x5)
    Return()

    # Function_45_8186 end

    def Function_46_87F9(): pass

    label("Function_46_87F9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31200.itc", 0x1E)
    LoadChrToIndex("chr/ch31300.itc", 0x1F)
    LoadChrToIndex("chr/ch44900.itc", 0x20)
    SetChrChipByIndex(0x48, 0x0)
    SetChrSubChip(0x48, 0x0)
    ClearChrFlags(0x48, 0x80)
    SetChrFlags(0x48, 0x8000)
    SetChrPos(0x48, -2500, 0, 22800, 180)
    BeginChrThread(0x48, 0, 0, 0)
    SetChrChipByIndex(0x49, 0x0)
    SetChrSubChip(0x49, 0x0)
    ClearChrFlags(0x49, 0x80)
    SetChrFlags(0x49, 0x8000)
    SetChrPos(0x49, 2500, 0, 22800, 180)
    BeginChrThread(0x49, 0, 0, 0)
    SetChrChipByIndex(0x4A, 0x0)
    SetChrSubChip(0x4A, 0x0)
    ClearChrFlags(0x4A, 0x80)
    SetChrFlags(0x4A, 0x8000)
    SetChrPos(0x4A, 2000, 0, -19500, 180)
    BeginChrThread(0x4A, 0, 0, 0)
    SetChrChipByIndex(0x4B, 0x0)
    SetChrSubChip(0x4B, 0x0)
    ClearChrFlags(0x4B, 0x80)
    SetChrFlags(0x4B, 0x8000)
    SetChrPos(0x4B, -2000, 0, -19500, 180)
    BeginChrThread(0x4B, 0, 0, 0)
    SetChrChipByIndex(0x4C, 0x0)
    SetChrSubChip(0x4C, 0x0)
    ClearChrFlags(0x4C, 0x80)
    SetChrFlags(0x4C, 0x8000)
    SetChrPos(0x4C, 21700, 300, 19000, 180)
    BeginChrThread(0x4C, 0, 0, 47)
    SetChrChipByIndex(0x4D, 0x0)
    SetChrSubChip(0x4D, 0x0)
    ClearChrFlags(0x4D, 0x80)
    SetChrFlags(0x4D, 0x8000)
    SetChrPos(0x4D, -21700, 300, -6000, 0)
    BeginChrThread(0x4D, 0, 0, 48)
    SetChrChipByIndex(0x4E, 0x0)
    SetChrSubChip(0x4E, 0x0)
    ClearChrFlags(0x4E, 0x80)
    ClearChrFlags(0x4E, 0x4)
    SetChrFlags(0x4E, 0x8000)
    SetChrPos(0x4E, -19000, 0, 5500, 90)
    BeginChrThread(0x4E, 0, 0, 49)
    SetChrChipByIndex(0x4F, 0x0)
    SetChrSubChip(0x4F, 0x0)
    ClearChrFlags(0x4F, 0x80)
    ClearChrFlags(0x4F, 0x4)
    SetChrFlags(0x4F, 0x8000)
    SetChrPos(0x4F, 19000, 0, 5500, 270)
    BeginChrThread(0x4F, 0, 0, 50)
    SetChrChipByIndex(0x47, 0x20)
    SetChrSubChip(0x47, 0x0)
    ClearChrFlags(0x47, 0x80)
    SetChrFlags(0x47, 0x8000)
    SetChrPos(0x47, 0, 240, -800, 180)
    SetChrChipByIndex(0x52, 0x1E)
    SetChrSubChip(0x52, 0x0)
    ClearChrFlags(0x52, 0x80)
    SetChrFlags(0x52, 0x8000)
    SetChrPos(0x52, -2100, 0, -3500, 0)
    SetChrChipByIndex(0x53, 0x1F)
    SetChrSubChip(0x53, 0x0)
    ClearChrFlags(0x53, 0x80)
    SetChrFlags(0x53, 0x8000)
    SetChrPos(0x53, -700, 0, -3500, 0)
    SetChrChipByIndex(0x54, 0x1E)
    SetChrSubChip(0x54, 0x0)
    ClearChrFlags(0x54, 0x80)
    SetChrFlags(0x54, 0x8000)
    SetChrPos(0x54, 700, 0, -3500, 0)
    SetChrChipByIndex(0x55, 0x1F)
    SetChrSubChip(0x55, 0x0)
    ClearChrFlags(0x55, 0x80)
    SetChrFlags(0x55, 0x8000)
    SetChrPos(0x55, 2100, 0, -3500, 0)
    SetChrChipByIndex(0x56, 0x1F)
    SetChrSubChip(0x56, 0x0)
    ClearChrFlags(0x56, 0x80)
    SetChrFlags(0x56, 0x8000)
    SetChrPos(0x56, -2100, 0, -4900, 0)
    SetChrChipByIndex(0x57, 0x1E)
    SetChrSubChip(0x57, 0x0)
    ClearChrFlags(0x57, 0x80)
    SetChrFlags(0x57, 0x8000)
    SetChrPos(0x57, -700, 0, -4900, 0)
    SetChrChipByIndex(0x58, 0x1F)
    SetChrSubChip(0x58, 0x0)
    ClearChrFlags(0x58, 0x80)
    SetChrFlags(0x58, 0x8000)
    SetChrPos(0x58, 700, 0, -4900, 0)
    SetChrChipByIndex(0x59, 0x1E)
    SetChrSubChip(0x59, 0x0)
    ClearChrFlags(0x59, 0x80)
    SetChrFlags(0x59, 0x8000)
    SetChrPos(0x59, 2100, 0, -4900, 0)
    SetChrPos(0x0, 0, 0, 50000, 0)
    SetChrPos(0x1, 0, 0, 50000, 0)
    SetChrPos(0x2, 0, 0, 50000, 0)
    SetChrPos(0x3, 0, 0, 50000, 0)
    Sleep(1000)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "'Western Zemria Trade Council' ──\x02\x03",
            "The international conference inviting the leaders of each country\x01",
            "With the advocacy of New Mayor of Dieter Crois\x01",
            "It was about to be held.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    PlayBGM("ed7111", 0)
    OP_68(0, 1000, -20000, 0)
    MoveCamera(40, 30, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(15000, 0)
    OP_68(0, 1000, 0, 9000)
    MoveCamera(0, 30, 0, 9000)
    SetCameraDistance(30000, 9000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(1000)
    Fade(1000)
    OP_68(0, 5500, 25000, 0)
    MoveCamera(0, -5, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(38000, 0)
    OP_68(0, 20500, 25000, 15000)
    MoveCamera(0, -20, 0, 15000)
    SetCameraDistance(48000, 15000)
    OP_0D()
    Sleep(3000)
    FadeToDark(300, 0, 100)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "At the same time, it is just completed\x01",
            "It also served as an announcement of the new city hall building.\x02\x03",
            "── Generic name \"Orkis Tower\".\x02\x03",
            "It will be 40 floors above ground and 250 heights high,\x01",
            "The first skyscraper in continental history\x01",
            "Now people are interested in the continents.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c1150", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_46_87F9 end

    def Function_47_8D68(): pass

    label("Function_47_8D68")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8DB4")
    OP_95(0xFE, 21700, 300, -6000, 2000, 0x0)
    Sleep(1000)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_95(0xFE, 21700, 300, 19000, 2000, 0x0)
    Sleep(1000)
    OP_93(0xFE, 0xB4, 0x1F4)
    Jump("Function_47_8D68")

    label("loc_8DB4")

    Return()

    # Function_47_8D68 end

    def Function_48_8DB5(): pass

    label("Function_48_8DB5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8E01")
    OP_95(0xFE, -21700, 300, 19000, 2000, 0x0)
    Sleep(1000)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_95(0xFE, -21700, 300, -6000, 2000, 0x0)
    Sleep(1000)
    OP_93(0xFE, 0x0, 0x1F4)
    Jump("Function_48_8DB5")

    label("loc_8E01")

    Return()

    # Function_48_8DB5 end

    def Function_49_8E02(): pass

    label("Function_49_8E02")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8E4E")
    OP_95(0xFE, -7000, 0, 5500, 2000, 0x0)
    Sleep(1000)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_95(0xFE, -19000, 0, 5500, 2000, 0x0)
    Sleep(1000)
    OP_93(0xFE, 0x5A, 0x1F4)
    Jump("Function_49_8E02")

    label("loc_8E4E")

    Return()

    # Function_49_8E02 end

    def Function_50_8E4F(): pass

    label("Function_50_8E4F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8E9B")
    OP_95(0xFE, 7000, 0, 5500, 2000, 0x0)
    Sleep(1000)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_95(0xFE, 19000, 0, 5500, 2000, 0x0)
    Sleep(1000)
    OP_93(0xFE, 0x10E, 0x1F4)
    Jump("Function_50_8E4F")

    label("loc_8E9B")

    Return()

    # Function_50_8E4F end

    def Function_51_8E9C(): pass

    label("Function_51_8E9C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10900.itc", 0x1E)
    LoadChrToIndex("chr/ch12400.itc", 0x1F)
    LoadChrToIndex("chr/ch11100.itc", 0x20)
    LoadChrToIndex("chr/ch11300.itc", 0x21)
    LoadChrToIndex("chr/ch11000.itc", 0x22)
    LoadChrToIndex("chr/ch11200.itc", 0x23)
    LoadChrToIndex("chr/ch11800.itc", 0x24)
    LoadChrToIndex("chr/ch11700.itc", 0x25)
    LoadChrToIndex("chr/ch13300.itc", 0x26)
    LoadChrToIndex("chr/ch05600.itc", 0x27)
    LoadChrToIndex("chr/ch05500.itc", 0x28)
    LoadChrToIndex("chr/ch05800.itc", 0x29)
    LoadChrToIndex("chr/ch25800.itc", 0x2A)
    LoadChrToIndex("chr/ch27800.itc", 0x2B)
    LoadChrToIndex("chr/ch41000.itc", 0x2C)
    LoadChrToIndex("chr/ch41200.itc", 0x2D)
    LoadChrToIndex("chr/ch41600.itc", 0x2E)
    SoundLoad(468)
    SoundLoad(924)
    SoundLoad(835)
    SoundLoad(851)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02800.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02500.itp")
    CreatePortrait(2, 16, 200, 528, 264, 0, 0, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis520.itp")
    CreatePortrait(3, 16, 200, 528, 264, 0, 0, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis521.itp")
    LoadEffect(0x1, "event\\ev12031.eff")
    LoadEffect(0x2, "event\\ev12030.eff")
    SetChrPos(0x101, 18200, 0, 5400, 270)
    SetChrPos(0x102, 18200, 0, 6600, 270)
    SetChrPos(0x104, 19300, 0, 7100, 270)
    SetChrPos(0x109, 19300, 0, 4900, 270)
    SetChrPos(0x105, 19700, 0, 6000, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x5C, 0x2C)
    SetChrSubChip(0x5C, 0x0)
    ClearChrFlags(0x5C, 0x80)
    SetChrFlags(0x5C, 0x8000)
    SetChrPos(0x5C, 3600, 250, 500, 0)
    SetChrChipByIndex(0x5D, 0x2C)
    SetChrSubChip(0x5D, 0x0)
    ClearChrFlags(0x5D, 0x80)
    SetChrFlags(0x5D, 0x8000)
    SetChrPos(0x5D, 2500, 250, 500, 0)
    SetChrChipByIndex(0x5E, 0x2D)
    SetChrSubChip(0x5E, 0x0)
    ClearChrFlags(0x5E, 0x80)
    SetChrFlags(0x5E, 0x8000)
    SetChrPos(0x5E, 550, 250, 500, 0)
    SetChrChipByIndex(0x5F, 0x2D)
    SetChrSubChip(0x5F, 0x0)
    ClearChrFlags(0x5F, 0x80)
    SetChrFlags(0x5F, 0x8000)
    SetChrPos(0x5F, -550, 250, 500, 0)
    SetChrChipByIndex(0x60, 0x2E)
    SetChrSubChip(0x60, 0x0)
    ClearChrFlags(0x60, 0x80)
    SetChrFlags(0x60, 0x8000)
    SetChrPos(0x60, -2500, 250, 500, 0)
    SetChrChipByIndex(0x61, 0x2E)
    SetChrSubChip(0x61, 0x0)
    ClearChrFlags(0x61, 0x80)
    SetChrFlags(0x61, 0x8000)
    SetChrPos(0x61, -3600, 250, 500, 0)
    SetChrChipByIndex(0x27, 0x1E)
    SetChrSubChip(0x27, 0x0)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, 1200, 100, 4400, 0)
    SetChrChipByIndex(0x28, 0x1F)
    SetChrSubChip(0x28, 0x0)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    SetChrPos(0x28, 600, 100, 3100, 0)
    SetChrChipByIndex(0x29, 0x20)
    SetChrSubChip(0x29, 0x0)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    SetChrPos(0x29, 2500, 100, 4100, 325)
    SetChrChipByIndex(0x2A, 0x21)
    SetChrSubChip(0x2A, 0x0)
    ClearChrFlags(0x2A, 0x80)
    SetChrFlags(0x2A, 0x8000)
    SetChrPos(0x2A, 3500, 100, 4700, 330)
    SetChrChipByIndex(0x2B, 0x22)
    SetChrSubChip(0x2B, 0x0)
    ClearChrFlags(0x2B, 0x80)
    SetChrFlags(0x2B, 0x8000)
    SetChrPos(0x2B, -2800, 100, 4900, 70)
    SetChrChipByIndex(0x2C, 0x23)
    SetChrSubChip(0x2C, 0x0)
    ClearChrFlags(0x2C, 0x80)
    SetChrFlags(0x2C, 0x8000)
    SetChrPos(0x2C, -3500, 100, 5500, 75)
    SetChrChipByIndex(0x2D, 0x24)
    SetChrSubChip(0x2D, 0x0)
    ClearChrFlags(0x2D, 0x80)
    SetChrFlags(0x2D, 0x8000)
    SetChrPos(0x2D, 3300, 100, 6700, 270)
    SetChrChipByIndex(0x2E, 0x25)
    SetChrSubChip(0x2E, 0x0)
    ClearChrFlags(0x2E, 0x80)
    SetChrFlags(0x2E, 0x8000)
    SetChrPos(0x2E, -700, 100, 4300, 0)
    SetChrChipByIndex(0x2F, 0x26)
    SetChrSubChip(0x2F, 0x0)
    ClearChrFlags(0x2F, 0x80)
    SetChrFlags(0x2F, 0x8000)
    SetChrPos(0x2F, -1650, 100, 3700, 15)
    SetChrChipByIndex(0x30, 0x27)
    SetChrSubChip(0x30, 0x0)
    ClearChrFlags(0x30, 0x80)
    SetChrFlags(0x30, 0x8000)
    SetChrPos(0x30, -1000, 100, 7200, 180)
    SetChrChipByIndex(0x31, 0x28)
    SetChrSubChip(0x31, 0x0)
    ClearChrFlags(0x31, 0x80)
    SetChrFlags(0x31, 0x8000)
    SetChrPos(0x31, -1600, 100, 8200, 180)
    SetChrChipByIndex(0x22, 0x29)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, 1300, 100, 6500, 160)
    SetChrChipByIndex(0x5B, 0x2A)
    SetChrSubChip(0x5B, 0x0)
    ClearChrFlags(0x5B, 0x80)
    SetChrFlags(0x5B, 0x8000)
    SetChrPos(0x5B, 600, 100, 7100, 160)
    SetChrChipByIndex(0x5A, 0x2B)
    SetChrSubChip(0x5A, 0x0)
    ClearChrFlags(0x5A, 0x80)
    SetChrFlags(0x5A, 0x8000)
    SetChrPos(0x5A, 4300, 100, 6400, 270)
    SetChrChipByIndex(0x48, 0x0)
    SetChrSubChip(0x48, 0x0)
    ClearChrFlags(0x48, 0x80)
    SetChrFlags(0x48, 0x8000)
    SetChrPos(0x48, 14000, 0, 8000, 270)
    SetChrChipByIndex(0x49, 0x0)
    SetChrSubChip(0x49, 0x0)
    ClearChrFlags(0x49, 0x80)
    SetChrFlags(0x49, 0x8000)
    SetChrPos(0x49, 14000, 0, 4000, 270)
    SetChrChipByIndex(0x4A, 0x0)
    SetChrSubChip(0x4A, 0x0)
    ClearChrFlags(0x4A, 0x80)
    SetChrFlags(0x4A, 0x8000)
    SetChrPos(0x4A, 14000, 0, 21000, 180)
    SetChrChipByIndex(0x4B, 0x0)
    SetChrSubChip(0x4B, 0x0)
    ClearChrFlags(0x4B, 0x80)
    SetChrFlags(0x4B, 0x8000)
    SetChrPos(0x4B, 14000, 0, -6000, 315)
    SetChrChipByIndex(0x4C, 0x0)
    SetChrSubChip(0x4C, 0x0)
    ClearChrFlags(0x4C, 0x80)
    SetChrFlags(0x4C, 0x8000)
    SetChrPos(0x4C, -14000, 0, 8000, 90)
    SetChrChipByIndex(0x4D, 0x0)
    SetChrSubChip(0x4D, 0x0)
    ClearChrFlags(0x4D, 0x80)
    SetChrFlags(0x4D, 0x8000)
    SetChrPos(0x4D, -14000, 0, 4000, 90)
    SetChrChipByIndex(0x4E, 0x0)
    SetChrSubChip(0x4E, 0x0)
    ClearChrFlags(0x4E, 0x80)
    SetChrFlags(0x4E, 0x8000)
    SetChrPos(0x4E, -14000, 0, 21000, 180)
    SetChrChipByIndex(0x4F, 0x0)
    SetChrSubChip(0x4F, 0x0)
    ClearChrFlags(0x4F, 0x80)
    SetChrFlags(0x4F, 0x8000)
    SetChrPos(0x4F, -14000, 0, -6000, 45)
    SetChrChipByIndex(0x50, 0x0)
    SetChrSubChip(0x50, 0x0)
    ClearChrFlags(0x50, 0x80)
    SetChrFlags(0x50, 0x8000)
    SetChrPos(0x50, -2500, 0, -12000, 180)
    SetChrChipByIndex(0x51, 0x0)
    SetChrSubChip(0x51, 0x0)
    ClearChrFlags(0x51, 0x80)
    SetChrFlags(0x51, 0x8000)
    SetChrPos(0x51, 2500, 0, -12000, 180)
    ClearChrFlags(0x71, 0x80)
    ClearChrFlags(0x71, 0x4)
    OP_78(0xA, 0x71)
    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    OP_49()
    OP_90(0x71, 0, -15500, -83500, 0)
    OP_D5(0x71, 0xFFFFC568, 0x0, 0x0, 0x0)
    SetMapObjFlags(0xA, 0x1000)
    OP_74(0xA, 0x1E)
    OP_70(0xA, 0x1E)
    OP_71(0xA, 0x79, 0xB4, 0x0, 0x20)
    ClearChrFlags(0x72, 0x80)
    ClearChrFlags(0x72, 0x4)
    SetMapObjFlags(0xB, 0x4)
    OP_78(0xB, 0x72)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    OP_49()
    OP_90(0x72, 0, -15500, -83500, 0)
    OP_D5(0x72, 0xFFFFC568, 0x0, 0x0, 0x0)
    SetMapObjFlags(0xB, 0x1000)
    OP_74(0xB, 0x1E)
    OP_70(0xB, 0x1E)
    OP_71(0xB, 0x79, 0xB4, 0x0, 0x20)
    OP_68(0, -8500, -55000, 0)
    MoveCamera(20, -8, 0, 0)
    OP_6E(850, 0)
    SetCameraDistance(30000, 0)
    OP_68(0, -500, -30000, 10000)
    MoveCamera(0, -8, 0, 10000)
    SetCameraDistance(24000, 10000)

    def lambda_9585():
        OP_98(0xFE, 0x0, 0x0, 0xEA60, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x71, 1, lambda_9585)
    BeginChrThread(0x79, 1, 0, 55)
    FadeToBright(2000, 0)
    Sleep(3000)
    ClearMapObjFlags(0xB, 0x4)

    def lambda_95B7():
        OP_98(0xFE, 0x0, 0x0, 0xD6D8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x72, 1, lambda_95B7)
    Sleep(1000)
    Sound(494, 0, 80, 0)
    Sleep(5000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xA, 0x4)
    Sleep(1000)
    Sound(492, 0, 100, 0)
    StopSound(468, 1000, 100)
    StopSound(924, 1000, 20)
    Sleep(1000)
    OP_68(0, 900, 5700, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(24000, 0)
    Sound(835, 2, 50, 0)
    Sound(851, 2, 50, 0)
    MoveCamera(30, 23, 0, 7000)
    SetCameraDistance(14000, 7000)
    FadeToBright(2000, 0)
    BeginChrThread(0x27, 3, 0, 54)
    Sleep(300)
    BeginChrThread(0x22, 3, 0, 54)
    Sleep(400)
    BeginChrThread(0x29, 3, 0, 54)
    Sleep(300)
    BeginChrThread(0x30, 3, 0, 54)
    Sleep(400)
    BeginChrThread(0x2E, 3, 0, 54)
    Sleep(300)
    BeginChrThread(0x2B, 3, 0, 54)
    Sleep(400)
    BeginChrThread(0x2D, 3, 0, 54)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 52)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(1300, 1000, 6500, 0)
    MoveCamera(27, 27, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13500, 0)

    def lambda_96E0():
        TurnDirection(0xFE, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x30, 2, lambda_96E0)
    SetCameraDistance(12500, 2000)
    OP_0D()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(2500)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    OP_CC(0x0, 0x2, 0x3)

    def lambda_9792():
        TurnDirection(0xFE, 0x2D, 500)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_9792)
    OP_68(-1000, 1000, 6200, 2500)
    MoveCamera(9, 27, 0, 2500)
    SetCameraDistance(13500, 2500)
    OP_6F(0x79)
    Sleep(500)

    def lambda_97C9():
        TurnDirection(0xFE, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x30, 2, lambda_97C9)
    SetCameraDistance(12500, 2000)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(2500)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)

    def lambda_987A():
        TurnDirection(0xFE, 0x27, 500)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_987A)
    Fade(500)
    OP_68(19650, 900, 6530, 0)
    MoveCamera(53, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16340, 0)
    SetCameraDistance(15340, 1500)
    OP_4B(0x101, 0x3)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#11P#00011F(… …. It is amazing ………)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#5P(Yeah … … As expected one country\x01",
            "Not only those who put together. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#5P(But \"Chairman of Iron Blood\" ……\x01",
            "I'm pretty nice guy. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#11P#10302F(Huff, who is the President of the Republic\x01",
            "Foolishly#4RHyogo Prefecture#I feel like a raccoon dog. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#10102F(Libert's Claudia Queen also\x01",
            "It is wonderful …\x02\x03",
            "#10109F(… … and that Assistant Yulia\x01",
            "To be seen in such a place …! )\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    Fade(500)
    EndChrThread(0x27, 0xFF)
    OP_64(0x27)
    EndChrThread(0x22, 0xFF)
    OP_64(0x22)
    EndChrThread(0x29, 0xFF)
    OP_64(0x29)
    EndChrThread(0x30, 0xFF)
    OP_64(0x30)
    EndChrThread(0x2E, 0xFF)
    OP_64(0x2E)
    EndChrThread(0x2B, 0xFF)
    OP_64(0x2B)
    EndChrThread(0x2D, 0xFF)
    OP_64(0x2D)
    SetChrPos(0x30, 0, 100, 6800, 180)
    SetChrPos(0x31, -900, 100, 8000, 180)
    SetChrPos(0x22, 1500, 100, 8200, 180)
    SetChrPos(0x5B, 2500, 100, 8200, 180)

    def lambda_9AF5():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_9AF5)

    def lambda_9B02():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x2F, 2, lambda_9B02)

    def lambda_9B0F():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_9B0F)

    def lambda_9B1C():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_9B1C)

    def lambda_9B29():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_9B29)

    def lambda_9B36():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_9B36)

    def lambda_9B43():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_9B43)

    def lambda_9B50():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_9B50)
    OP_68(70, 1000, 7670, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(15500, 0)
    OP_4C(0x101, 0x3)
    SetCameraDistance(14000, 2000)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x30,
        (
            "#02804F#5P── Everyone of the leaders of each country.\x02\x03",
            "#02800FWelcome to the long way\x01",
            "I came to the crossbell.\x02\x03",
            "Mayor of Crossbell City,\x01",
            "It is Dieter Crois.\x02",
        )
    )

    CloseMessageWindow()
    Sound(968, 0, 70, 0)
    Sleep(2500)

    ChrTalk(
        0x30,
        (
            "#02804F#5PThis time in the \"Western Zemria Trade Council\"\x01",
            "Thank you very much for participating.\x02\x03",
            "As usual, with welcome spot at this place\x01",
            "I am going to let the opening declaration … …\x02\x03",
            "#02800FBefore that, let's go over this memorable day\x01",
            "I would like to have your time.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x101, 0x3)
    OP_68(-1330, 4700, 14630, 3000)
    MoveCamera(28, 2, 0, 3000)
    OP_6E(750, 3000)
    SetCameraDistance(15500, 3000)
    OP_93(0x30, 0x0, 0x1F4)
    Sleep(500)

    def lambda_9D6E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_9D6E)

    def lambda_9D7B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_9D7B)
    Sleep(50)

    def lambda_9D8B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_9D8B)

    def lambda_9D98():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2F, 2, lambda_9D98)
    Sleep(50)

    def lambda_9DA8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_9DA8)

    def lambda_9DB5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_9DB5)
    Sleep(50)

    def lambda_9DC5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_9DC5)

    def lambda_9DD2():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_9DD2)
    Sleep(50)

    def lambda_9DE2():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_9DE2)

    def lambda_9DEF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x5A, 2, lambda_9DEF)
    Sleep(50)

    def lambda_9DFF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x31, 2, lambda_9DFF)

    def lambda_9E0C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_9E0C)

    def lambda_9E19():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x5B, 2, lambda_9E19)
    WaitChrThread(0x31, 2)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x30,
        (
            "#02803F#N#11P── Introduction.\x02\x03",
            "As Crosbell City's new city hall.\x02\x03",
            "It symbolizes trade and financial city crossbell\x01",
            "As a new landmark.\x02\x03",
            "#02800FMore than anything, for peace and development across the continent\x01",
            "As an international exchange center to contribute.\x02\x03",
            "As much as we were letting you show off,\x01",
            "The first skyscraper in continental history -\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x30,
        "#02809F#N#4S#11PIt is \"Orkis Tower\"!\x02",
    )

    CloseMessageWindow()
    PlayBGM("ed7550", 0)
    OP_68(0, 12300, 8000, 5000)
    MoveCamera(0, -27, 0, 5000)
    SetCameraDistance(21500, 5000)
    Sleep(3000)
    StopSound(835, 1000, 50)
    StopSound(851, 1000, 50)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_C9(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed72_02.pmf", 0x226, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C9(0x1, 0x10)
    SetMapObjFlags(0x9, 0x4)
    OP_93(0x101, 0x14A, 0x0)
    OP_93(0x102, 0x14A, 0x0)
    OP_93(0x104, 0x14A, 0x0)
    OP_93(0x109, 0x14A, 0x0)
    OP_93(0x105, 0x14A, 0x0)
    OP_4C(0x101, 0x3)
    PlayEffect(0x1, 0x1, 0xFF, 0x0, 0, 0, 15000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x2, 0xFF, 0x0, 3000, 0, 15000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x3, 0xFF, 0x0, -3000, 0, 15000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x4, 0xFF, 0x0, 5000, 0, 15000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x5, 0xFF, 0x0, -5000, 0, 15000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_68(0, 2300, 8000, 5000)
    MoveCamera(0, 11, 0, 5000)
    SetCameraDistance(15500, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(1000)
    Sound(967, 0, 100, 0)
    Fade(500)
    OP_68(19080, 11500, 6140, 0)
    MoveCamera(331, -63, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    OP_68(19080, 11300, 6140, 3000)
    MoveCamera(330, -70, 0, 3000)
    OP_6E(650, 3000)
    SetCameraDistance(15000, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00011F#NHere, this …\x01",
            "\"Orchis Tower\"……!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00102F#NI knew the overview, but\x01",
            "It was so magnificent so far …\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x109,
        (
            "#6P#10111F#NJust looking at me somehow\x01",
            "It seems to be overwhelming …\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00306F#NI guess it is impossible ……\x01",
            "Doronke Mira is on it.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#12P#10302F#NHuh, I feel like being distant\x01",
            "I guess Mira was introduced.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    EndChrThread(0x101, 0x3)
    Fade(500)
    OP_68(3720, 1100, 4019, 0)
    MoveCamera(141, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    PlayEffect(0x1, 0x1, 0xFF, 0x0, 0, -10000, 15000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x2, 0xFF, 0x0, 3000, -10000, 15000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x3, 0xFF, 0x0, -3000, -10000, 15000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x4, 0xFF, 0x0, 5000, -10000, 15000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x5, 0xFF, 0x0, -5000, -10000, 15000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x29,
        (
            "#07205F#11P(No, no … ….\x01",
            "It was truly exaggerated to me. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "#07303F#5P(… … the advancement of technology is\x01",
            "It's a terrible thing … …)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-3710, 1100, 5280, 2500)
    MoveCamera(216, 31, 0, 2500)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x2B,
        (
            "#07000F#5P(… … as if Libert = arc\x01",
            "I remember … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2C,
        (
            "#07104F#5P(Yeah … … the center tower#6RAxis pillar#About\x01",
            "It is not height, but …).\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-1460, 1100, 3570, 1500)
    MoveCamera(180, 27, 0, 1500)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x2E,
        (
            "#07511F#5P(Ha ha ha ha,\x01",
            "It's nothing extraordinary! )\x02\x03",
            "#07510F(I received your report on Kimi\x01",
            "No way No way is it! )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "#12004F#11P(Yeah, I also real thing\x01",
            "I did not think it was far. )\x02\x03",
            "#12000F(Truly, with the capital strength of IBC\x01",
            "I told you. )\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(1170, 1100, 3330, 1500)
    MoveCamera(136, 26, 0, 1500)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x27,
        (
            "#07404F#11P(Huh, it's actually a big deal.)\x02\x03",
            "#07400F(In this causeway land\x01",
            "This is the Great Cathedral#6RLiberty#You do not have to build. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#11509F#11P(Well, for the time being,\x01",
            "I do not want to climb the rooftop. )\x02\x03",
            "#11502F(Try asking the mayor\x01",
            "Would you let me climb? )\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(70, 1000, 7670, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(15500, 0)
    SetCameraDistance(14000, 2000)
    Sleep(1000)
    OP_93(0x30, 0xB4, 0x1F4)
    Sleep(300)

    def lambda_A878():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x31, 2, lambda_A878)

    def lambda_A885():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_A885)

    def lambda_A892():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x5B, 2, lambda_A892)
    Sleep(50)

    def lambda_A8A2():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_A8A2)

    def lambda_A8AF():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x2F, 2, lambda_A8AF)
    Sleep(50)

    def lambda_A8BF():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_A8BF)

    def lambda_A8CC():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_A8CC)
    Sleep(50)

    def lambda_A8DC():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_A8DC)

    def lambda_A8E9():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_A8E9)
    Sleep(50)

    def lambda_A8F9():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_A8F9)

    def lambda_A906():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_A906)
    Sleep(50)

    def lambda_A916():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_A916)

    def lambda_A923():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x5A, 2, lambda_A923)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x30,
        (
            "#02804F── Then, please revise.\x02\x03",
            "People from the Leaders and in this place\x01",
            "Under the witness of all officials ──\x02\x03",
            "#02800F\"Western Zemria Trade Council\"\x01",
            "I will declare the opening!\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 53)
    Sound(820, 0, 100, 0)
    Sound(968, 0, 100, 0)
    SetCameraDistance(17500, 3000)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x226), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("c1300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_51_8E9C end

    def Function_52_AA19(): pass

    label("Function_52_AA19")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AAD1")
    Sound(810, 0, 80, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AA84")
    Sleep(500)
    Jump("loc_AACC")

    label("loc_AA84")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AA9B")
    Sleep(1000)
    Jump("loc_AACC")

    label("loc_AA9B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AAB2")
    Sleep(150)
    Jump("loc_AACC")

    label("loc_AAB2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AAC9")
    Sleep(2000)
    Jump("loc_AACC")

    label("loc_AAC9")

    Sleep(2500)

    label("loc_AACC")

    Jump("Function_52_AA19")

    label("loc_AAD1")

    Return()

    # Function_52_AA19 end

    def Function_53_AAD2(): pass

    label("Function_53_AAD2")

    Sound(810, 0, 80, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Sound(810, 0, 80, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Sound(810, 0, 80, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(700)
    Sound(810, 0, 80, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Sound(810, 0, 80, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(700)
    Sound(810, 0, 80, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_53_AAD2 end

    def Function_54_AC50(): pass

    label("Function_54_AC50")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AC75")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(4000)
    Jump("Function_54_AC50")

    label("loc_AC75")

    Return()

    # Function_54_AC50 end

    def Function_55_AC76(): pass

    label("Function_55_AC76")

    Sound(457, 0, 80, 0)
    Sound(468, 2, 20, 0)
    Sound(924, 2, 0, 0)
    Sleep(100)
    OP_25(0x1D4, 0x1E)
    Sleep(100)
    OP_25(0x1D4, 0x28)
    OP_25(0x39C, 0x5)
    Sleep(100)
    OP_25(0x1D4, 0x32)
    Sleep(100)
    OP_25(0x1D4, 0x3C)
    OP_25(0x39C, 0xA)
    Sleep(100)
    OP_25(0x1D4, 0x46)
    Sleep(100)
    OP_25(0x1D4, 0x50)
    OP_25(0x39C, 0xF)
    Sleep(100)
    OP_25(0x1D4, 0x5A)
    Sleep(100)
    OP_25(0x1D4, 0x64)
    OP_25(0x39C, 0x14)
    Return()

    # Function_55_AC76 end

    def Function_56_ACD1(): pass

    label("Function_56_ACD1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, 950, 0, -16620, 0)
    SetChrPos(0x102, -750, 0, -16720, 0)
    SetChrPos(0x104, -1690, 0, -17640, 0)
    SetChrPos(0x105, 280, 0, -17860, 0)
    SetChrPos(0x109, 1930, 0, -17220, 0)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    OP_68(0, 20000, -14480, 0)
    MoveCamera(0, -59, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(19000, 0)
    FadeToBright(2000, 0)
    OP_68(0, 5300, -14480, 8000)
    MoveCamera(0, 2, 0, 8000)
    OP_6E(1000, 8000)
    SetCameraDistance(19000, 8000)
    Sleep(8500)
    OP_68(-2230, 2500, 14840, 0)
    MoveCamera(43, 37, 0, 0)
    OP_6E(870, 0)
    SetCameraDistance(22500, 0)
    Fade(500)
    OP_68(-2029, 2500, -13510, 8000)
    MoveCamera(43, 37, 0, 8000)
    OP_6E(870, 8000)
    SetCameraDistance(22500, 8000)
    Sleep(8500)
    Fade(500)
    OP_68(-990, 2500, -18610, 0)
    MoveCamera(33, 33, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(10170, 0)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0x1B, 0x8000)
    ClearChrFlags(0x1C, 0x8000)
    ClearChrFlags(0x1D, 0x8000)
    ClearChrFlags(0x1E, 0x8000)
    ClearChrFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    OP_0D()
    Sleep(1500)

    ChrTalk(
        0x101,
        (
            "#00000FHaha, you are not crowded.\x02\x03",
            "Ryu and Henry also\x01",
            "It seems they are coming out to play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FAfter this unveiling ceremony,\x01",
            "Soon after the leaders left\x01",
            "It was opened to citizens.\x02\x03",
            "#00104FHuhu, my uncle\x01",
            "I wonder if the chic is said to be bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FHaha, it is like Mayor of Dieter.\x02\x03",
            "#10100FHowever, there are many police officers as expected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#4PWell, now the whole city is\x01",
            "It's in a state of emergence.\x02\x03",
            "#10300FTrouble will also occur easily\x01",
            "Do not you be vigilant, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FOh, up to the inside of the tower as a treasure\x01",
            "It seems that they are trying not to enter.\x02\x03",
            "#00000FAs of now,\x01",
            "Let's stop entering inside.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x15E, 6)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x0, 0, 0, -17130, 0)
    EventEnd(0x5)
    Return()

    # Function_56_ACD1 end

    def Function_57_B12A(): pass

    label("Function_57_B12A")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FToday, the citizens also inside the tower\x01",
            "It seems that they are trying not to enter.\x02\x03",
            "As of now,\x01",
            "Let's stop entering inside.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 0, 0, 25470, 180)
    EventEnd(0x4)
    Return()

    # Function_57_B12A end

    def Function_58_B1C8(): pass

    label("Function_58_B1C8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, -1500, -25000, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(20500, 0)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    OP_90(0x101, 500, 0, -31700, 0)
    OP_90(0x102, -500, 0, -31700, 0)
    OP_90(0x103, 1200, 0, -33400, 0)
    OP_90(0x104, -1200, 0, -33400, 0)
    OP_90(0x109, -700, 0, -34700, 0)
    OP_90(0x105, 700, 0, -34700, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearMapFlags(0x10000000)

    def lambda_B290():
        OP_97(0x105, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_B290)
    Sleep(100)

    def lambda_B2AD():
        OP_97(0x109, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B2AD)
    Sleep(100)

    def lambda_B2CA():
        OP_97(0x103, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_B2CA)
    Sleep(100)

    def lambda_B2E7():
        OP_97(0x104, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B2E7)
    Sleep(100)

    def lambda_B304():
        OP_97(0x101, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B304)
    Sleep(100)

    def lambda_B321():
        OP_97(0x102, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B321)
    OP_68(0, -500, -25000, 7000)
    SetCameraDistance(15500, 7000)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x102, 0)
    OP_6F(0x79)
    Fade(500)
    OP_68(0, 20000, -9000, 0)
    MoveCamera(0, -55, 0, 0)
    OP_6E(850, 0)
    SetCameraDistance(12000, 0)
    OP_68(0, 3000, -18000, 7000)
    MoveCamera(0, 0, 0, 7000)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#00206F#11PLast night before arriving at the airport\x01",
            "I wrote this lighted building\x01",
            "I saw you ……\x02\x03",
            "#00202FIn this way you actually look up\x01",
            "It is a terrible size.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F#11PHahaha … I understand your feelings.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102F#5PJust Cross Bell's new\x01",
            "I feel like a landmark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5PBut this big building,\x01",
            "What on earth are you using it?\x02\x03",
            "#00301FCompared to the previous city hall\x01",
            "Is not it too much deck?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#5PWell, various functions\x01",
            "Because it is a built-in building.\x02\x03",
            "#00100FApart from administrative districts of the city and autonomous province\x01",
            "International trade center and\x01",
            "There is also a floor on cultural exchange.\x02\x03",
            "To be the center of the western continent,\x01",
            "You can say that it was built.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#5PThe\x01",
            "It's a big talk of scale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F#5PBut, when it is said that way\x01",
            "I am convinced of this trade meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11PIn fact, at the completion of this building\x01",
            "Capital and information concentration in Crossbell\x01",
            "It will accelerate more than ever.\x02\x03",
            "#10300FBased on that perspective\x01",
            "A future arrangement or something\x01",
            "Is it a place to talk?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#5PYes, I heard that.\x02\x03",
            "#00108FOnly the most economical story\x01",
            "I will not stop but …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 900, -17650, 0)
    MoveCamera(6, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17100, 0)
    OP_0D()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003F#11P── Well, what do you do?\x02\x03",
            "#00001FWith Dudley\x01",
            "On the entrance floor of 1F at noon\x01",
            "I'm meeting you.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B85B():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B85B)
    Sleep(50)

    def lambda_B86B():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_B86B)
    Sleep(50)

    def lambda_B87B():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B87B)
    Sleep(50)

    def lambda_B88B():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B88B)
    Sleep(50)

    def lambda_B89B():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_B89B)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7B, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B90F")

    ChrTalk(
        0x102,
        (
            "#00108F#5PI see …\x01",
            "I still have time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B942")

    label("loc_B90F")


    ChrTalk(
        0x102,
        (
            "#00105F#5PI see …\x01",
            "I still have much time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B942")


    ChrTalk(
        0x104,
        (
            "#6P#00304FWell, anyhow errands\x01",
            "Let 's finish preparations.\x02\x03",
            "#00300FDo not worry about what happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FI agree……\x01",
            "Indeed if the meeting began\x01",
            "I can not go outside either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00202FThen, once you have done business and preparation\x01",
            "Lets enter the building.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 0, 0, -19000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetScenarioFlags(0x141, 6)
    ModifyEventFlags(1, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_58_B1C8 end

    def Function_59_BA8D(): pass

    label("Function_59_BA8D")

    EventBegin(0x0)
    Fade(500)
    OP_68(0, 1500, 26500, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 0, 0, 26000, 0)
    SetChrPos(0x102, -1000, 0, 25300, 0)
    SetChrPos(0x103, 1000, 0, 25300, 0)
    SetChrPos(0x104, 1100, 0, 23400, 0)
    SetChrPos(0x109, -1100, 0, 23400, 0)
    SetChrPos(0x105, 0, 0, 22700, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7B, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BBF3")

    ChrTalk(
        0x101,
        (
            "#00003F#5P(What is Mr. Dudley?\x01",
            "On the entrance floor of 1F at noon\x01",
            "I am meeting … …)\x02\x03",
            "#00001F(I still have time.\x01",
            "Shall we go inside? )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BC8D")

    label("loc_BBF3")


    ChrTalk(
        0x101,
        (
            "#00003F#5P(What is Mr. Dudley?\x01",
            "On the entrance floor of 1F at noon\x01",
            "I am meeting … …)\x02\x03",
            "#00001F(I still have time for Oita though\x01",
            "Would you like to enter early and wait? )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BC8D")

    FadeToDark(300, 0, 100)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Once in the tower\x01",
            "Equipment, items and the auction\x01",
            "You will not be able to arrange.\x02\x03",
            "Also, the remaining quests\x01",
            "Please be careful as it all ends.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【There are still other things to do】\x01",            # 0
            "[Enter into the Orkis Tower]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_BDB7"),
        (0, "loc_BED9"),
        (SWITCH_DEFAULT, "loc_BF03"),
    )


    label("loc_BDB7")

    OP_68(0, 1500, 30500, 4000)
    MoveCamera(0, 7, 0, 4000)

    def lambda_BDD8():
        OP_97(0x101, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BDD8)
    Sleep(50)

    def lambda_BDF5():
        OP_97(0x103, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BDF5)
    Sleep(50)

    def lambda_BE12():
        OP_97(0x102, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BE12)
    Sleep(50)

    def lambda_BE2F():
        OP_97(0x104, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BE2F)
    Sleep(50)

    def lambda_BE4C():
        OP_97(0x109, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_BE4C)
    Sleep(50)

    def lambda_BE69():
        OP_97(0x105, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_BE69)
    Sleep(700)
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    StopBGM(0xBB8)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("c1510", 0, 0, 0)
    IdleLoop()
    Jump("loc_BF03")

    label("loc_BED9")

    SetChrPos(0x0, 0, 0, 24500, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jump("loc_BF03")

    label("loc_BF03")

    EventEnd(0x5)
    Return()

    # Function_59_BA8D end

    def Function_60_BF06(): pass

    label("Function_60_BF06")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(1000)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "Mayor Dieter proposed\x01",
            "Question about the pros and cons of \"Cross Bell's national independence\"\x01",
            "The day of the referendum was approaching.\x02\x03",
            "Empire, republic government pressure also\x01",
            "Although it began to be blatant day by day\x01",
            "Citizen's interest is very high ……\x02\x03",
            "Depends on alkane shell\x01",
            "Coupled with the release of the renewal stage\x01",
            "The heat in the city was even higher.\x02\x03",
            "In such circumstances, a new problem\x01",
            "I was unknowingly getting up in the suburbs.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    PlayBGM("ed7151", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(0, 25000, 40000, 0)
    MoveCamera(335, -20, 0, 0)
    OP_6E(1100, 0)
    SetCameraDistance(70000, 0)
    OP_F0(0x0, 0x1)
    SetChrPos(0x0, 0, 0, 50000, 0)
    SetChrPos(0x1, 0, 0, 50000, 0)
    SetChrPos(0x2, 0, 0, 50000, 0)
    SetChrPos(0x3, 0, 0, 50000, 0)
    OP_68(0, 65000, 45000, 10000)
    MoveCamera(20, -35, 0, 10000)
    SetCameraDistance(120000, 10000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(1000)
    OP_68(0, 170000, 45000, 0)
    MoveCamera(30, -45, 0, 0)
    OP_6E(1100, 0)
    SetCameraDistance(80000, 0)
    OP_68(0, 175000, 45000, 5000)
    SetCameraDistance(60000, 5000)
    Sleep(3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_F0(0x0, 0xA)
    SetScenarioFlags(0x22, 4)
    NewScene("c1530", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_60_BF06 end

    def Function_61_C1A8(): pass

    label("Function_61_C1A8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch27200.itc", 0x1E)
    LoadChrToIndex("chr/ch27300.itc", 0x1F)
    LoadChrToIndex("chr/ch32000.itc", 0x20)
    LoadChrToIndex("chr/ch32100.itc", 0x21)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis251.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis408.itp")
    SetChrChipByIndex(0x32, 0x1E)
    SetChrSubChip(0x32, 0x0)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x32, 0x4)
    SetChrFlags(0x32, 0x8000)
    SetChrPos(0x32, 550, 200, 32700, 0)
    OP_A7(0x32, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x33, 0x1F)
    SetChrSubChip(0x33, 0x0)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x33, 0x4)
    SetChrFlags(0x33, 0x8000)
    SetChrPos(0x33, 1200, 200, 33700, 0)
    OP_A7(0x33, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x34, 0x20)
    SetChrSubChip(0x34, 0x0)
    ClearChrFlags(0x34, 0x80)
    ClearChrFlags(0x34, 0x4)
    SetChrFlags(0x34, 0x8000)
    SetChrPos(0x34, -550, 200, 32700, 0)
    OP_A7(0x34, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x35, 0x21)
    SetChrSubChip(0x35, 0x0)
    ClearChrFlags(0x35, 0x80)
    ClearChrFlags(0x35, 0x4)
    SetChrFlags(0x35, 0x8000)
    SetChrPos(0x35, -1200, 200, 33700, 0)
    OP_A7(0x35, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 900, 31000, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, -550, 0, 32400, 180)
    SetChrPos(0x102, 550, 0, 32400, 180)
    SetChrPos(0x103, -1200, 0, 33400, 180)
    SetChrPos(0x104, 1200, 0, 33400, 180)
    SetChrPos(0x109, -700, 0, 34400, 180)
    SetChrPos(0x105, 700, 0, 34400, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetCameraDistance(24000, 8500)
    FadeToBright(1000, 0)
    Sleep(500)
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    BeginChrThread(0x32, 3, 0, 62)
    Sleep(2000)
    BeginChrThread(0x101, 3, 0, 63)
    Sleep(3000)
    Sound(107, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x32, 0)
    OP_6F(0x79)
    EndChrThread(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    EndChrThread(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    EndChrThread(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    EndChrThread(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    EndChrThread(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    EndChrThread(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    EndChrThread(0x34, 0xFF)
    SetChrSubChip(0x34, 0x0)
    EndChrThread(0x33, 0xFF)
    SetChrSubChip(0x33, 0x0)
    EndChrThread(0x35, 0xFF)
    SetChrSubChip(0x35, 0x0)
    Fade(500)
    OP_68(-280, 1500, 19760, 0)
    MoveCamera(127, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17530, 0)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0x9, 0x8)
    SetCameraDistance(16530, 1500)
    SetChrPos(0x101, -600, 0, 20400, 180)
    SetChrPos(0x102, 600, 0, 20400, 180)
    SetChrPos(0x103, -1000, 0, 21400, 180)
    SetChrPos(0x104, 1000, 0, 21400, 180)
    SetChrPos(0x109, -600, 0, 22400, 180)
    SetChrPos(0x105, 600, 0, 22400, 180)
    SetChrPos(0x32, 600, 0, 17700, 0)
    SetChrPos(0x33, 1100, 0, 16700, 0)
    SetChrPos(0x34, -600, 0, 17700, 0)
    SetChrPos(0x35, -1100, 0, 16700, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x34,
        (
            "#11PIn short, with you\x01",
            "It is hard to fight in this way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x33,
        (
            "#11PFu … … From the very beginning\x01",
            "I can not imagine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00012Fmy mother……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FWell, as it is\x01",
            "You mean you are growing up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x32,
        "#11PNo, it's actually a big deal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x32,
        (
            "#11PIf you get fired of the police\x01",
            "Why do you welcome me anytime?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x35,
        "#11PYes Yes!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x35,
        (
            "#11PEspecially Tio-chan\x01",
            "I think that it is for the guild.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x35, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#6P#00211FEven so being told.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FHehu ……\x01",
            "I will only have your words.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FBut is \"a phantom beast\"?\x01",
            "It certainly comes to mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x32,
        (
            "#11POh, for the time being\x01",
            "Let's break it out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x32,
        (
            "#11PThe guard came from\x01",
            "5 cases in total ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x32,
        (
            "#11PTo you guys,\x01",
            "I want two categories to serve.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x105,
        (
            "#10302FWell, quite a while\x01",
            "It is a generosity, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FIs that ok?\x01",
            "Even though there is much division there … ….\x02\x03",
            "#00001FEven so, Arios\x01",
            "Now I can not move … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x34,
        "#11PThat is why.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x34,
        (
            "#11PBecause he can not move, you also\x01",
            "You should definitely bring wrinkles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x35,
        (
            "#11PEvil spirits are the origin\x01",
            "Hitter fighter#6RWe#The eighteenth of … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x35,
        (
            "#11PI have other jobs, each other\x01",
            "Should be shared efficiently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104F…… I am saved.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10108FSomething\x01",
            "I am sorry but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x32,
        "#11PWhat are you doing with each other.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x32,
        (
            "#11PAnd to you guys\x01",
            "There is also a problem of \"association\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00006F……Yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FGeez……\x01",
            "I have that problem.\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x46, 0x3E8)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(120, 210, -1, -1)

    AnonymousTalk(
        0x103,
        (
            "#00203FAssociation \"Serving meat snake#10RUroboros#\"… ….\x02\x03",
            "#00201FWhatever is the associate society\x01",
            "Different relationships … …?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(40, 200, -1, -1)

    AnonymousTalk(
        0x35,
        (
            "Yeah, even if Libert's strangeness\x01",
            "Let's start with escha-chan\x01",
            "The hypocrite missed … …\x02\x03",
            "Besides that, in various cases\x01",
            "You are confronted with it many times.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(230, 140, -1, -1)

    AnonymousTalk(
        0x33,
        (
            "…… The guild of the empire\x01",
            "It was also temporarily destroyed\x01",
            "It is said that they are doing their work.\x02\x03",
            "However, the cause of the subsequent decline is\x01",
            "It depends on the pressure of the Imperial Army.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 190, -1, -1)

    AnonymousTalk(
        0x101,
        "#00001FReally……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(100, 210, -1, -1)

    AnonymousTalk(
        0x104,
        (
            "#00301FBut the more I hear it\x01",
            "Think about it, hey guys.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    VolumeBGM(0x64, 0x3E8)
    Sleep(300)

    ChrTalk(
        0x32,
        (
            "#11PEither way, even the guild\x01",
            "They are still people who can not grasp the actual situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x32,
        (
            "#11PI do not know what is the purpose\x01",
            "Take care and be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x34,
        (
            "#11PIf there is something in trouble\x01",
            "Please do not hesitate to contact me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x34,
        (
            "#11PTo be honest, about the people\x01",
            "This is not another stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002F……I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FDo not hesitate if there is something\x01",
            "I will rely on it.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(17030, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xA)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_57(0x3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_E5(0xB)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 7)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_61_C1A8 end

    def Function_62_CF44(): pass

    label("Function_62_CF44")


    def lambda_CF49():
        OP_97(0x32, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x32, 0, lambda_CF49)
    Sleep(50)

    def lambda_CF66():
        OP_97(0x34, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 0, lambda_CF66)
    Sleep(50)

    def lambda_CF83():
        OP_97(0x33, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 0, lambda_CF83)
    Sleep(50)

    def lambda_CFA0():
        OP_97(0x35, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 0, lambda_CFA0)

    def lambda_CFBA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x32, 2, lambda_CFBA)
    Sleep(100)

    def lambda_CFCE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x34, 2, lambda_CFCE)
    Sleep(400)

    def lambda_CFE2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x33, 2, lambda_CFE2)
    Sleep(100)

    def lambda_CFF6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x35, 2, lambda_CFF6)
    Return()

    # Function_62_CF44 end

    def Function_63_D003(): pass

    label("Function_63_D003")


    def lambda_D008():
        OP_97(0x101, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D008)
    Sleep(50)

    def lambda_D025():
        OP_97(0x102, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_D025)
    Sleep(50)

    def lambda_D042():
        OP_97(0x103, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_D042)
    Sleep(50)

    def lambda_D05F():
        OP_97(0x104, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_D05F)
    Sleep(50)

    def lambda_D07C():
        OP_97(0x109, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D07C)
    Sleep(50)

    def lambda_D099():
        OP_97(0x105, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_D099)

    def lambda_D0B3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D0B3)
    Sleep(100)

    def lambda_D0C7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D0C7)
    Sleep(400)

    def lambda_D0DB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_D0DB)
    Sleep(100)

    def lambda_D0EF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_D0EF)
    Sleep(400)

    def lambda_D103():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_D103)
    Sleep(100)

    def lambda_D117():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_D117)
    Return()

    # Function_63_D003 end

    def Function_64_D124(): pass

    label("Function_64_D124")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05620.itc", 0x1E)
    LoadChrToIndex("apl/ch51524.itc", 0x1F)
    LoadChrToIndex("chr/ch03800.itc", 0x20)
    LoadChrToIndex("chr/ch12200.itc", 0x21)
    LoadChrToIndex("chr/ch41400.itc", 0x22)
    LoadChrToIndex("chr/ch41500.itc", 0x23)
    LoadChrToIndex("chr/ch41800.itc", 0x24)
    LoadChrToIndex("chr/ch06000.itc", 0x25)
    LoadChrToIndex("chr/ch47900.itc", 0x26)
    LoadChrToIndex("apl/ch50314.itc", 0x27)
    LoadChrToIndex("chr/ch27400.itc", 0x28)
    LoadChrToIndex("chr/ch27800.itc", 0x29)
    LoadChrToIndex("chr/ch27900.itc", 0x2A)
    LoadChrToIndex("chr/ch27600.itc", 0x2B)
    LoadEffect(0x0, "event\\eva02_00.eff")
    SoundLoad(851)
    SoundLoad(835)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu11300.itp")
    SetChrPos(0x0, 0, 0, 50000, 0)
    SetChrPos(0x1, 0, 0, 50000, 0)
    SetChrPos(0x2, 0, 0, 50000, 0)
    SetChrPos(0x3, 0, 0, 50000, 0)
    SetChrChipByIndex(0x30, 0x1E)
    SetChrSubChip(0x30, 0x0)
    ClearChrFlags(0x30, 0x80)
    SetChrFlags(0x30, 0x8000)
    SetChrPos(0x30, 0, 10500, 35000, 180)
    OP_8E(0x30, "President Dieter")
    SetChrChipByIndex(0x36, 0x20)
    SetChrSubChip(0x36, 0x0)
    ClearChrFlags(0x36, 0x80)
    SetChrFlags(0x36, 0x8000)
    SetChrPos(0x36, -1400, 10380, 36500, 180)
    OP_52(0x36, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x36, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x36, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x47, 0x21)
    SetChrSubChip(0x47, 0x0)
    ClearChrFlags(0x47, 0x80)
    SetChrFlags(0x47, 0x8000)
    SetChrPos(0x47, -2500, 10380, 36500, 180)
    SetChrChipByIndex(0x63, 0x22)
    SetChrSubChip(0x63, 0x0)
    ClearChrFlags(0x63, 0x80)
    SetChrFlags(0x63, 0x8000)
    SetChrPos(0x63, -5500, 10380, 37000, 180)
    SetChrChipByIndex(0x64, 0x23)
    SetChrSubChip(0x64, 0x0)
    ClearChrFlags(0x64, 0x80)
    SetChrFlags(0x64, 0x8000)
    SetChrPos(0x64, 5500, 10380, 37000, 180)
    SetChrChipByIndex(0x65, 0x23)
    SetChrSubChip(0x65, 0x0)
    ClearChrFlags(0x65, 0x80)
    SetChrFlags(0x65, 0x8000)
    SetChrPos(0x65, -900, 0, 15500, 180)
    SetChrChipByIndex(0x66, 0x23)
    SetChrSubChip(0x66, 0x0)
    ClearChrFlags(0x66, 0x80)
    SetChrFlags(0x66, 0x8000)
    SetChrPos(0x66, -2300, 0, 15500, 180)
    SetChrChipByIndex(0x67, 0x24)
    SetChrSubChip(0x67, 0x0)
    ClearChrFlags(0x67, 0x80)
    SetChrFlags(0x67, 0x8000)
    SetChrPos(0x67, 900, 0, 15500, 180)
    SetChrChipByIndex(0x68, 0x24)
    SetChrSubChip(0x68, 0x0)
    ClearChrFlags(0x68, 0x80)
    SetChrFlags(0x68, 0x8000)
    SetChrPos(0x68, 2300, 0, 15500, 180)
    SetChrChipByIndex(0x69, 0x22)
    SetChrSubChip(0x69, 0x0)
    ClearChrFlags(0x69, 0x80)
    SetChrFlags(0x69, 0x8000)
    SetChrPos(0x69, -9800, 0, 14500, 135)
    SetChrChipByIndex(0x6A, 0x22)
    SetChrSubChip(0x6A, 0x0)
    ClearChrFlags(0x6A, 0x80)
    SetChrFlags(0x6A, 0x8000)
    SetChrPos(0x6A, 9800, 0, 14500, 225)
    SetChrChipByIndex(0x6B, 0x25)
    SetChrSubChip(0x6B, 0x0)
    ClearChrFlags(0x6B, 0x80)
    SetChrFlags(0x6B, 0x8000)
    SetChrPos(0x6B, 600, 250, 12600, 0)
    OP_4B(0x1F, 0xFF)
    SetChrChipByIndex(0x1F, 0x26)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -2000, 250, 12600, 0)
    SetChrChipByIndex(0x6C, 0x27)
    SetChrSubChip(0x6C, 0x0)
    ClearChrFlags(0x6C, 0x80)
    SetChrFlags(0x6C, 0x8000)
    SetChrPos(0x6C, 1700, 250, 12200, 0)
    SetChrChipByIndex(0x6D, 0x28)
    SetChrSubChip(0x6D, 0x0)
    ClearChrFlags(0x6D, 0x80)
    SetChrFlags(0x6D, 0x8000)
    SetChrPos(0x6D, -1700, 250, 10900, 0)
    SetChrChipByIndex(0x6E, 0x29)
    SetChrSubChip(0x6E, 0x0)
    ClearChrFlags(0x6E, 0x80)
    SetChrFlags(0x6E, 0x8000)
    SetChrPos(0x6E, 0, 250, 11300, 0)
    SetChrChipByIndex(0x6F, 0x2A)
    SetChrSubChip(0x6F, 0x0)
    ClearChrFlags(0x6F, 0x80)
    SetChrFlags(0x6F, 0x8000)
    SetChrPos(0x6F, -1000, 250, 12100, 0)
    SetChrChipByIndex(0x70, 0x2B)
    SetChrSubChip(0x70, 0x0)
    ClearChrFlags(0x70, 0x80)
    SetChrFlags(0x70, 0x8000)
    SetChrPos(0x70, 1200, 250, 10700, 0)
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x22)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x12, 0x2)
    SetChrSubChip(0x12, 0x0)
    OP_4B(0x12, 0xFF)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 800, 100, 8300, 0)
    OP_4B(0x13, 0xFF)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 2000, 100, 7300, 0)
    OP_4B(0x14, 0xFF)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 3100, 100, 8600, 0)
    OP_4B(0x15, 0xFF)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, -800, 100, 8300, 0)
    OP_4B(0x16, 0xFF)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, -2000, 100, 7300, 0)
    SetChrChipByIndex(0x17, 0x3)
    SetChrSubChip(0x17, 0x0)
    OP_4B(0x17, 0xFF)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, -3100, 100, 8600, 0)
    ClearChrFlags(0x71, 0x80)
    OP_78(0x10, 0x71)
    OP_49()
    SetChrPos(0x71, -8500, 0, 17000, 180)
    OP_D5(0x71, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x10, 0x1000)
    ClearMapObjFlags(0x10, 0x4)
    OP_74(0x10, 0x1E)
    OP_70(0x10, 0x0)
    ClearChrFlags(0x72, 0x80)
    OP_78(0x11, 0x72)
    OP_49()
    SetChrPos(0x72, 6500, 0, 17000, 180)
    OP_D5(0x72, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x11, 0x1000)
    ClearMapObjFlags(0x11, 0x4)
    OP_74(0x11, 0x1E)
    OP_70(0x11, 0x0)
    SetMapObjFlags(0x19, 0x1000)
    ClearMapObjFlags(0x19, 0x4)
    OP_68(0, 1500, 13000, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(15500, 0)
    Sound(851, 2, 50, 0)
    Sound(835, 2, 80, 0)
    BeginChrThread(0x6C, 0, 0, 65)
    SetCameraDistance(17500, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(0, 1500, 13000, 0)
    MoveCamera(35, 25, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(15000, 0)
    OP_0D()
    OP_68(0, 11600, 34750, 6000)
    MoveCamera(30, 27, 0, 6000)
    SetCameraDistance(14000, 6000)
    OP_6F(0x79)
    Fade(500)
    OP_68(0, 11500, 34750, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(13000, 0)
    SetChrChipByIndex(0x30, 0x1F)
    SetChrSubChip(0x30, 0x0)
    SetChrFlags(0x30, 0x10)
    SetChrFlags(0x30, 0x2)
    SetCameraDistance(12000, 3000)
    OP_6F(0x79)
    ClearChrFlags(0x30, 0x10)
    ClearChrFlags(0x30, 0x2)
    SetChrChipByIndex(0x30, 0x1E)
    SetChrSubChip(0x30, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x30,
        (
            "── Everyone, thank you.\x02\x03",
            "This time, \"Crossbell independent country\"\x01",
            "I became the first President\x01",
            "It is Dieter Crois.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    PlayBGM("ed7566", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x236), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    StopSound(851, 1000, 50)
    StopSound(835, 1000, 80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 1)
    NewScene("c110D", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_64_D124 end

    def Function_65_D865(): pass

    label("Function_65_D865")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D91D")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D893")
    Sleep(500)
    Jump("loc_D8DB")

    label("loc_D893")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D8AA")
    Sleep(1000)
    Jump("loc_D8DB")

    label("loc_D8AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D8C1")
    Sleep(1500)
    Jump("loc_D8DB")

    label("loc_D8C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D8D8")
    Sleep(2000)
    Jump("loc_D8DB")

    label("loc_D8D8")

    Sleep(2500)

    label("loc_D8DB")

    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(810, 0, 70, 0)
    Jump("Function_65_D865")

    label("loc_D91D")

    Return()

    # Function_65_D865 end

    def Function_66_D91E(): pass

    label("Function_66_D91E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05620.itc", 0x1E)
    LoadChrToIndex("apl/ch51525.itc", 0x1F)
    LoadChrToIndex("chr/ch03800.itc", 0x20)
    LoadChrToIndex("chr/ch12200.itc", 0x21)
    LoadChrToIndex("chr/ch41400.itc", 0x22)
    LoadChrToIndex("chr/ch41500.itc", 0x23)
    LoadChrToIndex("chr/ch41800.itc", 0x24)
    LoadChrToIndex("chr/ch06000.itc", 0x25)
    LoadChrToIndex("chr/ch47900.itc", 0x26)
    LoadChrToIndex("apl/ch50314.itc", 0x27)
    LoadChrToIndex("chr/ch27400.itc", 0x28)
    LoadChrToIndex("chr/ch27800.itc", 0x29)
    LoadChrToIndex("chr/ch27900.itc", 0x2A)
    LoadChrToIndex("chr/ch27600.itc", 0x2B)
    LoadEffect(0x0, "event\\eva02_00.eff")
    SoundLoad(821)
    SoundLoad(835)
    SoundLoad(4084)
    SoundLoad(4085)
    SoundLoad(4086)
    SoundLoad(4087)
    SoundLoad(4088)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10501.itp")
    CreatePortrait(1, 224, 0, 480, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10500.itp")
    SetChrPos(0x0, 0, 0, 50000, 0)
    SetChrPos(0x1, 0, 0, 50000, 0)
    SetChrPos(0x2, 0, 0, 50000, 0)
    SetChrPos(0x3, 0, 0, 50000, 0)
    SetChrChipByIndex(0x30, 0x1F)
    SetChrSubChip(0x30, 0x0)
    SetChrFlags(0x30, 0x10)
    SetChrFlags(0x30, 0x2)
    ClearChrFlags(0x30, 0x80)
    SetChrFlags(0x30, 0x8000)
    SetChrPos(0x30, 0, 10500, 35000, 180)
    OP_8E(0x30, "President Dieter")
    SetChrChipByIndex(0x36, 0x20)
    SetChrSubChip(0x36, 0x0)
    ClearChrFlags(0x36, 0x80)
    SetChrFlags(0x36, 0x8000)
    SetChrPos(0x36, -1400, 10380, 36500, 180)
    OP_52(0x36, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x36, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x36, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x47, 0x21)
    SetChrSubChip(0x47, 0x0)
    ClearChrFlags(0x47, 0x80)
    SetChrFlags(0x47, 0x8000)
    SetChrPos(0x47, -2500, 10380, 36500, 180)
    SetChrChipByIndex(0x63, 0x22)
    SetChrSubChip(0x63, 0x0)
    ClearChrFlags(0x63, 0x80)
    SetChrFlags(0x63, 0x8000)
    SetChrPos(0x63, -5500, 10380, 37000, 180)
    SetChrChipByIndex(0x64, 0x23)
    SetChrSubChip(0x64, 0x0)
    ClearChrFlags(0x64, 0x80)
    SetChrFlags(0x64, 0x8000)
    SetChrPos(0x64, 5500, 10380, 37000, 180)
    SetChrChipByIndex(0x65, 0x23)
    SetChrSubChip(0x65, 0x0)
    ClearChrFlags(0x65, 0x80)
    SetChrFlags(0x65, 0x8000)
    SetChrPos(0x65, -900, 0, 15500, 180)
    SetChrChipByIndex(0x66, 0x23)
    SetChrSubChip(0x66, 0x0)
    ClearChrFlags(0x66, 0x80)
    SetChrFlags(0x66, 0x8000)
    SetChrPos(0x66, -2300, 0, 15500, 180)
    SetChrChipByIndex(0x67, 0x24)
    SetChrSubChip(0x67, 0x0)
    ClearChrFlags(0x67, 0x80)
    SetChrFlags(0x67, 0x8000)
    SetChrPos(0x67, 900, 0, 15500, 180)
    SetChrChipByIndex(0x68, 0x24)
    SetChrSubChip(0x68, 0x0)
    ClearChrFlags(0x68, 0x80)
    SetChrFlags(0x68, 0x8000)
    SetChrPos(0x68, 2300, 0, 15500, 180)
    SetChrChipByIndex(0x69, 0x22)
    SetChrSubChip(0x69, 0x0)
    ClearChrFlags(0x69, 0x80)
    SetChrFlags(0x69, 0x8000)
    SetChrPos(0x69, -9800, 0, 14500, 135)
    SetChrChipByIndex(0x6A, 0x22)
    SetChrSubChip(0x6A, 0x0)
    ClearChrFlags(0x6A, 0x80)
    SetChrFlags(0x6A, 0x8000)
    SetChrPos(0x6A, 9800, 0, 14500, 225)
    SetChrChipByIndex(0x6B, 0x25)
    SetChrSubChip(0x6B, 0x0)
    ClearChrFlags(0x6B, 0x80)
    SetChrFlags(0x6B, 0x8000)
    SetChrPos(0x6B, 600, 250, 12600, 0)
    OP_4B(0x1F, 0xFF)
    SetChrChipByIndex(0x1F, 0x26)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -2000, 250, 12600, 0)
    SetChrChipByIndex(0x6C, 0x27)
    SetChrSubChip(0x6C, 0x0)
    ClearChrFlags(0x6C, 0x80)
    SetChrFlags(0x6C, 0x8000)
    SetChrPos(0x6C, 1700, 250, 12200, 0)
    SetChrChipByIndex(0x6D, 0x28)
    SetChrSubChip(0x6D, 0x0)
    ClearChrFlags(0x6D, 0x80)
    SetChrFlags(0x6D, 0x8000)
    SetChrPos(0x6D, -1700, 250, 10900, 0)
    SetChrChipByIndex(0x6E, 0x29)
    SetChrSubChip(0x6E, 0x0)
    ClearChrFlags(0x6E, 0x80)
    SetChrFlags(0x6E, 0x8000)
    SetChrPos(0x6E, 0, 250, 11300, 0)
    SetChrChipByIndex(0x6F, 0x2A)
    SetChrSubChip(0x6F, 0x0)
    ClearChrFlags(0x6F, 0x80)
    SetChrFlags(0x6F, 0x8000)
    SetChrPos(0x6F, -1000, 250, 12100, 0)
    SetChrChipByIndex(0x70, 0x2B)
    SetChrSubChip(0x70, 0x0)
    ClearChrFlags(0x70, 0x80)
    SetChrFlags(0x70, 0x8000)
    SetChrPos(0x70, 1200, 250, 10700, 0)
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x22)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x12, 0x2)
    SetChrSubChip(0x12, 0x0)
    OP_4B(0x12, 0xFF)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 800, 100, 8300, 0)
    OP_4B(0x13, 0xFF)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 2000, 100, 7300, 0)
    OP_4B(0x14, 0xFF)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 3100, 100, 8600, 0)
    OP_4B(0x15, 0xFF)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, -800, 100, 8300, 0)
    OP_4B(0x16, 0xFF)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, -2000, 100, 7300, 0)
    SetChrChipByIndex(0x17, 0x3)
    SetChrSubChip(0x17, 0x0)
    OP_4B(0x17, 0xFF)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, -3100, 100, 8600, 0)
    ClearChrFlags(0x71, 0x80)
    OP_78(0x10, 0x71)
    OP_49()
    SetChrPos(0x71, -8500, 0, 17000, 180)
    OP_D5(0x71, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x10, 0x1000)
    ClearMapObjFlags(0x10, 0x4)
    OP_74(0x10, 0x1E)
    OP_70(0x10, 0x1)
    ClearChrFlags(0x72, 0x80)
    OP_78(0x11, 0x72)
    OP_49()
    SetChrPos(0x72, 6500, 0, 17000, 180)
    OP_D5(0x72, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x11, 0x1000)
    ClearMapObjFlags(0x11, 0x4)
    OP_74(0x11, 0x1E)
    OP_70(0x11, 0x1)
    SetMapObjFlags(0x19, 0x1000)
    ClearMapObjFlags(0x19, 0x4)
    OP_63(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x14, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x16, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x17, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    BeginChrThread(0x6C, 0, 0, 65)
    OP_68(0, 5000, 19500, 0)
    MoveCamera(0, 0, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(25000, 0)
    Sound(821, 2, 60, 0)
    Sound(835, 2, 80, 0)
    OP_68(0, 4000, 19500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x30,
        (
            "#11303F#6P─ ─ For that I am today,\x01",
            "In the position of President\x01",
            "It was decided that I would like to start.\x02\x03",
            "#11300FOf course this is only\x01",
            "To cope with the imminent crisis\x01",
            "It is only an interim measure.\x02\x03",
            "#11304FEvery time we regain peace\x01",
            "Asking people's will in the form of elections\x01",
            "I promise you on this occasion.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 11400, 34500, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(13500, 0)
    OP_0D()
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x30, 0x1E)
    SetChrSubChip(0x30, 0x0)
    ClearChrFlags(0x30, 0x10)
    ClearChrFlags(0x30, 0x2)
    OP_0D()
    Sleep(300)
    TurnDirection(0x30, 0x36, 500)
    Sleep(150)

    ChrTalk(
        0x30,
        (
            "#11303F#11PAnd one more …\x02\x03",
            "#11300FThis person who also knows well,\x01",
            "New-generation \"Crossbell independent country\"\x01",
            "It was to cooperate.\x02",
        )
    )

    CloseMessageWindow()
    MoveCamera(27, 20, 0, 1500)
    SetCameraDistance(13000, 1500)
    BeginChrThread(0x30, 1, 0, 67)
    Sleep(300)
    BeginChrThread(0x36, 1, 0, 68)
    WaitChrThread(0x30, 1)
    WaitChrThread(0x36, 1)
    OP_93(0x30, 0xB4, 0x1F4)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x30,
        (
            "#11304F#5PLet me introduce\x02\x03",
            "In the previous Crossbell City raid\x01",
            "With the work of Shishinpaku Orkis Tower\x01",
            "Person who protected himself … …\x02\x03",
            "#11300FKnown under the name \"Wind sword of the wind\"\x01",
            "To the Association of Shogi Shogaku and Crosbell\x01",
            "A former A gravel fighter belonging … …\x02\x03",
            "#11309FCommander General of the Cross Bell National Defense Force,\x01",
            "Arios McClein!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    VolumeBGM(0x50, 0x1F4)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(1000)
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x15E, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0x36,
        (
            "#4084V── I was in the introduction,\x01",
            "It is Arios · McLaein.\x02\x03",
            "#4085VBecause of still young people,\x01",
            "Some people who feel uneasy\x01",
            "You may come.\x02\x03",
            "#4086VHowever, than working as a hypothetical wrestler\x01",
            "I will deny any threat\x01",
            "Let's promise.\x02\x03",
            "#4087VAs a shield that defends the crossbell … …\x02\x03",
            "#4088VAnd threaten justice and peace\x01",
            "As a sword to defeat all enemies …!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xFF8)
    VolumeBGM(0x64, 0x3E8)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_C9(0x1, 0x80000000)
    StopSound(851, 1000, 70)
    StopSound(835, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 6)
    NewScene("c1550", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_66_D91E end

    def Function_67_E4A6(): pass

    label("Function_67_E4A6")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_96(0xFE, 0x3E8, 0x2904, 0x88B8, 0x3E8, 0x0)
    Return()

    # Function_67_E4A6 end

    def Function_68_E4C2(): pass

    label("Function_68_E4C2")

    OP_95(0xFE, 0, 10380, 35600, 1500, 0x0)
    OP_95(0xFE, 0, 10500, 35000, 1500, 0x0)
    Return()

    # Function_68_E4C2 end

    def Function_69_E4EB(): pass

    label("Function_69_E4EB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 25000, 40000, 0)
    MoveCamera(335, -20, 0, 0)
    OP_6E(1100, 0)
    SetCameraDistance(70000, 0)
    OP_F0(0x0, 0x1)
    SetChrPos(0x0, 0, 0, 50000, 0)
    SetChrPos(0x1, 0, 0, 50000, 0)
    SetChrPos(0x2, 0, 0, 50000, 0)
    SetChrPos(0x3, 0, 0, 50000, 0)
    OP_68(0, 65000, 45000, 8000)
    MoveCamera(20, -35, 0, 8000)
    SetCameraDistance(120000, 8000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(1000)
    OP_68(0, 80000, 45000, 0)
    MoveCamera(35, -15, 0, 0)
    OP_6E(1100, 0)
    SetCameraDistance(80000, 0)
    SetCameraDistance(60000, 4000)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_F0(0x0, 0xA)
    SetScenarioFlags(0x22, 0)
    NewScene("c1560", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_69_E4EB end

    def Function_70_E5F9(): pass

    label("Function_70_E5F9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51719.itc", 0x0)
    LoadChrToIndex("apl/ch51718.itc", 0x1)
    LoadChrToIndex("chr/ch32050.itc", 0x2)
    LoadChrToIndex("chr/ch32051.itc", 0x3)
    LoadChrToIndex("chr/ch32052.itc", 0x4)
    LoadChrToIndex("chr/ch32056.itc", 0x5)
    LoadChrToIndex("chr/ch32150.itc", 0x6)
    LoadChrToIndex("chr/ch32151.itc", 0x7)
    LoadChrToIndex("chr/ch32152.itc", 0x8)
    LoadChrToIndex("monster/ch85150.itc", 0x9)
    LoadChrToIndex("monster/ch85151.itc", 0xA)
    LoadChrToIndex("monster/ch85153.itc", 0xB)
    LoadChrToIndex("monster/ch85152.itc", 0xC)
    LoadChrToIndex("apl/ch50509.itc", 0xD)
    LoadChrToIndex("apl/ch50506.itc", 0xE)
    LoadChrToIndex("chr/ch30200.itc", 0xF)
    LoadChrToIndex("apl/ch51720.itc", 0x10)
    LoadChrToIndex("chr/ch30500.itc", 0x11)
    LoadChrToIndex("chr/ch30100.itc", 0x12)
    LoadChrToIndex("chr/ch30000.itc", 0x13)
    LoadChrToIndex("apl/ch51236.itc", 0x14)
    LoadChrToIndex("apl/ch50006.itc", 0x15)
    LoadChrToIndex("apl/ch51721.itc", 0x16)
    LoadChrToIndex("apl/ch51760.itc", 0x17)
    LoadChrToIndex("apl/ch51762.itc", 0x18)
    LoadChrToIndex("apl/ch51722.itc", 0x19)
    LoadChrToIndex("apl/ch51764.itc", 0x1A)
    LoadChrToIndex("apl/ch51765.itc", 0x1B)
    LoadChrToIndex("apl/ch50372.itc", 0x1C)
    LoadChrToIndex("apl/ch51766.itc", 0x1D)
    LoadChrToIndex("apl/ch51763.itc", 0x1E)
    LoadChrToIndex("chr/ch30600.itc", 0x1F)
    LoadEffect(0x9, "map/mpmoya.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0x78, 0x96, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xFF, 0xD, 0x190, 0x0)
    LoadEffect(0x0, "event/ev17060.eff")
    LoadEffect(0x1, "event/ev17062.eff")
    LoadEffect(0x2, "battle/btgun00.eff")
    LoadEffect(0x3, "event/ev606_00.eff")
    LoadEffect(0x4, "battle\\ms00001.eff")
    LoadEffect(0x5, "event/eva01_01.eff")
    LoadEffect(0x6, "battle\\cr320000.eff")
    LoadEffect(0x7, "event/ev17046.eff")
    LoadEffect(0x8, "event\\ev310_00.eff")
    SoundLoad(861)
    SoundLoad(863)
    SoundLoad(926)
    OP_8E(0x2F, "Kirika")
    OP_8E(0x28, "Rector")
    SetChrPos(0x0, 0, 0, 50000, 0)
    SetChrPos(0x1, 0, 0, 50000, 0)
    SetChrPos(0x2, 0, 0, 50000, 0)
    SetChrPos(0x3, 0, 0, 50000, 0)
    SetChrChipByIndex(0x32, 0x0)
    SetChrSubChip(0x32, 0x0)
    SetChrFlags(0x32, 0x8000)
    ClearChrFlags(0x32, 0x4)
    SetChrPos(0x32, 800, 0, -17400, 0)
    SetChrChipByIndex(0x33, 0x1)
    SetChrSubChip(0x33, 0x0)
    SetChrFlags(0x33, 0x8000)
    ClearChrFlags(0x33, 0x4)
    SetChrPos(0x33, 600, 0, -15600, 0)
    SetChrChipByIndex(0x34, 0x2)
    SetChrSubChip(0x34, 0x0)
    SetChrFlags(0x34, 0x8000)
    ClearChrFlags(0x34, 0x4)
    SetChrPos(0x34, -600, 0, -15600, 0)
    SetChrChipByIndex(0x35, 0x6)
    SetChrSubChip(0x35, 0x0)
    SetChrFlags(0x35, 0x8000)
    ClearChrFlags(0x35, 0x4)
    SetChrPos(0x35, -800, 0, -17400, 0)
    SetChrChipByIndex(0x38, 0xF)
    SetChrSubChip(0x38, 0x0)
    SetChrFlags(0x38, 0x8000)
    ClearChrFlags(0x38, 0x4)
    SetChrPos(0x38, 5200, 250, 300, 135)
    OP_A7(0x38, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x48, 0x13)
    SetChrSubChip(0x48, 0x0)
    SetChrFlags(0x48, 0x8000)
    ClearChrFlags(0x48, 0x4)
    SetChrPos(0x48, 5200, 250, 300, 135)
    OP_A7(0x48, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x3C, 0x13)
    SetChrSubChip(0x3C, 0x0)
    SetChrFlags(0x3C, 0x8000)
    ClearChrFlags(0x3C, 0x4)
    SetChrPos(0x3C, 5200, 250, 300, 135)
    OP_A7(0x3C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x49, 0x13)
    SetChrSubChip(0x49, 0x0)
    SetChrFlags(0x49, 0x8000)
    ClearChrFlags(0x49, 0x4)
    SetChrPos(0x49, -5200, 250, 300, 225)
    OP_A7(0x49, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x39, 0x11)
    SetChrSubChip(0x39, 0x0)
    SetChrFlags(0x39, 0x8000)
    ClearChrFlags(0x39, 0x4)
    SetChrPos(0x39, -5200, 250, 300, 225)
    OP_A7(0x39, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x4A, 0x13)
    SetChrSubChip(0x4A, 0x0)
    SetChrFlags(0x4A, 0x8000)
    ClearChrFlags(0x4A, 0x4)
    SetChrPos(0x4A, -5200, 250, 300, 225)
    OP_A7(0x4A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x3B, 0x1F)
    SetChrSubChip(0x3B, 0x0)
    SetChrFlags(0x3B, 0x8000)
    ClearChrFlags(0x3B, 0x4)
    SetChrPos(0x3B, -5200, 250, 300, 225)
    OP_A7(0x3B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x3A, 0x12)
    SetChrSubChip(0x3A, 0x0)
    SetChrFlags(0x3A, 0x8000)
    ClearChrFlags(0x3A, 0x4)
    SetChrPos(0x3A, 5200, 250, 300, 135)
    OP_A7(0x3A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x23, 0xD)
    SetChrSubChip(0x23, 0x0)
    SetChrFlags(0x23, 0x8000)
    ClearChrFlags(0x23, 0x4)
    SetChrPos(0x23, -5200, 250, 300, 225)
    OP_A7(0x23, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x2F, 0x19)
    SetChrSubChip(0x2F, 0x0)
    SetChrFlags(0x2F, 0x8000)
    ClearChrFlags(0x2F, 0x4)
    SetChrPos(0x2F, -11000, 250, -4500, 0)
    SetChrChipByIndex(0x28, 0x16)
    SetChrSubChip(0x28, 0x0)
    SetChrFlags(0x28, 0x8000)
    ClearChrFlags(0x28, 0x4)
    SetChrPos(0x28, 2500, 0, -10000, 0)
    SetChrChipByIndex(0x3E, 0x9)
    SetChrSubChip(0x3E, 0x0)
    ClearChrFlags(0x3E, 0x80)
    SetChrFlags(0x3E, 0x8000)
    OP_52(0x3E, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x3E, -2000, 250, 9500, 180)
    BeginChrThread(0x3E, 0, 0, 8)
    SetChrChipByIndex(0x3F, 0x9)
    SetChrSubChip(0x3F, 0x0)
    ClearChrFlags(0x3F, 0x80)
    SetChrFlags(0x3F, 0x8000)
    OP_52(0x3F, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x3F, 2000, 250, 9500, 180)
    BeginChrThread(0x3F, 0, 0, 8)
    SetChrChipByIndex(0x40, 0x9)
    SetChrSubChip(0x40, 0x0)
    ClearChrFlags(0x40, 0x80)
    SetChrFlags(0x40, 0x8000)
    OP_52(0x40, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x40, -6000, 0, 12500, 180)
    BeginChrThread(0x40, 0, 0, 8)
    SetChrChipByIndex(0x41, 0x9)
    SetChrSubChip(0x41, 0x0)
    ClearChrFlags(0x41, 0x80)
    SetChrFlags(0x41, 0x8000)
    OP_52(0x41, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x41, 6000, 0, 12500, 180)
    BeginChrThread(0x41, 0, 0, 8)
    SetChrChipByIndex(0x42, 0x9)
    SetChrSubChip(0x42, 0x0)
    ClearChrFlags(0x42, 0x80)
    SetChrFlags(0x42, 0x8000)
    OP_52(0x42, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x42, 4000, 0, 16500, 180)
    BeginChrThread(0x42, 0, 0, 8)
    SetChrChipByIndex(0x43, 0x9)
    SetChrSubChip(0x43, 0x0)
    ClearChrFlags(0x43, 0x80)
    SetChrFlags(0x43, 0x8000)
    OP_52(0x43, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x43, -4000, 0, 16500, 180)
    BeginChrThread(0x43, 0, 0, 8)
    ClearChrFlags(0x71, 0x80)
    ClearChrFlags(0x71, 0x4)
    OP_78(0x12, 0x71)
    SetMapObjFrame(0x12, "light", 0x0, 0x1)
    OP_49()
    OP_90(0x71, 0, -8500, -54800, 0)
    OP_D5(0x71, 0xFFFFCD38, 0x0, 0x0, 0x0)
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x12, 0x1000)
    OP_74(0x12, 0x1E)
    OP_71(0x12, 0xB5, 0xF0, 0x0, 0x20)
    ClearChrFlags(0x72, 0x80)
    ClearChrFlags(0x72, 0x4)
    OP_78(0x13, 0x72)
    SetMapObjFrame(0x13, "light", 0x0, 0x1)
    OP_49()
    OP_90(0x72, 0, -10500, -61800, 0)
    OP_D5(0x72, 0xFFFFCD38, 0x0, 0x0, 0x0)
    ClearMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x13, 0x1000)
    OP_74(0x13, 0x1E)
    OP_71(0x13, 0xB5, 0xF0, 0x0, 0x20)
    ClearChrFlags(0x73, 0x80)
    ClearChrFlags(0x73, 0x4)
    OP_78(0x14, 0x73)
    SetMapObjFrame(0x14, "light", 0x0, 0x1)
    OP_49()
    OP_90(0x73, 0, -13500, -75800, 0)
    OP_D5(0x73, 0xFFFFCD38, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x14, 0x1000)
    OP_74(0x14, 0x1E)
    OP_70(0x14, 0x0)
    OP_71(0x14, 0xB5, 0xF0, 0x0, 0x20)
    SetMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x17, 0x1000)
    OP_74(0x17, 0x1E)
    OP_70(0x17, 0x0)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x18, 0x4)
    SetMapObjFlags(0x18, 0x1000)
    ClearChrFlags(0x75, 0x80)
    OP_78(0x15, 0x75)
    OP_49()
    SetChrPos(0x75, 0, 0, -20000, 0)
    OP_D5(0x75, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x15, 0x1000)
    ClearChrFlags(0x76, 0x80)
    OP_78(0x16, 0x76)
    OP_49()
    SetChrPos(0x76, 0, 0, 0, 0)
    OP_D5(0x76, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x16, 0x4)
    SetMapObjFlags(0x16, 0x1000)
    SetChrChipByIndex(0x77, 0x1C)
    SetChrSubChip(0x77, 0x0)
    SetChrChipByIndex(0x78, 0x1C)
    SetChrSubChip(0x78, 0x0)
    SetChrFlags(0x77, 0x8000)
    SetChrFlags(0x78, 0x8000)
    SetChrFlags(0x77, 0x20)
    SetChrFlags(0x78, 0x20)
    SetChrFlags(0x77, 0x2)
    SetChrFlags(0x78, 0x2)
    SetChrFlags(0x77, 0x10)
    SetChrFlags(0x78, 0x10)
    BeginChrThread(0x77, 0, 0, 125)
    BeginChrThread(0x78, 0, 0, 125)
    ClearChrFlags(0x38, 0x80)
    ClearChrFlags(0x39, 0x80)
    ClearChrFlags(0x3A, 0x80)
    ClearChrFlags(0x4A, 0x80)
    ClearChrFlags(0x3B, 0x80)
    ClearChrFlags(0x3C, 0x80)
    ClearChrFlags(0x48, 0x80)
    ClearChrFlags(0x49, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearScenarioFlags(0x1, 1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    OP_68(0, 3000, 15000, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(20500, 0)
    OP_68(0, 1000, 15000, 5000)
    MoveCamera(0, 15, 5, 5000)
    SetCameraDistance(17500, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)
    Fade(500)
    OP_68(0, -3050, -40000, 0)
    MoveCamera(0, 11, 0, 0)
    OP_6E(850, 0)
    SetCameraDistance(17500, 0)
    OP_F0(0x0, 0x1)
    SetChrPos(0x42, 3000, 0, 16500, 180)
    SetChrPos(0x43, -3000, 0, 16500, 180)
    BeginChrThread(0x71, 3, 0, 118)
    BeginChrThread(0x72, 3, 0, 119)
    BeginChrThread(0x79, 1, 0, 133)
    OP_68(0, 1350, 3300, 7000)
    MoveCamera(27, 17, 0, 7000)
    OP_6E(750, 7000)
    SetCameraDistance(19500, 7000)
    Sleep(6000)

    def lambda_EFD7():
        OP_93(0xFE, 0xC8, 0x1F4)
        ExitThread()

    QueueWorkItem(0x40, 2, lambda_EFD7)
    Sleep(500)

    def lambda_EFE7():
        OP_93(0xFE, 0xC8, 0x1F4)
        ExitThread()

    QueueWorkItem(0x43, 2, lambda_EFE7)
    WaitChrThread(0x71, 3)
    Sound(861, 2, 30, 0)
    Sound(863, 2, 50, 0)
    BeginChrThread(0x71, 3, 0, 80)
    WaitChrThread(0x72, 3)
    BeginChrThread(0x72, 3, 0, 81)
    BeginChrThread(0x3E, 2, 0, 83)
    BeginChrThread(0x3E, 1, 0, 138)
    Sleep(300)
    BeginChrThread(0x3F, 2, 0, 83)
    BeginChrThread(0x3F, 1, 0, 139)
    Sleep(300)
    BeginChrThread(0x40, 2, 0, 83)
    BeginChrThread(0x40, 1, 0, 140)
    Sleep(300)
    BeginChrThread(0x41, 2, 0, 83)
    BeginChrThread(0x41, 1, 0, 141)
    WaitChrThread(0x39, 3)
    WaitChrThread(0x3A, 3)
    Sleep(500)
    OP_6F(0x79)
    OP_F0(0x0, 0xA)
    ClearChrFlags(0x34, 0x80)
    ClearChrFlags(0x35, 0x80)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x32, 0x80)
    OP_68(0, 1350, 5300, 3000)
    SetCameraDistance(14500, 3000)
    BeginChrThread(0x34, 3, 0, 98)
    Sleep(600)
    BeginChrThread(0x3E, 3, 0, 86)
    BeginChrThread(0x33, 3, 0, 96)
    Sleep(600)
    BeginChrThread(0x32, 3, 0, 94)
    Sleep(300)
    BeginChrThread(0x35, 3, 0, 102)
    Sleep(300)
    BeginChrThread(0x3F, 3, 0, 87)
    Sleep(1300)
    OP_68(-200, 1350, 4800, 1000)
    MoveCamera(25, 25, -10, 1000)
    SetCameraDistance(12000, 1000)
    WaitChrThread(0x34, 3)
    WaitChrThread(0x33, 3)
    WaitChrThread(0x35, 3)
    WaitChrThread(0x32, 3)
    WaitChrThread(0x3E, 3)
    WaitChrThread(0x3F, 3)
    OP_6F(0x79)
    OP_68(-300, 1350, 7310, 1500)
    MoveCamera(23, 20, -10, 1500)
    SetCameraDistance(14500, 1500)
    BeginChrThread(0x23, 2, 0, 126)
    Sleep(800)
    Fade(500)
    EndChrThread(0x40, 0x1)
    EndChrThread(0x41, 0x1)
    ClearChrFlags(0x40, 0x20)
    ClearChrFlags(0x41, 0x20)
    BeginChrThread(0x40, 0, 0, 135)
    BeginChrThread(0x41, 0, 0, 135)
    SetChrPos(0x40, -6000, 0, 12500, 180)
    SetChrPos(0x41, 6000, 0, 12500, 180)
    SetChrPos(0x43, -4000, 0, 16500, 180)
    OP_68(5600, 1350, 1000, 0)
    MoveCamera(87, 29, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(14500, 0)
    MoveCamera(97, 29, 0, 3000)
    SetCameraDistance(13000, 3000)
    SetChrPos(0x38, 2300, 250, -800, 0)
    SetChrFlags(0x33, 0x8)
    SetChrFlags(0x32, 0x8)
    SetChrFlags(0x34, 0x8)
    SetChrFlags(0x35, 0x8)
    OP_0D()
    BeginChrThread(0x3E, 3, 0, 90)
    Sleep(3500)
    EndChrThread(0x72, 0x3)
    EndChrThread(0x79, 0x2)
    EndChrThread(0x79, 0x1)
    EndChrThread(0x3C, 0x1)
    SetChrChipByIndex(0x3C, 0x13)
    SetChrSubChip(0x3C, 0x0)
    OP_63(0x3C, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_F21D():
        TurnDirection(0xFE, 0x3E, 500)
        ExitThread()

    QueueWorkItem(0x3C, 2, lambda_F21D)

    def lambda_F22A():
        OP_96(0xFE, 0x1CE8, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3C, 1, lambda_F22A)
    Sleep(50)
    EndChrThread(0x48, 0x1)
    SetChrChipByIndex(0x48, 0x13)
    SetChrSubChip(0x48, 0x0)
    OP_63(0x48, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_F265():
        TurnDirection(0xFE, 0x3E, 500)
        ExitThread()

    QueueWorkItem(0x48, 2, lambda_F265)

    def lambda_F272():
        OP_96(0xFE, 0x17D4, 0x32, 0xFFFFF95C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x48, 1, lambda_F272)
    Sleep(50)
    EndChrThread(0x38, 0x1)
    EndChrThread(0x79, 0x0)
    SetChrChipByIndex(0x38, 0xF)
    SetChrSubChip(0x38, 0x0)
    OP_63(0x38, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_F2B1():
        TurnDirection(0xFE, 0x3E, 500)
        ExitThread()

    QueueWorkItem(0x38, 2, lambda_F2B1)
    Sleep(50)
    OP_63(0x3A, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_F2D3():
        TurnDirection(0xFE, 0x3E, 500)
        ExitThread()

    QueueWorkItem(0x3A, 2, lambda_F2D3)
    Sleep(50)

    ChrTalk(
        0x3C,
        "Ooooo! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x38,
        "Hell yeah! Is it?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x3E, 3)
    BeginChrThread(0x79, 0, 0, 129)
    BeginChrThread(0x79, 2, 0, 131)
    OP_68(5600, 1150, 1000, 1500)
    MoveCamera(122, 29, 0, 1500)
    SetCameraDistance(15000, 1500)
    Sleep(500)
    ClearChrFlags(0x77, 0x80)
    SetChrPos(0x77, -2000, 1000, -3000, 0)
    BeginChrThread(0x77, 3, 0, 110)
    Sound(926, 2, 80, 0)
    Sleep(800)
    OP_82(0xC8, 0xC8, 0xBB8, 0x12C)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)
    Sound(501, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0x3E, 0x5, 0, 1500, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x3E, 0x5, 0, 1500, 1000, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    EndChrThread(0x3E, 0x0)
    SetChrChipByIndex(0x3E, 0xB)
    SetChrSubChip(0x3E, 0x0)
    OP_52(0x3E, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x3E, 0x20)

    def lambda_F41A():
        OP_A6(0xFE, 0x0, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_F41A)

    def lambda_F433():
        OP_9B(0x1, 0xFE, 0xB4, 0x384, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3E, 1, lambda_F433)
    StopSound(926, 2000, 70)
    SetChrFlags(0x28, 0x800)
    ClearChrFlags(0x28, 0x80)
    BeginChrThread(0x28, 3, 0, 106)
    OP_68(6150, 2350, 3200, 2000)
    MoveCamera(155, 30, 5, 2000)
    SetCameraDistance(10000, 2000)
    WaitChrThread(0x28, 3)
    OP_64(0x3C)
    OP_64(0x48)
    OP_64(0x38)
    OP_64(0x3A)
    WaitChrThread(0x3E, 3)
    SetChrChip(0x1, 0x28, 0x0, 0x0)
    SetChrChipByIndex(0x28, 0x16)
    SetChrSubChip(0x28, 0x0)
    TurnDirection(0x28, 0x2F, 500)
    ClearChrFlags(0x28, 0x800)
    ClearChrFlags(0x2F, 0x80)
    LoadEffect(0x6, "battle\\cr004101.eff")
    LoadEffect(0x7, "battle\\ms00101.eff")

    ChrTalk(
        0x28,
        "#11507F#5PLet me leave it to you next time ~.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        "#03404F─ ─ Yes.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_68(-5600, 1150, 2000, 0)
    MoveCamera(105, 23, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(14500, 0)
    SetChrChipByIndex(0x3C, 0x14)
    SetChrSubChip(0x3C, 0x0)
    SetChrPos(0x3C, 7400, 0, -500, 0)
    SetChrChipByIndex(0x48, 0x14)
    SetChrSubChip(0x48, 0x0)
    SetChrPos(0x48, 6100, 50, -700, 0)
    SetChrChipByIndex(0x38, 0x10)
    SetChrSubChip(0x38, 0x0)
    SetChrPos(0x38, 2300, 250, -800, 0)
    SetChrPos(0x3A, 4400, 0, -2200, 0)
    BeginChrThread(0x3A, 3, 0, 117)
    BeginChrThread(0x3F, 3, 0, 91)
    Sleep(1000)
    OP_68(-8500, 1350, 4400, 2000)
    MoveCamera(135, 15, -5, 2000)
    SetCameraDistance(11000, 2000)
    ClearChrFlags(0x78, 0x80)
    SetChrPos(0x78, 1000, 3000, -4000, 0)
    BeginChrThread(0x78, 3, 0, 114)
    Sound(926, 2, 80, 0)
    Sleep(1000)
    OP_82(0xC8, 0xC8, 0xBB8, 0x12C)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)
    Sound(501, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0x3F, 0x5, 0, 1500, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x3F, 0x5, 0, 1500, 1000, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    EndChrThread(0x3F, 0x0)
    StopSound(926, 1000, 70)
    SetChrChipByIndex(0x3F, 0xB)
    SetChrSubChip(0x3F, 0x0)
    OP_52(0x3F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x3F, 0x20)

    def lambda_F6BF():
        OP_A6(0xFE, 0x0, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3F, 2, lambda_F6BF)

    def lambda_F6D8():
        OP_9B(0x1, 0xFE, 0xB4, 0x384, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_F6D8)
    BeginChrThread(0x2F, 3, 0, 104)
    WaitChrThread(0x2F, 3)
    EndChrThread(0x4A, 0x1)
    SetChrChipByIndex(0x4A, 0x13)
    SetChrSubChip(0x4A, 0x0)
    OP_93(0x4A, 0x0, 0x1F4)

    ChrTalk(
        0x3B,
        "That's amazing …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "#5P#N#01005FAs expected it is Yasutoshi … …\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x3F, 3)
    Fade(500)
    OP_68(-6950, 1350, 6300, 0)
    MoveCamera(350, 25, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(12500, 0)
    SetCameraDistance(8750, 2000)
    SetChrPos(0x2F, -7400, 250, 5800, 0)
    SetChrPos(0x34, -3500, 250, 9200, 225)
    ClearChrFlags(0x34, 0x8)
    SetChrPos(0x77, -7900, 1000, -2200, 0)
    OP_A7(0x77, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x78, 1100, 1000, 5800, 0)
    OP_A7(0x78, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x43, -1500, 250, 10500, 225)
    BeginChrThread(0x43, 2, 0, 83)
    OP_93(0x4A, 0x2D, 0x1F4)
    SetChrChipByIndex(0x4A, 0x14)
    SetChrSubChip(0x4A, 0x0)
    BeginChrThread(0x4A, 1, 0, 123)
    Sound(926, 2, 80, 0)
    BeginChrThread(0x34, 3, 0, 101)
    BeginChrThread(0x77, 3, 0, 111)
    BeginChrThread(0x78, 3, 0, 115)
    WaitChrThread(0x77, 3)
    WaitChrThread(0x78, 3)
    StopSound(926, 300, 70)
    Sound(308, 0, 100, 0)
    Fade(250)
    SetChrChipByIndex(0x2F, 0x19)
    SetChrSubChip(0x2F, 0x0)
    OP_0D()
    WaitChrThread(0x34, 3)
    OP_6F(0x79)

    ChrTalk(
        0x34,
        (
            "#11PMr. Kirika!\x01",
            "I'll help you!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2F, 0x34, 500)
    BeginChrThread(0x3E, 3, 0, 92)

    ChrTalk(
        0x2F,
        (
            "#6P#03402FYes, the essence of Towo,\x01",
            "Let me show you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x34,
        "#11PYes!\x02",
    )

    CloseMessageWindow()

    def lambda_F8CF():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2F, 2, lambda_F8CF)
    OP_93(0x34, 0x2D, 0x1F4)
    WaitChrThread(0x3E, 3)
    WaitChrThread(0x3F, 3)
    OP_68(-6950, 2150, 6300, 5500)
    MoveCamera(5, 25, -15, 5500)
    SetCameraDistance(13000, 5500)
    BeginChrThread(0x2F, 3, 0, 105)
    BeginChrThread(0x34, 3, 0, 99)
    OP_6F(0x79)
    StopSound(926, 1000, 40)
    Fade(500)
    OP_68(7000, 1350, 5200, 0)
    MoveCamera(40, 20, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(13000, 0)
    OP_68(9400, 1350, 4200, 1500)
    MoveCamera(30, 25, 0, 1500)
    SetCameraDistance(10000, 1500)
    SetChrPos(0x28, 9400, 0, 4200, 315)
    SetChrPos(0x33, 6500, 250, 9400, 0)
    SetChrPos(0x32, 4700, 250, 5800, 0)
    SetChrPos(0x35, 3700, 100, 6900, 0)
    SetChrChipByIndex(0x35, 0x8)
    SetChrSubChip(0x35, 0x1)
    ClearChrFlags(0x33, 0x8)
    ClearChrFlags(0x32, 0x8)
    ClearChrFlags(0x35, 0x8)
    OP_A7(0x43, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    BeginChrThread(0x72, 3, 0, 82)
    BeginChrThread(0x42, 2, 0, 83)
    BeginChrThread(0x41, 3, 0, 88)
    EndChrThread(0x2F, 0xFF)
    EndChrThread(0x34, 0xFF)
    EndChrThread(0x77, 0xFF)
    EndChrThread(0x78, 0xFF)
    OP_0D()
    LoadEffect(0x6, "battle/mgaria0.eff")
    LoadEffect(0x7, "battle/mgaria1.eff")
    LoadEffect(0x8, "battle/mg063_00.eff")
    LoadEffect(0xA, "battle/mg063_01.eff")
    BeginChrThread(0x3F, 3, 0, 93)
    BeginChrThread(0x79, 0, 0, 132)
    BeginChrThread(0x32, 3, 0, 95)
    BeginChrThread(0x33, 3, 0, 97)
    OP_6F(0x79)

    ChrTalk(
        0x28,
        (
            "#11P#11509FWhew.\x01",
            "It is conspicuous.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x28, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x28,
        (
            "#11P#11502FWell, this is a bit,\x01",
            "Would you let me make it easy?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x33, 3)
    WaitChrThread(0x3F, 3)
    WaitChrThread(0x41, 3)
    BeginChrThread(0x28, 3, 0, 109)
    WaitChrThread(0x28, 3)
    EndChrThread(0x79, 0x0)
    Fade(500)
    OP_68(-4400, 1150, -2700, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(12500, 0)
    SetChrChipByIndex(0x2F, 0x19)
    SetChrSubChip(0x2F, 0x0)
    SetChrPos(0x2F, -6400, 250, 5800, 270)
    ClearChrFlags(0x34, 0x20)
    ClearChrFlags(0x34, 0x10)
    ClearChrFlags(0x34, 0x2)
    SetChrChipByIndex(0x34, 0x2)
    SetChrSubChip(0x34, 0x0)
    SetChrPos(0x34, -4400, 250, 7800, 0)
    ClearScenarioFlags(0x1, 0)
    BeginChrThread(0x35, 3, 0, 103)
    SetChrChipByIndex(0x28, 0x16)
    SetChrSubChip(0x28, 0x1)
    EndChrThread(0x23, 0x1)
    EndChrThread(0x79, 0x2)
    SetChrSubChip(0x23, 0x0)
    SetChrPos(0x23, -4400, 0, -2700, 0)
    SetChrChipByIndex(0x3F, 0x9)
    SetChrSubChip(0x3F, 0x0)
    OP_52(0x3F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x3F, 0, 0, 8)
    SetChrChipByIndex(0x41, 0x9)
    SetChrSubChip(0x41, 0x0)
    OP_52(0x41, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x41, 0, 0, 8)
    SetChrChipByIndex(0x42, 0x9)
    SetChrSubChip(0x42, 0x0)
    OP_52(0x42, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x42, 0, 0, 8)
    SetChrChipByIndex(0x3E, 0x9)
    SetChrSubChip(0x3E, 0x0)
    OP_52(0x3E, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x3E, 0, 0, 8)
    SetChrPos(0x3E, -11500, 0, 8300, 90)
    SetCameraDistance(12000, 1000)
    OP_6F(0x79)
    LoadEffect(0x8, "battle/mg043_00.eff")
    LoadEffect(0xA, "event\\eva03_01.eff")

    ChrTalk(
        0x23,
        "#01003F#11PIt's about time ……\x02",
    )

    CloseMessageWindow()
    OP_93(0x23, 0x10E, 0x1F4)
    Fade(250)
    SetChrFlags(0x23, 0x20)
    SetChrFlags(0x23, 0x10)
    SetChrFlags(0x23, 0x2)
    SetChrChipByIndex(0x23, 0x15)
    SetChrSubChip(0x23, 0x2)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x23, 0x3)
    Sound(804, 0, 100, 0)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x23,
        (
            "#01007F#4S#11P─ ─ Special Affairs Support Division, rushing!\x02\x03",
            "\"Road\" opened up!\x01",
            "I will leave it to you afterwards!\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x3D, -4400, 0, -2400, 0)
    ClearChrFlags(0x3D, 0x80)
    SetChrFlags(0x3D, 0x8)
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x3D,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4Sroger that!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, -4150, -40000, 0)
    MoveCamera(139, 31, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(19500, 0)
    OP_F0(0x0, 0x1)
    OP_68(0, 1150, -20000, 3300)
    MoveCamera(149, 31, 0, 3300)
    SetCameraDistance(12500, 3300)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0x0)
    ClearMapObjFlags(0x14, 0x4)
    BeginChrThread(0x73, 3, 0, 120)
    BeginChrThread(0x79, 1, 0, 134)
    SetChrChipByIndex(0x23, 0xD)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x20)
    ClearChrFlags(0x23, 0x10)
    ClearChrFlags(0x23, 0x2)
    OP_93(0x23, 0x0, 0x0)
    OP_6F(0x79)
    PlayEffect(0xA, 0x4, 0x73, 0x1, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0xA, 0x5, 0x73, 0x1, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0xA, 0x6, 0x73, 0x1, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_68(0, 650, 12000, 4000)
    MoveCamera(153, 19, -13, 4000)
    SetCameraDistance(14500, 4000)
    SetScenarioFlags(0x1, 0)
    OP_6F(0x79)
    Fade(100)
    OP_68(0, 1050, 22000, 0)
    MoveCamera(25, 17, 5, 0)
    OP_6E(750, 0)
    SetCameraDistance(19000, 0)
    OP_F0(0x0, 0xA)
    SetMapObjFlags(0x18, 0x4)
    OP_68(0, 1050, 29000, 2500)
    MoveCamera(25, 17, 13, 2500)
    SetCameraDistance(16000, 2500)
    Sleep(1500)
    StopSound(861, 2000, 30)
    StopSound(863, 2000, 30)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x73, 3)
    StopBGM(0x1770)
    WaitBGM()
    ReplaceBGM(-1, -1)
    OP_24(0x35D)
    OP_24(0x35F)
    OP_24(0x39E)
    SetScenarioFlags(0x23, 4)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_70_E5F9 end

    def Function_71_FF58(): pass

    label("Function_71_FF58")


    def lambda_FF5D():
        OP_95(0xFE, 5400, 100, -1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FF5D)

    def lambda_FF77():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FF77)
    WaitChrThread(0xFE, 1)

    def lambda_FF8C():
        OP_95(0xFE, 3100, 250, -1700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FF8C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    SetChrChipByIndex(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0x38, 1, 0, 123)
    BeginChrThread(0x79, 0, 0, 127)
    Return()

    # Function_71_FF58 end

    def Function_72_FFC1(): pass

    label("Function_72_FFC1")


    def lambda_FFC6():
        OP_95(0xFE, 5400, 100, -1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FFC6)

    def lambda_FFE0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FFE0)
    WaitChrThread(0xFE, 1)

    def lambda_FFF5():
        OP_95(0xFE, 6100, 50, -700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FFF5)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0x48, 1, 0, 123)
    Return()

    # Function_72_FFC1 end

    def Function_73_10024(): pass

    label("Function_73_10024")


    def lambda_10029():
        OP_95(0xFE, 5400, 100, -1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10029)

    def lambda_10043():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10043)
    WaitChrThread(0xFE, 1)

    def lambda_10058():
        OP_95(0xFE, 7400, 0, -500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10058)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0x3C, 1, 0, 123)
    Return()

    # Function_73_10024 end

    def Function_74_10087(): pass

    label("Function_74_10087")


    def lambda_1008C():
        OP_95(0xFE, -5400, 100, -1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1008C)

    def lambda_100A6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_100A6)
    WaitChrThread(0xFE, 1)

    def lambda_100BB():
        OP_95(0xFE, -3100, 250, -1700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_100BB)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0x49, 1, 0, 123)
    Return()

    # Function_74_10087 end

    def Function_75_100EA(): pass

    label("Function_75_100EA")


    def lambda_100EF():
        OP_95(0xFE, -5400, 100, -1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_100EF)

    def lambda_10109():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10109)
    WaitChrThread(0xFE, 1)

    def lambda_1011E():
        OP_95(0xFE, -6100, 50, -700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1011E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)

    ChrTalk(
        0x39,
        "#5PBeginning raid\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Return()

    # Function_75_100EA end

    def Function_76_1015D(): pass

    label("Function_76_1015D")


    def lambda_10162():
        OP_95(0xFE, -5400, 100, -1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10162)

    def lambda_1017C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1017C)
    WaitChrThread(0xFE, 1)

    def lambda_10191():
        OP_95(0xFE, -7400, 0, -500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10191)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0x4A, 1, 0, 123)
    BeginChrThread(0x79, 1, 0, 128)
    Return()

    # Function_76_1015D end

    def Function_77_101C6(): pass

    label("Function_77_101C6")


    def lambda_101CB():
        OP_95(0xFE, -5400, 100, -1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_101CB)

    def lambda_101E5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_101E5)
    WaitChrThread(0xFE, 1)

    def lambda_101FA():
        OP_95(0xFE, -6400, 0, -3000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_101FA)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_77_101C6 end

    def Function_78_1021B(): pass

    label("Function_78_1021B")


    def lambda_10220():
        OP_95(0xFE, 5400, 100, -1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10220)

    def lambda_1023A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1023A)
    WaitChrThread(0xFE, 1)

    def lambda_1024F():
        OP_95(0xFE, 4400, 0, -2200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1024F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_AD(0x9)

    ChrTalk(
        0x3A,
        "Keep cover behind the cars!\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_78_1021B end

    def Function_79_1028B(): pass

    label("Function_79_1028B")

    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)

    def lambda_10298():
        OP_95(0xFE, -5400, 100, -1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10298)

    def lambda_102B2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_102B2)
    WaitChrThread(0xFE, 1)

    def lambda_102C7():
        OP_95(0xFE, -2000, 250, -1600, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_102C7)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    SetChrChipByIndex(0xFE, 0xD)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0x23, 1, 0, 124)
    BeginChrThread(0x79, 2, 0, 130)
    Return()

    # Function_79_1028B end

    def Function_80_102FC(): pass

    label("Function_80_102FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_104A2")
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -2600, 100, 6500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -3700, 250, 11100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -5500, 250, 8800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -1300, 100, 8000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -3300, 150, 9000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -6800, 250, 9100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -5500, 250, 6700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Jump("Function_80_102FC")

    label("loc_104A2")

    Return()

    # Function_80_102FC end

    def Function_81_104A3(): pass

    label("Function_81_104A3")

    Sleep(300)

    label("loc_104A6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1064C")
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 2600, 100, 6500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 3700, 250, 11100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 5500, 250, 8800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 1300, 100, 8000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 3300, 150, 9000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 6800, 250, 9100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 5500, 250, 6700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Jump("loc_104A6")

    label("loc_1064C")

    Return()

    # Function_81_104A3 end

    def Function_82_1064D(): pass

    label("Function_82_1064D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_107F3")
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 2600, 250, 9500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 3700, 0, 14100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 5500, 250, 11800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 1300, 250, 11000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 3300, 250, 12000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 6800, 250, 12100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 5500, 250, 9700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Jump("Function_82_1064D")

    label("loc_107F3")

    Return()

    # Function_82_1064D end

    def Function_83_107F4(): pass

    label("Function_83_107F4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1083E")
    PlayEffect(0x5, 0xFF, 0xFE, 0x0, 0, 1600, -500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(900)
    Jump("Function_83_107F4")

    label("loc_1083E")

    Return()

    # Function_83_107F4 end

    def Function_84_1083F(): pass

    label("Function_84_1083F")

    Sleep(6500)
    BeginChrThread(0x3E, 3, 0, 85)
    Sleep(50)
    BeginChrThread(0x43, 3, 0, 85)
    Sleep(500)
    BeginChrThread(0x3F, 3, 0, 85)
    Sleep(50)
    BeginChrThread(0x41, 3, 0, 85)
    Sleep(500)
    BeginChrThread(0x40, 3, 0, 85)
    Sleep(50)
    BeginChrThread(0x42, 3, 0, 85)
    WaitChrThread(0x3E, 3)
    WaitChrThread(0x3F, 3)
    WaitChrThread(0x40, 3)
    WaitChrThread(0x41, 3)
    WaitChrThread(0x42, 3)
    WaitChrThread(0x43, 3)
    Return()

    # Function_84_1083F end

    def Function_85_1088E(): pass

    label("Function_85_1088E")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0xA)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 9)

    def lambda_108B5():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_108B5)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x20)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 8)
    Return()

    # Function_85_1088E end

    def Function_86_108F1(): pass

    label("Function_86_108F1")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0xA)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 9)

    def lambda_10918():
        OP_95(0xFE, -2200, 100, 5300, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10918)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x20)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 8)
    Return()

    # Function_86_108F1 end

    def Function_87_10954(): pass

    label("Function_87_10954")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0xA)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 9)

    def lambda_1097B():
        OP_95(0xFE, 2000, 100, 5800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1097B)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x20)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 8)
    Return()

    # Function_87_10954 end

    def Function_88_109B7(): pass

    label("Function_88_109B7")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(630)
    SetChrSubChip(0xFE, 0x1)
    Sleep(130)

    def lambda_109DD():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_109DD)
    Sleep(1000)
    SetChrSubChip(0xFE, 0x2)
    Sleep(1000)
    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 8)
    Return()

    # Function_88_109B7 end

    def Function_89_10A15(): pass

    label("Function_89_10A15")

    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_10A35():
        OP_A6(0xFE, 0x0, 0x64, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_10A35)
    Sleep(1000)
    Sound(985, 0, 80, 0)
    PlayEffect(0x1, 0xFF, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_10A91():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10A91)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_89_10A15 end

    def Function_90_10AA2(): pass

    label("Function_90_10AA2")

    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xFE, 7300, 250, 4300, 225)
    Sound(985, 0, 100, 0)
    PlayEffect(0x0, 0x1, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_10B0B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10B0B)
    WaitChrThread(0xFE, 2)
    StopEffect(0x1, 0x2)
    Sleep(130)
    SetChrSubChip(0x3E, 0x1)
    Sleep(130)

    def lambda_10B2D():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_10B2D)
    Sleep(1000)
    Sound(951, 0, 100, 0)
    SetChrSubChip(0xFE, 0x2)
    SetChrFlags(0xFE, 0x20)

    def lambda_10B58():
        OP_9B(0x1, 0xFE, 0x0, 0x2BC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10B58)
    Sleep(50)
    Sound(893, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    OP_82(0x0, 0x3E8, 0xBB8, 0x3E8)
    Sound(876, 0, 100, 0)
    Sound(880, 0, 100, 0)
    Sound(196, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 4500, 1700, 1000, 0, 0, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 4500, 1800, 1000, 0, 0, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    OP_52(0x76, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x72, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x76, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x72, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x76, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x72, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_D5(0x76, 0x0, 0x11170, 0x0, 0x0)
    SetMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x16, 0x4)
    WaitChrThread(0xFE, 1)
    CancelBlur(700)
    Sleep(2000)
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 8)
    Return()

    # Function_90_10AA2 end

    def Function_91_10C78(): pass

    label("Function_91_10C78")

    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 8)
    SetChrPos(0xFE, -7300, 250, 4300, 135)
    Sound(985, 0, 100, 0)
    PlayEffect(0x0, 0x2, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_10CE7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10CE7)
    WaitChrThread(0xFE, 2)
    StopEffect(0x2, 0x2)
    Return()

    # Function_91_10C78 end

    def Function_92_10CFB(): pass

    label("Function_92_10CFB")

    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 8)
    SetChrPos(0xFE, -12800, 0, 8300, 135)
    Sound(985, 0, 100, 0)
    PlayEffect(0x0, 0x1, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_10D6A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10D6A)
    WaitChrThread(0xFE, 2)
    StopEffect(0x1, 0x2)
    Return()

    # Function_92_10CFB end

    def Function_93_10D7E(): pass

    label("Function_93_10D7E")

    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 8)
    SetChrPos(0xFE, 8300, 0, 15000, 180)
    Sound(985, 0, 70, 0)
    PlayEffect(0x0, 0x2, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_10DED():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10DED)
    WaitChrThread(0xFE, 2)
    StopEffect(0x2, 0x2)
    Return()

    # Function_93_10D7E end

    def Function_94_10E01(): pass

    label("Function_94_10E01")


    def lambda_10E06():
        OP_95(0xFE, 800, 100, 600, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10E06)
    WaitChrThread(0xFE, 1)

    def lambda_10E24():
        OP_96(0xFE, 0x44C, 0x64, 0xA28, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10E24)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x5)
    Sleep(100)
    SetChrSubChip(0xFE, 0x6)
    Sound(567, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x3, 0, 1100, 1100, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    OP_82(0x64, 0x64, 0xBB8, 0xC8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)

    def lambda_10EAF():
        OP_98(0xFE, 0x0, 0x0, 0xC8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_10EAF)
    Sound(501, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0x3F, 0x0, 0, 2350, 200, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0x3F, 0x0, 0, 2350, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x5)
    Sleep(300)
    SetChrSubChip(0xFE, 0x6)
    Sound(567, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x3, 0, 1100, 1100, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    OP_82(0x64, 0x64, 0xBB8, 0xC8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)

    def lambda_10FAD():
        OP_98(0xFE, 0x0, 0x0, 0xC8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_10FAD)
    Sound(501, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0x3F, 0x0, 300, 2350, 200, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0x3F, 0x0, 300, 2350, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x5)
    Sleep(300)
    SetChrSubChip(0xFE, 0x6)
    Sound(567, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x3, 0, 1100, 1100, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    OP_82(0x64, 0x64, 0xBB8, 0xC8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)

    def lambda_110AB():
        OP_98(0xFE, 0x0, 0x0, 0xC8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_110AB)
    Sound(501, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0x3F, 0x0, -300, 2350, 200, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0x3F, 0x0, -300, 2350, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x5)
    Sleep(300)
    BeginChrThread(0x3F, 3, 0, 89)
    Return()

    # Function_94_10E01 end

    def Function_95_11145(): pass

    label("Function_95_11145")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1119A")
    PlayEffect(0x2, 0xFF, 0xFE, 0x3, 0, 1100, 1100, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x6)
    Sleep(500)
    SetChrSubChip(0xFE, 0x5)
    Sleep(500)
    Jump("Function_95_11145")

    label("loc_1119A")

    Return()

    # Function_95_11145 end

    def Function_96_1119B(): pass

    label("Function_96_1119B")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_111AB():
        OP_95(0xFE, 600, 250, 400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_111AB)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x6)
    Sound(809, 0, 100, 0)

    def lambda_111D3():
        OP_9D(0xFE, 0x6A4, 0x64, 0x1130, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_111D3)
    Sleep(500)
    SetChrSubChip(0xFE, 0x7)
    Sound(538, 0, 100, 0)
    OP_82(0x190, 0x190, 0xBB8, 0x12C)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)
    PlayEffect(0x4, 0xFF, 0xFE, 0x3, 0, 1500, 1300, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    EndChrThread(0x3F, 0x0)
    SetChrChipByIndex(0x3F, 0xB)
    SetChrSubChip(0x3F, 0x0)
    OP_52(0x3F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x3F, 0x20)

    def lambda_11272():
        OP_A6(0xFE, 0x0, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3F, 2, lambda_11272)
    OP_52(0x3F, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_11296():
        OP_9D(0xFE, 0x7D0, 0x64, 0x1E78, 0x12C, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_11296)
    WaitChrThread(0xFE, 1)
    Sleep(2000)
    SetChrSubChip(0xFE, 0x5)
    Return()

    # Function_96_1119B end

    def Function_97_112BA(): pass

    label("Function_97_112BA")

    SetChrSubChip(0xFE, 0x7)
    Sleep(1200)
    SetChrSubChip(0xFE, 0x3)
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0x1964, 0xFA, 0x170C, 0x1F4, 0x3E8)
    SetChrSubChip(0xFE, 0x5)
    Sleep(300)
    OP_96(0xFE, 0x1964, 0xFA, 0x1CE8, 0xFA0, 0x0)
    SetChrSubChip(0xFE, 0x5)
    Return()

    # Function_97_112BA end

    def Function_98_11302(): pass

    label("Function_98_11302")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x3)
    SetChrSubChip(0xFE, 0x0)

    def lambda_1131A():
        OP_95(0xFE, -600, 250, 400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1131A)
    WaitChrThread(0xFE, 1)

    def lambda_11338():
        OP_95(0xFE, -1300, 100, 4400, 8000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11338)
    Sleep(100)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x4)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sound(533, 0, 60, 0)
    Sleep(100)
    OP_82(0xC8, 0xC8, 0xBB8, 0xC8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)
    Sound(815, 0, 100, 0)
    Sound(635, 0, 100, 0)
    PlayEffect(0x6, 0xFF, 0xFE, 0x3, 0, 1100, 0, 0, 0, 0, 1400, 1400, 1400, 0xFF, 0, 0, 0, 0)
    EndChrThread(0x3E, 0x0)
    SetChrChipByIndex(0x3E, 0xB)
    SetChrSubChip(0x3E, 0x0)
    OP_52(0x3E, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x3E, 0x20)

    def lambda_113FA():
        OP_A6(0xFE, 0x0, 0x64, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_113FA)

    def lambda_11413():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3E, 1, lambda_11413)
    WaitChrThread(0xFE, 1)
    Sleep(300)
    SetChrSubChip(0xFE, 0x4)
    Sleep(90)
    SetChrSubChip(0xFE, 0x1)
    Sleep(90)
    SetChrSubChip(0xFE, 0x2)
    Sleep(90)
    SetChrSubChip(0xFE, 0x3)

    def lambda_1144D():
        OP_95(0xFE, -1400, 100, 5400, 8000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1144D)
    Sound(533, 0, 60, 0)
    Sleep(100)
    OP_82(0xC8, 0xC8, 0xBB8, 0xC8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)
    Sound(815, 0, 100, 0)
    Sound(635, 0, 100, 0)
    PlayEffect(0x6, 0xFF, 0xFE, 0x3, 0, 1100, 0, 0, 0, 0, 1400, 1400, 1400, 0xFF, 0, 0, 0, 0)

    def lambda_114D5():
        OP_A6(0xFE, 0x0, 0x64, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_114D5)

    def lambda_114EE():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3E, 1, lambda_114EE)
    WaitChrThread(0xFE, 1)
    Sleep(200)
    SetChrSubChip(0xFE, 0x4)
    Sleep(90)
    SetChrSubChip(0xFE, 0x1)
    Sleep(90)
    SetChrSubChip(0xFE, 0x2)
    Sleep(90)
    SetChrSubChip(0xFE, 0x3)

    def lambda_11528():
        OP_95(0xFE, -1500, 100, 6400, 8000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11528)
    Sound(533, 0, 60, 0)
    Sleep(100)
    OP_82(0xC8, 0xC8, 0xBB8, 0xC8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)
    Sound(815, 0, 100, 0)
    Sound(635, 0, 100, 0)
    PlayEffect(0x6, 0xFF, 0xFE, 0x3, 0, 1100, 0, 0, 0, 0, 1400, 1400, 1400, 0xFF, 0, 0, 0, 0)

    def lambda_115B0():
        OP_A6(0xFE, 0x0, 0x64, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_115B0)

    def lambda_115C9():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3E, 1, lambda_115C9)
    WaitChrThread(0xFE, 1)
    Sleep(2000)
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x2)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_98_11302 end

    def Function_99_115FA(): pass

    label("Function_99_115FA")

    SetChrChipByIndex(0xFE, 0x3)
    SetChrSubChip(0xFE, 0x0)

    def lambda_11607():
        OP_95(0xFE, -3900, 250, 8800, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11607)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x5)
    SetChrSubChip(0xFE, 0x1)
    Sleep(300)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x10)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x20)
    Sound(844, 0, 100, 0)

    def lambda_1164A():
        OP_9C(0xFE, 0x0, 0x2BC, 0x0, 0x2EE, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1164A)
    SetChrSubChip(0xFE, 0x14)
    Sleep(50)
    BeginChrThread(0xFE, 2, 0, 100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x10)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x20)
    Return()

    # Function_99_115FA end

    def Function_100_11688(): pass

    label("Function_100_11688")

    EndChrThread(0x43, 0x0)
    EndChrThread(0x43, 0x2)
    SetChrChipByIndex(0x43, 0xB)
    SetChrSubChip(0x43, 0x0)
    OP_52(0x43, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_116A3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11795")
    Sound(815, 0, 100, 0)
    Sound(635, 0, 50, 0)
    OP_82(0xC8, 0xC8, 0xBB8, 0xC8)
    PlayEffect(0x4, 0xFF, 0x43, 0x1, 0, 1200, -200, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    def lambda_11707():
        OP_A6(0xFE, 0x0, 0x64, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x43, 2, lambda_11707)
    Sound(253, 0, 40, 0)
    PlayEffect(0x6, 0xFF, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x1B)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1A)
    Sleep(50)
    SetChrSubChip(0xFE, 0x19)
    Sleep(50)
    SetChrSubChip(0xFE, 0x18)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1F)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1E)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1D)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1C)
    Sleep(50)
    Jump("loc_116A3")

    label("loc_11795")

    Return()

    # Function_100_11688 end

    def Function_101_11796(): pass

    label("Function_101_11796")

    SetChrChipByIndex(0x34, 0x3)
    SetChrSubChip(0x34, 0x0)

    def lambda_117A3():
        OP_95(0xFE, -6500, 250, 6800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_117A3)
    WaitChrThread(0x34, 1)
    SetChrChipByIndex(0x34, 0x2)
    SetChrSubChip(0x34, 0x0)
    Return()

    # Function_101_11796 end

    def Function_102_117C5(): pass

    label("Function_102_117C5")

    SetChrChipByIndex(0xFE, 0x7)
    SetChrSubChip(0xFE, 0x0)

    def lambda_117D2():
        OP_95(0xFE, -800, 100, 2600, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_117D2)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x8)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(500)
    SetChrSubChip(0xFE, 0x2)
    Sound(253, 0, 100, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0x5, -200, 1100, 0, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Sound(256, 0, 100, 0)
    OP_82(0xC8, 0xC8, 0xBB8, 0xC8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)
    BeginChrThread(0x3E, 3, 0, 89)
    Sleep(1500)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_102_117C5 end

    def Function_103_1187E(): pass

    label("Function_103_1187E")

    Sleep(1000)
    SetChrChipByIndex(0xFE, 0x8)
    SetChrSubChip(0xFE, 0x1)
    PlayEffect(0x6, 0x3, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_AD(0x8)
    StopEffect(0x3, 0x2)
    PlayEffect(0x7, 0xFF, 0xFE, 0x5, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    EndChrThread(0x42, 0x2)
    PlayEffect(0x8, 0xFF, 0x42, 0x1, 0, 0, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    BeginChrThread(0x42, 3, 0, 89)
    Sleep(4000)
    SetChrChipByIndex(0xFE, 0x8)
    SetChrSubChip(0xFE, 0x1)
    PlayEffect(0x6, 0x3, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_103_1187E end

    def Function_104_1198B(): pass

    label("Function_104_1198B")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x1A)
    SetChrSubChip(0xFE, 0x0)

    def lambda_119AB():
        OP_95(0xFE, -8500, 150, 3500, 9000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_119AB)
    WaitChrThread(0xFE, 1)
    Sound(621, 0, 100, 0)
    Sound(534, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    CancelBlur(500)
    SetCameraDistance(8000, 500)
    MoveCamera(145, 20, -10, 500)
    SetChrChipByIndex(0xFE, 0x1D)
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0x2F,
        "#03401F#9AHappy …!\x02",
    )

    Sleep(700)

    def lambda_11A1E():
        OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11A1E)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x14)
    OP_82(0x1F4, 0x1F4, 0xBB8, 0x1F4)
    Sound(833, 0, 80, 0)
    Sound(635, 0, 100, 0)
    OP_68(-8500, 1350, 4900, 500)
    MoveCamera(135, 15, -5, 500)
    SetCameraDistance(11500, 500)
    PlayEffect(0x7, 0xFF, 0xFE, 0x5, 0, 1100, -1300, 180, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x3F, 3, 0, 89)

    def lambda_11AC5():
        OP_9D(0xFE, 0xFFFFDF94, 0xFA, 0x2454, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_11AC5)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    CancelBlur(700)
    Sleep(500)
    Sound(880, 0, 100, 0)
    Sleep(1500)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_104_1198B end

    def Function_105_11B02(): pass

    label("Function_105_11B02")

    Sleep(500)
    SetChrChipByIndex(0xFE, 0x1B)
    SetChrSubChip(0xFE, 0x0)
    Sleep(90)
    SetChrSubChip(0xFE, 0x1)
    Sound(250, 0, 100, 0)
    Sleep(250)
    SetChrSubChip(0xFE, 0x2)
    Sound(926, 2, 50, 0)
    BeginChrThread(0x77, 3, 0, 112)
    BeginChrThread(0x78, 3, 0, 116)
    Sleep(90)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_105_11B02 end

    def Function_106_11B3B(): pass

    label("Function_106_11B3B")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)

    def lambda_11B5B():
        OP_95(0xFE, 2500, 100, -2600, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11B5B)
    WaitChrThread(0xFE, 1)

    ChrTalk(
        0x28,
        "#12P#11507F#9ASorry!\x02",
    )

    TurnDirection(0xFE, 0x3E, 0)
    SetChrFlags(0xFE, 0x4)
    SetChrSubChip(0xFE, 0x2)
    Sound(844, 0, 100, 0)

    def lambda_11BAE():
        OP_9D(0xFE, 0x1194, 0x5DC, 0x258, 0x76C, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11BAE)
    WaitChrThread(0xFE, 1)
    Sound(326, 0, 100, 0)
    BlurSwitch(0x0, 0x55FFFFFF, 0x0, 0x1, 0x0)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Sound(844, 0, 100, 0)

    def lambda_11BEF():
        OP_9D(0xFE, 0x1A90, 0xFA, 0xABE, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11BEF)
    Sleep(400)
    Sound(540, 0, 100, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    OP_68(6800, 850, 2750, 300)
    MoveCamera(150, 25, 5, 300)
    SetCameraDistance(10000, 300)
    OP_82(0x12C, 0x12C, 0xBB8, 0x12C)
    CancelBlur(0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)
    Sound(246, 0, 100, 0)
    Sound(288, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0x3E, 0x5, 0, 1900, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x3E, 0x5, 0, 1900, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)

    def lambda_11CE6():
        OP_A6(0xFE, 0x0, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_11CE6)

    def lambda_11CFF():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x3E, 1, lambda_11CFF)
    WaitChrThread(0xFE, 1)
    Sound(326, 0, 100, 0)
    SetChrSubChip(0xFE, 0x3)
    ClearChrFlags(0xFE, 0x4)
    Sleep(1000)
    BeginChrThread(0xFE, 0, 0, 108)
    TurnDirection(0xFE, 0x3E, 1000)
    OP_6F(0x79)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9C(0xFE, 0xC8, 0x0, 0x0, 0xFA, 0x1388)
    Sleep(50)
    OP_9C(0xFE, 0xFFFFFF38, 0x0, 0x0, 0xFA, 0x1388)
    Sleep(200)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0x0)

    def lambda_11D8F():
        OP_A6(0xFE, 0x0, 0x64, 0x9C4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_11D8F)
    OP_82(0x12C, 0x12C, 0xBB8, 0x9C4)
    OP_68(7300, 850, 4300, 300)
    MoveCamera(145, 30, 5, 300)
    SetChrFlags(0xFE, 0x20)
    SetChrChip(0x0, 0xFE, 0x5, 0x1F4)
    BeginChrThread(0xFE, 0, 0, 107)
    OP_9A(0xFE, 0x3E, 0x0, 0x4E20, 0x0)
    Sound(287, 0, 100, 0)
    Sound(538, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0x3E, 0x5, 0, 1900, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x3E, 0x5, 0, 1900, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(329, 0, 100, 0)
    SetChrPos(0xFE, 5170, 250, 2670, 45)
    BeginChrThread(0xFE, 0, 0, 107)
    OP_9B(0x1, 0xFE, 0x0, 0x1388, 0x4E20, 0x0)
    Sound(538, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0x3E, 0x5, 0, 1900, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x3E, 0x5, 0, 1900, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(329, 0, 100, 0)
    SetChrPos(0xFE, 9280, 0, 1780, 315)
    BeginChrThread(0xFE, 0, 0, 107)
    OP_9B(0x1, 0xFE, 0x0, 0x1388, 0x4E20, 0x0)
    Sound(538, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0x3E, 0x5, 0, 1900, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x3E, 0x5, 0, 1900, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(329, 0, 100, 0)
    SetChrPos(0xFE, 4640, 250, 3970, 90)
    BeginChrThread(0xFE, 0, 0, 107)
    OP_9B(0x1, 0xFE, 0x0, 0x1388, 0x4E20, 0x0)
    Sound(538, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0x3E, 0x5, 0, 1900, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x3E, 0x5, 0, 1900, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(329, 0, 100, 0)
    OP_68(8100, 850, 5270, 300)
    MoveCamera(135, 25, 10, 300)
    SetCameraDistance(11000, 300)
    SetChrPos(0xFE, 6730, 850, 1510, 0)
    BeginChrThread(0xFE, 0, 0, 107)
    OP_96(0xFE, 0x2134, 0xFA, 0x16A8, 0x4E20, 0x0)
    Sound(264, 0, 100, 0)
    Sound(681, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0x3E, 0x5, 0, 1900, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x3E, 0x5, 0, 1900, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    WaitChrThread(0xFE, 0)
    CancelBlur(500)
    ClearChrFlags(0xFE, 0x20)
    Sleep(500)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    OP_68(7300, 1350, 3300, 2000)
    MoveCamera(155, 25, 5, 2000)
    SetCameraDistance(13500, 2000)
    BeginChrThread(0x3E, 3, 0, 89)
    Return()

    # Function_106_11B3B end

    def Function_107_1217B(): pass

    label("Function_107_1217B")

    SetChrChipByIndex(0xFE, 0x18)
    OP_A0(0xFE, 1500, 0x0, 0x3)
    Return()

    # Function_107_1217B end

    def Function_108_12187(): pass

    label("Function_108_12187")

    SetChrChipByIndex(0xFE, 0x16)

    label("loc_1218B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_121A9")
    OP_A0(0xFE, 1500, 0x0, 0x4)
    OP_A0(0xFE, 1500, 0x3, 0x1)
    Jump("loc_1218B")

    label("loc_121A9")

    Return()

    # Function_108_12187 end

    def Function_109_121AA(): pass

    label("Function_109_121AA")

    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    OP_68(9400, 850, 4200, 2000)
    MoveCamera(30, 30, 5, 2000)
    SetCameraDistance(9500, 2000)
    Sound(357, 0, 70, 0)
    PlayEffect(0x6, 0x0, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    StopEffect(0x0, 0x2)
    Sound(280, 0, 80, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0x5, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x4)
    Sleep(300)
    OP_68(5600, 1550, 14500, 1500)
    MoveCamera(40, 27, 0, 1500)
    SetCameraDistance(14500, 1500)
    OP_6F(0x79)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0x0)
    PlayEffect(0x8, 0xFF, 0xFF, 0x0, 5600, 250, 14500, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0xA, 0xFF, 0xFF, 0x0, 5600, 250, 14500, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    MoveCamera(50, 27, 0, 3500)
    SetCameraDistance(16500, 3500)
    EndChrThread(0x3F, 0x0)
    EndChrThread(0x3F, 0x2)
    SetChrChipByIndex(0x3F, 0xB)
    SetChrSubChip(0x3F, 0x0)
    OP_52(0x3F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_12356():
        OP_A6(0xFE, 0x0, 0x64, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3F, 2, lambda_12356)
    Sleep(50)
    EndChrThread(0x41, 0x0)
    EndChrThread(0x41, 0x2)
    SetChrChipByIndex(0x41, 0xB)
    SetChrSubChip(0x41, 0x0)
    OP_52(0x41, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1238D():
        OP_A6(0xFE, 0x0, 0x64, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x41, 2, lambda_1238D)
    Sleep(50)
    EndChrThread(0x42, 0x0)
    EndChrThread(0x42, 0x2)
    SetChrChipByIndex(0x42, 0xB)
    SetChrSubChip(0x42, 0x0)
    OP_52(0x42, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_123C4():
        OP_A6(0xFE, 0x0, 0x64, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x42, 2, lambda_123C4)
    Sleep(2500)
    CancelBlur(0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    Sleep(1000)
    Return()

    # Function_109_121AA end

    def Function_110_123F5(): pass

    label("Function_110_123F5")

    PlayEffect(0x8, 0xFF, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1200, 1000, 1200, 0xFF, 0, 0, 0, 0)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)

    def lambda_12439():
        OP_9E(0xFE, 0xFA0, 0xFFFFF448, 0x36EE8, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12439)

    label("loc_1244F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_12477")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(10)
    Jump("loc_1244F")

    label("loc_12477")

    WaitChrThread(0xFE, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Return()

    # Function_110_123F5 end

    def Function_111_1248F(): pass

    label("Function_111_1248F")

    SetChrChip(0x0, 0x77, 0x32, 0x12C)

    def lambda_1249C():
        OP_9E(0xFE, 0xFFFFE124, 0x708, 0x2BF20, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x77, 1, lambda_1249C)

    label("loc_124B2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_124DA")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(10)
    Jump("loc_124B2")

    label("loc_124DA")

    WaitChrThread(0x77, 1)
    SetChrChip(0x1, 0x77, 0x0, 0x0)
    OP_A7(0x77, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Return()

    # Function_111_1248F end

    def Function_112_124F2(): pass

    label("Function_112_124F2")

    SetChrPos(0xFE, -7400, 250, 5400, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    BeginChrThread(0xFE, 2, 0, 113)

    def lambda_12521():
        OP_9E(0xFE, 0xFFFFD9B8, 0x1C84, 0x2BF20, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12521)
    WaitChrThread(0xFE, 1)
    OP_82(0xC8, 0xC8, 0xBB8, 0xC8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)
    Sound(501, 0, 40, 0)
    Sound(308, 0, 100, 0)
    EndChrThread(0x3E, 0x0)
    SetChrChipByIndex(0x3E, 0xB)
    SetChrSubChip(0x3E, 0x0)
    OP_52(0x3E, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x4, 0xFF, 0x3E, 0x1, 0, 1200, -200, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    def lambda_125BC():
        OP_A6(0xFE, 0x0, 0x64, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_125BC)

    label("loc_125D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1267D")

    def lambda_125E0():
        OP_9E(0xFE, 0xFFFFD3DC, 0x2CEC, 0x57E40, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_125E0)
    WaitChrThread(0xFE, 1)
    OP_82(0xC8, 0xC8, 0xBB8, 0xC8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)
    Sound(501, 0, 40, 0)
    Sound(308, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0x3E, 0x1, 0, 1200, -200, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    def lambda_12664():
        OP_A6(0xFE, 0x0, 0x64, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_12664)
    Jump("loc_125D0")

    label("loc_1267D")

    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Return()

    # Function_112_124F2 end

    def Function_113_12691(): pass

    label("Function_113_12691")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_126DB")
    PlayEffect(0x8, 0xFF, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1200, 1000, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(1900)
    Jump("Function_113_12691")

    label("loc_126DB")

    Return()

    # Function_113_12691 end

    def Function_114_126DC(): pass

    label("Function_114_126DC")

    PlayEffect(0x8, 0xFF, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1200, 1000, 1200, 0xFF, 0, 0, 0, 0)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)

    def lambda_12720():
        OP_9E(0xFE, 0xFFFFE4A8, 0xFFFFF060, 0xFFFD40E0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12720)

    label("loc_12736")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1275E")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(10)
    Jump("loc_12736")

    label("loc_1275E")

    WaitChrThread(0xFE, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Return()

    # Function_114_126DC end

    def Function_115_12776(): pass

    label("Function_115_12776")

    Sleep(150)
    SetChrChip(0x0, 0x78, 0x32, 0x12C)

    def lambda_12786():
        OP_9E(0xFE, 0xFFFFF4AC, 0x16A8, 0x2BF20, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x78, 1, lambda_12786)

    label("loc_1279C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_127C4")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(10)
    Jump("loc_1279C")

    label("loc_127C4")

    WaitChrThread(0x78, 1)
    SetChrChip(0x1, 0x78, 0x0, 0x0)
    OP_A7(0x78, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Return()

    # Function_115_12776 end

    def Function_116_127DC(): pass

    label("Function_116_127DC")

    SetChrPos(0xFE, -7400, 250, 6200, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    BeginChrThread(0xFE, 2, 0, 113)

    def lambda_1280B():
        OP_9E(0xFE, 0xFFFFD9B8, 0x1C84, 0xFFFD5468, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1280B)
    WaitChrThread(0xFE, 1)

    label("loc_12825")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12854")

    def lambda_12835():
        OP_9E(0xFE, 0xFFFFCE00, 0x17D4, 0xFFFA81C0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12835)
    WaitChrThread(0xFE, 1)
    Jump("loc_12825")

    label("loc_12854")

    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Return()

    # Function_116_127DC end

    def Function_117_12868(): pass

    label("Function_117_12868")

    BeginChrThread(0x3C, 1, 0, 123)
    Sleep(300)
    BeginChrThread(0x38, 1, 0, 123)
    Sleep(300)
    BeginChrThread(0x48, 1, 0, 123)
    BeginChrThread(0x72, 3, 0, 81)
    Return()

    # Function_117_12868 end

    def Function_118_12887(): pass

    label("Function_118_12887")

    OP_96(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x2710, 0x0)

    def lambda_128A0():
        OP_D5(0xFE, 0x0, 0x0, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_128A0)
    OP_96(0xFE, 0x0, 0x0, 0xFFFFE4A8, 0x2710, 0x0)

    def lambda_128CD():
        OP_D5(0xFE, 0x0, 0xFFFEEE90, 0x0, 0x4B0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_128CD)
    OP_9E(0xFE, 0xFFFFDCD8, 0xFFFFE4A8, 0xFFFF15A0, 0x1F40, 0x0)
    Sound(487, 0, 100, 0)
    OP_71(0x12, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x12)
    Sound(462, 0, 100, 0)
    OP_71(0x12, 0x12D, 0x14A, 0x0, 0x0)
    OP_79(0x12)
    BeginChrThread(0x4A, 3, 0, 76)
    Sleep(400)
    BeginChrThread(0x39, 3, 0, 75)
    Sleep(400)
    BeginChrThread(0x23, 3, 0, 79)
    Sleep(400)
    BeginChrThread(0x49, 3, 0, 74)
    Sleep(400)
    BeginChrThread(0x3B, 3, 0, 77)
    Sleep(400)
    Sound(461, 0, 100, 0)
    OP_71(0x12, 0x14B, 0x168, 0x0, 0x0)
    OP_79(0x12)
    Sound(485, 0, 100, 0)
    Return()

    # Function_118_12887 end

    def Function_119_12969(): pass

    label("Function_119_12969")

    OP_96(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x2710, 0x0)

    def lambda_12982():
        OP_D5(0xFE, 0x0, 0x0, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12982)
    OP_96(0xFE, 0x0, 0x0, 0xFFFFE4A8, 0x2710, 0x0)

    def lambda_129AF():
        OP_D5(0xFE, 0x0, 0x11170, 0x0, 0x4B0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_129AF)
    OP_9E(0xFE, 0x2328, 0xFFFFE4A8, 0xEA60, 0x1F40, 0x0)
    Sound(492, 0, 100, 0)
    OP_71(0x13, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x13)
    Sound(462, 0, 100, 0)
    OP_71(0x13, 0xF1, 0x10E, 0x0, 0x0)
    OP_79(0x13)
    BeginChrThread(0x3C, 3, 0, 73)
    Sleep(400)
    BeginChrThread(0x48, 3, 0, 72)
    Sleep(400)
    BeginChrThread(0x38, 3, 0, 71)
    Sleep(400)
    BeginChrThread(0x3A, 3, 0, 78)
    Sleep(800)
    Sound(461, 0, 100, 0)
    OP_71(0x13, 0x10F, 0x12C, 0x0, 0x0)
    OP_79(0x13)
    Return()

    # Function_119_12969 end

    def Function_120_12A3C(): pass

    label("Function_120_12A3C")

    OP_96(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x3A98, 0x0)

    def lambda_12A55():
        OP_D5(0xFE, 0x0, 0x0, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12A55)
    SetMapObjFrame(0x14, "kage", 0x0, 0x1)
    ClearMapObjFlags(0x15, 0x4)
    BeginChrThread(0x75, 3, 0, 121)
    OP_9D(0xFE, 0x0, 0x0, 0xFFFFCD38, 0x514, 0x514)

    def lambda_12A9D():
        OP_D5(0xFE, 0x0, 0x1B58, 0x0, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12A9D)
    OP_82(0x0, 0xC8, 0xBB8, 0xC8)
    Sound(833, 0, 100, 0)
    OP_9D(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x12C, 0x44C)
    EndChrThread(0xFE, 0x2)

    def lambda_12AE8():
        OP_D5(0xFE, 0x0, 0xFFFFE4A8, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12AE8)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    Sound(833, 0, 100, 0)
    Sound(487, 0, 100, 0)
    SetMapObjFrame(0x14, "kage", 0x1, 0x1)
    SetMapObjFlags(0x15, 0x4)
    EndChrThread(0x75, 0x3)
    BeginChrThread(0x74, 3, 0, 122)

    def lambda_12B3A():
        OP_96(0xFE, 0x0, 0xC8, 0x9C40, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12B3A)
    WaitChrThread(0xFE, 2)

    def lambda_12B58():
        OP_D5(0xFE, 0x0, 0x0, 0x0, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12B58)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_120_12A3C end

    def Function_121_12B71(): pass

    label("Function_121_12B71")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12B98")
    OP_52(0xFE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x73, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x73, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(30)
    Jump("Function_121_12B71")

    label("loc_12B98")

    Return()

    # Function_121_12B71 end

    def Function_122_12B99(): pass

    label("Function_122_12B99")

    Sleep(3100)
    Sound(880, 0, 100, 0)
    Sound(991, 0, 100, 0)
    Sound(200, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, -900, 1200, 31000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 900, 1200, 31000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x1F4, 0x1F4, 0xBB8, 0x1F4)
    OP_71(0x17, 0x0, 0xA, 0x0, 0x0)
    Return()

    # Function_122_12B99 end

    def Function_123_12C3A(): pass

    label("Function_123_12C3A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12C8F")
    PlayEffect(0x2, 0xFF, 0xFE, 0x3, 0, 1100, 1100, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Sleep(700)
    Jump("Function_123_12C3A")

    label("loc_12C8F")

    Return()

    # Function_123_12C3A end

    def Function_124_12C90(): pass

    label("Function_124_12C90")

    PlayEffect(0x2, 0xFF, 0xFE, 0x5, 0, 1100, 1100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)

    label("loc_12CC7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12D62")
    SetChrSubChip(0x23, 0x5)
    Sleep(150)
    SetChrSubChip(0x23, 0x6)
    Sleep(100)
    SetChrSubChip(0x23, 0x7)
    Sleep(100)
    SetChrSubChip(0x23, 0x4)
    Sleep(100)
    SetChrSubChip(0x23, 0x3)
    Sleep(70)
    SetChrSubChip(0x23, 0x2)
    Sleep(70)
    SetChrSubChip(0x23, 0x1)
    Sleep(70)
    SetChrSubChip(0x23, 0x0)
    Sleep(70)
    SetChrSubChip(0x23, 0x1)
    Sleep(70)
    SetChrSubChip(0x23, 0x2)
    Sleep(70)
    SetChrSubChip(0x23, 0x3)
    Sleep(70)
    SetChrSubChip(0x23, 0x4)
    Sleep(600)
    PlayEffect(0x2, 0xFF, 0xFE, 0x5, 0, 1100, 1100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Jump("loc_12CC7")

    label("loc_12D62")

    Return()

    # Function_124_12C90 end

    def Function_125_12D63(): pass

    label("Function_125_12D63")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12D81")
    OP_A1(0xFE, 0xFA0, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_125_12D63")

    label("loc_12D81")

    Return()

    # Function_125_12D63 end

    def Function_126_12D82(): pass

    label("Function_126_12D82")


    def lambda_12D87():
        OP_96(0xFE, 0xA8C, 0xFA, 0x283C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_12D87)
    Sleep(50)

    def lambda_12DA4():
        OP_96(0xFE, 0x44C, 0x64, 0x206C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x32, 1, lambda_12DA4)
    Sleep(100)
    SetChrChipByIndex(0x34, 0x3)
    SetChrSubChip(0x34, 0x0)

    def lambda_12DC9():
        OP_96(0xFE, 0xFFFFF18C, 0xFA, 0x2454, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_12DC9)
    Sleep(50)
    SetChrChipByIndex(0x35, 0x7)
    SetChrSubChip(0x35, 0x0)

    def lambda_12DEE():
        OP_96(0xFE, 0xFFFFF2B8, 0x64, 0x1BBC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_12DEE)
    WaitChrThread(0x33, 1)
    SetChrSubChip(0x33, 0x5)
    WaitChrThread(0x32, 1)
    SetChrSubChip(0x32, 0x5)
    WaitChrThread(0x34, 1)
    SetChrChipByIndex(0x34, 0x2)
    SetChrSubChip(0x34, 0x0)
    WaitChrThread(0x35, 1)
    SetChrChipByIndex(0x35, 0x6)
    SetChrSubChip(0x35, 0x0)
    Return()

    # Function_126_12D82 end

    def Function_127_12E2C(): pass

    label("Function_127_12E2C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12E45")
    Sound(567, 0, 100, 0)
    Sleep(1200)
    Jump("Function_127_12E2C")

    label("loc_12E45")

    Return()

    # Function_127_12E2C end

    def Function_128_12E46(): pass

    label("Function_128_12E46")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12E5F")
    Sound(530, 0, 70, 0)
    Sleep(1200)
    Jump("Function_128_12E46")

    label("loc_12E5F")

    Return()

    # Function_128_12E46 end

    def Function_129_12E60(): pass

    label("Function_129_12E60")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12E79")
    Sound(530, 0, 50, 0)
    Sleep(1200)
    Jump("Function_129_12E60")

    label("loc_12E79")

    Return()

    # Function_129_12E60 end

    def Function_130_12E7A(): pass

    label("Function_130_12E7A")

    Sound(987, 0, 100, 0)

    label("loc_12E80")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12EC0")
    Sleep(150)
    Sleep(100)
    Sleep(100)
    Sound(531, 0, 50, 0)
    Sleep(100)
    Sleep(70)
    Sleep(70)
    Sleep(70)
    Sleep(70)
    Sleep(70)
    Sleep(70)
    Sleep(70)
    Sleep(600)
    Sound(987, 0, 70, 0)
    Jump("loc_12E80")

    label("loc_12EC0")

    Return()

    # Function_130_12E7A end

    def Function_131_12EC1(): pass

    label("Function_131_12EC1")

    Sound(987, 0, 50, 0)

    label("loc_12EC7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12F07")
    Sleep(150)
    Sleep(100)
    Sleep(100)
    Sound(531, 0, 30, 0)
    Sleep(100)
    Sleep(70)
    Sleep(70)
    Sleep(70)
    Sleep(70)
    Sleep(70)
    Sleep(70)
    Sleep(70)
    Sleep(600)
    Sound(987, 0, 40, 0)
    Jump("loc_12EC7")

    label("loc_12F07")

    Return()

    # Function_131_12EC1 end

    def Function_132_12F08(): pass

    label("Function_132_12F08")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12F24")
    Sound(567, 0, 40, 0)
    Sleep(500)
    Sleep(500)
    Jump("Function_132_12F08")

    label("loc_12F24")

    Return()

    # Function_132_12F08 end

    def Function_133_12F25(): pass

    label("Function_133_12F25")

    Sound(457, 0, 100, 0)
    Sound(486, 0, 100, 0)
    Sleep(2000)
    Sound(458, 0, 100, 0)
    Sound(494, 0, 100, 0)
    Sleep(1000)
    Sound(493, 0, 100, 0)
    Sound(486, 0, 100, 0)
    Return()

    # Function_133_12F25 end

    def Function_134_12F50(): pass

    label("Function_134_12F50")

    Sound(457, 0, 100, 0)
    Sound(486, 0, 100, 0)
    Sleep(1000)
    Sound(493, 0, 100, 0)
    Sleep(1000)
    Sound(458, 0, 100, 0)
    Sound(494, 0, 100, 0)
    Sleep(1500)
    Sound(486, 0, 100, 0)
    Sound(457, 0, 100, 0)
    Sleep(500)
    Sound(493, 0, 100, 0)
    Sleep(1000)
    Sound(494, 0, 100, 0)
    Sleep(1000)
    Sound(486, 0, 100, 0)
    Return()

    # Function_134_12F50 end

    def Function_135_12F9F(): pass

    label("Function_135_12F9F")

    SetChrChipByIndex(0xFE, 0x9)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12FB9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12FD7")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("loc_12FB9")

    label("loc_12FD7")

    Return()

    # Function_135_12F9F end

    def Function_136_12FD8(): pass

    label("Function_136_12FD8")

    SetChrChipByIndex(0xFE, 0xA)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12FF2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13009")
    OP_A0(0xFE, 700, 0x0, 0x5)
    Jump("loc_12FF2")

    label("loc_13009")

    Return()

    # Function_136_12FD8 end

    def Function_137_1300A(): pass

    label("Function_137_1300A")

    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A6(0xFE, 0x0, 0x64, 0x12C, 0xBB8)
    Return()

    # Function_137_1300A end

    def Function_138_1303C(): pass

    label("Function_138_1303C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13091")
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 136)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE, 0x1F4, 0x0)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 137)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFD12, 0x1388, 0x0)
    WaitChrThread(0xFE, 0)
    ClearChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 135)
    Sleep(1500)
    Jump("Function_138_1303C")

    label("loc_13091")

    Return()

    # Function_138_1303C end

    def Function_139_13092(): pass

    label("Function_139_13092")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_130E7")
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 136)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x1F4, 0x0)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 137)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x1388, 0x0)
    WaitChrThread(0xFE, 0)
    ClearChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 135)
    Sleep(1000)
    Jump("Function_139_13092")

    label("loc_130E7")

    Return()

    # Function_139_13092 end

    def Function_140_130E8(): pass

    label("Function_140_130E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1313D")
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 136)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE, 0x2BC, 0x0)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 137)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFD12, 0x1388, 0x0)
    WaitChrThread(0xFE, 0)
    ClearChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 135)
    Sleep(2000)
    Jump("Function_140_130E8")

    label("loc_1313D")

    Return()

    # Function_140_130E8 end

    def Function_141_1313E(): pass

    label("Function_141_1313E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13193")
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 136)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x384, 0x0)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 137)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x1388, 0x0)
    WaitChrThread(0xFE, 0)
    ClearChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 135)
    Sleep(2500)
    Jump("Function_141_1313E")

    label("loc_13193")

    Return()

    # Function_141_1313E end

    def Function_142_13194(): pass

    label("Function_142_13194")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51719.itc", 0x0)
    LoadChrToIndex("apl/ch51718.itc", 0x1)
    LoadChrToIndex("chr/ch32050.itc", 0x2)
    LoadChrToIndex("chr/ch32056.itc", 0x5)
    LoadChrToIndex("chr/ch32152.itc", 0x8)
    LoadChrToIndex("monster/ch85150.itc", 0x9)
    LoadChrToIndex("monster/ch85151.itc", 0xA)
    LoadChrToIndex("monster/ch85153.itc", 0xB)
    LoadChrToIndex("apl/ch50509.itc", 0xD)
    LoadChrToIndex("chr/ch30200.itc", 0xF)
    LoadChrToIndex("apl/ch51720.itc", 0x10)
    LoadChrToIndex("chr/ch30500.itc", 0x11)
    LoadChrToIndex("chr/ch30100.itc", 0x12)
    LoadChrToIndex("chr/ch30000.itc", 0x13)
    LoadChrToIndex("apl/ch51236.itc", 0x14)
    LoadChrToIndex("apl/ch51721.itc", 0x16)
    LoadChrToIndex("apl/ch51722.itc", 0x19)
    LoadChrToIndex("chr/ch30600.itc", 0x1F)
    LoadEffect(0x9, "map/mpmoya.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0x78, 0x96, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xFF, 0xD, 0x190, 0x0)
    LoadEffect(0x1, "event/ev17061.eff")
    OP_8E(0x2F, "Kirika")
    OP_8E(0x28, "Rector")
    SetChrPos(0x0, 0, 0, 50000, 0)
    SetChrPos(0x1, 0, 0, 50000, 0)
    SetChrPos(0x2, 0, 0, 50000, 0)
    SetChrPos(0x3, 0, 0, 50000, 0)
    SetChrChipByIndex(0x32, 0x0)
    SetChrSubChip(0x32, 0x5)
    SetChrFlags(0x32, 0x8000)
    ClearChrFlags(0x32, 0x80)
    SetChrPos(0x32, 1900, 100, 4200, 45)
    SetChrChipByIndex(0x33, 0x1)
    SetChrSubChip(0x33, 0x5)
    SetChrFlags(0x33, 0x8000)
    ClearChrFlags(0x33, 0x80)
    SetChrPos(0x33, 2500, 100, 6500, 45)
    SetChrChipByIndex(0x34, 0x2)
    SetChrSubChip(0x34, 0x0)
    SetChrFlags(0x34, 0x8000)
    ClearChrFlags(0x34, 0x80)
    SetChrPos(0x34, -1500, 100, 6300, 0)
    SetChrChipByIndex(0x35, 0x8)
    SetChrSubChip(0x35, 0x1)
    SetChrFlags(0x35, 0x8000)
    ClearChrFlags(0x35, 0x80)
    SetChrPos(0x35, 500, 100, 4800, 0)
    SetChrChipByIndex(0x38, 0xF)
    SetChrSubChip(0x38, 0x0)
    SetChrFlags(0x38, 0x8000)
    ClearChrFlags(0x38, 0x80)
    SetChrPos(0x38, 3100, 250, -1700, 0)
    SetChrChipByIndex(0x48, 0x13)
    SetChrSubChip(0x48, 0x0)
    SetChrFlags(0x48, 0x8000)
    ClearChrFlags(0x48, 0x80)
    SetChrPos(0x48, 6100, 50, -700, 315)
    SetChrChipByIndex(0x3C, 0x13)
    SetChrSubChip(0x3C, 0x0)
    SetChrFlags(0x3C, 0x8000)
    ClearChrFlags(0x3C, 0x80)
    SetChrPos(0x3C, 7400, 0, -500, 315)
    SetChrChipByIndex(0x49, 0x13)
    SetChrSubChip(0x49, 0x0)
    SetChrFlags(0x49, 0x8000)
    ClearChrFlags(0x49, 0x80)
    SetChrPos(0x49, -3100, 250, -1700, 0)
    SetChrChipByIndex(0x39, 0x11)
    SetChrSubChip(0x39, 0x0)
    SetChrFlags(0x39, 0x8000)
    ClearChrFlags(0x39, 0x80)
    SetChrPos(0x39, -6100, 50, -700, 45)
    SetChrChipByIndex(0x4A, 0x13)
    SetChrSubChip(0x4A, 0x0)
    SetChrFlags(0x4A, 0x8000)
    ClearChrFlags(0x4A, 0x80)
    SetChrPos(0x4A, -7400, 0, -500, 45)
    SetChrChipByIndex(0x3B, 0x1F)
    SetChrSubChip(0x3B, 0x0)
    SetChrFlags(0x3B, 0x8000)
    ClearChrFlags(0x3B, 0x80)
    SetChrPos(0x3B, -6400, 0, -3000, 0)
    SetChrChipByIndex(0x3A, 0x12)
    SetChrSubChip(0x3A, 0x0)
    SetChrFlags(0x3A, 0x8000)
    ClearChrFlags(0x3A, 0x80)
    SetChrPos(0x3A, 4400, 0, -2200, 0)
    SetChrChipByIndex(0x23, 0xD)
    SetChrSubChip(0x23, 0x0)
    SetChrFlags(0x23, 0x8000)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x23, -2000, 250, -1600, 0)
    SetChrChipByIndex(0x2F, 0x19)
    SetChrSubChip(0x2F, 0x0)
    SetChrFlags(0x2F, 0x8000)
    ClearChrFlags(0x2F, 0x80)
    SetChrPos(0x2F, -3000, 100, 6600, 315)
    SetChrChipByIndex(0x28, 0x16)
    SetChrSubChip(0x28, 0x0)
    SetChrFlags(0x28, 0x8000)
    ClearChrFlags(0x28, 0x80)
    SetChrPos(0x28, 4100, 100, 4800, 45)
    SetChrChipByIndex(0x3E, 0x9)
    SetChrSubChip(0x3E, 0x0)
    ClearChrFlags(0x3E, 0x80)
    SetChrFlags(0x3E, 0x8000)
    OP_52(0x3E, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x3E, -8500, 0, 9500, 135)
    SetChrChipByIndex(0x3F, 0x9)
    SetChrSubChip(0x3F, 0x0)
    ClearChrFlags(0x3F, 0x80)
    SetChrFlags(0x3F, 0x8000)
    OP_52(0x3F, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x3F, 8500, 0, 9500, 225)
    SetChrChipByIndex(0x40, 0x9)
    SetChrSubChip(0x40, 0x0)
    ClearChrFlags(0x40, 0x80)
    SetChrFlags(0x40, 0x8000)
    OP_52(0x40, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x40, -5500, 250, 10500, 135)
    SetChrChipByIndex(0x41, 0x9)
    SetChrSubChip(0x41, 0x0)
    ClearChrFlags(0x41, 0x80)
    SetChrFlags(0x41, 0x8000)
    OP_52(0x41, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x41, 5500, 250, 10500, 225)
    SetChrChipByIndex(0x42, 0x9)
    SetChrSubChip(0x42, 0x0)
    ClearChrFlags(0x42, 0x80)
    SetChrFlags(0x42, 0x8000)
    OP_52(0x42, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x42, 3000, 100, 15000, 180)
    SetChrChipByIndex(0x43, 0x9)
    SetChrSubChip(0x43, 0x0)
    ClearChrFlags(0x43, 0x80)
    SetChrFlags(0x43, 0x8000)
    OP_52(0x43, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x43, -3000, 100, 15000, 180)
    BeginChrThread(0x3E, 3, 0, 143)
    BeginChrThread(0x3F, 3, 0, 144)
    BeginChrThread(0x40, 3, 0, 145)
    BeginChrThread(0x41, 3, 0, 146)
    BeginChrThread(0x42, 3, 0, 147)
    BeginChrThread(0x43, 3, 0, 148)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x18, 0x4)
    SetMapObjFlags(0x18, 0x1000)
    ClearChrFlags(0x71, 0x80)
    OP_78(0x12, 0x71)
    SetMapObjFrame(0x12, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x71, -4500, 250, 800, 0)
    OP_D5(0x71, 0x0, 0xFFFEEE90, 0x0, 0x0)
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x12, 0x1000)
    OP_74(0x12, 0x1E)
    OP_70(0x12, 0x0)
    ClearChrFlags(0x72, 0x80)
    OP_78(0x16, 0x72)
    OP_49()
    SetChrPos(0x72, 4500, 250, 800, 0)
    OP_D5(0x72, 0x0, 0x11170, 0x0, 0x0)
    ClearMapObjFlags(0x16, 0x4)
    SetMapObjFlags(0x16, 0x1000)
    OP_74(0x16, 0x1E)
    OP_70(0x16, 0x0)
    OP_68(0, 1350, 9300, 0)
    MoveCamera(37, 17, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(21500, 0)
    FadeToBright(2000, 0)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x1770)
    OP_11(0x8E, 0xC7, 0xFF, 0x1E, 0x26C, 0x1770)
    OP_68(0, 1250, 2300, 6000)
    MoveCamera(27, 17, 0, 6000)
    SetCameraDistance(16500, 6000)
    Sleep(2000)
    StopEffect(0x7, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x32,
        "#5PWoah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x38,
        "#12PT-they vanished?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "#03400F…… Supply of spiritual power\x01",
            "It seems I got ceased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#11P#11506FWhew ……\x01",
            "I'm tired from seriously ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "#01002FHydrofluoric acid\x01",
            "I did it.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 3)
    NewScene("c1600", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_142_13194 end

    def Function_143_138C9(): pass

    label("Function_143_138C9")

    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0x0, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Sound(985, 0, 100, 0)
    Sleep(1800)

    def lambda_13924():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_13924)
    WaitChrThread(0xFE, 2)
    StopEffect(0x0, 0x2)
    Return()

    # Function_143_138C9 end

    def Function_144_13938(): pass

    label("Function_144_13938")

    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0x1, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2400)

    def lambda_1398A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1398A)
    WaitChrThread(0xFE, 2)
    StopEffect(0x1, 0x2)
    Return()

    # Function_144_13938 end

    def Function_145_1399E(): pass

    label("Function_145_1399E")

    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0x2, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2800)

    def lambda_139F0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_139F0)
    WaitChrThread(0xFE, 2)
    StopEffect(0x2, 0x2)
    Return()

    # Function_145_1399E end

    def Function_146_13A04(): pass

    label("Function_146_13A04")

    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0x3, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2600)

    def lambda_13A56():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_13A56)
    WaitChrThread(0xFE, 2)
    StopEffect(0x3, 0x2)
    Return()

    # Function_146_13A04 end

    def Function_147_13A6A(): pass

    label("Function_147_13A6A")

    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0x4, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)

    def lambda_13ABC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_13ABC)
    WaitChrThread(0xFE, 2)
    StopEffect(0x4, 0x2)
    Return()

    # Function_147_13A6A end

    def Function_148_13AD0(): pass

    label("Function_148_13AD0")

    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0x5, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2200)

    def lambda_13B22():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_13B22)
    WaitChrThread(0xFE, 2)
    StopEffect(0x5, 0x2)
    Return()

    # Function_148_13AD0 end

    def Function_149_13B36(): pass

    label("Function_149_13B36")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFlags(0x9, 0x4)
    LoadChrToIndex("chr/ch31300.itc", 0x1)
    SetChrPos(0x0, 0, 0, 50000, 0)
    SetChrPos(0x1, 0, 0, 50000, 0)
    SetChrPos(0x2, 0, 0, 50000, 0)
    SetChrPos(0x3, 0, 0, 50000, 0)
    SetChrChipByIndex(0x48, 0x0)
    SetChrSubChip(0x48, 0x0)
    ClearChrFlags(0x48, 0x80)
    ClearChrFlags(0x48, 0x4)
    SetChrFlags(0x48, 0x8000)
    SetChrPos(0x48, -2100, 0, -20500, 180)
    SetChrChipByIndex(0x49, 0x0)
    SetChrSubChip(0x49, 0x0)
    ClearChrFlags(0x49, 0x80)
    ClearChrFlags(0x49, 0x4)
    SetChrFlags(0x49, 0x8000)
    SetChrPos(0x49, 2100, 0, -20500, 180)
    SetChrChipByIndex(0x4A, 0x0)
    SetChrSubChip(0x4A, 0x0)
    ClearChrFlags(0x4A, 0x80)
    ClearChrFlags(0x49, 0x4)
    SetChrFlags(0x4A, 0x8000)
    SetChrPos(0x4A, -900, 0, -15300, 90)
    SetChrChipByIndex(0x4B, 0x1)
    SetChrSubChip(0x4B, 0x0)
    ClearChrFlags(0x4B, 0x80)
    ClearChrFlags(0x4B, 0x4)
    SetChrFlags(0x4B, 0x8000)
    SetChrPos(0x4B, 200, 0, -15300, 270)
    SetChrChipByIndex(0x4C, 0x0)
    SetChrSubChip(0x4C, 0x0)
    ClearChrFlags(0x4C, 0x80)
    ClearChrFlags(0x4C, 0x4)
    SetChrFlags(0x4C, 0x8000)
    SetChrPos(0x4C, 900, 0, -11600, 30)
    SetChrChipByIndex(0x4D, 0x0)
    SetChrSubChip(0x4D, 0x0)
    ClearChrFlags(0x4D, 0x80)
    ClearChrFlags(0x4D, 0x4)
    SetChrFlags(0x4D, 0x8000)
    SetChrPos(0x4D, -2200, 0, -8900, 345)
    ClearChrFlags(0x71, 0x80)
    OP_78(0x13, 0x71)
    SetMapObjFrame(0x13, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x71, -2500, 0, -16000, 0)
    OP_D5(0x71, 0x0, 0x2BF20, 0x0, 0x0)
    ClearMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x13, 0x1000)
    OP_74(0x13, 0x1E)
    OP_70(0x13, 0x0)
    ClearChrFlags(0x72, 0x80)
    OP_78(0xC, 0x72)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x72, 2500, 0, -16000, 0)
    OP_D5(0x72, 0x0, 0x2BF20, 0x0, 0x0)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x1000)
    OP_74(0xC, 0x1E)
    OP_70(0xC, 0x0)
    ClearChrFlags(0x71, 0x80)
    OP_78(0x12, 0x73)
    SetMapObjFrame(0x12, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x73, 2300, 0, -9700, 300)
    OP_D5(0x73, 0x0, 0x493E0, 0x0, 0x0)
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x12, 0x1000)
    OP_74(0x12, 0x1E)
    OP_70(0x12, 0x0)
    ClearChrFlags(0x74, 0x80)
    OP_78(0xB, 0x74)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x74, -2300, 0, -5400, 70)
    OP_D5(0x74, 0x0, 0x11170, 0x0, 0x0)
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xB, 0x1000)
    OP_74(0xB, 0x1E)
    OP_70(0xB, 0x0)
    OP_68(-1000, 1700, -17500, 0)
    MoveCamera(35, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Return()

    # Function_149_13B36 end

    def Function_150_13DF7(): pass

    label("Function_150_13DF7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFlags(0x9, 0x4)
    LoadChrToIndex("chr/ch05620.itc", 0x1)
    SetChrPos(0x0, 0, 0, 50000, 0)
    SetChrPos(0x1, 0, 0, 50000, 0)
    SetChrPos(0x2, 0, 0, 50000, 0)
    SetChrPos(0x3, 0, 0, 50000, 0)
    ClearChrFlags(0x71, 0x80)
    OP_78(0x13, 0x71)
    SetMapObjFrame(0x13, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x71, 0, 0, -8500, 270)
    OP_D5(0x71, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x13, 0x1000)
    OP_74(0x13, 0x1E)
    OP_70(0x13, 0x186)
    SetChrChipByIndex(0x48, 0x0)
    SetChrSubChip(0x48, 0x0)
    ClearChrFlags(0x48, 0x80)
    ClearChrFlags(0x48, 0x4)
    SetChrFlags(0x48, 0x8000)
    SetChrPos(0x48, -800, 0, -4900, 180)
    SetChrChipByIndex(0x49, 0x0)
    SetChrSubChip(0x49, 0x0)
    ClearChrFlags(0x49, 0x80)
    ClearChrFlags(0x49, 0x4)
    SetChrFlags(0x49, 0x8000)
    SetChrPos(0x49, 800, 0, -4900, 180)
    SetChrChipByIndex(0x4A, 0x0)
    SetChrSubChip(0x4A, 0x0)
    ClearChrFlags(0x4A, 0x80)
    ClearChrFlags(0x4A, 0x4)
    SetChrFlags(0x4A, 0x8000)
    SetChrPos(0x4A, -2500, 0, -6800, 45)
    SetChrChipByIndex(0x30, 0x1)
    SetChrSubChip(0x30, 0x0)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x30, 0x4)
    SetChrFlags(0x30, 0x8000)
    SetChrPos(0x30, 0, 0, -5000, 180)
    OP_68(0, 900, -7000, 0)
    MoveCamera(137, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Return()

    # Function_150_13DF7 end

    SaveToFile()

Try(main)
