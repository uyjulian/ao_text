from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c120d.bin",                # FileName
        "c120d",                    # MapName
        "c120d",                    # Location
        0x001A,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\x03',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 4, 0, 5],
    )

    BuildStringList((
        "c120d",                  # 0
        "Jona",                   # 1
        "Policeman",              # 2
        "CGF Member",             # 3
        "CGF Member",             # 4
        "Cunha",                  # 5
        "Hauser",                 # 6
        "Bishop",                 # 7
        "Old Man Quine",          # 8
        "Amisaah",                # 9
        "Policeman",              # 10
        "State Guard Soldier",    # 11
        "Armored Vehicle",        # 12
        "Nielsen",                # 13
        "Mariabell",              # 14
        "Guard Bills",            # 15
        "車",                     # 16
        "車",                     # 17
        "bc1200",                 # 18
        "Central Square",         # 19
        "West Street",            # 20
        "Governmental District",  # 21
        "Residential Street",     # 22
        "Entertainment District", # 23
        "East Street",            # 24
        "Downtown",               # 25
        "Waterfront Area",        # 26
        "IBC",                    # 27
        "Station Street",         # 28
        "Back Street",            # 29
        "St. Ursula Byroad",      # 30
        "East Crossbell Highway", # 31
        "West Crossbell HIghway", # 32
        "Mainz Mountain Road",    # 33
        "Orchis Tower",           # 34
    ))

    ATBonus("ATBonus_674", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_786B", 8,   8,   8,   8,   11,  11,  11)

    MonsterBattlePostion("MonsterBattlePostion_6C4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_6C8", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_6CC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_6D0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6D4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6D8", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_6DC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6E0", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_724", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_728", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_72C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_730", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_734", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_738", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_73C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_740", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_6A4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_6A8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_6AC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_6B0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_6B4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6B8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6BC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6C0", 2, 13, 180)

    # monster count: 3

    BattleInfo(
        "BattleInfo_744", 0x0000, 99, 6, 60, 4, 1, 25, 0, "bc1200", "Sepith_786B", 60, 25, 10, 5,
        (
            ("ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6C4", "MonsterBattlePostion_724", "ed7450", "ed7453", "ATBonus_674"),
            ("ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6A4", "MonsterBattlePostion_724", "ed7450", "ed7453", "ATBonus_674"),
            ("ms85100.dat", "ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6C4", "MonsterBattlePostion_724", "ed7450", "ed7453", "ATBonus_674"),
            ("ms85100.dat", "ms85100.dat", "ms85100.dat", "ms85100.dat", 0, 0, 0, 0, "MonsterBattlePostion_6A4", "MonsterBattlePostion_724", "ed7450", "ed7453", "ATBonus_674"),
        )
    )

    AddCharChip((
        "chr/ch06100.itc",                   # 00
        "chr/ch30000.itc",                   # 01
        "chr/ch31200.itc",                   # 02
        "chr/ch31300.itc",                   # 03
        "chr/ch22100.itc",                   # 04
        "chr/ch25200.itc",                   # 05
        "chr/ch26000.itc",                   # 06
        "chr/ch24000.itc",                   # 07
        "chr/ch21500.itc",                   # 08
        "chr/ch30000.itc",                   # 09
        "chr/ch41400.itc",                   # 0A
        "chr/ch45102.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "monster/ch85150.itc",               # 10
        "monster/ch85151.itc",               # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(75500,   4294964796, 20000,   270,  389,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(22079,   0,       15050,   180,  389,  0x0, 0,   1,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(3130,    2000,    25149,   180,  389,  0x0, 0,   2,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(5530,    2000,    25000,   180,  389,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(4294954097, 0,       11500,   90,   385,  0x0, 0,   4,   0,   0,   1,   0,   12,  255,  0)
    DeclNpc(4294956826, 0,       13340,   180,  385,  0x0, 0,   5,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(4294914826, 2000,    21149,   90,   385,  0x0, 0,   6,   0,   0,   2,   0,   14,  255,  0)
    DeclNpc(39669,   4294964796, 4294947917, 135,  385,  0x0, 0,   7,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(40919,   4294964796, 4294948307, 135,  385,  0x0, 0,   8,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(4294949497, 0,       13369,   180,  389,  0x0, 0,   9,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(4294948817, 0,       12000,   180,  389,  0x0, 0,   10,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(4294946057, 0,       14350,   90,   196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(7820,    4294966896, 3200,    180,  389,  0x0, 0,   11,  0,   255, 255, 0,   19,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(3140,    4294966096, 4294966596, 0x10100E1,    "BattleInfo_744", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(38750,   1370,    4294964796, 0x10100E1,    "BattleInfo_744", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294950536, 9670,    4294967286, 0x10100E1,    "BattleInfo_744", 0,   16,  0xFFFF, 0,  1)

    DeclActor(16750,   4294966296, 4294951556, 1200,    16750,   0,       4294951556, 0x007C, 0,  6,  0x0000)
    DeclActor(82470,   4294964796, 15010,   1200,    79890,   4294963796, 8810,    0x007C, 0,  20, 0x0000)
    DeclActor(20620,   10,      15670,   2000,    20620,   1500,    15670,   0x007C, 0,  35, 0x0000)
    DeclActor(4550,    2000,    25990,   2000,    4550,    3000,    25990,   0x007C, 0,  36, 0x0000)
    DeclActor(77220,   4294964796, 20290,   2000,    77220,   4294966296, 20290,   0x007C, 0,  21, 0x0000)

    PlaceName(-123.13999938964844, 0.0, -85.1500015258789, 0x0000, 0x0000, "Central Square")
    PlaceName(-209.27000427246094, 0.0, -79.26000213623047, 0x0000, 0x0000, "West Street")
    PlaceName(-87.7699966430664, 0.0, 31.440000534057617, 0x0000, 0x0000, "Governmental District")
    PlaceName(-289.17999267578125, 0.0, 18.34000015258789, 0x0000, 0x0000, "Residential Street")
    PlaceName(-193.5500030517578, 0.0, 7.860000133514404, 0x0000, 0x0000, "Entertainment District")
    PlaceName(-16.700000762939453, 0.0, -115.27999877929688, 0x0000, 0x0000, "East Street")
    PlaceName(29.799999237060547, 0.0, -187.3300018310547, 0x0000, 0x0000, "Downtown")
    PlaceName(19.979999542236328, 0.0, -28.81999969482422, 0x0000, 0x0000, "Waterfront Area")
    PlaceName(-14.079999923706055, 0.0, 94.31999969482422, 0x0000, 0x0000, "IBC")
    PlaceName(-108.4000015258789, 0.0, -175.5399932861328, 0x0000, 0x0000, "Station Street")
    PlaceName(-169.97000122070312, 0.0, -39.29999923706055, 0x0000, 0x0000, "Back Street")
    PlaceName(-112.33000183105469, 0.0, -216.14999389648438, 0x0000, 0x0000, "St. Ursula Byroad")
    PlaceName(54.040000915527344, 0.0, -96.94000244140625, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-276.0799865722656, 0.0, -81.22000122070312, 0x0000, 0x0000, "West Crossbell HIghway")
    PlaceName(-268.2200012207031, 0.0, 49.779998779296875, 0x0000, 0x0000, "Mainz Mountain Road")
    PlaceName(-96.5, 0.0, 203.75, 0x0000, 0x0000, "Orchis Tower")
    PlaceName(-151.9600067138672, 0.0, -103.48999786376953, 0x0000, 0x0051, "")
    PlaceName(-81.55000305175781, 0.0, -69.43000030517578, 0x0000, 0x0054, "")
    PlaceName(-119.87000274658203, 0.0, -113.97000122070312, 0x0000, 0x0057, "")
    PlaceName(-152.94000244140625, 0.0, -65.5, 0x0000, 0x0053, "")
    PlaceName(-126.08999633789062, 0.0, -34.060001373291016, 0x0000, 0x0053, "")
    PlaceName(-192.57000732421875, 0.0, -72.05000305175781, 0x0000, 0x0053, "")
    PlaceName(-205.33999633789062, 0.0, -44.540000915527344, 0x0000, 0x0053, "")
    PlaceName(-173.89999389648438, 0.0, -2.619999885559082, 0x0000, 0x0052, "")
    PlaceName(-167.67999267578125, 0.0, -19.649999618530273, 0x0000, 0x0053, "")
    PlaceName(-156.22000122070312, 0.0, -30.790000915527344, 0x0000, 0x0053, "")
    PlaceName(-118.87999725341797, 0.0, 62.22999954223633, 0x0000, 0x0051, "")
    PlaceName(27.84000015258789, 0.0, -115.27999877929688, 0x0000, 0x0052, "")
    PlaceName(5.570000171661377, 0.0, -233.83999633789062, 0x0000, 0x0053, "")
    PlaceName(-11.460000038146973, 0.0, -209.60000610351562, 0x0000, 0x0053, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 1

    ScpFunction((
        "Function_0_8B8",          # 00, 0
        "Function_1_968",          # 01, 1
        "Function_2_A19",          # 02, 2
        "Function_3_B00",          # 03, 3
        "Function_4_B28",          # 04, 4
        "Function_5_EC7",          # 05, 5
        "Function_6_1512",         # 06, 6
        "Function_7_1663",         # 07, 7
        "Function_8_1676",         # 08, 8
        "Function_9_168C",         # 09, 9
        "Function_10_1816",        # 0A, 10
        "Function_11_18D1",        # 0B, 11
        "Function_12_199A",        # 0C, 12
        "Function_13_1E53",        # 0D, 13
        "Function_14_2287",        # 0E, 14
        "Function_15_25D3",        # 0F, 15
        "Function_16_2888",        # 10, 16
        "Function_17_2B22",        # 11, 17
        "Function_18_2C6D",        # 12, 18
        "Function_19_2D35",        # 13, 19
        "Function_20_2E53",        # 14, 20
        "Function_21_2F1A",        # 15, 21
        "Function_22_30A4",        # 16, 22
        "Function_23_4612",        # 17, 23
        "Function_24_48AD",        # 18, 24
        "Function_25_4938",        # 19, 25
        "Function_26_4980",        # 1A, 26
        "Function_27_606B",        # 1B, 27
        "Function_28_60A8",        # 1C, 28
        "Function_29_60FD",        # 1D, 29
        "Function_30_6152",        # 1E, 30
        "Function_31_61A7",        # 1F, 31
        "Function_32_61FC",        # 20, 32
        "Function_33_6251",        # 21, 33
        "Function_34_62A6",        # 22, 34
        "Function_35_7751",        # 23, 35
        "Function_36_77C3",        # 24, 36
    ))


    def Function_0_8B8(): pass

    label("Function_0_8B8")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_8F0"),
        (1, "loc_8FC"),
        (2, "loc_908"),
        (3, "loc_914"),
        (4, "loc_920"),
        (5, "loc_92C"),
        (6, "loc_938"),
        (SWITCH_DEFAULT, "loc_944"),
    )


    label("loc_8F0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_950")

    label("loc_8FC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_950")

    label("loc_908")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_950")

    label("loc_914")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_950")

    label("loc_920")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_950")

    label("loc_92C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_950")

    label("loc_938")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_950")

    label("loc_944")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_950")

    label("loc_950")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_967")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_950")

    label("loc_967")

    Return()

    # Function_0_8B8 end

    def Function_1_968(): pass

    label("Function_1_968")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A18")
    OP_95(0xFE, 14600, 0, 11500, 1000, 0x0)
    OP_95(0xFE, 20200, 0, 8200, 1000, 0x0)
    OP_95(0xFE, 20200, 0, -6200, 1000, 0x0)
    OP_95(0xFE, 14000, 0, -11700, 1000, 0x0)
    OP_95(0xFE, -14000, 0, -11700, 1000, 0x0)
    OP_95(0xFE, -20000, 0, -6400, 1000, 0x0)
    OP_95(0xFE, -20000, 0, 6000, 1000, 0x0)
    OP_95(0xFE, -13200, 0, 11500, 1000, 0x0)
    Jump("Function_1_968")

    label("loc_A18")

    Return()

    # Function_1_968 end

    def Function_2_A19(): pass

    label("Function_2_A19")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AFF")
    Sleep(3000)
    OP_95(0xFE, -13000, 2000, 21150, 5000, 0x0)
    OP_95(0xFE, -13000, 2000, 24150, 5000, 0x0)
    OP_A0(0xFE, 5000, 0x0, 0xFB)
    OP_A0(0xFE, 4000, 0x0, 0xFB)
    OP_A0(0xFE, 5000, 0x0, 0xFB)
    OP_A0(0xFE, 4000, 0x0, 0xFB)
    OP_95(0xFE, -13000, 0, 14240, 5000, 0x0)
    OP_95(0xFE, -22130, 0, 5860, 5000, 0x0)
    OP_95(0xFE, -22020, 0, -46700, 5000, 0x0)
    Sleep(3000)
    OP_95(0xFE, -22130, 0, 5860, 5000, 0x0)
    OP_95(0xFE, -15540, 0, 14240, 5000, 0x0)
    OP_95(0xFE, -15540, 2000, 21150, 5000, 0x0)
    OP_95(0xFE, -52470, 2000, 21150, 5000, 0x0)
    Jump("Function_2_A19")

    label("loc_AFF")

    Return()

    # Function_2_A19 end

    def Function_3_B00(): pass

    label("Function_3_B00")

    SetMapObjFlags(0xB, 0x2000000)
    SetMapObjFlags(0xC, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_B27")
    SetMapObjFlags(0x4, 0x2000000)
    ClearMapObjFlags(0xB, 0x2000000)
    ClearMapObjFlags(0xC, 0x2000000)

    label("loc_B27")

    Return()

    # Function_3_B00 end

    def Function_4_B28(): pass

    label("Function_4_B28")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D63")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BEA")
    SetChrPos(0x0, 4870, 3350, 31570, 180)
    SetChrPos(0x1, 4870, 3350, 31570, 180)
    SetChrPos(0x2, 4870, 3350, 31570, 180)
    SetChrPos(0x3, 4870, 3350, 31570, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BBD")
    SetChrPos(0x4, 4870, 3350, 31570, 180)
    SetChrPos(0x5, 4870, 3350, 31570, 180)
    Jump("loc_BDC")

    label("loc_BBD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BDC")
    SetChrPos(0x4, 4870, 3350, 31570, 180)

    label("loc_BDC")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D63")

    label("loc_BEA")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CC2")
    SetChrPos(0x0, -28110, 2000, 23520, 90)
    SetChrPos(0x1, -28110, 2000, 23520, 90)
    SetChrPos(0x2, -28110, 2000, 23520, 90)
    SetChrPos(0x3, -28110, 2000, 23520, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C95")
    SetChrPos(0x4, -28110, 2000, 23520, 90)
    SetChrPos(0x5, -28110, 2000, 23520, 90)
    Jump("loc_CB4")

    label("loc_C95")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CB4")
    SetChrPos(0x4, -28110, 2000, 23520, 90)

    label("loc_CB4")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D63")

    label("loc_CC2")

    SetChrPos(0x0, -19600, 0, -27950, 0)
    SetChrPos(0x1, -19600, 0, -27950, 0)
    SetChrPos(0x2, -19600, 0, -27950, 0)
    SetChrPos(0x3, -19600, 0, -27950, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D3B")
    SetChrPos(0x4, -19600, 0, -27950, 0)
    SetChrPos(0x5, -19600, 0, -27950, 0)
    Jump("loc_D5A")

    label("loc_D3B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D5A")
    SetChrPos(0x4, -19600, 0, -27950, 0)

    label("loc_D5A")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D63")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D7F")
    ClearChrFlags(0x8, 0x80)

    label("loc_D7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D9C")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)

    label("loc_D9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_DD2")
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x14, 0x4)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_E94")

    label("loc_DD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_DE0")
    Jump("loc_E94")

    label("loc_DE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_E34")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xF, -16840, 0, -5150, 180)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0x10, -16810, 0, -6100, 0)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_E94")

    label("loc_E34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_E94")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xF, 21190, 0, 1100, 0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0x10, 22390, 0, 1100, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -17800, 0, 13370, 180)

    label("loc_E94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_EA3")
    ClearScenarioFlags(0x22, 0)
    Event(0, 23)

    label("loc_EA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_EB2")
    ClearScenarioFlags(0x22, 1)
    Event(0, 8)

    label("loc_EB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EC6")
    SetScenarioFlags(0x0, 6)
    Event(0, 34)

    label("loc_EC6")

    Return()

    # Function_4_B28 end

    def Function_5_EC7(): pass

    label("Function_5_EC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_EDC")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 6)

    label("loc_EDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EF5")
    OP_10(0x1, 0x0)
    OP_10(0x8, 0x1)
    Jump("loc_EFB")

    label("loc_EF5")

    OP_10(0x1, 0x1)
    OP_10(0x8, 0x0)

    label("loc_EFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F8F")
    LoadEffect(0x9, "map/mpmoya.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0x78, 0x96, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xFF, 0xD, 0x190, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)

    label("loc_F8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_FD6")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x2D, 0x1AE, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)

    label("loc_FD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FEE")
    ClearMapFlags(0x2000)
    Jump("loc_FF5")

    label("loc_FEE")

    SetMapFlags(0x2000)
    OP_E2(0x1)

    label("loc_FF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_106B")
    SetMapObjFrame(0xFF, "koge2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "koge", 0x0, 0x1)
    SetMapObjFrame(0xFF, "syugeki01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "body03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "keepout", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sakutoka", 0x1, 0x1)
    SetMapObjFrame(0xFF, "atokabuse", 0x1, 0x1)
    Jump("loc_1149")

    label("loc_106B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_10E1")
    SetMapObjFrame(0xFF, "koge2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "koge", 0x0, 0x1)
    SetMapObjFrame(0xFF, "syugeki01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "body03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "keepout", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sakutoka", 0x1, 0x1)
    SetMapObjFrame(0xFF, "atokabuse", 0x1, 0x1)
    Jump("loc_1149")

    label("loc_10E1")

    SetMapObjFrame(0xFF, "koge2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "koge", 0x1, 0x1)
    SetMapObjFrame(0xFF, "syugeki01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "body03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "keepout", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sakutoka", 0x0, 0x1)
    SetMapObjFrame(0xFF, "atokabuse", 0x0, 0x1)

    label("loc_1149")

    OP_52(0x19, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0x19, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, 79890, -3500, 8810, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1419")
    OP_70(0x7, 0x0)
    Jump("loc_141D")

    label("loc_1419")

    OP_70(0x7, 0x1E)

    label("loc_141D")

    SetMapObjFlags(0x4, 0x4)
    OP_66(0x4, 0x1)
    ClearMapObjFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1440")
    OP_70(0x8, 0x0)
    Jump("loc_145A")

    label("loc_1440")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1456")
    OP_70(0x8, 0x28)
    OP_65(0x4, 0x1)
    Jump("loc_145A")

    label("loc_1456")

    OP_66(0x4, 0x1)

    label("loc_145A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14AE")
    ClearChrFlags(0x13, 0x80)
    OP_78(0xA, 0x13)
    SetChrPos(0x13, -20340, 0, 14300, 90)
    OP_D5(0x13, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x1000)
    SetMapObjFrame(0xA, "light", 0x0, 0x1)

    label("loc_14AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14C2")
    SetMapObjFlags(0x5, 0x4)

    label("loc_14C2")

    SoundDistance(0x7E, 0x13E3E, 0x0, 0xFFFF8972, 0x13880, 0xC350, 0x64, 0x0)
    OP_E3(0x13DE4, 0x0, 0x71E8)
    OP_E3(0x13C54, 0x0, 0xD1B0)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1511")
    OP_66(0x2, 0x1)
    OP_66(0x3, 0x1)

    label("loc_1511")

    Return()

    # Function_5_EC7 end

    def Function_6_1512(): pass

    label("Function_6_1512")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_160E")
    Sound(14, 0, 100, 0)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1D7, 1)"), scpexpr(EXPR_END)), "loc_1597")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_1609")

    label("loc_1597")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D7),
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

    label("loc_1609")

    Jump("loc_1657")

    label("loc_160E")

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

    label("loc_1657")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1512 end

    def Function_7_1663(): pass

    label("Function_7_1663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1675")
    Call(0, 26)
    Return()

    label("loc_1675")

    Return()

    # Function_7_1663 end

    def Function_8_1676(): pass

    label("Function_8_1676")

    EventBegin(0x0)
    SetChrPos(0x0, 75710, -2500, 20230, 270)
    EventEnd(0x5)
    Return()

    # Function_8_1676 end

    def Function_9_168C(): pass

    label("Function_9_168C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_178E")

    ChrTalk(
        0xFE,
        (
            "Those Heiyue guys are\x01",
            "nowhere to be seen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not a clue was found in\x01",
            "that collapsed building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They could be hiding\x01",
            "somewhere in Crossbell State\x01",
            "or fleeing back to Calvard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Where the hell could\x01",
            "they possibly have gone?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1812")

    label("loc_178E")


    ChrTalk(
        0xFE,
        (
            "Heiyue could be hiding\x01",
            "somewhere in Crossbell or\x01",
            "fleeing back to Calvard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Where the hell could\x01",
            "they possibly have gone?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1812")

    TalkEnd(0xFE)
    Return()

    # Function_9_168C end

    def Function_10_1816(): pass

    label("Function_10_1816")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1828")
    Call(0, 22)
    Jump("loc_18D0")

    label("loc_1828")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The collapsed IBC building\x01",
            "is just like a pile of\x01",
            "bricks and debris now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It'll be tough to rebuild\x01",
            "from this point, since so\x01",
            "much has been destroyed...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_18D0")

    Return()

    # Function_10_1816 end

    def Function_11_18D1(): pass

    label("Function_11_18D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18E3")
    Call(0, 22)
    Jump("loc_1999")

    label("loc_18E3")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "It seems that the Lady\x01",
            "of IBC's inspection\x01",
            "didn't bear much fruit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The fact that the bank's financial\x01",
            "system could be transferred to\x01",
            "Orchis Tower is a silver lining.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_1999")

    Return()

    # Function_11_18D1 end

    def Function_12_199A(): pass

    label("Function_12_199A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1A6E")

    ChrTalk(
        0xFE,
        (
            "I thought, at last, I could have laid\x01",
            "eyes on the sunny skies once again\x01",
            "but... What in the world is that tree?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It doesn't seem like a\x01",
            "weapon. Is it the work of\x01",
            "our new President, too?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E4F")

    label("loc_1A6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1A7C")
    Jump("loc_1E4F")

    label("loc_1A7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1C45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BB3")

    ChrTalk(
        0xFE,
        (
            "I was surprised by this sudden development,\x01",
            "but... If we don't make a show of strength,\x01",
            "won't the major powers make fun of us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why I strongly\x01",
            "support President\x01",
            "Dieter!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Secretary Arios is there... The\x01",
            "major powers won't be able to\x01",
            "do whatever they want any more!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C40")

    label("loc_1BB3")


    ChrTalk(
        0xFE,
        (
            "Of course I'm anxious.\x01",
            "But, I strongly support\x01",
            "President Dieter!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The major powers won't\x01",
            "be able to do whatever\x01",
            "they want any more!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C40")

    Jump("loc_1E4F")

    label("loc_1C45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1E4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D97")

    ChrTalk(
        0xFE,
        (
            "Near the park, a company branch had been\x01",
            "completely destroyed... Rumors say those\x01",
            "who did it were hired by the government.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of that, I wonder if\x01",
            "the attack was by a jaeger\x01",
            "group employed by the Empire...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That doesn't matter, but...\x01",
            "Anyway, I hope nothing\x01",
            "unnecessary happens to Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E4F")

    label("loc_1D97")


    ChrTalk(
        0xFE,
        (
            "It's become like this because\x01",
            "Crossbell has always been a\x01",
            "subordinate state... right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why it's necessary to\x01",
            "show the surrounding countries\x01",
            "our will to be independent.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E4F")

    TalkEnd(0xFE)
    Return()

    # Function_12_199A end

    def Function_13_1E53(): pass

    label("Function_13_1E53")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E60")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2283")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",        # 0
            "Shop\x01",        # 1
            "Cancel\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EB2")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1EB2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ED2")
    OP_AF(0x7B)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_227E")

    label("loc_1ED2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EE6")
    Jump("loc_227E")

    label("loc_1EE6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_227E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_20D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2025")

    ChrTalk(
        0xFE,
        (
            "In life, there exist many trials\x01",
            "to overcome... And there's no\x01",
            "trial that can't be overcome!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What are those two powerful\x01",
            "countries up to and what is\x01",
            "that mysterious tree!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...No matter what happens\x01",
            "to me or the world, I will\x01",
            "never stop making noodles!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_20CE")

    label("loc_2025")


    ChrTalk(
        0xFE,
        (
            "What are those two powerful\x01",
            "countries up to and what is\x01",
            "that mysterious tree!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...No matter what happens\x01",
            "to me or the world, I will\x01",
            "never stop making noodles!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20CE")

    Jump("loc_227E")

    label("loc_20D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_20E1")
    Jump("loc_227E")

    label("loc_20E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_217D")

    ChrTalk(
        0xFE,
        (
            "Hmm, so it's finally\x01",
            "come to this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm already prepared for whatever\x01",
            "happens. Now that it's come to\x01",
            "this, we can only push ahead!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_227E")

    label("loc_217D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_227E")

    ChrTalk(
        0xFE,
        (
            "Over many years, my cart and I have experienced many\x01",
            "joys and sorrows, so it's quite a shock for it to be\x01",
            "destroyed. It can't be helped if I can't stay positive!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With this newly purchased\x01",
            "cart, I plan to do my best\x01",
            "to make a fresh start!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_227E")

    Jump("loc_1E60")

    label("loc_2283")

    TalkEnd(0xFE)
    Return()

    # Function_13_1E53 end

    def Function_14_2287(): pass

    label("Function_14_2287")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2362")

    ChrTalk(
        0xFE,
        (
            "Sigh, I've been so busy as of late... Due\x01",
            "to the influence of martial law, delivery\x01",
            "work hasn't been this busy in a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Heheh, but this is how a\x01",
            "deliveryman should be. I\x01",
            "feel so alive!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25CF")

    label("loc_2362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2370")
    Jump("loc_25CF")

    label("loc_2370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_251F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_247E")

    ChrTalk(
        0xFE,
        (
            "Because the trains were halted\x01",
            "this morning, I have\x01",
            "considerably fewer deliveries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Or rather, if things continue\x01",
            "like this, I wonder what's going\x01",
            "to happen to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's a lot more\x01",
            "important than some job,\x01",
            "isn't it...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_251A")

    label("loc_247E")


    ChrTalk(
        0xFE,
        (
            "Really. If things continue at\x01",
            "this rate, I don't know what's\x01",
            "going to happen to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's a lot more\x01",
            "important than some job,\x01",
            "isn't it...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_251A")

    Jump("loc_25CF")

    label("loc_251F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_25CF")

    ChrTalk(
        0xFE,
        (
            "It's already been a week since the\x01",
            "attack, huh... I guess things are\x01",
            "finally settling down around here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyhow, I hope nothing\x01",
            "like that ever happens\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25CF")

    TalkEnd(0xFE)
    Return()

    # Function_14_2287 end

    def Function_15_25D3(): pass

    label("Function_15_25D3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_268B")

    ChrTalk(
        0xFE,
        (
            "I don't understand anything,\x01",
            "be it the President's\x01",
            "actions or that huge tree.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well whatever happens in\x01",
            "the future, I just need to\x01",
            "make sure Amisaah is safe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2884")

    label("loc_268B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2699")
    Jump("loc_2884")

    label("loc_2699")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_27E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2781")

    ChrTalk(
        0xFE,
        (
            "What a foolish address...\x01",
            "The world may be deceived,\x01",
            "but I shall not be!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Independent nation this, State Guard that!\x01",
            "Does he really believe we can hold on\x01",
            "against the threat of the major powers!?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_27DE")

    label("loc_2781")


    ChrTalk(
        0xFE,
        (
            "Goddess... Someone like\x01",
            "me matters not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But please, save my\x01",
            "granddaughter Amisaah!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27DE")

    Jump("loc_2884")

    label("loc_27E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2884")

    ChrTalk(
        0xFE,
        (
            "Back then, if Amisaah and\x01",
            "I had been just a little\x01",
            "too late in escaping...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I can't help but feel\x01",
            "afraid when I think\x01",
            "about that, even now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2884")

    TalkEnd(0xFE)
    Return()

    # Function_15_25D3 end

    def Function_16_2888(): pass

    label("Function_16_2888")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2A40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2998")

    ChrTalk(
        0xFE,
        (
            "My grandpa was saying\x01",
            "that any number of things\x01",
            "might happen from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm scared of our street\x01",
            "being under attack like\x01",
            "last time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But still, I feel like I can\x01",
            "make it through anything with\x01",
            "my favorite grandpa by my side.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2A3B")

    label("loc_2998")


    ChrTalk(
        0xFE,
        (
            "I'm scared of our street\x01",
            "being under attack like\x01",
            "last time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But still, I feel like I can\x01",
            "make it through anything with\x01",
            "my favorite grandpa by my side.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A3B")

    Jump("loc_2B1E")

    label("loc_2A40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2A4E")
    Jump("loc_2B1E")

    label("loc_2A4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2AC6")

    ChrTalk(
        0xFE,
        (
            "Like my grandfather\x01",
            "says, this has become a\x01",
            "real war, I guess...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hate that! And I'm\x01",
            "scared...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B1E")

    label("loc_2AC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2B1E")

    ChrTalk(
        0xFE,
        (
            "That eastern country\x01",
            "building that was there...\x01",
            "It's completely gone now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B1E")

    TalkEnd(0xFE)
    Return()

    # Function_16_2888 end

    def Function_17_2B22(): pass

    label("Function_17_2B22")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2C69")

    ChrTalk(
        0xFE,
        (
            "Though the Heiyue office was completely\x01",
            "destroyed, it looks like this place was\x01",
            "mostly repaired in just a week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And because of the upcoming\x01",
            "referendum, it seems not that\x01",
            "many citizens are depressed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think we'll feel the power of\x01",
            "those who make up their minds at\x01",
            "the last minute, for some reason.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C69")

    TalkEnd(0xFE)
    Return()

    # Function_17_2B22 end

    def Function_18_2C6D(): pass

    label("Function_18_2C6D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "That is to say, when wearing a new uniform,\x01",
            "your sleeves should feel tight while your\x01",
            "body and mind feel loose and relaxed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, from now on I\x01",
            "will do my best for\x01",
            "Crossbell State.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_2C6D end

    def Function_19_2D35(): pass

    label("Function_19_2D35")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2E4F")

    ChrTalk(
        0xFE,
        (
            "A big tree that gives\x01",
            "off a blue light, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is an event reminiscent of\x01",
            "the appearance of the Liber-\x01",
            "Ark that appeared in Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard the story that it turned out to\x01",
            "be an ancient city, but what in the world\x01",
            "is that large tree supposed to be...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E4F")

    TalkEnd(0xFE)
    Return()

    # Function_19_2D35 end

    def Function_20_2E53(): pass

    label("Function_20_2E53")

    EventBegin(0x1)
    Sound(2094, 255, 100, 0)

    ChrTalk(
        0x101,
        (
            "#0000FIt seems we can fish\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(75920, 0, 7460, 1500)
    MoveCamera(45, 24, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(11500, 1500)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Fish?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Fish\x01",        # 0
            "Cancel\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F15")
    OP_E2(0x2)
    MiniGame(0x6, 0x1, 0x14226, 0xFFFFF63C, 0x3AA2, 0xB4, 0x13812, 0xFFFFF254, 0x226A)

    label("loc_2F15")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_20_2E53 end

    def Function_21_2F1A(): pass

    label("Function_21_2F1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FA6")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　Lupinus River - No. 1 Lighthouse\x01",
            " \x01",
            "Authorized personnel only.\x01",
            "　　　　　～Crossbell City～\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Jump("loc_30A3")

    label("loc_2FA6")

    SetMapFlags(0x8000000)
    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's the door to\x01",
            "Geofront C-Division.\x01",
            "Open it?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3098")
    Fade(500)
    OP_68(75060, 800, 20060, 0)
    MoveCamera(43, 14, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20250, 0)
    OP_0D()
    Sleep(500)
    Sound(100, 0, 70, 0)
    OP_71(0x8, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x8)
    Sleep(500)
    Sound(454, 0, 100, 0)
    Sound(145, 2, 100, 0)
    OP_82(0x32, 0x32, 0xBB8, 0x3E8)
    OP_71(0x8, 0xB, 0x28, 0x0, 0x0)
    OP_79(0x8)
    Sound(143, 0, 100, 0)
    OP_24(0x91)
    Sleep(500)
    OP_65(0x4, 0x1)
    SetScenarioFlags(0x0, 7)

    label("loc_3098")

    ClearMapFlags(0x8000000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_30A3")

    Return()

    # Function_21_2F1A end

    def Function_22_30A4(): pass

    label("Function_22_30A4")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x109, 4330, 2000, 23330, 0)
    SetChrPos(0x102, 2900, 2000, 23240, 0)
    SetChrPos(0x101, 5350, 2000, 22780, 0)
    SetChrPos(0x103, 3280, 2000, 22060, 0)
    SetChrPos(0x104, 4150, 2000, 21040, 0)
    SetChrPos(0x105, 5950, 2000, 21600, 0)
    OP_68(4530, 3000, 23340, 0)
    MoveCamera(45, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15800, 0)
    LoadChrToIndex("chr/ch05500.itc", 0x1E)
    LoadChrToIndex("chr/ch28600.itc", 0x1F)
    SetChrChipByIndex(0x15, 0x1E)
    SetChrChipByIndex(0x16, 0x1F)
    SetChrSubChip(0x15, 0x0)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x15, 0x4)
    SetChrFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x15, 4700, 6500, 42400, 180)
    SetChrPos(0x16, 5750, 6500, 43250, 180)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02900.itp")
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x109,
        "#10100FGood work, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Oh, Sergeant Noｱl...\x01",
            "Good work!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The Sergeant Major is with you\x01",
            "guys. That must make you guys\x01",
            "that Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Do you need something\x01",
            "from us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FNo, that's not the case, but...\x02\x03",
            "#00003FWhen the IBC building exploded, you\x01",
            "were near the scene and we were\x01",
            "wondering about the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00101F...How bad is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yeah... It's practically\x01",
            "a pile of rubble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I think it'll be hard\x01",
            "for them to rebuild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "And that person was just\x01",
            "about to inspect, but...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Woman's Voice",
        (
            "My, Elie and everyone...\x01",
            "What are you doing in a\x01",
            "place like this, I wonder?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(700)

    def lambda_3522():
        OP_93(0xA, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3522)
    Sleep(50)

    def lambda_3532():
        OP_93(0xB, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_3532)
    Sleep(300)
    SetChrPos(0x15, 3900, 5000, 37400, 180)
    SetChrPos(0x16, 4950, 5000, 39500, 180)
    OP_68(4640, 3200, 24370, 2000)
    MoveCamera(45, 15, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(19450, 2000)

    def lambda_3592():
        OP_95(0x15, 3900, 5000, 27400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3592)
    Sleep(200)

    def lambda_35AF():
        OP_95(0x16, 4950, 5000, 28000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_35AF)
    Sleep(3000)

    ChrTalk(
        0x102,
        "#00105F#12PBell!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200F#12PMariabell?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x15, 1)
    WaitChrThread(0x16, 1)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x15,
        (
            "Yes, I was just coming to IBC for\x01",
            "an inspection.\x02\x03",
            "Uhuhu. Would you like to chat?\x02",
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
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0x0, 0x0)
    SetChrPos(0x15, 1350, 2000, 22900, 90)
    SetChrPos(0x16, 700, 2000, 24100, 90)
    OP_93(0x101, 0x10E, 0x0)
    OP_93(0x102, 0x10E, 0x0)
    OP_93(0x104, 0x10E, 0x0)
    OP_93(0x103, 0x10E, 0x0)
    OP_93(0x109, 0x10E, 0x0)
    OP_93(0x105, 0x10E, 0x0)
    OP_93(0xA, 0x10E, 0x0)
    OP_93(0xB, 0x10E, 0x0)
    OP_68(4570, 2700, 23870, 0)
    MoveCamera(45, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16720, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00000FMariabell... It's been a\x01",
            "while.\x02\x03",
            "#00004FI think the last time is\x01",
            "when we got that\x01",
            "invitation to Michelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#02900F#3PBut even so, it's been a while\x01",
            "since I've seen your faces.\x02\x03",
            "#02904FIt looks like you were present at\x01",
            "the scene of IBC's destruction,\x01",
            "but most importantly, you're safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00100FYou too Bell... It looks\x01",
            "like you were at Michelam at\x01",
            "the time of the incident.\x02\x03",
            "#00104FThank goodness you're\x01",
            "safe...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#02900F#3PUhuhu. Oh, Elie... You\x01",
            "were that worried about\x01",
            "me?\x02\x03",
            "#02909FAh, surely it's a trick\x01",
            "to make me fall in love\x01",
            "with you!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#11P#00106FB-Bell!... It's only\x01",
            "natural for me to worry\x01",
            "about you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FBut how to say this... You\x01",
            "seem relaxed even though the\x01",
            "IBC building was destroyed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, that's right. You\x01",
            "seem composed somehow,\x01",
            "given that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#02904F#3P*sigh*... Does it look\x01",
            "that way?\x02\x03",
            "#02901FThe situation is\x01",
            "serious.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x105,
        (
            "#10305FI knew it. I guess the\x01",
            "situation's pretty bad?\x02\x03",
            "#10303FI heard it's nothing\x01",
            "more than a mountain of\x01",
            "rubble, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#02901F#3PIt's not just bad!\x02\x03",
            "#02903FI mean, of all things,\x01",
            "to think the IBC\x01",
            "building was blown up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I'm just her guard, but\x01",
            "the situation is\x01",
            "honestly awful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "We looked for a way to recover the safe's\x01",
            "contents as well as the sepith ingots\x01",
            "that were stored in the basement, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#02906F#3PHonestly, I've given up at this point.\x02\x03",
            "#02901FRebuilding a completely destroyed\x01",
            "building will be difficult. It'll take\x01",
            "time even just to remove this rubble.\x02\x03",
            "#02906FI'm happy we were able to transfer\x01",
            "bank functions to Orchis Tower as an\x01",
            "emergency measure, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#2PI heard about that. You\x01",
            "were able to quickly\x01",
            "retreive the data backup.\x02\x03",
            "#00200FVarious countries praised\x01",
            "your emergency\x01",
            "preparedness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#02902F#3PAs system manager, it was the natural\x01",
            "thing to do.\x02\x03",
            "#02906FWell, we're now dealing with customers\x01",
            "at Orchis Tower, so everything turned\x01",
            "out all right, but...\x02\x03",
            "#02901FI'm positively furious at that Red\x01",
            "Constellation jaeger group.\x02\x03",
            "#02903FI'm busy even at the best of times,\x01",
            "and they've increased my workload even\x01",
            "more...\x02\x03",
            "#02901FIf I happen to see them, I will tear\x01",
            "every single limb off their bodies!!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#11P#00103F(Hmm, she's raging\x01",
            "mad...)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#11P#00105FBy the way, Bell.\x02\x03",
            "What about your precious\x01",
            "Rosenberg dolls?\x02\x03",
            "#00103FDon't tell me they're in\x01",
            "the rubble somewhere?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x15,
        (
            "#02903F#3PUhuhu. Listen to this.\x02\x03",
            "#02903FActually, I instructed the maid that\x01",
            "cleans my room to take the trunks\x01",
            "with her in the event of emergency.\x02\x03",
            "#02900FThanks to her, they're all unhurt.\x02\x03",
            "#02909FUhuhu. Force of habit. What a silver\x01",
            "lining.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F(Haha. She looks happy\x01",
            "whenever she talks about\x01",
            "her dolls.)\x02\x03",
            "#00006F(...It'd be helpful if\x01",
            "she was that nice to me,\x01",
            "though.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x16, 0x15, 500)

    ChrTalk(
        0x16,
        (
            "Umm, Miss Mariabell?\x01",
            "It's about time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#02905F#3PMy... The flower of our\x01",
            "short conversation has\x01",
            "bloomed.\x02\x03",
            "#02900FSee you then, Elie and\x01",
            "everyone. If you'll all\x01",
            "excuse me then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FYeah, sorry for\x01",
            "bothering you when\x01",
            "you're so busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00100FSee you, Bell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#02902F#3PHaha, good day.\x02",
    )

    CloseMessageWindow()
    OP_93(0x15, 0x10E, 0x1F4)

    def lambda_453C():
        OP_95(0x15, -20000, 2000, 22900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_453C)
    OP_68(2500, 2700, 23800, 5000)

    def lambda_4567():

        label("loc_4567")

        TurnDirection(0x16, 0x15, 500)
        Yield()
        Jump("loc_4567")

    QueueWorkItem2(0x16, 2, lambda_4567)
    Sleep(1050)
    EndChrThread(0x16, 0x2)

    def lambda_4580():
        OP_95(0x16, -20000, 2000, 24100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4580)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_68(2500, 2700, 23800, 0)
    Sleep(500)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x0)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_93(0xA, 0xB4, 0x0)
    OP_93(0xB, 0xB4, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 4320, 2000, 22960, 0)
    SetScenarioFlags(0x191, 3)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_22_30A4 end

    def Function_23_4612(): pass

    label("Function_23_4612")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xF, 21190, 0, 1100, 0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0x10, 22390, 0, 1100, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 7310, 0, 14850, 225)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    ClearChrFlags(0x17, 0x80)
    OP_78(0xB, 0x17)
    OP_49()
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    ClearChrFlags(0x18, 0x80)
    OP_78(0xC, 0x18)
    OP_49()
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x1000)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x17, 3000, 2000, 21500, 0)
    OP_D5(0x17, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x18, 6000, 5300, 40000, 180)
    OP_D5(0x18, 0x2710, 0x2BF20, 0x0, 0x0)
    OP_68(19250, 2500, 10000, 0)
    MoveCamera(30, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(30000, 0)
    OP_68(21000, 1000, 19800, 8000)
    MoveCamera(35, 15, 0, 8000)
    SetCameraDistance(20000, 8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(5000)
    Sound(459, 0, 50, 0)
    OP_6F(0x79)
    Fade(500)
    SetMapObjFrame(0xFF, "keepout", 0x0, 0x1)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_68(4450, 3200, 25750, 0)
    MoveCamera(35, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(23000, 0)
    MoveCamera(40, 30, 0, 7000)
    SetCameraDistance(25000, 7000)

    def lambda_4832():
        OP_95(0xFE, 500, 2000, 25450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4832)

    def lambda_484C():
        OP_95(0xFE, 8100, 2000, 25450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_484C)
    BeginChrThread(0x17, 1, 0, 24)
    OP_0D()
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0xB4, 0x1F4)
    WaitChrThread(0xB, 1)
    OP_93(0xB, 0x10E, 0x1F4)
    BeginChrThread(0x18, 1, 0, 25)
    Sleep(3500)
    Sound(459, 0, 100, 0)
    OP_6F(0x79)
    StopSound(459, 1000, 60)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c140D", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_23_4612 end

    def Function_24_48AD(): pass

    label("Function_24_48AD")

    Sound(492, 0, 50, 0)
    OP_71(0xB, 0x5B, 0x78, 0x0, 0x8)
    OP_96(0xFE, 0xBB8, 0x7D0, 0x57E4, 0x3E8, 0x0)
    OP_79(0xB)
    Sleep(1000)
    Sound(493, 0, 100, 0)
    StopSound(459, 200, 40)
    OP_71(0xB, 0x3C, 0x5A, 0x0, 0x8)
    OP_79(0xB)
    OP_71(0xB, 0x79, 0xB4, 0x0, 0x20)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 3000, 2000, 23500)
    OP_9F(0x1, 3000, 2200, 25500)
    OP_9F(0x1, 3000, 6700, 45500)
    OP_9F(0x2, 0xFE, 6000, 0x6)
    Return()

    # Function_24_48AD end

    def Function_25_4938(): pass

    label("Function_25_4938")

    OP_71(0xC, 0x5B, 0x78, 0x0, 0x8)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 6000, 6700, 45500)
    OP_9F(0x1, 6000, 2500, 27500)
    OP_9F(0x2, 0xFE, 4000, 0x6)
    OP_79(0xC)
    OP_71(0xC, 0x3C, 0x5A, 0x0, 0x8)
    OP_79(0xC)
    Return()

    # Function_25_4938 end

    def Function_26_4980(): pass

    label("Function_26_4980")

    EventBegin(0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02300.itp")
    Fade(500)
    OP_68(74500, -1600, 20000, 0)
    MoveCamera(41, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 73000, -2500, 19300, 90)
    SetChrPos(0x102, 73400, -2500, 20700, 90)
    SetChrPos(0x103, 72600, -2500, 18000, 45)
    SetChrPos(0x104, 72300, -2500, 21100, 90)
    SetChrPos(0x109, 71600, -2500, 18500, 90)
    SetChrPos(0x105, 71300, -2500, 20000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A31")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4B1D")
    OP_63(0x8, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0x8,
        (
            "What's with you? You're late!\x02\x03",
            "Well, whatever. Let's get going!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BA5")

    label("loc_4B1D")

    OP_63(0x8, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0x8,
        (
            "Hey. Been waiting.\x02\x03",
            "Alright, let's get going!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BA5")

    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    Sleep(150)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        (
            "#6P#00011FWait a sec... What's\x01",
            "going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FI mean, damn. This brat\x01",
            "always goes at his own\x01",
            "pace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02305F#11POh, that's right. I\x01",
            "guess I haven't told\x01",
            "you.\x02\x03",
            "#02309FYa see... I was hoping\x01",
            "you'd take me to a\x01",
            "Geofront terminal room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105FA Geofront terminal\x01",
            "room, you say...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10301FThat room that blew up\x01",
            "before?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02303F#11PThat was the "No. 8\x01",
            "Control Terminal" in\x01",
            "B-Division.\x02\x03",
            "#02300FI'd like you to take me\x01",
            "to the "No. 4 Control\x01",
            "Terminal" in C-Division.\x02\x03",
            "#02309FMan, I can't work freely\x01",
            "on the other control\x01",
            "terminals anymore.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#6P#00211FYou're so stubborn...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FThe "Orbal Network Basic\x01",
            "Law" has already gone\x01",
            "into effect.\x02\x03",
            "#00101FYou know we can't let\x01",
            "you take possession of\x01",
            "it illegally, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00013FMore importantly, based\x01",
            "on what Elie said, we\x01",
            "have to stop you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#02305F#11PN-No! I'm telling you, it's\x01",
            "not illegal!\x02\x03",
            "#02303FI'm currently a Foundation\x01",
            "network engineer!\x02\x03",
            "#02301FI'm telling you! I have\x01",
            "permission to access the\x01",
            "Geofront control terminals!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#5P#00001F...Tio, what do you\x01",
            "think?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5153():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5153)
    Sleep(50)

    def lambda_5163():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5163)
    Sleep(50)

    def lambda_5173():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5173)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x103,
        (
            "#6P#00206FHe is qualified to access\x01",
            "the terminals, but even so,\x01",
            "it's a gray area.\x02\x03",
            "#00200FI think it'll take a little\x01",
            "longer for the orbal network\x01",
            "law to be put in place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00108FHmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FBut isn't this request a\x01",
            "little strange?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FThat's right. Assisting\x01",
            "with activities that are\x01",
            "in a gray area...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02311F#11POh please. You guys are way too\x01",
            "strict!\x02\x03",
            "#02310FThat Ouroboros, right? Those\x01",
            "weird guys set a lot of traps\x01",
            "using the network, didn't they?\x02\x03",
            "Where's the guarantee that they\x01",
            "aren't using it even now?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_53B2():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_53B2)
    Sleep(50)

    def lambda_53C2():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_53C2)
    Sleep(50)

    def lambda_53D2():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_53D2)
    Sleep(50)

    def lambda_53E2():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_53E2)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x101,
        "#6P#00005FIsn't that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10303FHe does have a point.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02303F#11PChief was worried about\x01",
            "that but he's busy and\x01",
            "can't get around to it.\x02\x03",
            "He gave me you guys as\x01",
            "support for doing this.\x02\x03",
            "#02301FYou should thank me. And\x01",
            "don't hold back, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FDamn. At least his mouth\x01",
            "works.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FBut if he says he's worried\x01",
            "about it, he's worried\x01",
            "about it.\x02\x03",
            "#00208FThat Fool boy... and Dr.\x01",
            "Novartis...\x02\x03",
            "#00201FThey seemed to have network\x01",
            "technology surpassing that\x01",
            "of the foundation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00008F............\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#6P#00001F─Got it. We'll help.\x02\x03",
            "#00003FHowever, we won't tolerate\x01",
            "clearly illegal hacking,\x01",
            "you hear?\x02\x03",
            "And you won't spend several\x01",
            "days down there either.\x01",
            "You'll sleep in your bed.\x02\x03",
            "#00000FThose are the conditions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02306F#11PWhoa, hey, give me a\x01",
            "break, will ya?\x02\x03",
            "#02302FWhy does genius engineer\x01",
            "Jona have to clash with\x01",
            "the real world so bad─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00013F*glare*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#02305F#11PUgh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FHaha, you're strict when\x01",
            "it comes to things like\x01",
            "this, aren't you, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00204FWell if it's just that,\x01",
            "I think you can accept\x01",
            "the conditions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02311F#11POh fine! I got it, ok!?\x02\x03",
            "Those conditions are fine.\x01",
            "Hurry up and take me already!\x02\x03",
            "#02307FThose Orchis Tower terminal\x01",
            "restrictions are so tight.\x01",
            "Agh, I can't take it anymore!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FI guess that's how he\x01",
            "really feels.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10108FHmm... That's not\x01",
            "healthy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02306F#11PS-Shut up.\x02\x03",
            "#02300FSo... You guys ready for\x01",
            "C-Division?\x02\x03",
            "In think there are monsters\x01",
            "and stuff in here just like\x01",
            "the other divisions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00008FRight...\x02",
    )

    CloseMessageWindow()
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x181, 3)
    Jump("loc_5AC4")

    label("loc_5A31")


    ChrTalk(
        0x8,
        (
            "#02305F#11PWhat? You guys ready?\x02\x03",
            "#02300FIn think there are monsters\x01",
            "and stuff in here just like\x01",
            "the other divisions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00008FRight...\x02",
    )

    CloseMessageWindow()

    label("loc_5AC4")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Ready\x01",                  # 0
            "Need to get ready\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SoundLoad(145)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5B19"),
        (1, "loc_5FD2"),
        (SWITCH_DEFAULT, "loc_606A"),
    )


    label("loc_5B19")


    ChrTalk(
        0x8,
        (
            "#02309F#11PHehe, then let's hurry\x01",
            "and head down.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#6P#10105FDown, you say...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FWhat do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02304F#11PThe C-Division entrance\x01",
            "is in this lighthouse.\x02\x03",
            "#02302FYou didn't know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00011FR-Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#02309F#11PHeheh, watch and learn.\x02",
    )

    CloseMessageWindow()
    OP_68(77500, -1000, 20000, 1500)
    MoveCamera(49, 15, 0, 1500)
    SetCameraDistance(21000, 1500)
    OP_93(0x8, 0x5A, 0x1F4)

    def lambda_5CF0():
        OP_95(0xFE, 76400, -2500, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5CF0)
    WaitChrThread(0x8, 1)
    OP_6F(0x79)
    Sound(100, 0, 70, 0)
    OP_71(0x8, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x8)
    Sleep(1000)
    Sound(454, 0, 100, 0)
    Sound(145, 2, 100, 0)
    OP_82(0x32, 0x32, 0xBB8, 0x3E8)
    OP_71(0x8, 0xB, 0x28, 0x0, 0x0)
    OP_79(0x8)
    Sound(143, 0, 100, 0)
    OP_24(0x91)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00105FSo it was here...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#N#10302FMan. Who would put it\x01",
            "here?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x8, 0x10E, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#11P#02302F#11PAlright, let's head\x01",
            "inside already!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x1F4)
    OP_63(0x8, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)

    def lambda_5EA5():
        OP_95(0xFE, 77500, -2500, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5EA5)
    WaitChrThread(0x8, 1)
    Sound(102, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x2)

    def lambda_5EDE():
        OP_95(0xFE, 80500, -2500, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5EDE)
    BeginChrThread(0x101, 3, 0, 27)
    Sleep(900)
    BeginChrThread(0x102, 3, 0, 27)
    Sleep(300)
    BeginChrThread(0x103, 3, 0, 27)
    Sleep(800)
    BeginChrThread(0x104, 3, 0, 27)
    Sleep(600)
    BeginChrThread(0x109, 3, 0, 27)
    Sleep(600)
    BeginChrThread(0x105, 3, 0, 27)
    StopSound(126, 1000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Jona has been added to the\x01",
            "party as a guest. If his HP\x01",
            "reaches 0, it's game over.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddParty(0x3D, 0xFF, 0xFF)
    SetScenarioFlags(0x181, 4)
    OP_29(0xAC, 0x1, 0x8)
    StopBGM(0xFA0)
    WaitBGM()
    EventEnd(0x5)
    NewScene("m0200", 100, 0, 0)
    IdleLoop()
    Jump("loc_606A")

    label("loc_5FD2")


    ChrTalk(
        0x8,
        (
            "#02303F#11PAh, well in that case,\x01",
            "hurry up and get ready!\x02\x03",
            "#02300FI'll be waiting for you\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 72500, -2500, 20000, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x8, 0xFF)
    OP_24(0x91)
    EventEnd(0x5)
    Jump("loc_606A")

    label("loc_606A")

    Return()

    # Function_26_4980 end

    def Function_27_606B(): pass

    label("Function_27_606B")


    def lambda_6070():
        OP_95(0xFE, 76000, -2500, 20000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6070)
    WaitChrThread(0xFE, 1)

    def lambda_608E():
        OP_95(0xFE, 80500, -2500, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_608E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_27_606B end

    def Function_28_60A8(): pass

    label("Function_28_60A8")


    def lambda_60AD():
        OP_95(0xFE, 74000, -2500, 20000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_60AD)

    def lambda_60C7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_60C7)
    WaitChrThread(0xFE, 1)

    def lambda_60DC():
        OP_95(0xFE, 66900, -2500, 17100, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_60DC)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_28_60A8 end

    def Function_29_60FD(): pass

    label("Function_29_60FD")


    def lambda_6102():
        OP_95(0xFE, 74000, -2500, 20000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6102)

    def lambda_611C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_611C)
    WaitChrThread(0xFE, 1)

    def lambda_6131():
        OP_95(0xFE, 69300, -2500, 18400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6131)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_29_60FD end

    def Function_30_6152(): pass

    label("Function_30_6152")


    def lambda_6157():
        OP_95(0xFE, 74000, -2500, 20000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6157)

    def lambda_6171():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6171)
    WaitChrThread(0xFE, 1)

    def lambda_6186():
        OP_95(0xFE, 68500, -2500, 17300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6186)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_30_6152 end

    def Function_31_61A7(): pass

    label("Function_31_61A7")


    def lambda_61AC():
        OP_95(0xFE, 74000, -2500, 20000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_61AC)

    def lambda_61C6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_61C6)
    WaitChrThread(0xFE, 1)

    def lambda_61DB():
        OP_95(0xFE, 69800, -2500, 16600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_61DB)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_31_61A7 end

    def Function_32_61FC(): pass

    label("Function_32_61FC")


    def lambda_6201():
        OP_95(0xFE, 74000, -2500, 20000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6201)

    def lambda_621B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_621B)
    WaitChrThread(0xFE, 1)

    def lambda_6230():
        OP_95(0xFE, 70600, -2500, 17700, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6230)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_32_61FC end

    def Function_33_6251(): pass

    label("Function_33_6251")


    def lambda_6256():
        OP_95(0xFE, 74000, -2500, 20000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6256)

    def lambda_6270():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6270)
    WaitChrThread(0xFE, 1)

    def lambda_6285():
        OP_95(0xFE, 68300, 0, 19100, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6285)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_33_6251 end

    def Function_34_62A6(): pass

    label("Function_34_62A6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51522.itc", 0x1E)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10100.itp")
    SoundLoad(145)
    SoundLoad(3520)
    SoundLoad(3521)
    SoundLoad(3522)
    SetChrPos(0x101, 79000, -2500, 20000, 270)
    SetChrPos(0x102, 79000, -2500, 20000, 270)
    SetChrPos(0x103, 79000, -2500, 20000, 270)
    SetChrPos(0x104, 79000, -2500, 20000, 270)
    SetChrPos(0x109, 79000, -2500, 20000, 270)
    SetChrPos(0x105, 79000, -2500, 20000, 270)
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
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xEE, 0x98, 0x84, 0x2D, 0x1AE, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    PlayBGM("ed7514", 0)
    OP_68(79000, -1500, 20000, 0)
    MoveCamera(59, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(26500, 0)
    OP_70(0x8, 0xB)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(454, 0, 100, 0)
    Sound(145, 2, 100, 0)
    ClearMapObjFlags(0x8, 0x10)
    OP_71(0x8, 0xB, 0x28, 0x0, 0x0)
    OP_79(0x8)
    Sound(143, 0, 100, 0)
    OP_24(0x91)
    Sound(102, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x2)
    OP_68(69000, -1500, 17600, 7500)
    MoveCamera(59, 17, 0, 7500)
    SetCameraDistance(22500, 7500)
    BeginChrThread(0x101, 3, 0, 28)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 30)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 29)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 31)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 33)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 32)
    Sleep(1500)
    Sound(102, 0, 100, 0)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x2)
    Sound(454, 0, 100, 0)
    Sound(145, 2, 100, 0)
    OP_71(0x8, 0x28, 0x47, 0x0, 0x0)
    OP_79(0x8)
    Sound(143, 0, 100, 0)
    OP_24(0x91)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#5P#00008FIt's already evening,\x01",
            "huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00106FLet's eat out tonight...\x01",
            "That's all for the day's\x01",
            "work.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x109, 3)

    ChrTalk(
        0x109,
        "#10108F#5PRight...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x105)
    OP_64(0x109)
    Sleep(500)
    Fade(2000)
    OP_68(79000, 3000, 10000, 0)
    MoveCamera(55, 0, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(45000, 0)
    MoveCamera(75, 0, 0, 12000)
    SetCameraDistance(40000, 12000)
    OP_6F(0x79)
    Fade(500)
    OP_68(68300, -1500, 18500, 0)
    MoveCamera(59, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetCameraDistance(24000, 2000)

    def lambda_66A1():
        OP_96(0xFE, 0x10ACC, 0xFFFFF63C, 0x4C2C, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_66A1)
    WaitChrThread(0x109, 1)
    OP_6F(0x79)
    OP_C9(0x0, 0x80000000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0x109,
        (
            "#3520V#30W─Everyone. You all helped me so\x01",
            "much.\x02\x03",
            "#3521VIt wasn't all that long, but... I\x01",
            "really learned a lot.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xDC1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_C9(0x1, 0x80000000)

    def lambda_67B1():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_67B1)
    Sleep(50)

    def lambda_67C1():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_67C1)
    Sleep(50)

    def lambda_67D1():
        TurnDirection(0x104, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_67D1)
    Sleep(50)

    def lambda_67E1():
        TurnDirection(0x103, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_67E1)
    Sleep(50)

    def lambda_67F1():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_67F1)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    Sleep(150)

    ChrTalk(
        0x101,
        "#12P#00004FNoｱl... That's our line.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#12P...It's been just about\x01",
            "exactly three months,\x01",
            "hasn't it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00206FOnly two months for me,\x01",
            "I suppose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00302FI'm not sure how to say\x01",
            "this... We're going to\x01",
            "miss you, Noｱl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#5PAhaha... I don't want to\x01",
            "go, either.\x02\x03",
            "#10108FThere's the Ouroboros and\x01",
            "the jaegers... the cryptids\x01",
            "and those blue flowers...\x02\x03",
            "#10106FI'm sorry I have to leave\x01",
            "with none of that resolved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00008FNoｱl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11P─Though our positions may be\x01",
            "different, we're all thinking\x01",
            "of Crossbell, right?\x02\x03",
            "#10302FAlthough that may sound\x01",
            "strange coming from me.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x105, 500)
    Sleep(150)

    ChrTalk(
        0x109,
        "#10102F#5PWazy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11PI hope you come back to us if you get\x01",
            "the chance.\x02\x03",
            "#10302FAll our hopes are basically riding on\x01",
            "your shoulders, right?\x02\x03",
            "#10309FYou'll definitely have a better view of\x01",
            "the future using your guns in the CGF,\x01",
            "so I hope you'll do your very best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#5PC'mon... Cocky until the\x01",
            "very end, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00012FHaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00304FI'm sure that was the reason\x01",
            "Commander Sonya let you\x01",
            "transfer in the first place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#12PI would love the chance\x01",
            "to work with you again\x01",
            "someday.\x02\x03",
            "#00109FEven if that doesn't pan\x01",
            "out, let's meet up on\x01",
            "our days off, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00204F...I'd like you to teach\x01",
            "me how to drive a car,\x01",
            "too.\x02\x03",
            "#00202FYou couldn't teach me\x01",
            "this time because I'm\x01",
            "too young.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    ChrTalk(
        0x109,
        (
            "#10112F#5PAhaha... *sniff*. I'd\x01",
            "love to!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00008F............\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#12P#00004F─Thanks, Noｱl.\x02\x03",
            "Your driving, combat\x01",
            "skills and energy have\x01",
            "saved us so many times...\x02\x03",
            "#00000FBut above all, your\x01",
            "honesty encouraged all of\x01",
            "us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105F#5PLloyd...\x02",
    )

    CloseMessageWindow()
    OP_68(68400, -1400, 18800, 1800)
    MoveCamera(44, 13, 0, 1800)
    SetCameraDistance(22500, 1800)

    def lambda_6EB8():

        label("loc_6EB8")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_6EB8")

    QueueWorkItem2(0x109, 2, lambda_6EB8)

    def lambda_6ECA():
        OP_95(0xFE, 67300, -2500, 19200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6ECA)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x109, 500)
    EndChrThread(0x109, 0x2)
    OP_6F(0x79)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x10)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x20)
    SetChrChipByIndex(0x109, 0x1E)
    SetChrSubChip(0x109, 0x8)
    SetChrFlags(0x109, 0x10)
    SetChrFlags(0x109, 0x2)
    SetChrFlags(0x109, 0x20)
    Sound(802, 0, 100, 0)
    Sleep(110)
    SetChrSubChip(0x101, 0x1)
    Sleep(110)
    SetChrSubChip(0x101, 0x2)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#6P#00002FWe are friends, even if\x01",
            "apart.\x02\x03",
            "Please, ask for our help\x01",
            "if the CGF ever needs\x01",
            "us.\x02\x03",
            "#00009FOf course, we won't\x01",
            "hesitate to ask for your\x01",
            "help, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#11P#10114F...Ah...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0x109, 0xB)
    Sleep(130)
    SetChrSubChip(0x109, 0xC)
    Sleep(800)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x109,
        "#11P#10112FYes... I'd be glad to!\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1300)

    ChrTalk(
        0x105,
        (
            "#10302F#11P(Haha, that's our leader\x01",
            "for you.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00211F(I guess he does show\x01",
            "his good points every\x01",
            "once in a while...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00113F(S-Seriously...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00302F(Haha. At this rate,\x01",
            "you're gonna have to work\x01",
            "a little harder, milady.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00112F(I-I don't really...)\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x6)
    Sleep(50)
    SetChrSubChip(0x109, 0xE)
    Sleep(200)

    ChrTalk(
        0x101,
        "#5P#00005F? What's wrong?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x109,
        "#5P#10114F#3522V#12A#30WHuh? Ah!\x02",
    )

    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x10)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x20)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    ClearChrFlags(0x109, 0x10)
    ClearChrFlags(0x109, 0x2)
    ClearChrFlags(0x109, 0x20)
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_72B9():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_72B9)

    def lambda_72C6():

        label("loc_72C6")

        TurnDirection(0xFE, 0x109, 500)
        Yield()
        Jump("loc_72C6")

    QueueWorkItem2(0x102, 2, lambda_72C6)

    def lambda_72D8():

        label("loc_72D8")

        TurnDirection(0xFE, 0x109, 500)
        Yield()
        Jump("loc_72D8")

    QueueWorkItem2(0x105, 2, lambda_72D8)

    def lambda_72EA():

        label("loc_72EA")

        TurnDirection(0xFE, 0x109, 500)
        Yield()
        Jump("loc_72EA")

    QueueWorkItem2(0x104, 2, lambda_72EA)
    OP_68(69100, -1400, 18800, 650)
    SetCameraDistance(23000, 650)

    def lambda_7316():
        OP_96(0xFE, 0x10D88, 0xFFFFF63C, 0x4DBC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7316)
    WaitChrThread(0x109, 1)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x104, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x109,
        (
            "#10112F#5PS-Sorry. I didn't mean\x01",
            "that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00309FHmm? What do you mean by\x01",
            ""that"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FHehe. I think we'll see this kind\x01",
            "of thing again if you do end up\x01",
            "coming back to the Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10114F#5PR-Randy! Wazy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00113F*sigh*... I've had quite\x01",
            "enough of this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00011F???\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(69290, -1400, 18560, 1800)

    def lambda_7491():

        label("loc_7491")

        TurnDirection(0xFE, 0x109, 500)
        Yield()
        Jump("loc_7491")

    QueueWorkItem2(0x101, 2, lambda_7491)

    def lambda_74A3():
        OP_96(0xFE, 0x10810, 0xFFFFF63C, 0x4394, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_74A3)
    WaitChrThread(0x101, 1)
    EndChrThread(0x101, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#6P#00008F(...Tio, what are they\x01",
            "talking about?)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_757C")

    ChrTalk(
        0x103,
        (
            "#12P#00211F(...I don't know? Please\x01",
            "think about it\x01",
            "yourself.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006F(She's mad about\x01",
            "something...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_75EA")

    label("loc_757C")


    ChrTalk(
        0x103,
        (
            "#12P#00204F(I think they're saying\x01",
            "you're still too\x01",
            "inexperienced.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00006F(They're judging me?)\x02",
    )

    CloseMessageWindow()

    label("loc_75EA")

    SetCameraDistance(23500, 2000)
    StopSound(126, 1000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "That night, Lloyd and the others went\x01",
            "to the Central Square restaurant and\x01",
            "held a farewell party for Noｱl.\x02\x03",
            "Sergei, KeA and even Zeit attended.\x01",
            "They spent a bittersweet evening\x01",
            "together.\x02\x03",
            "Then, the next morning─ Noｱl packed\x01",
            "her bags and left the Support Section\x01",
            "building.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_32(0xFF, 0xFE, 0x0)
    RemoveParty(0x8, 0xFF)
    RemoveParty(0x4, 0xFF)
    OP_BC(0x8)
    OP_BC(0x4)
    StopBGM(0xFA0)
    WaitBGM()
    OP_CC(0x1, 0xFF, 0x0)
    OP_24(0x91)
    SetScenarioFlags(0x22, 2)
    NewScene("m0209", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_62A6 end

    def Function_35_7751(): pass

    label("Function_35_7751")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　  ～Land for Sale～\x01",
            "Crossbell City Development Office\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_35_7751 end

    def Function_36_77C3(): pass

    label("Function_36_77C3")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　  "Restricted Area"\x01",
            "It is dangerous, so please\x01",
            "refrain from entering.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_36_77C3 end

    SaveToFile()

Try(main)
