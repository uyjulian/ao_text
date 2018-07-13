from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c040d.bin",                # FileName
        "c040d",                    # MapName
        "c040d",                    # Location
        0x0022,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 4, 0, 5],
    )

    BuildStringList((
        "c040d",                  # 0
        "Polise",                 # 1
        "Tap",                    # 2
        "Sophille",               # 3
        "Tello",                  # 4
        "Barker Pim",             # 5
        "Lamanda",                # 6
        "Bunny Girl",             # 7
        "車",                     # 8
        "State Guard Soldier",    # 9
        "State Guard Soldier",    # 10
        "市民１",                 # 11
        "市民２",                 # 12
        "市民３",                 # 13
        "市民４",                 # 14
        "市民５",                 # 15
        "市民６",                 # 16
        "市民７",                 # 17
        "市民８",                 # 18
        "bc0400",                 # 19
        "Central Square",         # 20
        "West Street",            # 21
        "Governmental District",  # 22
        "Residential Street",     # 23
        "Entertainment District", # 24
        "East Street",            # 25
        "Downtown",               # 26
        "Waterfront Area",        # 27
        "IBC",                    # 28
        "Station Street",         # 29
        "Back Street",            # 30
        "St. Ursula Byroad",      # 31
        "East Crossbell Highway", # 32
        "West Crossbell HIghway", # 33
        "Mainz Mountain Road",    # 34
        "Orchis Tower",           # 35
    ))

    ATBonus("ATBonus_5AC", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_2C56", 8,   8,   8,   8,   11,  11,  11)

    MonsterBattlePostion("MonsterBattlePostion_5FC", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_600", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_604", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_608", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_60C", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_610", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_614", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_618", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_65C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_660", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_664", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_668", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_66C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_670", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_674", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_678", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_5DC", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_5E0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_5E4", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_5E8", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_5EC", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5F0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5F4", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5F8", 2, 13, 180)

    # monster count: 3

    BattleInfo(
        "BattleInfo_67C", 0x0000, 99, 6, 60, 4, 1, 25, 0, "bc0400", "Sepith_2C56", 60, 25, 10, 5,
        (
            ("ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5FC", "MonsterBattlePostion_65C", "ed7450", "ed7453", "ATBonus_5AC"),
            ("ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5DC", "MonsterBattlePostion_65C", "ed7450", "ed7453", "ATBonus_5AC"),
            ("ms85100.dat", "ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5FC", "MonsterBattlePostion_65C", "ed7450", "ed7453", "ATBonus_5AC"),
            ("ms85100.dat", "ms85100.dat", "ms85100.dat", "ms85100.dat", 0, 0, 0, 0, "MonsterBattlePostion_5DC", "MonsterBattlePostion_65C", "ed7450", "ed7453", "ATBonus_5AC"),
        )
    )

    AddCharChip((
        "chr/ch34500.itc",                   # 00
        "chr/ch36300.itc",                   # 01
        "chr/ch24400.itc",                   # 02
        "chr/ch20400.itc",                   # 03
        "chr/ch25900.itc",                   # 04
        "chr/ch21900.itc",                   # 05
        "chr/ch27100.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "monster/ch85150.itc",               # 10
        "monster/ch85151.itc",               # 11
    ))

    DeclNpc(379,     1769,    28049,   315,  261,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(1830,    1769,    27899,   315,  261,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(4294956546, 1759,    24469,   175,  261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(15439,   0,       10340,   45,   257,  0x0, 0,   3,   0,   0,   3,   0,   11,  255,  0)
    DeclNpc(4360,    0,       4294956336, 310,  257,  0x0, 0,   4,   0,   0,   1,   0,   7,   255,  0)
    DeclNpc(4294917296, 9,       12069,   220,  257,  0x0, 0,   5,   0,   0,   2,   0,   10,  255,  0)
    DeclNpc(4294945247, 0,       12489,   175,  261,  0x0, 0,   6,   0,   0,   0,   0,   12,  255,  0)
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

    DeclMonster(4294966976, 17690,   1990,    0x101013B,    "BattleInfo_67C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294949206, 8970,    0,       0x10100DC,    "BattleInfo_67C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(9570,    3690,    0,       0x10100E1,    "BattleInfo_67C", 0,   16,  0xFFFF, 0,  1)

    PlaceName(90.5999984741211, 0.0, -111.88999938964844, 0x0000, 0x0000, "Central Square")
    PlaceName(-19.209999084472656, 0.0, -104.37999725341797, 0x0000, 0x0000, "West Street")
    PlaceName(135.69000244140625, 0.0, 36.7400016784668, 0x0000, 0x0000, "Governmental District")
    PlaceName(-121.08000183105469, 0.0, 20.040000915527344, 0x0000, 0x0000, "Residential Street")
    PlaceName(0.8399999737739563, 0.0, 6.679999828338623, 0x0000, 0x0000, "Entertainment District")
    PlaceName(226.2899932861328, 0.0, -150.3000030517578, 0x0000, 0x0000, "East Street")
    PlaceName(285.57000732421875, 0.0, -242.14999389648438, 0x0000, 0x0000, "Downtown")
    PlaceName(273.04998779296875, 0.0, -40.08000183105469, 0x0000, 0x0000, "Waterfront Area")
    PlaceName(229.6300048828125, 0.0, 116.9000015258789, 0x0000, 0x0000, "IBC")
    PlaceName(109.38999938964844, 0.0, -227.1199951171875, 0x0000, 0x0000, "Station Street")
    PlaceName(30.899999618530273, 0.0, -53.439998626708984, 0x0000, 0x0000, "Back Street")
    PlaceName(104.37999725341797, 0.0, -278.8900146484375, 0x0000, 0x0000, "St. Ursula Byroad")
    PlaceName(316.4700012207031, 0.0, -126.91999816894531, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-104.37999725341797, 0.0, -106.87999725341797, 0x0000, 0x0000, "West Crossbell HIghway")
    PlaceName(-94.36000061035156, 0.0, 60.119998931884766, 0x0000, 0x0000, "Mainz Mountain Road")
    PlaceName(124.0, 0.0, 255.0, 0x0000, 0x0000, "Orchis Tower")
    PlaceName(53.86000061035156, 0.0, -135.27000427246094, 0x0000, 0x0051, "")
    PlaceName(143.6199951171875, 0.0, -91.8499984741211, 0x0000, 0x0054, "")
    PlaceName(94.7699966430664, 0.0, -148.6300048828125, 0x0000, 0x0057, "")
    PlaceName(52.61000061035156, 0.0, -86.83999633789062, 0x0000, 0x0053, "")
    PlaceName(86.83999633789062, 0.0, -46.7599983215332, 0x0000, 0x0053, "")
    PlaceName(2.0899999141693115, 0.0, -95.19000244140625, 0x0000, 0x0053, "")
    PlaceName(-14.199999809265137, 0.0, -60.119998931884766, 0x0000, 0x0053, "")
    PlaceName(25.889999389648438, 0.0, -6.679999828338623, 0x0000, 0x0052, "")
    PlaceName(33.81999969482422, 0.0, -28.389999389648438, 0x0000, 0x0053, "")
    PlaceName(48.43000030517578, 0.0, -42.59000015258789, 0x0000, 0x0053, "")
    PlaceName(96.02999877929688, 0.0, 75.98999786376953, 0x0000, 0x0051, "")
    PlaceName(283.07000732421875, 0.0, -150.3000030517578, 0x0000, 0x0052, "")
    PlaceName(254.67999267578125, 0.0, -301.44000244140625, 0x0000, 0x0053, "")
    PlaceName(232.97000122070312, 0.0, -270.5400085449219, 0x0000, 0x0053, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 1

    ScpFunction((
        "Function_0_798",          # 00, 0
        "Function_1_848",          # 01, 1
        "Function_2_873",          # 02, 2
        "Function_3_A00",          # 03, 3
        "Function_4_B07",          # 04, 4
        "Function_5_DC0",          # 05, 5
        "Function_6_123A",         # 06, 6
        "Function_7_15B4",         # 07, 7
        "Function_8_1821",         # 08, 8
        "Function_9_1AAA",         # 09, 9
        "Function_10_1CA6",        # 0A, 10
        "Function_11_1F32",        # 0B, 11
        "Function_12_21F1",        # 0C, 12
        "Function_13_246A",        # 0D, 13
        "Function_14_29D5",        # 0E, 14
    ))


    def Function_0_798(): pass

    label("Function_0_798")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_7D0"),
        (1, "loc_7DC"),
        (2, "loc_7E8"),
        (3, "loc_7F4"),
        (4, "loc_800"),
        (5, "loc_80C"),
        (6, "loc_818"),
        (SWITCH_DEFAULT, "loc_824"),
    )


    label("loc_7D0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_830")

    label("loc_7DC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_830")

    label("loc_7E8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_830")

    label("loc_7F4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_830")

    label("loc_800")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_830")

    label("loc_80C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_830")

    label("loc_818")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_830")

    label("loc_824")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_830")

    label("loc_830")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_847")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_830")

    label("loc_847")

    Return()

    # Function_0_798 end

    def Function_1_848(): pass

    label("Function_1_848")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_872")
    OP_94(0xFE, 0xED8, 0xFFFFEC96, 0x1AE0, 0xFFFFDE22, 0x3E8)
    Sleep(300)
    Jump("Function_1_848")

    label("loc_872")

    Return()

    # Function_1_848 end

    def Function_2_873(): pass

    label("Function_2_873")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9FF")
    SetChrPos(0xFE, -50000, 10, 12070, 220)
    OP_95(0xFE, -18740, 10, 10280, 1500, 0x0)
    OP_95(0xFE, -2040, 1770, 9880, 1500, 0x0)
    OP_95(0xFE, 30970, 0, 12150, 1500, 0x0)
    Sleep(1500)
    SetChrPos(0xFE, 30210, 0, 8600, 270)
    OP_95(0xFE, 17210, 0, 8600, 1500, 0x0)
    OP_95(0xFE, 15010, 0, 6790, 1500, 0x0)
    OP_95(0xFE, 10210, 0, -960, 1500, 0x0)
    OP_95(0xFE, 8450, 0, -7690, 1500, 0x0)
    OP_95(0xFE, 10100, 0, -11960, 1500, 0x0)
    OP_95(0xFE, 28170, 0, -38880, 1500, 0x0)
    Sleep(1500)
    SetChrPos(0xFE, 28170, 0, -38880, 315)
    OP_95(0xFE, 9370, 0, -17000, 1500, 0x0)
    OP_95(0xFE, 4280, 0, -11560, 1500, 0x0)
    OP_95(0xFE, -4810, 0, -3900, 1500, 0x0)
    OP_95(0xFE, -13140, 0, 1410, 1500, 0x0)
    OP_95(0xFE, -21060, 0, 5360, 1500, 0x0)
    OP_95(0xFE, -26790, 0, 8090, 1500, 0x0)
    OP_95(0xFE, -50000, 10, 12070, 1500, 0x0)
    Sleep(1500)
    Jump("Function_2_873")

    label("loc_9FF")

    Return()

    # Function_2_873 end

    def Function_3_A00(): pass

    label("Function_3_A00")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B06")
    OP_95(0xFE, 8780, 0, 6460, 1000, 0x0)
    OP_95(0xFE, 2270, 0, 3060, 1000, 0x0)
    OP_95(0xFE, -5460, 0, 2360, 1000, 0x0)
    OP_95(0xFE, -14070, 0, 5650, 1000, 0x0)
    OP_95(0xFE, -19800, 0, 8020, 1000, 0x0)
    OP_95(0xFE, -26870, 0, 10100, 1000, 0x0)
    Sleep(1500)
    OP_95(0xFE, -19800, 0, 8020, 1000, 0x0)
    OP_95(0xFE, -14070, 0, 5650, 1000, 0x0)
    OP_95(0xFE, -5460, 0, 2360, 1000, 0x0)
    OP_95(0xFE, 2270, 0, 3060, 1000, 0x0)
    OP_95(0xFE, 8780, 0, 6460, 1000, 0x0)
    OP_95(0xFE, 11400, 0, 7650, 1000, 0x0)
    Sleep(1500)
    Jump("Function_3_A00")

    label("loc_B06")

    Return()

    # Function_3_A00 end

    def Function_4_B07(): pass

    label("Function_4_B07")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D42")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BE4")
    SetChrPos(0x0, 21040, 0, 11840, 270)
    SetChrPos(0x1, 21040, 0, 11840, 270)
    SetChrPos(0x2, 21040, 0, 11840, 270)
    SetChrPos(0x3, 21040, 0, 11840, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BB7")
    SetChrPos(0x4, 21040, 0, 11840, 270)
    SetChrPos(0x5, 21040, 0, 11840, 270)
    Jump("loc_BD6")

    label("loc_BB7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BD6")
    SetChrPos(0x4, 21040, 0, 11840, 270)

    label("loc_BD6")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D42")

    label("loc_BE4")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CA1")
    SetChrPos(0x0, -39280, 0, 12420, 90)
    SetChrPos(0x1, -39280, 0, 12420, 90)
    SetChrPos(0x2, -39280, 0, 12420, 90)
    SetChrPos(0x3, -39280, 0, 12420, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C74")
    SetChrPos(0x4, -39280, 0, 12420, 90)
    SetChrPos(0x5, -39280, 0, 12420, 90)
    Jump("loc_C93")

    label("loc_C74")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C93")
    SetChrPos(0x4, -39280, 0, 12420, 90)

    label("loc_C93")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D42")

    label("loc_CA1")

    SetChrPos(0x0, 13270, 0, -19100, 315)
    SetChrPos(0x1, 13270, 0, -19100, 315)
    SetChrPos(0x2, 13270, 0, -19100, 315)
    SetChrPos(0x3, 13270, 0, -19100, 315)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D1A")
    SetChrPos(0x4, 13270, 0, -19100, 315)
    SetChrPos(0x5, 13270, 0, -19100, 315)
    Jump("loc_D39")

    label("loc_D1A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D39")
    SetChrPos(0x4, 13270, 0, -19100, 315)

    label("loc_D39")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D42")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_D68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D63")
    SetChrFlags(0x8, 0x10)

    label("loc_D63")

    Jump("loc_DB0")

    label("loc_D68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_D99")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    Jump("loc_DB0")

    label("loc_D99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_DA7")
    Jump("loc_DB0")

    label("loc_DA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_DB0")

    label("loc_DB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_DBF")
    ClearScenarioFlags(0x22, 4)
    Event(0, 13)

    label("loc_DBF")

    Return()

    # Function_4_B07 end

    def Function_5_DC0(): pass

    label("Function_5_DC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DDC")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DF3")

    label("loc_DDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DF3")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E0C")
    OP_10(0x1, 0x0)
    OP_10(0x8, 0x1)
    Jump("loc_E12")

    label("loc_E0C")

    OP_10(0x1, 0x1)
    OP_10(0x8, 0x0)

    label("loc_E12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E2C")
    SetMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x4, 0x2)

    label("loc_E2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ECC")
    LoadEffect(0x9, "map/mpmoya.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0x78, 0x96, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xFF, 0xD, 0x7D, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)

    label("loc_ECC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_F1F")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x2C, 0x9D, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)

    label("loc_F1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F37")
    ClearMapFlags(0x2000)
    Jump("loc_F3E")

    label("loc_F37")

    SetMapFlags(0x2000)
    OP_E2(0x1)

    label("loc_F3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_F70")
    SetMapObjFrame(0xFF, "ka03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ka04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "koge", 0x0, 0x1)
    Jump("loc_FC6")

    label("loc_F70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_FA2")
    SetMapObjFrame(0xFF, "ka03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ka04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "koge", 0x0, 0x1)
    Jump("loc_FC6")

    label("loc_FA2")

    SetMapObjFrame(0xFF, "ka03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ka04", 0x0, 0x1)
    SetMapObjFrame(0xFF, "koge", 0x1, 0x1)

    label("loc_FC6")

    OP_52(0x1A, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_5_DC0 end

    def Function_6_123A(): pass

    label("Function_6_123A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1263")
    Call(0, 14)
    Return()

    label("loc_1263")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1270")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15B0")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",      # 0
            "Shop\x01",      # 1
            "Quit\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12C0")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_12C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12E0")
    OP_AF(0x7E)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_15AB")

    label("loc_12E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12F4")
    Jump("loc_15AB")

    label("loc_12F4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15AB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_13F1")

    ChrTalk(
        0xFE,
        (
            ""I've finally resumed business..."\x01",
            "That's what I was thinking, but somehow\x01",
            "it seems that something crazy happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Well, on this occasion maybe it would be\x01",
            "better to chill our heads with an ice cream.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15AB")

    label("loc_13F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_13FF")
    Jump("loc_15AB")

    label("loc_13FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1483")

    ChrTalk(
        0xA,
        "Really, what an amazing clamor...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Somehow I feel that the ice creams\x01",
            "will melt due to all the enthusiasm...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15AB")

    label("loc_1483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_15AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1547")

    ChrTalk(
        0xA,
        "Miss Ilya...I'm really worried.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "My only merit is to\x01",
            "sell ice creams, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I intend to continue my business here\x01",
            "while waiting for Miss Ilya's comeback.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_15AB")

    label("loc_1547")


    ChrTalk(
        0xA,
        "Ice creams, do you want an ice cream?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's pleasantly cool, refreshing\x01",
            "and very gooood...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15AB")

    Jump("loc_1270")

    label("loc_15B0")

    TalkEnd(0xFE)
    Return()

    # Function_6_123A end

    def Function_7_15B4(): pass

    label("Function_7_15B4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1707")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1680")

    ChrTalk(
        0xFE,
        (
            "A faintly shining tree...\x01",
            "Really, I wonder what's that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it's useless even if I think about it.\x01",
            "At any rate, I must earn a lot\x01",
            "doing my job while I still can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_1702")

    label("loc_1680")


    ChrTalk(
        0xFE,
        (
            "At any rate, I must earn a lot\x01",
            "doing my job while I still can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Wait, as expected I'd hardly\x01",
            "catch any customers too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1702")

    Jump("loc_181D")

    label("loc_1707")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1715")
    Jump("loc_181D")

    label("loc_1715")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1796")

    ChrTalk(
        0xFE,
        (
            "Dear me...somehow the\x01",
            "situation is going crazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In any case, I just wish for\x01",
            "troubles to leave me alone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_181D")

    label("loc_1796")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_181D")

    ChrTalk(
        0xFE,
        (
            "Heh heh heh, don't you want\x01",
            "to come drink at our store?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You'll be able to learn a lot\x01",
            "due to our "charity service".\x02",
        )
    )

    CloseMessageWindow()

    label("loc_181D")

    TalkEnd(0xFE)
    Return()

    # Function_7_15B4 end

    def Function_8_1821(): pass

    label("Function_8_1821")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_195B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18C2")

    ChrTalk(
        0xFE,
        (
            "Suuuuullyyyyyy!!\x01",
            "And everyone too, please do your beeest!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll wait in anticipation for\x01",
            "the Arc-en-ciel come-back!!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    SetScenarioFlags(0x0, 0)
    Jump("loc_1956")

    label("loc_18C2")


    ChrTalk(
        0xFE,
        (
            "Lady Ilya has promised she'll\x01",
            "come back on stage for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Until that day comes, we\x01",
            "have to cheer with all our\x01",
            "might for the Arc-en-ciel!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1956")

    Jump("loc_1AA6")

    label("loc_195B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1969")
    Jump("loc_1AA6")

    label("loc_1969")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1A06")

    ChrTalk(
        0xFE,
        (
            "Who hurt Lady Ilya must've\x01",
            "been the Empire, for sure...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why...I won't forgive the Empire...!\x01",
            "As if I'll ever change my mind!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AA6")

    label("loc_1A06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1AA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A60")

    ChrTalk(
        0xFE,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Lady Ilya...\x01",
            "Why did such a thing...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AA6")

    label("loc_1A60")


    ChrTalk(
        0xFE,
        (
            "I won't forgive...the culprits...\x01",
            "...I'll never forgive them...!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AA6")

    TalkEnd(0xFE)
    Return()

    # Function_8_1821 end

    def Function_9_1AAA(): pass

    label("Function_9_1AAA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1BE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B9F")

    ChrTalk(
        0xFE,
        (
            "While we were helping at the hospital\x01",
            "we were able to visit Lady Ilya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then, she told us to cheer\x01",
            "for the people who're \x01",
            "practicing right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it's Lady Ilya's wish,\x01",
            "I'll fire myself up and cheer!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1BDD")

    label("loc_1B9F")


    ChrTalk(
        0xFE,
        (
            "If it's Lady Ilya's wish,\x01",
            "I'll fire myself up and cheer!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BDD")

    Jump("loc_1CA2")

    label("loc_1BE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1BF0")
    Jump("loc_1CA2")

    label("loc_1BF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1C3D")

    ChrTalk(
        0xFE,
        (
            "Uwooooh...\x01",
            "Well said, President!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Now we'll be free!!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CA2")

    label("loc_1C3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1CA2")

    ChrTalk(
        0xFE,
        (
            "Lady Ilya...\x01",
            "They say she's still in a coma.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Shit, what a really\x01",
            "absurd thing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CA2")

    TalkEnd(0xFE)
    Return()

    # Function_9_1AAA end

    def Function_10_1CA6(): pass

    label("Function_10_1CA6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1D64")

    ChrTalk(
        0xFE,
        (
            "*sigh*, there's simply a feeling of unrest\x01",
            "in the situation surrounding Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if I should flee abroad in a way\x01",
            "or another now that I still can...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F2E")

    label("loc_1D64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1D72")
    Jump("loc_1F2E")

    label("loc_1D72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1E69")

    ChrTalk(
        0xFE,
        (
            "There were some kind of rumors, but\x01",
            "to think the two major powers would\x01",
            "do such cowardly things...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I completely agree with the President's claim.\x01",
            "If we don't stand up against them now,\x01",
            "the same tragedies will be repeated!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F2E")

    label("loc_1E69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1F2E")

    ChrTalk(
        0xFE,
        (
            "The Arc-en-ciel play...\x01",
            "The truth is that I was supposed\x01",
            "to see it today, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With what has happened,\x01",
            "there's nothing I can do about it...\x01",
            "I wonder if Lady Ilya is all right.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F2E")

    TalkEnd(0xFE)
    Return()

    # Function_10_1CA6 end

    def Function_11_1F32(): pass

    label("Function_11_1F32")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1FD7")

    ChrTalk(
        0xFE,
        (
            "*haah*, that's absurd...\x01",
            "What's with that gigantic tree\x01",
            "which ignores the laws of physics?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Somehow...\x01",
            "Today I'm not in the mood to party.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21ED")

    label("loc_1FD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1FE5")
    Jump("loc_21ED")

    label("loc_1FE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_208F")

    ChrTalk(
        0xFE,
        (
            "The "Independent State of Crossbell", eh...?\x01",
            "Hehe, it doesn't sound bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It means that from now on we'll be\x01",
            "the citizens of an independent state.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21ED")

    label("loc_208F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_21ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21B9")

    ChrTalk(
        0xFE,
        (
            "Lately things have finally calmed down,\x01",
            "but since there was that raid, somehow\x01",
            "it's like the entire city is in a gloom mood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, that's why I think that...\x01",
            "Because the situation is like this, I must revitalize\x01",
            "the economy by partying even more than usual.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_21ED")

    label("loc_21B9")


    ChrTalk(
        0xFE,
        "And so, for that reason, I'll party today too.\x02",
    )

    CloseMessageWindow()

    label("loc_21ED")

    TalkEnd(0xFE)
    Return()

    # Function_11_1F32 end

    def Function_12_21F1(): pass

    label("Function_12_21F1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_22F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2291")

    ChrTalk(
        0xFE,
        "Hello, how're you doooing☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The mist got cleared, so let's\x01",
            "resume business at once!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Everyone, come and have fuuun.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_22F2")

    label("loc_2291")


    ChrTalk(
        0xFE,
        (
            "The mist got cleared, so let's\x01",
            "resume business at once!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Everyone, come and have fuuun.\x02",
    )

    CloseMessageWindow()

    label("loc_22F2")

    Jump("loc_2466")

    label("loc_22F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2305")
    Jump("loc_2466")

    label("loc_2305")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_23FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_239D")

    ChrTalk(
        0xFE,
        "Hello, how're you doooing☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Casino House "Barca" is\x01",
            "in high spirits today too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Everyone, come and have fuuun.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_23F9")

    label("loc_239D")


    ChrTalk(
        0xFE,
        (
            "Casino House "Barca" is\x01",
            "in high spirits today too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Everyone, come and have fuuun.\x02",
    )

    CloseMessageWindow()

    label("loc_23F9")

    Jump("loc_2466")

    label("loc_23FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2466")

    ChrTalk(
        0xFE,
        "Hello, how're you doooing☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Won't you come to bring some cheerfulness to the casino?\x02",
    )

    CloseMessageWindow()

    label("loc_2466")

    TalkEnd(0xFE)
    Return()

    # Function_12_21F1 end

    def Function_13_246A(): pass

    label("Function_13_246A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch41400.itc", 0x1E)
    LoadChrToIndex("chr/ch41800.itc", 0x1F)
    LoadChrToIndex("chr/ch26800.itc", 0x20)
    LoadChrToIndex("chr/ch26900.itc", 0x21)
    LoadChrToIndex("chr/ch27100.itc", 0x22)
    LoadChrToIndex("chr/ch26700.itc", 0x23)
    LoadChrToIndex("chr/ch26600.itc", 0x24)
    SoundLoad(821)
    SoundLoad(835)
    ClearChrFlags(0xF, 0x80)
    OP_78(0x6, 0xF)
    OP_49()
    SetChrPos(0xF, -3000, 2000, 21000, 270)
    OP_D5(0xF, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x6, 0x1000)
    ClearMapObjFlags(0x6, 0x4)
    OP_74(0x6, 0x1E)
    OP_70(0x6, 0x2)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -4400, 1990, 18800, 180)
    SetChrChipByIndex(0x11, 0x1F)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 500, 1990, 18800, 180)
    SetChrChipByIndex(0x12, 0x0)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -4400, 1990, 14200, 0)
    SetChrChipByIndex(0x13, 0x1)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, -3600, 1990, 13000, 0)
    SetChrChipByIndex(0x14, 0x2)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -1700, 1990, 13000, 0)
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 0, 1990, 13600, 0)
    SetChrChipByIndex(0x16, 0x21)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, -5500, 1990, 14900, 45)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 1500, 1990, 14600, 315)
    SetChrChipByIndex(0x18, 0x23)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, -700, 1990, 14800, 0)
    SetChrChipByIndex(0x19, 0x24)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, -2700, 1990, 15200, 0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    OP_63(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x18, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x19, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(-2000, 3500, 17000, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(15500, 10000)
    Sound(821, 2, 60, 0)
    Sound(835, 2, 80, 0)
    FadeToBright(1500, 0)
    OP_0D()
    SetMessageWindowPos(-1, 90, -1, -1)
    SetChrName("President Dieter")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You all know well that this\x01",
            "land was the place of their\x01",
            "strive over it.\x02\x03",
            "But after all, it's in the past, right?\x01",
            "...No, that's not true at all.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_70(0x6, 0x3)
    Sleep(600)
    SetMessageWindowPos(-1, 90, -1, -1)
    SetChrName("President Dieter")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In recent years, the many a time mysterious\x01",
            "and cryptid "accidents" that happened...\x02\x03",
            "Those took many forms,\x01",
            "like explosions or the\x01",
            "fall of an airship...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    Fade(250)
    OP_70(0x6, 0x4)
    Sleep(500)
    SetMessageWindowPos(-1, 90, -1, -1)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    SetChrName("President Dieter")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4S──However!\x01",
            "We should've noticed in some respects that...!\x02\x03",
            "#4SThat those "accidents" of unknown origin\x01",
            "and that we only had to meekly accept...\x02\x03",
            "#5SWere the result of their "secret feud"!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x14, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    StopSound(851, 1500, 60)
    StopSound(835, 1500, 80)
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 5)
    NewScene("c1550", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_246A end

    def Function_14_29D5(): pass

    label("Function_14_29D5")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BDC")

    ChrTalk(
        0xA,
        "Do you want some ice creeeam?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "It's pleasantly refreshing and good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(Maybe...she could appear\x01",
            "in the pageant as\x01",
            "the "maid" entry...?\x02\x03",
            "Uhm, excuse us.\x01",
            "We would like to ask you...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You asked her to participate \x01",
            "in the charity event pageant.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            "A pageant?\x01",
            "Uhhm, I thank you for\x01",
            "inviting me, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm not a maid\x01",
            "at all, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "This outfit too, I'm only wearing it\x01",
            "because it's pretty and catches the attention.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FI-Is that so...?\x01",
            "Pardon us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x199, 0)
    Jump("loc_2C2A")

    label("loc_2BDC")


    ChrTalk(
        0xA,
        (
            "I thank you for\x01",
            "inviting me, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm not a maid\x01",
            "at all, you see.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C2A")

    TalkEnd(0xA)
    Return()

    # Function_14_29D5 end

    SaveToFile()

Try(main)
