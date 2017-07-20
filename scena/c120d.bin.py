from ScenarioHelper import *

def main():
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
        "Yona",                   # 1
        "Policeman",                   # 2
        "A security guard",               # 3
        "A security guard",               # 4
        "Cunha",               # 5
        "Ozel",               # 6
        "Bishop",             # 7
        "Quinn old man",           # 8
        "Amisa",                 # 9
        "Policeman",                   # 10
        "Defense Forces soldier",             # 11
        "Armored car",                 # 12
        "Nielsen",             # 13
        "Marybele",             # 14
        "Security guards",           # 15
        "car",                     # 16
        "car",                     # 17
        "bc1200",                 # 18
        "Central square",               # 19
        "Nishi dori",                 # 20
        "Administrative district",                 # 21
        "Residential area",                 # 22
        "Entertainment district",                 # 23
        "East Street",                 # 24
        "old Town",                 # 25
        "Harbor district",                 # 26
        "IBC",                 # 27
        "Beside the station",               # 28
        "Back street",                 # 29
        "Ursula interchange",           # 30
        "East Crossbell Highway",       # 31
        "West Crossbell Highway",       # 32
        "Mainz Mountain Road",           # 33
        "Orchis Tower",         # 34
    ))

    ATBonus("ATBonus_674", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_7159", 8,   8,   8,   8,   11,  11,  11)

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
        "BattleInfo_744", 0x0000, 99, 6, 60, 4, 1, 25, 0, "bc1200", "Sepith_7159", 60, 25, 10, 5,
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

    PlaceName(-123.13999938964844, 0.0, -85.1500015258789, 0x0000, 0x0000, "Central square")
    PlaceName(-209.27000427246094, 0.0, -79.26000213623047, 0x0000, 0x0000, "Nishi dori")
    PlaceName(-87.7699966430664, 0.0, 31.440000534057617, 0x0000, 0x0000, "Administrative district")
    PlaceName(-289.17999267578125, 0.0, 18.34000015258789, 0x0000, 0x0000, "Residential area")
    PlaceName(-193.5500030517578, 0.0, 7.860000133514404, 0x0000, 0x0000, "Entertainment district")
    PlaceName(-16.700000762939453, 0.0, -115.27999877929688, 0x0000, 0x0000, "East Street")
    PlaceName(29.799999237060547, 0.0, -187.3300018310547, 0x0000, 0x0000, "old Town")
    PlaceName(19.979999542236328, 0.0, -28.81999969482422, 0x0000, 0x0000, "Harbor district")
    PlaceName(-14.079999923706055, 0.0, 94.31999969482422, 0x0000, 0x0000, "IBC")
    PlaceName(-108.4000015258789, 0.0, -175.5399932861328, 0x0000, 0x0000, "Beside the station")
    PlaceName(-169.97000122070312, 0.0, -39.29999923706055, 0x0000, 0x0000, "Back street")
    PlaceName(-112.33000183105469, 0.0, -216.14999389648438, 0x0000, 0x0000, "Ursula interchange")
    PlaceName(54.040000915527344, 0.0, -96.94000244140625, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-276.0799865722656, 0.0, -81.22000122070312, 0x0000, 0x0000, "West Crossbell Highway")
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
        "Function_10_17D6",        # 0A, 10
        "Function_11_1873",        # 0B, 11
        "Function_12_191D",        # 0C, 12
        "Function_13_1D1A",        # 0D, 13
        "Function_14_204F",        # 0E, 14
        "Function_15_22EE",        # 0F, 15
        "Function_16_255A",        # 10, 16
        "Function_17_27B2",        # 11, 17
        "Function_18_28A1",        # 12, 18
        "Function_19_293E",        # 13, 19
        "Function_20_2A10",        # 14, 20
        "Function_21_2AE4",        # 15, 21
        "Function_22_2C69",        # 16, 22
        "Function_23_413F",        # 17, 23
        "Function_24_43DA",        # 18, 24
        "Function_25_4465",        # 19, 25
        "Function_26_44AD",        # 1A, 26
        "Function_27_5A63",        # 1B, 27
        "Function_28_5AA0",        # 1C, 28
        "Function_29_5AF5",        # 1D, 29
        "Function_30_5B4A",        # 1E, 30
        "Function_31_5B9F",        # 1F, 31
        "Function_32_5BF4",        # 20, 32
        "Function_33_5C49",        # 21, 33
        "Function_34_5C9E",        # 22, 34
        "Function_35_704D",        # 23, 35
        "Function_36_70B7",        # 24, 36
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1612")
    Sound(14, 0, 100, 0)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('粉红液体', 1)"), scpexpr(EXPR_END)), "loc_159B")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '粉红液体'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_160D")

    label("loc_159B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '粉红液体'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '粉红液体'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

    label("loc_160D")

    Jump("loc_1657")

    label("loc_1612")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_175F")

    ChrTalk(
        0xFE,
        (
            "The people of the black moon,\x01",
            "I have not found it yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even in the collapsed building\x01",
            "I have no clue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whether it is latent in autonomous state,\x01",
            "Did you flee outside the country …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Where the hell have you gone\x01",
            "I guess it is.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_17D2")

    label("loc_175F")


    ChrTalk(
        0xFE,
        (
            "The people of the black moon,\x01",
            "Whether it is latent in autonomous state,\x01",
            "Did you flee outside the country …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Where the hell have you gone\x01",
            "I guess it is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17D2")

    TalkEnd(0xFE)
    Return()

    # Function_9_168C end

    def Function_10_17D6(): pass

    label("Function_10_17D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17E8")
    Call(0, 22)
    Jump("loc_1872")

    label("loc_17E8")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The collapsed IBC building,\x01",
            "Just like a mountain of debris.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As long as it has been broken,\x01",
            "It would be honestly difficult to rebuild … …\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_1872")

    Return()

    # Function_10_17D6 end

    def Function_11_1873(): pass

    label("Function_11_1873")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1885")
    Call(0, 22)
    Jump("loc_191C")

    label("loc_1885")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The visit of the daughter of IBC, too,\x01",
            "It seems that there was not much achievement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The bank's system\x01",
            "I moved to the Orkis Tower,\x01",
            "It will be the happiness of unhappiness.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_191C")

    Return()

    # Function_11_1873 end

    def Function_12_191D(): pass

    label("Function_12_191D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_19AF")

    ChrTalk(
        0xFE,
        (
            "Finally the sunny day\x01",
            "If you think you can look at the sky ……\x01",
            "What is that tree?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can not see it as a weapon, but ….\x01",
            "Is that the president's work?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D16")

    label("loc_19AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_19BD")
    Jump("loc_1D16")

    label("loc_19BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1B71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ADF")

    ChrTalk(
        0xFE,
        (
            "I was surprised by the sudden deployment to drift … ….\x01",
            "If you do not say it as strongly as this,\x01",
            "It is just being licked by two major powers, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So I, decidedly\x01",
            "I will support President Dieter!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I also have Director Arios … …\x01",
            "Already in the 2 biggest countries\x01",
            "Things I do not want only to do selfish!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B6C")

    label("loc_1ADF")


    ChrTalk(
        0xFE,
        (
            "Of course I am worried … …\x01",
            "I am firm\x01",
            "I will support President Dieter!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Already in the 2 biggest countries\x01",
            "Things I do not want only to do selfish!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B6C")

    Jump("loc_1D16")

    label("loc_1B71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1D16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C6A")

    ChrTalk(
        0xFE,
        (
            "A completely destroyed company near the park ……\x01",
            "It is rumored to be hired by the government of the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because I understood it Empire hired\x01",
            "They were hit by a hunting corps … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Such circumstances do not matter … …\x01",
            "Anyway, with this crossbell\x01",
            "You do not want to do extra things.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D16")

    label("loc_1C6A")


    ChrTalk(
        0xFE,
        (
            "This was the situation that\x01",
            "Cross Bells forever\x01",
            "Because it is a dependent state … what is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, after all,\x01",
            "We clearly state the will of independence\x01",
            "I think it should be shown to neighboring countries.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D16")

    TalkEnd(0xFE)
    Return()

    # Function_12_191D end

    def Function_13_1D1A(): pass

    label("Function_13_1D1A")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D27")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_204B")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",          # 0
            "to shop\x01",      # 1
            "quit\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D85")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1D85")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DA5")
    OP_AF(0x7B)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2046")

    label("loc_1DA5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DB9")
    Jump("loc_2046")

    label("loc_1DB9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2046")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1EFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E99")

    ChrTalk(
        0xFE,
        (
            "There are hardships to overcome … …\x01",
            "And there is no hardship that can not be overcome!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What are the two big powers, the creepy trees!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter what,\x01",
            "I just keep behaving noodles here!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1EFA")

    label("loc_1E99")


    ChrTalk(
        0xFE,
        "What are the two big powers, the creepy trees!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter what,\x01",
            "I just keep behaving noodles here!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EFA")

    Jump("loc_2046")

    label("loc_1EFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1F0D")
    Jump("loc_2046")

    label("loc_1F0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1F88")

    ChrTalk(
        0xFE,
        "Hmm, I finally came here … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I intended to do it as it was.\x01",
            "If you do this, you will only thoroughly fight!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2046")

    label("loc_1F88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2046")

    ChrTalk(
        0xFE,
        (
            "For many years, food stalls that have been accompanied by hardships\x01",
            "When it was destroyed it was quite a shock … …\x01",
            "It can not be helped not to look forward!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Along with this newly bought stall\x01",
            "I will change my mind again and I will try my best!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2046")

    Jump("loc_1D27")

    label("loc_204B")

    TalkEnd(0xFE)
    Return()

    # Function_13_1D1A end

    def Function_14_204F(): pass

    label("Function_14_204F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2106")

    ChrTalk(
        0xFE,
        (
            "Busy, busy ……\x01",
            "Delivery work by the influence of martial law\x01",
            "I am busy after a long absence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hello, but after all the delivery shop\x01",
            "I do not want it like this.\x01",
            "I feel like I'm alive.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22EA")

    label("loc_2106")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2114")
    Jump("loc_22EA")

    label("loc_2114")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_225F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21EF")

    ChrTalk(
        0xFE,
        (
            "Because rail services stopped this morning,\x01",
            "The number that can be delivered has also decreased considerably.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rather than going …\x01",
            "I wonder what the crossbell really becomes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It is more important than work … …\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_225A")

    label("loc_21EF")


    ChrTalk(
        0xFE,
        (
            "Really, if you go this way\x01",
            "I wonder what the crossbell really becomes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It is more important than work … …\x02",
    )

    CloseMessageWindow()

    label("loc_225A")

    Jump("loc_22EA")

    label("loc_225F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_22EA")

    ChrTalk(
        0xFE,
        (
            "As early as a week from the attack incident ……\x01",
            "Have you finally calmed down here as well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, such a case\x01",
            "I do not want you to get up again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22EA")

    TalkEnd(0xFE)
    Return()

    # Function_14_204F end

    def Function_15_22EE(): pass

    label("Function_15_22EE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2399")

    ChrTalk(
        0xFE,
        (
            "It is good with the President '\x01",
            "That big tree is good, absolutely\x01",
            "It is only a matter of acquaintance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Potatoes, the future\x01",
            "Whatever happens may I\x01",
            "Just protect Amisa.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2556")

    label("loc_2399")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_23A7")
    Jump("loc_2556")

    label("loc_23A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_24DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_246A")

    ChrTalk(
        0xFE,
        (
            "What a stupid speech ……\x01",
            "Even if the world can be fooled,\x01",
            "This eagle will not be deceived!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What is an independent country, what is a defense army!\x01",
            "Truly from us the threat of the two great countries\x01",
            "Do you even think that you can protect it!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_24D8")

    label("loc_246A")


    ChrTalk(
        0xFE,
        (
            "Goddess ……\x01",
            "I do not care about Eagle etc.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well then, please have a granddaughter,\x01",
            "Please save Amisa … …!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24D8")

    Jump("loc_2556")

    label("loc_24DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2556")

    ChrTalk(
        0xFE,
        (
            "At that time, if I was a little late for escape\x01",
            "Eagle and Amisa ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… I think so\x01",
            "Even now it is terrible and can not be helped.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2556")

    TalkEnd(0xFE)
    Return()

    # Function_15_22EE end

    def Function_16_255A(): pass

    label("Function_16_255A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_26E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2655")

    ChrTalk(
        0xFE,
        (
            "There are still many things to come\x01",
            "It might happen,\x01",
            "Grandpa was saying that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If the city is like the previous time\x01",
            "I'm scared when attacked ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Still, my favorite\x01",
            "If you are with grandpa\x01",
            "I feel like I can endure anything.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_26DC")

    label("loc_2655")


    ChrTalk(
        0xFE,
        (
            "If the city is like the previous time\x01",
            "I'm scared when attacked ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Still, my favorite\x01",
            "If you are with grandpa\x01",
            "I feel like I can endure anything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26DC")

    Jump("loc_27AE")

    label("loc_26E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_26EF")
    Jump("loc_27AE")

    label("loc_26EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2764")

    ChrTalk(
        0xFE,
        (
            "Like Grandpa says\x01",
            "I wonder if it really is going to be a war ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "… Yeah, I'm scared ………\x02",
    )

    CloseMessageWindow()
    Jump("loc_27AE")

    label("loc_2764")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_27AE")

    ChrTalk(
        0xFE,
        (
            "Toho-style building that was over there … …\x01",
            "It's totally gone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27AE")

    TalkEnd(0xFE)
    Return()

    # Function_16_255A end

    def Function_17_27B2(): pass

    label("Function_17_27B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_289D")

    ChrTalk(
        0xFE,
        (
            "Although the black month office was completely destroyed,\x01",
            "In this week as well in this week\x01",
            "It seems that it was oddly calm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Of the soon-to-be referendum ballot\x01",
            "Thanks, citizens who are depressed\x01",
            "It seems to be relatively small … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Something like this at the last minute\x01",
            "I feel something like powerfulness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_289D")

    TalkEnd(0xFE)
    Return()

    # Function_17_27B2 end

    def Function_18_28A1(): pass

    label("Function_18_28A1")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "What is it, so\x01",
            "Passing a sleeve through a new uniform\x01",
            "Do not tighten your body and mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, from now on\x01",
            "For the Crossbell independent country\x01",
            "I will do my best.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_28A1 end

    def Function_19_293E(): pass

    label("Function_19_293E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2A0C")

    ChrTalk(
        0xFE,
        "A big tree that gives off a blue light …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's as if it happened at Libert\x01",
            "The appearance of Libel-Ark\x01",
            "It is an association event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That was an ancient city over there\x01",
            "I heard a story,\x01",
            "Altogether with Taiki … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A0C")

    TalkEnd(0xFE)
    Return()

    # Function_19_293E end

    def Function_20_2A10(): pass

    label("Function_20_2A10")

    EventBegin(0x1)
    Sound(2094, 255, 100, 0)

    ChrTalk(
        0x101,
        "#0000FI'm going to catch you here.\x02",
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
            "Do you fish?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "To fish\x01",      # 0
            "quit\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ADF")
    OP_E2(0x2)
    MiniGame(0x6, 0x1, 0x14226, 0xFFFFF63C, 0x3AA2, 0xB4, 0x13812, 0xFFFFF254, 0x226A)

    label("loc_2ADF")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_20_2A10 end

    def Function_21_2AE4(): pass

    label("Function_21_2AE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B69")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "\"Lupinas river and first lighthouse\"\x01\x01",
            "Do not enter other than stakeholders.\x01",
            "~ Cross Bell City ~\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Jump("loc_2C68")

    label("loc_2B69")

    SetMapFlags(0x8000000)
    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a door to Geo Front C.\x01",
            "Do you want to open it?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C5D")
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

    label("loc_2C5D")

    ClearMapFlags(0x8000000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_2C68")

    Return()

    # Function_21_2AE4 end

    def Function_22_2C69(): pass

    label("Function_22_2C69")

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
            "Oh no, Sergeant Noel … ….\x01",
            "Is cheers for good work!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "When the sergeant is together,\x01",
            "Are you the Special Affairs Division of the example?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Is there any work here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FNo, that's why\x01",
            "I do not think so.\x02\x03",
            "#00003FWhen the IBC building was bombed,\x01",
            "I was near the work site\x01",
            "I was curious about the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101FAfter all,\x01",
            "Is that a terrible situation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Oh … exactly\x01",
            "In the state of a mountain of debris etc.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "To rebuild the building\x01",
            "It felt honestly seems difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Now, exactly that person\x01",
            "I am inspecting … …\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Female voice",
        (
            "Oh, everyone to Eli … ….\x01",
            "What in a place like this\x01",
            "I wonder?\x02",
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

    def lambda_30BA():
        OP_93(0xA, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_30BA)
    Sleep(50)

    def lambda_30CA():
        OP_93(0xB, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_30CA)
    Sleep(300)
    SetChrPos(0x15, 3900, 5000, 37400, 180)
    SetChrPos(0x16, 4950, 5000, 39500, 180)
    OP_68(4640, 3200, 24370, 2000)
    MoveCamera(45, 15, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(19450, 2000)

    def lambda_312A():
        OP_95(0x15, 3900, 5000, 27400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_312A)
    Sleep(200)

    def lambda_3147():
        OP_95(0x16, 4950, 5000, 28000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3147)
    Sleep(3000)

    ChrTalk(
        0x102,
        "#00105F#12PBell …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200F#12PWas it Maria Bell?\x02",
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
            "Yes, just to visit IBC\x01",
            "It is a place that has come.\x02\x03",
            "Uhufu, if you do not mind\x01",
            "Shall I tell you a story?\x02",
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
            "#00000FMr. Maria Bell ……\x01",
            "long time no see.\x02\x03",
            "#00004FBefore Michelam\x01",
            "Invite me\x01",
            "Ever since then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#02900F#3Pby the way\x01",
            "The face is aligned\x01",
            "It was a long time ago.\x02\x03",
            "#02904FOn the site of collapse of IBC\x01",
            "I heard that I was present,\x01",
            "It was safe and to the best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00100FBell …… At the time of the incident exactly,\x01",
            "You seem to have been in Michelin.\x02\x03",
            "#00104FIt was truly okay and good …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#02900F#3PUhufu, Ellie … ___ ___ 0\x01",
            "So far about me\x01",
            "Were you worried about me?\x02\x03",
            "#02909FOh, just this\x01",
            "It is a work to make love!\x02",
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
            "#11P#00106FWell, if the bell is already over ……\x01",
            "It is not natural to worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FBut what is it …?\x01",
            "I heard that IBC was destroyed\x01",
            "It is somewhat surplus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, that's right.\x01",
            "Thanks to you I feel relieved somewhat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#02904F#3PFu … … Do you see that?\x02\x03",
            "#02901FEven this is quite serious.\x02",
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
            "#10305FAfter all, is the situation considerably bad?\x02\x03",
            "#10303FIt has become a mountain of rubble\x01",
            "I just heard that ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#02901F#3PIt's not bad!\x02\x03",
            "#02903FTotally, more and more IBC Building\x01",
            "It will be blown up …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Although I accompanied the lady's escort\x01",
            "To be honest I was terrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "It was preserved in the basement\x01",
            "Collecting sepis ingots and safe deposits\x01",
            "It was an inspection to investigate … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#02906F#3PTo be honest, the place for now is upset.\x02\x03",
            "#02901FIt is difficult to rebuild a completely destroyed building,\x01",
            "It will take time to remove rubble.\x02\x03",
            "#02906FThe function of the bank as an emergency measure\x01",
            "I was able to move to the Orkis Tower\x01",
            "I was fortunate enough … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#2PI heard that story.\x01",
            "The data you were backing up\x01",
            "I promptly resurrected.\x02\x03",
            "#00200FThe measure at the time of emergency was perfect\x01",
            "Evaluations from countries as well\x01",
            "You heard it was expensive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#02902F#3PAs a system administrator\x01",
            "Until we did the obvious thing.\x02\x03",
            "#02906FWell, for the time being at the Orkis Tower\x01",
            "We can respond to customers\x01",
            "Although it became a result or ……\x02\x03",
            "#02901FThat \"red constellation\"\x01",
            "The hunting corps is really angry.\x02\x03",
            "#02903FEven though I'm just busy,\x01",
            "It increased my extra work … …\x02\x03",
            "#02901FIf you see something in the future,\x01",
            "Using all kinds of hands\x01",
            "I will do it for 8 tears! It is!\x02",
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
            "#11P#00103F(Well, angry heart and\x01",
            "I feel it … …)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#11P#00105FBy the way … Bell.\x02\x03",
            "I was cherishing for you\x01",
            "Rosenberg doll\x01",
            "What happened?\x02\x03",
            "#00103FNo way, get caught in rubble\x01",
            "Did not I ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x15,
        (
            "#02903F#3PUhufu, please listen to it.\x02\x03",
            "#02903FActually, to the maid who asked for the cleaning of the room\x01",
            "In an emergency, put it in the trunk\x01",
            "I was instructed to take it out.\x02\x03",
            "#02900FThanks to that, they\x01",
            "Everyone was intact.\x02\x03",
            "#02909FUhufu, everyday actions\x01",
            "I wonder if it was ok.\x01",
            "It is an unfortunate happiness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F(When it comes to dolls' story\x01",
            "It seemed like I was happy soon. )\x02\x03",
            "#00006F(… … I also have this\x01",
            "If you touch me gently\x01",
            "I am saved. )\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x16, 0x15, 500)

    ChrTalk(
        0x16,
        (
            "Um, Maria Bell Old Lady,\x01",
            "It's about time you already have it ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#02905F#3POh …… Talk a bit\x01",
            "The flowers have bloomed.\x02\x03",
            "#02900FWell then, Ellie, everyone.\x01",
            "I will excuse myself with this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FOh, you are busy.\x01",
            "Stopped me\x01",
            "I'm sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00100FWell then, bell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#02902F#3PHehe, thank you.\x02",
    )

    CloseMessageWindow()
    OP_93(0x15, 0x10E, 0x1F4)

    def lambda_4069():
        OP_95(0x15, -20000, 2000, 22900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4069)
    OP_68(2500, 2700, 23800, 5000)

    def lambda_4094():

        label("loc_4094")

        TurnDirection(0x16, 0x15, 500)
        Yield()
        Jump("loc_4094")

    QueueWorkItem2(0x16, 2, lambda_4094)
    Sleep(1050)
    EndChrThread(0x16, 0x2)

    def lambda_40AD():
        OP_95(0x16, -20000, 2000, 24100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_40AD)
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

    # Function_22_2C69 end

    def Function_23_413F(): pass

    label("Function_23_413F")

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

    def lambda_435F():
        OP_95(0xFE, 500, 2000, 25450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_435F)

    def lambda_4379():
        OP_95(0xFE, 8100, 2000, 25450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_4379)
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

    # Function_23_413F end

    def Function_24_43DA(): pass

    label("Function_24_43DA")

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

    # Function_24_43DA end

    def Function_25_4465(): pass

    label("Function_25_4465")

    OP_71(0xC, 0x5B, 0x78, 0x0, 0x8)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 6000, 6700, 45500)
    OP_9F(0x1, 6000, 2500, 27500)
    OP_9F(0x2, 0xFE, 4000, 0x6)
    OP_79(0xC)
    OP_71(0xC, 0x3C, 0x5A, 0x0, 0x8)
    OP_79(0xC)
    Return()

    # Function_25_4465 end

    def Function_26_44AD(): pass

    label("Function_26_44AD")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_542E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4657")
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
            "What is it, very much\x01",
            "Was it late?\x02\x03",
            "Well someday.\x01",
            "Let's hurry and go!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46E9")

    label("loc_4657")

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
            "Yo! I was waiting.\x02\x03",
            "Sort of\x01",
            "Let's hurry and go!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46E9")

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
            "#6P#00011Fwait a minute……\x01",
            "You do not understand suddenly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWait, as usual\x01",
            "It is a selfish pedant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02305F#11PWell, I see.\x01",
            "I did not talk properly.\x02\x03",
            "#02309FNo, in fact.\x01",
            "To the terminal room of Geo Front\x01",
            "I want you to take me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10105FA terminal room in the Geofront…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10301FThat room that was blown up before?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02303F#11PThat is a Geo Front\x01",
            "\"Eighth control terminal\" in B section.\x02\x03",
            "#02300FI would like you to take me\x01",
            "\"Fourth control terminal\" in C section.\x02\x03",
            "#02309FNo, as with other control terminals\x01",
            "Freedom does not work.\x02",
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
        "#6P#00211FJona, you have no resraint\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F\"Basic conductivity net method\"\x01",
            "It is already enforced.\x02\x03",
            "#00101FIndeed Illegal occupation\x01",
            "You can not help me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00013FBy the time I heard the story\x01",
            "I have no choice but to stop ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#02305F#11PNo, no\x01",
            "It's not illegal!\x02\x03",
            "#02303FMy current position is\x01",
            "I am an engineer of the Foundation!\x02\x03",
            "#02301FGeoFront's control terminal\x01",
            "You also have management qualifications!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(150)

    ChrTalk(
        0x101,
        "#5P#00001FTio… what do you think?\x02",
    )

    CloseMessageWindow()

    def lambda_4C3B():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4C3B)
    Sleep(50)

    def lambda_4C4B():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4C4B)
    Sleep(50)

    def lambda_4C5B():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4C5B)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x103,
        (
            "#6P#00206FThe management qualification is true\x01",
            "Still it is gray feeling.\x02\x03",
            "#00200FBasic conductivity net method is also\x01",
            "Should I be prepared a little more?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00108FHmmm\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FAs might be expected\x01",
            "Is it slightly subtle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FWell, gray zone's\x01",
            "Even helping the act ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02311F#11POh you guys are too strict\x02\x03",
            "#02310FWas it \"association\"?\x01",
            "That funny guys also on the power net\x01",
            "How did you get on with it?\x02\x03",
            "There is no guarantee that something is done now\x01",
            "Where is it?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4E2E():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4E2E)
    Sleep(50)

    def lambda_4E3E():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4E3E)
    Sleep(50)

    def lambda_4E4E():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4E4E)
    Sleep(50)

    def lambda_4E5E():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4E5E)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x101,
        "#6P#00005FThat is..\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303F…… Indeed it is\x01",
            "You may be saying that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02303F#11PBoss#4ROsassu#I was curious though\x01",
            "I am busy and my hands are running.\x02\x03",
            "It's easy to move out of my way\x01",
            "I'm gonna shoot it for support.\x02\x03",
            "#02301FI am thankful,\x01",
            "It is strange to be dismayed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FGeez.\x01",
            "Only mouth is a good boy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203F… but it certainly\x01",
            "Speaking of bothering you will be worried.\x02\x03",
            "#00208FThat \"clown\" boys …\x01",
            "Dr. Novartis … …\x02\x03",
            "#00201FNetwork technology that exceeds the foundation\x01",
            "Certainly it seemed to have it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00008F…\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#6P#00001FGot it. We'll help\x02\x03",
            "#00003FHowever, obviously illegal\x01",
            "You will have hacks refrained from you?\x02\x03",
            "And do not spend days in the basement\x01",
            "Sleeping in bed in the room.\x02\x03",
            "#00000FThose are the conditions\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02306F#11PCome on, c'mon, please ~?\x02\x03",
            "#02302FWhy is this genius Jonah\x01",
            "I have to adapt to such real - ─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00013FGlare.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#02305F#11PUgh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FHuhu, that is\x01",
            "Lloyd is a tough one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00204FWell, that condition is\x01",
            "He who drank it is safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02311F#11POh fine, I got it\x02\x03",
            "Because that's fine.\x01",
            "Bring it to moment!\x02\x03",
            "#02307FRestricted\x01",
            "Olkus tower's terminal\x01",
            "I can not bear it anymore!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00302FWell I guess he's serious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10108FHmmm\x01",
            "After all it is a little unhealthy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02306F#11PS-shut up\x02\x03",
            "#02300FSo it's a C block … …\x01",
            "Are you ready now?\x02\x03",
            "Like other geo front compartments,\x01",
            "Why do you think you are like a devil?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00008FRight…\x02",
    )

    CloseMessageWindow()
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x181, 3)
    Jump("loc_54B5")

    label("loc_542E")


    ChrTalk(
        0x8,
        (
            "#02305F#11PWhat, are you ready yet?\x02\x03",
            "#02300FLike other geo front compartments,\x01",
            "Why do you think you are like a devil?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00008FRight…\x02",
    )

    CloseMessageWindow()

    label("loc_54B5")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Choice 1: All set\x01",          # 0
            "Once the preparation is ready\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SoundLoad(145)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5518"),
        (1, "loc_59D2"),
        (SWITCH_DEFAULT, "loc_5A62"),
    )


    label("loc_5518")


    ChrTalk(
        0x8,
        (
            "#02309F#11PWell, then\x01",
            "Let's get off at last.\x02",
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
        "#6P#10105FHead in?\x02",
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
            "#02304F#11POh, the entrance of C block\x01",
            "You are on this lighthouse.\x02\x03",
            "#02302FYou didn't know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00011FR-really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#02309F#11PHehe, take a look\x02",
    )

    CloseMessageWindow()
    OP_68(77500, -1000, 20000, 1500)
    MoveCamera(49, 15, 0, 1500)
    SetCameraDistance(21000, 1500)
    OP_93(0x8, 0x5A, 0x1F4)

    def lambda_56EF():
        OP_95(0xFE, 76400, -2500, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_56EF)
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
        "#00105FIn a place like this\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#N#10302FWhew.\x01",
            "My hobby is fully opened.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x8, 0x10E, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#11P#02302F#11PAll right, sort of\x01",
            "Let's get in as soon as possible!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x1F4)
    OP_63(0x8, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)

    def lambda_58AD():
        OP_95(0xFE, 77500, -2500, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_58AD)
    WaitChrThread(0x8, 1)
    Sound(102, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x2)

    def lambda_58E6():
        OP_95(0xFE, 80500, -2500, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_58E6)
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
            "Jonah joined the escort subject.\x01",
            "Game over when HP becomes 0.\x07\x00\x02",
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
    Jump("loc_5A62")

    label("loc_59D2")


    ChrTalk(
        0x8,
        (
            "#02303F#11PIf so\x01",
            "Get ready now.\x02\x03",
            "#02300FWait here and do it.\x02",
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
    Jump("loc_5A62")

    label("loc_5A62")

    Return()

    # Function_26_44AD end

    def Function_27_5A63(): pass

    label("Function_27_5A63")


    def lambda_5A68():
        OP_95(0xFE, 76000, -2500, 20000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5A68)
    WaitChrThread(0xFE, 1)

    def lambda_5A86():
        OP_95(0xFE, 80500, -2500, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5A86)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_27_5A63 end

    def Function_28_5AA0(): pass

    label("Function_28_5AA0")


    def lambda_5AA5():
        OP_95(0xFE, 74000, -2500, 20000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5AA5)

    def lambda_5ABF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5ABF)
    WaitChrThread(0xFE, 1)

    def lambda_5AD4():
        OP_95(0xFE, 66900, -2500, 17100, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5AD4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_28_5AA0 end

    def Function_29_5AF5(): pass

    label("Function_29_5AF5")


    def lambda_5AFA():
        OP_95(0xFE, 74000, -2500, 20000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5AFA)

    def lambda_5B14():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5B14)
    WaitChrThread(0xFE, 1)

    def lambda_5B29():
        OP_95(0xFE, 69300, -2500, 18400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5B29)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_29_5AF5 end

    def Function_30_5B4A(): pass

    label("Function_30_5B4A")


    def lambda_5B4F():
        OP_95(0xFE, 74000, -2500, 20000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5B4F)

    def lambda_5B69():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5B69)
    WaitChrThread(0xFE, 1)

    def lambda_5B7E():
        OP_95(0xFE, 68500, -2500, 17300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5B7E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_30_5B4A end

    def Function_31_5B9F(): pass

    label("Function_31_5B9F")


    def lambda_5BA4():
        OP_95(0xFE, 74000, -2500, 20000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5BA4)

    def lambda_5BBE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5BBE)
    WaitChrThread(0xFE, 1)

    def lambda_5BD3():
        OP_95(0xFE, 69800, -2500, 16600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5BD3)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_31_5B9F end

    def Function_32_5BF4(): pass

    label("Function_32_5BF4")


    def lambda_5BF9():
        OP_95(0xFE, 74000, -2500, 20000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5BF9)

    def lambda_5C13():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5C13)
    WaitChrThread(0xFE, 1)

    def lambda_5C28():
        OP_95(0xFE, 70600, -2500, 17700, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5C28)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_32_5BF4 end

    def Function_33_5C49(): pass

    label("Function_33_5C49")


    def lambda_5C4E():
        OP_95(0xFE, 74000, -2500, 20000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5C4E)

    def lambda_5C68():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5C68)
    WaitChrThread(0xFE, 1)

    def lambda_5C7D():
        OP_95(0xFE, 68300, 0, 19100, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5C7D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_33_5C49 end

    def Function_34_5C9E(): pass

    label("Function_34_5C9E")

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
        "#5P#00008FIt's totally evening now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00106FI'm eating out tonight ….\x01",
            "I wonder if I have work here as well.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x109, 3)

    ChrTalk(
        0x109,
        "#10108F#5PYes…\x02",
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

    def lambda_6081():
        OP_96(0xFE, 0x10ACC, 0xFFFFF63C, 0x4C2C, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6081)
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
            "#3520V#30W── Everyone.\x01",
            "Thank you for everything.\x02\x03",
            "#3521VIt was a short while … ….\x01",
            "It was truly a study.\x02",
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

    def lambda_6188():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6188)
    Sleep(50)

    def lambda_6198():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6198)
    Sleep(50)

    def lambda_61A8():
        TurnDirection(0x104, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_61A8)
    Sleep(50)

    def lambda_61B8():
        TurnDirection(0x103, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_61B8)
    Sleep(50)

    def lambda_61C8():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_61C8)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#12P#00004FNoel…\x01",
            "Here's the line.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#12PJust outside\x01",
            "It was about three months.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00206FI was with you\x01",
            "About two months or so ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00302FWhat is it?\x01",
            "You will be sad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#5PHaha ……\x01",
            "I am sorry.\x02\x03",
            "#10108FAnd it's an association and a hunting soldier … …\x01",
            "The problem of phantom beasts and blue flowers … ….\x02\x03",
            "#10106FI have not solved it at all\x01",
            "Sorry to get away ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00008FNoel…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11P─ ─ Well, although the position is different\x01",
            "Feelings thinking of crossbell\x01",
            "I wish it was the same, were not you?\x02\x03",
            "#10302FWhen I say\x01",
            "It may be scattered, though.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x105, 500)
    Sleep(150)

    ChrTalk(
        0x109,
        "#10102F#5PWazy…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11PIf you get one step on it\x01",
            "You should come back again.\x02\x03",
            "#10302FYou, once#4R噵 噵#The future\x01",
            "It is the body you are expecting, right?\x02\x03",
            "#10309FI'm just doing guchi in the guard\x01",
            "Certainly the view can be expanded\x01",
            "I think that it will become a study.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#5PEven ….\x01",
            "Because it is cheeky to the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00012FHaha\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00304FWell, surely Sonja command as well\x01",
            "In the meantime you\x01",
            "I wonder whether he was sent off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#12PEven if Noel is good\x01",
            "Come and let's work together again.\x02\x03",
            "#00109FEven if it is not so holiday\x01",
            "You can go play together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00204F…… I also like driving a car\x01",
            "I want to tell you.\x02\x03",
            "#00202FBecause of age restrictions\x01",
            "I was not taught this time.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    ChrTalk(
        0x109,
        (
            "#10112F#5PHaha …. Gus.\x01",
            "It's a pleasure!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00008F…\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#12P#00004FThanks Noel.\x02\x03",
            "With your driving, battle techniques and\x01",
            "I was helped many times in my action power ….\x02\x03",
            "#00000FMore than anything in the straight\x01",
            "I think that I was always encouraged.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105F#5PLloyd….\x02",
    )

    CloseMessageWindow()
    OP_68(68400, -1400, 18800, 1800)
    MoveCamera(44, 13, 0, 1800)
    SetCameraDistance(22500, 1800)

    def lambda_681C():

        label("loc_681C")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_681C")

    QueueWorkItem2(0x109, 2, lambda_681C)

    def lambda_682E():
        OP_95(0xFE, 67300, -2500, 19200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_682E)
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
            "#6P#00002FEven if we're apart, we're friends.\x02\x03",
            "If there is a problem with the guard\x01",
            "Come and call us.\x02\x03",
            "#00009FWhen we also need help from Noel\x01",
            "I will depend on you without hesitation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#11P#10114F…AH…\x02",
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
        "#11P#10112FYes, gladly!\x02",
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
        "#10302F#11P(Heh, that's our leader)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00211F(A good place in a moment\x01",
            "You brought it … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00113F(S-seriously…)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00302F(Ha ha, this young lady too\x01",
            "I hope I will try my best. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00112F(I-I don't really care…)\x02",
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
        "#5P#10114F#3522V#12A#30WAhh! \x02",
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

    def lambda_6C02():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6C02)

    def lambda_6C0F():

        label("loc_6C0F")

        TurnDirection(0xFE, 0x109, 500)
        Yield()
        Jump("loc_6C0F")

    QueueWorkItem2(0x102, 2, lambda_6C0F)

    def lambda_6C21():

        label("loc_6C21")

        TurnDirection(0xFE, 0x109, 500)
        Yield()
        Jump("loc_6C21")

    QueueWorkItem2(0x105, 2, lambda_6C21)

    def lambda_6C33():

        label("loc_6C33")

        TurnDirection(0xFE, 0x109, 500)
        Yield()
        Jump("loc_6C33")

    QueueWorkItem2(0x104, 2, lambda_6C33)
    OP_68(69100, -1400, 18800, 650)
    SetCameraDistance(23000, 650)

    def lambda_6C5F():
        OP_96(0xFE, 0x10D88, 0xFFFFF63C, 0x4DBC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6C5F)
    WaitChrThread(0x109, 1)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x104, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x109,
        (
            "#10112F#5PWell, sorry.\x01",
            "Separately …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00309FHmm, that's why.\x01",
            "Why is that somehow?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FHuh, even in that way\x01",
            "Please come back to the support department\x01",
            "I feel like watching the rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10114F#5PS-senpai! Wazy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00113FOh seriously you guys…\x02",
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

    def lambda_6DCA():

        label("loc_6DCA")

        TurnDirection(0xFE, 0x109, 500)
        Yield()
        Jump("loc_6DCA")

    QueueWorkItem2(0x101, 2, lambda_6DCA)

    def lambda_6DDC():
        OP_96(0xFE, 0x10810, 0xFFFFF63C, 0x4394, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6DDC)
    WaitChrThread(0x101, 1)
    EndChrThread(0x101, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#6P#00008F(Tio, what are they talking about)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6E9C")

    ChrTalk(
        0x103,
        (
            "#12P#00211F(……here we go?\x01",
            "Please think about yourself. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00006F(I am mad at something ……)\x02",
    )

    CloseMessageWindow()
    Jump("loc_6F06")

    label("loc_6E9C")


    ChrTalk(
        0x103,
        (
            "#12P#00204F(Well, Mr. Lloyd also\x01",
            "It is still immature. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00006F(They're judging me again)\x02",
    )

    CloseMessageWindow()

    label("loc_6F06")

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
            "That night, Lloyd's at a restaurant in the central square\x01",
            "I held a farewell party for Noel.\x02\x03",
            "Not to mention Sergei and Ka'aa,\x01",
            "Zeit was also allowed to enter specially,\x01",
            "A fun evening is overriding night ……\x02\x03",
            "And next morning Noel put together the luggage\x01",
            "I left the building of the Special Affairs Support Division.\x07\x00\x02",
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

    # Function_34_5C9E end

    def Function_35_704D(): pass

    label("Function_35_704D")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "~ Sales floor ~\x01",
            "Crossbell City · Urban Development Division\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_35_704D end

    def Function_36_70B7(): pass

    label("Function_36_70B7")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "<Restricted area>\x01",
            "Because it is dangerous, within the premises\x01",
            "Please do not enter.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_36_70B7 end

    SaveToFile()

Try(main)
