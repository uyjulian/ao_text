from ScenarioHelper import *

def main():
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
        "Cronk",               # 1
        "Dins",               # 2
        "Lily",                 # 3
        "Marte",                 # 4
        "Danang",                 # 5
        "Anne",                 # 6
        "Renault grandfather",           # 7
        "Roy",                   # 8
        "Meyrin",               # 9
        "Susan",               # 10
        "Gillet",                   # 11
        "Kuta",                 # 12
        "Mols old man",             # 13
        "Investigator",                 # 14
        "car",                     # 15
        "Runaway vehicle",                 # 16
        "Police car",               # 17
        "Serdan branch chief",         # 18
        "Copan",                 # 19
        "Peter",               # 20
        "Charlie",             # 21
        "Defense Forces soldier",             # 22
        "Defense Forces soldier",             # 23
        "Citizen 1",                 # 24
        "Citizen 2",                 # 25
        "Citizen 3",                 # 26
        "Citizen 4",                 # 27
        "Citizen 5",                 # 28
        "Citizen 6",                 # 29
        "Citizen 7",                 # 30
        "Policeman",                   # 31
        "Policeman",                   # 32
        "Policeman",                   # 33
        "Policeman",                   # 34
        "Paola Lady",           # 35
        "bc1000",                 # 36
        "Central square",               # 37
        "Nishi dori",                 # 38
        "Administrative district",                 # 39
        "Residential area",                 # 40
        "Entertainment district",                 # 41
        "East Street",                 # 42
        "old Town",                 # 43
        "Harbor district",                 # 44
        "IBC",                 # 45
        "Beside the station",               # 46
        "Back street",                 # 47
        "Ursula interchange",           # 48
        "East Crossbell Highway",       # 49
        "West Crossbell Highway",       # 50
        "Mainz Mountain Road",           # 51
        "Orchis Tower",         # 52
    ))

    ATBonus("ATBonus_950", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_C605", 8,   8,   8,   8,   11,  11,  11)

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
        "BattleInfo_A20", 0x0000, 93, 6, 60, 4, 1, 25, 0, "bc1000", "Sepith_C605", 60, 30, 10, 0,
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

    PlaceName(-111.26000213623047, 0.0, 15.239999771118164, 0x0000, 0x0000, "Central square")
    PlaceName(-186.8800048828125, 0.0, 20.40999984741211, 0x0000, 0x0000, "Nishi dori")
    PlaceName(-80.20999908447266, 0.0, 117.58999633789062, 0x0000, 0x0000, "Administrative district")
    PlaceName(-257.0299987792969, 0.0, 106.08999633789062, 0x0000, 0x0000, "Residential area")
    PlaceName(-173.0800018310547, 0.0, 96.88999938964844, 0x0000, 0x0000, "Entertainment district")
    PlaceName(-17.829999923706055, 0.0, -11.210000038146973, 0x0000, 0x0000, "East Street")
    PlaceName(23.0, 0.0, -74.45999908447266, 0x0000, 0x0000, "old Town")
    PlaceName(14.380000114440918, 0.0, 64.69000244140625, 0x0000, 0x0000, "Harbor district")
    PlaceName(-15.529999732971191, 0.0, 172.7899932861328, 0x0000, 0x0000, "IBC")
    PlaceName(-98.33000183105469, 0.0, -64.11000061035156, 0x0000, 0x0000, "Beside the station")
    PlaceName(-152.3800048828125, 0.0, 55.4900016784668, 0x0000, 0x0000, "Back street")
    PlaceName(-101.77999877929688, 0.0, -99.76000213623047, 0x0000, 0x0000, "Ursula interchange")
    PlaceName(44.279998779296875, 0.0, 4.889999866485596, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-245.52999877929688, 0.0, 18.690000534057617, 0x0000, 0x0000, "West Crossbell Highway")
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
        "Function_13_20FC",        # 0D, 13
        "Function_14_2356",        # 0E, 14
        "Function_15_2B9E",        # 0F, 15
        "Function_16_2C89",        # 10, 16
        "Function_17_2EA9",        # 11, 17
        "Function_18_2EAA",        # 12, 18
        "Function_19_32EF",        # 13, 19
        "Function_20_34E2",        # 14, 20
        "Function_21_3849",        # 15, 21
        "Function_22_38ED",        # 16, 22
        "Function_23_3DAA",        # 17, 23
        "Function_24_4129",        # 18, 24
        "Function_25_4673",        # 19, 25
        "Function_26_49C9",        # 1A, 26
        "Function_27_4E77",        # 1B, 27
        "Function_28_52E5",        # 1C, 28
        "Function_29_5B4D",        # 1D, 29
        "Function_30_6E13",        # 1E, 30
        "Function_31_6E2F",        # 1F, 31
        "Function_32_6E4B",        # 20, 32
        "Function_33_6E67",        # 21, 33
        "Function_34_6E83",        # 22, 34
        "Function_35_6E9F",        # 23, 35
        "Function_36_759B",        # 24, 36
        "Function_37_7706",        # 25, 37
        "Function_38_9AAA",        # 26, 38
        "Function_39_9D0D",        # 27, 39
        "Function_40_9EE0",        # 28, 40
        "Function_41_B57D",        # 29, 41
        "Function_42_B6EC",        # 2A, 42
        "Function_43_C0FB",        # 2B, 43
        "Function_44_C132",        # 2C, 44
        "Function_45_C18D",        # 2D, 45
        "Function_46_C258",        # 2E, 46
        "Function_47_C50E",        # 2F, 47
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D33")
    Sound(14, 0, 100, 0)
    OP_74(0x6, 0x1E)
    OP_71(0x6, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('Ｕ材料', 1)"), scpexpr(EXPR_END)), "loc_1CBC")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_1D2E")

    label("loc_1CBC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x6, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1D2E")

    Jump("loc_1D78")

    label("loc_1D33")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the treasure box.\x07\x00\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E84")
    Sound(14, 0, 100, 0)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('封魔之刃', 1)"), scpexpr(EXPR_END)), "loc_1E0D")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '封魔之刃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_1E7F")

    label("loc_1E0D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '封魔之刃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '封魔之刃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1E7F")

    Jump("loc_1EC9")

    label("loc_1E84")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the treasure box.\x07\x00\x02",
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
        "#11P#00205F…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FTio?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00105FDid you notice something?\x02",
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
            "#11P#00200FI got a little from this direction\x01",
            "I felt a sign … …\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#6P#00203F… …. Sorry, probably\x01",
            "I wonder if things are worrisome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FIs it…\x02",
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

    def Function_13_20FC(): pass

    label("Function_13_20FC")

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
        "#11P#00205F…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FTio?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FDid you notice something?\x02",
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
            "#11P#00200FI got a little from this direction\x01",
            "I felt a sign … …\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#6P#00203F… …. Sorry, probably\x01",
            "I wonder if things are worrisome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FIs it…\x02",
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

    # Function_13_20FC end

    def Function_14_2356(): pass

    label("Function_14_2356")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2363")
    Call(0, 15)
    Return()

    label("loc_2363")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2870")
    SetScenarioFlags(0x2, 2)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I was stood by the wall.\x01",
            "You can see the darkness through the gaps in the wooden board.\x07\x00\x02",
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
            "#12P#00005Fthis is……\x01",
            "It seems like I am familiar with somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105FDoes it go into the Geofront?\x02\x03",
            "#00103FApparently,\x01",
            "I'm going to move the board ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00305FDid you mean, just a while ago\x01",
            "Tio Suke has reacted …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00200FYes. It was from this place\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_25CE")

    ChrTalk(
        0x10A,
        "#12P#00603FHmm, it's a bit concerning\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_264F")

    label("loc_25CE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_260F")

    ChrTalk(
        0x109,
        "#12P#10105F…… Who is it?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_264F")

    label("loc_260F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_264F")

    ChrTalk(
        0x105,
        "#12P#10405F… … Did someone get lost?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_264F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_268A")

    ChrTalk(
        0x106,
        "#12P#10701FShould we check it out?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_2703")

    label("loc_268A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_26C9")

    ChrTalk(
        0x105,
        "#12P#10400FDo you want to check in and check it?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_2703")

    label("loc_26C9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2703")

    ChrTalk(
        0x109,
        "#12P#10101FDo you want to check in and see?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2703")

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
            "【Explore the state inside】\x01",      # 0
            "【I will stop it】\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2800")

    ChrTalk(
        0x101,
        (
            "#12P#00001FThat's right.\x01",
            "Just to be sure for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00200FOk then let's go in\x02",
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
    Jump("loc_286B")

    label("loc_2800")


    ChrTalk(
        0x101,
        (
            "#12P#00003F…… No, I forced it now.\x01",
            "It will not be a long way.\x02\x03",
            "#00000FLet's leave this place for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_286B")

    Jump("loc_2A3D")

    label("loc_2870")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A wooden plate is stood against the wall,\x01",
            "I can see the darkness from the gap.\x07\x00\x02",
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
            "【Explore the situation inside】\x01",      # 0
            "【I will stop it】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29D8")

    ChrTalk(
        0x101,
        (
            "#12P#00003FAs expected after all …\x01",
            "Just to be sure for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00101FWell, it makes me feel somewhat.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00200FOk then let's go in\x02",
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
    Jump("loc_2A3D")

    label("loc_29D8")


    ChrTalk(
        0x101,
        (
            "#12P#00003F…… now impossible\x01",
            "It will not be a long way.\x02\x03",
            "#00000FLet's leave this place for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A3D")

    Jump("loc_2B67")

    label("loc_2A42")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A wooden plate is stood against the wall,\x01",
            "I can see the darkness from the gap.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#12P#00003F(Raines san?\x01",
            "No way, the research company\x01",
            "I was a human being. )\x02",
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
            "【Go to the latent place of Rains】\x01",      # 0
            "【I will stop it】\x01",                    # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B67")
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("m0304", 100, 0, 0)
    IdleLoop()
    Jump("loc_2B67")

    label("loc_2B67")

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

    # Function_14_2356 end

    def Function_15_2B9E(): pass

    label("Function_15_2B9E")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C3B")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A wooden plate is stood against the wall,\x01",
            "It is firmly fixed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00005FMr. Raines, from that\x01",
            "It seems that it closed up tightly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_2C85")

    label("loc_2C3B")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A wooden plate is stood against the wall,\x01",
            "It is firmly fixed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2C85")

    TalkEnd(0xFF)
    Return()

    # Function_15_2B9E end

    def Function_16_2C89(): pass

    label("Function_16_2C89")

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
            "#00203FEven so\x01",
            "R & A research, is … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301FOh, what kind\x01",
            "It looks like an excellent organization.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00100FYes, whatever\x01",
            "Because it is a company of former Colonel Richard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWell, I tentatively\x01",
            "It can not be helped even if it takes more than necessary.\x02\x03",
            "#00001FAnyway now\x01",
            "Let's prepare for the rush into the tower.\x02",
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

    # Function_16_2C89 end

    def Function_17_2EA9(): pass

    label("Function_17_2EA9")

    Return()

    # Function_17_2EA9 end

    def Function_18_2EAA(): pass

    label("Function_18_2EAA")

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

    def lambda_2F2D():
        OP_96(0xFE, 0x640, 0xFFFFF448, 0xFFFF88DC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2F2D)
    Sleep(50)

    def lambda_2F4A():
        OP_96(0xFE, 0x640, 0xFFFFF448, 0xFFFF7B30, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F4A)
    Sleep(50)

    def lambda_2F67():
        OP_96(0xFE, 0x9C4, 0xFFFFF448, 0xFFFF77AC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2F67)
    Sleep(50)

    def lambda_2F84():
        OP_96(0xFE, 0x2BC, 0xFFFFF448, 0xFFFF7554, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2F84)
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
        "#12P#00008F#30WWadi\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 1)
    WaitChrThread(0x109, 1)

    ChrTalk(
        0x109,
        "#12P#10106F#30WWaj, you …\x02",
    )

    CloseMessageWindow()
    OP_64(0x105)
    Sleep(500)
    OP_93(0x105, 0xB4, 0x190)
    Sleep(150)

    ChrTalk(
        0x105,
        (
            "#5P#10304F#30W…… Ha ha.\x01",
            "You showed an unlikely place.\x02\x03",
            "#10302FIt seems a little uninteresting\x01",
            "Have you become hot?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FDisagreeable……\x02\x03",
            "#00000FWhat is it?\x01",
            "A man is such a thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FThe feeling of a boy\x01",
            "I do not know for a moment … ….\x02\x03",
            "#00100FYou will tell him, in good faith\x01",
            "I knew they were facing each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10112FYes yeah …!\x02\x03",
            "#10100FSomeday surely he also\x01",
            "I think you can understand it!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3241")

    ChrTalk(
        0x105,
        (
            "#5P#10304F#30WGiggle\x01",
            "I hope so.\x02\x03",
            "#10300F─ ─ I took time.\x01",
            "Let's go to a different place anyway.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32AC")

    label("loc_3241")


    ChrTalk(
        0x105,
        (
            "#5P#10304F#30WGiggle\x01",
            "I hope so.\x02\x03",
            "#10300F─ ─ I took time.\x01",
            "Let's clean up the remaining support requests.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32AC")

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

    # Function_18_2EAA end

    def Function_19_32EF(): pass

    label("Function_19_32EF")

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

    def lambda_3427():
        OP_98(0xFE, 0x2AF8, 0x0, 0xFFFFD508, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_3427)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -14300, -300, 11700, 135)

    def lambda_3457():
        OP_98(0xFE, 0x2AF8, 0x0, 0xFFFFD508, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_3457)
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

    # Function_19_32EF end

    def Function_20_34E2(): pass

    label("Function_20_34E2")

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

    # Function_20_34E2 end

    def Function_21_3849(): pass

    label("Function_21_3849")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_3881"),
        (1, "loc_3889"),
        (2, "loc_3891"),
        (3, "loc_3899"),
        (4, "loc_38A1"),
        (5, "loc_38A9"),
        (6, "loc_38B1"),
        (SWITCH_DEFAULT, "loc_38B9"),
    )


    label("loc_3881")

    Sleep(100)
    Jump("loc_38C1")

    label("loc_3889")

    Sleep(200)
    Jump("loc_38C1")

    label("loc_3891")

    Sleep(300)
    Jump("loc_38C1")

    label("loc_3899")

    Sleep(400)
    Jump("loc_38C1")

    label("loc_38A1")

    Sleep(500)
    Jump("loc_38C1")

    label("loc_38A9")

    Sleep(600)
    Jump("loc_38C1")

    label("loc_38B1")

    Sleep(700)
    Jump("loc_38C1")

    label("loc_38B9")

    Sleep(800)
    Jump("loc_38C1")

    label("loc_38C1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_38EC")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xFE)
    Sleep(500)
    Jump("loc_38C1")

    label("loc_38EC")

    Return()

    # Function_21_3849 end

    def Function_22_38ED(): pass

    label("Function_22_38ED")

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
            "#6P#00012FFuu …\x01",
            "I am tired somewhat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00102FI see …\x01",
            "Surely, Mary has\x01",
            "I am glad I found it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F… … Sorry.\x01",
            "Spoiled itoko bothers us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10112FHaha ……\x01",
            "My seniors are not responsible.\x02\x03",
            "#10100FTo that,\x01",
            "It sounds like a good boy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FWell, what are you saying?\x01",
            "He cooperated with me as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302Fmy mother……\x01",
            "Well, it is certainly not bad.\x02\x03",
            "#00306FThat's pretty annoying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00008FI see……\x01",
            "There seems to be various things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#11P#10304FHuff, to the whim of a girl\x01",
            "Also being swayed\x01",
            "I think that it is a man's worthiness.\x02\x03",
            "#10300FSo what are you gonna do?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x72, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x77, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C9D")

    ChrTalk(
        0x101,
        (
            "#6P#00004FThat's right.\x01",
            "The request for support was over.\x02\x03",
            "#00000FOnce you return to the support department\x01",
            "It might be good to take a break.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D10")

    label("loc_3C9D")


    ChrTalk(
        0x101,
        (
            "#6P#00003FThat's right.\x01",
            "I still have requests for support.\x02\x03",
            "#00000FOnce you return to the support department\x01",
            "It might be good to take a break.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D10")


    ChrTalk(
        0x102,
        (
            "#12P#00104FI see …\x01",
            "Shall I do so?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FThen, on a break\x01",
            "I will return to the support department.\x02",
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

    # Function_22_38ED end

    def Function_23_3DAA(): pass

    label("Function_23_3DAA")

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
            "─ ─ Of course, as I have noticed,\x01",
            "There is not one evil will.\x02\x03",
            "\"Government of the Republic of Calvert\" … …\x02\x03",
            "I was holding hands with a cunning criminal organization\x01",
            "They also have peace with Crossbell\x01",
            "It is trying to tramplish dignity.\x02",
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

    # Function_23_3DAA end

    def Function_24_4129(): pass

    label("Function_24_4129")

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

    def lambda_4293():
        OP_95(0x101, 1000, -3000, -14740, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4293)

    def lambda_42AD():
        OP_95(0x102, 2600, -3000, -13540, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_42AD)

    def lambda_42C7():
        OP_95(0x109, 2000, -3000, -15940, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_42C7)

    def lambda_42E1():
        OP_95(0x105, 3600, -2930, -14740, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_42E1)

    def lambda_42FB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_42FB)
    Sleep(300)

    def lambda_430F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_430F)
    Sleep(300)

    def lambda_4323():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4323)
    Sleep(300)

    def lambda_4337():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4337)
    Sleep(1500)
    SetMapObjFlags(0x4, 0x0)
    WaitChrThread(0x101, 1)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    WaitChrThread(0x102, 1)

    def lambda_4385():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4385)
    Sleep(300)

    def lambda_4395():
        OP_93(0x102, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4395)
    Sleep(300)

    def lambda_43A5():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_43A5)
    Sleep(300)

    def lambda_43B5():
        OP_93(0x105, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_43B5)
    Sleep(300)

    def lambda_43C5():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_43C5)
    Sleep(300)

    def lambda_43D5():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_43D5)
    Sleep(300)

    def lambda_43E5():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_43E5)
    Sleep(300)

    def lambda_43F5():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_43F5)
    Sleep(300)
    OP_0D()

    def lambda_4406():
        OP_93(0x101, 0x5A, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4406)

    def lambda_4413():
        OP_93(0x102, 0xB4, 0x5DC)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4413)

    def lambda_4420():
        OP_93(0x109, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4420)

    def lambda_442D():
        OP_93(0x105, 0x10E, 0x5DC)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_442D)
    OP_0D()
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        "#6P#00001FI am useless …… I lost sight of it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FAnd, it is an outrageous person.\x02\x03",
            "#10101FAs if we were coming\x01",
            "Like I was hooked on … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FWell, that's about that\x01",
            "I guess it's a piece of cake ……\x02\x03",
            "#00101FAs expected it is\x01",
            "I just have to serve as a captain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHuff, you are a very military person\x01",
            "It's a way I can not imagine.\x02\x03",
            "#10302FSo, are you giving up here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FDisagreeable……\x01",
            "Let's chase after anyway.\x02\x03",
            "#00000FNow if you ask someone on the street\x01",
            "You may be able to grasp it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FI understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10100Flet's go!\x02",
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

    # Function_24_4129 end

    def Function_25_4673(): pass

    label("Function_25_4673")

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

    def lambda_47D6():
        OP_9B(0x1, 0xFE, 0x0, 0x61A8, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_47D6)

    def lambda_47EB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_47EB)
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
        "Haha, ambush me!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x17,
        "Yuri",
        "Hun, it is Asahi.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x17,
        "Yuri",
        "Reggie, can not you shake it?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x17,
        "Reggie",
        (
            "Tosen,\x01",
            "That's not your enemy!\x02",
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

    def lambda_493B():
        OP_9B(0x1, 0x17, 0x0, 0x2710, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_493B)
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

    # Function_25_4673 end

    def Function_26_49C9(): pass

    label("Function_26_49C9")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 5)), scpexpr(EXPR_END)), "loc_4C08")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "~ Now preparing ~\x01",
            "- the emperor#4RAfternoon tea#club\x07\x00\x02",
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
        "#12P#00003FWell, it's the same as when we last saw … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FHey, Lloyd.\x01",
            "You really do not know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FOh, honest\x01",
            "What is happening?\x01",
            "I have no idea.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00005FOh … but apparently\x01",
            "The key seems to be open?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D03")

    label("loc_4C08")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "~ Now preparing ~\x01",
            "- the emperor#4RAfternoon tea#club\x07\x00\x02",
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
            "#12P#00003FUnder preparation?\x01",
            "But the Emperor 's Club is one …?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00005FOh … but apparently\x01",
            "The key seems to be open?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D03")


    NpcTalk(
        0x1A,
        "Voice of a young man",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5POh, you …\x01",
            "Still it is an angler! Is it?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Voice of a man",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11PThat's right.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Voice of a man",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11PSuch a brutal way,\x01",
            "I will never accept it.\x07\x00\x02",
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
        "#6P#00105FLloyd, what are you now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FOh, that's a voice I know.\x01",
            "Let me have you inside.\x02",
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

    # Function_26_49C9 end

    def Function_27_4E77(): pass

    label("Function_27_4E77")

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
            "#5PWhy is it such a thing …?\x01",
            "I am not convinced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#11PYes, no branch\x01",
            "I do not think I will be deprived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#11PTentatively, again\x01",
            "I have to consult with Serdan branch manager.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FUm, Peter.\x01",
            "Still not very good,\x01",
            "I can not see the story … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#11POh, Lloyd for a while\x01",
            "Because it was a holiday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#11PAnyway, once with everyone\x01",
            "Let's gather and talk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#11PTalking to the branch manager from now on,\x01",
            "Jazz bar in the back street\x01",
            "I will have you come to \"Galante\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#11PLloyd, please come also.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#5PWell then, we\x01",
            "From the moment I go.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_517E():
        OP_9B(0x0, 0x1A, 0x5A, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_517E)
    Sleep(50)

    def lambda_5196():
        OP_93(0x101, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5196)
    Sleep(50)

    def lambda_51A6():
        OP_93(0x102, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_51A6)
    Sleep(50)
    WaitChrThread(0x1B, 1)

    def lambda_51BA():
        OP_9B(0x0, 0x1B, 0x5A, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_51BA)
    Sleep(50)

    def lambda_51D2():
        OP_93(0x109, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_51D2)
    Sleep(50)

    def lambda_51E2():
        OP_93(0x105, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_51E2)
    Sleep(50)
    WaitChrThread(0x1B, 1)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)

    ChrTalk(
        0x102,
        "#5P#00105FI wonder what really happened.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00003FI do not really know.\x01",
            "Anyway I have to check the circumstances.\x02\x03",
            "#00000FLet us also head to the jazz bar.\x02",
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

    # Function_27_4E77 end

    def Function_28_52E5(): pass

    label("Function_28_52E5")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_5382")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x1A2, 0x80)
    Jump("loc_53C1")

    label("loc_5382")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_53A4")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x1A2, 0x80)
    Jump("loc_53C1")

    label("loc_53A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_53C1")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x1A2, 0x80)

    label("loc_53C1")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_5535")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x104, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, -19400, -310, 26000, 180)
    SetChrPos(0x102, -20100, -310, 26000, 180)
    SetChrPos(0x101, -19150, -310, 27200, 180)
    SetChrPos(0x104, -20350, -310, 27200, 180)

    def lambda_54C7():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_54C7)

    def lambda_54E1():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_54E1)
    Sleep(100)

    def lambda_54FE():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_54FE)
    Sleep(50)

    def lambda_551B():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_551B)
    Jump("loc_56D8")

    label("loc_5535")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_5609")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x109, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, -19400, -310, 26000, 180)
    SetChrPos(0x102, -20100, -310, 26000, 180)
    SetChrPos(0x101, -19150, -310, 27200, 180)
    SetChrPos(0x109, -20350, -310, 27200, 180)

    def lambda_559B():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_559B)

    def lambda_55B5():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_55B5)
    Sleep(100)

    def lambda_55D2():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_55D2)
    Sleep(50)

    def lambda_55EF():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_55EF)
    Jump("loc_56D8")

    label("loc_5609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_56D8")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x105, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, -19400, -310, 26000, 180)
    SetChrPos(0x102, -20100, -310, 26000, 180)
    SetChrPos(0x101, -19150, -310, 27200, 180)
    SetChrPos(0x105, -20350, -310, 27200, 180)

    def lambda_566F():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_566F)

    def lambda_5689():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5689)
    Sleep(100)

    def lambda_56A6():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_56A6)
    Sleep(50)

    def lambda_56C3():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_56C3)

    label("loc_56D8")

    SetCameraDistance(14560, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x1A2,
        "This is East Street ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Thus, slowly\x01",
            "It is my first time to look at it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#6P#00100FHehe, this is similar to my hometown\x01",
            "Do not you calm down?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "#11PWell, maybe so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#11PHuh, even though\x01",
            "Activities · The lively atmosphere of the eastern people street\x01",
            "It's not like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#11Pif there is a chance,\x01",
            "I will be my sister next time\x01",
            "I would like to guide the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "#11POr rather, I want to return with Kuni!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_5939")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#6P#00112FLet me see……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FReally, it's a big approach.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FOh, I feel stylish\x01",
            "I do not feel hidden baby.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AD7")

    label("loc_5939")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_5A0E")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00112FLet me see……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FReally, it's a big approach.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FHaha, in a sense\x01",
            "It might be envious.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AD7")

    label("loc_5A0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_5AD7")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00112FLet me see……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FReally, it's a big approach.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHuh, de fastball is also a nice place, though.\x02",
    )

    CloseMessageWindow()

    label("loc_5AD7")

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

    # Function_28_52E5 end

    def Function_29_5B4D(): pass

    label("Function_29_5B4D")

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
        "Oh, is there any business you need?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FYeah, hey\x01",
            "There was something I wanted to ask.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained the circumstances,\x01",
            "I asked if a kitten mary came.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        (
            "Oh, it is a kitten of the Bond family.\x01",
            "It is safe if the police are searching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "But unfortunately\x01",
            "I have not seen you today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It was set for just in case\x01",
            "Dried food of that child's favorite food\x01",
            "It was as it was ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "From here at least last night\x01",
            "I guess they have not come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00103FIs that so……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Always with that family\x01",
            "Favor#5RPatronage#I have you do it,\x01",
            "I'd like to become a force ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "You can find me somehow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYes, of course.\x02",
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
        "#00303FFirst off, is it a free swing?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#12P#10105FMr. Lloyd,\x01",
            "What are you going to do after this?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000FOh, tentatively for the time being\x01",
            "Listen as you listen … …\x02\x03",
            "#00003FAfter that the search range expands,\x01",
            "We may have to rely on the nose of Zeit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00105FThat's fine, but ….\x02\x03",
            "#00106F…… In a situation where Tio does not exist\x01",
            "I wonder if you can communicate properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FI see.\x02\x03",
            "#00000FBut well, there somehow\x01",
            "With gestures -\x02",
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
        "Voice of a girl",
        "#3949VOh, what are you doing?\x02",
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

    def lambda_61AB():

        label("loc_61AB")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_61AB")

    QueueWorkItem2(0x101, 1, lambda_61AB)

    def lambda_61BD():

        label("loc_61BD")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_61BD")

    QueueWorkItem2(0x104, 1, lambda_61BD)

    def lambda_61CF():

        label("loc_61CF")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_61CF")

    QueueWorkItem2(0x102, 1, lambda_61CF)

    def lambda_61E1():

        label("loc_61E1")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_61E1")

    QueueWorkItem2(0x109, 1, lambda_61E1)

    def lambda_61F3():

        label("loc_61F3")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_61F3")

    QueueWorkItem2(0x105, 1, lambda_61F3)
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
        "#12P#00011FI mean …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FRandy's …\x02",
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
            "Randy's older brother#2RHiud#Into a\x01",
            "You and your older sister.\x02\x03",
            "What are you doing in such a place?\x02",
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
            "#00303F…… I do not care.\x01",
            "Let me get away at last.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x1C,
        (
            "#04606FMum, I can not connect.\x02\x03",
            "#04600FWell then, your older sister\x01",
            "Should I ask the body?\x02\x03",
            "#04609FI also want to massively scrape and spray\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00112FWait a minute … …!\x02",
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
            "#12P#00003F…… As you can see,\x01",
            "In the job of the Special Affairs Support Division.\x02\x03",
            "#00001FBecause it is not related to you guys\x01",
            "Will not you get tangled?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1C, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1C,
        (
            "#04606FOh, I'm involved separately.\x01",
            "I do not plan on doing it.\x02\x03",
            "#04600FBy the way what kind of work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006FFu … … It can not be helped.\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "About the matter of kitten\x01",
            "He explained it carefully.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x1C,
        (
            "#04605FWell, I see.\x02\x03",
            "#04600FWell, that Mary,\x01",
            "How do you search now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FOh, now for the police dog\x01",
            "Depending on the force and trying to follow the smell -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#04609FHaha, that's no good.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00005FHuh……! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#04602FOlder brother, the dog seems to be detailed, but\x01",
            "About cats is not enough yet?\x02\x03",
            "#04604FMore, Marie\x01",
            "I have to feel it and think about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006FWell, what do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#04600FI do not know the details,\x01",
            "That family recently moved, do not you?\x02\x03",
            "#04604FThen I think that the answer is one.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00105FI see. How come\x01",
            "I wonder if I did not notice.\x02\x03",
            "#00100FIt's a residential area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#04600FWell, there is a house in front there?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00005FThat's right, Marie started from the beginning\x01",
            "I was about to go home …!\x02\x03",
            "#00001FHowever, not a new house,\x01",
            "To the house of the residential area where I lived before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10103FI see.\x01",
            "Then the line will pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10303FIf anything the dog is to people,\x01",
            "Cats are familiar with the house.\x02\x03",
            "#10300FAfter getting stuck with the owner\x01",
            "Given the behavioral patterns of cats\x01",
            "Do you understand immediately?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F…… Indeed Coppe and something\x01",
            "Do not leave the building of the support department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#04609FHaha, that kind of thing.\x02\x03",
            "#04602FWell then, I'm going ahead ♪\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1C, 0x0, 0x1F4)
    Sleep(300)

    def lambda_6B5C():
        OP_95(0xFE, 2270, -220, -3590, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_6B5C)
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
            "#00005FWell, no way … ….\x01",
            "Are you going to thrust your neck?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FIt looks like, Huh.\x02\x03",
            "#10300FJust a whimsical kitten ……\x01",
            "No, it should be called a Toriko child?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10106FI'm not stylish … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FWell, hmm … ….\x01",
            "I wonder what it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F…… Well, I have to get involved\x01",
            "That is not a dangerous person so far.\x02\x03",
            "#00300FPerhaps I'm getting tired of it,\x01",
            "Let's look at the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI understood……\x01",
            "Let us also go to residential areas as soon as possible.\x02",
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

    # Function_29_5B4D end

    def Function_30_6E13(): pass

    label("Function_30_6E13")

    OP_95(0x101, 750, -3000, -12700, 2000, 0x0)
    OP_93(0x101, 0x5A, 0x1F4)
    Return()

    # Function_30_6E13 end

    def Function_31_6E2F(): pass

    label("Function_31_6E2F")

    OP_95(0x102, 2530, -3000, -11630, 2000, 0x0)
    OP_93(0x102, 0xB4, 0x1F4)
    Return()

    # Function_31_6E2F end

    def Function_32_6E4B(): pass

    label("Function_32_6E4B")

    OP_95(0x104, 3790, -3000, -12940, 2000, 0x0)
    OP_93(0x104, 0x10E, 0x1F4)
    Return()

    # Function_32_6E4B end

    def Function_33_6E67(): pass

    label("Function_33_6E67")

    OP_95(0x109, 1400, -3000, -14510, 2000, 0x0)
    OP_93(0x109, 0x2D, 0x1F4)
    Return()

    # Function_33_6E67 end

    def Function_34_6E83(): pass

    label("Function_34_6E83")

    OP_95(0x105, 3200, -3000, -14560, 2000, 0x0)
    OP_93(0x105, 0x13B, 0x1F4)
    Return()

    # Function_34_6E83 end

    def Function_35_6E9F(): pass

    label("Function_35_6E9F")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_72D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7298")

    ChrTalk(
        0x1A2,
        "Hanging Club … …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, that is\x01",
            "The emperor#4RAfternoon tea#I read the club.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Hunk, I do not really know.\x01",
            "Is it a gathering of fishing fighters?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Also in the crossbell,\x01",
            "There is a similar Jinsh.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00105FIs that also in the Republic?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "Well, there is this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "By the way my grandfather\x01",
            "I am fishing fishing,\x01",
            "Honestly I can not understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Because if you take a fish\x01",
            "I am using ami\x01",
            "Ichiban is efficient.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_713D")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_70EE():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_70EE)
    Sleep(50)

    def lambda_70FE():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_70FE)
    Sleep(50)

    def lambda_710E():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_710E)
    Sleep(300)

    ChrTalk(
        0x104,
        "#00306FHey neither the body nor the lid … …\x02",
    )

    CloseMessageWindow()
    Jump("loc_7290")

    label("loc_713D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_71E9")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_7196():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7196)
    Sleep(50)

    def lambda_71A6():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_71A6)
    Sleep(50)

    def lambda_71B6():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_71B6)
    Sleep(300)

    ChrTalk(
        0x109,
        "#10106FI have no body and no lid …\x02",
    )

    CloseMessageWindow()
    Jump("loc_7290")

    label("loc_71E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_7290")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_7242():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7242)
    Sleep(50)

    def lambda_7252():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7252)
    Sleep(50)

    def lambda_7262():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7262)
    Sleep(300)

    ChrTalk(
        0x105,
        "#10304FHe has no body and lid.\x02",
    )

    CloseMessageWindow()

    label("loc_7290")

    SetScenarioFlags(0x1, 6)
    Jump("loc_72CD")

    label("loc_7298")


    ChrTalk(
        0x1A2,
        (
            "You are not interested in such a tokoro.\x01",
            "Let's go to other places.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72CD")

    Jump("loc_7597")

    label("loc_72D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_72E8")
    Call(0, 26)
    Jump("loc_7597")

    label("loc_72E8")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74DD")
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a key on the door,\x01",
            "It has a message plate.\x07\x00\x02",
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
            "~ Now preparing ~\x01",
            "- the emperor#4RAfternoon tea#club\x07\x00\x02",
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
            "#00005FUnder preparation?\x01",
            "But \"The Emperor's Club\" …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FHere, Lloyd was in.\x01",
            "It is a building of \"Fishing public division\".\x02\x03",
            "#00100FFrom other members\x01",
            "Are not you hearing anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FOh, I'm busy lately\x01",
            "Because it was not fishing.\x02\x03",
            "#00000FThe key seems to be closed,\x01",
            "Will I get out again?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13F, 5)
    Jump("loc_7597")

    label("loc_74DD")

    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a key on the door,\x01",
            "It has a message plate.\x07\x00\x02",
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
            "~ Now preparing ~\x01",
            "- the emperor#4RAfternoon tea#club\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_7597")

    TalkEnd(0xFF)
    Return()

    # Function_35_6E9F end

    def Function_36_759B(): pass

    label("Function_36_759B")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7702")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_768E")

    ChrTalk(
        0x1A2,
        "Well, is this an apartment?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Even if something interesting\x01",
            "Are you going to be there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FNo, I do not think so.\x01",
            "I do not mean ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Huh, if it does not mean there is no point.\x01",
            "Go ahead quickly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_7702")

    label("loc_768E")


    ChrTalk(
        0x1A2,
        (
            "I have no special business\x01",
            "Zukazuka at the residence of others\x01",
            "There is no shimmer pushing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "Come on, please go on.\x02",
    )

    CloseMessageWindow()

    label("loc_7702")

    TalkEnd(0xFF)
    Return()

    # Function_36_759B end

    def Function_37_7706(): pass

    label("Function_37_7706")

    EventBegin(0x2)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The eastern side Jizo is being served.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7886")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7883")

    ChrTalk(
        0x1A2,
        (
            "Jizo? -\x01",
            "Really, it is as if as the East Town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FAgain, are there so many?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Well, fire-burned Jizo,\x01",
            "Temple of the Jizo Noodle, according to the interest\x01",
            "There are various kinds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Well, I do not mind.\x01",
            "The invisible benefit is invisible\x01",
            "I do not believe it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FThat's right.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DC, 4)
    EventEnd(0x3)
    Return()

    label("loc_7883")

    EventEnd(0x3)
    Return()

    label("loc_7886")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B01")

    ChrTalk(
        0x101,
        (
            "#00000FJizo of here …\x01",
            "I always cleaned carefully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FSomeone is eagerly visited\x01",
            "It looks like you have it.\x02\x03",
            "It's been awful and we also\x01",
            "Shall I give you the dish you made?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_79D0")

    ChrTalk(
        0x105,
        (
            "#10300FOh, the support department\x01",
            "Do you want to do that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHahaha …… It is not always a translation.\x01",
            "Will it also be a practice of cooking, do not you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A08")

    label("loc_79D0")


    ChrTalk(
        0x104,
        (
            "#00300FWell, why do not you try it.\x01",
            "You also have to practice cooking.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A08")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7A9B")

    ChrTalk(
        0x109,
        (
            "#10100FOkay, I agree!\x01",
            "Where there are goals\x01",
            "It seems that I can improve my skill ……\x02\x03",
            "If there is a good dish\x01",
            "Shall I take it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AFE")

    label("loc_7A9B")


    ChrTalk(
        0x103,
        (
            "#00200FWhere there are goals\x01",
            "Progress is quick.\x02\x03",
            "If there is a good dish\x01",
            "Let's bring it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AFE")

    SetScenarioFlags(0x20B, 0)

    label("loc_7B01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9AA7")
    Call(0, 38)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B6F")

    ChrTalk(
        0x101,
        (
            "#0000FIt seems good to give\x01",
            "There is no food now.\x02\x03",
            "Let's take it next time.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x3)
    Return()

    label("loc_7B6F")

    Call(0, 39)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 6)), scpexpr(EXPR_END)), "loc_7B92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B8D")
    Call(0, 40)
    Return()

    label("loc_7B8D")

    Jump("loc_9AA7")

    label("loc_7B92")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7FBE")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Along with the parcel, a letter is attached.\x02",
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
            "Those who always provide dishes,\x01",
            "We had a lot of cooking for this treasure,\x01",
            "I'm really thankful to you.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Actually I was living around here with my father when I was young,\x01",
            "Because I was handling each day from that hour\x01",
            "This Jizo had a lot of thought.\x01",
            "Those who are visiting us now\x01",
            "Although it has become completely unclear,\x01",
            "To the heart warm person like you came\x01",
            "I was quietly glad and even I felt something I was saved.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is someone who has the same as other than me\x01",
            "It is very encouraging thing.\x01",
            "I have also been rude for a long time.\x01",
            "It is just a rough product, but please give me some thanks\x01",
            "Please accept it.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There are things that you can not see directly yet\x01",
            "I am sorry, I still feel healthy,\x01",
            "In this way you can come to visit us without fail.\x01",
            "You might as well meet with you, do not you?\x01\x01",
            "~ Stranger than your neighbor\x02",
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
            "Tialal medicine came out from the parcel.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '大回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got two pieces.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('大回复药', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x20B, 6)
    SetScenarioFlags(0x2, 0)
    Jump("loc_9AA7")

    label("loc_7FBE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_839D")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "With the tiara's medicine,\x01",
            "A letter is attached.\x02",
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
            "Green grass grows steadily in strong sunlight,\x01",
            "I think that the sign of summer has finally arrived.\x01",
            "Those who always provide dishes\x01",
            "We wish to express our gratitude for your health every day.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "As I mentioned, when I stopped by the office the other day,\x01",
            "I had a chance to meet my acquaintance from school age by chance.\x01",
            "She had been away from the crossbell for a long time\x01",
            "Because I was returning to my aircraft after my son and couple relocated,\x01",
            "It is really what I met with a rose, so please join us\x01",
            "I am surprised a lot.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When my youth is familiar with my mind, even when I get older\x01",
            "It does not change. Forgotten that it was long normal\x01",
            "That year that was popular, there was war and it was serious,\x01",
            "Flowers bloomed on memories stories.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It was by chance that we met with such luck\x01",
            "This may well be the rough idea of the Jizo.\x01",
            "I have also put up on a boring story,\x01",
            "While praying for your health,\x01",
            "I would like to place a brush.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '中回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('中回复药', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x20B, 5)
    Jump("loc_9AA7")

    label("loc_839D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8729")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "With the tiara's medicine,\x01",
            "A letter is attached.\x02",
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
            "Those who always provide dishes,\x01",
            "How is everything going today?\x01",
            "It seems that you came to visit Jizo again\x01",
            "Really, thank you always.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The other day, I was standing in the kitchen\x01",
            "I will tell you what delicious dishes are always served\x01",
            "Remember, let's make that item\x01",
            "It depends on me suddenly thought.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Cooking has been severely trained by my mother since childhood,\x01",
            "I wish I was enthusiastic about myself\x01",
            "After all, things, it does not work well.\x01",
            "It was a little bit different from the usual that I was able to make a big fuss\x01",
            "It was like a cream stew.\x01",
            "He told me that the person at home is delicious.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Although the incident is a constant world,\x01",
            "So that you can live everyday\x01",
            "I would like to thank you deeply.\x01",
            "I wish you a peaceful day.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '中回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('中回复药', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x20B, 4)
    Jump("loc_9AA7")

    label("loc_8729")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8AB3")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "With the tiara's medicine,\x01",
            "A letter is attached.\x02",
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
            "This season, days with a lot of rain will continue\x01",
            "How is everything going?\x01",
            "If you are always serving dishes\x01",
            "I thought I'd surely read it,\x01",
            "In addition, I decided to take a brush without permission.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "As I watched the lively street the other day the other day\x01",
            "Energetic kids are running around happily\x01",
            "There was something to see.\x01",
            "It is the children who often see around here,\x01",
            "Every day I am friendly, I smile.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In the world it is crossbell which gathers attention to something,\x01",
            "It is the healthy growth of children\x01",
            "Is not it the treasure of this town?\x01",
            "It was up to you to think about with a thought.\x01",
            "Indeed, it is good to keep peaceful days forever.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Although it became the last,\x01",
            "In addition, we got prepared coarse goods without permission.\x01",
            "I hope you find something useful.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '中回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('中回复药', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x20B, 3)
    Jump("loc_9AA7")

    label("loc_8AB3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8CAE")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "With the tiara's medicine,\x01",
            "A letter is attached.\x02",
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
            "Those who always provide dishes,\x01",
            "Thank you very much.\x01",
            "I will visit you eagerly besides myself\x01",
            "Every time I see a person and see a delicious offering\x01",
            "Hot heart warming days continued.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I do not know where anyone is,\x01",
            "Today I had prepared coarse goods without permission.\x01",
            "Thinking that it was due to daily condolences\x01",
            "Please accept it.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '中回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('中回复药', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x20B, 2)
    Jump("loc_9AA7")

    label("loc_8CAE")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Can you make good dishes?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8CE5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AA7")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天上面『日轮』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8D38")
    MenuCmd(1, 1, "Tenmoku noodle ≪sunflower≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 0)), scpexpr(EXPR_END)), "loc_8D2E")
    Call(2, 6)

    label("loc_8D2E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8D38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('神仙麻婆『麒麟』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8D71")
    MenuCmd(1, 1, "Shin Genenza ≪Kirin≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 1)), scpexpr(EXPR_END)), "loc_8D67")
    Call(2, 6)

    label("loc_8D67")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8D71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天下一品炒饭', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8DA4")
    MenuCmd(1, 1, "Fried rice with Tenkaichi")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 2)), scpexpr(EXPR_END)), "loc_8D9A")
    Call(2, 6)

    label("loc_8D9A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8DA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('极品牛排『刚』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8DDF")
    MenuCmd(1, 1, "Extreme steak ≪rigid≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 3)), scpexpr(EXPR_END)), "loc_8DD5")
    Call(2, 6)

    label("loc_8DD5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8DDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('三日久煮炖菜', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8E1A")
    MenuCmd(1, 1, "Three-day simmered stew")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 4)), scpexpr(EXPR_END)), "loc_8E10")
    Call(2, 6)

    label("loc_8E10")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8E1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('大地锅『烂漫』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8E51")
    MenuCmd(1, 1, "Earth pot ≪Romantic≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 5)), scpexpr(EXPR_END)), "loc_8E47")
    Call(2, 6)

    label("loc_8E47")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8E51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天河锅『瑞云』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8E88")
    MenuCmd(1, 1, "Tianhe 鍋 ≪Mui Yun≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 6)), scpexpr(EXPR_END)), "loc_8E7E")
    Call(2, 6)

    label("loc_8E7E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8E88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('特快炸鱼『疾』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8EC1")
    MenuCmd(1, 1, "Express fly ≪Disease≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 7)), scpexpr(EXPR_END)), "loc_8EB7")
    Call(2, 6)

    label("loc_8EB7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8EC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('丰盛蛋包饭', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8EFA")
    MenuCmd(1, 1, "Mega Souce Omuraise")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 0)), scpexpr(EXPR_END)), "loc_8EF0")
    Call(2, 6)

    label("loc_8EF0")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8EFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('翠玉面『治愈』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8F31")
    MenuCmd(1, 1, "Jade ball noodles ≪healing≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 1)), scpexpr(EXPR_END)), "loc_8F27")
    Call(2, 6)

    label("loc_8F27")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8F31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('双层汉堡', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8F68")
    MenuCmd(1, 1, "Double burger")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 2)), scpexpr(EXPR_END)), "loc_8F5E")
    Call(2, 6)

    label("loc_8F5E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8F68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('四味奶酪比萨', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8FA3")
    MenuCmd(1, 1, "Quattro cheese pizza")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 3)), scpexpr(EXPR_END)), "loc_8F99")
    Call(2, 6)

    label("loc_8F99")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8FA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('强效三明治', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8FDA")
    MenuCmd(1, 1, "Powerful Sand")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 4)), scpexpr(EXPR_END)), "loc_8FD0")
    Call(2, 6)

    label("loc_8FD0")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8FDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('真心盒饭『诚』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9011")
    MenuCmd(1, 1, "Mind-bent lunch ≪Makoto≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 5)), scpexpr(EXPR_END)), "loc_9007")
    Call(2, 6)

    label("loc_9007")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9011")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('辉煌汤', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_904C")
    MenuCmd(1, 1, "Brilliant soup")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 6)), scpexpr(EXPR_END)), "loc_9042")
    Call(2, 6)

    label("loc_9042")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_904C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('奇幻糖果', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9087")
    MenuCmd(1, 1, "Wonder Candy")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 7)), scpexpr(EXPR_END)), "loc_907D")
    Call(2, 6)

    label("loc_907D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9087")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天上甜点『夜月』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_90BC")
    MenuCmd(1, 1, "Amakusa ≪夜 月≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 0)), scpexpr(EXPR_END)), "loc_90B2")
    Call(2, 6)

    label("loc_90B2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_90BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('宝物甜点『白雪』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_90F1")
    MenuCmd(1, 1, "Treasures ≪Snow White≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 1)), scpexpr(EXPR_END)), "loc_90E7")
    Call(2, 6)

    label("loc_90E7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_90F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('冰凉甜点『七彩』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9126")
    MenuCmd(1, 1, "Frozen dessert ≪sea urchin≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 2)), scpexpr(EXPR_END)), "loc_911C")
    Call(2, 6)

    label("loc_911C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('绝品甜点『瞬动』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_915B")
    MenuCmd(1, 1, "Confection ≪Spirit≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 3)), scpexpr(EXPR_END)), "loc_9151")
    Call(2, 6)

    label("loc_9151")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_915B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('玉露『绿风』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9190")
    MenuCmd(1, 1, "Gyokuro ≪Green wind≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 4)), scpexpr(EXPR_END)), "loc_9186")
    Call(2, 6)

    label("loc_9186")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9190")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('甘露『紫绀』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_91C5")
    MenuCmd(1, 1, "Honorable ≪purple blue≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 5)), scpexpr(EXPR_END)), "loc_91BB")
    Call(2, 6)

    label("loc_91BB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_91C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑茶『梦魇杀手』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_91FE")
    MenuCmd(1, 1, "Black tea ≪Mumma Kill≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 6)), scpexpr(EXPR_END)), "loc_91F4")
    Call(2, 6)

    label("loc_91F4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_91FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('秘水『桃源乡』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9235")
    MenuCmd(1, 1, "Hidden ≪Togeno-jou≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 7)), scpexpr(EXPR_END)), "loc_922B")
    Call(2, 6)

    label("loc_922B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9235")

    MenuCmd(1, 1, "quit")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9279")
    Sleep(500)
    Jump("loc_9AA2")

    label("loc_9279")

    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天上面『日轮』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_92E4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92DA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('天上面『日轮』', 1)
    SetScenarioFlags(0x208, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '天上面『日轮』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_92DA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_92E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('神仙麻婆『麒麟』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9330")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9326")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('神仙麻婆『麒麟』', 1)
    SetScenarioFlags(0x208, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '神仙麻婆『麒麟』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_9326")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天下一品炒饭', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_937C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9372")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('天下一品炒饭', 1)
    SetScenarioFlags(0x208, 2)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '天下一品炒饭'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_9372")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_937C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('极品牛排『刚』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_93C8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93BE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('极品牛排『刚』', 1)
    SetScenarioFlags(0x208, 3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '极品牛排『刚』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_93BE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_93C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('三日久煮炖菜', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9414")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_940A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('三日久煮炖菜', 1)
    SetScenarioFlags(0x208, 4)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '三日久煮炖菜'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_940A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('大地锅『烂漫』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9460")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9456")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('大地锅『烂漫』', 1)
    SetScenarioFlags(0x208, 5)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '大地锅『烂漫』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_9456")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天河锅『瑞云』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_94AC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94A2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('天河锅『瑞云』', 1)
    SetScenarioFlags(0x208, 6)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '天河锅『瑞云』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_94A2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_94AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('特快炸鱼『疾』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_94F8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94EE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('特快炸鱼『疾』', 1)
    SetScenarioFlags(0x208, 7)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '特快炸鱼『疾』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_94EE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_94F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('丰盛蛋包饭', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9544")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_953A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('丰盛蛋包饭', 1)
    SetScenarioFlags(0x209, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '丰盛蛋包饭'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_953A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9544")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('翠玉面『治愈』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9590")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9586")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('翠玉面『治愈』', 1)
    SetScenarioFlags(0x209, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '翠玉面『治愈』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_9586")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9590")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('双层汉堡', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_95DC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_95D2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('双层汉堡', 1)
    SetScenarioFlags(0x209, 2)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '双层汉堡'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_95D2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_95DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('四味奶酪比萨', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9628")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_961E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('四味奶酪比萨', 1)
    SetScenarioFlags(0x209, 3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '四味奶酪比萨'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_961E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9628")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('强效三明治', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9674")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_966A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('强效三明治', 1)
    SetScenarioFlags(0x209, 4)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '强效三明治'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_966A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9674")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('真心盒饭『诚』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_96C0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96B6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('真心盒饭『诚』', 1)
    SetScenarioFlags(0x209, 5)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '真心盒饭『诚』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_96B6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_96C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('辉煌汤', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_970C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9702")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('辉煌汤', 1)
    SetScenarioFlags(0x209, 6)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '辉煌汤'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_9702")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_970C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('奇幻糖果', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9758")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_974E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('奇幻糖果', 1)
    SetScenarioFlags(0x209, 7)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '奇幻糖果'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_974E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9758")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天上甜点『夜月』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_97A4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_979A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('天上甜点『夜月』', 1)
    SetScenarioFlags(0x20A, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '天上甜点『夜月』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_979A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_97A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('宝物甜点『白雪』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_97F0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97E6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('宝物甜点『白雪』', 1)
    SetScenarioFlags(0x20A, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '宝物甜点『白雪』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_97E6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_97F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('冰凉甜点『七彩』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_983C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9832")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('冰凉甜点『七彩』', 1)
    SetScenarioFlags(0x20A, 2)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '冰凉甜点『七彩』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_9832")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_983C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('绝品甜点『瞬动』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9888")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_987E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('绝品甜点『瞬动』', 1)
    SetScenarioFlags(0x20A, 3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '绝品甜点『瞬动』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_987E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9888")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('玉露『绿风』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_98D4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_98CA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('玉露『绿风』', 1)
    SetScenarioFlags(0x20A, 4)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '玉露『绿风』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_98CA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_98D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('甘露『紫绀』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9920")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9916")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('甘露『紫绀』', 1)
    SetScenarioFlags(0x20A, 5)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '甘露『紫绀』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_9916")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9920")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑茶『梦魇杀手』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_996C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9962")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('黑茶『梦魇杀手』', 1)
    SetScenarioFlags(0x20A, 6)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '黑茶『梦魇杀手』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_9962")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_996C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('秘水『桃源乡』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_99B8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_99AE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('秘水『桃源乡』', 1)
    SetScenarioFlags(0x20A, 7)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '秘水『桃源乡』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_99AE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_99B8")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A9F")

    ChrTalk(
        0x101,
        (
            "#00000FWith this, okay.\x01",
            "I guess I should bring it again.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9A9C")

    ChrTalk(
        0x102,
        (
            "#00100FIf only the same dishes are said\x01",
            "It will be rude,\x01",
            "It seems that goods are good about once a piece.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, would you?\x02",
    )

    CloseMessageWindow()

    label("loc_9A9C")

    SetScenarioFlags(0x20B, 1)

    label("loc_9A9F")

    SetScenarioFlags(0x2, 0)

    label("loc_9AA2")

    Jump("loc_8CE5")

    label("loc_9AA7")

    EventEnd(0x3)
    Return()

    # Function_37_7706 end

    def Function_38_9AAA(): pass

    label("Function_38_9AAA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天上面『日轮』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9ACD")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9ACD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('神仙麻婆『麒麟』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9AE6")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9AE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天下一品炒饭', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9AFF")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9AFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('极品牛排『刚』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9B18")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9B18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('三日久煮炖菜', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9B31")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9B31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('大地锅『烂漫』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9B4A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9B4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天河锅『瑞云』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9B63")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9B63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('特快炸鱼『疾』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9B7C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9B7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('丰盛蛋包饭', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9B95")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9B95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('翠玉面『治愈』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9BAE")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9BAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('双层汉堡', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9BC7")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9BC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('四味奶酪比萨', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9BE0")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9BE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('强效三明治', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9BF9")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9BF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('真心盒饭『诚』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9C12")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9C12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('辉煌汤', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9C2B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9C2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('奇幻糖果', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9C44")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9C44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天上甜点『夜月』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9C5D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9C5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('宝物甜点『白雪』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9C76")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9C76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('冰凉甜点『七彩』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9C8F")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9C8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('绝品甜点『瞬动』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9CA8")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9CA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('玉露『绿风』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9CC1")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9CC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('甘露『紫绀』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9CDA")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9CDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑茶『梦魇杀手』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9CF3")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9CF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('秘水『桃源乡』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9D0C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9D0C")

    Return()

    # Function_38_9AAA end

    def Function_39_9D0D(): pass

    label("Function_39_9D0D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 0)), scpexpr(EXPR_END)), "loc_9D2A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9D2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 1)), scpexpr(EXPR_END)), "loc_9D3D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9D3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 2)), scpexpr(EXPR_END)), "loc_9D50")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9D50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 3)), scpexpr(EXPR_END)), "loc_9D63")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9D63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 4)), scpexpr(EXPR_END)), "loc_9D76")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9D76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 5)), scpexpr(EXPR_END)), "loc_9D89")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9D89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 6)), scpexpr(EXPR_END)), "loc_9D9C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9D9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 7)), scpexpr(EXPR_END)), "loc_9DAF")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9DAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 0)), scpexpr(EXPR_END)), "loc_9DC2")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9DC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 1)), scpexpr(EXPR_END)), "loc_9DD5")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9DD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 2)), scpexpr(EXPR_END)), "loc_9DE8")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9DE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 3)), scpexpr(EXPR_END)), "loc_9DFB")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9DFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 4)), scpexpr(EXPR_END)), "loc_9E0E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9E0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 5)), scpexpr(EXPR_END)), "loc_9E21")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9E21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 6)), scpexpr(EXPR_END)), "loc_9E34")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9E34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 7)), scpexpr(EXPR_END)), "loc_9E47")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9E47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 0)), scpexpr(EXPR_END)), "loc_9E5A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9E5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 1)), scpexpr(EXPR_END)), "loc_9E6D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9E6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 2)), scpexpr(EXPR_END)), "loc_9E80")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9E80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 3)), scpexpr(EXPR_END)), "loc_9E93")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9E93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 4)), scpexpr(EXPR_END)), "loc_9EA6")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9EA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 5)), scpexpr(EXPR_END)), "loc_9EB9")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9EB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 6)), scpexpr(EXPR_END)), "loc_9ECC")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9ECC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 7)), scpexpr(EXPR_END)), "loc_9EDF")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9EDF")

    Return()

    # Function_39_9D0D end

    def Function_40_9EE0(): pass

    label("Function_40_9EE0")

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
            "#00000F(…… Jizo which had cooked food ……\x01",
            "I do not wish for a request … …)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_93(0x101, 0xB4, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00002FI wish everyone, that's it.\x01",
            "Would you like to visit before you leave?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0xE1, 0x1F4)

    ChrTalk(
        0x102,
        "#00100FOh, is not it okay?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A0DD")

    ChrTalk(
        0x109,
        (
            "#10100FIt is Kaya's salvation prayer.\x01",
            "… … I agree!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A0DD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A127")

    ChrTalk(
        0x10A,
        (
            "#00606FHun, a castor-clad castor\x01",
            "It should not be … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A127")


    ChrTalk(
        0x103,
        (
            "#00202FWell, I will not take time.\x01",
            "Such things are problems of feelings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FGiven the future morale\x01",
            "It is not too bad for spiritual unification.\x02\x03",
            "#00309FLet's go ahead, try!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x0, 0x1F4)

    ChrTalk(
        0x102,
        (
            "#00100FIn customs of the east, doing like this\x01",
            "Fit your hands together.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        "#00005FOops, like this …?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A28D")

    ChrTalk(
        0x105,
        (
            "#10402FHuff, drop me a shoulder\x01",
            "It seems good to make it around 45 degrees?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A28D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A33A")

    ChrTalk(
        0x106,
        (
            "#10702FTruly various stuff\x01",
            "I have it, but ….\x02\x03",
            "#10704FNow I pray at the Seven Yigh Church\x01",
            "I think the same procedure is fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOkay, I will try it.\x02",
    )

    CloseMessageWindow()

    label("loc_A33A")

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
            "Lloyd closed his eyes with his hands together,\x01",
            "I prayed to the Jizo.\x02",
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
        "voice",
        (
            "Oh no, sorry.\x01",
            "My ears are far away.\x02",
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

    def lambda_A498():
        OP_95(0xFE, 12120, -300, 1430, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_A498)
    Sleep(1000)
    OP_68(12510, 1450, 1570, 8000)
    MoveCamera(57, 25, 0, 8000)
    Sleep(4000)
    WaitChrThread(0x2A, 1)
    Sleep(500)

    ChrTalk(
        0x2A,
        "Oh, you guys …\x02",
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

    def lambda_A50D():

        label("loc_A50D")

        TurnDirection(0xFE, 0x2A, 400)
        Yield()
        Jump("loc_A50D")

    QueueWorkItem2(0x101, 2, lambda_A50D)
    Sleep(50)

    def lambda_A522():

        label("loc_A522")

        TurnDirection(0xFE, 0x2A, 400)
        Yield()
        Jump("loc_A522")

    QueueWorkItem2(0x102, 2, lambda_A522)
    Sleep(50)

    def lambda_A537():

        label("loc_A537")

        TurnDirection(0xFE, 0x2A, 400)
        Yield()
        Jump("loc_A537")

    QueueWorkItem2(0x103, 2, lambda_A537)
    Sleep(50)

    def lambda_A54C():

        label("loc_A54C")

        TurnDirection(0xFE, 0x2A, 400)
        Yield()
        Jump("loc_A54C")

    QueueWorkItem2(0x104, 2, lambda_A54C)
    Sleep(50)

    def lambda_A561():

        label("loc_A561")

        TurnDirection(0xFE, 0x2A, 400)
        Yield()
        Jump("loc_A561")

    QueueWorkItem2(0xF4, 2, lambda_A561)
    Sleep(50)

    def lambda_A576():

        label("loc_A576")

        TurnDirection(0xFE, 0x2A, 400)
        Yield()
        Jump("loc_A576")

    QueueWorkItem2(0xF5, 2, lambda_A576)
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
        "#00105F……Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "Did you mean …… to your estate store\x01",
            "The food that was provided for me,\x01",
            "I wonder … you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FOh … that …! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FPerhaps, the Lord of that letter ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x2A,
        "Oh well, then, I guess so! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "But these pretty children\x01",
            "It was a lot of … … clearly\x01",
            "I thought that it was someone of my age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FAhah, in reality on cooking practice\x01",
            "Everyone was serving us ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FWow, this is amazing.\x01",
            "Surely … … I sometimes see it in old town\x01",
            "Old lady right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FYour letter is very elegant\x01",
            "Because it comes with a stroke\x01",
            "I thought that it might be older … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "Uhufu, you always write a letter\x01",
            "Sorry to be late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "But, was that so … ….\x01",
            "Indeed the world,\x01",
            "There are various things.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_A903():
        OP_95(0xFE, 14600, -300, 3080, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_A903)
    Sleep(800)
    EndChrThread(0x101, 0x2)
    OP_93(0x101, 0x0, 0x12C)

    def lambda_A92B():
        OP_96(0xFE, 0x3F34, 0xFFFFFED4, 0x898, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A92B)
    Sleep(50)
    EndChrThread(0x103, 0x2)
    OP_93(0x103, 0x0, 0x0)

    def lambda_A953():
        OP_96(0xFE, 0x3B92, 0xFFFFFED4, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A953)
    FadeToDark(2000, 0, -1)
    Sleep(50)
    EndChrThread(0xF4, 0x2)

    def lambda_A97E():
        OP_96(0xFE, 0x3D68, 0xFFFFFED4, 0xFFFFFF9C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_A97E)
    WaitChrThread(0x2A, 1)

    def lambda_A99C():
        OP_95(0xFE, 17260, -300, 3820, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_A99C)
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
            "Paola quietly adjusted his hands towards the Jizo.\x02",
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
            "Like this Jizo, crossbell\x01",
            "I have been experiencing the era of disturbance for a long time\x01",
            "Sometimes I was torn down once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "Still, with the hands of people in this city\x01",
            "You are recovering over and over again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "…… People who visit these days too\x01",
            "Although it decreased sharply … ….\x01",
            "Huh, it seems I did not need to worry.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x2A, 0xB4, 0x190)

    ChrTalk(
        0x2A,
        (
            "That's right, me,\x01",
            "I have just the right thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "It's bad for a top thing ….\x01",
            "I wonder if you do not accept it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FWell, well … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "Huh, it is okay.\x01",
            "Because it is only a feeling good.\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x2A, 16010, -300, 2000, 1500, 0x0)
    TurnDirection(0x2A, 0x101, 500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('草⑿', 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD24")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '草⑿'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('草⑿', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x2, 7)
    Jump("loc_AD71")

    label("loc_AD24")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '风耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('风耀珠', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_AD71")


    def lambda_AD76():
        OP_96(0xFE, 0x3E80, 0xFFFFFED4, 0xA00, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_AD76)

    def lambda_AD90():

        label("loc_AD90")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_AD90")

    QueueWorkItem2(0x101, 2, lambda_AD90)

    def lambda_ADA2():

        label("loc_ADA2")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_ADA2")

    QueueWorkItem2(0x102, 2, lambda_ADA2)

    def lambda_ADB4():

        label("loc_ADB4")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_ADB4")

    QueueWorkItem2(0x103, 2, lambda_ADB4)

    def lambda_ADC6():

        label("loc_ADC6")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_ADC6")

    QueueWorkItem2(0x104, 2, lambda_ADC6)

    def lambda_ADD8():

        label("loc_ADD8")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_ADD8")

    QueueWorkItem2(0xF4, 2, lambda_ADD8)

    def lambda_ADEA():

        label("loc_ADEA")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_ADEA")

    QueueWorkItem2(0xF5, 2, lambda_ADEA)
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
            "Although my junior child gave me,\x01",
            "I only have to decorate it ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "… …. Uhufu, Imleda.\x01",
            "Truly forever\x01",
            "I do not care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "Well then, you guys.\x01",
            "It is OK if you feel like it,\x01",
            "Please give me a visit to your estate.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x2A, 0x10E, 0x1F4)

    def lambda_AF9A():
        OP_95(0xFE, -1050, -300, 2150, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_AF9A)
    Sleep(5000)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0xF4, 0x2)
    EndChrThread(0xF5, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B03C")

    ChrTalk(
        0x109,
        (
            "#10102FWell, what kind of grandmother is your grandmother\x01",
            "Was it?\x01",
            "It was a person who was dashing quite a bit … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B087")

    label("loc_B03C")


    ChrTalk(
        0x104,
        (
            "#00302FHuh\x01",
            "It's impressive about what,\x01",
            "It is also a daunting human.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B087")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B159")

    ChrTalk(
        0x106,
        (
            "#10702FWell near my apartment\x01",
            "It is a grandmother who is sunny.\x02\x03",
            "#10704FI am in the old city now,\x01",
            "It seems that he lived in a different place ……\x01",
            "I thought that it was a beautiful person.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B193")

    label("loc_B159")


    ChrTalk(
        0x103,
        (
            "#00202FI'm pretty older,\x01",
            "You looked healthy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B193")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_END)), "loc_B206")

    ChrTalk(
        0x101,
        (
            "#00005FThis is Master Quartz ……\x01",
            "Besides, give out the name of Imelda\x01",
            "I was told that he was a junior, but …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B26D")

    label("loc_B206")


    ChrTalk(
        0x101,
        (
            "#00005FThis is rare top quartz ……\x01",
            "Besides, give out the name of Imelda\x01",
            "I was told that he was a junior, but …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B26D")


    ChrTalk(
        0x102,
        (
            "#00100FI am really kind hearted\x01",
            "It was a strange person.\x02\x03",
            "#00103F(That remembered … In one generation above your grandfather\x01",
            "It is called legendary \"Flower of social circle\"\x01",
            "I heard there was a nice woman … …)\x02\x03",
            "(… Well, maybe not.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B3A9")

    ChrTalk(
        0x10A,
        (
            "#00606F(… … Do not you know, Hiyukoko?\x01",
            "It was a long time ago with a crossbell\x01",
            "You're a famous lady. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B3A9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B481")

    ChrTalk(
        0x105,
        (
            "#10404FHuh, occasionally also wishing for an invitation\x01",
            "It is a thing to try.\x02\x03",
            "#10400FBut the leader, it is almost time\x01",
            "Is not it a good time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FOops, that's right.\x01",
            "It is a matter of enthusiasm ……\x02\x03",
            "#00000FOK, let's go then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B504")

    label("loc_B481")


    ChrTalk(
        0x101,
        (
            "#00004FI am going to visit\x01",
            "Although it became an unexpected thing ……\x01",
            "It seems that the burning has also entered.\x02\x03",
            "#00000FOK, let's go soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FOh!\x02",
    )

    CloseMessageWindow()

    label("loc_B504")

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

    # Function_40_9EE0 end

    def Function_41_B57D(): pass

    label("Function_41_B57D")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B6E8")
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "here……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYeah, Cross Bell Chamber of Commerce\x01",
            "Your president's home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThere is a little border\x01",
            "I'm being friends with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "Hmm, was that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "As the Chairman of the Chamber of Commerce,\x01",
            "Naturally Tsao also\x01",
            "You will have a glance … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "What is it?\x01",
            "It might be nice to say hello.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C5, 3)
    OP_65(0x6, 0x1)
    SetMapObjFlags(0x3, 0x10)

    label("loc_B6E8")

    TalkEnd(0xFF)
    Return()

    # Function_41_B57D end

    def Function_42_B6EC(): pass

    label("Function_42_B6EC")

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
            "#00003F\"Bomb victory\" or …\x01",
            "The story became somewhat bigger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Hello, but it's a good victory.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Some of the four people,\x01",
            "Finally that Lake Road\x01",
            "It would be fine to defeat it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "No……\x01",
            "To be honest, I must be a force\x01",
            "I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Also,\x01",
            "\"Fishing Jie the heavenly King\" …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "There are also rules with unrestricted retries.\x01",
            "Someday it will win\x01",
            "I'm stepping on … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "At least, as Copan says\x01",
            "I think it's not an easy game.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "In rumors, each\x01",
            "More than \"special class wrestler\" in my place\x01",
            "She seems to have ability.\x02",
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
        "#00005FWell, that's right ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Haha …\x01",
            "After all it is impossible for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Hello, I see. ….\x01",
            "Is not it interesting?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Well, anyway once,\x01",
            "Returning to the new branch, it's a strategy meeting.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FNew branch, is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Oh, to Lloyd\x01",
            "I did not say that yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Actually in the direction of the East Crossbell Highway\x01",
            "The branch chief will be the new office building\x01",
            "I found it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Since being abandoned several years ago,\x01",
            "It was not used for a long time\x01",
            "It is a boat hut for rent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "It's narrow and boring but\x01",
            "I can fish in a nearby river,\x01",
            "It's quite a comfortable place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Oh, exactly to start again\x01",
            "Turning out to us for ourselves\x01",
            "It is a place of feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Triple track of East Crossbell Highway\x01",
            "When passing to the Tangram main gate,\x01",
            "I think that you can see a signboard … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "After that,\x01",
            "Before going down a little south\x01",
            "There exists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Members of Lloyd, too,\x01",
            "Give me your face if you have time.\x02",
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
            "Then Lloyd members,\x01",
            "The battle for bombs is for us\x01",
            "I'm going to do something … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Even a small number\x01",
            "It is better to have more.\x01",
            "Lloyd members also asked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYes, I also love you\x01",
            "It is impossible to fish\x01",
            "Because I am sorry.\x02\x03",
            "#00000FAs much as possible, I will try hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Hehe, members of Lloyd.\x01",
            "I will not lose, I ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "Well then with us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "Sure, good luck!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, the branch chiefs too!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 43)
    Sleep(200)
    BeginChrThread(0x19, 3, 0, 43)
    Sleep(200)
    BeginChrThread(0x1A, 3, 0, 43)
    Sleep(1000)

    def lambda_BF70():

        label("loc_BF70")

        TurnDirection(0x101, 0x1A, 500)
        Yield()
        Jump("loc_BF70")

    QueueWorkItem2(0x101, 2, lambda_BF70)

    def lambda_BF82():

        label("loc_BF82")

        TurnDirection(0x102, 0x1A, 500)
        Yield()
        Jump("loc_BF82")

    QueueWorkItem2(0x102, 2, lambda_BF82)

    def lambda_BF94():

        label("loc_BF94")

        TurnDirection(0x109, 0x1A, 500)
        Yield()
        Jump("loc_BF94")

    QueueWorkItem2(0x109, 2, lambda_BF94)

    def lambda_BFA6():

        label("loc_BFA6")

        TurnDirection(0x105, 0x1A, 500)
        Yield()
        Jump("loc_BFA6")

    QueueWorkItem2(0x105, 2, lambda_BFA6)

    def lambda_BFB8():

        label("loc_BFB8")

        TurnDirection(0x104, 0x1A, 500)
        Yield()
        Jump("loc_BFB8")

    QueueWorkItem2(0x104, 2, lambda_BFB8)
    WaitChrThread(0x1B, 3)

    ChrTalk(
        0x102,
        (
            "#00109F(Well, Lloyd said\x01",
            "What cares you. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F(Fishing, or ……\x01",
            "I do not know well, but hot people\x01",
            "There are lots of things. )\x02",
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

    # Function_42_B6EC end

    def Function_43_C0FB(): pass

    label("Function_43_C0FB")

    OP_93(0xFE, 0x87, 0x1F4)
    OP_95(0xFE, 110, -300, 1300, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x0)
    OP_95(0xFE, 14590, -300, 1300, 2000, 0x0)
    Return()

    # Function_43_C0FB end

    def Function_44_C132(): pass

    label("Function_44_C132")

    EventBegin(0x1)
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "You do not have to show me this.\x01",
            "Go to other places.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 1910, -3000, -35980, 0)
    EventEnd(0x4)
    Return()

    # Function_44_C132 end

    def Function_45_C18D(): pass

    label("Function_45_C18D")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C208")

    ChrTalk(
        0x1A2,
        (
            "Hey, this is\x01",
            "Is not it out of town?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000FOh, that's true.\x01",
            "Let's return to the city.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_C244")

    label("loc_C208")


    ChrTalk(
        0x101,
        (
            "#00000FI can not let go out on the highway.\x01",
            "Let's return to the city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C244")

    SetChrPos(0x0, 29390, -300, 500, 270)
    EventEnd(0x4)
    Return()

    # Function_45_C18D end

    def Function_46_C258(): pass

    label("Function_46_C258")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C308")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C2CC")

    ChrTalk(
        0x101,
        (
            "#00000FThe destination is the East Crossbell Highway.\x02\x03",
            "I do not have any particular business,\x01",
            "Let's stop getting out.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    Jump("loc_C308")

    label("loc_C2CC")


    ChrTalk(
        0x101,
        (
            "#00000FThere is no business in this direction.\x01",
            "Let's stop getting out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C3CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C384")

    ChrTalk(
        0x101,
        (
            "#00001FThe destination is the East Crossbell Highway.\x02\x03",
            "Right now,\x01",
            "Let's concentrate on the accident-related investigation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    Jump("loc_C3CA")

    label("loc_C384")


    ChrTalk(
        0x101,
        (
            "#00001FThere is no business in this direction.\x01",
            "Let 's concentrate on the accident - related investigation now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C3CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C42B")

    ChrTalk(
        0x101,
        (
            "#00001FAnyway now\x01",
            "I have to chase Randy -\x01",
            "It is not the case that it is on a side street.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C42B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C47B")

    ChrTalk(
        0x101,
        (
            "#00001FIt is not the case that I am out of town right now.\x01",
            "Let's turn back to life.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C47B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C4FA")

    ChrTalk(
        0x101,
        (
            "#00001FCome this far to the city\x01",
            "I can not leave.\x02\x03",
            "Operation into the Orkis Tower -\x01",
            "You must make it successful at all costs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C4FA")

    SetChrPos(0x0, 29390, -300, 500, 270)
    EventEnd(0x4)
    Return()

    # Function_46_C258 end

    def Function_47_C50E(): pass

    label("Function_47_C50E")

    EventBegin(0x1)

    ChrTalk(
        0x105,
        (
            "#10303F…… Lloyd's bad, but\x01",
            "Only a little if going back to old city\x01",
            "Will you give me some time?\x02\x03",
            "#10308FI need only a little.\x01",
            "It is not easy to get back to running water\x01",
            "A little bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FOh … I understand.\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 1610, -3000, -35150, 0)
    EventEnd(0x4)
    Return()

    # Function_47_C50E end

    SaveToFile()

Try(main)
