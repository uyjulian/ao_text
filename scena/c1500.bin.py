from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Patrol Officer Cunnings",# 1
        "Patrol Officer Martin",  # 2
        "Tajik",                  # 3
        "Policeman",              # 4
        "Policeman",              # 5
        "Policeman",              # 6
        "Policeman",              # 7
        "City Hall Staffer",      # 8
        "City Hall Staffer",      # 9
        "2nd Lt. Mireille",       # 10
        "Citizen",                # 11
        "Girl",                   # 12
        "Tourist",                # 13
        "Tourist",                # 14
        "Tourist",                # 15
        "Tourist",                # 16
        "Tourist",                # 17
        "Tourist",                # 18
        "Kindoll",                # 19
        "Ryｹ",                   # 20
        "Henri",                  # 21
        "Momo",                   # 22
        "Shing",                  # 23
        "Reporter Noticia",       # 24
        "Nielsen",                # 25
        "Vice Commander Douglas", # 26
        "Chairman MacDowell",     # 27
        "Chief Sergei",           # 28
        "壊れた支援課車",         # 29
        "新型装甲車",             # 30
        "新型装甲車",             # 31
        "Chancellor Osborne",     # 32
        "Secretary Lechter",      # 33
        "Prince Olivert",         # 34
        "Major Mueller",          # 35
        "Princess Klaudia",       # 36
        "Captain Julia",          # 37
        "Archduke Albert",        # 38
        "President Rocksmith",    # 39
        "Aide Kilika",            # 40
        "Mayor Dieter",           # 41
        "Mariabell",              # 42
        "Bracer Scott",           # 43
        "Bracer Wenzel",          # 44
        "Bracer Ling",            # 45
        "Bracer Eolia",           # 46
        "Secretary of Defense Arios",# 47
        "Detective Dudley",       # 48
        "Detective Raymond",      # 49
        "Detective Emma",         # 50
        "Section Chief Joe Ridge",# 51
        "Head Patrol Officer Kate",# 52
        "Patrol Officer Frantz",  # 53
        "Everyone's Voices",      # 54
        "イベント用モンスター",   # 55
        "イベント用モンスター",   # 56
        "イベント用モンスター",   # 57
        "イベント用モンスター",   # 58
        "イベント用モンスター",   # 59
        "イベント用モンスター",   # 60
        "イベント用モンスター",   # 61
        "イベント用モンスター",   # 62
        "イベント用モンスター",   # 63
        "Commander Sonya",        # 64
        "Policeman",              # 65
        "Policeman",              # 66
        "Policeman",              # 67
        "Policeman",              # 68
        "Policeman",              # 69
        "Policeman",              # 70
        "Policeman",              # 71
        "Policeman",              # 72
        "Policeman",              # 73
        "Policeman",              # 74
        "CGF",                    # 75
        "CGF",                    # 76
        "CGF",                    # 77
        "CGF",                    # 78
        "CGF",                    # 79
        "CGF",                    # 80
        "CGF",                    # 81
        "CGF",                    # 82
        "Secretary",              # 83
        "Butler",                 # 84
        "Imperial Military Officer",# 85
        "Imperial Military Officer",# 86
        "Republic Military Officer",# 87
        "Republic Military Officer",# 88
        "Bodyguard",              # 89
        "Bodyguard",              # 90
        "Soldier Carter",         # 91
        "State Guard Soldier - Man",# 92
        "State Guard Soldier - Man",# 93
        "State Guard Soldier - Man",# 94
        "State Guard Soldier - Man",# 95
        "State Guard Soldier - Woman",# 96
        "State Guard Soldier - Woman",# 97
        "State Guard Soldier - Woman",# 98
        "State Guard Officer",    # 99
        "Grace",                  # 100
        "Reins",                  # 101
        "Reporter",               # 102
        "Reporter",               # 103
        "Reporter",               # 104
        "Reporter",               # 105
        "車",                     # 106
        "車",                     # 107
        "車",                     # 108
        "車",                     # 109
        "New-Type Armored Vehicle A",# 110
        "New-Type Armored Vehicle B",# 111
        "Crescent Moon Ring",     # 112
        "Crescent Moon Ring",     # 113
        "SE制御",                 # 114
        "Central Square",         # 115
        "West Street",            # 116
        "Governmental District",  # 117
        "Residential Street",     # 118
        "Entertainment District", # 119
        "East Street",            # 120
        "Downtown",               # 121
        "Waterfront Area",        # 122
        "IBC",                    # 123
        "Station Street",         # 124
        "Back Street",            # 125
        "St. Ursula Byroad",      # 126
        "East Crossbell Highway", # 127
        "West Crossbell HIghway", # 128
        "Mainz Mountain Road",    # 129
        "Orchis Tower",           # 130
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

    PlaceName(-20.690000534057617, 0.0, -334.95001220703125, 0x0000, 0x0000, "Central Square")
    PlaceName(-176.4499969482422, 0.0, -343.79998779296875, 0x0000, 0x0000, "West Street")
    PlaceName(21.639999389648438, 0.0, -191.3000030517578, 0x0000, 0x0000, "Governmental District")
    PlaceName(-276.45001220703125, 0.0, -223.8000030517578, 0x0000, 0x0000, "Residential Street")
    PlaceName(-142.5, 0.0, -222.60000610351562, 0x0000, 0x0000, "Entertainment District")
    PlaceName(113.25, 0.0, -400.5, 0x0000, 0x0000, "East Street")
    PlaceName(183.5800018310547, 0.0, -513.25, 0x0000, 0x0000, "Downtown")
    PlaceName(154.9499969482422, 0.0, -274.3999938964844, 0x0000, 0x0000, "Waterfront Area")
    PlaceName(126.94999694824219, 0.0, -96.5, 0x0000, 0x0000, "IBC")
    PlaceName(-17.75, 0.0, -493.6000061035156, 0x0000, 0x0000, "Station Street")
    PlaceName(-101.80000305175781, 0.0, -283.20001220703125, 0x0000, 0x0000, "Back Street")
    PlaceName(-21.200000762939453, 0.0, -548.0499877929688, 0x0000, 0x0000, "St. Ursula Byroad")
    PlaceName(234.85000610351562, 0.0, -384.6000061035156, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-264.95001220703125, 0.0, -340.3999938964844, 0x0000, 0x0000, "West Crossbell HIghway")
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
        "Function_14_2BD6",        # 0E, 14
        "Function_15_36CD",        # 0F, 15
        "Function_16_4201",        # 10, 16
        "Function_17_4399",        # 11, 17
        "Function_18_4426",        # 12, 18
        "Function_19_44D8",        # 13, 19
        "Function_20_4561",        # 14, 20
        "Function_21_45FE",        # 15, 21
        "Function_22_4D01",        # 16, 22
        "Function_23_4E36",        # 17, 23
        "Function_24_4F62",        # 18, 24
        "Function_25_4FAD",        # 19, 25
        "Function_26_5028",        # 1A, 26
        "Function_27_50C4",        # 1B, 27
        "Function_28_5125",        # 1C, 28
        "Function_29_5630",        # 1D, 29
        "Function_30_5B6D",        # 1E, 30
        "Function_31_6123",        # 1F, 31
        "Function_32_66AA",        # 20, 32
        "Function_33_6BCC",        # 21, 33
        "Function_34_6E6B",        # 22, 34
        "Function_35_721D",        # 23, 35
        "Function_36_7431",        # 24, 36
        "Function_37_746C",        # 25, 37
        "Function_38_74C9",        # 26, 38
        "Function_39_76DC",        # 27, 39
        "Function_40_787A",        # 28, 40
        "Function_41_78B8",        # 29, 41
        "Function_42_7905",        # 2A, 42
        "Function_43_79A2",        # 2B, 43
        "Function_44_7A9B",        # 2C, 44
        "Function_45_8B47",        # 2D, 45
        "Function_46_91EC",        # 2E, 46
        "Function_47_97A9",        # 2F, 47
        "Function_48_97F6",        # 30, 48
        "Function_49_9843",        # 31, 49
        "Function_50_9890",        # 32, 50
        "Function_51_98DD",        # 33, 51
        "Function_52_B3F6",        # 34, 52
        "Function_53_B4AF",        # 35, 53
        "Function_54_B62D",        # 36, 54
        "Function_55_B653",        # 37, 55
        "Function_56_B6AE",        # 38, 56
        "Function_57_BB30",        # 39, 57
        "Function_58_BBCB",        # 3A, 58
        "Function_59_C550",        # 3B, 59
        "Function_60_C9A8",        # 3C, 60
        "Function_61_CC93",        # 3D, 61
        "Function_62_DAC0",        # 3E, 62
        "Function_63_DB7F",        # 3F, 63
        "Function_64_DCA0",        # 40, 64
        "Function_65_E3F0",        # 41, 65
        "Function_66_E4A9",        # 42, 66
        "Function_67_F082",        # 43, 67
        "Function_68_F09E",        # 44, 68
        "Function_69_F0C7",        # 45, 69
        "Function_70_F1D5",        # 46, 70
        "Function_71_10B5A",       # 47, 71
        "Function_72_10BC3",       # 48, 72
        "Function_73_10C26",       # 49, 73
        "Function_74_10C89",       # 4A, 74
        "Function_75_10CEC",       # 4B, 75
        "Function_76_10D5F",       # 4C, 76
        "Function_77_10DC8",       # 4D, 77
        "Function_78_10E1D",       # 4E, 78
        "Function_79_10E93",       # 4F, 79
        "Function_80_10F04",       # 50, 80
        "Function_81_110AB",       # 51, 81
        "Function_82_11255",       # 52, 82
        "Function_83_113FC",       # 53, 83
        "Function_84_11447",       # 54, 84
        "Function_85_11496",       # 55, 85
        "Function_86_114F9",       # 56, 86
        "Function_87_1155C",       # 57, 87
        "Function_88_115BF",       # 58, 88
        "Function_89_1161D",       # 59, 89
        "Function_90_116AA",       # 5A, 90
        "Function_91_11880",       # 5B, 91
        "Function_92_11903",       # 5C, 92
        "Function_93_11986",       # 5D, 93
        "Function_94_11A09",       # 5E, 94
        "Function_95_11D4D",       # 5F, 95
        "Function_96_11DA3",       # 60, 96
        "Function_97_11EC2",       # 61, 97
        "Function_98_11F0A",       # 62, 98
        "Function_99_12202",       # 63, 99
        "Function_100_12290",      # 64, 100
        "Function_101_1239E",      # 65, 101
        "Function_102_123CD",      # 66, 102
        "Function_103_12486",      # 67, 103
        "Function_104_12593",      # 68, 104
        "Function_105_12704",      # 69, 105
        "Function_106_1273D",      # 6A, 106
        "Function_107_12D77",      # 6B, 107
        "Function_108_12D83",      # 6C, 108
        "Function_109_12DA6",      # 6D, 109
        "Function_110_12FF1",      # 6E, 110
        "Function_111_1308B",      # 6F, 111
        "Function_112_130EE",      # 70, 112
        "Function_113_1328D",      # 71, 113
        "Function_114_132D8",      # 72, 114
        "Function_115_13372",      # 73, 115
        "Function_116_133D8",      # 74, 116
        "Function_117_13464",      # 75, 117
        "Function_118_13483",      # 76, 118
        "Function_119_13565",      # 77, 119
        "Function_120_13638",      # 78, 120
        "Function_121_1376D",      # 79, 121
        "Function_122_13795",      # 7A, 122
        "Function_123_13836",      # 7B, 123
        "Function_124_1388C",      # 7C, 124
        "Function_125_1395F",      # 7D, 125
        "Function_126_1397E",      # 7E, 126
        "Function_127_13A28",      # 7F, 127
        "Function_128_13A42",      # 80, 128
        "Function_129_13A5C",      # 81, 129
        "Function_130_13A76",      # 82, 130
        "Function_131_13ABD",      # 83, 131
        "Function_132_13B04",      # 84, 132
        "Function_133_13B21",      # 85, 133
        "Function_134_13B4C",      # 86, 134
        "Function_135_13B9B",      # 87, 135
        "Function_136_13BD4",      # 88, 136
        "Function_137_13C06",      # 89, 137
        "Function_138_13C38",      # 8A, 138
        "Function_139_13C8E",      # 8B, 139
        "Function_140_13CE4",      # 8C, 140
        "Function_141_13D3A",      # 8D, 141
        "Function_142_13D90",      # 8E, 142
        "Function_143_144B9",      # 8F, 143
        "Function_144_14528",      # 90, 144
        "Function_145_1458E",      # 91, 145
        "Function_146_145F4",      # 92, 146
        "Function_147_1465A",      # 93, 147
        "Function_148_146C0",      # 94, 148
        "Function_149_14726",      # 95, 149
        "Function_150_149E7",      # 96, 150
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_20FE")

    ChrTalk(
        0xFE,
        (
            "Since the State Guard soldiers have\x01",
            "retreated, we, the patrol division,\x01",
            "have decided to re-deploy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a tough situation,\x01",
            "but let's each do our\x01",
            "best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BD2")

    label("loc_20FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_210C")
    Jump("loc_2BD2")

    label("loc_210C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_211A")
    Jump("loc_2BD2")

    label("loc_211A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2356")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_227B")

    ChrTalk(
        0xFE,
        (
            "Offense and defense in front of\x01",
            "Orchis Tower... It was truly a\x01",
            "fierce, decisive battle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honestly, without Arios\x01",
            "here, this place could\x01",
            "end up like IBC...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Ugh, what am I saying.\x01",
            "By saying that, I'm getting\x01",
            "myself even more scared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, this place is\x01",
            "safe. Thinking about other\x01",
            "things can't be helped.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2351")

    label("loc_227B")


    ChrTalk(
        0xFE,
        (
            "Detective Dudley is amazing,\x01",
            "but... Arios is a whole\x01",
            "other dimension of strength.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sword movements so fast, you could say\x01",
            "they're an act of the Goddess... That's\x01",
            "why they call him the Sword Saint of Wind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2351")

    Jump("loc_2BD2")

    label("loc_2356")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2413")

    ChrTalk(
        0xFE,
        (
            "An occupation at Mainz, huh...\x01",
            "Ugh, another unthinkable thing\x01",
            "has happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although the situation is\x01",
            "pretty intense, the CGF has to\x01",
            "hold out for us no matter what.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BD2")

    label("loc_2413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_24C6")

    ChrTalk(
        0xFE,
        (
            "As you might expect, there's\x01",
            "hardly any people in this\x01",
            "plaza on rainy days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And because the plaza is\x01",
            "this vast, it makes it even\x01",
            "more sad for some reason.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BD2")

    label("loc_24C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2599")

    ChrTalk(
        0xFE,
        (
            "I heard from the receptionist\x01",
            "just now. She said there's\x01",
            "been a derailment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Section Two and the CGF have already left\x01",
            "to investigate, but... I'm concerned\x01",
            "about the extent of the damage.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BD2")

    label("loc_2599")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_26B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_265E")

    ChrTalk(
        0xFE,
        (
            "It seems this plaza in front of\x01",
            "the tower is taking hold as a\x01",
            "place for the citizens to relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's heartwarming,\x01",
            "seeing families enjoying\x01",
            "their time together.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_26B3")

    label("loc_265E")


    ChrTalk(
        0xFE,
        (
            "Bright sun and close\x01",
            "families...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. No scene could be\x01",
            "more heartwarming.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26B3")

    Jump("loc_2BD2")

    label("loc_26B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2905")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2841")

    ChrTalk(
        0xFE,
        (
            "More than a month has\x01",
            "passed since the trade\x01",
            "conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The terrorist attack was of course a\x01",
            "major incident, but the independence\x01",
            "proposal immediately following...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, major incidents and events\x01",
            "have really been occurring one\x01",
            "after the next this year, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With my head spinning like\x01",
            "this, I feel the time has\x01",
            "passed in the blink of an eye.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2900")

    label("loc_2841")


    ChrTalk(
        0xFE,
        (
            "Anyway, major incidents and events\x01",
            "have really been occurring one\x01",
            "after the next this year, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With my head spinning like\x01",
            "this, I feel the time has\x01",
            "passed in the blink of an eye.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2900")

    Jump("loc_2BD2")

    label("loc_2905")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2A5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29D6")

    ChrTalk(
        0xFE,
        (
            "Hey, if it isn't the\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard you were\x01",
            "participating in the trade\x01",
            "conference security detail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, you can head\x01",
            "inside whenever you're\x01",
            "ready.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2A59")

    label("loc_29D6")


    ChrTalk(
        0xFE,
        (
            "I heard you were\x01",
            "participating in the trade\x01",
            "conference security detail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, you can head\x01",
            "inside whenever you're\x01",
            "ready.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A59")

    Jump("loc_2BD2")

    label("loc_2A5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2BD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B3C")

    ChrTalk(
        0xFE,
        (
            "Oh, you're the Special\x01",
            "Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We, the patrol division,\x01",
            "are responsible for\x01",
            "Orchis Tower security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, we're both police.\x01",
            "Let's help each other\x01",
            "out if anything happens.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2BD2")

    label("loc_2B3C")


    ChrTalk(
        0xFE,
        (
            "We, the patrol division,\x01",
            "are responsible for\x01",
            "Orchis Tower security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, we're both police.\x01",
            "Let's help each other\x01",
            "out if anything happens.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BD2")

    TalkEnd(0xFE)
    Return()

    # Function_13_204C end

    def Function_14_2BD6(): pass

    label("Function_14_2BD6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2C6B")

    ChrTalk(
        0xFE,
        (
            "President Dieter is in\x01",
            "custody on 36F.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To think the leader of my\x01",
            "state was arrested. ...That's\x01",
            "not a good feeling at all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36C9")

    label("loc_2C6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2C79")
    Jump("loc_36C9")

    label("loc_2C79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2C87")
    Jump("loc_36C9")

    label("loc_2C87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2DFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D94")

    ChrTalk(
        0xFE,
        (
            "Red Constellation...\x01",
            "They were really\x01",
            "terrifying guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The difference in combat techniques\x01",
            "aside, even their weapons were\x01",
            "clearly better than ours...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If Crossbell had a military,\x01",
            "the situation would have\x01",
            "been different, but...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2DF9")

    label("loc_2D94")


    ChrTalk(
        0xFE,
        (
            "Red Constellation...\x01",
            "They were really\x01",
            "terrifying guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, if Crossbell had a\x01",
            "military...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DF9")

    Jump("loc_36C9")

    label("loc_2DFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2FC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F0D")

    ChrTalk(
        0xFE,
        (
            "It's especially in times like\x01",
            "these that we police have to\x01",
            "look after the citizens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just like the CGF, we\x01",
            "train regularly for\x01",
            "things like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Be model citizens. Let's\x01",
            "reflect on those words, and\x01",
            "give this everything we've got.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2FC0")

    label("loc_2F0D")


    ChrTalk(
        0xFE,
        (
            "It's especially in times like\x01",
            "these that we police have to\x01",
            "look after the citizens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Be model citizens. Let's\x01",
            "reflect on those words, and\x01",
            "give this everything we've got.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FC0")

    Jump("loc_36C9")

    label("loc_2FC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3094")

    ChrTalk(
        0xFE,
        (
            "Because of the CGF's great\x01",
            "efforts, the railway was somehow\x01",
            "completely repaired yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There might have been trouble\x01",
            "due to this rain, but I have to\x01",
            "respect their rapid response.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36C9")

    label("loc_3094")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3131")

    ChrTalk(
        0xFE,
        (
            "An orbal train derailed\x01",
            "around West Crossbell\x01",
            "Highway...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We rarely hear about\x01",
            "accidents in Crossbell. Just\x01",
            "what could have happened?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36C9")

    label("loc_3131")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_31EB")

    ChrTalk(
        0xFE,
        (
            "Once use of Orchis Tower\x01",
            "gets up to speed, there'll\x01",
            "be even more traffic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Work will get busier once that\x01",
            "happens, but as a Crossbellian,\x01",
            "no joy could be greater.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36C9")

    label("loc_31EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3476")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3392")

    ChrTalk(
        0xFE,
        (
            "I hate to bring it up again,\x01",
            "but that terror incident was\x01",
            "a real embarrassment for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We police fought on the defensive. In\x01",
            "the end, the major powers relied on the\x01",
            "armed forces they each had prepared...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And on top of that, our\x01",
            "own security was used\x01",
            "against us, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To raise our crisis management abilities\x01",
            "even further, it's only natural that we\x01",
            "heighten our awareness...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3471")

    label("loc_3392")


    ChrTalk(
        0xFE,
        (
            "That line of defense were counting\x01",
            "was penetrated so easily. Even if we\x01",
            "had two or three times the men...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To raise our crisis management abilities\x01",
            "even further, it's only natural that we\x01",
            "heighten our awareness...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3471")

    Jump("loc_36C9")

    label("loc_3476")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_34FB")

    ChrTalk(
        0xFE,
        (
            "Good work today,\x01",
            "everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's both do our very best to\x01",
            "ensure the trade conference\x01",
            "ends without incident.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36C9")

    label("loc_34FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_36C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35E3")

    ChrTalk(
        0xFE,
        (
            "Officer Cunnings and I\x01",
            "are assigned as Orchis\x01",
            "Tower security personnel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There is the trade conference of course,\x01",
            "but this plaza is also expected to be\x01",
            "packed going forward, so let's do our best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_36C9")

    label("loc_35E3")


    ChrTalk(
        0xFE,
        (
            "It's an honor to work at this Orchis\x01",
            "Tower, that has attracted attention\x01",
            "from all over the continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We won't be satisfied with the cutting\x01",
            "edge security this building is provides,\x01",
            "so we'll do our duty the best we can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36C9")

    TalkEnd(0xFE)
    Return()

    # Function_14_2BD6 end

    def Function_15_36CD(): pass

    label("Function_15_36CD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3756")

    ChrTalk(
        0xFE,
        (
            "If that happened to the\x01",
            "President, what's going\x01",
            "to become of Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Well, whatever\x01",
            "happens, happens.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41FD")

    label("loc_3756")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3764")
    Jump("loc_41FD")

    label("loc_3764")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3772")
    Jump("loc_41FD")

    label("loc_3772")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3947")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38B3")

    ChrTalk(
        0xFE,
        (
            "When the attack hit, I was able\x01",
            "to take refuge in basement from\x01",
            "the finance section floor, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "None of us were able to\x01",
            "use the elevators. The\x01",
            "young men used the stairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, the finance\x01",
            "section is on 31F.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I was so short of\x01",
            "breath, I thought I was\x01",
            "going to die.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3942")

    label("loc_38B3")


    ChrTalk(
        0xFE,
        (
            "I never thought I'd have\x01",
            "to run down the stairs of\x01",
            "this skyscraper, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How to say this...\x01",
            "Regular fitness training\x01",
            "is important.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3942")

    Jump("loc_41FD")

    label("loc_3947")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3AFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A4E")

    ChrTalk(
        0xFE,
        (
            "A war between a jaeger\x01",
            "group and the CGF, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yet another unnecessary expense on\x01",
            "the pile... Err, this is no time\x01",
            "to be saying stuff like that, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I pray to the\x01",
            "Goddess that the situation\x01",
            "is concluded quickly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3AF5")

    label("loc_3A4E")


    ChrTalk(
        0xFE,
        (
            "Man. I give up, with all these\x01",
            "major incidents occurring one\x01",
            "after the next recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I pray to the\x01",
            "Goddess that the situation\x01",
            "is concluded quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AF5")

    Jump("loc_41FD")

    label("loc_3AFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3B08")
    Jump("loc_41FD")

    label("loc_3B08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3C97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BFC")

    ChrTalk(
        0xFE,
        (
            "I don't really get it,\x01",
            "but they said the trains\x01",
            "have stopped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Stopping the aorta of the\x01",
            "continental economy... That's\x01",
            "a joke that just isn't funny.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It'll be a huge problem\x01",
            "if it's not restored\x01",
            "quickly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3C92")

    label("loc_3BFC")


    ChrTalk(
        0xFE,
        (
            "Stopping the aorta of the\x01",
            "continental economy... That's\x01",
            "a joke that just isn't funny.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It'll be a huge problem\x01",
            "if it's not restored\x01",
            "quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C92")

    Jump("loc_41FD")

    label("loc_3C97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3D6D")

    ChrTalk(
        0xFE,
        (
            "Mayor Dieter pays his entertainment\x01",
            "and travel expenses not with public\x01",
            "funds, but with his own money.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's the IBC president for\x01",
            "you... In his case, that goes\x01",
            "beyond just being generous.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41FD")

    label("loc_3D6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4014")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F36")

    ChrTalk(
        0xFE,
        (
            "Crossbell becoming a nation,\x01",
            "huh... I can't believe Mayor Crois\x01",
            "put forward a plan this bold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm in the Finance Division, so I\x01",
            "understand vexing problems\x01",
            "regarding tax revenue assignment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, even just putting\x01",
            "dependent state-related\x01",
            "problems into words is taboo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected, the major\x01",
            "powers put out statements\x01",
            "in opposition...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't help but be\x01",
            "worried about what they'll\x01",
            "both do in the future.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_400F")

    label("loc_3F36")


    ChrTalk(
        0xFE,
        (
            "They said in the end, the referendum\x01",
            "is to question the people's will to\x01",
            "be independent, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In any case, the major powers surely\x01",
            "won't look kindly upon it. I'm worried\x01",
            "about their actions going forward.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_400F")

    Jump("loc_41FD")

    label("loc_4014")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4022")
    Jump("loc_41FD")

    label("loc_4022")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_41FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4138")

    ChrTalk(
        0xFE,
        (
            "Wow. To think Orchis\x01",
            "Tower is finally\x01",
            "completed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How magnanimous of Mayor\x01",
            "Dieter to invest IBC's funds\x01",
            "in public works projects.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's quite the different from some\x01",
            "zealous congressmen who look only to\x01",
            "enriching their own pockets, eh?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_41FD")

    label("loc_4138")


    ChrTalk(
        0xFE,
        (
            "How magnanimous of Mayor\x01",
            "Dieter to invest IBC's funds\x01",
            "in public works projects.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's quite the different from some\x01",
            "zealous congressmen who look only to\x01",
            "enriching their own pockets, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41FD")

    TalkEnd(0xFE)
    Return()

    # Function_15_36CD end

    def Function_16_4201(): pass

    label("Function_16_4201")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_438C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42FB")

    ChrTalk(
        0xFE,
        (
            "So "Orchis Tower"\x01",
            "finally showed its form\x01",
            "to the citizens...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Its majesty touches even the\x01",
            "sky, and its blue and white\x01",
            "exterior is indeed beautiful...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm really glad I\x01",
            "undertook the job of\x01",
            "designing it...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4387")

    label("loc_42FB")


    ChrTalk(
        0xFE,
        (
            "The difficulty of designing a\x01",
            "building that stretches 40F above\x01",
            "ground is hard to grasp, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Hmm... My eyes are\x01",
            "burning up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4387")

    Jump("loc_4395")

    label("loc_438C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4395")

    label("loc_4395")

    TalkEnd(0xFE)
    Return()

    # Function_16_4201 end

    def Function_17_4399(): pass

    label("Function_17_4399")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43AE")
    Call(0, 21)
    Jump("loc_4422")

    label("loc_43AE")


    ChrTalk(
        0xFE,
        (
            "Oh yeah, I wonder if\x01",
            "KeA's all right...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On the department store\x01",
            "roof, she seemed kind of\x01",
            "weird, though...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4422")

    TalkEnd(0xFE)
    Return()

    # Function_17_4399 end

    def Function_18_4426(): pass

    label("Function_18_4426")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_443B")
    Call(0, 21)
    Jump("loc_44D4")

    label("loc_443B")


    ChrTalk(
        0xFE,
        (
            "Shing's way of speaking is\x01",
            "self-important, but he's a\x01",
            "good guy at his core.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's going home tomorrow,\x01",
            "so we've got to play\x01",
            "while we still can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44D4")

    TalkEnd(0xFE)
    Return()

    # Function_18_4426 end

    def Function_19_44D8(): pass

    label("Function_19_44D8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44ED")
    Call(0, 21)
    Jump("loc_455D")

    label("loc_44ED")


    ChrTalk(
        0xFE,
        (
            "Even so, Orchis Tower...\x01",
            "It's even cooler than I\x01",
            "imagined.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If possible, I'd like to\x01",
            "try going inside.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_455D")

    TalkEnd(0xFE)
    Return()

    # Function_19_44D8 end

    def Function_20_4561(): pass

    label("Function_20_4561")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4576")
    Call(0, 21)
    Jump("loc_45FA")

    label("loc_4576")


    ChrTalk(
        0xFE,
        (
            "H-Hmph... This is why\x01",
            "the masses trouble me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway... For the sake of\x01",
            "my brilliant future, I must\x01",
            "properly observe them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45FA")

    TalkEnd(0xFE)
    Return()

    # Function_20_4561 end

    def Function_21_45FE(): pass

    label("Function_21_45FE")

    OP_4B(0x1E, 0xFF)
    OP_4B(0x1B, 0xFF)
    OP_4B(0x1C, 0xFF)
    OP_4B(0x1D, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4784")

    ChrTalk(
        0x101,
        "#00005FOh, if it isn't Shing.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x101, 500)

    ChrTalk(
        0x1E,
        (
            "Ah... You're the guys\x01",
            "from yesterday!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x102, 500)

    ChrTalk(
        0x1E,
        "Elie, hello!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FHaha, hello. Are Ryｹ and\x01",
            "Henri with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Yes, that's right. They\x01",
            "wanted to come no matter\x01",
            "what, so I had no choice...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x1E, 500)

    ChrTalk(
        0x1B,
        "What are you saying?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "You said you were lonely\x01",
            "because KeA and Shizuku\x01",
            "left, so we joined you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B94")

    label("loc_4784")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A00")

    ChrTalk(
        0x101,
        (
            "#00005FHuh? Is that true,\x01",
            "Shing?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x101, 500)

    ChrTalk(
        0x1E,
        (
            "Ah... You're the guys\x01",
            "from yesterday!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "You refused the request\x01",
            "to show me around.\x01",
            "What's up with that!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FSorry, Shing. We just\x01",
            "didn't have time, you\x01",
            "see...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x102, 500)

    ChrTalk(
        0x1E,
        (
            "Shut up. It's not like I\x01",
            "attacked you, Elie...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "...Hmph, whatever. A subordinate gave\x01",
            "me a tour that wasn't that interesting,\x01",
            "but I was able to see the whole city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FEven so, you're with\x01",
            "those lads today, huh.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x104, 500)

    ChrTalk(
        0x1B,
        (
            "Yeah. We saw the unveiling on\x01",
            "the department store roof, and\x01",
            "now we're playing together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "He said it'd be lonely\x01",
            "alone, so we joined him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B94")

    label("loc_4A00")


    ChrTalk(
        0x101,
        (
            "#00002FHey, if it isn't Ryｹ and\x01",
            "Henri.\x02\x03",
            "#00005F...Huh? There's a kid\x01",
            "I'm not used to seeing?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x0, 500)

    ChrTalk(
        0x1E,
        (
            "What's with you guys? Do\x01",
            "you know Ryｹ and Henri?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "Listen up, I'm Hei─\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x0, 500)

    ChrTalk(
        0x1B,
        (
            "Well, I don't really get\x01",
            "it, but he's visiting\x01",
            "from the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "We saw the unveiling on the\x01",
            "department store roof, and\x01",
            "now we're playing together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "He said it'd be lonely\x01",
            "alone, so we joined him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B94")

    TurnDirection(0x1E, 0x1B, 500)

    ChrTalk(
        0x1E,
        (
            "W-Who was lonely? Stop\x01",
            "making things up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Ah, but you did! Right\x01",
            "Momo? Didn't he?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x1D, 500)

    ChrTalk(
        0x1D,
        "U-Umm, you see...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x1B, 500)

    ChrTalk(
        0x1C,
        (
            "H-Hey, Ryｹ! Stop making\x01",
            "fun of him!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4C96")

    ChrTalk(
        0x101,
        (
            "#00002F(Haha. Looks like\x01",
            "they're already friends,\x01",
            "somehow.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CD1")

    label("loc_4C96")


    ChrTalk(
        0x101,
        (
            "#00002F(Haha, looks like\x01",
            "they're getting along\x01",
            "well.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CD1")

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

    # Function_21_45FE end

    def Function_22_4D01(): pass

    label("Function_22_4D01")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4D9F")

    ChrTalk(
        0xFE,
        (
            "There's no sign of\x01",
            "terrorists right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't think they'll come from\x01",
            "the front, but... Anyway, we've\x01",
            "got to keep up our guard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E32")

    label("loc_4D9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4E32")

    ChrTalk(
        0xFE,
        (
            "Hey, good afternoon.\x01",
            "Isn't this plaza such a\x01",
            "nice place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's no mistake that\x01",
            "it'll become one of\x01",
            "Crossbell's famous places.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E32")

    TalkEnd(0xFE)
    Return()

    # Function_22_4D01 end

    def Function_23_4E36(): pass

    label("Function_23_4E36")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4ED8")

    ChrTalk(
        0xFE,
        (
            "Today, all day, Orchis\x01",
            "Tower is restricted to\x01",
            "authorized personnel only.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You guys are the Special\x01",
            "Support Section, right?\x01",
            "Please pass.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F5E")

    label("loc_4ED8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4F5E")

    ChrTalk(
        0xFE,
        "Welcome to Orchis Tower.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You're free to come and go from\x01",
            "this plaza as you please, so\x01",
            "please feel free to stop by.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F5E")

    TalkEnd(0xFE)
    Return()

    # Function_23_4E36 end

    def Function_24_4F62(): pass

    label("Function_24_4F62")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Good work, everyone.\x01",
            "Nothing out of the\x01",
            "ordinary in the plaza.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_4F62 end

    def Function_25_4FAD(): pass

    label("Function_25_4FAD")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "*sigh*. Finally, the\x01",
            "opening of the main\x01",
            "session.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm getting a little\x01",
            "nervous, but... I've got\x01",
            "to relax.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_4FAD end

    def Function_26_5028(): pass

    label("Function_26_5028")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "L-Listen up. When greeting\x01",
            "the heads of state, smile\x01",
            "and don't be rude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And if we're careless,\x01",
            "our heads will get blown\x01",
            "off in an instant.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_5028 end

    def Function_27_50C4(): pass

    label("Function_27_50C4")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "C-Chief. We know that\x01",
            "already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please don't pressure\x01",
            "your subordinates so\x01",
            "hard.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_50C4 end

    def Function_28_5125(): pass

    label("Function_28_5125")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5585")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5143")
    Call(0, 30)
    Jump("loc_5580")

    label("loc_5143")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54DE")

    ChrTalk(
        0x11,
        (
            "#07902FEveryone... And Randy,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FHey Mireille. It looks\x01",
            "like you've returned to\x01",
            "your unit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#07904FYes, thanks to you.\x02\x03",
            "#07902FThe commander gladly\x01",
            "accepted us, a unit that\x01",
            "disobeyed orders...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_52D2")

    ChrTalk(
        0x109,
        (
            "#10100FHaha. That's just how\x01",
            "Commander Sonya would deal\x01",
            "with that.\x02\x03",
            "With this situation, she'd\x01",
            "want an outstanding officer\x01",
            "like you, even alone...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5366")

    label("loc_52D2")


    ChrTalk(
        0x103,
        (
            "#00204FA flexible approach,\x01",
            "typical of Commander Sonya.\x02\x03",
            "#00202FWith this situation, she'd\x01",
            "want an outstanding officer\x01",
            "like you, even alone...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5366")


    ChrTalk(
        0x11,
        (
            "#07904FHaha. I don't know if I'm\x01",
            "outstanding, but...\x02\x03",
            "#07902FNow that I'm back, I plan to\x01",
            "give this everything I've\x01",
            "got.\x02\x03",
            "As one with a duty to protect\x01",
            "Crossbell rather than a State\x01",
            "Guard soldier or CGF member.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FDo your best, Mireille.\x02\x03",
            "#00309FWell, don't get too\x01",
            "fired up and spin your\x01",
            "wheels.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#07906FI-I know that already!\x01",
            "...Ugh, stupid Randy!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AE, 2)
    Jump("loc_5580")

    label("loc_54DE")


    ChrTalk(
        0x11,
        (
            "#07902FNow that I'm back, I plan to\x01",
            "give this everything I've\x01",
            "got.\x02\x03",
            "As one with a duty to protect\x01",
            "Crossbell rather than a State\x01",
            "Guard soldier or CGF member.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5580")

    Jump("loc_562C")

    label("loc_5585")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_562C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55A0")
    Call(0, 45)
    Jump("loc_562C")

    label("loc_55A0")


    ChrTalk(
        0x11,
        (
            "#07903FAfter we've organized\x01",
            "the unit, we'll come\x01",
            "rushing after you too.\x02\x03",
            "#07901FSo everyone... Please\x01",
            "take care of that idiot\x01",
            "for me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_562C")

    TalkEnd(0xFE)
    Return()

    # Function_28_5125 end

    def Function_29_5630(): pass

    label("Function_29_5630")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5645")
    Call(0, 30)
    Jump("loc_5B69")

    label("loc_5645")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_597B")

    ChrTalk(
        0x22,
        (
            "#02501FThe impact of Dieter's arrest will soon spread\x01",
            "both within and outside the state.\x02\x03",
            "Even if we manage to get this situation under\x01",
            "control, many difficulties await Crossbell\x01",
            "going forward.\x02\x03",
            "#02503F...Perhaps Crossbell's future was too heavy a\x01",
            "burden for Dieter to bear.\x02\x03",
            "As a state representative, I wonder if there\x01",
            "was anything I could have done to prevent this.\x01",
            "...I am keenly aware of my powerlessness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108FGrandfather...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...I think this incident\x01",
            "is a problem for all of\x01",
            "Crossbell.\x02\x03",
            "#00000FWhat should we do\x01",
            "now...? That's the most\x01",
            "important thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "#02503F...Yes, exactly right.\x02\x03",
            "#02500FAnyway, what we need to do now is\x01",
            "solve the problems before us, one-\x01",
            "by-one.\x02\x03",
            "I've foisted terrible hardships on\x01",
            "you youngsters, but... Please,\x01",
            "lend me your strength for a while.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AE, 3)
    Jump("loc_5B69")

    label("loc_597B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AA3")

    ChrTalk(
        0x22,
        (
            "#02503FAnyway, what we need to do now is\x01",
            "solve the problems before us, one-\x01",
            "by-one.\x02\x03",
            "#02500FAs a Crossbell state\x01",
            "representative, I must settle this\x01",
            "issue, no matter what.\x02\x03",
            "I've foisted terrible hardships on\x01",
            "you youngsters, but... Please,\x01",
            "lend me your strength for a while.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5B69")

    label("loc_5AA3")


    ChrTalk(
        0x22,
        (
            "#02503FAnyway, what we need to do now is\x01",
            "solve the problems before us, one-\x01",
            "by-one.\x02\x03",
            "#02500FI've foisted terrible hardships on\x01",
            "you youngsters, but... Please,\x01",
            "lend me your strength for a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B69")

    TalkEnd(0xFE)
    Return()

    # Function_29_5630 end

    def Function_30_5B6D(): pass

    label("Function_30_5B6D")

    OP_4B(0x22, 0xFF)
    OP_4B(0x21, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_4B(0x23, 0xFF)

    ChrTalk(
        0x22,
        (
            "#02503FRumors of Dieter's arrest are\x01",
            "already spreading within and\x01",
            "outside the state.\x02\x03",
            "#02500FWe can't let down our guard against\x01",
            "the major powers... How is the\x01",
            "situation throughout Crossbell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "As we thought, the\x01",
            "appearance of that Huge Tree\x01",
            "is causing chaos everywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "And because the barrier is down,\x01",
            "a great many citizens are\x01",
            "heading for St. Ursula Hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "I've directed 2nd Lt.\x01",
            "Mireille to deal with\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#07903FOutside the city, I've deployed platoons\x01",
            "on each of the highways and increased the\x01",
            "number of armored cars.\x02\x03",
            "#07900FBecause the President's restrictions are\x01",
            "no longer in effect, it's possible we'll\x01",
            "be transporting more citizens than normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "#02503FYes, thanks for your quick response.\x02\x03",
            "#02500FAs for me, as Chairman of state\x01",
            "Congress, I need to explain the\x01",
            "President's arrest in a public place.\x02\x03",
            "Preparations are already being made\x01",
            "at City Meeting Hall, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "#01002FRegarding that, I think we'll\x01",
            "be able to use the screen\x01",
            "cars the President prepared.\x02\x03",
            "The police in the city can\x01",
            "divide things up and get them\x01",
            "ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "#02503FThanks for taking care of\x01",
            "that.\x02\x03",
            "#02501FWe must stay on guard against\x01",
            "the major powers... Ladies and\x01",
            "gentlemen, please be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F(It looks like Chairman MacDowell\x01",
            "and the others are dealing with\x01",
            "problems throughout Crossbell.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(It should be fine if we\x01",
            "leave this to my grandfather\x01",
            "and the others.)\x02",
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

    # Function_30_5B6D end

    def Function_31_6123(): pass

    label("Function_31_6123")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6138")
    Call(0, 30)
    Jump("loc_66A6")

    label("loc_6138")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64B0")

    ChrTalk(
        0x23,
        (
            "#01002FYou guys, huh... What,\x01",
            "did something happen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FNo, I was just wondering\x01",
            "about the situation\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "#01003FWell, as you can see, we're\x01",
            "discussing how to deal with the\x01",
            "problems throughout Crossbell.\x02\x03",
            "#01001FI'm here as a police liaison.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6293")

    ChrTalk(
        0x10A,
        (
            "#00604FHmm... You're certainly\x01",
            "qualified, Sergei.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62C9")

    label("loc_6293")


    ChrTalk(
        0x103,
        (
            "#00204FI see. You're certainly\x01",
            "qualified, Chief.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62C9")


    ChrTalk(
        0x104,
        (
            "#00300FThen... The Support\x01",
            "Section's unoccupied, huh.\x01",
            "Have any requests come in?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "#01002FA lot of 'em from all\x01",
            "over the place. We passed\x01",
            "them to the guild.\x02\x03",
            "#01004FYou guys have no need to\x01",
            "worry about requests, do\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FIf the guild is handling\x01",
            "them, that's fine with\x01",
            "us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "#01004FAnyway, go and do your\x01",
            "own thing until you're\x01",
            "satisfied...\x02\x03",
            "#01002FAs the "Special Support\x01",
            "Section"... But most of\x01",
            "all, as yourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FRight!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AE, 4)
    Jump("loc_66A6")

    label("loc_64B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65FF")

    ChrTalk(
        0x23,
        (
            "#01003F...By the way, the President is being held in\x01",
            "a room on 36F.\x02\x03",
            "Because of the situation, I've called off his\x01",
            "guard. It doesn't seem like he's resisting,\x01",
            "so we've placed him under minimum security.\x02\x03",
            "#01002FWell, if you feel like it, you can go see\x01",
            "him. He'll probably tell you the same thing\x01",
            "again, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_66A6")

    label("loc_65FF")


    ChrTalk(
        0x23,
        (
            "#01003FThe President is being held in a\x01",
            "room on 36F.\x02\x03",
            "#01002FWell, if you feel like it, you can\x01",
            "go see him. He'll probably tell\x01",
            "you the same thing again, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66A6")

    TalkEnd(0xFE)
    Return()

    # Function_31_6123 end

    def Function_32_66AA(): pass

    label("Function_32_66AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66BF")
    Call(0, 30)
    Jump("loc_6BC8")

    label("loc_66BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A1C")

    ChrTalk(
        0x104,
        (
            "#00300FYou're here, old man\x01",
            "Douglas.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_672A")

    ChrTalk(
        0x109,
        (
            "#10100FGood work, Vice\x01",
            "Commander!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_672A")


    ChrTalk(
        0xFE,
        (
            "You guys, huh. Haha,\x01",
            "it's been a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Commander Sonya asked me\x01",
            "to come as the State\x01",
            "Guard representative.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FSo that's how it is, huh.\x02\x03",
            "#00000FEven so, those clothes...\x01",
            "So that's the uniform of\x01",
            "the State Guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. They look a little\x01",
            "more formal than the CGF\x01",
            "ones.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We'll be acting like this\x01",
            "until the situation's\x01",
            "calmed down a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F...It looks like the\x01",
            "situation's really bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah... Now that we've lost the barrier over\x01",
            "the city as well as those Aions, we've got\x01",
            "to be on guard against the major powers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Well, I don't think any\x01",
            "invasions are imminent, so\x01",
            "you just leave that to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You guys should do what\x01",
            "only you guys can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWe will... And thanks\x01",
            "for all your help.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AE, 5)
    Jump("loc_6BC8")

    label("loc_6A1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B3D")

    ChrTalk(
        0xFE,
        (
            "Ever since we got wind of the\x01",
            "President's arrest, the commander\x01",
            "sometimes looks like she's thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...She has a deep sense of responsibility.\x01",
            "Most likely she's thinking about things,\x01",
            "her own actions included.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As Vice Commander, I\x01",
            "must support her fully.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6BC8")

    label("loc_6B3D")


    ChrTalk(
        0xFE,
        (
            "I don't think the major powers\x01",
            "will invade immediately, so\x01",
            "you just leave them to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You guys should do what\x01",
            "only you guys can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BC8")

    TalkEnd(0xFE)
    Return()

    # Function_32_66AA end

    def Function_33_6BCC(): pass

    label("Function_33_6BCC")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D7E")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C42")

    ChrTalk(
        0x109,
        "#10105FUmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FThe Support Section's\x01",
            "car... It was moved\x01",
            "here, huh.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C8A")

    label("loc_6C42")


    ChrTalk(
        0x101,
        (
            "#00005FAh...\x02\x03",
            "The Support Section's\x01",
            "car... It was moved\x01",
            "here, huh.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C8A")


    ChrTalk(
        0x102,
        (
            "#00106FHow sad... With this\x01",
            "situation, we'll have to leave\x01",
            "it like this for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWell, it is because of\x01",
            "this situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FOnce it's under control,\x01",
            "I'm sure we'll repair\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, that's right.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AE, 6)
    Jump("loc_6E67")

    label("loc_6D7E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E03")

    ChrTalk(
        0x109,
        (
            "#10100FOne this situation's\x01",
            "over, I'm sure we'll\x01",
            "repair it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah... It was of great\x01",
            "use to us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E67")

    label("loc_6E03")


    ChrTalk(
        0x101,
        (
            "#00000FOne this situation's\x01",
            "over, I'm sure we'll\x01",
            "repair it.\x02\x03",
            "#00004FIt was of great use to\x01",
            "us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E67")

    TalkEnd(0xFF)
    Return()

    # Function_33_6BCC end

    def Function_34_6E6B(): pass

    label("Function_34_6E6B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6E7C")
    Jump("loc_7219")

    label("loc_6E7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6F73")

    ChrTalk(
        0xFE,
        (
            "My daughter and I were\x01",
            "in the plaza when the\x01",
            "attack hit...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When they told me to\x01",
            "shelter in the building, I\x01",
            "felt we were already dead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm really thankful to Arios\x01",
            "and everyone else who defended\x01",
            "this place to the last.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7219")

    label("loc_6F73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6FFD")

    ChrTalk(
        0xFE,
        (
            "With such nice weather\x01",
            "today, it's sad to hear of\x01",
            "an occupation incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder just why this\x01",
            "had to happen...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7219")

    label("loc_6FFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_700B")
    Jump("loc_7219")

    label("loc_700B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7071")

    ChrTalk(
        0xFE,
        (
            "Now then, it's about\x01",
            "time for lunch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I'll have this\x01",
            "sandwich I brought.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7219")

    label("loc_7071")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_70D7")

    ChrTalk(
        0xFE,
        (
            "Haha, nice weather we're\x01",
            "having today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Orchis Tower shines in\x01",
            "this clear sky.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7219")

    label("loc_70D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_716A")

    ChrTalk(
        0xFE,
        (
            "Haha. I knew this plaza\x01",
            "would be a nice place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though it's far from the\x01",
            "business district, I thought\x01",
            "I'd make my way here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7219")

    label("loc_716A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7178")
    Jump("loc_7219")

    label("loc_7178")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7219")

    ChrTalk(
        0xFE,
        (
            "Haha. You wouldn't think\x01",
            "they just held the\x01",
            "unveiling ceremony here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mayor Dieter is generous,\x01",
            "opening a nice place like\x01",
            "this on opening day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7219")

    TalkEnd(0xFE)
    Return()

    # Function_34_6E6B end

    def Function_35_721D(): pass

    label("Function_35_721D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_722E")
    Jump("loc_742D")

    label("loc_722E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_729D")

    ChrTalk(
        0xFE,
        (
            "They said Arios and the\x01",
            "police are gonna protect\x01",
            "us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm very, very grateful\x01",
            "to them♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_742D")

    label("loc_729D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_72E2")

    ChrTalk(
        0xFE,
        (
            "Mom looks sad today. I\x01",
            "wish she would cheer\x01",
            "up...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_742D")

    label("loc_72E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_72F0")
    Jump("loc_742D")

    label("loc_72F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_731B")

    ChrTalk(
        0xFE,
        "Meal, meal, noon meal♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_742D")

    label("loc_731B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7365")

    ChrTalk(
        0xFE,
        (
            "Weather, weather, good\x01",
            "weather♪ Rain, rain, go\x01",
            "away♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_742D")

    label("loc_7365")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_73B2")

    ChrTalk(
        0xFE,
        (
            "Ehehe, I came here\x01",
            "walking with my mom\x01",
            "today. Hm-hm-hmm♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_742D")

    label("loc_73B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_73C0")
    Jump("loc_742D")

    label("loc_73C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_742D")

    ChrTalk(
        0xFE,
        (
            "My neck hurts when I try\x01",
            "to look at the top of\x01",
            "Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ouchie, ouch, ouch,\x01",
            "ouchie♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_742D")

    TalkEnd(0xFE)
    Return()

    # Function_35_721D end

    def Function_36_7431(): pass

    label("Function_36_7431")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "...*sigh*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Only sighs will come\x01",
            "out.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_36_7431 end

    def Function_37_746C(): pass

    label("Function_37_746C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Hmm. I guess there's no\x01",
            "way to express it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe "dumbfounded" is\x01",
            "the word.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_37_746C end

    def Function_38_74C9(): pass

    label("Function_38_74C9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_756B")

    ChrTalk(
        0xFE,
        (
            "They say something\x01",
            "terrible's happened at\x01",
            "Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't really get it, but...\x01",
            "Maybe I should head home\x01",
            "before I get wrapped up in it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76D8")

    label("loc_756B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7579")
    Jump("loc_76D8")

    label("loc_7579")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_75CB")

    ChrTalk(
        0xFE,
        (
            "Now then, it's about\x01",
            "time I headed back to\x01",
            "the city for lunch.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76D8")

    label("loc_75CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_764F")

    ChrTalk(
        0xFE,
        (
            "The Orchis Tower roof\x01",
            "isn't yet open to the\x01",
            "general public.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aww, too bad. I'll have\x01",
            "to come again sometime.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76D8")

    label("loc_764F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_76D8")

    ChrTalk(
        0xFE,
        (
            "I came to see the rumored\x01",
            "Orchis Tower... It's more\x01",
            "amazing than I imagined.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just how much money does\x01",
            "Crossbell have?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76D8")

    TalkEnd(0xFE)
    Return()

    # Function_38_74C9 end

    def Function_39_76DC(): pass

    label("Function_39_76DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7774")

    ChrTalk(
        0xFE,
        (
            "She's a member of the\x01",
            "Crossbell Guardian\x01",
            "Force, isn't she.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's quite beautiful...\x01",
            "I wonder if she has a\x01",
            "weapon and fights.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7876")

    label("loc_7774")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7782")
    Jump("loc_7876")

    label("loc_7782")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_77F5")

    ChrTalk(
        0xFE,
        (
            "Come to think of it, I'm\x01",
            "hungry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. Somehow, you lose\x01",
            "track of time when you\x01",
            "come here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7876")

    label("loc_77F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_782D")

    ChrTalk(
        0xFE,
        (
            "Aww. They postponed\x01",
            "rooftop viewing!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7876")

    label("loc_782D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7876")

    ChrTalk(
        0xFE,
        (
            "Wow! I knew its grandeur\x01",
            "would be different from\x01",
            "up close.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7876")

    TalkEnd(0xFE)
    Return()

    # Function_39_76DC end

    def Function_40_787A(): pass

    label("Function_40_787A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Hmm. With this rain, I\x01",
            "can't see the top\x01",
            "clearly.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_40_787A end

    def Function_41_78B8(): pass

    label("Function_41_78B8")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "And after I came all the\x01",
            "way here. Oh, why did it\x01",
            "have to rain!?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_41_78B8 end

    def Function_42_7905(): pass

    label("Function_42_7905")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Haha. Looking at it\x01",
            "again, it really is\x01",
            "unthinkable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's nothing to compare it\x01",
            "to. It can't be compared to\x01",
            "the Tetracyclic Towers, huh.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_42_7905 end

    def Function_43_79A2(): pass

    label("Function_43_79A2")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The presence of Orchis Tower is so\x01",
            "overwhelming that, even if I can't\x01",
            "see it with my eyes, I can feel it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With IBC destroyed, it\x01",
            "is a new symbol of the\x01",
            "city they protected...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. In the end, I\x01",
            "suppose it's just a\x01",
            "coincidence?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_43_79A2 end

    def Function_44_7A9B(): pass

    label("Function_44_7A9B")

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
        "#12P#00005FThis is...\x02",
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
            "#12P#00301FThose State Guard guys\x01",
            "are tightly securin'\x01",
            "Orchis Tower, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108FThis is where "uncle" declared\x01",
            "independence. This level of\x01",
            "security is only natural.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_63(0x62, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_4B(0x62, 0x1)

    ChrTalk(
        0x62,
        "Huh, you're... Randy?\x02",
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
            "#00305F#12PCould you be Carter?\x02\x03",
            "#00302FHaha, I didn't recognize\x01",
            "you in that white\x01",
            "uniform.\x02\x03",
            "Weren't you stationed at\x01",
            "Bellguard Gate before?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x62,
        (
            "Yeah. Some of us were called\x01",
            "from the border gates coincident\x01",
            "with the President's address.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x62,
        (
            "Loggins is patrolling\x01",
            "over there.\x02",
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
        "#00000F#12P(He's...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#6P(Looks like he's Randy's\x01",
            "colleague from when he\x01",
            "was in the CGF.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x62,
        (
            "Ah, but it was really\x01",
            "difficult, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x62,
        (
            "We were surprised at\x01",
            "first, having suddenly\x01",
            "been given these uniforms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12PYeah. It was too sudden and you\x01",
            "didn't know what was going on...\x02\x03",
            "#00300FThinking about it again, the\x01",
            "President seemed a little too\x01",
            "prepared for this, uniforms aside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x62,
        (
            "I'm sure the President\x01",
            "has been preparing for\x01",
            "this for a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x62,
        (
            "He promised to improve the\x01",
            "State Guard's equipment too,\x01",
            "so we've got to stay focused.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F#12PR-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#12P(...It looks like the State\x01",
            "Guard soldiers view this\x01",
            "reorganization favorably.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6P(Having been compared to the\x01",
            "armies of other nations, I\x01",
            "understand how they feel, but...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x62,
        (
            "By the way, when we became the\x01",
            "State Guard, it was decided we'll\x01",
            "use normal military rank names.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x62,
        (
            "We were called Captain [ichii], 1st Lt.\x01",
            "[nii], 2nd Lt. [san'i], but now it's Captain\x01",
            "[taii],1st Lt. [chｹi], 2nd Lt. [shｷi].\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x62,
        (
            "It's rude if we get it wrong\x01",
            "when addressing an officer,\x01",
            "so we'll have to be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F#12PYeah, thanks for the warning.\x02\x03",
            "#00303FThen, because that Mireille\x01",
            "was a 2nd Lt. [san'i]... She's\x01",
            "now a 2nd Lt. [shｷi], huh.\x02\x03",
            "#00309FHaha, that's a new way to make\x01",
            "fun of her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#12PHey now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x62,
        (
            "U-Umm... Well, that's\x01",
            "how it is I guess.\x02",
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
            "#00305F#12PWhat's with that half-\x01",
            "baked response...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F#12PThat's how to address\x01",
            "her, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x62,
        "No, that's not it...\x02",
    )

    CloseMessageWindow()
    OP_63(0x62, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x62)

    ChrTalk(
        0x62,
        "Umm, Randy, you see...\x02",
    )

    CloseMessageWindow()
    OP_4B(0x6A, 0x1)
    TurnDirection(0x6A, 0x62, 500)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("State Guard Officer's Voice")

    ChrTalk(
        0x6A,
        (
            "#4SCarter!! Use some\x01",
            "discretion while on\x01",
            "duty!!\x02",
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
        "...Y-Yes, sir!!\x02",
    )

    CloseMessageWindow()
    OP_4C(0x6A, 0x1)
    TurnDirection(0x62, 0x104, 300)

    ChrTalk(
        0x62,
        (
            "...Sorry, Randy. I'll\x01",
            "give you the details\x01",
            "next time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F#12PI don't get it, but...\x01",
            "I'm sorry too for\x01",
            "talking so long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x62,
        (
            "Haha, don't worry about\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x62,
        (
            "Oh yeah, you police will\x01",
            "be joining the State\x01",
            "Guard, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x62,
        (
            "We'll be colleagues from\x01",
            "here on out. Good to be\x01",
            "working with you.\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x62, -3160, 0, -12800, 2000, 0x0)
    OP_93(0x62, 0xB4, 0x12C)
    OP_4C(0x62, 0x1)

    ChrTalk(
        0x104,
        (
            "#00306F#12PMan... Another thing to\x01",
            "worry about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#12PWe should leave for now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#12PYeah, let's go.\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_68(0, 2770, -13870, 5000)
    MoveCamera(0, 7, 0, 5000)
    OP_6E(750, 5000)
    SetCameraDistance(19000, 5000)

    def lambda_8AA6():

        label("loc_8AA6")

        TurnDirection(0x62, 0x104, 500)
        Yield()
        Jump("loc_8AA6")

    QueueWorkItem2(0x62, 2, lambda_8AA6)
    OP_93(0x101, 0xB4, 0x1F4)

    def lambda_8ABF():

        label("loc_8ABF")

        OP_9B(0x0, 0x101, 0x0, 0x2710, 0x7D0, 0x0)
        Yield()
        Jump("loc_8ABF")

    QueueWorkItem2(0x101, 1, lambda_8ABF)
    OP_93(0x104, 0xB4, 0x1F4)

    def lambda_8AE0():

        label("loc_8AE0")

        OP_9B(0x0, 0x104, 0x0, 0x2710, 0x7D0, 0x0)
        Yield()
        Jump("loc_8AE0")

    QueueWorkItem2(0x104, 1, lambda_8AE0)
    OP_93(0x103, 0xB4, 0x1F4)

    def lambda_8B01():

        label("loc_8B01")

        OP_9B(0x0, 0x103, 0x0, 0x2710, 0x7D0, 0x0)
        Yield()
        Jump("loc_8B01")

    QueueWorkItem2(0x103, 1, lambda_8B01)
    OP_93(0x102, 0xB4, 0x1F4)

    def lambda_8B22():

        label("loc_8B22")

        OP_9B(0x0, 0x102, 0x0, 0x2710, 0x7D0, 0x0)
        Yield()
        Jump("loc_8B22")

    QueueWorkItem2(0x102, 1, lambda_8B22)
    OP_0D()
    SetScenarioFlags(0x191, 4)
    EventEnd(0x6)
    NewScene("c1100", 108, 0, 0)
    IdleLoop()
    Return()

    # Function_44_7A9B end

    def Function_45_8B47(): pass

    label("Function_45_8B47")

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
            "#6P#00001FLt. Mireille... You came\x01",
            "to the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#07903FYes, I just got here.\x02\x03",
            "#07900FThe Commander and Vice\x01",
            "Commander are having a\x01",
            "series of meetings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FChief participated in\x01",
            "one of them last night\x01",
            "as well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00201FIf the CGF commander and the others are\x01",
            "still here, it means the countermeasures\x01",
            "aren't progressing smoothly.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x11)

    ChrTalk(
        0x11,
        (
            "#07901F...Guys. We heard from\x01",
            "your chief this morning,\x01",
            "but...\x02\x03",
            "He said Randy\x01",
            "disappeared?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F...Yes.\x02\x03",
            "#00001FHe's most likely heading\x01",
            "for Mainz Mountain Path\x01",
            "as we speak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#07908F...I see...\x02",
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x11)

    ChrTalk(
        0x105,
        "#6P#10300F...Are you ok?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#07903FYes, I'm fine. More\x01",
            "importantly...\x02\x03",
            "#07901FRandy's disappearance is\x01",
            "related to his past...\x01",
            "Don't you think so?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00008FT-That's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#07908F...It's hard for me to say\x01",
            "this, but I don't know that\x01",
            "much about Randy's past.\x02\x03",
            "Even now, I don't even know\x01",
            "the reason Randy doesn't use\x01",
            "a rifle in combat training.\x02\x03",
            "#07901FBut... I understand his was\x01",
            "an act of true stupidity that\x01",
            "greatly worried all of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10108FLt. Mireille...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FIndeed. It goes beyond\x01",
            "stupidity, to utter\x01",
            "foolishness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#07903F...The CGF has sustained serious damage as\x01",
            "well. I think the commanders have decided\x01",
            "to put together another relief force.\x02\x03",
            "We can't do anything until then... We\x01",
            "can't accelerate our deployment for Randy\x01",
            "alone.\x02\x03",
            "#07900FSo everyone... Please take care of that\x01",
            "idiot for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FLeave it to us. We'll\x01",
            "definitely save Randy!\x02",
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

    # Function_45_8B47 end

    def Function_46_91EC(): pass

    label("Function_46_91EC")

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
            "The West Zemuria Trade Conference─\x02\x03",
            "An international conference proposed by new\x01",
            "Mayor Dieter Crois was to be held, and to which\x01",
            "the heads of state of each country were invited.\x07\x00\x02",
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
            "At the same time, the new City Hall\x01",
            "building would be unveiled.\x02\x03",
            "─Popularly known as "Orchis Tower".\x02\x03",
            "At 40 floors and 250 arge tall, the\x01",
            "continent's first skyscraper was even now\x01",
            "attracting the attention of its people.\x07\x00\x02",
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

    # Function_46_91EC end

    def Function_47_97A9(): pass

    label("Function_47_97A9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_97F5")
    OP_95(0xFE, 21700, 300, -6000, 2000, 0x0)
    Sleep(1000)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_95(0xFE, 21700, 300, 19000, 2000, 0x0)
    Sleep(1000)
    OP_93(0xFE, 0xB4, 0x1F4)
    Jump("Function_47_97A9")

    label("loc_97F5")

    Return()

    # Function_47_97A9 end

    def Function_48_97F6(): pass

    label("Function_48_97F6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9842")
    OP_95(0xFE, -21700, 300, 19000, 2000, 0x0)
    Sleep(1000)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_95(0xFE, -21700, 300, -6000, 2000, 0x0)
    Sleep(1000)
    OP_93(0xFE, 0x0, 0x1F4)
    Jump("Function_48_97F6")

    label("loc_9842")

    Return()

    # Function_48_97F6 end

    def Function_49_9843(): pass

    label("Function_49_9843")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_988F")
    OP_95(0xFE, -7000, 0, 5500, 2000, 0x0)
    Sleep(1000)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_95(0xFE, -19000, 0, 5500, 2000, 0x0)
    Sleep(1000)
    OP_93(0xFE, 0x5A, 0x1F4)
    Jump("Function_49_9843")

    label("loc_988F")

    Return()

    # Function_49_9843 end

    def Function_50_9890(): pass

    label("Function_50_9890")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_98DC")
    OP_95(0xFE, 7000, 0, 5500, 2000, 0x0)
    Sleep(1000)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_95(0xFE, 19000, 0, 5500, 2000, 0x0)
    Sleep(1000)
    OP_93(0xFE, 0x10E, 0x1F4)
    Jump("Function_50_9890")

    label("loc_98DC")

    Return()

    # Function_50_9890 end

    def Function_51_98DD(): pass

    label("Function_51_98DD")

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

    def lambda_9FC6():
        OP_98(0xFE, 0x0, 0x0, 0xEA60, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x71, 1, lambda_9FC6)
    BeginChrThread(0x79, 1, 0, 55)
    FadeToBright(2000, 0)
    Sleep(3000)
    ClearMapObjFlags(0xB, 0x4)

    def lambda_9FF8():
        OP_98(0xFE, 0x0, 0x0, 0xD6D8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x72, 1, lambda_9FF8)
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

    def lambda_A121():
        TurnDirection(0xFE, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x30, 2, lambda_A121)
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

    def lambda_A1D3():
        TurnDirection(0xFE, 0x2D, 500)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_A1D3)
    OP_68(-1000, 1000, 6200, 2500)
    MoveCamera(9, 27, 0, 2500)
    SetCameraDistance(13500, 2500)
    OP_6F(0x79)
    Sleep(500)

    def lambda_A20A():
        TurnDirection(0xFE, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x30, 2, lambda_A20A)
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

    def lambda_A2BB():
        TurnDirection(0xFE, 0x27, 500)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_A2BB)
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
        "#11P#00011F(A-Amazing...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#5P(Yes... It really is\x01",
            "nothing but heads of\x01",
            "state.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#5P(But that Blood and Iron\x01",
            "Chancellor... He's\x01",
            "certainly well built.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#11P#10302F(Hehe. The Calvardian\x01",
            "President seems more\x01",
            "like a raccoon dog.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#10102F(Liberl's Crown Princess\x01",
            "Klaudia is gorgeous...)\x02\x03",
            "#10109F(...and to see Captain\x01",
            "Julia in person!)\x02",
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

    def lambda_A501():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_A501)

    def lambda_A50E():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x2F, 2, lambda_A50E)

    def lambda_A51B():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_A51B)

    def lambda_A528():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_A528)

    def lambda_A535():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_A535)

    def lambda_A542():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_A542)

    def lambda_A54F():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_A54F)

    def lambda_A55C():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_A55C)
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
            "#02804F#5P─Heads of state.\x02\x03",
            "#02800FCrossbell welcomes you\x01",
            "after your long\x01",
            "journeys.\x02\x03",
            "I am Crossbell City\x01",
            "Mayor Dieter Crois.\x02",
        )
    )

    CloseMessageWindow()
    Sound(968, 0, 70, 0)
    Sleep(2500)

    ChrTalk(
        0x30,
        (
            "#02804F#5PI would like to thank each of you for\x01",
            "agreeing to participate in the West\x01",
            "Zemuria Trade Conference.\x02\x03",
            "Normally I would declare the\x01",
            "conference officially open in addition\x01",
            "to welcoming all of you, but...\x02\x03",
            "#02800FBefore that, to commemorate this\x01",
            "auspicious day, I would like a moment\x01",
            "of your time.\x02",
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

    def lambda_A7A7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_A7A7)

    def lambda_A7B4():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_A7B4)
    Sleep(50)

    def lambda_A7C4():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_A7C4)

    def lambda_A7D1():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2F, 2, lambda_A7D1)
    Sleep(50)

    def lambda_A7E1():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_A7E1)

    def lambda_A7EE():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_A7EE)
    Sleep(50)

    def lambda_A7FE():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_A7FE)

    def lambda_A80B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_A80B)
    Sleep(50)

    def lambda_A81B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_A81B)

    def lambda_A828():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x5A, 2, lambda_A828)
    Sleep(50)

    def lambda_A838():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x31, 2, lambda_A838)

    def lambda_A845():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_A845)

    def lambda_A852():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x5B, 2, lambda_A852)
    WaitChrThread(0x31, 2)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x30,
        (
            "#02803F#N#11P─Allow me to introduce...\x02\x03",
            "Crossbell City's new City Hall.\x02\x03",
            "A new landmark that symbolizes\x01",
            "Crossbell's dedication to trade and\x01",
            "finance.\x02\x03",
            "#02800FAnd above all, an international\x01",
            "exchange center for the advancement\x01",
            "of peace throughout the continent.\x02\x03",
            "I unveil to you the continent's\x01",
            "first-ever skyscraper─\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x30,
        "#02809F#N#4S#11POrchis Tower!!\x02",
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
            "#00011F#NT-This is... Orchis\x01",
            "Tower!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00102F#NI read about it, but to\x01",
            "think it would be this\x01",
            "spectacular...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x109,
        (
            "#6P#10111F#NJ-Just looking at it is\x01",
            "overwhelming...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00306F#NIt's insane... How much\x01",
            "mira did this thing\x01",
            "cost?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#12P#10302F#NHehe, they must've been\x01",
            "sinking mira into this\x01",
            "thing for an eternity.\x02",
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
            "#07205F#11P(Dear me! I'm\x01",
            "dumbfounded.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "#07303F#5P(Technological progress\x01",
            "is a terrifying\x01",
            "thing...)\x02",
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
            "#07000F#5P(It almost reminds you\x01",
            "of the Liber Ark.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2C,
        (
            "#07104F#5P(Yes... Though it's not\x01",
            "quite as tall as the\x01",
            "central axis pillar was.)\x02",
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
            "#07511F#5P(Ha ha ha! How\x01",
            "splendid!)\x02\x03",
            "#07510F(I received your report,\x01",
            "but I still can't\x01",
            "believe it!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "#12004F#11P(I can scarcely believe\x01",
            "it myself.)\x02\x03",
            "#12000F(To think IBC has this\x01",
            "much capital.)\x02",
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
            "#07404F#11P(Haha, truly great.)\x02\x03",
            "#07400F(To think such a large\x01",
            "temple was built in this\x01",
            "place of connections.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#11509F#11P(Hmm. I'd like to visit\x01",
            "the roof.)\x02\x03",
            "#11502F(You think he'll let us\x01",
            "if we ask?)\x02",
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

    def lambda_B241():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x31, 2, lambda_B241)

    def lambda_B24E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_B24E)

    def lambda_B25B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x5B, 2, lambda_B25B)
    Sleep(50)

    def lambda_B26B():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_B26B)

    def lambda_B278():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x2F, 2, lambda_B278)
    Sleep(50)

    def lambda_B288():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_B288)

    def lambda_B295():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_B295)
    Sleep(50)

    def lambda_B2A5():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_B2A5)

    def lambda_B2B2():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_B2B2)
    Sleep(50)

    def lambda_B2C2():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_B2C2)

    def lambda_B2CF():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_B2CF)
    Sleep(50)

    def lambda_B2DF():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_B2DF)

    def lambda_B2EC():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x5A, 2, lambda_B2EC)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x30,
        (
            "#02804F─Now then, let's try\x01",
            "this again.\x02\x03",
            "With the heads of state\x01",
            "and their respective\x01",
            "staffs as witnesses─\x02\x03",
            "#02800FI declare the opening of\x01",
            "the West Zemuria Trade\x01",
            "Conference!\x02",
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

    # Function_51_98DD end

    def Function_52_B3F6(): pass

    label("Function_52_B3F6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B4AE")
    Sound(810, 0, 80, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B461")
    Sleep(500)
    Jump("loc_B4A9")

    label("loc_B461")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B478")
    Sleep(1000)
    Jump("loc_B4A9")

    label("loc_B478")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B48F")
    Sleep(150)
    Jump("loc_B4A9")

    label("loc_B48F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B4A6")
    Sleep(2000)
    Jump("loc_B4A9")

    label("loc_B4A6")

    Sleep(2500)

    label("loc_B4A9")

    Jump("Function_52_B3F6")

    label("loc_B4AE")

    Return()

    # Function_52_B3F6 end

    def Function_53_B4AF(): pass

    label("Function_53_B4AF")

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

    # Function_53_B4AF end

    def Function_54_B62D(): pass

    label("Function_54_B62D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B652")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(4000)
    Jump("Function_54_B62D")

    label("loc_B652")

    Return()

    # Function_54_B62D end

    def Function_55_B653(): pass

    label("Function_55_B653")

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

    # Function_55_B653 end

    def Function_56_B6AE(): pass

    label("Function_56_B6AE")

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
            "#00000FHaha, it sure is\x01",
            "crowded.\x02\x03",
            "It looks like Ryｹ and\x01",
            "Henri stopped by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FAfter the unveiling ceremony, this\x01",
            "plaza was opened to the public not\x01",
            "long after the heads of state left.\x02\x03",
            "#00104FHaha. I guess it's because "uncle"\x01",
            "is so considerate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FAhaha, that's a very\x01",
            "Mayor Dieter thing to\x01",
            "do.\x02\x03",
            "#10100FBut there are a lot of\x01",
            "officers here too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#4PWell, the whole city is\x01",
            "lively right now.\x02\x03",
            "#10300FTrouble could occur\x01",
            "easily, so shouldn't\x01",
            "there be more police?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah. It looks like the\x01",
            "tower interior is\x01",
            "closed.\x02\x03",
            "#00000FFor the time being,\x01",
            "let's refrain from going\x01",
            "inside.\x02",
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

    # Function_56_B6AE end

    def Function_57_BB30(): pass

    label("Function_57_BB30")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FIt looks like the tower\x01",
            "interior is closed to\x01",
            "the public today.\x02\x03",
            "For the time being,\x01",
            "let's refrain from going\x01",
            "inside.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 0, 0, 25470, 180)
    EventEnd(0x4)
    Return()

    # Function_57_BB30 end

    def Function_58_BBCB(): pass

    label("Function_58_BBCB")

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

    def lambda_BC93():
        OP_97(0x105, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_BC93)
    Sleep(100)

    def lambda_BCB0():
        OP_97(0x109, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_BCB0)
    Sleep(100)

    def lambda_BCCD():
        OP_97(0x103, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BCCD)
    Sleep(100)

    def lambda_BCEA():
        OP_97(0x104, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BCEA)
    Sleep(100)

    def lambda_BD07():
        OP_97(0x101, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BD07)
    Sleep(100)

    def lambda_BD24():
        OP_97(0x102, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BD24)
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
            "#00206F#11PI saw this building's lights\x01",
            "before I arrived at the\x01",
            "airport last night, but...\x02\x03",
            "#00202FLooking up at it from this\x01",
            "close, it's impossibly big.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F#11PHaha... I feel you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102F#5PI feel like it's\x01",
            "Crossbell's new\x01",
            "landmark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5PBut how are they gonna\x01",
            "use such a huge\x01",
            "building?\x02\x03",
            "#00301FIf you compare it to the\x01",
            "old city hall, it's way\x01",
            "too big.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#5PWell, I think it will include various\x01",
            "facilities.\x02\x03",
            "#00100FIn addition to city and state\x01",
            "administration, it has floors for\x01",
            "international trade and cultural exchange.\x02\x03",
            "It's almost like it was built to be the\x01",
            "center of West Zemuria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#5PWow... They sure talk a\x01",
            "big game.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F#5PBut when you think of it\x01",
            "that way, this trade\x01",
            "conference makes sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11PWith the completion of this building,\x01",
            "the concentration of funds and info in\x01",
            "Crossbell will accelerate even more.\x02\x03",
            "#10300FI wonder if they're planning on\x01",
            "discussing future agreements based on\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#5PYes, that's what I've\x01",
            "heard.\x02\x03",
            "#00108FI might not be strictly\x01",
            "limited to economic\x01",
            "talks, though.\x02",
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
            "#00003F#11P─So, what do we do?\x02\x03",
            "#00001FWe'll be meeting up with\x01",
            "Detective Dudley on 1F\x01",
            "at noon, though.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C2AA():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_C2AA)
    Sleep(50)

    def lambda_C2BA():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_C2BA)
    Sleep(50)

    def lambda_C2CA():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_C2CA)
    Sleep(50)

    def lambda_C2DA():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C2DA)
    Sleep(50)

    def lambda_C2EA():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_C2EA)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7B, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C36F")

    ChrTalk(
        0x102,
        (
            "#00108F#5PThat's right... We still\x01",
            "have some time, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C3B3")

    label("loc_C36F")


    ChrTalk(
        0x102,
        (
            "#00105F#5PThat's right... We still\x01",
            "have a lot of time,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C3B3")


    ChrTalk(
        0x104,
        (
            "#6P#00304FAnyway, let's take care\x01",
            "of any business or\x01",
            "preparations before then.\x02\x03",
            "#00300FWe don't want to be in a\x01",
            "bind if something does\x01",
            "happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FThat's right... It's not like\x01",
            "we'll be able to leave the\x01",
            "conference once it starts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00202FLet's enter the building\x01",
            "once we've taken care of our\x01",
            "business and preparations.\x02",
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

    # Function_58_BBCB end

    def Function_59_C550(): pass

    label("Function_59_C550")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7B, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C6A4")

    ChrTalk(
        0x101,
        (
            "#00003F#5P(We're meeting up with\x01",
            "Detective Dudley on 1F\x01",
            "at noon...)\x02\x03",
            "#00001F(There's still time.\x01",
            "Should we head inside?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C730")

    label("loc_C6A4")


    ChrTalk(
        0x101,
        (
            "#00003F#5P(We're meeting up with\x01",
            "Detective Dudley on 1F\x01",
            "at noon...)\x02\x03",
            "#00001F(There's still a lot of\x01",
            "time left. Should we\x01",
            "head inside?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C730")

    FadeToDark(300, 0, 100)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Upon entering Orchis Tower,\x01",
            "you will be unable to adjust\x01",
            "equipment, items or orbments.\x02\x03",
            "Also, please note that all\x01",
            "remaining quests will close\x01",
            "as well.\x07\x00\x02",
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
            "[We Have Other Things to Do]\x01",      # 0
            "[Enter the Tower]\x01",                 # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_C859"),
        (0, "loc_C97B"),
        (SWITCH_DEFAULT, "loc_C9A5"),
    )


    label("loc_C859")

    OP_68(0, 1500, 30500, 4000)
    MoveCamera(0, 7, 0, 4000)

    def lambda_C87A():
        OP_97(0x101, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C87A)
    Sleep(50)

    def lambda_C897():
        OP_97(0x103, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_C897)
    Sleep(50)

    def lambda_C8B4():
        OP_97(0x102, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_C8B4)
    Sleep(50)

    def lambda_C8D1():
        OP_97(0x104, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_C8D1)
    Sleep(50)

    def lambda_C8EE():
        OP_97(0x109, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C8EE)
    Sleep(50)

    def lambda_C90B():
        OP_97(0x105, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_C90B)
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
    Jump("loc_C9A5")

    label("loc_C97B")

    SetChrPos(0x0, 0, 0, 24500, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jump("loc_C9A5")

    label("loc_C9A5")

    EventEnd(0x5)
    Return()

    # Function_59_C550 end

    def Function_60_C9A8(): pass

    label("Function_60_C9A8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(1000)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "The day of the referendum on "Crossbell\x01",
            "State independence" proposed by Mayor\x01",
            "Dieter drew near.\x02\x03",
            "Though pressure from the Imperial and\x01",
            "Republican governments grew day by day, so\x01",
            "too did citizen interest in the matter.\x02\x03",
            "Together with the opening of the Arc-en-\x01",
            "Ciel renewal performance, emotions in the\x01",
            "city ran ever hotter.\x02\x03",
            "─Amongst all of that, a new problem was\x01",
            "flaring up in secret in the outskirts.\x02",
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

    # Function_60_C9A8 end

    def Function_61_CC93(): pass

    label("Function_61_CC93")

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
            "#11PBut, to think we'd get\x01",
            "to work with you guys on\x01",
            "something like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x33,
        (
            "#11PHmm. I never could have\x01",
            "imagined it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00012FHaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FWell, we've also grown\x01",
            "quite a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x32,
        (
            "#11PYeah, you guys are a big\x01",
            "deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x32,
        (
            "#11PIf you guys ever get fired\x01",
            "by the police, you're\x01",
            "welcome to join us anytime!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x35,
        "#11PYeah, yeah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x35,
        (
            "#11PEspecially Tio. You'd\x01",
            "fit in the guild\x01",
            "perfectly!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x35, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#6P#00211FEven if you say that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FHaha... Thank you for\x01",
            "your kind words.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FBut Cryptids, huh...\x01",
            "That's quite concerning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x32,
        (
            "#11PRight. Let's split up\x01",
            "for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x32,
        (
            "#11PThe CGF has told us\x01",
            "about five of them in\x01",
            "total.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x32,
        (
            "#11PI'd like you guys to\x01",
            "take care of two of\x01",
            "them.\x02",
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
            "#10302FWow, that's awfully\x01",
            "generous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FAre you sure? You guys\x01",
            "have more of them...\x02\x03",
            "#00001FAnd Arios can't assist\x01",
            "you as it is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x34,
        "#11PThat's exactly why.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x34,
        (
            "#11PHe can't help, so we\x01",
            "have to shift his share\x01",
            "to you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x35,
        (
            "#11PFrom the start, monster\x01",
            "extermination is a\x01",
            "bracer's specialty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x35,
        (
            "#11PWe both have other work to\x01",
            "do too, so this is the\x01",
            "best way to divide things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104F...Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10108FT-This doesn't sit well\x01",
            "with me somehow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x32,
        (
            "#11PWhat? We're in this\x01",
            "together!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x32,
        (
            "#11PThere's the problem of\x01",
            "Ouroboros you guys have\x01",
            "to deal with too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00006F...Right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FDamn... I forgot about\x01",
            "'em.\x02",
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
            "#00203FThe secret society of\x01",
            "Ouroboros...\x02\x03",
            "#00201FI understand they have\x01",
            "some connection with the\x01",
            "Bracer Guild?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(40, 200, -1, -1)

    AnonymousTalk(
        0x35,
        (
            "Yes. Estelle and other\x01",
            "bracers first opposed them\x01",
            "in the Liberl incident...\x02\x03",
            "Since then, we've\x01",
            "encountered them countless\x01",
            "times.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(230, 140, -1, -1)

    AnonymousTalk(
        0x33,
        (
            "...And the disappearance of guild\x01",
            "branches in the Empire is thought\x01",
            "to be their doing as well.\x02\x03",
            "After that, our influence there\x01",
            "continued to decline due to\x01",
            "pressure by the Imperial army.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 190, -1, -1)

    AnonymousTalk(
        0x101,
        "#00001FIs that right.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(100, 210, -1, -1)

    AnonymousTalk(
        0x104,
        (
            "#00301FBut, it seems like the\x01",
            "more we learn about 'em,\x01",
            "the less we know.\x02",
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
            "#11PIn any case, even the guild\x01",
            "hasn't yet learned the true\x01",
            "nature of their organization.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x32,
        (
            "#11PWe don't know what their\x01",
            "goal is. Be extra\x01",
            "careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x34,
        (
            "#11PDon't hesitate to call\x01",
            "us if you get into\x01",
            "trouble, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x34,
        (
            "#11PTo be perfectly honest,\x01",
            "those guys are our\x01",
            "problem too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002F...Understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FWe'll call you if\x01",
            "anything happens.\x02",
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

    # Function_61_CC93 end

    def Function_62_DAC0(): pass

    label("Function_62_DAC0")


    def lambda_DAC5():
        OP_97(0x32, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x32, 0, lambda_DAC5)
    Sleep(50)

    def lambda_DAE2():
        OP_97(0x34, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 0, lambda_DAE2)
    Sleep(50)

    def lambda_DAFF():
        OP_97(0x33, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 0, lambda_DAFF)
    Sleep(50)

    def lambda_DB1C():
        OP_97(0x35, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 0, lambda_DB1C)

    def lambda_DB36():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x32, 2, lambda_DB36)
    Sleep(100)

    def lambda_DB4A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x34, 2, lambda_DB4A)
    Sleep(400)

    def lambda_DB5E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x33, 2, lambda_DB5E)
    Sleep(100)

    def lambda_DB72():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x35, 2, lambda_DB72)
    Return()

    # Function_62_DAC0 end

    def Function_63_DB7F(): pass

    label("Function_63_DB7F")


    def lambda_DB84():
        OP_97(0x101, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_DB84)
    Sleep(50)

    def lambda_DBA1():
        OP_97(0x102, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_DBA1)
    Sleep(50)

    def lambda_DBBE():
        OP_97(0x103, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_DBBE)
    Sleep(50)

    def lambda_DBDB():
        OP_97(0x104, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_DBDB)
    Sleep(50)

    def lambda_DBF8():
        OP_97(0x109, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_DBF8)
    Sleep(50)

    def lambda_DC15():
        OP_97(0x105, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_DC15)

    def lambda_DC2F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DC2F)
    Sleep(100)

    def lambda_DC43():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_DC43)
    Sleep(400)

    def lambda_DC57():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_DC57)
    Sleep(100)

    def lambda_DC6B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_DC6B)
    Sleep(400)

    def lambda_DC7F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_DC7F)
    Sleep(100)

    def lambda_DC93():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_DC93)
    Return()

    # Function_63_DB7F end

    def Function_64_DCA0(): pass

    label("Function_64_DCA0")

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
            "─Good day, everyone.\x02\x03",
            "At this time I address you as\x01",
            "Dieter Crois, founding President\x01",
            "of the "Independent State of\x02\x03",
            "Crossbell".\x02",
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

    # Function_64_DCA0 end

    def Function_65_E3F0(): pass

    label("Function_65_E3F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E4A8")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E41E")
    Sleep(500)
    Jump("loc_E466")

    label("loc_E41E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E435")
    Sleep(1000)
    Jump("loc_E466")

    label("loc_E435")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E44C")
    Sleep(1500)
    Jump("loc_E466")

    label("loc_E44C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E463")
    Sleep(2000)
    Jump("loc_E466")

    label("loc_E463")

    Sleep(2500)

    label("loc_E466")

    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(810, 0, 70, 0)
    Jump("Function_65_E3F0")

    label("loc_E4A8")

    Return()

    # Function_65_E3F0 end

    def Function_66_E4A9(): pass

    label("Function_66_E4A9")

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
            "#11303F#6P─It is for these reasons that\x01",
            "I've assumed the office of\x01",
            "President today.\x02\x03",
            "#11300FThis is only a temporary measure\x01",
            "for dealing with the imminent\x01",
            "threats, of course.\x02\x03",
            "#11304FI promise you here and now that\x01",
            "the people will hold an election\x01",
            "once peace has returned.\x02",
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
            "#11303F#11PThere's someone else, too...\x02\x03",
            "#11300FHe is someone you all know well,\x01",
            "and will help create this new\x01",
            "Independent State of Crossbell.\x02",
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
            "#11304F#5PLet me introduce him─\x02\x03",
            "The character who defended\x01",
            "Orchis Tower to the last in the\x01",
            "recent attack...\x02\x03",
            "#11300FKnown as the Divine Blade of\x01",
            "Wind and former A-Rank bracer,\x01",
            "Crossbell branch, I give you...\x02\x03",
            "#11309FCrossbell State Guard\x01",
            "Commander-in-Chief, Arios\x01",
            "MacLaine!\x02",
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
            "#4084V─I am Arios MacLaine, as\x01",
            "introduced.\x02\x03",
            "#4085VI am still inexperienced, and for\x01",
            "this reason there may be some of\x01",
            "you who are uneasy.\x02\x03",
            "#4086VHowever, I do promise to work even\x01",
            "harder than I did as a bracer to\x01",
            "repel whatever threats face us.\x02\x03",
            "#4087VAs the shield that protects\x01",
            "Crossbell...\x02\x03",
            "#4088VAnd, as the sword that destroys\x01",
            "all enemies who threaten justice\x01",
            "or peace!\x02",
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

    # Function_66_E4A9 end

    def Function_67_F082(): pass

    label("Function_67_F082")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_96(0xFE, 0x3E8, 0x2904, 0x88B8, 0x3E8, 0x0)
    Return()

    # Function_67_F082 end

    def Function_68_F09E(): pass

    label("Function_68_F09E")

    OP_95(0xFE, 0, 10380, 35600, 1500, 0x0)
    OP_95(0xFE, 0, 10500, 35000, 1500, 0x0)
    Return()

    # Function_68_F09E end

    def Function_69_F0C7(): pass

    label("Function_69_F0C7")

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

    # Function_69_F0C7 end

    def Function_70_F1D5(): pass

    label("Function_70_F1D5")

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
    OP_8E(0x2F, "Kilika")
    OP_8E(0x28, "Lechter")
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

    def lambda_FBB2():
        OP_93(0xFE, 0xC8, 0x1F4)
        ExitThread()

    QueueWorkItem(0x40, 2, lambda_FBB2)
    Sleep(500)

    def lambda_FBC2():
        OP_93(0xFE, 0xC8, 0x1F4)
        ExitThread()

    QueueWorkItem(0x43, 2, lambda_FBC2)
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

    def lambda_FDF8():
        TurnDirection(0xFE, 0x3E, 500)
        ExitThread()

    QueueWorkItem(0x3C, 2, lambda_FDF8)

    def lambda_FE05():
        OP_96(0xFE, 0x1CE8, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3C, 1, lambda_FE05)
    Sleep(50)
    EndChrThread(0x48, 0x1)
    SetChrChipByIndex(0x48, 0x13)
    SetChrSubChip(0x48, 0x0)
    OP_63(0x48, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_FE40():
        TurnDirection(0xFE, 0x3E, 500)
        ExitThread()

    QueueWorkItem(0x48, 2, lambda_FE40)

    def lambda_FE4D():
        OP_96(0xFE, 0x17D4, 0x32, 0xFFFFF95C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x48, 1, lambda_FE4D)
    Sleep(50)
    EndChrThread(0x38, 0x1)
    EndChrThread(0x79, 0x0)
    SetChrChipByIndex(0x38, 0xF)
    SetChrSubChip(0x38, 0x0)
    OP_63(0x38, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_FE8C():
        TurnDirection(0xFE, 0x3E, 500)
        ExitThread()

    QueueWorkItem(0x38, 2, lambda_FE8C)
    Sleep(50)
    OP_63(0x3A, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_FEAE():
        TurnDirection(0xFE, 0x3E, 500)
        ExitThread()

    QueueWorkItem(0x3A, 2, lambda_FEAE)
    Sleep(50)

    ChrTalk(
        0x3C,
        "Whaaat!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x38,
        "Eeeek!!\x02",
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

    def lambda_FFE8():
        OP_A6(0xFE, 0x0, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_FFE8)

    def lambda_10001():
        OP_9B(0x1, 0xFE, 0xB4, 0x384, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3E, 1, lambda_10001)
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
        "#11507F#5PThe next one's yours!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        "#03404F─Right.\x02",
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

    def lambda_1028E():
        OP_A6(0xFE, 0x0, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3F, 2, lambda_1028E)

    def lambda_102A7():
        OP_9B(0x1, 0xFE, 0xB4, 0x384, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_102A7)
    BeginChrThread(0x2F, 3, 0, 104)
    WaitChrThread(0x2F, 3)
    EndChrThread(0x4A, 0x1)
    SetChrChipByIndex(0x4A, 0x13)
    SetChrSubChip(0x4A, 0x0)
    OP_93(0x4A, 0x0, 0x1F4)

    ChrTalk(
        0x3B,
        "A-Amazing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "#5P#N#01005FI'd expect nothing less\x01",
            "from the Crimson\x01",
            "Swallow...\x02",
        )
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
            "#11PKilika! I'll help you\x01",
            "out!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2F, 0x34, 500)
    BeginChrThread(0x3E, 3, 0, 92)

    ChrTalk(
        0x2F,
        (
            "#6P#03402FAlright. We'll show them\x01",
            "the power of the Taito\x01",
            "style.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x34,
        "#11PRight!\x02",
    )

    CloseMessageWindow()

    def lambda_104C3():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2F, 2, lambda_104C3)
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
            "#11P#11509FMy, my. They really\x01",
            "stand out.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x28, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x28,
        (
            "#11P#11502FAllow me to make things\x01",
            "a bit easier for you.\x02",
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
        "#01003F#11PGood timing...\x02",
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
            "#01007F#4S#11P─Special Support\x01",
            "Section, now!!\x02\x03",
            "The "path" is open! The\x01",
            "rest is up to you!\x02",
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
            "#4SRoger!\x07\x00\x02",
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

    # Function_70_F1D5 end

    def Function_71_10B5A(): pass

    label("Function_71_10B5A")


    def lambda_10B5F():
        OP_95(0xFE, 5400, 100, -1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10B5F)

    def lambda_10B79():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10B79)
    WaitChrThread(0xFE, 1)

    def lambda_10B8E():
        OP_95(0xFE, 3100, 250, -1700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10B8E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    SetChrChipByIndex(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0x38, 1, 0, 123)
    BeginChrThread(0x79, 0, 0, 127)
    Return()

    # Function_71_10B5A end

    def Function_72_10BC3(): pass

    label("Function_72_10BC3")


    def lambda_10BC8():
        OP_95(0xFE, 5400, 100, -1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10BC8)

    def lambda_10BE2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10BE2)
    WaitChrThread(0xFE, 1)

    def lambda_10BF7():
        OP_95(0xFE, 6100, 50, -700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10BF7)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0x48, 1, 0, 123)
    Return()

    # Function_72_10BC3 end

    def Function_73_10C26(): pass

    label("Function_73_10C26")


    def lambda_10C2B():
        OP_95(0xFE, 5400, 100, -1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10C2B)

    def lambda_10C45():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10C45)
    WaitChrThread(0xFE, 1)

    def lambda_10C5A():
        OP_95(0xFE, 7400, 0, -500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10C5A)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0x3C, 1, 0, 123)
    Return()

    # Function_73_10C26 end

    def Function_74_10C89(): pass

    label("Function_74_10C89")


    def lambda_10C8E():
        OP_95(0xFE, -5400, 100, -1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10C8E)

    def lambda_10CA8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10CA8)
    WaitChrThread(0xFE, 1)

    def lambda_10CBD():
        OP_95(0xFE, -3100, 250, -1700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10CBD)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0x49, 1, 0, 123)
    Return()

    # Function_74_10C89 end

    def Function_75_10CEC(): pass

    label("Function_75_10CEC")


    def lambda_10CF1():
        OP_95(0xFE, -5400, 100, -1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10CF1)

    def lambda_10D0B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10D0B)
    WaitChrThread(0xFE, 1)

    def lambda_10D20():
        OP_95(0xFE, -6100, 50, -700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10D20)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)

    ChrTalk(
        0x39,
        "#5PCommencing attack!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Return()

    # Function_75_10CEC end

    def Function_76_10D5F(): pass

    label("Function_76_10D5F")


    def lambda_10D64():
        OP_95(0xFE, -5400, 100, -1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10D64)

    def lambda_10D7E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10D7E)
    WaitChrThread(0xFE, 1)

    def lambda_10D93():
        OP_95(0xFE, -7400, 0, -500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10D93)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0x4A, 1, 0, 123)
    BeginChrThread(0x79, 1, 0, 128)
    Return()

    # Function_76_10D5F end

    def Function_77_10DC8(): pass

    label("Function_77_10DC8")


    def lambda_10DCD():
        OP_95(0xFE, -5400, 100, -1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10DCD)

    def lambda_10DE7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10DE7)
    WaitChrThread(0xFE, 1)

    def lambda_10DFC():
        OP_95(0xFE, -6400, 0, -3000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10DFC)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_77_10DC8 end

    def Function_78_10E1D(): pass

    label("Function_78_10E1D")


    def lambda_10E22():
        OP_95(0xFE, 5400, 100, -1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10E22)

    def lambda_10E3C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10E3C)
    WaitChrThread(0xFE, 1)

    def lambda_10E51():
        OP_95(0xFE, 4400, 0, -2200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10E51)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_AD(0x9)

    ChrTalk(
        0x3A,
        "Use the cars as shields!\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_78_10E1D end

    def Function_79_10E93(): pass

    label("Function_79_10E93")

    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)

    def lambda_10EA0():
        OP_95(0xFE, -5400, 100, -1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10EA0)

    def lambda_10EBA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10EBA)
    WaitChrThread(0xFE, 1)

    def lambda_10ECF():
        OP_95(0xFE, -2000, 250, -1600, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10ECF)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    SetChrChipByIndex(0xFE, 0xD)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0x23, 1, 0, 124)
    BeginChrThread(0x79, 2, 0, 130)
    Return()

    # Function_79_10E93 end

    def Function_80_10F04(): pass

    label("Function_80_10F04")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_110AA")
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
    Jump("Function_80_10F04")

    label("loc_110AA")

    Return()

    # Function_80_10F04 end

    def Function_81_110AB(): pass

    label("Function_81_110AB")

    Sleep(300)

    label("loc_110AE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11254")
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
    Jump("loc_110AE")

    label("loc_11254")

    Return()

    # Function_81_110AB end

    def Function_82_11255(): pass

    label("Function_82_11255")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_113FB")
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
    Jump("Function_82_11255")

    label("loc_113FB")

    Return()

    # Function_82_11255 end

    def Function_83_113FC(): pass

    label("Function_83_113FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11446")
    PlayEffect(0x5, 0xFF, 0xFE, 0x0, 0, 1600, -500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(900)
    Jump("Function_83_113FC")

    label("loc_11446")

    Return()

    # Function_83_113FC end

    def Function_84_11447(): pass

    label("Function_84_11447")

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

    # Function_84_11447 end

    def Function_85_11496(): pass

    label("Function_85_11496")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0xA)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 9)

    def lambda_114BD():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_114BD)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x20)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 8)
    Return()

    # Function_85_11496 end

    def Function_86_114F9(): pass

    label("Function_86_114F9")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0xA)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 9)

    def lambda_11520():
        OP_95(0xFE, -2200, 100, 5300, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11520)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x20)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 8)
    Return()

    # Function_86_114F9 end

    def Function_87_1155C(): pass

    label("Function_87_1155C")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0xA)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 9)

    def lambda_11583():
        OP_95(0xFE, 2000, 100, 5800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11583)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x20)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 8)
    Return()

    # Function_87_1155C end

    def Function_88_115BF(): pass

    label("Function_88_115BF")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(630)
    SetChrSubChip(0xFE, 0x1)
    Sleep(130)

    def lambda_115E5():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_115E5)
    Sleep(1000)
    SetChrSubChip(0xFE, 0x2)
    Sleep(1000)
    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 8)
    Return()

    # Function_88_115BF end

    def Function_89_1161D(): pass

    label("Function_89_1161D")

    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1163D():
        OP_A6(0xFE, 0x0, 0x64, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_1163D)
    Sleep(1000)
    Sound(985, 0, 80, 0)
    PlayEffect(0x1, 0xFF, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_11699():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_11699)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_89_1161D end

    def Function_90_116AA(): pass

    label("Function_90_116AA")

    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xFE, 7300, 250, 4300, 225)
    Sound(985, 0, 100, 0)
    PlayEffect(0x0, 0x1, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_11713():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_11713)
    WaitChrThread(0xFE, 2)
    StopEffect(0x1, 0x2)
    Sleep(130)
    SetChrSubChip(0x3E, 0x1)
    Sleep(130)

    def lambda_11735():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_11735)
    Sleep(1000)
    Sound(951, 0, 100, 0)
    SetChrSubChip(0xFE, 0x2)
    SetChrFlags(0xFE, 0x20)

    def lambda_11760():
        OP_9B(0x1, 0xFE, 0x0, 0x2BC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11760)
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

    # Function_90_116AA end

    def Function_91_11880(): pass

    label("Function_91_11880")

    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 8)
    SetChrPos(0xFE, -7300, 250, 4300, 135)
    Sound(985, 0, 100, 0)
    PlayEffect(0x0, 0x2, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_118EF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_118EF)
    WaitChrThread(0xFE, 2)
    StopEffect(0x2, 0x2)
    Return()

    # Function_91_11880 end

    def Function_92_11903(): pass

    label("Function_92_11903")

    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 8)
    SetChrPos(0xFE, -12800, 0, 8300, 135)
    Sound(985, 0, 100, 0)
    PlayEffect(0x0, 0x1, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_11972():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_11972)
    WaitChrThread(0xFE, 2)
    StopEffect(0x1, 0x2)
    Return()

    # Function_92_11903 end

    def Function_93_11986(): pass

    label("Function_93_11986")

    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 8)
    SetChrPos(0xFE, 8300, 0, 15000, 180)
    Sound(985, 0, 70, 0)
    PlayEffect(0x0, 0x2, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_119F5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_119F5)
    WaitChrThread(0xFE, 2)
    StopEffect(0x2, 0x2)
    Return()

    # Function_93_11986 end

    def Function_94_11A09(): pass

    label("Function_94_11A09")


    def lambda_11A0E():
        OP_95(0xFE, 800, 100, 600, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11A0E)
    WaitChrThread(0xFE, 1)

    def lambda_11A2C():
        OP_96(0xFE, 0x44C, 0x64, 0xA28, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11A2C)
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

    def lambda_11AB7():
        OP_98(0xFE, 0x0, 0x0, 0xC8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_11AB7)
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

    def lambda_11BB5():
        OP_98(0xFE, 0x0, 0x0, 0xC8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_11BB5)
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

    def lambda_11CB3():
        OP_98(0xFE, 0x0, 0x0, 0xC8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_11CB3)
    Sound(501, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0x3F, 0x0, -300, 2350, 200, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0x3F, 0x0, -300, 2350, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x5)
    Sleep(300)
    BeginChrThread(0x3F, 3, 0, 89)
    Return()

    # Function_94_11A09 end

    def Function_95_11D4D(): pass

    label("Function_95_11D4D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11DA2")
    PlayEffect(0x2, 0xFF, 0xFE, 0x3, 0, 1100, 1100, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x6)
    Sleep(500)
    SetChrSubChip(0xFE, 0x5)
    Sleep(500)
    Jump("Function_95_11D4D")

    label("loc_11DA2")

    Return()

    # Function_95_11D4D end

    def Function_96_11DA3(): pass

    label("Function_96_11DA3")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_11DB3():
        OP_95(0xFE, 600, 250, 400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11DB3)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x6)
    Sound(809, 0, 100, 0)

    def lambda_11DDB():
        OP_9D(0xFE, 0x6A4, 0x64, 0x1130, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11DDB)
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

    def lambda_11E7A():
        OP_A6(0xFE, 0x0, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3F, 2, lambda_11E7A)
    OP_52(0x3F, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_11E9E():
        OP_9D(0xFE, 0x7D0, 0x64, 0x1E78, 0x12C, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_11E9E)
    WaitChrThread(0xFE, 1)
    Sleep(2000)
    SetChrSubChip(0xFE, 0x5)
    Return()

    # Function_96_11DA3 end

    def Function_97_11EC2(): pass

    label("Function_97_11EC2")

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

    # Function_97_11EC2 end

    def Function_98_11F0A(): pass

    label("Function_98_11F0A")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x3)
    SetChrSubChip(0xFE, 0x0)

    def lambda_11F22():
        OP_95(0xFE, -600, 250, 400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11F22)
    WaitChrThread(0xFE, 1)

    def lambda_11F40():
        OP_95(0xFE, -1300, 100, 4400, 8000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11F40)
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

    def lambda_12002():
        OP_A6(0xFE, 0x0, 0x64, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_12002)

    def lambda_1201B():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3E, 1, lambda_1201B)
    WaitChrThread(0xFE, 1)
    Sleep(300)
    SetChrSubChip(0xFE, 0x4)
    Sleep(90)
    SetChrSubChip(0xFE, 0x1)
    Sleep(90)
    SetChrSubChip(0xFE, 0x2)
    Sleep(90)
    SetChrSubChip(0xFE, 0x3)

    def lambda_12055():
        OP_95(0xFE, -1400, 100, 5400, 8000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12055)
    Sound(533, 0, 60, 0)
    Sleep(100)
    OP_82(0xC8, 0xC8, 0xBB8, 0xC8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)
    Sound(815, 0, 100, 0)
    Sound(635, 0, 100, 0)
    PlayEffect(0x6, 0xFF, 0xFE, 0x3, 0, 1100, 0, 0, 0, 0, 1400, 1400, 1400, 0xFF, 0, 0, 0, 0)

    def lambda_120DD():
        OP_A6(0xFE, 0x0, 0x64, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_120DD)

    def lambda_120F6():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3E, 1, lambda_120F6)
    WaitChrThread(0xFE, 1)
    Sleep(200)
    SetChrSubChip(0xFE, 0x4)
    Sleep(90)
    SetChrSubChip(0xFE, 0x1)
    Sleep(90)
    SetChrSubChip(0xFE, 0x2)
    Sleep(90)
    SetChrSubChip(0xFE, 0x3)

    def lambda_12130():
        OP_95(0xFE, -1500, 100, 6400, 8000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12130)
    Sound(533, 0, 60, 0)
    Sleep(100)
    OP_82(0xC8, 0xC8, 0xBB8, 0xC8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)
    Sound(815, 0, 100, 0)
    Sound(635, 0, 100, 0)
    PlayEffect(0x6, 0xFF, 0xFE, 0x3, 0, 1100, 0, 0, 0, 0, 1400, 1400, 1400, 0xFF, 0, 0, 0, 0)

    def lambda_121B8():
        OP_A6(0xFE, 0x0, 0x64, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_121B8)

    def lambda_121D1():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3E, 1, lambda_121D1)
    WaitChrThread(0xFE, 1)
    Sleep(2000)
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x2)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_98_11F0A end

    def Function_99_12202(): pass

    label("Function_99_12202")

    SetChrChipByIndex(0xFE, 0x3)
    SetChrSubChip(0xFE, 0x0)

    def lambda_1220F():
        OP_95(0xFE, -3900, 250, 8800, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1220F)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x5)
    SetChrSubChip(0xFE, 0x1)
    Sleep(300)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x10)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x20)
    Sound(844, 0, 100, 0)

    def lambda_12252():
        OP_9C(0xFE, 0x0, 0x2BC, 0x0, 0x2EE, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12252)
    SetChrSubChip(0xFE, 0x14)
    Sleep(50)
    BeginChrThread(0xFE, 2, 0, 100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x10)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x20)
    Return()

    # Function_99_12202 end

    def Function_100_12290(): pass

    label("Function_100_12290")

    EndChrThread(0x43, 0x0)
    EndChrThread(0x43, 0x2)
    SetChrChipByIndex(0x43, 0xB)
    SetChrSubChip(0x43, 0x0)
    OP_52(0x43, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_122AB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1239D")
    Sound(815, 0, 100, 0)
    Sound(635, 0, 50, 0)
    OP_82(0xC8, 0xC8, 0xBB8, 0xC8)
    PlayEffect(0x4, 0xFF, 0x43, 0x1, 0, 1200, -200, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    def lambda_1230F():
        OP_A6(0xFE, 0x0, 0x64, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x43, 2, lambda_1230F)
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
    Jump("loc_122AB")

    label("loc_1239D")

    Return()

    # Function_100_12290 end

    def Function_101_1239E(): pass

    label("Function_101_1239E")

    SetChrChipByIndex(0x34, 0x3)
    SetChrSubChip(0x34, 0x0)

    def lambda_123AB():
        OP_95(0xFE, -6500, 250, 6800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_123AB)
    WaitChrThread(0x34, 1)
    SetChrChipByIndex(0x34, 0x2)
    SetChrSubChip(0x34, 0x0)
    Return()

    # Function_101_1239E end

    def Function_102_123CD(): pass

    label("Function_102_123CD")

    SetChrChipByIndex(0xFE, 0x7)
    SetChrSubChip(0xFE, 0x0)

    def lambda_123DA():
        OP_95(0xFE, -800, 100, 2600, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_123DA)
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

    # Function_102_123CD end

    def Function_103_12486(): pass

    label("Function_103_12486")

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

    # Function_103_12486 end

    def Function_104_12593(): pass

    label("Function_104_12593")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x1A)
    SetChrSubChip(0xFE, 0x0)

    def lambda_125B3():
        OP_95(0xFE, -8500, 150, 3500, 9000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_125B3)
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
        "#03401F#9AHah!\x02",
    )

    Sleep(700)

    def lambda_12620():
        OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12620)
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

    def lambda_126C7():
        OP_9D(0xFE, 0xFFFFDF94, 0xFA, 0x2454, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_126C7)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    CancelBlur(700)
    Sleep(500)
    Sound(880, 0, 100, 0)
    Sleep(1500)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_104_12593 end

    def Function_105_12704(): pass

    label("Function_105_12704")

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

    # Function_105_12704 end

    def Function_106_1273D(): pass

    label("Function_106_1273D")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)

    def lambda_1275D():
        OP_95(0xFE, 2500, 100, -2600, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1275D)
    WaitChrThread(0xFE, 1)

    ChrTalk(
        0x28,
        "#12P#11507F#9AThere!\x02",
    )

    TurnDirection(0xFE, 0x3E, 0)
    SetChrFlags(0xFE, 0x4)
    SetChrSubChip(0xFE, 0x2)
    Sound(844, 0, 100, 0)

    def lambda_127AA():
        OP_9D(0xFE, 0x1194, 0x5DC, 0x258, 0x76C, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_127AA)
    WaitChrThread(0xFE, 1)
    Sound(326, 0, 100, 0)
    BlurSwitch(0x0, 0x55FFFFFF, 0x0, 0x1, 0x0)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Sound(844, 0, 100, 0)

    def lambda_127EB():
        OP_9D(0xFE, 0x1A90, 0xFA, 0xABE, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_127EB)
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

    def lambda_128E2():
        OP_A6(0xFE, 0x0, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_128E2)

    def lambda_128FB():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x3E, 1, lambda_128FB)
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

    def lambda_1298B():
        OP_A6(0xFE, 0x0, 0x64, 0x9C4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_1298B)
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

    # Function_106_1273D end

    def Function_107_12D77(): pass

    label("Function_107_12D77")

    SetChrChipByIndex(0xFE, 0x18)
    OP_A0(0xFE, 1500, 0x0, 0x3)
    Return()

    # Function_107_12D77 end

    def Function_108_12D83(): pass

    label("Function_108_12D83")

    SetChrChipByIndex(0xFE, 0x16)

    label("loc_12D87")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12DA5")
    OP_A0(0xFE, 1500, 0x0, 0x4)
    OP_A0(0xFE, 1500, 0x3, 0x1)
    Jump("loc_12D87")

    label("loc_12DA5")

    Return()

    # Function_108_12D83 end

    def Function_109_12DA6(): pass

    label("Function_109_12DA6")

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

    def lambda_12F52():
        OP_A6(0xFE, 0x0, 0x64, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3F, 2, lambda_12F52)
    Sleep(50)
    EndChrThread(0x41, 0x0)
    EndChrThread(0x41, 0x2)
    SetChrChipByIndex(0x41, 0xB)
    SetChrSubChip(0x41, 0x0)
    OP_52(0x41, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_12F89():
        OP_A6(0xFE, 0x0, 0x64, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x41, 2, lambda_12F89)
    Sleep(50)
    EndChrThread(0x42, 0x0)
    EndChrThread(0x42, 0x2)
    SetChrChipByIndex(0x42, 0xB)
    SetChrSubChip(0x42, 0x0)
    OP_52(0x42, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_12FC0():
        OP_A6(0xFE, 0x0, 0x64, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x42, 2, lambda_12FC0)
    Sleep(2500)
    CancelBlur(0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    Sleep(1000)
    Return()

    # Function_109_12DA6 end

    def Function_110_12FF1(): pass

    label("Function_110_12FF1")

    PlayEffect(0x8, 0xFF, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1200, 1000, 1200, 0xFF, 0, 0, 0, 0)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)

    def lambda_13035():
        OP_9E(0xFE, 0xFA0, 0xFFFFF448, 0x36EE8, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13035)

    label("loc_1304B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13073")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(10)
    Jump("loc_1304B")

    label("loc_13073")

    WaitChrThread(0xFE, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Return()

    # Function_110_12FF1 end

    def Function_111_1308B(): pass

    label("Function_111_1308B")

    SetChrChip(0x0, 0x77, 0x32, 0x12C)

    def lambda_13098():
        OP_9E(0xFE, 0xFFFFE124, 0x708, 0x2BF20, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x77, 1, lambda_13098)

    label("loc_130AE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_130D6")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(10)
    Jump("loc_130AE")

    label("loc_130D6")

    WaitChrThread(0x77, 1)
    SetChrChip(0x1, 0x77, 0x0, 0x0)
    OP_A7(0x77, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Return()

    # Function_111_1308B end

    def Function_112_130EE(): pass

    label("Function_112_130EE")

    SetChrPos(0xFE, -7400, 250, 5400, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    BeginChrThread(0xFE, 2, 0, 113)

    def lambda_1311D():
        OP_9E(0xFE, 0xFFFFD9B8, 0x1C84, 0x2BF20, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1311D)
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

    def lambda_131B8():
        OP_A6(0xFE, 0x0, 0x64, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_131B8)

    label("loc_131CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13279")

    def lambda_131DC():
        OP_9E(0xFE, 0xFFFFD3DC, 0x2CEC, 0x57E40, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_131DC)
    WaitChrThread(0xFE, 1)
    OP_82(0xC8, 0xC8, 0xBB8, 0xC8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)
    Sound(501, 0, 40, 0)
    Sound(308, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0x3E, 0x1, 0, 1200, -200, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    def lambda_13260():
        OP_A6(0xFE, 0x0, 0x64, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_13260)
    Jump("loc_131CC")

    label("loc_13279")

    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Return()

    # Function_112_130EE end

    def Function_113_1328D(): pass

    label("Function_113_1328D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_132D7")
    PlayEffect(0x8, 0xFF, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1200, 1000, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(1900)
    Jump("Function_113_1328D")

    label("loc_132D7")

    Return()

    # Function_113_1328D end

    def Function_114_132D8(): pass

    label("Function_114_132D8")

    PlayEffect(0x8, 0xFF, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1200, 1000, 1200, 0xFF, 0, 0, 0, 0)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)

    def lambda_1331C():
        OP_9E(0xFE, 0xFFFFE4A8, 0xFFFFF060, 0xFFFD40E0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1331C)

    label("loc_13332")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1335A")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(10)
    Jump("loc_13332")

    label("loc_1335A")

    WaitChrThread(0xFE, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Return()

    # Function_114_132D8 end

    def Function_115_13372(): pass

    label("Function_115_13372")

    Sleep(150)
    SetChrChip(0x0, 0x78, 0x32, 0x12C)

    def lambda_13382():
        OP_9E(0xFE, 0xFFFFF4AC, 0x16A8, 0x2BF20, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x78, 1, lambda_13382)

    label("loc_13398")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_133C0")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(10)
    Jump("loc_13398")

    label("loc_133C0")

    WaitChrThread(0x78, 1)
    SetChrChip(0x1, 0x78, 0x0, 0x0)
    OP_A7(0x78, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Return()

    # Function_115_13372 end

    def Function_116_133D8(): pass

    label("Function_116_133D8")

    SetChrPos(0xFE, -7400, 250, 6200, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    BeginChrThread(0xFE, 2, 0, 113)

    def lambda_13407():
        OP_9E(0xFE, 0xFFFFD9B8, 0x1C84, 0xFFFD5468, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13407)
    WaitChrThread(0xFE, 1)

    label("loc_13421")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13450")

    def lambda_13431():
        OP_9E(0xFE, 0xFFFFCE00, 0x17D4, 0xFFFA81C0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13431)
    WaitChrThread(0xFE, 1)
    Jump("loc_13421")

    label("loc_13450")

    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Return()

    # Function_116_133D8 end

    def Function_117_13464(): pass

    label("Function_117_13464")

    BeginChrThread(0x3C, 1, 0, 123)
    Sleep(300)
    BeginChrThread(0x38, 1, 0, 123)
    Sleep(300)
    BeginChrThread(0x48, 1, 0, 123)
    BeginChrThread(0x72, 3, 0, 81)
    Return()

    # Function_117_13464 end

    def Function_118_13483(): pass

    label("Function_118_13483")

    OP_96(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x2710, 0x0)

    def lambda_1349C():
        OP_D5(0xFE, 0x0, 0x0, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1349C)
    OP_96(0xFE, 0x0, 0x0, 0xFFFFE4A8, 0x2710, 0x0)

    def lambda_134C9():
        OP_D5(0xFE, 0x0, 0xFFFEEE90, 0x0, 0x4B0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_134C9)
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

    # Function_118_13483 end

    def Function_119_13565(): pass

    label("Function_119_13565")

    OP_96(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x2710, 0x0)

    def lambda_1357E():
        OP_D5(0xFE, 0x0, 0x0, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1357E)
    OP_96(0xFE, 0x0, 0x0, 0xFFFFE4A8, 0x2710, 0x0)

    def lambda_135AB():
        OP_D5(0xFE, 0x0, 0x11170, 0x0, 0x4B0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_135AB)
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

    # Function_119_13565 end

    def Function_120_13638(): pass

    label("Function_120_13638")

    OP_96(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x3A98, 0x0)

    def lambda_13651():
        OP_D5(0xFE, 0x0, 0x0, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_13651)
    SetMapObjFrame(0x14, "kage", 0x0, 0x1)
    ClearMapObjFlags(0x15, 0x4)
    BeginChrThread(0x75, 3, 0, 121)
    OP_9D(0xFE, 0x0, 0x0, 0xFFFFCD38, 0x514, 0x514)

    def lambda_13699():
        OP_D5(0xFE, 0x0, 0x1B58, 0x0, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_13699)
    OP_82(0x0, 0xC8, 0xBB8, 0xC8)
    Sound(833, 0, 100, 0)
    OP_9D(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x12C, 0x44C)
    EndChrThread(0xFE, 0x2)

    def lambda_136E4():
        OP_D5(0xFE, 0x0, 0xFFFFE4A8, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_136E4)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    Sound(833, 0, 100, 0)
    Sound(487, 0, 100, 0)
    SetMapObjFrame(0x14, "kage", 0x1, 0x1)
    SetMapObjFlags(0x15, 0x4)
    EndChrThread(0x75, 0x3)
    BeginChrThread(0x74, 3, 0, 122)

    def lambda_13736():
        OP_96(0xFE, 0x0, 0xC8, 0x9C40, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13736)
    WaitChrThread(0xFE, 2)

    def lambda_13754():
        OP_D5(0xFE, 0x0, 0x0, 0x0, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_13754)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_120_13638 end

    def Function_121_1376D(): pass

    label("Function_121_1376D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13794")
    OP_52(0xFE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x73, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x73, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(30)
    Jump("Function_121_1376D")

    label("loc_13794")

    Return()

    # Function_121_1376D end

    def Function_122_13795(): pass

    label("Function_122_13795")

    Sleep(3100)
    Sound(880, 0, 100, 0)
    Sound(991, 0, 100, 0)
    Sound(200, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, -900, 1200, 31000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 900, 1200, 31000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x1F4, 0x1F4, 0xBB8, 0x1F4)
    OP_71(0x17, 0x0, 0xA, 0x0, 0x0)
    Return()

    # Function_122_13795 end

    def Function_123_13836(): pass

    label("Function_123_13836")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1388B")
    PlayEffect(0x2, 0xFF, 0xFE, 0x3, 0, 1100, 1100, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Sleep(700)
    Jump("Function_123_13836")

    label("loc_1388B")

    Return()

    # Function_123_13836 end

    def Function_124_1388C(): pass

    label("Function_124_1388C")

    PlayEffect(0x2, 0xFF, 0xFE, 0x5, 0, 1100, 1100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)

    label("loc_138C3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1395E")
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
    Jump("loc_138C3")

    label("loc_1395E")

    Return()

    # Function_124_1388C end

    def Function_125_1395F(): pass

    label("Function_125_1395F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1397D")
    OP_A1(0xFE, 0xFA0, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_125_1395F")

    label("loc_1397D")

    Return()

    # Function_125_1395F end

    def Function_126_1397E(): pass

    label("Function_126_1397E")


    def lambda_13983():
        OP_96(0xFE, 0xA8C, 0xFA, 0x283C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_13983)
    Sleep(50)

    def lambda_139A0():
        OP_96(0xFE, 0x44C, 0x64, 0x206C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x32, 1, lambda_139A0)
    Sleep(100)
    SetChrChipByIndex(0x34, 0x3)
    SetChrSubChip(0x34, 0x0)

    def lambda_139C5():
        OP_96(0xFE, 0xFFFFF18C, 0xFA, 0x2454, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_139C5)
    Sleep(50)
    SetChrChipByIndex(0x35, 0x7)
    SetChrSubChip(0x35, 0x0)

    def lambda_139EA():
        OP_96(0xFE, 0xFFFFF2B8, 0x64, 0x1BBC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_139EA)
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

    # Function_126_1397E end

    def Function_127_13A28(): pass

    label("Function_127_13A28")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13A41")
    Sound(567, 0, 100, 0)
    Sleep(1200)
    Jump("Function_127_13A28")

    label("loc_13A41")

    Return()

    # Function_127_13A28 end

    def Function_128_13A42(): pass

    label("Function_128_13A42")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13A5B")
    Sound(530, 0, 70, 0)
    Sleep(1200)
    Jump("Function_128_13A42")

    label("loc_13A5B")

    Return()

    # Function_128_13A42 end

    def Function_129_13A5C(): pass

    label("Function_129_13A5C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13A75")
    Sound(530, 0, 50, 0)
    Sleep(1200)
    Jump("Function_129_13A5C")

    label("loc_13A75")

    Return()

    # Function_129_13A5C end

    def Function_130_13A76(): pass

    label("Function_130_13A76")

    Sound(987, 0, 100, 0)

    label("loc_13A7C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13ABC")
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
    Jump("loc_13A7C")

    label("loc_13ABC")

    Return()

    # Function_130_13A76 end

    def Function_131_13ABD(): pass

    label("Function_131_13ABD")

    Sound(987, 0, 50, 0)

    label("loc_13AC3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13B03")
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
    Jump("loc_13AC3")

    label("loc_13B03")

    Return()

    # Function_131_13ABD end

    def Function_132_13B04(): pass

    label("Function_132_13B04")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13B20")
    Sound(567, 0, 40, 0)
    Sleep(500)
    Sleep(500)
    Jump("Function_132_13B04")

    label("loc_13B20")

    Return()

    # Function_132_13B04 end

    def Function_133_13B21(): pass

    label("Function_133_13B21")

    Sound(457, 0, 100, 0)
    Sound(486, 0, 100, 0)
    Sleep(2000)
    Sound(458, 0, 100, 0)
    Sound(494, 0, 100, 0)
    Sleep(1000)
    Sound(493, 0, 100, 0)
    Sound(486, 0, 100, 0)
    Return()

    # Function_133_13B21 end

    def Function_134_13B4C(): pass

    label("Function_134_13B4C")

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

    # Function_134_13B4C end

    def Function_135_13B9B(): pass

    label("Function_135_13B9B")

    SetChrChipByIndex(0xFE, 0x9)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13BB5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13BD3")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("loc_13BB5")

    label("loc_13BD3")

    Return()

    # Function_135_13B9B end

    def Function_136_13BD4(): pass

    label("Function_136_13BD4")

    SetChrChipByIndex(0xFE, 0xA)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13BEE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13C05")
    OP_A0(0xFE, 700, 0x0, 0x5)
    Jump("loc_13BEE")

    label("loc_13C05")

    Return()

    # Function_136_13BD4 end

    def Function_137_13C06(): pass

    label("Function_137_13C06")

    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A6(0xFE, 0x0, 0x64, 0x12C, 0xBB8)
    Return()

    # Function_137_13C06 end

    def Function_138_13C38(): pass

    label("Function_138_13C38")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13C8D")
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
    Jump("Function_138_13C38")

    label("loc_13C8D")

    Return()

    # Function_138_13C38 end

    def Function_139_13C8E(): pass

    label("Function_139_13C8E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13CE3")
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
    Jump("Function_139_13C8E")

    label("loc_13CE3")

    Return()

    # Function_139_13C8E end

    def Function_140_13CE4(): pass

    label("Function_140_13CE4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13D39")
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
    Jump("Function_140_13CE4")

    label("loc_13D39")

    Return()

    # Function_140_13CE4 end

    def Function_141_13D3A(): pass

    label("Function_141_13D3A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13D8F")
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
    Jump("Function_141_13D3A")

    label("loc_13D8F")

    Return()

    # Function_141_13D3A end

    def Function_142_13D90(): pass

    label("Function_142_13D90")

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
    OP_8E(0x2F, "Kilika")
    OP_8E(0x28, "Lechter")
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
        "#12PT-They vanished!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "#03400F...It seems their supply\x01",
            "of spiritual power has\x01",
            "ceased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        "#11P#11506FMan... I'm beat.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "#01002FHeh... We did it.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 3)
    NewScene("c1600", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_142_13D90 end

    def Function_143_144B9(): pass

    label("Function_143_144B9")

    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0x0, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Sound(985, 0, 100, 0)
    Sleep(1800)

    def lambda_14514():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_14514)
    WaitChrThread(0xFE, 2)
    StopEffect(0x0, 0x2)
    Return()

    # Function_143_144B9 end

    def Function_144_14528(): pass

    label("Function_144_14528")

    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0x1, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2400)

    def lambda_1457A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1457A)
    WaitChrThread(0xFE, 2)
    StopEffect(0x1, 0x2)
    Return()

    # Function_144_14528 end

    def Function_145_1458E(): pass

    label("Function_145_1458E")

    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0x2, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2800)

    def lambda_145E0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_145E0)
    WaitChrThread(0xFE, 2)
    StopEffect(0x2, 0x2)
    Return()

    # Function_145_1458E end

    def Function_146_145F4(): pass

    label("Function_146_145F4")

    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0x3, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2600)

    def lambda_14646():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_14646)
    WaitChrThread(0xFE, 2)
    StopEffect(0x3, 0x2)
    Return()

    # Function_146_145F4 end

    def Function_147_1465A(): pass

    label("Function_147_1465A")

    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0x4, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)

    def lambda_146AC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_146AC)
    WaitChrThread(0xFE, 2)
    StopEffect(0x4, 0x2)
    Return()

    # Function_147_1465A end

    def Function_148_146C0(): pass

    label("Function_148_146C0")

    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0x5, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2200)

    def lambda_14712():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_14712)
    WaitChrThread(0xFE, 2)
    StopEffect(0x5, 0x2)
    Return()

    # Function_148_146C0 end

    def Function_149_14726(): pass

    label("Function_149_14726")

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

    # Function_149_14726 end

    def Function_150_149E7(): pass

    label("Function_150_149E7")

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

    # Function_150_149E7 end

    SaveToFile()

Try(main)
