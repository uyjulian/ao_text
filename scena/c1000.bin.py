from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1000.bin",                # FileName
        "c1000",                    # MapName
        "c1000",                    # Location
        0x0010,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("c1000", "c1000_1", "c1000_2", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 16, 0, 8, 0, 9],
    )

    BuildStringList((
        "c1000",                  # 0
        "Cronk",                  # 1
        "Danes",                  # 2
        "Lily",                   # 3
        "Marte",                  # 4
        "Danan",                  # 5
        "Anne",                   # 6
        "Grandpa Renaud",         # 7
        "Roy",                    # 8
        "Meiling",                # 9
        "Susan",                  # 10
        "Gilles",                 # 11
        "Coutaz",                 # 12
        "Old Man Mors",           # 13
        "Detective",              # 14
        "車",                     # 15
        "暴走車",                 # 16
        "Patrol Car",             # 17
        "Branch Manager Celdan",  # 18
        "Coppen",                 # 19
        "Peter",                  # 20
        "Shirley",                # 21
        "State Guard Soldier",    # 22
        "State Guard Soldier",    # 23
        "市民１",                 # 24
        "市民２",                 # 25
        "市民３",                 # 26
        "市民４",                 # 27
        "市民５",                 # 28
        "市民６",                 # 29
        "市民７",                 # 30
        "Policeman",              # 31
        "Policeman",              # 32
        "Policeman",              # 33
        "Policeman",              # 34
        "Grandma Paola",          # 35
        "bc1000",                 # 36
        "Central Square",         # 37
        "West Street",            # 38
        "Governmental District",  # 39
        "Residential Street",     # 40
        "Entertainment District", # 41
        "East Street",            # 42
        "Downtown",               # 43
        "Waterfront Area",        # 44
        "IBC",                    # 45
        "Station Street",         # 46
        "Back Street",            # 47
        "St. Ursula Byroad",      # 48
        "East Crossbell Highway", # 49
        "West Crossbell HIghway", # 50
        "Mainz Mountain Road",    # 51
        "Orchis Tower",           # 52
    ))

    ATBonus("ATBonus_950", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_D467", 8,   8,   8,   8,   11,  11,  11)

    MonsterBattlePostion("MonsterBattlePostion_9A0", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_9A4", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_9A8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_9AC", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_9B0", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_9B4", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_9B8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_9BC", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_A00", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_A04", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_A08", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_A0C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_A10", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_A14", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_A18", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_A1C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_980", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_984", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_988", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_98C", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_990", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_994", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_998", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_99C", 2, 13, 180)

    # monster count: 2

    BattleInfo(
        "BattleInfo_A20", 0x0000, 93, 6, 60, 4, 1, 25, 0, "bc1000", "Sepith_D467", 60, 30, 10, 0,
        (
            ("ms85100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_9A0", "MonsterBattlePostion_A00", "ed7450", "ed7453", "ATBonus_950"),
            ("ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_980", "MonsterBattlePostion_A00", "ed7450", "ed7453", "ATBonus_950"),
            ("ms85100.dat", "ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_9A0", "MonsterBattlePostion_A00", "ed7450", "ed7453", "ATBonus_950"),
            (),
        )
    )

    AddCharChip((
        "chr/ch23500.itc",                   # 00
        "chr/ch20400.itc",                   # 01
        "chr/ch24800.itc",                   # 02
        "chr/ch24900.itc",                   # 03
        "chr/ch21100.itc",                   # 04
        "chr/ch24000.itc",                   # 05
        "chr/ch21200.itc",                   # 06
        "chr/ch21500.itc",                   # 07
        "chr/ch10300.itc",                   # 08
        "chr/ch26200.itc",                   # 09
        "chr/ch21400.itc",                   # 0A
        "chr/ch20800.itc",                   # 0B
        "chr/ch49800.itc",                   # 0C
        "chr/ch49600.itc",                   # 0D
        "chr/ch49700.itc",                   # 0E
        "chr/ch49900.itc",                   # 0F
        "monster/ch85150.itc",               # 10
        "monster/ch85151.itc",               # 11
        "chr/ch27600.itc",                   # 12
        "chr/ch24200.itc",                   # 13
    ))

    DeclNpc(4294942887, 4294964296, 5239,    180,  261,  0x0, 0,   1,   0,   0,   0,   2,   0,   255,  0)
    DeclNpc(4294954257, 4294964296, 4294966486, 225,  261,  0x0, 0,   2,   0,   0,   0,   2,   1,   255,  0)
    DeclNpc(4294950796, 4294964296, 2920,    45,   261,  0x0, 0,   3,   0,   0,   7,   2,   2,   255,  0)
    DeclNpc(4294962737, 4294964296, 4294958347, 180,  261,  0x0, 0,   0,   0,   0,   0,   2,   3,   255,  0)
    DeclNpc(4294961737, 4294964296, 4294958347, 180,  389,  0x0, 0,   19,  0,   0,   0,   2,   15,  255,  0)
    DeclNpc(26200,   4294966996, 4294966247, 270,  261,  0x0, 0,   4,   0,   0,   1,   2,   7,   255,  0)
    DeclNpc(4294926806, 4294966996, 15850,   90,   261,  0x0, 0,   5,   0,   0,   6,   2,   8,   255,  0)
    DeclNpc(4294949096, 4294966996, 18139,   270,  261,  0x0, 0,   6,   0,   0,   0,   2,   9,   255,  0)
    DeclNpc(4294945016, 4294966996, 18370,   225,  261,  0x0, 0,   7,   0,   0,   2,   2,   10,  255,  0)
    DeclNpc(4294958826, 4294964296, 4294959947, 45,   261,  0x0, 0,   8,   0,   0,   0,   2,   12,  255,  0)
    DeclNpc(4294959876, 4294964296, 4294958696, 45,   261,  0x0, 0,   9,   0,   0,   0,   2,   13,  255,  0)
    DeclNpc(4294951357, 4294964296, 4294966696, 45,   261,  0x0, 0,   10,  0,   0,   3,   2,   14,  255,  0)
    DeclNpc(4294949096, 4294966996, 18139,   270,  389,  0x0, 0,   11,  0,   0,   0,   2,   11,  255,  0)
    DeclNpc(4294964247, 4294964296, 4294953517, 315,  385,  0x0, 0,   18,  0,   0,   0,   2,   16,  255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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

    DeclMonster(4294949656, 14650,   4294966986, 0x10100E1,    "BattleInfo_A20", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(530,     4294954136, 4294964296, 0x101013B,    "BattleInfo_A20", 0,   16,  0xFFFF, 0,  1)

    DeclEvent(0x0000, 0, 12,  -26.8700008392334,     4.059999942779541,     -4.0,                  20.25,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   8.956666946411133,     -1.3533333539962769,   0.800000011920929,     1.0])
    DeclEvent(0x0000, 0, 13,  -15.1899995803833,     -5.800000190734863,    -6.5,                  37.515625,             [0.20203045010566711,  0.20203058421611786,   -0.0,                  0.0,                   -0.20203058421611786,  0.20203045010566711,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   1.8970650434494019,    4.240621089935303,     1.3000000715255737,    1.0])

    DeclActor(4294937296, 4294961796, 4000,    1200,    4294937296, 4294962796, 4000,    0x007C, 0,  10, 0x0000)
    DeclActor(4294944286, 4294952396, 4294962466, 1200,    4294944286, 4294953396, 4294962466, 0x007C, 0,  11, 0x0000)
    DeclActor(4294967106, 340,     6410,    2000,    4294967106, 1540,    6410,    0x007C, 0,  35, 0x0000)
    DeclActor(17360,   4294966996, 4630,    1200,    17530,   1500,    5120,    0x007C, 0,  17, 0x0000)
    DeclActor(4294951376, 240,     24020,   2000,    4294951376, 1540,    24020,   0x007C, 0,  36, 0x0000)
    DeclActor(17360,   4294966996, 4630,    1200,    17530,   1500,    5120,    0x007C, 0,  37, 0x0000)
    DeclActor(12360,   250,     5680,    1200,    12360,   1540,    5680,    0x007C, 0,  41, 0x0000)
    DeclActor(4294933946, 4294961796, 9380,    1200,    4294933946, 4294963296, 9380,    0x007C, 0,  14, 0x0000)

    PlaceName(-111.26000213623047, 0.0, 15.239999771118164, 0x0000, 0x0000, "Central Square")
    PlaceName(-186.8800048828125, 0.0, 20.40999984741211, 0x0000, 0x0000, "West Street")
    PlaceName(-80.20999908447266, 0.0, 117.58999633789062, 0x0000, 0x0000, "Governmental District")
    PlaceName(-257.0299987792969, 0.0, 106.08999633789062, 0x0000, 0x0000, "Residential Street")
    PlaceName(-173.0800018310547, 0.0, 96.88999938964844, 0x0000, 0x0000, "Entertainment District")
    PlaceName(-17.829999923706055, 0.0, -11.210000038146973, 0x0000, 0x0000, "East Street")
    PlaceName(23.0, 0.0, -74.45999908447266, 0x0000, 0x0000, "Downtown")
    PlaceName(14.380000114440918, 0.0, 64.69000244140625, 0x0000, 0x0000, "Waterfront Area")
    PlaceName(-15.529999732971191, 0.0, 172.7899932861328, 0x0000, 0x0000, "IBC")
    PlaceName(-98.33000183105469, 0.0, -64.11000061035156, 0x0000, 0x0000, "Station Street")
    PlaceName(-152.3800048828125, 0.0, 55.4900016784668, 0x0000, 0x0000, "Back Street")
    PlaceName(-101.77999877929688, 0.0, -99.76000213623047, 0x0000, 0x0000, "St. Ursula Byroad")
    PlaceName(44.279998779296875, 0.0, 4.889999866485596, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-245.52999877929688, 0.0, 18.690000534057617, 0x0000, 0x0000, "West Crossbell HIghway")
    PlaceName(-238.6300048828125, 0.0, 133.69000244140625, 0x0000, 0x0000, "Mainz Mountain Road")
    PlaceName(-88.0, 0.0, 269.0, 0x0000, 0x0000, "Orchis Tower")
    PlaceName(-136.55999755859375, 0.0, -0.8600000143051147, 0x0000, 0x0051, "")
    PlaceName(-74.75, 0.0, 29.040000915527344, 0x0000, 0x0054, "")
    PlaceName(-108.38999938964844, 0.0, -10.0600004196167, 0x0000, 0x0057, "")
    PlaceName(-137.42999267578125, 0.0, 32.4900016784668, 0x0000, 0x0053, "")
    PlaceName(-113.8499984741211, 0.0, 60.09000015258789, 0x0000, 0x0053, "")
    PlaceName(-172.2100067138672, 0.0, 26.739999771118164, 0x0000, 0x0053, "")
    PlaceName(-183.42999267578125, 0.0, 50.88999938964844, 0x0000, 0x0053, "")
    PlaceName(-155.8300018310547, 0.0, 87.69000244140625, 0x0000, 0x0052, "")
    PlaceName(-150.36000061035156, 0.0, 72.73999786376953, 0x0000, 0x0053, "")
    PlaceName(-140.3000030517578, 0.0, 62.959999084472656, 0x0000, 0x0053, "")
    PlaceName(-107.52999877929688, 0.0, 144.61000061035156, 0x0000, 0x0051, "")
    PlaceName(21.280000686645508, 0.0, -11.210000038146973, 0x0000, 0x0052, "")
    PlaceName(1.7300000190734863, 0.0, -115.29000091552734, 0x0000, 0x0053, "")
    PlaceName(-13.229999542236328, 0.0, -94.01000213623047, 0x0000, 0x0053, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 1

    ScpFunction((
        "Function_0_B94",          # 00, 0
        "Function_1_C44",          # 01, 1
        "Function_2_CDD",          # 02, 2
        "Function_3_D08",          # 03, 3
        "Function_4_D7D",          # 04, 4
        "Function_5_E1A",          # 05, 5
        "Function_6_E67",          # 06, 6
        "Function_7_F28",          # 07, 7
        "Function_8_F75",          # 08, 8
        "Function_9_169B",         # 09, 9
        "Function_10_1C33",        # 0A, 10
        "Function_11_1D85",        # 0B, 11
        "Function_12_1ED7",        # 0C, 12
        "Function_13_2110",        # 0D, 13
        "Function_14_237C",        # 0E, 14
        "Function_15_2C62",        # 0F, 15
        "Function_16_2D5A",        # 10, 16
        "Function_17_2FD1",        # 11, 17
        "Function_18_2FD2",        # 12, 18
        "Function_19_347A",        # 13, 19
        "Function_20_366D",        # 14, 20
        "Function_21_39D4",        # 15, 21
        "Function_22_3A78",        # 16, 22
        "Function_23_3FF2",        # 17, 23
        "Function_24_4382",        # 18, 24
        "Function_25_4909",        # 19, 25
        "Function_26_4C6D",        # 1A, 26
        "Function_27_514C",        # 1B, 27
        "Function_28_55F3",        # 1C, 28
        "Function_29_5EB4",        # 1D, 29
        "Function_30_736E",        # 1E, 30
        "Function_31_738A",        # 1F, 31
        "Function_32_73A6",        # 20, 32
        "Function_33_73C2",        # 21, 33
        "Function_34_73DE",        # 22, 34
        "Function_35_73FA",        # 23, 35
        "Function_36_7B2B",        # 24, 36
        "Function_37_7CDC",        # 25, 37
        "Function_38_A46C",        # 26, 38
        "Function_39_A6CF",        # 27, 39
        "Function_40_A8A2",        # 28, 40
        "Function_41_C146",        # 29, 41
        "Function_42_C2FC",        # 2A, 42
        "Function_43_CE46",        # 2B, 43
        "Function_44_CE7D",        # 2C, 44
        "Function_45_CEDE",        # 2D, 45
        "Function_46_CFC4",        # 2E, 46
        "Function_47_D335",        # 2F, 47
    ))


    def Function_0_B94(): pass

    label("Function_0_B94")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_BCC"),
        (1, "loc_BD8"),
        (2, "loc_BE4"),
        (3, "loc_BF0"),
        (4, "loc_BFC"),
        (5, "loc_C08"),
        (6, "loc_C14"),
        (SWITCH_DEFAULT, "loc_C20"),
    )


    label("loc_BCC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_C2C")

    label("loc_BD8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_C2C")

    label("loc_BE4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_C2C")

    label("loc_BF0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_C2C")

    label("loc_BFC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_C2C")

    label("loc_C08")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_C2C")

    label("loc_C14")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_C2C")

    label("loc_C20")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_C2C")

    label("loc_C2C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C43")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_C2C")

    label("loc_C43")

    Return()

    # Function_0_B94 end

    def Function_1_C44(): pass

    label("Function_1_C44")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CDC")
    OP_95(0xFE, -1180, -300, -1100, 2000, 0x0)
    OP_95(0xFE, -15670, -300, 12310, 2000, 0x0)
    OP_95(0xFE, -40270, -300, 12170, 2000, 0x0)
    Sleep(2500)
    OP_95(0xFE, -15670, -300, 12310, 2000, 0x0)
    OP_95(0xFE, -1180, -300, -1100, 2000, 0x0)
    OP_95(0xFE, 26200, -300, -1050, 2000, 0x0)
    Sleep(200)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    Jump("Function_1_C44")

    label("loc_CDC")

    Return()

    # Function_1_C44 end

    def Function_2_CDD(): pass

    label("Function_2_CDD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D07")
    OP_94(0xFE, 0xFFFFB000, 0x4ECA, 0xFFFFA8EE, 0x3F01, 0x3E8)
    Sleep(300)
    Jump("Function_2_CDD")

    label("loc_D07")

    Return()

    # Function_2_CDD end

    def Function_3_D08(): pass

    label("Function_3_D08")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D7C")
    OP_95(0xFE, -19740, -3000, 3190, 1000, 0x0)
    OP_95(0xFE, -22610, -3000, 3390, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x12C)
    Sleep(1500)
    OP_95(0xFE, -19740, -3000, 3190, 1000, 0x0)
    OP_95(0xFE, -15940, -3000, -600, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(1500)
    Jump("Function_3_D08")

    label("loc_D7C")

    Return()

    # Function_3_D08 end

    def Function_4_D7D(): pass

    label("Function_4_D7D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E19")
    OP_95(0xFE, -19740, -3000, 3190, 1000, 0x0)
    OP_95(0xFE, -22610, -3000, 3390, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x12C)
    Sleep(1500)
    OP_95(0xFE, -19740, -3000, 3190, 1000, 0x0)
    OP_95(0xFE, -15940, -3000, -600, 1000, 0x0)
    OP_95(0xFE, -8470, -3000, -7350, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(1500)
    OP_95(0xFE, -15940, -3000, -600, 1000, 0x0)
    Jump("Function_4_D7D")

    label("loc_E19")

    Return()

    # Function_4_D7D end

    def Function_5_E1A(): pass

    label("Function_5_E1A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E66")
    OP_95(0xFE, -15940, -3000, -600, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(1500)
    OP_95(0xFE, -9950, -3000, -6670, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(1500)
    Jump("Function_5_E1A")

    label("loc_E66")

    Return()

    # Function_5_E1A end

    def Function_6_E67(): pass

    label("Function_6_E67")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F27")
    OP_95(0xFE, -16760, -300, 15130, 2000, 0x0)
    OP_95(0xFE, -13780, -300, 14160, 2000, 0x0)
    OP_95(0xFE, -1180, -300, 2190, 2000, 0x0)
    OP_95(0xFE, 26030, -300, 2230, 2000, 0x0)
    Sleep(200)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -1180, -300, 2190, 2000, 0x0)
    OP_95(0xFE, -13780, -300, 14160, 2000, 0x0)
    OP_95(0xFE, -16760, -300, 15130, 2000, 0x0)
    OP_95(0xFE, -40490, -300, 15850, 2000, 0x0)
    Sleep(2400)
    Jump("Function_6_E67")

    label("loc_F27")

    Return()

    # Function_6_E67 end

    def Function_7_F28(): pass

    label("Function_7_F28")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F74")
    OP_95(0xFE, -15130, -3000, 1420, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(3000)
    OP_95(0xFE, -16500, -3000, 2920, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(3000)
    Jump("Function_7_F28")

    label("loc_F74")

    Return()

    # Function_7_F28 end

    def Function_8_F75(): pass

    label("Function_8_F75")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1195")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1040")
    SetChrPos(0x0, -20760, -310, 33300, 180)
    SetChrPos(0x1, -20760, -310, 33300, 180)
    SetChrPos(0x2, -20760, -310, 33300, 180)
    SetChrPos(0x3, -20760, -310, 33300, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1013")
    SetChrPos(0x4, -20760, -310, 33300, 180)
    SetChrPos(0x5, -20760, -310, 33300, 180)
    Jump("loc_1032")

    label("loc_1013")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1032")
    SetChrPos(0x4, -20760, -310, 33300, 180)

    label("loc_1032")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1195")

    label("loc_1040")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F4")
    SetChrPos(0x0, 1910, -3000, -35980, 0)
    SetChrPos(0x1, 1910, -3000, -35980, 0)
    SetChrPos(0x2, 1910, -3000, -35980, 0)
    SetChrPos(0x3, 1910, -3000, -35980, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10C7")
    SetChrPos(0x4, 1910, -3000, -35980, 0)
    SetChrPos(0x5, 1910, -3000, -35980, 0)
    Jump("loc_10E6")

    label("loc_10C7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10E6")
    SetChrPos(0x4, 1910, -3000, -35980, 0)

    label("loc_10E6")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1195")

    label("loc_10F4")

    SetChrPos(0x0, -29790, -330, 13830, 90)
    SetChrPos(0x1, -29790, -330, 13830, 90)
    SetChrPos(0x2, -29790, -330, 13830, 90)
    SetChrPos(0x3, -29790, -330, 13830, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_116D")
    SetChrPos(0x4, -29790, -330, 13830, 90)
    SetChrPos(0x5, -29790, -330, 13830, 90)
    Jump("loc_118C")

    label("loc_116D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_118C")
    SetChrPos(0x4, -29790, -330, 13830, 90)

    label("loc_118C")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1195")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_11B1")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_154F")

    label("loc_11B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_11F6")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    Jump("loc_154F")

    label("loc_11F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1237")
    SetChrPos(0x10, -22760, -3000, 5010, 0)
    BeginChrThread(0x10, 0, 0, 0)
    SetChrPos(0xF, -21950, -3000, 5010, 0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrFlags(0x11, 0x80)
    Jump("loc_154F")

    label("loc_1237")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_124F")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x12, 0x80)
    Jump("loc_154F")

    label("loc_124F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1290")
    SetChrPos(0x10, -14890, -300, 9170, 225)
    BeginChrThread(0x10, 0, 0, 0)
    SetChrPos(0xF, -22760, -3000, 5010, 0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrFlags(0x11, 0x80)
    Jump("loc_154F")

    label("loc_1290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_12C3")
    SetChrChipByIndex(0xF, 0xD)
    SetChrChipByIndex(0x10, 0xE)
    SetChrChipByIndex(0xD, 0xC)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x13, 0xF)
    BeginChrThread(0x13, 0, 0, 4)
    SetChrFlags(0x11, 0x80)
    Jump("loc_154F")

    label("loc_12C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_12F2")
    SetChrPos(0xF, -23170, -3000, 5100, 0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x14, 0x80)
    Jump("loc_154F")

    label("loc_12F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_133D")
    SetChrPos(0x10, -19280, -320, 18240, 90)
    BeginChrThread(0x10, 0, 0, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x10, 0x10)
    SetChrPos(0xF, -22760, -3000, 5010, 0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrFlags(0x12, 0x80)
    Jump("loc_154F")

    label("loc_133D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1383")
    SetChrPos(0x10, -14890, -300, 9170, 225)
    BeginChrThread(0x10, 0, 0, 0)
    SetChrPos(0xF, -26620, -3000, 5100, 0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x13, 0x80)
    Jump("loc_154F")

    label("loc_1383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_13C3")
    SetChrPos(0xF, -23170, -3000, 5100, 270)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0x8, -24410, -3000, 5240, 90)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jump("loc_154F")

    label("loc_13C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1413")
    SetChrPos(0xF, -22760, -3000, 5010, 0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0x10, -21950, -3000, 5010, 0)
    BeginChrThread(0x10, 0, 0, 0)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jump("loc_154F")

    label("loc_1413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1489")
    SetChrPos(0x10, -17150, -300, 16600, 315)
    BeginChrThread(0x10, 0, 0, 0)
    TurnDirection(0x10, 0xF, 0)
    TurnDirection(0xF, 0x10, 0)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1484")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1484")
    SetChrFlags(0x8, 0x10)

    label("loc_1484")

    Jump("loc_154F")

    label("loc_1489")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_14FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_END)), "loc_14AA")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    Jump("loc_14DC")

    label("loc_14AA")

    SetChrChipByIndex(0xF, 0xD)
    SetChrChipByIndex(0x10, 0xE)
    SetChrPos(0x10, -17150, -300, 16600, 315)
    BeginChrThread(0x10, 0, 0, 0)
    TurnDirection(0x10, 0xF, 0)
    TurnDirection(0xF, 0x10, 0)
    SetChrFlags(0x10, 0x10)

    label("loc_14DC")

    SetChrChipByIndex(0xD, 0xC)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x13, 0xF)
    BeginChrThread(0x13, 0, 0, 4)
    SetChrFlags(0x11, 0x80)
    Jump("loc_154F")

    label("loc_14FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_154F")
    SetChrFlags(0x11, 0x80)
    SetChrPos(0x10, -17150, -300, 16600, 315)
    BeginChrThread(0x10, 0, 0, 0)
    TurnDirection(0x10, 0xF, 0)
    TurnDirection(0xF, 0x10, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_154F")
    SetChrFlags(0x10, 0x10)

    label("loc_154F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1563")
    ClearScenarioFlags(0x22, 0)
    Event(0, 18)
    Jump("loc_162A")

    label("loc_1563")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_1577")
    ClearScenarioFlags(0x22, 1)
    Event(0, 19)
    Jump("loc_162A")

    label("loc_1577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_158B")
    ClearScenarioFlags(0x22, 2)
    Event(0, 20)
    Jump("loc_162A")

    label("loc_158B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_159F")
    ClearScenarioFlags(0x22, 3)
    Event(0, 23)
    Jump("loc_162A")

    label("loc_159F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_15B3")
    ClearScenarioFlags(0x22, 4)
    Event(0, 24)
    Jump("loc_162A")

    label("loc_15B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_15C7")
    ClearScenarioFlags(0x22, 5)
    Event(0, 27)
    Jump("loc_162A")

    label("loc_15C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_15E0")
    ClearScenarioFlags(0x22, 6)
    SetMapFlags(0x10000000)
    Event(0, 25)
    Jump("loc_162A")

    label("loc_15E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 7)), scpexpr(EXPR_END)), "loc_15F4")
    ClearScenarioFlags(0x22, 7)
    Event(0, 42)
    Jump("loc_162A")

    label("loc_15F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_END)), "loc_161B")
    ClearScenarioFlags(0x23, 0)
    OP_1B(0x2, 0x0, 0x2C)
    SetChrPos(0x0, 1910, -3000, -35980, 0)
    Jump("loc_162A")

    label("loc_161B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_END)), "loc_162A")
    ClearScenarioFlags(0x23, 1)
    Event(0, 16)

    label("loc_162A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1655")
    SetMapFlags(0x10000000)
    Event(1, 0)

    label("loc_1655")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_166D")
    Event(0, 22)

    label("loc_166D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_169A")
    SetMapFlags(0x10000000)
    Event(0, 28)

    label("loc_169A")

    Return()

    # Function_8_F75 end

    def Function_9_169B(): pass

    label("Function_9_169B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1744")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xF, 0x64, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Sound(128, 1, 100, 0)

    label("loc_1744")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17D8")
    LoadEffect(0x9, "map/mpmoya.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0x78, 0x96, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xFF, 0xD, 0x5F, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)

    label("loc_17D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_181F")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x23, 0x96, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)

    label("loc_181F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1837")
    ClearMapFlags(0x2000)
    Jump("loc_183E")

    label("loc_1837")

    SetMapFlags(0x2000)
    OP_E2(0x1)

    label("loc_183E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_185A")
    SetMapObjFrame(0xFF, "turi00", 0x0, 0x1)
    Jump("loc_1868")

    label("loc_185A")

    SetMapObjFrame(0xFF, "turi01", 0x0, 0x1)

    label("loc_1868")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1881")
    ClearMapObjFlags(0x9, 0x4)
    Jump("loc_1887")

    label("loc_1881")

    SetMapObjFlags(0x9, 0x4)

    label("loc_1887")

    ClearMapObjFlags(0x5, 0x10)
    OP_70(0x5, 0x1E)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18C8")
    OP_1B(0x8, 0x0, 0x2D)
    OP_66(0x4, 0x1)
    ClearMapObjFlags(0x2, 0x10)
    OP_70(0x2, 0x0)

    label("loc_18C8")

    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18FB")
    OP_66(0x6, 0x1)
    ClearMapObjFlags(0x3, 0x10)
    OP_70(0x3, 0x0)

    label("loc_18FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1920")
    OP_1B(0x2, 0x0, 0x2C)

    label("loc_1920")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_END)), "loc_192E")
    OP_1B(0x2, 0x0, 0x2F)

    label("loc_192E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_193D")
    OP_1B(0x8, 0x0, 0x2E)

    label("loc_193D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1950")
    OP_1B(0x8, 0x0, 0x2E)

    label("loc_1950")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1963")
    OP_1B(0x8, 0x0, 0x2E)

    label("loc_1963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1976")
    OP_1B(0x8, 0x0, 0x2E)

    label("loc_1976")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1989")
    OP_1B(0x8, 0x0, 0x2E)

    label("loc_1989")

    OP_52(0x2B, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B3E")
    OP_70(0x6, 0x0)
    Jump("loc_1B42")

    label("loc_1B3E")

    OP_70(0x6, 0x1E)

    label("loc_1B42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B55")
    OP_70(0x7, 0x0)
    Jump("loc_1B59")

    label("loc_1B55")

    OP_70(0x7, 0x1E)

    label("loc_1B59")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B7F")
    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0x0)
    OP_66(0x2, 0x1)
    Jump("loc_1BAD")

    label("loc_1B7F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BAD")
    OP_66(0x2, 0x1)
    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0x0)

    label("loc_1BAD")

    OP_65(0x3, 0x1)
    OP_65(0x7, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BCB")
    OP_66(0x7, 0x1)

    label("loc_1BCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BDC")
    OP_66(0x7, 0x1)

    label("loc_1BDC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1BFB")
    OP_10(0x2, 0x0)
    OP_10(0xB, 0x1)
    OP_10(0x1, 0x0)
    OP_10(0xC, 0x1)
    Jump("loc_1C07")

    label("loc_1BFB")

    OP_10(0x2, 0x1)
    OP_10(0xB, 0x0)
    OP_10(0x1, 0x1)
    OP_10(0xC, 0x0)

    label("loc_1C07")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C32")
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_1C32")

    Return()

    # Function_9_169B end

    def Function_10_1C33(): pass

    label("Function_10_1C33")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D2F")
    Sound(14, 0, 100, 0)
    OP_74(0x6, 0x1E)
    OP_71(0x6, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x38E, 1)"), scpexpr(EXPR_END)), "loc_1CB8")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_1D2A")

    label("loc_1CB8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x6, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1D2A")

    Jump("loc_1D79")

    label("loc_1D2F")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the chest. \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1D79")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_1C33 end

    def Function_11_1D85(): pass

    label("Function_11_1D85")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E81")
    Sound(14, 0, 100, 0)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x98, 1)"), scpexpr(EXPR_END)), "loc_1E0A")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x98),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_1E7C")

    label("loc_1E0A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x98),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1E7C")

    Jump("loc_1ECB")

    label("loc_1E81")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the chest. \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1ECB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_1D85 end

    def Function_12_1ED7(): pass

    label("Function_12_1ED7")

    EventBegin(0x0)
    Fade(500)
    OP_68(-25670, -1400, 3480, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_E2(0x3)
    SetChrPos(0x101, -24530, -3000, 3820, 270)
    SetChrPos(0x102, -24620, -3000, 4610, 270)
    SetChrPos(0x103, -26670, -3000, 3480, 270)
    SetChrPos(0x104, -23080, -3000, 4470, 270)
    SetChrPos(0xF4, -23280, -3000, 3480, 270)
    SetChrPos(0xF5, -23030, -3000, 2550, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    ChrTalk(
        0x103,
        "#11P#00205F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F...Tio?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00105FWas there something bothering you?\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)
    OP_68(-32299, -1400, 3240, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x103,
        (
            "#11P#00200FI felt a small presence coming\x01",
            "from this direction, but...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#6P#00203F...I am sorry, it is probably nothing\x01",
            "to be concerned about, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FI see...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    SetScenarioFlags(0x1BF, 1)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -24530, -3000, 3820, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_12_1ED7 end

    def Function_13_2110(): pass

    label("Function_13_2110")

    EventBegin(0x0)
    Fade(500)
    OP_68(-16840, -3900, -5030, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_E2(0x3)
    SetChrPos(0x101, -15840, -5500, -6030, 315)
    SetChrPos(0x102, -15430, -5500, -4830, 270)
    SetChrPos(0x103, -16840, -5500, -5030, 315)
    SetChrPos(0x104, -14440, -5500, -5410, 270)
    SetChrPos(0xF4, -14440, -5500, -6610, 315)
    SetChrPos(0xF5, -14850, -5500, -7820, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    ChrTalk(
        0x103,
        "#11P#00205F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F...Tio?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FWas there something bothering you?\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)
    OP_68(-30570, -3900, 4350, 5000)
    OP_6F(0x79)
    Sleep(2000)
    Fade(500)
    OP_68(-16840, -3900, -5030, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_0D()

    ChrTalk(
        0x103,
        (
            "#11P#00200FI felt a small presence coming\x01",
            "from this direction, but...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#6P#00203F...I am sorry, it is probably nothing\x01",
            "to be concerned about, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FI see...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    SetScenarioFlags(0x1BF, 1)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -15840, -5500, -6030, 315)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_13_2110 end

    def Function_14_237C(): pass

    label("Function_14_237C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2389")
    Call(0, 15)
    Return()

    label("loc_2389")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-33380, -3950, 5900, 0)
    MoveCamera(25, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15420, 0)
    SetChrPos(0x101, -33000, -5500, 6670, 0)
    SetChrPos(0x102, -32000, -5500, 5870, 0)
    SetChrPos(0x103, -34000, -5500, 5660, 0)
    SetChrPos(0x104, -33000, -5500, 5160, 0)
    SetChrPos(0xF4, -34400, -5500, 4450, 0)
    SetChrPos(0xF5, -31790, -5500, 4570, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28F0")
    SetScenarioFlags(0x2, 2)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You can see darkness from a creak in the\x01",
            "wooden planks leaned against the wall.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00005FThis...\x01",
            "...It looks like it connects to somewhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105FA place in the Geofront, maybe?\x02\x03",
            "#00103FIt looks like the planks\x01",
            "can be moved away...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00305FCould it be that what peTiote\x01",
            "reacted at before is...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00200FYes, I think it is this place.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2633")

    ChrTalk(
        0x10A,
        "#12P#00603FHm...it slightly bothers me.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_26B8")

    label("loc_2633")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2674")

    ChrTalk(
        0x109,
        "#12P#10105F...Could there be someone?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_26B8")

    label("loc_2674")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_26B8")

    ChrTalk(
        0x105,
        "#12P#10405F...Could someone have gone astray?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_26B8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_26F4")

    ChrTalk(
        0x106,
        "#12P#10701FDo we go in to check?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_277B")

    label("loc_26F4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2739")

    ChrTalk(
        0x105,
        "#12P#10400FDo you want to go in to check?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_277B")

    label("loc_2739")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_277B")

    ChrTalk(
        0x109,
        "#12P#10101FShould we try going in to check?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_277B")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Try Checking Inside]\x01",      # 0
            "[Quitl]\x01",                    # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_287C")

    ChrTalk(
        0x101,
        (
            "#12P#00001FYou're right...\x01",
            "We should check just in case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00200FThen, let's enter immediately.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("m0304", 0, 0, 0)
    IdleLoop()
    Jump("loc_28EB")

    label("loc_287C")


    ChrTalk(
        0x101,
        (
            "#12P#00003F...No, we can't do any unnecessary\x01",
            "stops right now.\x02\x03",
            "#00000FLet's leave this place be for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28EB")

    Jump("loc_2AE1")

    label("loc_28F0")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You can see darkness from a creak in the\x01",
            "wooden planks leaned against the wall.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Check Inside]\x01",      # 0
            "[Quitl]\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A72")

    ChrTalk(
        0x101,
        (
            "#12P#00003FAs I thought...\x01",
            "Let's check just in case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00101FRight, somehow it bothers me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00200FThen, let's enter immediately.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("m0304", 0, 0, 0)
    IdleLoop()
    Jump("loc_2AE1")

    label("loc_2A72")


    ChrTalk(
        0x101,
        (
            "#12P#00003F...No, we can't do any unnecessary\x01",
            "stops right now.\x02\x03",
            "#00000FLet's leave this place be for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AE1")

    Jump("loc_2C2B")

    label("loc_2AE6")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You can see darkness from a creak in the\x01",
            "wooden planks leaned against the wall.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#12P#00003F(Mr. Reins, eh...?\x01",
            "Who would've thought he was someone\x01",
            "from a research agency...)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Go To Reins' Hiding Place]\x01",      # 0
            "[Quit]\x01",                           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C2B")
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("m0304", 100, 0, 0)
    IdleLoop()
    Jump("loc_2C2B")

    label("loc_2C2B")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -33410, -5500, 5850, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_14_237C end

    def Function_15_2C62(): pass

    label("Function_15_2C62")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D0B")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The planks leaning against the\x01",
            "wall have been fixed tightly.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00005FIt looks like Mr. Reins has\x01",
            "tightly closed it up since then.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_2D56")

    label("loc_2D0B")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The planks leaning against the\x01",
            "wall have been fixed tightly.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2D56")

    TalkEnd(0xFF)
    Return()

    # Function_15_2C62 end

    def Function_16_2D5A(): pass

    label("Function_16_2D5A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-33310, -3750, 5030, 0)
    MoveCamera(57, 31, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14690, 0)
    SetChrPos(0x101, -33000, -5500, 6670, 180)
    SetChrPos(0x102, -31600, -5500, 6070, 225)
    SetChrPos(0x103, -31790, -5500, 5070, 270)
    SetChrPos(0x104, -33000, -5500, 3860, 0)
    SetChrPos(0xF4, -34400, -5500, 4450, 45)
    SetChrPos(0xF5, -34400, -5500, 5660, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x103,
        (
            "#00203FNevertheless, the\x01",
            "R&A Research, is it...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301FYeah, it seems it's, like,\x01",
            "a quite excellent organization.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00100FYes, to say the least, it's the agency\x01",
            "of that former Colonel Richard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWell, for now it's useless to be\x01",
            "suspicious more than necessary.\x02\x03",
            "#00001FAt any rate, let's proceed with the\x01",
            "preparations to break into the tower now.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -33410, -5500, 5850, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1BF, 3)
    OP_2C(0xB1, 0x2)
    EventEnd(0x5)
    Return()

    # Function_16_2D5A end

    def Function_17_2FD1(): pass

    label("Function_17_2FD1")

    Return()

    # Function_17_2FD1 end

    def Function_18_2FD2(): pass

    label("Function_18_2FD2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(1600, -900, -42250, 0)
    MoveCamera(47, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(26000, 0)
    SetChrPos(0x101, 1600, -3000, -47000, 0)
    SetChrPos(0x102, 2500, -3000, -47900, 0)
    SetChrPos(0x109, 700, -3000, -48500, 0)
    SetChrPos(0x105, 1600, -3000, -40500, 0)

    def lambda_3055():
        OP_96(0xFE, 0x640, 0xFFFFF448, 0xFFFF88DC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3055)
    Sleep(50)

    def lambda_3072():
        OP_96(0xFE, 0x640, 0xFFFFF448, 0xFFFF7B30, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3072)
    Sleep(50)

    def lambda_308F():
        OP_96(0xFE, 0x9C4, 0xFFFFF448, 0xFFFF77AC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_308F)
    Sleep(50)

    def lambda_30AC():
        OP_96(0xFE, 0x2BC, 0xFFFFF448, 0xFFFF7554, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_30AC)
    OP_68(1600, -1900, -32250, 7000)
    MoveCamera(40, 15, 0, 7000)
    SetCameraDistance(15000, 7000)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x105, 1)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        "#12P#00008F#30WWazy...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 1)
    WaitChrThread(0x109, 1)

    ChrTalk(
        0x109,
        "#12P#10106F#30WWazy, uhhm...\x02",
    )

    CloseMessageWindow()
    OP_64(0x105)
    Sleep(500)
    OP_93(0x105, 0xB4, 0x190)
    Sleep(150)

    ChrTalk(
        0x105,
        (
            "#5P#10304F#30W...Ha ha.\x01",
            "It seems I showed you something unsightly.\x02\x03",
            "#10302FMaybe I got a little fired up...\x01",
            "That's not in my style, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FWell...\x02\x03",
            "#00000F...How can I say it,\x01",
            "men are like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FAlthough I don't understand\x01",
            "boys' feelings well...\x02\x03",
            "#00100FI know that you've faced\x01",
            "him in good faith.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10112FYes, yes...!\x02\x03",
            "#10100FI think that one day\x01",
            "he'll understand too!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_33A4")

    ChrTalk(
        0x105,
        (
            "#5P#10304F#30WHu hu...\x01",
            "I hope it's like you say.\x02\x03",
            "#10300F──I'm sorry for taking up our time.\x01",
            "At any rate, let's go somewhere else.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3437")

    label("loc_33A4")


    ChrTalk(
        0x105,
        (
            "#5P#10304F#30WHu hu...\x01",
            "I hope it's like you say.\x02\x03",
            "#10300F──I'm sorry for taking up our time.\x01",
            "Let's clear up the remaining support requests.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3437")

    SetCameraDistance(15500, 1500)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetChrPos(0x0, 1530, -3000, -23230, 0)
    SetScenarioFlags(0x128, 6)
    SetScenarioFlags(0x2, 6)
    OP_1B(0x2, 0x0, 0x2F)
    OP_32(0xFF, 0xFE, 0x0)
    OP_C9(0x1, 0x1000)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_18_2FD2 end

    def Function_19_347A(): pass

    label("Function_19_347A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-10500, 2000, -1000, 0)
    MoveCamera(65, 3, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(30000, 0)
    SetChrPos(0x0, 27600, -300, -2700, 0)
    SetChrPos(0x1, 27600, -300, -2700, 0)
    SetChrPos(0x2, 27600, -300, -2700, 0)
    SetChrPos(0x3, 27600, -300, -2700, 0)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xF7, 0xCD, 0xB7, 0x23, 0x96, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0xE, 0x8000)
    BeginChrThread(0xE, 0, 0, 0)
    SetChrPos(0xE, -4200, -300, -500, 315)
    SetChrFlags(0xD, 0x8000)
    BeginChrThread(0xD, 0, 0, 0)
    SetChrPos(0xD, -5200, -300, 500, 135)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -13300, -300, 12700, 135)

    def lambda_35B2():
        OP_98(0xFE, 0x2AF8, 0x0, 0xFFFFD508, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_35B2)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -14300, -300, 11700, 135)

    def lambda_35E2():
        OP_98(0xFE, 0x2AF8, 0x0, 0xFFFFD508, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_35E2)
    OP_68(-10500, 1000, -1000, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(-7500, 2100, 14100, 0)
    MoveCamera(75, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(21500, 0)
    SetCameraDistance(17500, 4000)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    SetScenarioFlags(0x22, 0)
    NewScene("c1010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_347A end

    def Function_20_366D(): pass

    label("Function_20_366D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30000.itc", 0x1E)
    SoundLoad(835)
    SoundLoad(821)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    BeginChrThread(0xA, 0, 0, 0)
    BeginChrThread(0xD, 0, 0, 0)
    BeginChrThread(0xE, 0, 0, 0)
    BeginChrThread(0x10, 0, 0, 0)
    BeginChrThread(0x13, 0, 0, 0)
    SetChrChipByIndex(0x26, 0x1E)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x8000)
    BeginChrThread(0x26, 0, 0, 0)
    SetChrChipByIndex(0x27, 0x1E)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x27, 0x8000)
    BeginChrThread(0x27, 0, 0, 0)
    SetChrChipByIndex(0x28, 0x1E)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    BeginChrThread(0x28, 0, 0, 0)
    SetChrChipByIndex(0x29, 0x1E)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    BeginChrThread(0x29, 0, 0, 0)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x1000)
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x1000)
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x1000)
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xF, 0x1000)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x26, -23200, -340, 16500, 180)
    SetChrPos(0x27, -18350, -300, 16500, 180)
    SetChrPos(0x28, -18150, -300, 11450, 0)
    SetChrPos(0x29, 1900, -300, -2300, 0)
    SetChrPos(0xF, -19750, -300, 18450, 180)
    SetChrPos(0x10, -18650, -300, 18900, 180)
    SetChrPos(0xE, -20200, -300, 19900, 180)
    SetChrPos(0xD, -22800, -300, 18500, 180)
    SetChrPos(0x13, -21300, -300, 20900, 180)
    SetChrPos(0x11, -18200, -300, 21250, 180)
    SetChrPos(0x8, -18600, -600, 9150, 0)
    SetChrPos(0x9, -17550, -830, 8850, 0)
    SetChrPos(0xA, 1250, -580, -4500, 0)
    SetChrPos(0xB, 2600, -310, -4150, 0)
    SetChrPos(0x12, 2150, -1030, -5050, 0)
    BeginChrThread(0xF, 3, 0, 21)
    BeginChrThread(0xE, 3, 0, 21)
    BeginChrThread(0xD, 3, 0, 21)
    BeginChrThread(0x11, 3, 0, 21)
    BeginChrThread(0x8, 3, 0, 21)
    BeginChrThread(0x9, 3, 0, 21)
    BeginChrThread(0xA, 3, 0, 21)
    BeginChrThread(0xB, 3, 0, 21)
    BeginChrThread(0x12, 3, 0, 21)
    OP_68(-24900, 1000, 12950, 0)
    MoveCamera(55, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_68(-19900, 1000, 12950, 5000)
    MoveCamera(50, 30, 0, 5000)
    SetCameraDistance(15000, 5000)
    Sound(835, 2, 100, 0)
    Sound(821, 2, 50, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    SetChrPos(0x11, 3160, -950, -4950, 0)
    SetChrPos(0xE, 2160, -1250, -5340, 0)
    SetChrPos(0xD, 550, -350, -4150, 0)
    OP_68(-850, 1000, -7900, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13000, 0)
    OP_68(11450, 1750, -350, 5000)
    MoveCamera(60, 20, 0, 5000)
    SetCameraDistance(15000, 5000)
    Sleep(4000)
    StopSound(835, 1000, 100)
    StopSound(821, 1000, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_20_366D end

    def Function_21_39D4(): pass

    label("Function_21_39D4")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_3A0C"),
        (1, "loc_3A14"),
        (2, "loc_3A1C"),
        (3, "loc_3A24"),
        (4, "loc_3A2C"),
        (5, "loc_3A34"),
        (6, "loc_3A3C"),
        (SWITCH_DEFAULT, "loc_3A44"),
    )


    label("loc_3A0C")

    Sleep(100)
    Jump("loc_3A4C")

    label("loc_3A14")

    Sleep(200)
    Jump("loc_3A4C")

    label("loc_3A1C")

    Sleep(300)
    Jump("loc_3A4C")

    label("loc_3A24")

    Sleep(400)
    Jump("loc_3A4C")

    label("loc_3A2C")

    Sleep(500)
    Jump("loc_3A4C")

    label("loc_3A34")

    Sleep(600)
    Jump("loc_3A4C")

    label("loc_3A3C")

    Sleep(700)
    Jump("loc_3A4C")

    label("loc_3A44")

    Sleep(800)
    Jump("loc_3A4C")

    label("loc_3A4C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A77")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xFE)
    Sleep(500)
    Jump("loc_3A4C")

    label("loc_3A77")

    Return()

    # Function_21_39D4 end

    def Function_22_3A78(): pass

    label("Function_22_3A78")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-19500, 1020, 24400, 0)
    MoveCamera(39, 29, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -20800, -320, 24400, 90)
    SetChrPos(0x102, -20000, -320, 23100, 45)
    SetChrPos(0x104, -18400, -320, 25100, 270)
    SetChrPos(0x109, -20000, -320, 25700, 135)
    SetChrPos(0x105, -18400, -320, 23700, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    MoveCamera(49, 25, 0, 3000)
    SetCameraDistance(16500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#6P#00012F*sigh*...\x01",
            "Somehow, all of a sudden I feel tired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00102FRight...\x01",
            "Although I'm glad we could\x01",
            "find Mary safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F...Sorry about my bad\x01",
            "cousin botherin' you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10112FAhaha...\x01",
            "It's not your fault, senior.\x02\x03",
            "#10100FAlso, she looked like\x01",
            "a very good kid to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FRight, no matter what one can say,\x01",
            "she cordially gave us a hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FHa ha...\x01",
            "Well, it's true that she means no harm.\x02\x03",
            "#00306FFor that reason alone, she's quite the bother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00008FI see... It appears there're\x01",
            "many circumstances...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#11P#10304FHu hu, I think that even getting\x01",
            "swang around by a girl's whims\x01",
            "is a man's ability.\x02\x03",
            "#10300FSo, what do we do?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x72, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x77, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EAB")

    ChrTalk(
        0x101,
        (
            "#6P#00004FLet's see...\x01",
            "For now, we're done with the support requests.\x02\x03",
            "#00000FIt could be good to return briefly to\x01",
            "the Support Section and take a break.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F41")

    label("loc_3EAB")


    ChrTalk(
        0x101,
        (
            "#6P#00003FLet's see...\x01",
            "We still have support requests to do.\x02\x03",
            "#00000FIt could be good to return briefly to\x01",
            "the Support Section and take a break.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F41")


    ChrTalk(
        0x102,
        (
            "#12P#00104FRight...\x01",
            "Should we do that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FThen, let's go back to the Support\x01",
            "Section and get some rest, huh?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -18400, -310, 24400, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x140, 5)
    OP_29(0xA3, 0x1, 0xF)
    EventEnd(0x5)
    Return()

    # Function_22_3A78 end

    def Function_23_3FF2(): pass

    label("Function_23_3FF2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch41400.itc", 0x1E)
    LoadChrToIndex("chr/ch41500.itc", 0x1F)
    SoundLoad(821)
    SoundLoad(835)
    ClearChrFlags(0x16, 0x80)
    OP_78(0x8, 0x16)
    OP_49()
    SetChrPos(0x16, -18400, -300, 16800, 225)
    OP_D5(0x16, 0x0, 0x4CE78, 0x0, 0x0)
    SetMapObjFlags(0x8, 0x1000)
    ClearMapObjFlags(0x8, 0x4)
    OP_74(0x8, 0x1E)
    OP_70(0x8, 0x2)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, -20800, -320, 16200, 225)
    SetChrChipByIndex(0x1E, 0x1F)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, -17500, -310, 12900, 225)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrChipByIndex(0x1F, 0x2)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -22000, -300, 12900, 90)
    SetChrChipByIndex(0x20, 0x3)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, -22650, -300, 13500, 90)
    SetChrChipByIndex(0x21, 0x4)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, -20200, -300, 12100, 45)
    SetChrChipByIndex(0x22, 0x5)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, -21700, -300, 11300, 45)
    SetChrChipByIndex(0x23, 0x6)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -19200, -300, 11300, 45)
    SetChrChipByIndex(0x24, 0x8)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, -22500, -300, 15200, 90)
    SetChrChipByIndex(0x25, 0xB)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, -24100, -300, 12850, 90)
    OP_63(0x1F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x21, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x25, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(-20000, 3300, 13800, 0)
    MoveCamera(33, 21, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15500, 0)
    OP_68(-20000, 1300, 13800, 10000)
    Sound(821, 2, 60, 0)
    Sound(835, 2, 80, 0)
    FadeToBright(1500, 0)
    OP_0D()
    SetMessageWindowPos(120, 90, -1, -1)
    SetChrName("President Dieter")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──Of course, like you noticed,\x01",
            "the wicked will is not only one.\x02\x03",
            "The "Calvard Republican Government"...\x02\x03",
            "They too, joining hands with a sly\x01",
            "crime syndicate, are trying to tread\x01",
            "on Crossbell peace and dignity.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x22, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    StopSound(851, 1500, 60)
    StopSound(835, 1500, 80)
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("c0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_23_3FF2 end

    def Function_24_4382(): pass

    label("Function_24_4382")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(13890, -1330, -14740, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(13890, -1330, -14740, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 16400, -2500, -15030, 270)
    SetChrPos(0x102, 18400, -2500, -15030, 270)
    SetChrPos(0x109, 20400, -2500, -15030, 270)
    SetChrPos(0x105, 22400, -2500, -15030, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x0)
    OP_68(1120, -1400, -15440, 3000)
    MoveCamera(45, 13, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(12000, 3000)
    OP_0D()

    def lambda_44EC():
        OP_95(0x101, 1000, -3000, -14740, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_44EC)

    def lambda_4506():
        OP_95(0x102, 2600, -3000, -13540, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4506)

    def lambda_4520():
        OP_95(0x109, 2000, -3000, -15940, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4520)

    def lambda_453A():
        OP_95(0x105, 3600, -2930, -14740, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_453A)

    def lambda_4554():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4554)
    Sleep(300)

    def lambda_4568():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4568)
    Sleep(300)

    def lambda_457C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_457C)
    Sleep(300)

    def lambda_4590():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4590)
    Sleep(1500)
    SetMapObjFlags(0x4, 0x0)
    WaitChrThread(0x101, 1)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    WaitChrThread(0x102, 1)

    def lambda_45DE():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_45DE)
    Sleep(300)

    def lambda_45EE():
        OP_93(0x102, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_45EE)
    Sleep(300)

    def lambda_45FE():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_45FE)
    Sleep(300)

    def lambda_460E():
        OP_93(0x105, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_460E)
    Sleep(300)

    def lambda_461E():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_461E)
    Sleep(300)

    def lambda_462E():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_462E)
    Sleep(300)

    def lambda_463E():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_463E)
    Sleep(300)

    def lambda_464E():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_464E)
    Sleep(300)
    OP_0D()

    def lambda_465F():
        OP_93(0x101, 0x5A, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_465F)

    def lambda_466C():
        OP_93(0x102, 0xB4, 0x5DC)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_466C)

    def lambda_4679():
        OP_93(0x109, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4679)

    def lambda_4686():
        OP_93(0x105, 0x10E, 0x5DC)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4686)
    OP_0D()
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        "#6P#00001FIt's no use...we lost him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FW-What an incredible person.\x02\x03",
            "#10101FIt's like he withdrew knowing\x01",
            "that we were coming...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FWell, a thing of that caliber\x01",
            "should be trivial for him...\x02\x03",
            "#00101FNot for nothing he works as captain\x01",
            "of the intelligence agency.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHu hu, although he uses not\x01",
            "very soldier-like methods.\x02\x03",
            "#10302FSo, do we give up here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FNo...\x01",
            "Anyhow, let's try to follow him.\x02\x03",
            "#00000FMaybe if we inquire the people passing by,\x01",
            "we can figure out his whereabouts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10100FLet's go!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapObjFlags(0x4, 0x10)
    SetScenarioFlags(0x130, 3)
    OP_29(0x66, 0x1, 0x3)
    SetChrPos(0x0, 1000, -3000, -14740, 225)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_24_4382 end

    def Function_25_4909(): pass

    label("Function_25_4909")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(975)
    OP_68(-23060, 4740, 24030, 0)
    MoveCamera(63, 44, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17480, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetMapObjFlags(0xB, 0x1000)
    ClearMapObjFlags(0xB, 0x4)
    OP_78(0xB, 0x17)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x17, -20760, -310, 40300, 180)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_D5(0x17, 0x0, 0x2BF20, 0x0, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    OP_78(0xA, 0x18)
    OP_49()
    SetChrPos(0x18, -13070, -300, 11900, 315)
    OP_D5(0x18, 0x0, 0x4CE78, 0x0, 0x0)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x1000)
    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    OP_74(0xA, 0x1E)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    Sound(486, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(-25830, 4740, 8470, 1500)
    MoveCamera(42, 17, 0, 1500)
    OP_6E(700, 1500)
    SetCameraDistance(14250, 1500)

    def lambda_4A6C():
        OP_9B(0x1, 0xFE, 0x0, 0x61A8, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4A6C)

    def lambda_4A81():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_4A81)
    OP_71(0xB, 0xB5, 0xF0, 0x0, 0x20)
    Sleep(1000)
    Sound(492, 0, 100, 0)
    StopSound(486, 300, 100)
    WaitChrThread(0x17, 1)
    OP_6F(0x79)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_71(0xB, 0x5B, 0x78, 0x0, 0x0)
    WaitChrThread(0x17, 1)
    OP_0D()

    NpcTalk(
        0x17,
        "Sykes",
        "Ha ha, an ambush!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x17,
        "Yuri",
        "Hmph, what shallow thinking.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x17,
        "Yuri",
        "Reggie, can you shake them off?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x17,
        "Reggie",
        (
            "Of course, they aren't\x01",
            "such great opponents!\x02",
        )
    )

    CloseMessageWindow()
    Sound(493, 0, 100, 0)
    OP_9B(0x1, 0x17, 0x0, 0xFFFFF830, 0x1388, 0x0)
    OP_71(0xB, 0x5B, 0x78, 0x0, 0x20)
    Sleep(200)
    OP_71(0xB, 0xB5, 0xF0, 0x0, 0x20)
    OP_9F(0x0, 0x17)
    OP_9F(0x1, -22600, -330, 15200)
    OP_9F(0x1, -28560, -330, 14320)
    OP_9F(0x2, 0x17, 11000, 0x6)

    def lambda_4BDF():
        OP_9B(0x1, 0x17, 0x0, 0x2710, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4BDF)
    Sleep(50)
    Sound(494, 0, 100, 0)
    Sound(975, 2, 100, 0)
    OP_71(0xA, 0x79, 0xB4, 0x0, 0x20)
    OP_96(0x18, 0xFFFFC6A8, 0xFFFFFED4, 0x35DE, 0x1388, 0x0)
    WaitChrThread(0x18, 1)
    OP_9F(0x0, 0x18)
    OP_9F(0x1, -15680, -300, 13790)
    OP_9F(0x1, -18990, -300, 13910)
    OP_9F(0x2, 0x18, 11000, 0x6)
    OP_9B(0x1, 0x18, 0x0, 0x3A98, 0x3A98, 0x0)
    StopSound(975, 300, 100)
    SetScenarioFlags(0x24, 2)
    NewScene("c0100", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_25_4909 end

    def Function_26_4C6D(): pass

    label("Function_26_4C6D")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch23600.itc", 0x1E)
    LoadChrToIndex("chr/ch24200.itc", 0x1F)
    ClearChrFlags(0x1A, 0x80)
    SetChrChipByIndex(0x1A, 0x1E)
    SetChrPos(0x1A, 1200, 0, 7800, 225)
    ClearChrFlags(0x1B, 0x80)
    SetChrChipByIndex(0x1B, 0x1E)
    SetChrPos(0x1B, 1200, 0, 7800, 225)
    OP_68(-790, 690, 5800, 0)
    MoveCamera(44, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16700, 0)
    SetChrPos(0x101, -1400, -300, 4400, 45)
    SetChrPos(0x102, -2150, -300, 5100, 45)
    SetChrPos(0x109, -1700, -300, 3200, 45)
    SetChrPos(0x105, -3400, -300, 4800, 45)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 5)), scpexpr(EXPR_END)), "loc_4EB8")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "～Now Closed～　　\x01",
            "　   Fishing Emperor Club\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#12P#00003FHmm, same as when we saw it back then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FHey, Lloyd.\x01",
            "Don't you have any clue?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FNo, honestly speaking,\x01",
            "I don't have the slightest\x01",
            "about what's happened.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00005FOh...but it looks like\x01",
            "it's not locked?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FC0")

    label("loc_4EB8")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "～Now Closed～　　\x01",
            "　　　Fishing Emperor Club\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#12P#00003FClosed, eh? But what in the world \x01",
            "could the Fishing Emperor Club be...?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00005FOh...but it looks like\x01",
            "it's not locked?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FC0")


    NpcTalk(
        0x1A,
        "Youth's Voice",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5PY-You...\x01",
            "You call yourself a fisherman!?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Man's Voice",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11PT-That's right.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Man's Voice",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11PI won't ever approve of\x01",
            "your forcible methods.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#6P#00105FLloyd, what was that now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FYeah, I know those voices.\x01",
            "Let's enter inside.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    SetScenarioFlags(0x22, 0)
    NewScene("c1020", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_26_4C6D end

    def Function_27_514C(): pass

    label("Function_27_514C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch23600.itc", 0x1E)
    LoadChrToIndex("chr/ch24200.itc", 0x1F)
    SetChrChipByIndex(0x1A, 0x1E)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, -2600, -300, 4800, 225)
    SetChrChipByIndex(0x1B, 0x1F)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, -1800, -300, 4000, 225)
    SetChrFlags(0xD, 0x80)
    EndChrThread(0xD, 0x0)
    OP_68(-1990, 90, 4670, 0)
    MoveCamera(44, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15630, 0)
    SetChrPos(0x101, -3300, 0, 2500, 45)
    SetChrPos(0x102, -4100, 0, 3300, 45)
    SetChrPos(0x109, -3300, 0, 1400, 45)
    SetChrPos(0x105, -5200, 0, 3300, 45)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x1A,
        (
            "#5PHow could a thing like this...\x01",
            "I won't accept it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#11PYes, who'd ever would want\x01",
            "to have the branch stolen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#11PAt any rate, we have to consult\x01",
            "again with Branch Manager Celdan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FHmm, Mr. Peter.\x01",
            "I'm not quite getting\x01",
            "what's going on yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#11PAh, Lloyd, it's because\x01",
            "you've been resting for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#11PAt any rate, let's gather everyone\x01",
            "for now and talk about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#11PI'll call the branch manager\x01",
            "and have him come to the\x01",
            "Back Street "Garante" jazz bar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#11PLloyd, please come too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PAlright, we'll go\x01",
            "on ahead.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5472():
        OP_9B(0x0, 0x1A, 0x5A, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_5472)
    Sleep(50)

    def lambda_548A():
        OP_93(0x101, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_548A)
    Sleep(50)

    def lambda_549A():
        OP_93(0x102, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_549A)
    Sleep(50)
    WaitChrThread(0x1B, 1)

    def lambda_54AE():
        OP_9B(0x0, 0x1B, 0x5A, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_54AE)
    Sleep(50)

    def lambda_54C6():
        OP_93(0x109, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_54C6)
    Sleep(50)

    def lambda_54D6():
        OP_93(0x105, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_54D6)
    Sleep(50)
    WaitChrThread(0x1B, 1)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)

    ChrTalk(
        0x102,
        "#5P#00105FI guess something has really happened.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00003FI don't really get it, but we must\x01",
            "confirm the details anyway.\x02\x03",
            "#00000FLet's head to the jazz bar too.\x02",
        )
    )

    CloseMessageWindow()
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_65(0x2, 0x1)
    SetMapObjFlags(0x0, 0x10)
    OP_D7(0x1E)
    OP_D7(0x1F)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 26200, -300, -1050, 270)
    BeginChrThread(0xD, 1, 0, 1)
    SetScenarioFlags(0x132, 0)
    OP_29(0x6A, 0x1, 0x3)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -4200, 0, 2400, 225)
    EventEnd(0x5)
    Return()

    # Function_27_514C end

    def Function_28_55F3(): pass

    label("Function_28_55F3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(4570, 40, -12620, 0)
    MoveCamera(44, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(33000, 0)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_5690")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x1A2, 0x80)
    Jump("loc_56CF")

    label("loc_5690")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_56B2")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x1A2, 0x80)
    Jump("loc_56CF")

    label("loc_56B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_56CF")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x1A2, 0x80)

    label("loc_56CF")

    OP_68(4570, 40, -12620, 5000)
    MoveCamera(44, 13, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(37220, 5000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_68(-23840, 1240, 8210, 7000)
    MoveCamera(33, 13, 0, 7000)
    OP_6E(600, 7000)
    SetCameraDistance(37220, 7000)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(-20080, 1440, 21740, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16560, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_5843")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x104, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, -19400, -310, 26000, 180)
    SetChrPos(0x102, -20100, -310, 26000, 180)
    SetChrPos(0x101, -19150, -310, 27200, 180)
    SetChrPos(0x104, -20350, -310, 27200, 180)

    def lambda_57D5():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_57D5)

    def lambda_57EF():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_57EF)
    Sleep(100)

    def lambda_580C():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_580C)
    Sleep(50)

    def lambda_5829():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5829)
    Jump("loc_59E6")

    label("loc_5843")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_5917")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x109, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, -19400, -310, 26000, 180)
    SetChrPos(0x102, -20100, -310, 26000, 180)
    SetChrPos(0x101, -19150, -310, 27200, 180)
    SetChrPos(0x109, -20350, -310, 27200, 180)

    def lambda_58A9():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_58A9)

    def lambda_58C3():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_58C3)
    Sleep(100)

    def lambda_58E0():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_58E0)
    Sleep(50)

    def lambda_58FD():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_58FD)
    Jump("loc_59E6")

    label("loc_5917")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_59E6")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x105, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, -19400, -310, 26000, 180)
    SetChrPos(0x102, -20100, -310, 26000, 180)
    SetChrPos(0x101, -19150, -310, 27200, 180)
    SetChrPos(0x105, -20350, -310, 27200, 180)

    def lambda_597D():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_597D)

    def lambda_5997():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5997)
    Sleep(100)

    def lambda_59B4():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_59B4)
    Sleep(50)

    def lambda_59D1():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_59D1)

    label("loc_59E6")

    SetCameraDistance(14560, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x1A2,
        "This is the East Street...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "It's my first time seeing\x01",
            "it at leisure like this.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#6P#00100F*giggle*, does it relax you since\x01",
            "here resembles your home?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "#11PYes, it could be so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#11PUh uh, although I say that\x01",
            "the genuine Eastern District\x01",
            "liveliness is nothing like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#11PIf the occasion permits it,\x01",
            "next time I'd like to show you\x01",
            "around the Republic, miss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "#11PMeaning, I want to take you back with me!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_5C90")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#6P#00112FE-Ehm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FWhat a considerable approach this is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FYeah, to hell with\x01",
            "the sense of humor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E3E")

    label("loc_5C90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_5D6B")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00112FE-Ehm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FWhat a considerable approach this is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FAhaha, in a certain\x01",
            "sense, I could be envious.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E3E")

    label("loc_5D6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_5E3E")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00112FE-Ehm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FWhat a considerable approach this is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHu hu, being frank is a good point, though.\x02",
    )

    CloseMessageWindow()

    label("loc_5E3E")

    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x8000)
    OP_1B(0x8, 0x0, 0x2D)
    SetScenarioFlags(0x153, 6)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -19750, -310, 26000, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_28_55F3 end

    def Function_29_5EB4(): pass

    label("Function_29_5EB4")

    EventBegin(0x0)
    Fade(500)
    LoadChrToIndex("chr/ch03400.itc", 0x1E)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04600.itp")
    SoundLoad(3949)
    OP_68(-5300, -1400, -11050, 0)
    MoveCamera(44, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13490, 0)
    SetChrPos(0x101, -5200, -3000, -10840, 0)
    SetChrPos(0x102, -3970, -3000, -10800, 0)
    SetChrPos(0x109, -6270, -3000, -10440, 45)
    SetChrPos(0x104, -2970, -3000, -11500, 315)
    SetChrPos(0x105, -3950, -3000, -12150, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0xB, 0xFF)
    OP_0D()

    ChrTalk(
        0xB,
        "Oh, do you need something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FYes, I'd like to ask\x01",
            "you something.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained the situation and\x01",
            "asked if Mary the kitty came there.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        (
            "Ah, Mr. Bond's family kitty, right?\x01",
            "If police are searching for her, it's reassuring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Still, unfortunately I haven't\x01",
            "seen her today yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "For that reason, her favorite\x01",
            "dried food I put there is\x01",
            "still like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "At least, I guess she hasn't come\x01",
            "here since last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00103FIs that so...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "That family have been my\x01",
            "regular customers, so\x01",
            "I'd like to be of help...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Please, find her in a way or another.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYes, naturally.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100FThank you for your cooperation.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x104, 3, 0, 32)
    Sleep(100)
    BeginChrThread(0x105, 3, 0, 34)
    Sleep(100)
    BeginChrThread(0x102, 3, 0, 31)
    Sleep(100)
    BeginChrThread(0x101, 3, 0, 30)
    Sleep(100)
    BeginChrThread(0x109, 3, 0, 33)
    OP_68(2580, -1400, -13440, 5000)
    MoveCamera(32, 28, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(15530, 5000)
    WaitChrThread(0x109, 3)
    OP_6F(0x79)

    ChrTalk(
        0x104,
        "#00303FSo the first one was a miss, eh?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#12P#10105FMr. Lloyd, what're\x01",
            "we going to do now?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000FYes, for now let's do a general\x01",
            "inquiry in the neighborhood...\x02\x03",
            "#00003FThen, the search range could end up widening,\x01",
            "so maybe we can only count on Zeit's nose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00105FI think it's okay, but...\x02\x03",
            "#00106F...In a situation where Tio isn't around, I wonder\x01",
            "if we'll be able to understand each other well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FYou're right...\x02\x03",
            "#00000FBut still, we could use\x01",
            "some gesturing and...\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x1C, 0x1E)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 2270, -220, -3590, 180)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x1C,
        "Young Girl's Voice",
        "#3949VOoh, what're you up to?\x02",
    )

    CloseMessageWindow()
    OP_24(0xF6D)
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-1420, 800, -15420, 3000)
    MoveCamera(35, 19, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(13050, 3000)

    def lambda_6593():

        label("loc_6593")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_6593")

    QueueWorkItem2(0x101, 1, lambda_6593)

    def lambda_65A5():

        label("loc_65A5")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_65A5")

    QueueWorkItem2(0x104, 1, lambda_65A5)

    def lambda_65B7():

        label("loc_65B7")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_65B7")

    QueueWorkItem2(0x102, 1, lambda_65B7)

    def lambda_65C9():

        label("loc_65C9")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_65C9")

    QueueWorkItem2(0x109, 1, lambda_65C9)

    def lambda_65DB():

        label("loc_65DB")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_65DB")

    QueueWorkItem2(0x105, 1, lambda_65DB)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00011FWha...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FRandy's...\x02",
    )

    CloseMessageWindow()
    OP_68(870, -1400, -12100, 4000)
    MoveCamera(53, 30, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(14790, 4000)
    OP_95(0x1C, 1340, -3000, -9310, 2000, 0x0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    WaitChrThread(0x1C, 1)
    OP_6F(0x79)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x1C,
        (
            "Randy bro and...\x01",
            "Misters and misses.\x02\x03",
            "What're you doing here?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x104,
        (
            "#00303F... Nothing you should care 'bout.\x01",
            "Scram at once.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x1C,
        (
            "#04606FMrr, you're so unfriendly.\x02\x03",
            "#04600FThen, should I ask the body\x01",
            "of the miss over there?\x02\x03",
            "#04609FI want to try to fondle them\x01",
            "with all my might again㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00112FW-Wait...!\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_9B(0x1, 0x102, 0xB4, 0x1F4, 0x5DC, 0x0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_64(0x102)

    ChrTalk(
        0x101,
        (
            "#12P#00003F...As you can see, we're doing\x01",
            "a Special Support Section job.\x02\x03",
            "#00001FIt has nothing to do with you, so\x01",
            "could you please not get involved?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1C, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1C,
        (
            "#04606FHmm, I don't intend\x01",
            "to get involved at all...\x02\x03",
            "#04600FBy the way, what kind of job is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006F*sigh*...it can't be helped.\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You explained by summarizing the\x01",
            "request about the kitty case.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x1C,
        (
            "#04605FEeeh, I see.\x02\x03",
            "#04600FSo, how're you going to search\x01",
            "for that Mary from now on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FYes, we are going to rely on a \x01",
            "police dog, following the same...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#04609FAhaha, that won't do.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00005FHuh...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#04602FMister, you seem to know well about dogs,\x01",
            "but as for cats, you still have a long way to go.\x02\x03",
            "#04604FYou must, you know, think about\x01",
            "that Mary's feelings more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006FW-What do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#04600FShirley doesn't know the details, but that\x01",
            "family...did they move recently?\x02\x03",
            "#04604FIn that case, I think the answer is only one.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00105FI see, I wonder why we\x01",
            "didn't notice earlier.\x02\x03",
            "#00100FIt's Residential Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#04600FEeh, so her former house is there?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00005FI see, Mary has been trying to\x01",
            "go back home since the beginning...!\x02\x03",
            "#00001FHowever, not towards her new house, but\x01",
            "towards the one she was living in before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10103FI see, in that case it\x01",
            "really makes sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10303FIf anything, they say the dogs become\x01",
            "familiar with people, the cats with home.\x02\x03",
            "#10300FYou figure it immediately if you think\x01",
            "about the action patterns of a cat after\x01",
            "it has been separated from its owner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F...It's true that even Koppe never\x01",
            "left from the Support Section building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#04609FAhaha, that's exactly it.\x02\x03",
            "#04602FThen, Shirley will go on ahead, 'k?♪\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1C, 0x0, 0x1F4)
    Sleep(300)

    def lambda_7061():
        OP_95(0xFE, 2270, -220, -3590, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_7061)
    Sleep(1000)
    OP_68(1440, -1400, -13650, 3000)
    MoveCamera(27, 27, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(14300, 3000)
    OP_6F(0x79)
    SetChrFlags(0x1C, 0x80)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FD-Don't tell me...\x01",
            "She wants to poke her nose in it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHu hu, likely.\x02\x03",
            "#10300FA really whimsical kitty...\x01",
            "Well, should I say a tiger cub, maybe?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10106FThere's nothing to joke about, though...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FU-Uhhm...\x01",
            "What's got into her, I wonder?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F...Well, she's not that dangerous\x01",
            "unless fightin' isn't involved.\x02\x03",
            "#00300FShe could get bored immediately, so\x01",
            "let's go have a look at the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FUnderstood...\x01",
            "Let's quickly make to the Residential Street too.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x155, 1)
    OP_29(0x74, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 2000, -3000, -11920, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_29_5EB4 end

    def Function_30_736E(): pass

    label("Function_30_736E")

    OP_95(0x101, 750, -3000, -12700, 2000, 0x0)
    OP_93(0x101, 0x5A, 0x1F4)
    Return()

    # Function_30_736E end

    def Function_31_738A(): pass

    label("Function_31_738A")

    OP_95(0x102, 2530, -3000, -11630, 2000, 0x0)
    OP_93(0x102, 0xB4, 0x1F4)
    Return()

    # Function_31_738A end

    def Function_32_73A6(): pass

    label("Function_32_73A6")

    OP_95(0x104, 3790, -3000, -12940, 2000, 0x0)
    OP_93(0x104, 0x10E, 0x1F4)
    Return()

    # Function_32_73A6 end

    def Function_33_73C2(): pass

    label("Function_33_73C2")

    OP_95(0x109, 1400, -3000, -14510, 2000, 0x0)
    OP_93(0x109, 0x2D, 0x1F4)
    Return()

    # Function_33_73C2 end

    def Function_34_73DE(): pass

    label("Function_34_73DE")

    OP_95(0x105, 3200, -3000, -14560, 2000, 0x0)
    OP_93(0x105, 0x13B, 0x1F4)
    Return()

    # Function_34_73DE end

    def Function_35_73FA(): pass

    label("Function_35_73FA")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_784D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7805")

    ChrTalk(
        0x1A2,
        "Fisherman Emperor Club...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FAh, that is read as in\x01",
            ""Fishing Emperor Club".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Hmph, I don't really get it, but it means\x01",
            "it's a gather of fishing enthusiasts, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "So their race exists\x01",
            "in Crossbell too.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00105FYou mean that in the Republic too?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "Yes, there's this there too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Incidentally, grandfather has\x01",
            "a taste for fishing too, but\x01",
            "frankly, I don't understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "After all, to get fish the\x01",
            "most efficient way is to\x01",
            "use a net.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_76AE")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_7666():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7666)
    Sleep(50)

    def lambda_7676():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7676)
    Sleep(50)

    def lambda_7686():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7686)
    Sleep(300)

    ChrTalk(
        0x104,
        "#00306FSo blunt...\x02",
    )

    CloseMessageWindow()
    Jump("loc_77FD")

    label("loc_76AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_7753")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_7707():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7707)
    Sleep(50)

    def lambda_7717():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7717)
    Sleep(50)

    def lambda_7727():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7727)
    Sleep(300)

    ChrTalk(
        0x109,
        "#10106FSo outspoken...\x02",
    )

    CloseMessageWindow()
    Jump("loc_77FD")

    label("loc_7753")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_77FD")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_77AC():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_77AC)
    Sleep(50)

    def lambda_77BC():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_77BC)
    Sleep(50)

    def lambda_77CC():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_77CC)
    Sleep(300)

    ChrTalk(
        0x105,
        "#10304FHu hu, he's so outspoken.\x02",
    )

    CloseMessageWindow()

    label("loc_77FD")

    SetScenarioFlags(0x1, 6)
    Jump("loc_7848")

    label("loc_7805")


    ChrTalk(
        0x1A2,
        (
            "I have no interest for such a place.\x01",
            "Let's go somewhere else.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7848")

    Jump("loc_7B27")

    label("loc_784D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7863")
    Call(0, 26)
    Jump("loc_7B27")

    label("loc_7863")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A80")
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked and there\x01",
            "is a message plate.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "～Now Closed～　　\x01",
            "　　　Fishing Emperor Club\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00005FClosed, eh? But what could the\x01",
            ""Fishing Emperor Club" be...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FThis place is the building of the\x01",
            ""Fisherman's Guild" you joined to.\x02\x03",
            "#00100FHaven't you heard anything\x01",
            "from the other members?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FNo, I've been busy lately and\x01",
            "I haven't kept up fishing.\x02\x03",
            "#00000FIt also looks like it's locked,\x01",
            "so we'll visit another time...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13F, 5)
    Jump("loc_7B27")

    label("loc_7A80")

    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked and there\x01",
            "is a message plate.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "～Now Closed～　　\x01",
            "　　　Fishing Emperor Club\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_7B27")

    TalkEnd(0xFF)
    Return()

    # Function_35_73FA end

    def Function_36_7B2B(): pass

    label("Function_36_7B2B")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7CD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C3A")

    ChrTalk(
        0x1A2,
        "Hm, is this an apartment?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Are there some kind of interesting\x01",
            "things in here...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FNo, that's not the case...\x01\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Hmph, then there's no meaning in going inside.\x01",
            "Let's go to the next place at once.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_7CD8")

    label("loc_7C3A")


    ChrTalk(
        0x1A2,
        (
            "It's not in my style rudely breaking\x01",
            "into strangers' dwellings without\x01",
            "having any particular business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "Come on, let's go to the next place at once.\x02",
    )

    CloseMessageWindow()

    label("loc_7CD8")

    TalkEnd(0xFF)
    Return()

    # Function_36_7B2B end

    def Function_37_7CDC(): pass

    label("Function_37_7CDC")

    EventBegin(0x2)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "An Eastern Jizｷ Buddha is enshrined here.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7E9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E98")

    ChrTalk(
        0x1A2,
        (
            "A Jizｷ Buddha, eh...?\x01",
            "It really looks like those of the Eastern District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FAs I thought, are there many there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Yeah, there're many kinds depending\x01",
            "on the benefits asked for, like the\x01",
            "burnt Jizｷ or the thorn-pulling Jizｷ...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Well, I don't believe\x01",
            "in such invisible\x01",
            "benefits though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FI-I see...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DC, 4)
    EventEnd(0x3)
    Return()

    label("loc_7E98")

    EventEnd(0x3)
    Return()

    label("loc_7E9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8151")

    ChrTalk(
        0x101,
        (
            "#00000FThis Jizｷ...\x01",
            "It's always being carefully cleaned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIt looks like it's fervently\x01",
            "visited by someone.\x02\x03",
            "Since we are here, why don't\x01",
            "we too offer a dish we made?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8000")

    ChrTalk(
        0x105,
        (
            "#10300FEeh, the Support Section\x01",
            "does these things too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHa ha...it's not always, though.\x01",
            "It'll also be cooking practice, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8046")

    label("loc_8000")


    ChrTalk(
        0x104,
        (
            "#00300FWell, let's give it a try.\x01",
            "It'll be cooking practice too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8046")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_80E9")

    ChrTalk(
        0x109,
        (
            "#10100FThat's nice, I approve!\x01",
            "It looks like we should be\x01",
            "making improvements...\x02\x03",
            "Let's try bringing it Superb\x01",
            "dishes when we have them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_814E")

    label("loc_80E9")


    ChrTalk(
        0x103,
        (
            "#00200FWe should make\x01",
            "quick progresses.\x02\x03",
            "Let's try bringing it Superb\x01",
            "dishes when we have them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_814E")

    SetScenarioFlags(0x20B, 0)

    label("loc_8151")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A469")
    Call(0, 38)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81CF")

    ChrTalk(
        0x101,
        (
            "#0000FNow we don't have any\x01",
            "suitable dishes to offer.\x02\x03",
            "Let's try bringing them next time.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x3)
    Return()

    label("loc_81CF")

    Call(0, 39)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 6)), scpexpr(EXPR_END)), "loc_81F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_81ED")
    Call(0, 40)
    Return()

    label("loc_81ED")

    Jump("loc_A469")

    label("loc_81F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8677")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A letter accompanies a small package.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You, who always offer dishes...\x01",
            "Thank you very much for offering a\x01",
            "lot of dishes to the venerable Jizｷ.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Actually, I have been living nearby with my father since\x01",
            "I was little, and from that time, because I prayed to it\x01",
            "every day, I feel attached to the venerable Jizｷ.\x01",
            "Nowadays there are very few people who\x01",
            "come to visit it, but by feeling glad in\x01",
            "secret that there are heart-warming people\x01",
            "like you, somehow I felt even relieved.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is something very reassuring that there is\x01",
            "someone with the same resolve aside myself.\x01",
            "I am sorry for another very long letter.\x01",
            "This is a mere little gift, please accept\x01",
            "it as a token of my gratitude.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is a pity that I can't meet you in person yet,\x01",
            "but being still healthy I will be able to regularly\x01",
            "visit the venerable Jizｷ every day like this.\x01",
            "Maybe one day I will be able to meet you too.\x01\x01",
            "                  From a neighbor you don't know\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "From inside the package, Tearal Balms appeared.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2 obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1F6, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x20B, 6)
    SetScenarioFlags(0x2, 0)
    Jump("loc_A469")

    label("loc_8677")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8B27")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a letter bundled\x01",
            "with a Teara Balm.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "With the strong sunlight and the green grass steadily\x01",
            "growing, I think the summer presence has finally arrived.\x01",
            "To you who always offer dishes, \x01",
            "I wish you good health day after day.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Speaking about me, when the other day I stopped by the \x01",
            "public office, I had the opportunity to coincidentally meet \x01",
            "an acquaintance of when I was a student.\x01",
            "She had been away from Crossbell for a very long time,\x01",
            "but she came back because of the son's family moving.\x01",
            "Since we really bumped into each other,\x01",
            "we both were greatly surprised.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The temper we had when we were young didn't change,\x01",
            "even with growing old. We longly forgot to keep in\x01",
            "touch with each other and we ended up in reminiscent\x01",
            "talks about what was in vogue in what year, and that\x01",
            "it was hard during the war...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Such a fortuitous luckily coincidence meeting\x01",
            "maybe was arranged by the venerable Jizｷ.\x01",
            "I ended up talking to you about something\x01",
            "boring. I will keep praying for your good\x01",
            "health. Allow me to close the letter like this.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1F5, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x20B, 5)
    Jump("loc_A469")

    label("loc_8B27")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8F23")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a letter bundled\x01",
            "with a Teara Balm.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You, who always offer dishes, \x01",
            "I wonder how you spent this day?\x01",
            "I really thank you very much for always\x01",
            "coming to visit the venerable Jizｷ.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The other day, when it came to stand in the kitchen\x01",
            "thinking about a delicious dish to offer as always,\x01",
            "I suddenly thought "let's try preparing that" and I\x01",
            "remembered...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When I was little, I was strictly trained in cooking by\x01",
            "my mother. I was enthusiastic thinking it was fine, but\x01",
            "like you can imagine, not everything goes in such a\x01",
            "smooth way. What she fussed over above all else was\x01",
            "the cream stew which had a little different seasoning\x01",
            "than always. The people in the house told me that\x01",
            "it was good, though.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "These are time of endless incidents,\x01",
            "but I am deeply grateful to her for being\x01",
            "able to live every day like this.\x01",
            "May you be visited by calm days too.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1F5, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x20B, 4)
    Jump("loc_A469")

    label("loc_8F23")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_936E")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a letter bundled\x01",
            "with a Teara Balm.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The many days with a little rain are continuing in\x01",
            "this season...I wonder how are you spending them?\x01",
            "Thinking that, if you are keeping to offer\x01",
            "dishes you will be reading this for sure,\x01",
            "I selfishly write to you again.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "During yesterday, when I was looking\x01",
            "at the bustling street, I happened to see\x01",
            "energetic kids running around happily.\x01",
            "They are kids I can see often in this neighborhood, but I\x01",
            "think that it is pleasant that they get along well every day.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Crossbell somewhat gathers the attention of society,\x01",
            "so isn't children's sound growth the best treasure\x01",
            "for this city? I kept thinking about this and other\x01",
            "things over and over... It would be really nice if\x01",
            "calm days were to continue on forever.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I have arrived at the end of this letter, but once again I \x01",
            "selfishly allowed myself to prepare a little gift for you.\x01",
            "I would be happy if it could be useful to you in some way.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1F5, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x20B, 3)
    Jump("loc_A469")

    label("loc_936E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_95D8")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a letter bundled\x01",
            "with a Teara Balm.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Thank you very much to you\x01",
            "who always offer dishes.\x01",
            "Seeing that there is someone aside from me who\x01",
            "fervently visits the venerable Jizｷ and seeing every\x01",
            "time those delicious looking offerings, my days\x01",
            "continued feeling relieved and heart-warmed.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I don't know who you are, but today I selfishly \x01",
            "allowed myself to prepare a little gift for you.\x01",
            "Please accept it considering it\x01",
            "something for your habitual devotion.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1F5, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x20B, 2)
    Jump("loc_A469")

    label("loc_95D8")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Offer a Superb dish?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9605")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A469")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x190, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9661")
    MenuCmd(1, 1, "Celestial Noodles "Sun"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 0)), scpexpr(EXPR_END)), "loc_9657")
    Call(2, 6)

    label("loc_9657")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9661")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x193, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_969F")
    MenuCmd(1, 1, "Immortal Mapo "Qilin"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 1)), scpexpr(EXPR_END)), "loc_9695")
    Call(2, 6)

    label("loc_9695")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_969F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x196, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_96DB")
    MenuCmd(1, 1, "Peerless Fried Rice")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 2)), scpexpr(EXPR_END)), "loc_96D1")
    Call(2, 6)

    label("loc_96D1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_96DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x199, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_971F")
    MenuCmd(1, 1, "First-Rate Steak "Strength"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 3)), scpexpr(EXPR_END)), "loc_9715")
    Call(2, 6)

    label("loc_9715")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_971F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9756")
    MenuCmd(1, 1, "Three-Day Stew")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 4)), scpexpr(EXPR_END)), "loc_974C")
    Call(2, 6)

    label("loc_974C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9756")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9796")
    MenuCmd(1, 1, "Land Hot Pot "Glorious"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 5)), scpexpr(EXPR_END)), "loc_978C")
    Call(2, 6)

    label("loc_978C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9796")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_97D3")
    MenuCmd(1, 1, "Hot Pot "Calm Cloud"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 6)), scpexpr(EXPR_END)), "loc_97C9")
    Call(2, 6)

    label("loc_97C9")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_97D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9811")
    MenuCmd(1, 1, "Express Fries "Rapid"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 7)), scpexpr(EXPR_END)), "loc_9807")
    Call(2, 6)

    label("loc_9807")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9811")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A8, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_984A")
    MenuCmd(1, 1, "Mega Omelet Rice")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 0)), scpexpr(EXPR_END)), "loc_9840")
    Call(2, 6)

    label("loc_9840")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_984A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AB, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9887")
    MenuCmd(1, 1, "Jade Noodles "Sooth"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 1)), scpexpr(EXPR_END)), "loc_987D")
    Call(2, 6)

    label("loc_987D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9887")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AE, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_98BD")
    MenuCmd(1, 1, "Double Burger")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 2)), scpexpr(EXPR_END)), "loc_98B3")
    Call(2, 6)

    label("loc_98B3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_98BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_98FA")
    MenuCmd(1, 1, "Quattro Cheese Pizza")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 3)), scpexpr(EXPR_END)), "loc_98F0")
    Call(2, 6)

    label("loc_98F0")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_98FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9934")
    MenuCmd(1, 1, "Powerful Sandwich")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 4)), scpexpr(EXPR_END)), "loc_992A")
    Call(2, 6)

    label("loc_992A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9934")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9972")
    MenuCmd(1, 1, "Lunch Box "Sincerity"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 5)), scpexpr(EXPR_END)), "loc_9968")
    Call(2, 6)

    label("loc_9968")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9972")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BA, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_99A9")
    MenuCmd(1, 1, "Brilliant Soup")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 6)), scpexpr(EXPR_END)), "loc_999F")
    Call(2, 6)

    label("loc_999F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_99A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BD, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_99DE")
    MenuCmd(1, 1, "Wonder Candy")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 7)), scpexpr(EXPR_END)), "loc_99D4")
    Call(2, 6)

    label("loc_99D4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_99DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C0, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9A1F")
    MenuCmd(1, 1, "Heavenly "Midnight Moon"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 0)), scpexpr(EXPR_END)), "loc_9A15")
    Call(2, 6)

    label("loc_9A15")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9A1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C3, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9A5F")
    MenuCmd(1, 1, "RoyalSweet "Snow White"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 1)), scpexpr(EXPR_END)), "loc_9A55")
    Call(2, 6)

    label("loc_9A55")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9A5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C6, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9A9F")
    MenuCmd(1, 1, "Sherbert "Seven Colors"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 2)), scpexpr(EXPR_END)), "loc_9A95")
    Call(2, 6)

    label("loc_9A95")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9A9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C9, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9AD5")
    MenuCmd(1, 1, "Snack "Pulse"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 3)), scpexpr(EXPR_END)), "loc_9ACB")
    Call(2, 6)

    label("loc_9ACB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9AD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CC, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9B11")
    MenuCmd(1, 1, "Tea "Summer Breeze"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 4)), scpexpr(EXPR_END)), "loc_9B07")
    Call(2, 6)

    label("loc_9B07")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9B11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CF, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9B50")
    MenuCmd(1, 1, "Nectar "Bluish Purple"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 5)), scpexpr(EXPR_END)), "loc_9B46")
    Call(2, 6)

    label("loc_9B46")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9B50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9B8B")
    MenuCmd(1, 1, ""Nightmare Killer"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 6)), scpexpr(EXPR_END)), "loc_9B81")
    Call(2, 6)

    label("loc_9B81")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9B8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9BC6")
    MenuCmd(1, 1, "Water "Shangri-la"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 7)), scpexpr(EXPR_END)), "loc_9BBC")
    Call(2, 6)

    label("loc_9BBC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9BC6")

    MenuCmd(1, 1, "Quit")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9C08")
    Sleep(500)
    Jump("loc_A464")

    label("loc_9C08")

    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x190, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9C72")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C68")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x190, 1)
    SetScenarioFlags(0x208, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x190),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " offered.\x02",
        )
    )


    label("loc_9C68")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9C72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x193, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9CBD")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9CB3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x193, 1)
    SetScenarioFlags(0x208, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x193),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " offered.\x02",
        )
    )


    label("loc_9CB3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9CBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x196, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9D08")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9CFE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x196, 1)
    SetScenarioFlags(0x208, 2)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x196),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " offered.\x02",
        )
    )


    label("loc_9CFE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9D08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x199, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9D53")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D49")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x199, 1)
    SetScenarioFlags(0x208, 3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x199),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " offered.\x02",
        )
    )


    label("loc_9D49")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9D53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9D9E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D94")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x19C, 1)
    SetScenarioFlags(0x208, 4)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x19C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " offered.\x02",
        )
    )


    label("loc_9D94")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9D9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9DE9")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9DDF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x19F, 1)
    SetScenarioFlags(0x208, 5)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x19F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " offered.\x02",
        )
    )


    label("loc_9DDF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9DE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9E34")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E2A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1A2, 1)
    SetScenarioFlags(0x208, 6)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1A2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " offered.\x02",
        )
    )


    label("loc_9E2A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9E34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9E7F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E75")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1A5, 1)
    SetScenarioFlags(0x208, 7)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1A5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " offered.\x02",
        )
    )


    label("loc_9E75")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9E7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A8, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9ECA")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9EC0")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1A8, 1)
    SetScenarioFlags(0x209, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1A8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " offered.\x02",
        )
    )


    label("loc_9EC0")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9ECA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AB, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9F15")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F0B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1AB, 1)
    SetScenarioFlags(0x209, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1AB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " offered.\x02",
        )
    )


    label("loc_9F0B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9F15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AE, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9F60")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F56")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1AE, 1)
    SetScenarioFlags(0x209, 2)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1AE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " offered.\x02",
        )
    )


    label("loc_9F56")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9F60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9FAB")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9FA1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1B1, 1)
    SetScenarioFlags(0x209, 3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1B1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " offered.\x02",
        )
    )


    label("loc_9FA1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9FAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9FF6")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9FEC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1B4, 1)
    SetScenarioFlags(0x209, 4)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1B4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " offered.\x02",
        )
    )


    label("loc_9FEC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9FF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A041")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A037")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1B7, 1)
    SetScenarioFlags(0x209, 5)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1B7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " offered.\x02",
        )
    )


    label("loc_A037")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A041")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BA, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A08C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A082")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1BA, 1)
    SetScenarioFlags(0x209, 6)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1BA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " offered.\x02",
        )
    )


    label("loc_A082")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A08C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BD, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A0D7")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0CD")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1BD, 1)
    SetScenarioFlags(0x209, 7)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1BD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " offered.\x02",
        )
    )


    label("loc_A0CD")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A0D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C0, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A122")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A118")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1C0, 1)
    SetScenarioFlags(0x20A, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1C0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " offered.\x02",
        )
    )


    label("loc_A118")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C3, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A16D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A163")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1C3, 1)
    SetScenarioFlags(0x20A, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1C3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " offered.\x02",
        )
    )


    label("loc_A163")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A16D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C6, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A1B8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1AE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1C6, 1)
    SetScenarioFlags(0x20A, 2)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1C6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " offered.\x02",
        )
    )


    label("loc_A1AE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A1B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C9, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A203")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1F9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1C9, 1)
    SetScenarioFlags(0x20A, 3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1C9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " offered.\x02",
        )
    )


    label("loc_A1F9")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A203")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CC, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A24E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A244")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1CC, 1)
    SetScenarioFlags(0x20A, 4)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1CC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " offered.\x02",
        )
    )


    label("loc_A244")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A24E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CF, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A299")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A28F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1CF, 1)
    SetScenarioFlags(0x20A, 5)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1CF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " offered.\x02",
        )
    )


    label("loc_A28F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A299")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A2E4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2DA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1D2, 1)
    SetScenarioFlags(0x20A, 6)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " offered.\x02",
        )
    )


    label("loc_A2DA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A2E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A32F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A325")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1D5, 1)
    SetScenarioFlags(0x20A, 7)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " offered.\x02",
        )
    )


    label("loc_A325")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A32F")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A464")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A461")

    ChrTalk(
        0x101,
        (
            "#00000FAll right, all set.\x01",
            "...I guess we'll try to bring something again.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A45E")

    ChrTalk(
        0x102,
        (
            "#00100FSince I think it would be rude bringing\x01",
            "always the same dishes, it would be nice\x01",
            "to offer at least one different every time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, let's do that.\x02",
    )

    CloseMessageWindow()

    label("loc_A45E")

    SetScenarioFlags(0x20B, 1)

    label("loc_A461")

    SetScenarioFlags(0x2, 0)

    label("loc_A464")

    Jump("loc_9605")

    label("loc_A469")

    EventEnd(0x3)
    Return()

    # Function_37_7CDC end

    def Function_38_A46C(): pass

    label("Function_38_A46C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x190, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A48F")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A48F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x193, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A4A8")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A4A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x196, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A4C1")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A4C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x199, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A4DA")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A4DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A4F3")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A4F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A50C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A50C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A525")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A525")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A53E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A53E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A8, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A557")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AB, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A570")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A570")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AE, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A589")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A589")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A5A2")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A5A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A5BB")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A5BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A5D4")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A5D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BA, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A5ED")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A5ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BD, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A606")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C0, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A61F")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A61F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C3, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A638")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A638")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C6, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A651")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C9, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A66A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A66A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CC, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A683")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A683")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CF, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A69C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A69C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A6B5")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A6B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A6CE")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A6CE")

    Return()

    # Function_38_A46C end

    def Function_39_A6CF(): pass

    label("Function_39_A6CF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 0)), scpexpr(EXPR_END)), "loc_A6EC")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A6EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 1)), scpexpr(EXPR_END)), "loc_A6FF")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A6FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 2)), scpexpr(EXPR_END)), "loc_A712")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A712")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 3)), scpexpr(EXPR_END)), "loc_A725")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A725")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 4)), scpexpr(EXPR_END)), "loc_A738")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A738")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 5)), scpexpr(EXPR_END)), "loc_A74B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A74B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 6)), scpexpr(EXPR_END)), "loc_A75E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A75E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 7)), scpexpr(EXPR_END)), "loc_A771")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A771")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 0)), scpexpr(EXPR_END)), "loc_A784")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A784")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 1)), scpexpr(EXPR_END)), "loc_A797")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A797")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 2)), scpexpr(EXPR_END)), "loc_A7AA")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A7AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 3)), scpexpr(EXPR_END)), "loc_A7BD")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A7BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 4)), scpexpr(EXPR_END)), "loc_A7D0")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A7D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 5)), scpexpr(EXPR_END)), "loc_A7E3")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A7E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 6)), scpexpr(EXPR_END)), "loc_A7F6")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A7F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 7)), scpexpr(EXPR_END)), "loc_A809")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A809")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 0)), scpexpr(EXPR_END)), "loc_A81C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A81C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 1)), scpexpr(EXPR_END)), "loc_A82F")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A82F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 2)), scpexpr(EXPR_END)), "loc_A842")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A842")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 3)), scpexpr(EXPR_END)), "loc_A855")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A855")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 4)), scpexpr(EXPR_END)), "loc_A868")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A868")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 5)), scpexpr(EXPR_END)), "loc_A87B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A87B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 6)), scpexpr(EXPR_END)), "loc_A88E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A88E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 7)), scpexpr(EXPR_END)), "loc_A8A1")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A8A1")

    Return()

    # Function_39_A6CF end

    def Function_40_A8A2(): pass

    label("Function_40_A8A2")

    EventBegin(0x0)
    Fade(1000)
    OP_68(14950, 1450, 2880, 0)
    MoveCamera(44, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14180, 0)
    SetChrPos(0x101, 16200, -300, 2570, 0)
    SetChrPos(0x102, 17600, -300, 2700, 0)
    SetChrPos(0x103, 15750, -300, 1260, 0)
    SetChrPos(0x104, 17570, -300, 1120, 0)
    SetChrPos(0xF4, 15720, -300, 20, 0)
    SetChrPos(0xF5, 16940, -300, 30, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xD, 0x80)
    LoadChrToIndex("chr/ch23300.itc", 0x1E)
    SetChrChipByIndex(0x2A, 0x1E)
    SetChrSubChip(0x2A, 0x0)
    ClearChrFlags(0x2A, 0x80)
    SetChrFlags(0x2A, 0x8000)
    SetChrPos(0x2A, -3400, -300, 1670, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000F(...The Jizｷ we offered the dishes to, eh...?\x01",
            "I'm not a prayer of their religion, but...)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_93(0x101, 0xB4, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00002FSay, everyone, since we're here, why don't\x01",
            "we pray to the Jizｷ before setting out?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0xE1, 0x1F4)

    ChrTalk(
        0x102,
        "#00100FMy, why not?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AABB")

    ChrTalk(
        0x109,
        (
            "#10100FA prayer for rescuing KeA?\x01",
            "...I agree too!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AABB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AB05")

    ChrTalk(
        0x10A,
        (
            "#00606FHmph, we don't have\x01",
            "time for this, however...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB05")


    ChrTalk(
        0x103,
        (
            "#00202FWell, it won't take that much time...\x01",
            "Such a thing is a question of feelings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FThinkin' about the morale from now on,\x01",
            "I guess it's not bad for mental concentration.\x02\x03",
            "#00309FAlright, let's do it!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x0, 0x1F4)

    ChrTalk(
        0x102,
        (
            "#00100FAs an Eastern custom, you\x01",
            "join your hands like this...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        "#00005FOops, like this...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ACBE")

    ChrTalk(
        0x105,
        (
            "#10402FHu hu, it seems it's also good to drop your\x01",
            "shoulders and make about a 45 degree.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ACBE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AD84")

    ChrTalk(
        0x106,
        (
            "#10702FActually, there're so\x01",
            "many customs, but...\x02\x03",
            "#10704FI think that it's essentially alright if you\x01",
            "pray like you do in a Septian Church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FAll right, let's do it.\x02",
    )

    CloseMessageWindow()

    label("loc_AD84")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and friends joined both hands, closed\x01",
            "their eyes and offered a prayer to the Jizｷ.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(1000)
    Sound(491, 0, 100, 0)
    Sleep(300)
    Sound(491, 0, 80, 0)
    Sleep(500)

    NpcTalk(
        0x2A,
        "Voice",
        (
            "My my, I'm sorry.\x01",
            "I'm hard of hearing.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sleep(500)
    OP_68(-3070, 1450, 2110, 0)
    MoveCamera(44, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14180, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_93(0x2A, 0x5A, 0x1F4)
    Sleep(100)

    def lambda_AEFB():
        OP_95(0xFE, 12120, -300, 1430, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_AEFB)
    Sleep(1000)
    OP_68(12510, 1450, 1570, 8000)
    MoveCamera(57, 25, 0, 8000)
    Sleep(4000)
    WaitChrThread(0x2A, 1)
    Sleep(500)

    ChrTalk(
        0x2A,
        "Oh, you all...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xF4)
    OP_64(0xF5)
    Sleep(500)

    def lambda_AF6A():

        label("loc_AF6A")

        TurnDirection(0xFE, 0x2A, 400)
        Yield()
        Jump("loc_AF6A")

    QueueWorkItem2(0x101, 2, lambda_AF6A)
    Sleep(50)

    def lambda_AF7F():

        label("loc_AF7F")

        TurnDirection(0xFE, 0x2A, 400)
        Yield()
        Jump("loc_AF7F")

    QueueWorkItem2(0x102, 2, lambda_AF7F)
    Sleep(50)

    def lambda_AF94():

        label("loc_AF94")

        TurnDirection(0xFE, 0x2A, 400)
        Yield()
        Jump("loc_AF94")

    QueueWorkItem2(0x103, 2, lambda_AF94)
    Sleep(50)

    def lambda_AFA9():

        label("loc_AFA9")

        TurnDirection(0xFE, 0x2A, 400)
        Yield()
        Jump("loc_AFA9")

    QueueWorkItem2(0x104, 2, lambda_AFA9)
    Sleep(50)

    def lambda_AFBE():

        label("loc_AFBE")

        TurnDirection(0xFE, 0x2A, 400)
        Yield()
        Jump("loc_AFBE")

    QueueWorkItem2(0xF4, 2, lambda_AFBE)
    Sleep(50)

    def lambda_AFD3():

        label("loc_AFD3")

        TurnDirection(0xFE, 0x2A, 400)
        Yield()
        Jump("loc_AFD3")

    QueueWorkItem2(0xF5, 2, lambda_AFD3)
    Sleep(50)
    Sleep(800)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0xF4, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00105F...Eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "Could it be that...you are the ones\x01",
            "who have been offering dishes to\x01",
            "the venerable Jizｷ...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FAh...that means that...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FAre you perhaps who wrote those letters...\x02",
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x2A,
        "Oh my, so it's like that!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "However, to think that such many\x01",
            "adorable children would... I thought\x01",
            "for sure it was some elderly like me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FAhaha, actually, with the occasion of practicing\x01",
            "cooking, we all offered something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FMaaan, we're surprised too.\x01",
            "I think...you're an old madam that we see\x01",
            "every now and then in Downtown, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FBecause the letters are very refined\x01",
            "and skillfully written, I thought that\x01",
            "it could've been an elderly person...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "Uhuhu, my apologies for always\x01",
            "taking your time with my letters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "However, it was like this then...\x01",
            "Really, many things\x01",
            "happen in this world.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_B3E8():
        OP_95(0xFE, 14600, -300, 3080, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_B3E8)
    Sleep(800)
    EndChrThread(0x101, 0x2)
    OP_93(0x101, 0x0, 0x12C)

    def lambda_B410():
        OP_96(0xFE, 0x3F34, 0xFFFFFED4, 0x898, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B410)
    Sleep(50)
    EndChrThread(0x103, 0x2)
    OP_93(0x103, 0x0, 0x0)

    def lambda_B438():
        OP_96(0xFE, 0x3B92, 0xFFFFFED4, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B438)
    FadeToDark(2000, 0, -1)
    Sleep(50)
    EndChrThread(0xF4, 0x2)

    def lambda_B463():
        OP_96(0xFE, 0x3D68, 0xFFFFFED4, 0xFFFFFF9C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_B463)
    WaitChrThread(0x2A, 1)

    def lambda_B481():
        OP_95(0xFE, 17260, -300, 3820, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_B481)
    OP_0D()
    Sleep(1000)
    OP_68(14150, 1450, 840, 0)
    MoveCamera(62, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12970, 0)
    SetChrPos(0x2A, 17260, -300, 3820, 0)
    SetChrPos(0x101, 16000, -300, 1250, 0)
    SetChrPos(0x102, 18000, -300, 1340, 0)
    SetChrPos(0x103, 14800, -300, 50, 0)
    SetChrPos(0x104, 18800, -300, 370, 0)
    SetChrPos(0xF4, 16400, -300, -650, 0)
    SetChrPos(0xF5, 18200, -300, -730, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Paola faced towards the Jizｷ and silently joined her hands.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(12770, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_63(0x2A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(2000)

    ChrTalk(
        0x2A,
        (
            "This venerable Jizｷ had experienced\x01",
            "all of the Crossbell turbulent times\x01",
            "and it was even destroyed once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "Nevertheless, it was restored many times\x01",
            "by the hands of the people of this city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "...Recently, the people who visit it\x01",
            "have remarkably decreased, but...\x01",
            "Uh uh, it looks like I hadn't to worry.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x2A, 0xB4, 0x190)

    ChrTalk(
        0x2A,
        (
            "Oh, right, I just have something\x01",
            "nice here with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "I am sorry that it is a received present, but...\x01",
            "I wonder if you could accept it, if you like?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FUhhm, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "Uh uh, it's all right.\x01",
            "It is simply a thank you gift.\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x2A, 16010, -300, 2000, 1500, 0x0)
    TurnDirection(0x2A, 0x101, 500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xEC, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B85B")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xEC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0xEC, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x2, 7)
    Jump("loc_B8A4")

    label("loc_B85B")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x86),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x86, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_B8A4")


    def lambda_B8A9():
        OP_96(0xFE, 0x3E80, 0xFFFFFED4, 0xA00, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_B8A9)

    def lambda_B8C3():

        label("loc_B8C3")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_B8C3")

    QueueWorkItem2(0x101, 2, lambda_B8C3)

    def lambda_B8D5():

        label("loc_B8D5")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_B8D5")

    QueueWorkItem2(0x102, 2, lambda_B8D5)

    def lambda_B8E7():

        label("loc_B8E7")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_B8E7")

    QueueWorkItem2(0x103, 2, lambda_B8E7)

    def lambda_B8F9():

        label("loc_B8F9")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_B8F9")

    QueueWorkItem2(0x104, 2, lambda_B8F9)

    def lambda_B90B():

        label("loc_B90B")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_B90B")

    QueueWorkItem2(0xF4, 2, lambda_B90B)

    def lambda_B91D():

        label("loc_B91D")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_B91D")

    QueueWorkItem2(0xF5, 2, lambda_B91D)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x2A,
        (
            "I have received it from my \x01",
            "junior, but I can't wear it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "...Uhuhu, that Imelda.\x01",
            "No matter how much time passes,\x01",
            "she is always awkward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "Goodbye then.\x01",
            "When you feel likely again,\x01",
            "please visit the venerable Jizｷ.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x2A, 0x10E, 0x1F4)

    def lambda_BABB():
        OP_95(0xFE, -1050, -300, 2150, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_BABB)
    Sleep(5000)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0xF4, 0x2)
    EndChrThread(0xF5, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BB55")

    ChrTalk(
        0x109,
        (
            "#10102FHmm, I wonder who\x01",
            "that old lady was?\x01",
            "She was extremely dashing though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BBA8")

    label("loc_BB55")


    ChrTalk(
        0x104,
        (
            "#00302F*haah*...\x01",
            "I haven't the slightest at all,\x01",
            "but she was a gallant woman.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BBA8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BCA2")

    ChrTalk(
        0x106,
        (
            "#10702FShe's an old lady who often basks in the\x01",
            "sun nearby the apartment where I live.\x02\x03",
            "#10704FShe now stays in Downtown, but it looks like\x01",
            "she was living in a different place before...\x01",
            "I thought she was a beautiful person.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BCE1")

    label("loc_BCA2")


    ChrTalk(
        0x103,
        (
            "#00202FQuite advanced in old age,\x01",
            "but she looked healthy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BCE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_END)), "loc_BD5C")

    ChrTalk(
        0x101,
        (
            "#00005FThis is a Master Quartz...\x01",
            "Also, she mentioned Mrs. Imelda's\x01",
            "name and said she was her junior...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BDD2")

    label("loc_BD5C")


    ChrTalk(
        0x101,
        (
            "#00005FThis is a rare high class Quartz...\x01",
            "Also, she mentioned Mrs. Imelda's\x01",
            "name and said she was her junior...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BDD2")


    ChrTalk(
        0x102,
        (
            "#00100FShe was really a kind and\x01",
            "mysterious person.\x02\x03",
            "#00103F(Now that I think about it...it seems there\x01",
            "was a splendid woman called the legendary\x01",
            "Belle of High Society in one of the older\x01",
            "generations of grandfather...)\x02\x03",
            "(...I-Impossible.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BF43")

    ChrTalk(
        0x10A,
        (
            "#00606F(...These kids don't know her?\x01",
            "She's a famous lady who took\x01",
            "Crossbell by storm back in the day.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BF43")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C020")

    ChrTalk(
        0x105,
        (
            "#10404FHu hu, every now and then you\x01",
            "want to give a prayer too.\x02\x03",
            "#10400FHowever, leader, is\x01",
            "this a good time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FOh, you're right.\x01",
            "I also got fired up...\x02\x03",
            "#00000FAlright, let's go then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C0CD")

    label("loc_C020")


    ChrTalk(
        0x101,
        (
            "#00004FI only wanted to pay a visit but it\x01",
            "turned into something unexpected...\x01",
            "But it seems this has fired me up too.\x02\x03",
            "#00000FAlright, let's go then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FYeah!\x02",
    )

    CloseMessageWindow()

    label("loc_C0CD")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 17130, -300, 2670, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 26200, -300, -1050, 270)
    BeginChrThread(0xD, 1, 0, 1)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -40490, -300, 15850, 90)
    BeginChrThread(0xE, 1, 0, 6)
    EndChrThread(0x2A, 0xFF)
    SetChrFlags(0x2A, 0x80)
    OP_D7(0x1E)
    SetScenarioFlags(0x20B, 7)
    EventEnd(0x5)
    Return()

    # Function_40_A8A2 end

    def Function_41_C146(): pass

    label("Function_41_C146")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C2F8")
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "What's this place...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, this is the home of the president\x01",
            "of Crossbell Merchants Association.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWe know him a little and\x01",
            "he's being kind to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "Hm, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "If he's the Merchants Association\x01",
            "President, even Cao and the others\x01",
            "would of course take their hats off to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Maybe greeting him could\x01",
            "be good, if possible.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C5, 3)
    OP_65(0x6, 0x1)
    SetMapObjFlags(0x3, 0x10)

    label("loc_C2F8")

    TalkEnd(0xFF)
    Return()

    # Function_41_C146 end

    def Function_42_C2FC(): pass

    label("Function_42_C2FC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch32200.itc", 0x1E)
    LoadChrToIndex("chr/ch23600.itc", 0x1F)
    LoadChrToIndex("chr/ch24200.itc", 0x20)
    SetChrChipByIndex(0x19, 0x1E)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, -2200, -300, 4400, 225)
    SetChrChipByIndex(0x1A, 0x1F)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, -3000, -300, 5200, 225)
    SetChrChipByIndex(0x1B, 0x20)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, -1400, -300, 3600, 225)
    OP_68(-4790, 1690, 1740, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14500, 0)
    SetChrPos(0x101, -3700, -300, 2600, 45)
    SetChrPos(0x102, -4650, -300, 1000, 45)
    SetChrPos(0x104, -5350, -300, 1750, 45)
    SetChrPos(0x109, -4650, -300, -100, 45)
    SetChrPos(0x105, -6350, -300, 1750, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00003F"Angler Duels"...?\x01",
            "Somehow things have become serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Eh eh, but it'll be an easy win.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Someone of us four\x01",
            "just needs to beat that\x01",
            "Lakelord completely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Y-Yes...\x01",
            "Honestly, I don't think\x01",
            "I'll be useful to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "What bothers me then\x01",
            "is the "Elite Four"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "There's also the limitless retry rule.\x01",
            "Persisting, of course we'll\x01",
            "win sooner or later, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "At least I think they won't be\x01",
            "easy matches like Coppen says.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "According to rumors, each of them\x01",
            "has a real strength greater than what\x01",
            "we here call "Master Fisherman".\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FI-Is that so...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "*s-sigh*... As I thought,\x01",
            "it'll be impossible for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Eh eh, I see...\x01",
            "Things have gotten interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Well, let's go back to the new branch\x01",
            "for now and hold a strategy meeting.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FThe new branch, you say...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Oh, I didn't tell you\x01",
            "about it yet, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Actually, the Branch Manager has found\x01",
            "a new building on the East Crossbell\x01",
            "Highway that has become our new office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Although it's a hire boat shed that's\x01",
            "never been used since it was\x01",
            "abandoned several years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "It's narrow, worn-out and crumbling,\x01",
            "but being near the river we can even\x01",
            "fish, so it's quite comfortable, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Yes, it's a place that feels\x01",
            "quite suitable for our sure\x01",
            "fresh start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "When you come to the Tangram Gate area\x01",
            "at the crossroad of the East Crossbell \x01",
            "Highway, you should see the sign...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Then, follow that and\x01",
            "it's a little further\x01",
            "down to the south.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Member Lloyd too, if you have\x01",
            "time, please come visit us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Well then, member Lloyd, for now \x01",
            "I plan for us to do something\x01",
            "about the Angler Duels, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Since our numbers are few,\x01",
            "it would be better being more.\x01",
            "I count on you too, member Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYes, I too don't want to\x01",
            "become unable to fish \x01",
            "in my favorite spots.\x02\x03",
            "#00000FI'll support you as much as I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Eh eh, member Lloyd.\x01",
            "I won't lose too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "Then, we say goodbye here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "Then, goddessspeed!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, to you all too!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 43)
    Sleep(200)
    BeginChrThread(0x19, 3, 0, 43)
    Sleep(200)
    BeginChrThread(0x1A, 3, 0, 43)
    Sleep(1000)

    def lambda_CCA4():

        label("loc_CCA4")

        TurnDirection(0x101, 0x1A, 500)
        Yield()
        Jump("loc_CCA4")

    QueueWorkItem2(0x101, 2, lambda_CCA4)

    def lambda_CCB6():

        label("loc_CCB6")

        TurnDirection(0x102, 0x1A, 500)
        Yield()
        Jump("loc_CCB6")

    QueueWorkItem2(0x102, 2, lambda_CCB6)

    def lambda_CCC8():

        label("loc_CCC8")

        TurnDirection(0x109, 0x1A, 500)
        Yield()
        Jump("loc_CCC8")

    QueueWorkItem2(0x109, 2, lambda_CCC8)

    def lambda_CCDA():

        label("loc_CCDA")

        TurnDirection(0x105, 0x1A, 500)
        Yield()
        Jump("loc_CCDA")

    QueueWorkItem2(0x105, 2, lambda_CCDA)

    def lambda_CCEC():

        label("loc_CCEC")

        TurnDirection(0x104, 0x1A, 500)
        Yield()
        Jump("loc_CCEC")

    QueueWorkItem2(0x104, 2, lambda_CCEC)
    WaitChrThread(0x1B, 3)

    ChrTalk(
        0x102,
        (
            "#00109F(Uhhm, that Lloyd, he's\x01",
            "so in high spirits, eh?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F(Fishing, eh...?\x01",
            "I don't really get it, but there're a\x01",
            "lot of passionate people about it.)\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x104, 0x2)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    SetScenarioFlags(0x1C0, 2)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0xD, 26200, -300, -1050, 270)
    BeginChrThread(0xD, 0, 0, 1)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrPos(0xE, -40490, -300, 15850, 90)
    BeginChrThread(0xE, 0, 0, 6)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -3700, -300, 2600, 45)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_42_C2FC end

    def Function_43_CE46(): pass

    label("Function_43_CE46")

    OP_93(0xFE, 0x87, 0x1F4)
    OP_95(0xFE, 110, -300, 1300, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x0)
    OP_95(0xFE, 14590, -300, 1300, 2000, 0x0)
    Return()

    # Function_43_CE46 end

    def Function_44_CE7D(): pass

    label("Function_44_CE7D")

    EventBegin(0x1)
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "There's no need to show me here.\x01",
            "Let's go to another place.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 1910, -3000, -35980, 0)
    EventEnd(0x4)
    Return()

    # Function_44_CE7D end

    def Function_45_CEDE(): pass

    label("Function_45_CEDE")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF6B")

    ChrTalk(
        0x1A2,
        (
            "Hey, doesn't this way lead\x01",
            "outside the city?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000FYeah, indeed it does.\x01",
            "Let's go back to the city.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_CFB0")

    label("loc_CF6B")


    ChrTalk(
        0x101,
        (
            "#00000FWe can't exit on the highway.\x01",
            "Let's go back to the city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CFB0")

    SetChrPos(0x0, 29390, -300, 500, 270)
    EventEnd(0x4)
    Return()

    # Function_45_CEDE end

    def Function_46_CFC4(): pass

    label("Function_46_CFC4")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D0A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D054")

    ChrTalk(
        0x101,
        (
            "#00000FThis way is the East Crossbell Highway.\x02\x03",
            "We don't have any particular business\x01",
            "so let's not go there.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    Jump("loc_D0A1")

    label("loc_D054")


    ChrTalk(
        0x101,
        (
            "#00000FWe don't have any particular business\x01",
            "this way, so let's not go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D0A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D1BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D148")

    ChrTalk(
        0x101,
        (
            "#00001FThis way is the East Crossbell Highway.\x02\x03",
            "Let's focus on the investigation related to\x01",
            "the accident without any detours now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    Jump("loc_D1BE")

    label("loc_D148")


    ChrTalk(
        0x101,
        (
            "#00001FWe don't have any particular business\x01",
            "this way. Let's focus on the\x01",
            "investigation related to accident now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D1BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D220")

    ChrTalk(
        0x101,
        (
            "#00001FNow we have to chase Randy down...\x01",
            "It's not the time to wander around.\x01\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D220")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D285")

    ChrTalk(
        0x101,
        (
            "#00001FNow it's not the time to go out the city.\x01",
            "Let's quietly retrace our steps.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D285")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D321")

    ChrTalk(
        0x101,
        (
            "#00001FAfter coming here,\x01",
            "we can't leave the city.\x02\x03",
            "The operation to break into Orchis Tower...\x01",
            "We have to make it succeed at all costs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D321")

    SetChrPos(0x0, 29390, -300, 500, 270)
    EventEnd(0x4)
    Return()

    # Function_46_CFC4 end

    def Function_47_D335(): pass

    label("Function_47_D335")

    EventBegin(0x1)

    ChrTalk(
        0x105,
        (
            "#10303F...Lloyd, I'm sorry but if we're\x01",
            "going back to Downtown, could\x01",
            "you give me just a little time?\x02\x03",
            "#10308FEven a tiny little bit is fine.\x01",
            "Going back immediately would\x01",
            "be, like you can imagine, a little...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FYeah...all right.\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 1610, -3000, -35150, 0)
    EventEnd(0x4)
    Return()

    # Function_47_D335 end

    SaveToFile()

Try(main)
