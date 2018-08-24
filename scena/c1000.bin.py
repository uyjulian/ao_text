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

    Sepith("Sepith_D0FF", 8,   8,   8,   8,   11,  11,  11)

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
        "BattleInfo_A20", 0x0000, 93, 6, 60, 4, 1, 25, 0, "bc1000", "Sepith_D0FF", 60, 30, 10, 0,
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
        "Function_11_1D84",        # 0B, 11
        "Function_12_1ED5",        # 0C, 12
        "Function_13_20FE",        # 0D, 13
        "Function_14_235A",        # 0E, 14
        "Function_15_2C0C",        # 0F, 15
        "Function_16_2D06",        # 10, 16
        "Function_17_2F4E",        # 11, 17
        "Function_18_2F4F",        # 12, 18
        "Function_19_33AC",        # 13, 19
        "Function_20_359F",        # 14, 20
        "Function_21_3906",        # 15, 21
        "Function_22_39AA",        # 16, 22
        "Function_23_3EF1",        # 17, 23
        "Function_24_4284",        # 18, 24
        "Function_25_47C8",        # 19, 25
        "Function_26_4B22",        # 1A, 26
        "Function_27_4FB9",        # 1B, 27
        "Function_28_546C",        # 1C, 28
        "Function_29_5D33",        # 1D, 29
        "Function_30_7124",        # 1E, 30
        "Function_31_7140",        # 1F, 31
        "Function_32_715C",        # 20, 32
        "Function_33_7178",        # 21, 33
        "Function_34_7194",        # 22, 34
        "Function_35_71B0",        # 23, 35
        "Function_36_78D1",        # 24, 36
        "Function_37_7A75",        # 25, 37
        "Function_38_A152",        # 26, 38
        "Function_39_A3B5",        # 27, 39
        "Function_40_A588",        # 28, 40
        "Function_41_BE21",        # 29, 41
        "Function_42_BFA1",        # 2A, 42
        "Function_43_CADD",        # 2B, 43
        "Function_44_CB14",        # 2C, 44
        "Function_45_CB79",        # 2D, 45
        "Function_46_CC5A",        # 2E, 46
        "Function_47_CFD2",        # 2F, 47
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
            "Since you have too many,\x01",
            "you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x6, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1D2A")

    Jump("loc_1D78")

    label("loc_1D2F")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the\x01",
            "chest.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1D78")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_1C33 end

    def Function_11_1D84(): pass

    label("Function_11_1D84")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E80")
    Sound(14, 0, 100, 0)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x98, 1)"), scpexpr(EXPR_END)), "loc_1E09")
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
    Jump("loc_1E7B")

    label("loc_1E09")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x98),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many,\x01",
            "you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1E7B")

    Jump("loc_1EC9")

    label("loc_1E80")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the\x01",
            "chest.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1EC9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_1D84 end

    def Function_12_1ED5(): pass

    label("Function_12_1ED5")

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
        (
            "#11P#00105FIs something bothering\x01",
            "you?\x02",
        )
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
            "#11P#00200FI felt a small presence\x01",
            "coming from this\x01",
            "direction, but...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#6P#00203F... Sorry, it's probably\x01",
            "nothing to be concerned\x01",
            "about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FIs that so...\x02",
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

    # Function_12_1ED5 end

    def Function_13_20FE(): pass

    label("Function_13_20FE")

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
        (
            "#00105FIs something bothering\x01",
            "you?\x02",
        )
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
            "#11P#00200FI felt a small presence\x01",
            "coming from this\x01",
            "direction, but...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#6P#00203F... Sorry, it's probably\x01",
            "nothing to be concerned\x01",
            "about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FIs that so...\x02",
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

    # Function_13_20FE end

    def Function_14_235A(): pass

    label("Function_14_235A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2367")
    Call(0, 15)
    Return()

    label("loc_2367")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28B2")
    SetScenarioFlags(0x2, 2)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Darkness can be seen\x01",
            "between the wooden planks\x01",
            "leaning against the wall.\x07\x00\x02",
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
            "#12P#00005FThis... looks like it\x01",
            "connects to somewhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105FA place in the Geofront,\x01",
            "maybe?\x02\x03",
            "#00103FIt looks like the planks\x01",
            "can be moved...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00305FCould this be what Tio\x01",
            "noticed back there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FYes. It was coming from\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_25F1")

    ChrTalk(
        0x10A,
        (
            "#12P#00603FHmm, it's a bit\x01",
            "concerning.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_267F")

    label("loc_25F1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2632")

    ChrTalk(
        0x109,
        (
            "#12P#10105F...Could there be\x01",
            "someone?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_267F")

    label("loc_2632")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_267F")

    ChrTalk(
        0x105,
        (
            "#12P#10405F...Could someone have\x01",
            "gotten lost in there?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_267F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_26BD")

    ChrTalk(
        0x106,
        "#12P#10701FShould we check it out?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_2739")

    label("loc_26BD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2701")

    ChrTalk(
        0x105,
        (
            "#12P#10400FShould we take a look\x01",
            "inside?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_2739")

    label("loc_2701")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2739")

    ChrTalk(
        0x109,
        "#12P#10101FShould we look inside?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2739")

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
            "[Cancel]\x01",                   # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_283E")

    ChrTalk(
        0x101,
        (
            "#12P#00001FYou're right... We\x01",
            "should check it just in\x01",
            "case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FThen, let's enter\x01",
            "immediately.\x02",
        )
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
    Jump("loc_28AD")

    label("loc_283E")


    ChrTalk(
        0x101,
        (
            "#12P#00003F...No, we can't do any\x01",
            "unnecessary stops right\x01",
            "now.\x02\x03",
            "#00000FLet's leave this place\x01",
            "be for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28AD")

    Jump("loc_2A9C")

    label("loc_28B2")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You can see something\x01",
            "within the wooden planks\x01",
            "leaned against the wall.\x07\x00\x02",
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
            "[Cancel]\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A2D")

    ChrTalk(
        0x101,
        (
            "#12P#00003FAs I thought... Let's\x01",
            "check just in case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101FRight, somehow it\x01",
            "bothers me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FThen, let's enter\x01",
            "immediately.\x02",
        )
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
    Jump("loc_2A9C")

    label("loc_2A2D")


    ChrTalk(
        0x101,
        (
            "#12P#00003F...No, we can't do any\x01",
            "unnecessary stops right\x01",
            "now.\x02\x03",
            "#00000FLet's leave this place\x01",
            "be for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A9C")

    Jump("loc_2BD5")

    label("loc_2AA1")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You can see something\x01",
            "within the wooden planks\x01",
            "leaned against the wall.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#12P#00003F(Reins, huh...? Who\x01",
            "would've thought he was\x01",
            "with a research agency...)\x02",
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
            "[Go to Reins' Hiding Place]\x01",      # 0
            "[Cancel]\x01",                         # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BD5")
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("m0304", 100, 0, 0)
    IdleLoop()
    Jump("loc_2BD5")

    label("loc_2BD5")

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

    # Function_14_235A end

    def Function_15_2C0C(): pass

    label("Function_15_2C0C")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CB6")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The planks leaning\x01",
            "against the wall have\x01",
            "been fixed securely.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00005FIt looks like Mr. Reins\x01",
            "has tightly closed it up\x01",
            "since then.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_2D02")

    label("loc_2CB6")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The planks leaning\x01",
            "against the wall have\x01",
            "been fixed securely.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2D02")

    TalkEnd(0xFF)
    Return()

    # Function_15_2C0C end

    def Function_16_2D06(): pass

    label("Function_16_2D06")

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
            "#00203FEven so, R&A Research,\x01",
            "huh...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301FPretty legit, don'tcha\x01",
            "think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00100FYes. After all, the\x01",
            "organization is led by\x01",
            "former Colonel Richard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWell for now, we shouldn't\x01",
            "pry into their actions any\x01",
            "more than necessary.\x02\x03",
            "#00001FAnyway, let's proceed with\x01",
            "preparations to infiltrate\x01",
            "the tower.\x02",
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

    # Function_16_2D06 end

    def Function_17_2F4E(): pass

    label("Function_17_2F4E")

    Return()

    # Function_17_2F4E end

    def Function_18_2F4F(): pass

    label("Function_18_2F4F")

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

    def lambda_2FD2():
        OP_96(0xFE, 0x640, 0xFFFFF448, 0xFFFF88DC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2FD2)
    Sleep(50)

    def lambda_2FEF():
        OP_96(0xFE, 0x640, 0xFFFFF448, 0xFFFF7B30, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2FEF)
    Sleep(50)

    def lambda_300C():
        OP_96(0xFE, 0x9C4, 0xFFFFF448, 0xFFFF77AC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_300C)
    Sleep(50)

    def lambda_3029():
        OP_96(0xFE, 0x2BC, 0xFFFFF448, 0xFFFF7554, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3029)
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
        "#12P#10106F#30WWazy, umm...\x02",
    )

    CloseMessageWindow()
    OP_64(0x105)
    Sleep(500)
    OP_93(0x105, 0xB4, 0x190)
    Sleep(150)

    ChrTalk(
        0x105,
        (
            "#5P#10304F#30W...Haha. I showed you\x01",
            "something I shouldn't\x01",
            "have.\x02\x03",
            "#10302FIt's not like me to get\x01",
            "so worked up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FNo...\x02\x03",
            "#00000F...How can I say it, men\x01",
            "are like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FAlthough I don't\x01",
            "understand boys'\x01",
            "feelings very well...\x02\x03",
            "#00100FI know that you faced\x01",
            "him in good faith.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10112FRight, right!\x02\x03",
            "#10100FI think one day he'll\x01",
            "get it too!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32E4")

    ChrTalk(
        0x105,
        (
            "#5P#10304F#30WHaha... I hope you're\x01",
            "right.\x02\x03",
            "#10300F─I've wasted enough of\x01",
            "our time. Let's go\x01",
            "somewhere else.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3369")

    label("loc_32E4")


    ChrTalk(
        0x105,
        (
            "#5P#10304F#30WHaha... I hope you're\x01",
            "right.\x02\x03",
            "#10300F─Sorry for wasting time.\x01",
            "Let's take care of the\x01",
            "remaining support requests.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3369")

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

    # Function_18_2F4F end

    def Function_19_33AC(): pass

    label("Function_19_33AC")

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

    def lambda_34E4():
        OP_98(0xFE, 0x2AF8, 0x0, 0xFFFFD508, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_34E4)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -14300, -300, 11700, 135)

    def lambda_3514():
        OP_98(0xFE, 0x2AF8, 0x0, 0xFFFFD508, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_3514)
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

    # Function_19_33AC end

    def Function_20_359F(): pass

    label("Function_20_359F")

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

    # Function_20_359F end

    def Function_21_3906(): pass

    label("Function_21_3906")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_393E"),
        (1, "loc_3946"),
        (2, "loc_394E"),
        (3, "loc_3956"),
        (4, "loc_395E"),
        (5, "loc_3966"),
        (6, "loc_396E"),
        (SWITCH_DEFAULT, "loc_3976"),
    )


    label("loc_393E")

    Sleep(100)
    Jump("loc_397E")

    label("loc_3946")

    Sleep(200)
    Jump("loc_397E")

    label("loc_394E")

    Sleep(300)
    Jump("loc_397E")

    label("loc_3956")

    Sleep(400)
    Jump("loc_397E")

    label("loc_395E")

    Sleep(500)
    Jump("loc_397E")

    label("loc_3966")

    Sleep(600)
    Jump("loc_397E")

    label("loc_396E")

    Sleep(700)
    Jump("loc_397E")

    label("loc_3976")

    Sleep(800)
    Jump("loc_397E")

    label("loc_397E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_39A9")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xFE)
    Sleep(500)
    Jump("loc_397E")

    label("loc_39A9")

    Return()

    # Function_21_3906 end

    def Function_22_39AA(): pass

    label("Function_22_39AA")

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
        "#6P#00012FPhew... I'm beat.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00102FYes... Thank goodness we\x01",
            "were able to find Mary,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FSorry guys. That stupid\x01",
            "cousin of mine was such\x01",
            "a pain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10112FAhaha... That's not your\x01",
            "fault. Don't worry about\x01",
            "it.\x02\x03",
            "#10100FAnd, she's a very good\x01",
            "girl, isn't she.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FThat's right. No matter\x01",
            "what you say, she did offer\x01",
            "us her sincere assistance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FHaha... Well, I guess\x01",
            "she's not evil.\x02\x03",
            "#00306FBut that just makes her\x01",
            "all the more\x01",
            "troublesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00008FI see... It seems like\x01",
            "there are a lot of\x01",
            "things between you two.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#11P#10304FHehe. The ability to sweep\x01",
            "girls off their feet is an\x01",
            "ability guys have too.\x02\x03",
            "#10300FSo, what do we do now?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x72, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x77, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DCB")

    ChrTalk(
        0x101,
        (
            "#6P#00004FHmm... We are done with\x01",
            "our support requests.\x02\x03",
            "#00000FMaybe we should return\x01",
            "to the Support Section\x01",
            "for a break.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E50")

    label("loc_3DCB")


    ChrTalk(
        0x101,
        (
            "#6P#00003FLet's see... We still\x01",
            "have support requests to\x01",
            "do.\x02\x03",
            "#00000FMaybe we should return\x01",
            "to the Support Section\x01",
            "for a break.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E50")


    ChrTalk(
        0x102,
        (
            "#12P#00104FYes... Let's do just\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FIt's back to the Support\x01",
            "Section for a break,\x01",
            "then.\x02",
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

    # Function_22_39AA end

    def Function_23_3EF1(): pass

    label("Function_23_3EF1")

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
            "─Of course, as you noticed, there is\x01",
            "not only one wicked will.\x02\x03",
            "The "Calvard Republican Government"...\x02\x03",
            "Joining hands with a cunning crime\x01",
            "syndicate, they too are trying to tread\x01",
            "on Crossbell's peace and dignity.\x02",
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

    # Function_23_3EF1 end

    def Function_24_4284(): pass

    label("Function_24_4284")

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

    def lambda_43EE():
        OP_95(0x101, 1000, -3000, -14740, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_43EE)

    def lambda_4408():
        OP_95(0x102, 2600, -3000, -13540, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4408)

    def lambda_4422():
        OP_95(0x109, 2000, -3000, -15940, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4422)

    def lambda_443C():
        OP_95(0x105, 3600, -2930, -14740, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_443C)

    def lambda_4456():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4456)
    Sleep(300)

    def lambda_446A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_446A)
    Sleep(300)

    def lambda_447E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_447E)
    Sleep(300)

    def lambda_4492():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4492)
    Sleep(1500)
    SetMapObjFlags(0x4, 0x0)
    WaitChrThread(0x101, 1)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    WaitChrThread(0x102, 1)

    def lambda_44E0():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_44E0)
    Sleep(300)

    def lambda_44F0():
        OP_93(0x102, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_44F0)
    Sleep(300)

    def lambda_4500():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4500)
    Sleep(300)

    def lambda_4510():
        OP_93(0x105, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4510)
    Sleep(300)

    def lambda_4520():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4520)
    Sleep(300)

    def lambda_4530():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4530)
    Sleep(300)

    def lambda_4540():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4540)
    Sleep(300)

    def lambda_4550():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4550)
    Sleep(300)
    OP_0D()

    def lambda_4561():
        OP_93(0x101, 0x5A, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4561)

    def lambda_456E():
        OP_93(0x102, 0xB4, 0x5DC)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_456E)

    def lambda_457B():
        OP_93(0x109, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_457B)

    def lambda_4588():
        OP_93(0x105, 0x10E, 0x5DC)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4588)
    OP_0D()
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        (
            "#6P#00001FIt's no good... We lost\x01",
            "him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FH-He's something else!\x02\x03",
            "#10101FIt's like he knew we\x01",
            "were coming and trapped\x01",
            "us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FWell for him, that's a\x01",
            "piece of cake.\x02\x03",
            "#00101FHe's not an intelligence\x01",
            "captain for nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHaha, that's a method no\x01",
            "soldier could think of,\x01",
            "though.\x02\x03",
            "#10302FSo, do we give up here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FNo... Anyhow, let's try\x01",
            "to follow him.\x02\x03",
            "#00000FIf we ask around, we\x01",
            "might be able to track\x01",
            "him down.\x02",
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

    # Function_24_4284 end

    def Function_25_47C8(): pass

    label("Function_25_47C8")

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

    def lambda_492B():
        OP_9B(0x1, 0xFE, 0x0, 0x61A8, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_492B)

    def lambda_4940():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_4940)
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
        "Haha, an ambush!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x17,
        "Yuri",
        (
            "Hmph, what shallow\x01",
            "thinking.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x17,
        "Yuri",
        (
            "Reggie, can you shake\x01",
            "them off?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x17,
        "Reggie",
        (
            "Of course, they're\x01",
            "nothing special!\x02",
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

    def lambda_4A94():
        OP_9B(0x1, 0x17, 0x0, 0x2710, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4A94)
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

    # Function_25_47C8 end

    def Function_26_4B22(): pass

    label("Function_26_4B22")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 5)), scpexpr(EXPR_END)), "loc_4D4A")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "  ～Now Closed～\x01",
            "Imperial Fishing Club\x07\x00\x02",
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
            "#12P#00003FHmm, it's the same as\x01",
            "before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FHey Lloyd. Do have have\x01",
            "any clue about this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FNo. To be honest, I\x01",
            "haven't a clue about\x01",
            "what's happened.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00005FOh... But it's not\x01",
            "locked?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E36")

    label("loc_4D4A")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "  ～Now Closed～\x01",
            "Imperial Fishing Club\x07\x00\x02",
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
            "#12P#00003FClosed, huh? But what in\x01",
            "the world is the\x01",
            "Imperial Fishing Club?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00005FOh... But it's not\x01",
            "locked?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E36")


    NpcTalk(
        0x1A,
        "Youth's Voice",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5PY-You... You call\x01",
            "yourself a fisherman!?\x07\x00\x02",
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
            "your heavy-handed\x01",
            "methods.\x07\x00\x02",
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
        "#6P#00105FLloyd, what was that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FI know those voices.\x01",
            "Let's go inside.\x02",
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

    # Function_26_4B22 end

    def Function_27_4FB9(): pass

    label("Function_27_4FB9")

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
            "#5PHow could it have come\x01",
            "to this...? I can't\x01",
            "accept it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#11PYeah, to think our\x01",
            "branch office was stolen\x01",
            "from us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#11PFor now, we'll need to\x01",
            "again consult with\x01",
            "Branch Manager Celdan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FUmm, Peter? I'm not\x01",
            "quite getting what's\x01",
            "going on yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#11PAh, that must be because\x01",
            "you've been on break from the\x01",
            "guild for a while, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#11PAnyway, I'll gather\x01",
            "everyone, and then we'll\x01",
            "talk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#11PI'll call the branch\x01",
            "manager. Please come to Jazz\x01",
            "Bar Galante on Back Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#11PYou come too, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PAlright, then we'll go\x01",
            "on ahead.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_52E4():
        OP_9B(0x0, 0x1A, 0x5A, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_52E4)
    Sleep(50)

    def lambda_52FC():
        OP_93(0x101, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_52FC)
    Sleep(50)

    def lambda_530C():
        OP_93(0x102, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_530C)
    Sleep(50)
    WaitChrThread(0x1B, 1)

    def lambda_5320():
        OP_9B(0x0, 0x1B, 0x5A, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_5320)
    Sleep(50)

    def lambda_5338():
        OP_93(0x109, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5338)
    Sleep(50)

    def lambda_5348():
        OP_93(0x105, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5348)
    Sleep(50)
    WaitChrThread(0x1B, 1)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)

    ChrTalk(
        0x102,
        (
            "#5P#00105FI really wonder what\x01",
            "exactly happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00003FI don't really get it,\x01",
            "but anyway, we've got to\x01",
            "confirm the details.\x02\x03",
            "#00000FLet's also head to the\x01",
            "jazz bar.\x02",
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

    # Function_27_4FB9 end

    def Function_28_546C(): pass

    label("Function_28_546C")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_5509")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x1A2, 0x80)
    Jump("loc_5548")

    label("loc_5509")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_552B")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x1A2, 0x80)
    Jump("loc_5548")

    label("loc_552B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_5548")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x1A2, 0x80)

    label("loc_5548")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_56BC")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x104, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, -19400, -310, 26000, 180)
    SetChrPos(0x102, -20100, -310, 26000, 180)
    SetChrPos(0x101, -19150, -310, 27200, 180)
    SetChrPos(0x104, -20350, -310, 27200, 180)

    def lambda_564E():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_564E)

    def lambda_5668():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5668)
    Sleep(100)

    def lambda_5685():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5685)
    Sleep(50)

    def lambda_56A2():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_56A2)
    Jump("loc_585F")

    label("loc_56BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_5790")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x109, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, -19400, -310, 26000, 180)
    SetChrPos(0x102, -20100, -310, 26000, 180)
    SetChrPos(0x101, -19150, -310, 27200, 180)
    SetChrPos(0x109, -20350, -310, 27200, 180)

    def lambda_5722():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_5722)

    def lambda_573C():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_573C)
    Sleep(100)

    def lambda_5759():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5759)
    Sleep(50)

    def lambda_5776():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5776)
    Jump("loc_585F")

    label("loc_5790")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_585F")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x105, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, -19400, -310, 26000, 180)
    SetChrPos(0x102, -20100, -310, 26000, 180)
    SetChrPos(0x101, -19150, -310, 27200, 180)
    SetChrPos(0x105, -20350, -310, 27200, 180)

    def lambda_57F6():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_57F6)

    def lambda_5810():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5810)
    Sleep(100)

    def lambda_582D():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_582D)
    Sleep(50)

    def lambda_584A():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_584A)

    label("loc_585F")

    SetCameraDistance(14560, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x1A2,
        "This is East Street...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "It's my first time\x01",
            "looking at it like this.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#6P#00100FHaha. You can relax\x01",
            "because it reminds you\x01",
            "of home, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "#11PI suppose.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#11PHaha. Though the energy of\x01",
            "the real Eastern Quarter is\x01",
            "nothing like this, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#11PIf there's a chance, I'd love\x01",
            "to show you around the Eastern\x01",
            "Quarter personally, miss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#11PI mean, I want to take\x01",
            "you back with me!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_5B01")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#6P#00112FU-Uhmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FThat's quite the\x01",
            "delivery he's got there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FYou're tellin' me. He\x01",
            "threw tact right out the\x01",
            "window.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CBD")

    label("loc_5B01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_5BDF")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00112FU-Uhmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FThat's quite the\x01",
            "delivery he's got there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FAhaha. I think I might\x01",
            "be jealous, in a way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CBD")

    label("loc_5BDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_5CBD")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00112FU-Uhmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FThat's quite the\x01",
            "delivery he's got there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHaha. Honesty is one of\x01",
            "his strong points, I\x01",
            "see.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CBD")

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

    # Function_28_546C end

    def Function_29_5D33(): pass

    label("Function_29_5D33")

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
        "Oh, need something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FYes. We'd like to ask\x01",
            "you a little something.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained the situation\x01",
            "and asked if Sunita's kitten\x01",
            "Mary had stopped by.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        (
            "Ah, she belongs to Mr. Bond's family,\x01",
            "right? If the police are looking for\x01",
            "her, I'm sure she'll be fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "But, I haven't seen her\x01",
            "today, sorry to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Her favorite dried fish I\x01",
            "left for her is still\x01",
            "sitting there, you see...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I can at least be sure\x01",
            "she hasn't been here\x01",
            "since last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00103FIs that so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "They're regular customers,\x01",
            "so I'd like to help in any\x01",
            "way that I can, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Please, find her\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYes, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FThank you for your\x01",
            "cooperation.\x02",
        )
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
        (
            "#00303FA swing and a miss right\x01",
            "off the bat, eh?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#12P#10105FWhat are we going to do\x01",
            "now?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000FWell for now, we should interview\x01",
            "everyone in the area...\x02\x03",
            "#00003FIf that fails, our search area will\x01",
            "be quite large. Relying on Zeit's\x01",
            "nose might be our only choice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00105FI think that's fine,\x01",
            "but...\x02\x03",
            "#00106FI wonder if we'll be\x01",
            "able to understand him\x01",
            "without Tio.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FThat's true...\x02\x03",
            "#00000FBut, we could use some\x01",
            "gestures and...\x02",
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
        "#3949VHey! What're you doing?\x02",
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

    def lambda_63FD():

        label("loc_63FD")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_63FD")

    QueueWorkItem2(0x101, 1, lambda_63FD)

    def lambda_640F():

        label("loc_640F")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_640F")

    QueueWorkItem2(0x104, 1, lambda_640F)

    def lambda_6421():

        label("loc_6421")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_6421")

    QueueWorkItem2(0x102, 1, lambda_6421)

    def lambda_6433():

        label("loc_6433")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_6433")

    QueueWorkItem2(0x109, 1, lambda_6433)

    def lambda_6445():

        label("loc_6445")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_6445")

    QueueWorkItem2(0x105, 1, lambda_6445)
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
        "#12P#00011FWha!?\x02",
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
            "It's big brother Randy!\x01",
            "...And that guy and that\x01",
            "lady.\x02\x03",
            "Wha'cha doin' here?\x02",
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
            "#00303FNot that you care.\x01",
            "Scram.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x1C,
        (
            "#04606FMrr, how cold.\x02\x03",
            "#04600FThen, should I ask the\x01",
            "body of that lady over\x01",
            "there?\x02\x03",
            "#04609FI want to fondle them\x01",
            "with all my might again㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00112FW-Wait!\x02",
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
            "#12P#00003FAs you can see, we're\x01",
            "doing a Special Support\x01",
            "Section job.\x02\x03",
            "#00001FIt has nothing to do\x01",
            "with you, so please stay\x01",
            "out of our way.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1C, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1C,
        (
            "#04606FHmm, I wasn't really\x01",
            "planning on getting in\x01",
            "your way, though.\x02\x03",
            "#04600FSo, what kinda job?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006F*sigh*... We're not\x01",
            "getting anywhere at this\x01",
            "rate...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Explained about the lost kitten.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x1C,
        (
            "#04605FOhhh, I see.\x02\x03",
            "#04600FSo, how are you gonna\x01",
            "find Mary now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FWe're going to use our\x01",
            "police dog and follow\x01",
            "her scent...\x02",
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
        "#12P#00005FHuh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#04602FYou seem to know a lot about\x01",
            "dogs, but for cats, you have\x01",
            "a long way to go, mister.\x02\x03",
            "#04604FYou have to think about\x01",
            "Mary's feelings!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006FW-What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#04600FI don't know the\x01",
            "details, but didn't that\x01",
            "family move recently?\x02\x03",
            "#04604FIn that case, there's\x01",
            "only one answer.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00105FThat's right. Why didn't\x01",
            "we notice earlier?\x02\x03",
            "#00100FIt's Residential Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#04600FOhhh, so her former home\x01",
            "is there?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00005FI see. So Mary must've been\x01",
            "trying to return home in the\x01",
            "first place!\x02\x03",
            "#00001FBut, to the Residential Street\x01",
            "house where she lived before,\x01",
            "rather than her new home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10103FI see. That does make\x01",
            "sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10303FIf pushed, I'd say dogs are drawn to\x01",
            "people and cats are drawn to homes.\x02\x03",
            "#10300FI think you'll understand if you think\x01",
            "about the action pattern of a cat after\x01",
            "it's been separated from its owner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F...It's certainly true that\x01",
            "Koppe's never left the\x01",
            "Support Section building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#04609FAhaha, exactly.\x02\x03",
            "#04602FThen, I'll go on ahead,\x01",
            "'k?♪\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1C, 0x0, 0x1F4)
    Sleep(300)

    def lambda_6E1E():
        OP_95(0xFE, 2270, -220, -3590, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_6E1E)
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
            "#00005FD-Don't tell me... Is\x01",
            "she planning to get\x01",
            "involved?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHehe, looks like it.\x02\x03",
            "#10300FLike a whimsical\x01",
            "kitten... Or maybe I\x01",
            "should say a tiger cub.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FThat's no laughing\x01",
            "matter, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FH-Hmm... I wonder what's\x01",
            "gotten into her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F...Well, unless we're\x01",
            "caught in her gunfire, it\x01",
            "won't be that dangerous.\x02\x03",
            "#00300FShe might lose interest\x01",
            "soon. Let's go have a\x01",
            "look at the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FUnderstood... Let's\x01",
            "hurry to Residential\x01",
            "Street ourselves.\x02",
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

    # Function_29_5D33 end

    def Function_30_7124(): pass

    label("Function_30_7124")

    OP_95(0x101, 750, -3000, -12700, 2000, 0x0)
    OP_93(0x101, 0x5A, 0x1F4)
    Return()

    # Function_30_7124 end

    def Function_31_7140(): pass

    label("Function_31_7140")

    OP_95(0x102, 2530, -3000, -11630, 2000, 0x0)
    OP_93(0x102, 0xB4, 0x1F4)
    Return()

    # Function_31_7140 end

    def Function_32_715C(): pass

    label("Function_32_715C")

    OP_95(0x104, 3790, -3000, -12940, 2000, 0x0)
    OP_93(0x104, 0x10E, 0x1F4)
    Return()

    # Function_32_715C end

    def Function_33_7178(): pass

    label("Function_33_7178")

    OP_95(0x109, 1400, -3000, -14510, 2000, 0x0)
    OP_93(0x109, 0x2D, 0x1F4)
    Return()

    # Function_33_7178 end

    def Function_34_7194(): pass

    label("Function_34_7194")

    OP_95(0x105, 3200, -3000, -14560, 2000, 0x0)
    OP_93(0x105, 0x13B, 0x1F4)
    Return()

    # Function_34_7194 end

    def Function_35_71B0(): pass

    label("Function_35_71B0")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_75F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75B0")

    ChrTalk(
        0x1A2,
        "Fishing King Club...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FAh, that is read as\x01",
            ""Imperial Fishing Club".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Hmph. I don't really get it,\x01",
            "but it means it's a gathering\x01",
            "of fishing enthusiasts, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "So their type exists in\x01",
            "Crossbell too.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00105FYou mean, they're in the\x01",
            "Republic too?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "Yes, indeed they are.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Incidentally, grandfather\x01",
            "has a taste for fishing too,\x01",
            "but frankly, I don't get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "After all, the most\x01",
            "efficient way to fish is\x01",
            "to use a net.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_7456")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_740E():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_740E)
    Sleep(50)

    def lambda_741E():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_741E)
    Sleep(50)

    def lambda_742E():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_742E)
    Sleep(300)

    ChrTalk(
        0x104,
        "#00306FSo blunt...\x02",
    )

    CloseMessageWindow()
    Jump("loc_75A8")

    label("loc_7456")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_74FB")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_74AF():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_74AF)
    Sleep(50)

    def lambda_74BF():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_74BF)
    Sleep(50)

    def lambda_74CF():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_74CF)
    Sleep(300)

    ChrTalk(
        0x109,
        "#10106FSo outspoken...\x02",
    )

    CloseMessageWindow()
    Jump("loc_75A8")

    label("loc_74FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_75A8")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_7554():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7554)
    Sleep(50)

    def lambda_7564():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7564)
    Sleep(50)

    def lambda_7574():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7574)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10304FHehe. He says it like it\x01",
            "is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_75A8")

    SetScenarioFlags(0x1, 6)
    Jump("loc_75F0")

    label("loc_75B0")


    ChrTalk(
        0x1A2,
        (
            "I've no interest in a\x01",
            "place like this. Let's\x01",
            "go elsewhere.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_75F0")

    Jump("loc_78CD")

    label("loc_75F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_760B")
    Call(0, 26)
    Jump("loc_78CD")

    label("loc_760B")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_782E")
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked and\x01",
            "there's a message plate.\x07\x00\x02",
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
            "  ～Now Closed～\x01",
            "Imperial Fishing Club\x07\x00\x02",
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
            "#00005FClosed, huh? But what\x01",
            "could the Imperial\x01",
            "Fishing Club be...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FThis is the building of\x01",
            "the Fisherman's Guild\x01",
            "you joined, isn't it.\x02\x03",
            "#00100FHave you heard anything\x01",
            "from the other members?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FNo, I've been busy lately\x01",
            "and I haven't kept up my\x01",
            "fishing.\x02\x03",
            "#00000FIt also looks like it's\x01",
            "locked, so maybe we should\x01",
            "come again another time...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13F, 5)
    Jump("loc_78CD")

    label("loc_782E")

    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked and\x01",
            "there's a message plate.\x07\x00\x02",
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
            "  ～Now Closed～\x01",
            "Imperial Fishing Club\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_78CD")

    TalkEnd(0xFF)
    Return()

    # Function_35_71B0 end

    def Function_36_78D1(): pass

    label("Function_36_78D1")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79D5")

    ChrTalk(
        0x1A2,
        (
            "Hmm, is this an\x01",
            "apartment?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Is there anything\x01",
            "interesting in there...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FNo, that's not the\x01",
            "case...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Hmph, then there's no meaning\x01",
            "in going inside. Let's go to\x01",
            "the next place at once.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_7A71")

    label("loc_79D5")


    ChrTalk(
        0x1A2,
        (
            "Rudely breaking into strangers'\x01",
            "dwellings without having any\x01",
            "particular business isn't my style.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Come on, let's go to the\x01",
            "next place immediately.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A71")

    TalkEnd(0xFF)
    Return()

    # Function_36_78D1 end

    def Function_37_7A75(): pass

    label("Function_37_7A75")

    EventBegin(0x2)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "An Eastern Jizｷ Buddha\x01",
            "is enshrined here.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C26")

    ChrTalk(
        0x1A2,
        (
            "A Jizｷ Buddha, eh? It\x01",
            "looks just like the ones\x01",
            "in the Eastern Quarter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FAre there many there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Yeah, there are many kinds depending on\x01",
            "what you're praying for, like the burnt\x01",
            "Jizｷ or the thorn-pulling Jizｷ...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Well, I don't believe in\x01",
            "unseen miracles like\x01",
            "those, though.\x02",
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

    label("loc_7C26")

    EventEnd(0x3)
    Return()

    label("loc_7C29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EDD")

    ChrTalk(
        0x101,
        (
            "#00000FThis Jizｷ... It's always\x01",
            "being carefully cleaned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIt looks like someone\x01",
            "visits it often.\x02\x03",
            "Since we're here, why\x01",
            "don't we offer a dish we\x01",
            "made?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7D88")

    ChrTalk(
        0x105,
        (
            "#10300FWow, the Support Section\x01",
            "does stuff like this,\x01",
            "too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha... We don't always,\x01",
            "though. It'll also be good\x01",
            "cooking practice, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7DD3")

    label("loc_7D88")


    ChrTalk(
        0x104,
        (
            "#00300FWell, let's give it a\x01",
            "try. It'll be good\x01",
            "cooking practice too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DD3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7E7D")

    ChrTalk(
        0x109,
        (
            "#10100FThat's nice, I agree! If we\x01",
            "need an objective, perhaps we\x01",
            "could make it improvement...\x02\x03",
            "Let's try bringing it any\x01",
            "superb dishes we have.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EDA")

    label("loc_7E7D")


    ChrTalk(
        0x103,
        (
            "#00200FWe should make quick\x01",
            "progress.\x02\x03",
            "Let's try bringing it\x01",
            "any superb dishes we\x01",
            "have.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7EDA")

    SetScenarioFlags(0x20B, 0)

    label("loc_7EDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A14F")
    Call(0, 38)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F61")

    ChrTalk(
        0x101,
        (
            "#0000FWe don't have any\x01",
            "suitable dishes to offer\x01",
            "right now.\x02\x03",
            "Let's try bringing some\x01",
            "next time.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x3)
    Return()

    label("loc_7F61")

    Call(0, 39)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 6)), scpexpr(EXPR_END)), "loc_7F84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F7F")
    Call(0, 40)
    Return()

    label("loc_7F7F")

    Jump("loc_A14F")

    label("loc_7F84")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_83DD")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A letter accompanies a\x01",
            "small package.\x02",
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
            "To you, who always offers dishes...\x01",
            "Thank you very much for offering so\x01",
            "many dishes to the venerable Jizｷ.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Actually, I have been living nearby with my father since\x01",
            "I was little, and ever since then, because I prayed to it\x01",
            "every day, I have felt attached to the venerable Jizｷ.\x01",
            "Nowadays there are few who visit it, but I am secretly\x01",
            "glad there are warm-hearted people like yourselves. Allow\x01",
            "me to express my feelings of gratitude.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is reassuring that there is someone with the\x01",
            "same resolve aside from myself. I am sorry for\x01",
            "another lengthy letter. Though it is meager, please\x01",
            "accept this gift as a token of my gratitude.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is a pity I cannot yet meet you in person, but still\x01",
            "being healthy I will be able to regularly visit the\x01",
            "venerable Jizｷ daily like this. Perhaps I will be able\x01",
            "to meet you as well one day. -From an unknown neighbor.\x02",
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
            "Two Tearal Balms were\x01",
            "inside the package.\x02",
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
    Jump("loc_A14F")

    label("loc_83DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_886C")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a letter\x01",
            "bundled with a Teara\x01",
            "Balm.\x02",
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
            "With the strong sunlight and the green grass\x01",
            "steadily growing, I feel the summer presence has\x01",
            "finally arrived. To you who are always offering\x01",
            "dishes, I wish you good health day after day.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Speaking of myself, when I stopped by the government\x01",
            "office the other day, I happened to run into an\x01",
            "acquaintance of when I was a student. She had been away\x01",
            "from Crossbell for a very long time, but she came back\x01",
            "because of the son's family moving. Since we really\x01",
            "bumped into each other, we both were greatly surprised.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The temper we had when we were young didn't change, even\x01",
            "after growing old. We forgot to keep in touch with each\x01",
            "other and ended up in reminiscent talks about what was in\x01",
            "vogue in what year, and that it was hard during the war...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Perhaps such a fortuitous coincidence was arranged by\x01",
            "the venerable Jizｷ. I ended up talking to you about\x01",
            "something boring. I will continue to pray for your\x01",
            "good health. Allow me to close the letter like this.\x02",
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
    Jump("loc_A14F")

    label("loc_886C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8C66")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a letter\x01",
            "bundled with a Teara\x01",
            "Balm.\x02",
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
            "You, who always offer dishes, I wonder how you\x01",
            "have spent this day. I really must thank you\x01",
            "for always coming to visit the venerable Jizｷ.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The other day, when I stood in the kitchen as always,\x01",
            "thinking of a delicious dish to offer, I suddenly\x01",
            "thought "let me try making that" and I remembered...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When I was little, I was strictly trained in cooking by my\x01",
            "mother. I was enthusiastic thinking it would be fine, but\x01",
            "as you might imagine, not everything goes as smoothly as we\x01",
            "think. What she fussed over above all else was the cream\x01",
            "stew whose seasoning was a little different than usual. The\x01",
            "people in the house told me that it was good, though.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "These are times of endless incidents, but I am deeply\x01",
            "grateful to her for being able to live every day like\x01",
            "this. May you be visited by calm days as well.\x02",
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
    Jump("loc_A14F")

    label("loc_8C66")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9066")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a letter\x01",
            "bundled with a Teara\x01",
            "Balm.\x02",
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
            "The many days with a little rain continue in this\x01",
            "season... I wonder how are you spending them?\x01",
            "Thinking you will read this if you continue to\x01",
            "offer dishes, I selfishly write to you again.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yesterday when I was looking at the bustling street, I\x01",
            "happened to see energetic kids running around happily.\x01",
            "They are kids I see often in this neighborhood, but I\x01",
            "think that it is good that they get along well every day.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Crossbell gathers the attention of society somewhat, so\x01",
            "aren't healthy, growing children its greatest treasure?\x01",
            "I kept thinking about this and other things over and\x01",
            "over... I do hope these calm days continue on forever.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I have arrived at the end of this letter, but once again I\x01",
            "selfishly allowed myself to prepare a little gift for you.\x01",
            "I would be pleased if it was useful to you in some way.\x02",
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
    Jump("loc_A14F")

    label("loc_9066")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_92C4")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a letter\x01",
            "bundled with a Teara\x01",
            "Balm.\x02",
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
            "To you who always offers dishes, I thank you.\x01",
            "Seeing that there is someone aside from myself who\x01",
            "frequently visits the venerable Jizｷ and seeing\x01",
            "your delicious-looking offerings every time, my\x01",
            "days continued feeling relieved and warmhearted.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I don't know who you are, but today I selfishly allowed\x01",
            "myself to prepare a little gift for you. Please accept\x01",
            "it as consideration for your habitual devotion.\x02",
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
    Jump("loc_A14F")

    label("loc_92C4")

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

    label("loc_92F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A14F")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x190, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_934D")
    MenuCmd(1, 1, "Celestial Noodles "Sun"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 0)), scpexpr(EXPR_END)), "loc_9343")
    Call(2, 6)

    label("loc_9343")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_934D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x193, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_938B")
    MenuCmd(1, 1, "Immortal Mapo "Qilin"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 1)), scpexpr(EXPR_END)), "loc_9381")
    Call(2, 6)

    label("loc_9381")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_938B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x196, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_93C7")
    MenuCmd(1, 1, "Peerless Fried Rice")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 2)), scpexpr(EXPR_END)), "loc_93BD")
    Call(2, 6)

    label("loc_93BD")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_93C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x199, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_940B")
    MenuCmd(1, 1, "First-Rate Steak "Strength"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 3)), scpexpr(EXPR_END)), "loc_9401")
    Call(2, 6)

    label("loc_9401")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_940B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9442")
    MenuCmd(1, 1, "Three-Day Stew")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 4)), scpexpr(EXPR_END)), "loc_9438")
    Call(2, 6)

    label("loc_9438")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9482")
    MenuCmd(1, 1, "Land Hot Pot "Glorious"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 5)), scpexpr(EXPR_END)), "loc_9478")
    Call(2, 6)

    label("loc_9478")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_94BF")
    MenuCmd(1, 1, "Hot Pot "Calm Cloud"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 6)), scpexpr(EXPR_END)), "loc_94B5")
    Call(2, 6)

    label("loc_94B5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_94BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_94FD")
    MenuCmd(1, 1, "Express Fries "Rapid"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 7)), scpexpr(EXPR_END)), "loc_94F3")
    Call(2, 6)

    label("loc_94F3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_94FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A8, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9536")
    MenuCmd(1, 1, "Mega Omelet Rice")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 0)), scpexpr(EXPR_END)), "loc_952C")
    Call(2, 6)

    label("loc_952C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9536")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AB, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9573")
    MenuCmd(1, 1, "Jade Noodles "Sooth"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 1)), scpexpr(EXPR_END)), "loc_9569")
    Call(2, 6)

    label("loc_9569")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9573")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AE, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_95A9")
    MenuCmd(1, 1, "Double Burger")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 2)), scpexpr(EXPR_END)), "loc_959F")
    Call(2, 6)

    label("loc_959F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_95A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_95E6")
    MenuCmd(1, 1, "Quattro Cheese Pizza")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 3)), scpexpr(EXPR_END)), "loc_95DC")
    Call(2, 6)

    label("loc_95DC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_95E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9620")
    MenuCmd(1, 1, "Powerful Sandwich")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 4)), scpexpr(EXPR_END)), "loc_9616")
    Call(2, 6)

    label("loc_9616")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9620")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_965E")
    MenuCmd(1, 1, "Lunch Box "Sincerity"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 5)), scpexpr(EXPR_END)), "loc_9654")
    Call(2, 6)

    label("loc_9654")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_965E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BA, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9695")
    MenuCmd(1, 1, "Brilliant Soup")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 6)), scpexpr(EXPR_END)), "loc_968B")
    Call(2, 6)

    label("loc_968B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BD, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_96CA")
    MenuCmd(1, 1, "Wonder Candy")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 7)), scpexpr(EXPR_END)), "loc_96C0")
    Call(2, 6)

    label("loc_96C0")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_96CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C0, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_970B")
    MenuCmd(1, 1, "Heavenly "Midnight Moon"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 0)), scpexpr(EXPR_END)), "loc_9701")
    Call(2, 6)

    label("loc_9701")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_970B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C3, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_974B")
    MenuCmd(1, 1, "RoyalSweet "Snow White"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 1)), scpexpr(EXPR_END)), "loc_9741")
    Call(2, 6)

    label("loc_9741")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_974B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C6, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_978B")
    MenuCmd(1, 1, "Sherbert "Seven Colors"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 2)), scpexpr(EXPR_END)), "loc_9781")
    Call(2, 6)

    label("loc_9781")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_978B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C9, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_97C1")
    MenuCmd(1, 1, "Snack "Pulse"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 3)), scpexpr(EXPR_END)), "loc_97B7")
    Call(2, 6)

    label("loc_97B7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_97C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CC, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_97FD")
    MenuCmd(1, 1, "Tea "Summer Breeze"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 4)), scpexpr(EXPR_END)), "loc_97F3")
    Call(2, 6)

    label("loc_97F3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_97FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CF, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_983C")
    MenuCmd(1, 1, "Nectar "Bluish Purple"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 5)), scpexpr(EXPR_END)), "loc_9832")
    Call(2, 6)

    label("loc_9832")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_983C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9877")
    MenuCmd(1, 1, ""Nightmare Killer"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 6)), scpexpr(EXPR_END)), "loc_986D")
    Call(2, 6)

    label("loc_986D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9877")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_98B2")
    MenuCmd(1, 1, "Water "Shangri-la"")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 7)), scpexpr(EXPR_END)), "loc_98A8")
    Call(2, 6)

    label("loc_98A8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_98B2")

    MenuCmd(1, 1, "Cancel")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_98F6")
    Sleep(500)
    Jump("loc_A14A")

    label("loc_98F6")

    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x190, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9960")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9956")
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


    label("loc_9956")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9960")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x193, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_99AB")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_99A1")
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


    label("loc_99A1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_99AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x196, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_99F6")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_99EC")
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


    label("loc_99EC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_99F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x199, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9A41")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A37")
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


    label("loc_9A37")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9A41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9A8C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A82")
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


    label("loc_9A82")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9A8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9AD7")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9ACD")
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


    label("loc_9ACD")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9AD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9B22")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B18")
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


    label("loc_9B18")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9B22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9B6D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B63")
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


    label("loc_9B63")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9B6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A8, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9BB8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BAE")
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


    label("loc_9BAE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9BB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AB, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9C03")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BF9")
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


    label("loc_9BF9")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9C03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AE, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9C4E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C44")
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


    label("loc_9C44")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9C4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9C99")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C8F")
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


    label("loc_9C8F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9C99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9CE4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9CDA")
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


    label("loc_9CDA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9CE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9D2F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D25")
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


    label("loc_9D25")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9D2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BA, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9D7A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D70")
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


    label("loc_9D70")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9D7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BD, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9DC5")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9DBB")
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


    label("loc_9DBB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9DC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C0, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9E10")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E06")
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


    label("loc_9E06")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9E10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C3, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9E5B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E51")
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


    label("loc_9E51")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9E5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C6, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9EA6")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E9C")
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


    label("loc_9E9C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9EA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C9, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9EF1")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9EE7")
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


    label("loc_9EE7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9EF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CC, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9F3C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F32")
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


    label("loc_9F32")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9F3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CF, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9F87")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F7D")
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


    label("loc_9F7D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9F87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9FD2")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9FC8")
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


    label("loc_9FC8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9FD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A01D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A013")
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


    label("loc_A013")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A01D")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A14A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A147")

    ChrTalk(
        0x101,
        (
            "#00000FAll right, there we go.\x01",
            "...Let's bring things here\x01",
            "in the future, maybe.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A144")

    ChrTalk(
        0x102,
        (
            "#00100FSince always bringing the same dishes\x01",
            "would be rude, it would be nice if we\x01",
            "offered a different one each time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, let's do that.\x02",
    )

    CloseMessageWindow()

    label("loc_A144")

    SetScenarioFlags(0x20B, 1)

    label("loc_A147")

    SetScenarioFlags(0x2, 0)

    label("loc_A14A")

    Jump("loc_92F1")

    label("loc_A14F")

    EventEnd(0x3)
    Return()

    # Function_37_7A75 end

    def Function_38_A152(): pass

    label("Function_38_A152")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x190, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A175")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A175")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x193, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A18E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A18E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x196, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A1A7")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A1A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x199, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A1C0")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A1C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A1D9")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A1D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A1F2")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A1F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A20B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A20B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A224")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A224")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A8, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A23D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A23D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AB, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A256")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A256")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AE, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A26F")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A26F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A288")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A288")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A2A1")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A2A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A2BA")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A2BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BA, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A2D3")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A2D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BD, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A2EC")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A2EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C0, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A305")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A305")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C3, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A31E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A31E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C6, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A337")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A337")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C9, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A350")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CC, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A369")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CF, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A382")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A382")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A39B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A39B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A3B4")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A3B4")

    Return()

    # Function_38_A152 end

    def Function_39_A3B5(): pass

    label("Function_39_A3B5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 0)), scpexpr(EXPR_END)), "loc_A3D2")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A3D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 1)), scpexpr(EXPR_END)), "loc_A3E5")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A3E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 2)), scpexpr(EXPR_END)), "loc_A3F8")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A3F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 3)), scpexpr(EXPR_END)), "loc_A40B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A40B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 4)), scpexpr(EXPR_END)), "loc_A41E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A41E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 5)), scpexpr(EXPR_END)), "loc_A431")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A431")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 6)), scpexpr(EXPR_END)), "loc_A444")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 7)), scpexpr(EXPR_END)), "loc_A457")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A457")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 0)), scpexpr(EXPR_END)), "loc_A46A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A46A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 1)), scpexpr(EXPR_END)), "loc_A47D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A47D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 2)), scpexpr(EXPR_END)), "loc_A490")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A490")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 3)), scpexpr(EXPR_END)), "loc_A4A3")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A4A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 4)), scpexpr(EXPR_END)), "loc_A4B6")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A4B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 5)), scpexpr(EXPR_END)), "loc_A4C9")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A4C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 6)), scpexpr(EXPR_END)), "loc_A4DC")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A4DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 7)), scpexpr(EXPR_END)), "loc_A4EF")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A4EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 0)), scpexpr(EXPR_END)), "loc_A502")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 1)), scpexpr(EXPR_END)), "loc_A515")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A515")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 2)), scpexpr(EXPR_END)), "loc_A528")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A528")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 3)), scpexpr(EXPR_END)), "loc_A53B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A53B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 4)), scpexpr(EXPR_END)), "loc_A54E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A54E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 5)), scpexpr(EXPR_END)), "loc_A561")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A561")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 6)), scpexpr(EXPR_END)), "loc_A574")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 7)), scpexpr(EXPR_END)), "loc_A587")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A587")

    Return()

    # Function_39_A3B5 end

    def Function_40_A588(): pass

    label("Function_40_A588")

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
            "#00000F(...The Jizｷ we offered the dishes\x01",
            "to, eh...? I don't subscribe to\x01",
            "its religion, but...)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_93(0x101, 0xB4, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00002FSay, everyone, since we're\x01",
            "here, why don't we pray to\x01",
            "the Jizｷ before setting out?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0xE1, 0x1F4)

    ChrTalk(
        0x102,
        "#00100FMy, why not?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A79C")

    ChrTalk(
        0x109,
        (
            "#10100FA prayer for rescuing\x01",
            "KeA? ...I agree!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A79C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A7E6")

    ChrTalk(
        0x10A,
        (
            "#00606FHmph. We don't have time\x01",
            "for this, however...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A7E6")


    ChrTalk(
        0x103,
        (
            "#00202FWell, it won't take that much\x01",
            "time... This kind of thing is\x01",
            "a question of feelings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FThinkin' about our morale\x01",
            "from now on, I guess it's not\x01",
            "bad for mental concentration.\x02\x03",
            "#00309FAlright, let's do it!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x0, 0x1F4)

    ChrTalk(
        0x102,
        (
            "#00100FAs an Eastern custom,\x01",
            "you join your hands like\x01",
            "this...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        "#00005FOh, like this...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A9A8")

    ChrTalk(
        0x105,
        (
            "#10402FHehe. It seems it's also good\x01",
            "to drop your shoulders and\x01",
            "make about a 45 degree angle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A9A8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA6A")

    ChrTalk(
        0x106,
        (
            "#10702FActually, there's many\x01",
            "customs, but...\x02\x03",
            "#10704FI think that it's essentially\x01",
            "alright if you pray like you\x01",
            "do at a Septian Church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FAll right, let's do it.\x02",
    )

    CloseMessageWindow()

    label("loc_AA6A")

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
            "Lloyd and friends joined their\x01",
            "hands, closed their eyes and\x01",
            "offered a prayer to the Jizｷ.\x02",
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
            "My my, I'm sorry. I'm\x01",
            "hard of hearing.\x02",
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

    def lambda_ABE2():
        OP_95(0xFE, 12120, -300, 1430, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_ABE2)
    Sleep(1000)
    OP_68(12510, 1450, 1570, 8000)
    MoveCamera(57, 25, 0, 8000)
    Sleep(4000)
    WaitChrThread(0x2A, 1)
    Sleep(500)

    ChrTalk(
        0x2A,
        "Oh, it's you guys...\x02",
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

    def lambda_AC57():

        label("loc_AC57")

        TurnDirection(0xFE, 0x2A, 400)
        Yield()
        Jump("loc_AC57")

    QueueWorkItem2(0x101, 2, lambda_AC57)
    Sleep(50)

    def lambda_AC6C():

        label("loc_AC6C")

        TurnDirection(0xFE, 0x2A, 400)
        Yield()
        Jump("loc_AC6C")

    QueueWorkItem2(0x102, 2, lambda_AC6C)
    Sleep(50)

    def lambda_AC81():

        label("loc_AC81")

        TurnDirection(0xFE, 0x2A, 400)
        Yield()
        Jump("loc_AC81")

    QueueWorkItem2(0x103, 2, lambda_AC81)
    Sleep(50)

    def lambda_AC96():

        label("loc_AC96")

        TurnDirection(0xFE, 0x2A, 400)
        Yield()
        Jump("loc_AC96")

    QueueWorkItem2(0x104, 2, lambda_AC96)
    Sleep(50)

    def lambda_ACAB():

        label("loc_ACAB")

        TurnDirection(0xFE, 0x2A, 400)
        Yield()
        Jump("loc_ACAB")

    QueueWorkItem2(0xF4, 2, lambda_ACAB)
    Sleep(50)

    def lambda_ACC0():

        label("loc_ACC0")

        TurnDirection(0xFE, 0x2A, 400)
        Yield()
        Jump("loc_ACC0")

    QueueWorkItem2(0xF5, 2, lambda_ACC0)
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
            "Could it be... Are you are the\x01",
            "ones who have been offering\x01",
            "dishes to the venerable Jizｷ...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FAh...that means\x01",
            "that...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205FAre you perhaps the one\x01",
            "who wrote those\x01",
            "letters...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x2A,
        (
            "Oh my, is that how it\x01",
            "is!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "However, to think that so many adorable\x01",
            "children would... I thought for sure it\x01",
            "was someone elderly like myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FAhaha. Actually, we\x01",
            "offered them as a chance\x01",
            "to practice our cooking...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FMaaan, we're surprised too. I think...\x01",
            "You're that old lady we see every now\x01",
            "and then in Downtown, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FBecause the letters are very refined\x01",
            "and skillfully written, I thought it\x01",
            "might've been someone elderly...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "Uhuhu, my apologies for\x01",
            "always taking up your\x01",
            "time with my letters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "But, that's right... Truly,\x01",
            "all manner of things can\x01",
            "happen in this world.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_B0CC():
        OP_95(0xFE, 14600, -300, 3080, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_B0CC)
    Sleep(800)
    EndChrThread(0x101, 0x2)
    OP_93(0x101, 0x0, 0x12C)

    def lambda_B0F4():
        OP_96(0xFE, 0x3F34, 0xFFFFFED4, 0x898, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B0F4)
    Sleep(50)
    EndChrThread(0x103, 0x2)
    OP_93(0x103, 0x0, 0x0)

    def lambda_B11C():
        OP_96(0xFE, 0x3B92, 0xFFFFFED4, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B11C)
    FadeToDark(2000, 0, -1)
    Sleep(50)
    EndChrThread(0xF4, 0x2)

    def lambda_B147():
        OP_96(0xFE, 0x3D68, 0xFFFFFED4, 0xFFFFFF9C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_B147)
    WaitChrThread(0x2A, 1)

    def lambda_B165():
        OP_95(0xFE, 17260, -300, 3820, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_B165)
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
            "Paola faced towards the\x01",
            "Jizｷ and silently joined\x01",
            "her hands.\x02",
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
            "This venerable Jizｷ experienced all\x01",
            "of the Crossbell's turbulent times\x01",
            "and it was even destroyed once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "Nevertheless, it was restored\x01",
            "many times by the hands of\x01",
            "the people of this city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "...Recently, the people who visit it\x01",
            "have markedly decreased, but... Haha,\x01",
            "it looks like I had no need to worry.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x2A, 0xB4, 0x190)

    ChrTalk(
        0x2A,
        (
            "Oh, right, I just happen\x01",
            "to have something nice\x01",
            "here with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "I hate to ask this of you,\x01",
            "but... if you like, I wonder\x01",
            "if you can accept it?\x02",
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
            "Haha, it's all right. It\x01",
            "is merely a thank-you\x01",
            "gift.\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x2A, 16010, -300, 2000, 1500, 0x0)
    TurnDirection(0x2A, 0x101, 500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xEC, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B537")
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
    Jump("loc_B580")

    label("loc_B537")

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

    label("loc_B580")


    def lambda_B585():
        OP_96(0xFE, 0x3E80, 0xFFFFFED4, 0xA00, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_B585)

    def lambda_B59F():

        label("loc_B59F")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_B59F")

    QueueWorkItem2(0x101, 2, lambda_B59F)

    def lambda_B5B1():

        label("loc_B5B1")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_B5B1")

    QueueWorkItem2(0x102, 2, lambda_B5B1)

    def lambda_B5C3():

        label("loc_B5C3")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_B5C3")

    QueueWorkItem2(0x103, 2, lambda_B5C3)

    def lambda_B5D5():

        label("loc_B5D5")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_B5D5")

    QueueWorkItem2(0x104, 2, lambda_B5D5)

    def lambda_B5E7():

        label("loc_B5E7")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_B5E7")

    QueueWorkItem2(0xF4, 2, lambda_B5E7)

    def lambda_B5F9():

        label("loc_B5F9")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_B5F9")

    QueueWorkItem2(0xF5, 2, lambda_B5F9)
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
            "I received it from my\x01",
            "junior, but I can't wear\x01",
            "it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "...Uhuhu, that Imelda. She's\x01",
            "always awkward no matter how\x01",
            "much time passes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "Goodbye then. Please feel\x01",
            "free to visit the venerable\x01",
            "Jizｷ again whenever you like.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x2A, 0x10E, 0x1F4)

    def lambda_B798():
        OP_95(0xFE, -1050, -300, 2150, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_B798)
    Sleep(5000)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0xF4, 0x2)
    EndChrThread(0xF5, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B832")

    ChrTalk(
        0x109,
        (
            "#10102FHmm, I wonder who that old\x01",
            "lady was? She was extremely\x01",
            "dashing though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B881")

    label("loc_B832")


    ChrTalk(
        0x104,
        (
            "#00302F*sigh*... I haven't the\x01",
            "slightest clue, but she\x01",
            "was a brave woman.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B881")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B970")

    ChrTalk(
        0x106,
        (
            "#10702FShe's an old lady who often basks in the\x01",
            "sun near the apartment where I live.\x02\x03",
            "#10704FShe's now lives in Downtown, but it looks\x01",
            "like she lived somewhere else before... I\x01",
            "thought she was a beautiful person.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9B5")

    label("loc_B970")


    ChrTalk(
        0x103,
        (
            "#00202FShe's quite advanced in\x01",
            "old age, but she looked\x01",
            "healthy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B9B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_END)), "loc_BA30")

    ChrTalk(
        0x101,
        (
            "#00005FThis is a master quartz... Also,\x01",
            "she mentioned Mrs. Imelda's name\x01",
            "and said she was her junior...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BAA5")

    label("loc_BA30")


    ChrTalk(
        0x101,
        (
            "#00005FThis is a rare high-rank quartz...\x01",
            "Also, she mentioned Mrs. Imelda's\x01",
            "name and said she was her junior...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BAA5")


    ChrTalk(
        0x102,
        (
            "#00100FShe was really a kind and mysterious\x01",
            "person.\x02\x03",
            "#00103F(Come to think of it... I heard from\x01",
            "grandfather about a splendid woman called\x01",
            "the legendary Belle of High Society in\x01",
            "one of the older generations...)\x02\x03",
            "(...I-Impossible.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BC0E")

    ChrTalk(
        0x10A,
        (
            "#00606F(...These kids don't know her? She's\x01",
            "a famous lady who took Crossbell by\x01",
            "storm back in the day.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BC0E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BCEC")

    ChrTalk(
        0x105,
        (
            "#10404FHehe. I might come to\x01",
            "pray here every now and\x01",
            "then.\x02\x03",
            "#10400FHowever, leader, is this\x01",
            "a good time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FOh, you're right. I got\x01",
            "carried away myself...\x02\x03",
            "#00000FAlright, let's go then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BDA8")

    label("loc_BCEC")


    ChrTalk(
        0x101,
        (
            "#00004FI only wanted to pay a visit but it\x01",
            "unexpectedly turned into something...\x01",
            "It seems I got carried away.\x02\x03",
            "#00000FAlright, I guess it's time for us to\x01",
            "be going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FYeah!\x02",
    )

    CloseMessageWindow()

    label("loc_BDA8")

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

    # Function_40_A588 end

    def Function_41_BE21(): pass

    label("Function_41_BE21")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BF9D")
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "What's this place?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThis is the home of the\x01",
            "president of Crossbell\x01",
            "Merchants Association.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FActually, we know him\x01",
            "fairly well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "Hmm, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "If he's the Merchants Association\x01",
            "President, then Cao and the\x01",
            "others must respect him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "If you like, why don't\x01",
            "we greet him?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C5, 3)
    OP_65(0x6, 0x1)
    SetMapObjFlags(0x3, 0x10)

    label("loc_BF9D")

    TalkEnd(0xFF)
    Return()

    # Function_41_BE21 end

    def Function_42_BFA1(): pass

    label("Function_42_BFA1")

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
            "Things have gotten\x01",
            "serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Hehe, but it'll be an\x01",
            "easy win.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Just one of us four\x01",
            "needs to beat that\x01",
            "Lakelord completely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "H-Hmm... I honestly\x01",
            "don't think I have what\x01",
            "it takes to beat him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "The other thing that\x01",
            "worries me is those\x01",
            ""Elite Four"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "There's also the limitless\x01",
            "retry rule. We'll win sooner\x01",
            "or later of course, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "At the very least, I don't\x01",
            "think beating them will be\x01",
            "as easy as Coppen says.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "According to rumors, each of them has\x01",
            "a real strength greater than that of\x01",
            "our so-called "Master Fishermen".\x02",
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
            "*s-sigh*... As I\x01",
            "thought, it'll be\x01",
            "impossible for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Hehe, I see... Things\x01",
            "have gotten interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Well, let's return to our\x01",
            "new branch for now and\x01",
            "hold a strategy meeting.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FNew branch, you say...?\x02",
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
            "Actually, Branch Manager Celdan has\x01",
            "found a building on the East\x01",
            "Crossbell Highway for our new office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Although it's a boat rental shed\x01",
            "that hasn't been used since it\x01",
            "was abandoned several years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "It's cramped, worn-out and crumbling,\x01",
            "but because it's near the river we can\x01",
            "even fish, so it's quite nice, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Yeah, I feel it's an\x01",
            "ideal place for our\x01",
            "fresh start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "You should see the sign when you come\x01",
            "to the Tangram Gate area at the\x01",
            "crossroads of East Crossbell Highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Follow it and it's a\x01",
            "little further south.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "If you have time, please\x01",
            "come visit us, Member\x01",
            "Lloyd.\x02",
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
            "Well then, Member Lloyd. I\x01",
            "plan to do something about\x01",
            "the Angler Duels before long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "However, since our numbers are few, we\x01",
            "can use all the help we can get. I'm\x01",
            "counting on you as well, Member Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FRight. I don't want to\x01",
            "be unable to fish in my\x01",
            "favorite spots, either.\x02\x03",
            "#00000FI'll support you as much\x01",
            "as I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Hehe. I won't lose\x01",
            "either, member Lloyd!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Then we'll take our\x01",
            "leave here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "Alright then, good luck!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, the same to all of\x01",
            "you!\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 43)
    Sleep(200)
    BeginChrThread(0x19, 3, 0, 43)
    Sleep(200)
    BeginChrThread(0x1A, 3, 0, 43)
    Sleep(1000)

    def lambda_C938():

        label("loc_C938")

        TurnDirection(0x101, 0x1A, 500)
        Yield()
        Jump("loc_C938")

    QueueWorkItem2(0x101, 2, lambda_C938)

    def lambda_C94A():

        label("loc_C94A")

        TurnDirection(0x102, 0x1A, 500)
        Yield()
        Jump("loc_C94A")

    QueueWorkItem2(0x102, 2, lambda_C94A)

    def lambda_C95C():

        label("loc_C95C")

        TurnDirection(0x109, 0x1A, 500)
        Yield()
        Jump("loc_C95C")

    QueueWorkItem2(0x109, 2, lambda_C95C)

    def lambda_C96E():

        label("loc_C96E")

        TurnDirection(0x105, 0x1A, 500)
        Yield()
        Jump("loc_C96E")

    QueueWorkItem2(0x105, 2, lambda_C96E)

    def lambda_C980():

        label("loc_C980")

        TurnDirection(0x104, 0x1A, 500)
        Yield()
        Jump("loc_C980")

    QueueWorkItem2(0x104, 2, lambda_C980)
    WaitChrThread(0x1B, 3)

    ChrTalk(
        0x102,
        (
            "#00109F(Hmm. Lloyd seems happy\x01",
            "for some reason.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F(Fishing, huh...? I don't get it\x01",
            "myself, but there are a lot of\x01",
            "people who are passionate about it.)\x02",
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

    # Function_42_BFA1 end

    def Function_43_CADD(): pass

    label("Function_43_CADD")

    OP_93(0xFE, 0x87, 0x1F4)
    OP_95(0xFE, 110, -300, 1300, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x0)
    OP_95(0xFE, 14590, -300, 1300, 2000, 0x0)
    Return()

    # Function_43_CADD end

    def Function_44_CB14(): pass

    label("Function_44_CB14")

    EventBegin(0x1)
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "There's no need to show\x01",
            "me this place. Let's go\x01",
            "somewhere else.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 1910, -3000, -35980, 0)
    EventEnd(0x4)
    Return()

    # Function_44_CB14 end

    def Function_45_CB79(): pass

    label("Function_45_CB79")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CBFF")

    ChrTalk(
        0x1A2,
        (
            "Hey, isn't this the way\x01",
            "out of the city?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000FYeah, indeed it is.\x01",
            "Let's return to the\x01",
            "city.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_CC46")

    label("loc_CBFF")


    ChrTalk(
        0x101,
        (
            "#00000FWe can't leave for the\x01",
            "highway. Let's go back\x01",
            "to the city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CC46")

    SetChrPos(0x0, 29390, -300, 500, 270)
    EventEnd(0x4)
    Return()

    # Function_45_CB79 end

    def Function_46_CC5A(): pass

    label("Function_46_CC5A")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CCE9")

    ChrTalk(
        0x101,
        (
            "#00000FEast Crossbell Highway\x01",
            "is this way.\x02\x03",
            "We don't have any\x01",
            "special business this\x01",
            "way, so let's not exit.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    Jump("loc_CD44")

    label("loc_CCE9")


    ChrTalk(
        0x101,
        (
            "#00000FWe don't have any particular\x01",
            "business this way, so let's\x01",
            "refrain from leaving.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CD44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CE49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CDE0")

    ChrTalk(
        0x101,
        (
            "#00001FEast Crossbell Highway is\x01",
            "this way.\x02\x03",
            "For now, let's focus on\x01",
            "accident investigation\x01",
            "without taking any detours.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    Jump("loc_CE49")

    label("loc_CDE0")


    ChrTalk(
        0x101,
        (
            "#00001FWe don't have any special\x01",
            "business this way. For now, let's\x01",
            "focus on accident investigation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CE49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CEAD")

    ChrTalk(
        0x101,
        (
            "#00001FWe've got to chase after\x01",
            "Randy... This is no time\x01",
            "to be wandering around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CEAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CF02")

    ChrTalk(
        0x101,
        (
            "#00001FThis is no time to be\x01",
            "leaving the city. Let's\x01",
            "turn around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CFBE")

    ChrTalk(
        0x101,
        (
            "#00001FWe've come this far. There's no way\x01",
            "we're leaving the city now.\x02\x03",
            "The Orchis Tower infiltration\x01",
            "operation... We have to do whatever\x01",
            "it takes to make it a success.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CFBE")

    SetChrPos(0x0, 29390, -300, 500, 270)
    EventEnd(0x4)
    Return()

    # Function_46_CC5A end

    def Function_47_CFD2(): pass

    label("Function_47_CFD2")

    EventBegin(0x1)

    ChrTalk(
        0x105,
        (
            "#10303F...Lloyd, I'm sorry, but if we're\x01",
            "going back to Downtown, could you\x01",
            "give me a little more time?\x02\x03",
            "#10308FEven a tiny bit is fine. Going\x01",
            "back immediately would be, like\x01",
            "you can imagine, a little...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FYeah... All right.\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 1610, -3000, -35150, 0)
    EventEnd(0x4)
    Return()

    # Function_47_CFD2 end

    SaveToFile()

Try(main)
