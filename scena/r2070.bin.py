from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r2070.bin",                # FileName
        "r2070",                    # MapName
        "r2070",                    # Location
        0x0062,                     # MapIndex
        "ed7202",
        0x00000000,                 # Flags
        ("r2070", "r0000_1", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x23,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 202, 0, 4, 0, 5],
    )

    BuildStringList((
        "r2070",                  # 0
        "レオールガンイージ",     # 1
        "レオールガンイージ",     # 2
        "アビスワーム",           # 3
        "アビスワーム",           # 4
        "鉄鋼ドリュー",           # 5
        "鉄鋼ドリュー",           # 6
        "Sister Ries",            # 7
        "SE制御",                 # 8
        "br2070",                 # 9
        "br2070",                 # 10
        "br2070",                 # 11
        "br2070",                 # 12
        "br2080",                 # 13
        "To Mainz Mountain Path", # 14
    ))

    ATBonus("ATBonus_640", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_660", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_6879", 10,  0,   7,   0,   4,   2,   4)
    Sepith("Sepith_6881", 0,   4,   2,   9,   6,   4,   2)

    MonsterBattlePostion("MonsterBattlePostion_6A0", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_6A4", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_6A8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_6AC", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6B0", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6B4", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_6B8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6BC", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_700", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_704", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_708", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_70C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_710", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_714", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_718", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_71C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_680", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_684", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_688", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_68C", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_690", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_694", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_698", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_69C", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_720", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_724", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_728", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_72C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_730", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_734", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_738", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_73C", 0, 0, 180)

    # monster count: 6

    BattleInfo(
        "BattleInfo_740", 0x0000, 64, 6, 60, 6, 1, 25, 0, "br2070", "Sepith_6879", 30, 30, 25, 15,
        (
            ("ms76100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6A0", "MonsterBattlePostion_700", "ed7450", "ed7453", "ATBonus_640"),
            ("ms76100.dat", "ms76100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_680", "MonsterBattlePostion_700", "ed7450", "ed7453", "ATBonus_640"),
            ("ms76100.dat", "ms76100.dat", "ms76100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6A0", "MonsterBattlePostion_700", "ed7450", "ed7453", "ATBonus_640"),
            ("ms76100.dat", "ms76100.dat", "ms66300.dat", "ms76100.dat", 0, 0, 0, 0, "MonsterBattlePostion_680", "MonsterBattlePostion_700", "ed7450", "ed7453", "ATBonus_640"),
        )
    )

    BattleInfo(
        "BattleInfo_808", 0x0000, 64, 6, 60, 6, 1, 40, 0, "br2070", "Sepith_6881", 30, 30, 25, 15,
        (
            ("ms64300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6A0", "MonsterBattlePostion_700", "ed7450", "ed7453", "ATBonus_640"),
            ("ms64300.dat", "ms76100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_680", "MonsterBattlePostion_700", "ed7450", "ed7453", "ATBonus_640"),
            ("ms64300.dat", "ms76100.dat", "ms76100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6A0", "MonsterBattlePostion_700", "ed7450", "ed7453", "ATBonus_640"),
            ("ms64300.dat", "ms66300.dat", "ms66300.dat", "ms66300.dat", 0, 0, 0, 0, "MonsterBattlePostion_680", "MonsterBattlePostion_700", "ed7450", "ed7453", "ATBonus_640"),
        )
    )

    # event battle count: 5

    BattleInfo(
        "BattleInfo_8D0", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br2070", 0x00000000, 100, 0, 0, 0,
        (
            ("ms76100.dat", "ms76100.dat", "ms76100.dat", "ms76100.dat", "ms76100.dat", "ms76100.dat", "ms76100.dat", "ms76100.dat", "MonsterBattlePostion_680", "MonsterBattlePostion_700", "ed7453", "ed7453", "ATBonus_640"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_914", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br2070", 0x00000000, 100, 0, 0, 0,
        (
            ("ms76001.dat", "ms76001.dat", "ms76001.dat", "ms76001.dat", "ms76001.dat", "ms76001.dat", 0, 0, "MonsterBattlePostion_680", "MonsterBattlePostion_700", "ed7453", "ed7453", "ATBonus_640"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_958", 0x0042, 255, 6, 45, 3, 3, 30, 0, "br2080", 0x00000000, 100, 0, 0, 0,
        (
            ("ms80300.dat", "ms80300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_720", "MonsterBattlePostion_700", "ed7451", "ed7453", "ATBonus_660"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch14000.itc",                   # 00
        "monster/ch80350.itc",               # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "monster/ch76150.itc",               # 10
        "monster/ch76150.itc",               # 11
        "monster/ch64350.itc",               # 12
        "monster/ch64350.itc",               # 13
        "monster/ch76050.itc",               # 14
        "monster/ch76051.itc",               # 15
    ))

    DeclNpc(4294875996, 19750,   183369,  225,  453,  0x0, 0,   1,   0,   0,   3,   255, 255, 255,  0)
    DeclNpc(4294880597, 19750,   178770,  225,  453,  0x0, 0,   1,   0,   0,   3,   255, 255, 255,  0)
    DeclNpc(4294866207, 6000,    56509,   270,  484,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(4294835796, 20000,   73660,   270,  484,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(4294866207, 7000,    56509,   270,  484,  0x0, 0,   20,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(4294835796, 21000,   73660,   270,  484,  0x0, 0,   20,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(4294833877, 20000,   135100,  55,   385,  0x0, 0,   0,   0,   0,   2,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(4294940066, 5960,    0,       0x1010000,    "BattleInfo_740", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294898796, 36190,   10000,   0x1010000,    "BattleInfo_808", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294859316, 55130,   6000,    0x1010000,    "BattleInfo_740", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294855836, 28450,   2000,    0x1010000,    "BattleInfo_808", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294858556, 75420,   20000,   0x1010000,    "BattleInfo_740", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294830226, 87090,   20000,   0x1010000,    "BattleInfo_808", 0,   18,  0xFFFF, 2,  3)

    DeclEvent(0x0000, 0, 24,  -96.0,                 174.0,                 19.0,                  441.0,                 [-0.2357024997472763,  0.05050758272409439,   0.0,                   0.0,                   -0.2357020527124405,   -0.05050767958164215,  0.0,                   0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   18.38471794128418,     13.637063980102539,    -3.8000004291534424,   1.0])
    DeclEvent(0x0000, 0, 28,  -134.30999755859375,   133.35000610351562,    18.5,                  626.0004272460938,     [-0.07552560418844223, -0.10134761780500412,  0.0,                   0.0,                   0.03521830216050148,   -0.21733985841274261,  -0.0,                  0.0,                   0.0,                   0.0,                   0.25,                  0.0,                   -14.840204238891602,   15.37027359008789,     -4.625,                1.0])
    DeclEvent(0x0000, 0, 29,  -128.0,                142.0,                 18.5,                  626.0004272460938,     [-0.05892546847462654, -0.1695702224969864,   0.0,                   0.0,                   0.05892566218972206,   -0.1695697009563446,   -0.0,                  0.0,                   0.0,                   0.0,                   0.2499999850988388,    0.0,                   -15.909903526306152,   2.3739089965820312,    -4.624999523162842,    1.0])
    DeclEvent(0x0000, 0, 17,  -135.17999267578125,   126.5999984741211,     20.0,                  81.0,                  [0.1666666716337204,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   22.529998779296875,    -42.20000076293945,    -4.0,                  1.0])
    DeclEvent(0x0000, 0, 28,  -135.17999267578125,   126.5999984741211,     20.0,                  81.0,                  [0.1666666716337204,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   22.529998779296875,    -42.20000076293945,    -4.0,                  1.0])

    DeclActor(4294858576, 2000,    22560,   1200,    4294858576, 3000,    22560,   0x007C, 0,  6,  0x0000)
    DeclActor(4294851096, 2000,    29390,   1200,    4294851096, 3000,    29390,   0x007C, 0,  7,  0x0000)
    DeclActor(4294889456, 3750,    170050,  1200,    4294889456, 4750,    170050,  0x007C, 0,  8,  0x0000)
    DeclActor(4294867756, 7750,    191810,  1200,    4294867756, 8750,    191810,  0x007C, 0,  9,  0x0000)
    DeclActor(4294886546, 19750,   189250,  1200,    4294886546, 20750,   189250,  0x007C, 0,  15, 0x0000)
    DeclActor(4294904916, 11750,   159630,  1200,    4294904916, 12750,   159630,  0x007C, 0,  16, 0x0000)
    DeclActor(4294866206, 6000,    56510,   1200,    4294866206, 6000,    56510,   0x007C, 0,  10, 0x0000)
    DeclActor(4294835796, 20000,   73660,   1200,    4294835796, 20000,   73660,   0x007C, 0,  11, 0x0000)
    DeclActor(4294871596, 19750,   184720,  1200,    4294871596, 21750,   184720,  0x007C, 0,  13, 0x0000)
    DeclActor(4294871056, 20000,   185900,  1200,    4294871056, 22000,   185900,  0x007C, 0,  13, 0x0000)
    DeclActor(4294904916, 4294967046, 159630,  1200,    4294904916, 750,     159630,  0x007C, 0,  16, 0x0000)
    DeclActor(4294835046, 20000,   134700,  1200,    4294835046, 21500,   134700,  0x007C, 0,  32, 0x0000)

    PlaceName(16.25, 0.0, 5.0, 0x0000, 0x0000, "To Mainz Mountain Path")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 5])                   # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 3

    ScpFunction((
        "Function_0_A50",          # 00, 0
        "Function_1_A6D",          # 01, 1
        "Function_2_A8C",          # 02, 2
        "Function_3_B44",          # 03, 3
        "Function_4_BF4",          # 04, 4
        "Function_5_CE3",          # 05, 5
        "Function_6_154F",         # 06, 6
        "Function_7_16A1",         # 07, 7
        "Function_8_17F3",         # 08, 8
        "Function_9_1945",         # 09, 9
        "Function_10_1A97",        # 0A, 10
        "Function_11_1DF5",        # 0B, 11
        "Function_12_2153",        # 0C, 12
        "Function_13_2157",        # 0D, 13
        "Function_14_2490",        # 0E, 14
        "Function_15_2524",        # 0F, 15
        "Function_16_2570",        # 10, 16
        "Function_17_259C",        # 11, 17
        "Function_18_25E8",        # 12, 18
        "Function_19_2C3E",        # 13, 19
        "Function_20_2FB1",        # 14, 20
        "Function_21_3037",        # 15, 21
        "Function_22_33AF",        # 16, 22
        "Function_23_346D",        # 17, 23
        "Function_24_34A2",        # 18, 24
        "Function_25_42F7",        # 19, 25
        "Function_26_4BCD",        # 1A, 26
        "Function_27_4C11",        # 1B, 27
        "Function_28_4C2A",        # 1C, 28
        "Function_29_60FE",        # 1D, 29
        "Function_30_65B9",        # 1E, 30
        "Function_31_671B",        # 1F, 31
        "Function_32_67B1",        # 20, 32
    ))


    def Function_0_A50(): pass

    label("Function_0_A50")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A6C")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_0_A50")

    label("loc_A6C")

    Return()

    # Function_0_A50 end

    def Function_1_A6D(): pass

    label("Function_1_A6D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A8B")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_A6D")

    label("loc_A8B")

    Return()

    # Function_1_A6D end

    def Function_2_A8C(): pass

    label("Function_2_A8C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_ACC"),
        (1, "loc_AD8"),
        (2, "loc_AE4"),
        (3, "loc_AF0"),
        (4, "loc_AFC"),
        (5, "loc_B08"),
        (6, "loc_B14"),
        (SWITCH_DEFAULT, "loc_B20"),
    )


    label("loc_ACC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_B2C")

    label("loc_AD8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_B2C")

    label("loc_AE4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_B2C")

    label("loc_AF0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_B2C")

    label("loc_AFC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_B2C")

    label("loc_B08")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_B2C")

    label("loc_B14")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_B2C")

    label("loc_B20")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_B2C")

    label("loc_B2C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B43")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_B2C")

    label("loc_B43")

    Return()

    # Function_2_A8C end

    def Function_3_B44(): pass

    label("Function_3_B44")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_B7C"),
        (1, "loc_B88"),
        (2, "loc_B94"),
        (3, "loc_BA0"),
        (4, "loc_BAC"),
        (5, "loc_BB8"),
        (6, "loc_BC4"),
        (SWITCH_DEFAULT, "loc_BD0"),
    )


    label("loc_B7C")

    OP_A0(0xFE, 950, 0x0, 0x3)
    Jump("loc_BDC")

    label("loc_B88")

    OP_A0(0xFE, 1050, 0x0, 0x3)
    Jump("loc_BDC")

    label("loc_B94")

    OP_A0(0xFE, 1100, 0x0, 0x3)
    Jump("loc_BDC")

    label("loc_BA0")

    OP_A0(0xFE, 900, 0x0, 0x3)
    Jump("loc_BDC")

    label("loc_BAC")

    OP_A0(0xFE, 1150, 0x0, 0x3)
    Jump("loc_BDC")

    label("loc_BB8")

    OP_A0(0xFE, 850, 0x0, 0x3)
    Jump("loc_BDC")

    label("loc_BC4")

    OP_A0(0xFE, 1000, 0x0, 0x3)
    Jump("loc_BDC")

    label("loc_BD0")

    OP_A0(0xFE, 1000, 0x0, 0x3)
    Jump("loc_BDC")

    label("loc_BDC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BF3")
    OP_A0(0xFE, 1000, 0x0, 0x3)
    Jump("loc_BDC")

    label("loc_BF3")

    Return()

    # Function_3_B44 end

    def Function_4_BF4(): pass

    label("Function_4_BF4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C0A")
    SetScenarioFlags(0x150, 6)
    Jump("loc_C0D")

    label("loc_C0A")

    SetScenarioFlags(0x150, 7)

    label("loc_C0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C2F")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)

    label("loc_C2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C67")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8C)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C67")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)

    label("loc_C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x37, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C7D")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x23), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CAF")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CAF")
    SetChrPos(0x0, -95100, 19750, 184090, 135)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 14)

    label("loc_CAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_CE2")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE2")
    SetChrPos(0x0, -96240, 20000, 185900, 135)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_CE2")

    Return()

    # Function_4_BF4 end

    def Function_5_CE3(): pass

    label("Function_5_CE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 5)), scpexpr(EXPR_END)), "loc_D5A")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D23")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D55")

    label("loc_D23")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D55")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x130), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D55")

    Jump("loc_D71")

    label("loc_D5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D71")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x12F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D71")

    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_11D3")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_11D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_122A")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x12C, 0x0)
    ClearMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x16, 0x4)
    ClearMapObjFlags(0x17, 0x4)
    Jump("loc_125A")

    label("loc_122A")

    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x16, 0x4)
    SetMapObjFlags(0x17, 0x4)

    label("loc_125A")

    SetBarrier(0x0, 0x0, 0x1, 0x0, -81250, 19750, 189000, 6000, 3000, 45000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1290")
    SetBarrier(0x3, 0x0, 0x1)
    ClearMapObjFlags(0x1, 0x10)
    Jump("loc_1298")

    label("loc_1290")

    SetBarrier(0x2, 0x0, 0x1)
    OP_65(0x4, 0x1)

    label("loc_1298")

    SetBarrier(0x0, 0x1, 0x1, 0x0, -62550, 11750, 159550, 5000, 3000, 45000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12CE")
    SetBarrier(0x3, 0x1, 0x1)
    ClearMapObjFlags(0x4, 0x10)
    Jump("loc_12D6")

    label("loc_12CE")

    SetBarrier(0x2, 0x1, 0x1)
    OP_65(0x5, 0x1)

    label("loc_12D6")

    SetBarrier(0x0, 0x2, 0x1, 0x0, -62550, -250, 159550, 6000, 3000, 45000)
    ClearMapObjFlags(0x5, 0x10)
    MiniGame(0x2F, 0x8, 0x9, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_132E")
    OP_70(0x7, 0x0)
    Jump("loc_1332")

    label("loc_132E")

    OP_70(0x7, 0x1E)

    label("loc_1332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1345")
    OP_70(0x8, 0x0)
    Jump("loc_1349")

    label("loc_1345")

    OP_70(0x8, 0x1E)

    label("loc_1349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_135C")
    OP_70(0x9, 0x0)
    Jump("loc_1360")

    label("loc_135C")

    OP_70(0x9, 0x1E)

    label("loc_1360")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1373")
    OP_70(0xA, 0x0)
    Jump("loc_1377")

    label("loc_1373")

    OP_70(0xA, 0x1E)

    label("loc_1377")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_13D8")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, -101090, 6000, 56510, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x6, 0x1)

    label("loc_13D8")

    OP_65(0x7, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1424")
    PlayEffect(0x10, 0xA, 0xFF, 0x0, -131500, 20000, 73660, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x7, 0x1)

    label("loc_1424")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1447")
    SetMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xB, 0x2)
    OP_65(0xB, 0x1)
    Jump("loc_1453")

    label("loc_1447")

    SetMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xC, 0x2)

    label("loc_1453")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1471")
    ClearMapObjFlags(0xF, 0x2)
    SetMapObjFlags(0xF, 0x4)

    label("loc_1471")

    SetMapObjFlags(0x1B, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_148B")
    ClearMapObjFlags(0x1B, 0x4)

    label("loc_148B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14AF")
    ClearMapObjFlags(0x1B, 0x4)

    label("loc_14AF")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14C7")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_14C7")

    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14DF")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_14DF")

    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 4, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_152D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_150E")
    ModifyEventFlags(1, 4, 0x80)

    label("loc_150E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_152D")
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)

    label("loc_152D")

    OP_1C(0x0, 0x18, 0x0, 0x32, 0x0, 0xC, 0x0, 0x0)
    OP_1C(0x0, 0x19, 0x0, 0x32, 0x0, 0xC, 0x0, 0x0)
    OP_1C(0x0, 0x1A, 0x0, 0x32, 0x0, 0xC, 0x0, 0x0)
    Return()

    # Function_5_CE3 end

    def Function_6_154F(): pass

    label("Function_6_154F")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_164B")
    Sound(14, 0, 100, 0)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5E2, 1)"), scpexpr(EXPR_END)), "loc_15D4")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5E2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E7, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_1646")

    label("loc_15D4")

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
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1646")

    Jump("loc_1695")

    label("loc_164B")

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

    label("loc_1695")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_154F end

    def Function_7_16A1(): pass

    label("Function_7_16A1")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_179D")
    Sound(14, 0, 100, 0)
    OP_74(0x8, 0x1E)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x16, 1)"), scpexpr(EXPR_END)), "loc_1726")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x16),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E7, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_1798")

    label("loc_1726")

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
    OP_71(0x8, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1798")

    Jump("loc_17E7")

    label("loc_179D")

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

    label("loc_17E7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_16A1 end

    def Function_8_17F3(): pass

    label("Function_8_17F3")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18EF")
    Sound(14, 0, 100, 0)
    OP_74(0x9, 0x1E)
    OP_71(0x9, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x442, 1)"), scpexpr(EXPR_END)), "loc_1878")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x442),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E8, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_18EA")

    label("loc_1878")

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
    OP_71(0x9, 0x1E, 0x0, 0x0, 0x0)

    label("loc_18EA")

    Jump("loc_1939")

    label("loc_18EF")

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

    label("loc_1939")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_17F3 end

    def Function_9_1945(): pass

    label("Function_9_1945")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A41")
    Sound(14, 0, 100, 0)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x456, 1)"), scpexpr(EXPR_END)), "loc_19CA")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x456),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E8, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_1A3C")

    label("loc_19CA")

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
    OP_71(0xA, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1A3C")

    Jump("loc_1A8B")

    label("loc_1A41")

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

    label("loc_1A8B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_1945 end

    def Function_10_1A97(): pass

    label("Function_10_1A97")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1C4F")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 5)), scpexpr(EXPR_END)), "loc_1C30")
    LoadEffect(0x7, "event\\eva07_00.eff")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "It looks like something is buried.\x01",
            "Dig it out?\x07\x00\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C2B")
    ClearScenarioFlags(0x3B, 5)
    OP_65(0x6, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 5)), scpexpr(EXPR_END)), "loc_1C28")
    ClearScenarioFlags(0x39, 5)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1B4D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1B4D)
    TurnDirection(0xA, 0x0, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    PlayEffect(0x7, 0x1, 0xA, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_8D0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C23")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1C0A")
    Call(1, 5)
    Jump("loc_1C23")

    label("loc_1C0A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1C20")
    Call(1, 4)
    Jump("loc_1C23")

    label("loc_1C20")

    Call(1, 3)

    label("loc_1C23")

    Jump("loc_1C2B")

    label("loc_1C28")

    Call(1, 1)

    label("loc_1C2B")

    Jump("loc_1C46")

    label("loc_1C30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 5)), scpexpr(EXPR_END)), "loc_1C46")
    ClearScenarioFlags(0x39, 5)
    OP_65(0x6, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_1C46")

    TalkEnd(0xFF)
    Return()

    label("loc_1C4F")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 5)), scpexpr(EXPR_END)), "loc_1DDA")
    LoadEffect(0x7, "event\\eva07_00.eff")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "It looks like something is buried.\x01",
            "Dig it out?\x07\x00\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DD5")
    ClearScenarioFlags(0x3B, 5)
    OP_65(0x6, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 5)), scpexpr(EXPR_END)), "loc_1DD2")
    ClearScenarioFlags(0x39, 5)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1CF7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1CF7)
    TurnDirection(0xC, 0x0, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    PlayEffect(0x7, 0x1, 0xC, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_914", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DCD")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1DB4")
    Call(1, 5)
    Jump("loc_1DCD")

    label("loc_1DB4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1DCA")
    Call(1, 4)
    Jump("loc_1DCD")

    label("loc_1DCA")

    Call(1, 3)

    label("loc_1DCD")

    Jump("loc_1DD5")

    label("loc_1DD2")

    Call(1, 1)

    label("loc_1DD5")

    Jump("loc_1DF0")

    label("loc_1DDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 5)), scpexpr(EXPR_END)), "loc_1DF0")
    ClearScenarioFlags(0x39, 5)
    OP_65(0x6, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_1DF0")

    TalkEnd(0xFF)
    Return()

    # Function_10_1A97 end

    def Function_11_1DF5(): pass

    label("Function_11_1DF5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1FAD")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 6)), scpexpr(EXPR_END)), "loc_1F8E")
    LoadEffect(0x7, "event\\eva07_00.eff")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "It looks like something is buried.\x01",
            "Dig it out?\x07\x00\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F89")
    ClearScenarioFlags(0x3B, 6)
    OP_65(0x7, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 6)), scpexpr(EXPR_END)), "loc_1F86")
    ClearScenarioFlags(0x39, 6)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1EAB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1EAB)
    TurnDirection(0xB, 0x0, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    PlayEffect(0x7, 0x1, 0xB, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_8D0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F81")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1F68")
    Call(1, 5)
    Jump("loc_1F81")

    label("loc_1F68")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1F7E")
    Call(1, 4)
    Jump("loc_1F81")

    label("loc_1F7E")

    Call(1, 3)

    label("loc_1F81")

    Jump("loc_1F89")

    label("loc_1F86")

    Call(1, 1)

    label("loc_1F89")

    Jump("loc_1FA4")

    label("loc_1F8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 6)), scpexpr(EXPR_END)), "loc_1FA4")
    ClearScenarioFlags(0x39, 6)
    OP_65(0x7, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_1FA4")

    TalkEnd(0xFF)
    Return()

    label("loc_1FAD")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 6)), scpexpr(EXPR_END)), "loc_2138")
    LoadEffect(0x7, "event\\eva07_00.eff")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "It looks like something is buried.\x01",
            "Dig it out?\x07\x00\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2133")
    ClearScenarioFlags(0x3B, 6)
    OP_65(0x7, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 6)), scpexpr(EXPR_END)), "loc_2130")
    ClearScenarioFlags(0x39, 6)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2055():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2055)
    TurnDirection(0xD, 0x0, 0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    PlayEffect(0x7, 0x1, 0xD, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_914", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_212B")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2112")
    Call(1, 5)
    Jump("loc_212B")

    label("loc_2112")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2128")
    Call(1, 4)
    Jump("loc_212B")

    label("loc_2128")

    Call(1, 3)

    label("loc_212B")

    Jump("loc_2133")

    label("loc_2130")

    Call(1, 1)

    label("loc_2133")

    Jump("loc_214E")

    label("loc_2138")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 6)), scpexpr(EXPR_END)), "loc_214E")
    ClearScenarioFlags(0x39, 6)
    OP_65(0x7, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_214E")

    TalkEnd(0xFF)
    Return()

    # Function_11_1DF5 end

    def Function_12_2153(): pass

    label("Function_12_2153")

    Call(1, 6)
    Return()

    # Function_12_2153 end

    def Function_13_2157(): pass

    label("Function_13_2157")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2189")
    SetScenarioFlags(0x31, 2)

    label("loc_2189")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_21CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_21C9")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_21BE")
    Sound(2499, 255, 100, 0)
    Jump("loc_21C4")

    label("loc_21BE")

    Sound(3537, 255, 100, 0)

    label("loc_21C4")

    Jump("loc_21CF")

    label("loc_21C9")

    Sound(3344, 255, 100, 0)

    label("loc_21CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2482")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_2242")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2222"),
        (SWITCH_DEFAULT, "loc_2233"),
    )


    label("loc_2222")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_223D")

    label("loc_2233")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_223D")

    Jump("loc_247D")

    label("loc_2242")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_2274")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_2274")

    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_22A6"),
        (1, "loc_23AA"),
        (2, "loc_243B"),
        (SWITCH_DEFAULT, "loc_2473"),
    )


    label("loc_22A6")

    SetMapObjFrame(0xD, "light", 0x0, 0x1)
    OP_74(0xD, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_22D7")
    OP_70(0xD, 0x12C)
    OP_71(0xD, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_22E7")

    label("loc_22D7")

    OP_70(0xD, 0xF0)
    OP_71(0xD, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_22E7")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_233D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_233D")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2360")
    Sound(461, 0, 100, 0)

    label("loc_2360")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2380")
    OP_70(0xD, 0x14A)
    OP_71(0xD, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_2390")

    label("loc_2380")

    OP_70(0xD, 0x10E)
    OP_71(0xD, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_2390")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0xD, "light", 0x1, 0x1)
    OP_70(0xD, 0x0)
    Jump("loc_21CF")

    label("loc_23AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_241C")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_23DF")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_23F7")

    label("loc_23DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_23F2")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_23F7")

    label("loc_23F2")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_23F7")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2436")

    label("loc_241C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_242C")
    OP_AF(0xFB)
    Jump("loc_2436")

    label("loc_242C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2436")

    Jump("loc_247D")

    label("loc_243B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2454")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_246E")

    label("loc_2454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2464")
    OP_AF(0xFB)
    Jump("loc_246E")

    label("loc_2464")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_246E")

    Jump("loc_247D")

    label("loc_2473")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_247D")

    Jump("loc_21CF")

    label("loc_2482")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_13_2157 end

    def Function_14_2490(): pass

    label("Function_14_2490")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_24EB")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_24E0")
    Sound(2502, 255, 100, 0)
    Jump("loc_24E6")

    label("loc_24E0")

    Sound(2503, 255, 100, 0)

    label("loc_24E6")

    Jump("loc_250F")

    label("loc_24EB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2509")
    Sound(3347, 255, 100, 0)
    Jump("loc_250F")

    label("loc_2509")

    Sound(3348, 255, 100, 0)

    label("loc_250F")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_14_2490 end

    def Function_15_2524(): pass

    label("Function_15_2524")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2544")
    Call(0, 31)
    Return()

    label("loc_2544")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The gate is firmly shut.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_15_2524 end

    def Function_16_2570(): pass

    label("Function_16_2570")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The gate is firmly shut.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_16_2570 end

    def Function_17_259C(): pass

    label("Function_17_259C")

    OP_E2(0x3)
    SetMapObjFlags(0x17, 0x1000)
    SetMapObjFlags(0xC, 0x1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 5)), scpexpr(EXPR_END)), "loc_25BB")
    Call(0, 20)
    Jump("loc_25CF")

    label("loc_25BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 4)), scpexpr(EXPR_END)), "loc_25CC")
    Call(0, 19)
    Jump("loc_25CF")

    label("loc_25CC")

    Call(0, 18)

    label("loc_25CF")

    OP_E2(0x2)
    ClearMapObjFlags(0x17, 0x1000)
    ClearMapObjFlags(0xC, 0x1000)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    Return()

    # Function_17_259C end

    def Function_18_25E8(): pass

    label("Function_18_25E8")

    EventBegin(0x0)
    Call(0, 22)
    Call(0, 21)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2BF4")

    AnonymousTalk(
        0x105,
        (
            "#10403F"Ouroboros"...\x01",
            "It seems they're guarding this place.\x02\x03",
            "#10401FWhat're standing in front of the door\x01",
            "are Society's heavy archaisms for base\x01",
            "defense called "Leor Gun-EZ".\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x103,
        (
            "#00203FThey seem armed with\x01",
            "a lot of weapons...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_273B")

    AnonymousTalk(
        0x109,
        (
            "#10101FYes, probably large firepower\x01",
            "types for base defense.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_273B")


    AnonymousTalk(
        0x104,
        (
            "#00301FGettin' close to them nonchalantly\x01",
            "is probably a suicide act.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 23)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00003F#6P...At any rate, it would be\x01",
            "better to pull out for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#6PEven so, Wazy, it seems\x01",
            "you're very knowledgeable\x01",
            "about the "Society", huh?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_293F")

    ChrTalk(
        0x105,
        (
            "#10404F#12PHu hu...\x01",
            "Well, somewhat, I guess?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#6P#3CThe "Knights" and the "Society" are\x01",
            "recorded to have confronted each other\x01",
            "many times in the shadows of history.\x02\x03",
            "Even among them, knowing their\x01",
            "opponents is the most important thing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A4A")

    label("loc_293F")


    ChrTalk(
        0x105,
        (
            "#10404F#12PHu hu...\x01",
            "Well, somewhat, I guess?\x02\x03",
            "#10400FThe "Knights" and the "Society" are\x01",
            "recorded to have confronted each other\x01",
            "many times in the shadows of history.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PI see...If the circumstances are like that,\x01",
            "knowing your opponents is important.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A4A")


    ChrTalk(
        0x105,
        (
            "#10406F#12PWell, since the "Knights" and the "Society"\x01",
            "circumstances are always changing,\x01",
            "they're frankly into a vicious circle.\x02\x03",
            "#10402FOops, I wonder if Abbass would get angry at\x01",
            "me for talking carelessly about such things?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B7B")

    ChrTalk(
        0x109,
        "#10106F#6PG-Geez, Wazy...\x02",
    )

    CloseMessageWindow()

    label("loc_2B7B")


    ChrTalk(
        0x106,
        (
            "#10709F#6PA-Ahaha...\x01",
            "Mr. Abbas seems to have it hard too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6P...Let's walk away from here for now.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BF4")

    label("loc_2BF4")

    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2C0E")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_2C0E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2C27")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_2C27")

    SetChrPos(0x0, -135390, 20000, 123030, 180)
    SetScenarioFlags(0x1AF, 5)
    EventEnd(0x5)
    Return()

    # Function_18_25E8 end

    def Function_19_2C3E(): pass

    label("Function_19_2C3E")

    EventBegin(0x0)
    Call(0, 22)
    Call(0, 21)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2D2F")

    AnonymousTalk(
        0x105,
        (
            "#10403F"Ouroboros" is here too, eh...?\x02\x03",
            "#10401FWhat're standing in front of the door\x01",
            "are Society's heavy archaisms for base\x01",
            "defense called "Leor Gun-EZ".\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x103,
        (
            "#00203FThey seem armed with\x01",
            "a lot of weapons...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DA4")

    label("loc_2D2F")


    AnonymousTalk(
        0x106,
        "#10701FOuroboros is here too...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x103,
        (
            "#00203FThe archaisms in front of\x01",
            "the door seem to be\x01",
            "very heavily armed...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DA4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2DF6")

    AnonymousTalk(
        0x109,
        (
            "#10101FYes, probably large firepower\x01",
            "types for base defense.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DF6")


    AnonymousTalk(
        0x104,
        (
            "#00301F#6PGettin' close to them nonchalantly\x01",
            "is probably a suicide act.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 23)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2ED1")

    ChrTalk(
        0x101,
        (
            "#00003F#6P...As suspected, it's better\x01",
            "we don't act recklessly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10701F#6PYes, let's step away for now.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F37")

    label("loc_2ED1")


    ChrTalk(
        0x101,
        (
            "#00003F#6P...As suspected, it's better\x01",
            "we don't act recklessly.\x02\x03",
            "#00001FLet's step away for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F37")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F67")

    ChrTalk(
        0x107,
        "#01200F#6P#3CHm, let's go.\x02",
    )

    CloseMessageWindow()

    label("loc_2F67")

    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2F81")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_2F81")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2F9A")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_2F9A")

    SetChrPos(0x0, -135390, 20000, 123030, 180)
    SetScenarioFlags(0x1AF, 5)
    EventEnd(0x5)
    Return()

    # Function_19_2C3E end

    def Function_20_2FB1(): pass

    label("Function_20_2FB1")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FIt seems that the "Society"\x01",
            "is guarding up ahead.\x02\x03",
            "#00003F...Now it would seem\x01",
            "better to withdraw.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -135390, 20000, 123030, 180)
    EventEnd(0x4)
    Return()

    # Function_20_2FB1 end

    def Function_21_3037(): pass

    label("Function_21_3037")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3079")
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_306E():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_306E)
    Sleep(50)

    label("loc_3079")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30BB")
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_30B0():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_30B0)
    Sleep(50)

    label("loc_30BB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30FD")
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_30F2():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_30F2)
    Sleep(50)

    label("loc_30FD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3146")
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x104, 0x8, 500)

    def lambda_313B():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_313B)
    Sleep(50)

    label("loc_3146")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_318F")
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x105, 0x8, 500)

    def lambda_3184():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3184)
    Sleep(50)

    label("loc_318F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_31D8")
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x106, 0x8, 500)

    def lambda_31CD():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_31CD)
    Sleep(50)

    label("loc_31D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3221")
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x109, 0x8, 500)

    def lambda_3216():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3216)
    Sleep(50)

    label("loc_3221")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_326A")
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x107, 0x8, 500)

    def lambda_325F():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_325F)
    Sleep(50)

    label("loc_326A")

    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FThose are...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-115530, 21850, 135930, 0)
    MoveCamera(358, 22, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(25000, 0)
    OP_68(-88910, 21850, 177310, 7000)
    MoveCamera(6, 14, 0, 7000)
    Sleep(8000)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_32FA")
    SetChrPos(0x0, -133380, 20000, 124530, 39)

    label("loc_32FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_331A")
    SetChrPos(0x1, -134310, 20000, 125180, 39)

    label("loc_331A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_333A")
    SetChrPos(0x2, -132840, 20000, 123600, 39)

    label("loc_333A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_335A")
    SetChrPos(0x3, -132290, 20000, 122620, 39)

    label("loc_335A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3384")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x4, -134600, 20000, 123840, 39)

    label("loc_3384")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_33AE")
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x5, -134300, 20000, 122570, 39)

    label("loc_33AE")

    Return()

    # Function_21_3037 end

    def Function_22_33AF(): pass

    label("Function_22_33AF")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_33CF")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_33CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_33E4")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_33E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_33F9")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_33F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_340E")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_340E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3423")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3423")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3438")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3438")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_344D")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_344D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3462")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3462")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Return()

    # Function_22_33AF end

    def Function_23_346D(): pass

    label("Function_23_346D")

    Fade(500)
    OP_68(-134300, 21620, 122570, 0)
    MoveCamera(39, 6, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(17870, 0)
    OP_0D()
    Return()

    # Function_23_346D end

    def Function_24_34A2(): pass

    label("Function_24_34A2")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00056.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00156.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00256.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00356.itc", 0x25)
    SoundLoad(959)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3515")
    LoadChrToIndex("chr/ch02950.itc", 0x26)
    LoadChrToIndex("chr/ch0295F.itc", 0x27)

    label("loc_3515")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3533")
    LoadChrToIndex("chr/ch03150.itc", 0x26)
    LoadChrToIndex("chr/ch0315F.itc", 0x27)

    label("loc_3533")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3551")
    LoadChrToIndex("chr/ch03250.itc", 0x26)
    LoadChrToIndex("chr/ch0325A.itc", 0x27)

    label("loc_3551")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_356F")
    LoadChrToIndex("chr/ch02950.itc", 0x28)
    LoadChrToIndex("chr/ch0295F.itc", 0x29)

    label("loc_356F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_358D")
    LoadChrToIndex("chr/ch03150.itc", 0x28)
    LoadChrToIndex("chr/ch0315F.itc", 0x29)

    label("loc_358D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_35AB")
    LoadChrToIndex("chr/ch03250.itc", 0x28)
    LoadChrToIndex("chr/ch0325A.itc", 0x29)

    label("loc_35AB")

    LoadEffect(0x0, "event\\ev10002.eff")
    SoundLoad(3720)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -91820, 19750, 178310, 45)
    SetChrPos(0x102, -92990, 19750, 178120, 45)
    SetChrPos(0x103, -92650, 19750, 176650, 45)
    SetChrPos(0x104, -91640, 19750, 176190, 45)
    SetChrPos(0xF4, -94120, 19750, 177940, 45)
    SetChrPos(0xF5, -93700, 19750, 176110, 45)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -88300, 19750, 186370, 235)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -83700, 19750, 181770, 235)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-82750, 22750, 187250, 0)
    OP_68(-87750, 22550, 182250, 6000)
    MoveCamera(9, 21, 0, 0)
    MoveCamera(9, 15, 0, 6000)
    OP_6E(700, 0)
    SetCameraDistance(21000, 0)
    SetCameraDistance(24000, 6000)
    FadeToBright(1000, 0)
    Sleep(2500)

    def lambda_373E():
        OP_9B(0x0, 0x101, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_373E)
    Sleep(50)

    def lambda_3756():
        OP_9B(0x0, 0x102, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3756)
    Sleep(50)

    def lambda_376E():
        OP_9B(0x0, 0x103, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_376E)
    Sleep(50)

    def lambda_3786():
        OP_9B(0x0, 0x104, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3786)
    Sleep(50)

    def lambda_379E():
        OP_9B(0x0, 0xF4, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_379E)
    Sleep(50)

    def lambda_37B6():
        OP_9B(0x0, 0xF5, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_37B6)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(-87750, 21000, 182250, 0)
    MoveCamera(9, 15, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14650, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3857")

    ChrTalk(
        0x105,
        "#10401F#6PThe "Ouroboros" crest, eh...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_387F")

    label("loc_3857")


    ChrTalk(
        0x106,
        "#10701F#6PThe "Ouroboros" crest...\x02",
    )

    CloseMessageWindow()

    label("loc_387F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 5)), scpexpr(EXPR_END)), "loc_3920")

    ChrTalk(
        0x103,
        (
            "#00201F#6PIt appears it has been sealed\x01",
            "with some kind of power...\x02\x03",
            "#00203FBy the way, where did the archaisms\x01",
            "that were guarding here go...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3968")

    label("loc_3920")


    ChrTalk(
        0x103,
        (
            "#00201F#6PIt appears it has been sealed\x01",
            "with some kind of power...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3968")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_39BA")
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10107F#6PEveryone, that...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_39EF")

    label("loc_39BA")

    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x106,
        "#10707F#6PThat's...!\x02",
    )

    CloseMessageWindow()

    label("loc_39EF")

    OP_68(-87750, 30600, 182250, 4000)
    MoveCamera(45, -10, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(9350, 4000)
    Sleep(2000)
    Sound(944, 0, 100, 0)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        "#00101FThat big bell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FIn any case, we just have to\x01",
            "stop that thing's ringin', huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, 60, -1, -1)
    SetChrName("Boy's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3720V#30W#25AUhuhu, exactly.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x101,
        "#00013F!!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(-80750, 22750, 189250, 0)
    MoveCamera(45, 39, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(21000, 0)
    SetCameraDistance(19000, 10000)
    OP_0D()
    SetMessageWindowPos(-1, 20, -1, -1)
    SetChrName("Boy's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "My oh my, if you've come here it means\x01",
            "you've heard about it from the Meister.\x02\x03",
            "Did the Gordias-class final\x01",
            "models and the Arc-en-ciel\x01",
            "raid angered him, perhaps?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(-87750, 21000, 182250, 0)
    MoveCamera(18, 15, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14650, 0)
    OP_0D()

    ChrTalk(
        0x104,
        "#00304F#6PYes, quite a lot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F#6PWell, you reap what you saw.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(280, 20, -1, -1)
    SetChrName("Boy's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Uhhm, I have a feeling that I was dragged\x01",
            "into this by the Doctor and the jaegers, but...\x02\x03",
            "Uh uh, oh, well.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0xBB8)
    Fade(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_82(0x64, 0xC8, 0xBB8, 0x2EE)
    SetCameraDistance(15650, 500)
    Sound(959, 2, 100, 0)
    Sound(817, 0, 100, 0)
    Sound(202, 0, 100, 0)
    PlayEffect(0x0, 0x0, 0x8, 0x5, 0, 100, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x9, 0x5, 0, 100, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x79)
    OP_0D()
    CancelBlur(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(350)
    OP_68(-88250, 21000, 181750, 500)
    SetChrChipByIndex(0xF5, 0x29)
    SetChrSubChip(0xF5, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_3EA8():
        OP_9C(0xFE, 0xFFFFFC18, 0x0, 0xFFFFFC18, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_3EA8)
    Sleep(50)
    SetChrChipByIndex(0xF4, 0x27)
    SetChrSubChip(0xF4, 0x0)

    def lambda_3ED0():
        OP_9C(0xFE, 0xFFFFFC18, 0x0, 0xFFFFFC18, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_3ED0)
    Sleep(50)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)

    def lambda_3EF8():
        OP_9C(0xFE, 0xFFFFFC18, 0x0, 0xFFFFFC18, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3EF8)
    Sleep(50)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)

    def lambda_3F20():
        OP_9C(0xFE, 0xFFFFFC18, 0x0, 0xFFFFFC18, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3F20)
    Sleep(50)
    SetChrChipByIndex(0x102, 0x21)
    SetChrSubChip(0x102, 0x2)

    def lambda_3F48():
        OP_9C(0xFE, 0xFFFFFC18, 0x0, 0xFFFFFC18, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3F48)
    Sleep(50)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x2)

    def lambda_3F70():
        OP_9C(0xFE, 0xFFFFFC18, 0x0, 0xFFFFFC18, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F70)
    Sleep(50)
    WaitChrThread(0xF5, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3FA5")
    Sound(540, 0, 50, 0)

    label("loc_3FA5")

    SetChrChipByIndex(0xF5, 0x28)
    SetChrSubChip(0xF5, 0x0)
    WaitChrThread(0xF4, 1)
    SetChrChipByIndex(0xF4, 0x26)
    SetChrSubChip(0xF4, 0x0)
    WaitChrThread(0x103, 1)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    WaitChrThread(0x104, 1)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    WaitChrThread(0x102, 1)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    WaitChrThread(0x101, 1)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_6F(0x79)
    OP_0D()
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_82(0x64, 0xC8, 0xBB8, 0x2EE)
    StopSound(959, 1000, 100)
    Sound(902, 0, 100, 0)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)

    def lambda_402C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_402C)

    def lambda_403D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_403D)
    WaitChrThread(0x8, 2)
    WaitChrThread(0x9, 2)
    CancelBlur(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7451", 0)
    SetMessageWindowPos(280, 20, -1, -1)
    SetChrName("Boy's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "──If you've come here, it means you're \x01",
            "prepared to a certain degree, right?\x02\x03",
            "Uhuhu, I'll enjoy this.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 5)), scpexpr(EXPR_END)), "loc_412F")

    ChrTalk(
        0x101,
        (
            "#00007F#6PKh...\x01",
            "The things we saw before!?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_421A")

    label("loc_412F")


    ChrTalk(
        0x101,
        "#00007F#6PKh...archaisms!?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_41BF")

    ChrTalk(
        0x105,
        (
            "#10410F#6P"Leor Gun-EZ"!\x02\x03",
            "#10407FThey're Society heavy archaisms\x01",
            "for base defense...!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_421A")

    label("loc_41BF")


    ChrTalk(
        0x109,
        (
            "#10107F#6PMany weapons confirmed!\x02\x03",
            "Probably large firepower\x01",
            "ones for base defense...!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_421A")


    ChrTalk(
        0x104,
        "#00307F#6PAnyway, we're gonna scrap 'em!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4271")

    ChrTalk(
        0x106,
        "#10707F#6PYes!\x02",
    )

    CloseMessageWindow()
    Jump("loc_428C")

    label("loc_4271")


    ChrTalk(
        0x109,
        "#10107F#6PRoger that!\x02",
    )

    CloseMessageWindow()

    label("loc_428C")

    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(10650, 500)

    def lambda_42A6():
        OP_9B(0x1, 0xFE, 0xFFE2, 0x9C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_42A6)

    def lambda_42BB():
        OP_9B(0x1, 0xFE, 0x1E, 0x9C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_42BB)
    Sleep(500)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    OP_24(0x3BF)
    Battle("BattleInfo_958", 0x0, 0x0, 0x100, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 25)
    Return()

    # Function_24_34A2 end

    def Function_25_42F7(): pass

    label("Function_25_42F7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    SoundLoad(155)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4338")
    LoadChrToIndex("chr/ch02950.itc", 0x22)

    label("loc_4338")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4350")
    LoadChrToIndex("chr/ch03150.itc", 0x22)

    label("loc_4350")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4368")
    LoadChrToIndex("chr/ch03250.itc", 0x22)

    label("loc_4368")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4380")
    LoadChrToIndex("chr/ch02950.itc", 0x23)

    label("loc_4380")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4398")
    LoadChrToIndex("chr/ch03150.itc", 0x23)

    label("loc_4398")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_43B0")
    LoadChrToIndex("chr/ch03250.itc", 0x23)

    label("loc_43B0")

    LoadEffect(0x0, "event/ev17029.eff")
    LoadEffect(0x1, "event\\ev14002.eff")
    SoundLoad(3721)
    SoundLoad(3722)
    SoundLoad(3723)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -89280, 19750, 180850, 45)
    SetChrPos(0x102, -90450, 19750, 180660, 45)
    SetChrPos(0x103, -90110, 19750, 179190, 45)
    SetChrPos(0x104, -89100, 19750, 178730, 45)
    SetChrPos(0xF4, -91580, 19750, 180480, 45)
    SetChrPos(0xF5, -91160, 19750, 178650, 45)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x22)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x23)
    SetChrSubChip(0xF5, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -88300, 19750, 186370, 235)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -83700, 19750, 181770, 235)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    BeginChrThread(0xF, 1, 0, 27)
    PlayEffect(0x0, 0x0, 0x8, 0x5, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x9, 0x5, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_4552():

        label("loc_4552")

        OP_A6(0xFE, 0x32, 0x32, 0x1F4, 0xBB8)
        Yield()
        Jump("loc_4552")

    QueueWorkItem2(0x8, 3, lambda_4552)

    def lambda_4570():

        label("loc_4570")

        OP_A6(0xFE, 0x32, 0x32, 0x1F4, 0xBB8)
        Yield()
        Jump("loc_4570")

    QueueWorkItem2(0x9, 3, lambda_4570)
    OP_68(-86250, 21000, 183750, 0)
    MoveCamera(6, 18, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12000, 0)
    FadeToBright(1000, 0)
    OP_68(-86250, 21000, 183750, 3000)
    MoveCamera(0, 30, 0, 3000)
    SetCameraDistance(14000, 3000)
    OP_6F(0x79)
    OP_0D()
    SetCameraDistance(22000, 500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_82(0x12C, 0x12C, 0x1388, 0x7D0)

    def lambda_4613():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_4613)
    Sound(200, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopEffect(0x0, 0x2)
    Sleep(100)
    Sound(833, 0, 50, 0)

    def lambda_466D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_466D)
    PlayEffect(0x1, 0xFF, 0x9, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopEffect(0x1, 0x2)
    CancelBlur(2500)
    WaitChrThread(0x8, 2)
    WaitChrThread(0x9, 2)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x9, 0x3)
    OP_6F(0x79)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Sleep(1800)
    Fade(1000)
    OP_68(-81300, 23000, 188600, 0)
    MoveCamera(45, 18, 0, 0)
    MoveCamera(45, 15, 0, 3000)
    OP_6E(700, 0)
    SetCameraDistance(19650, 0)
    SetCameraDistance(17650, 3000)
    OP_6F(0x79)
    OP_0D()
    Sound(202, 0, 100, 0)
    Sound(223, 0, 100, 0)
    OP_75(0xF, 0x1, 0x3E8)
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 26)
    Sleep(400)
    OP_68(-89300, 22000, 180600, 3000)
    MoveCamera(45, 8, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(13550, 3000)
    Sleep(2000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(280, 20, -1, -1)
    SetChrName("Boy's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3721V#30W#25AUhuhu, very well done.\x02\x03",
            "#3722V#30W#32AThen, feel free\x01",
            "to come inside.\x02\x03",
            "#3723V#30W#27AI'll be waiting in front of the bell㈱\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xF4)
    OP_64(0xF5)

    ChrTalk(
        0x102,
        "#00108F#5P...What do you think?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PNo matter what I think, it seems\x01",
            "he's got some tricks prepared...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4A1D")

    ChrTalk(
        0x105,
        (
            "#10403F#5PAnd also, it's very likely\x01",
            "they're some nasty ones.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A5F")

    label("loc_4A1D")


    ChrTalk(
        0x106,
        (
            "#10703F#5PYes, and it's very likely\x01",
            "they're some nasty ones.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A5F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4ACA")

    ChrTalk(
        0x109,
        (
            "#10101F#5PBut still, I think that the only\x01",
            "thing we can do is to step inside...!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AFB")

    label("loc_4ACA")


    ChrTalk(
        0x106,
        (
            "#10701F#5PEven so, we can\x01",
            "only step inside.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AFB")


    ChrTalk(
        0x104,
        (
            "#00307F#11PYeah.\x01",
            "Let's brace ourselves.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapObjFlags(0xF, 0x2)
    SetMapObjFlags(0xF, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0xFF)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0xFF)
    SetChrSubChip(0xF5, 0x0)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_37()
    SetChrPos(0x0, -89300, 19750, 180600, 45)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A4, 3)
    OP_29(0xB0, 0x1, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    ClearScenarioFlags(0x150, 7)
    SetBarrier(0x3, 0x1, 0x1)
    ClearMapObjFlags(0x4, 0x10)
    OP_66(0x5, 0x1)
    OP_24(0x9B)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_25_42F7 end

    def Function_26_4BCD(): pass

    label("Function_26_4BCD")

    Sound(116, 0, 100, 0)
    Sound(155, 2, 100, 0)
    OP_82(0x32, 0x32, 0xBB8, 0xBB8)
    ClearMapObjFlags(0x1, 0x10)
    OP_74(0x1, 0x5)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x1)
    OP_24(0x9B)
    Sound(149, 0, 80, 0)
    OP_74(0x1, 0x1E)
    Return()

    # Function_26_4BCD end

    def Function_27_4C11(): pass

    label("Function_27_4C11")

    Sound(203, 0, 60, 0)
    Sleep(900)
    Sound(203, 0, 70, 0)
    Sleep(900)
    Sound(203, 0, 60, 0)
    Return()

    # Function_27_4C11 end

    def Function_28_4C2A(): pass

    label("Function_28_4C2A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_4C3A")
    Call(0, 30)
    Return()

    label("loc_4C3A")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_E2(0x3)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04400.itp")
    SetChrPos(0x101, -136050, 20000, 132320, 45)
    SetChrPos(0x102, -137070, 20000, 133060, 45)
    SetChrPos(0x103, -135790, 20000, 131260, 45)
    SetChrPos(0x104, -137600, 20000, 131410, 45)
    SetChrPos(0x109, -138640, 20000, 131920, 45)
    SetChrPos(0x105, -137150, 20000, 130120, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xE, 0xFF)
    OP_68(-62530, 30850, 175200, 0)
    MoveCamera(31, -2, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(81900, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(-83430, 30850, 189890, 10000)
    PlaceName2(340, 40, "c_plac29", 0x0, 6000)
    OP_6F(0x1)
    OP_68(-126570, 23100, 136030, 5000)
    MoveCamera(28, -1, 0, 5000)
    OP_6E(510, 5000)
    SetCameraDistance(24080, 5000)
    OP_6F(0x79)

    NpcTalk(
        0xE,
        "Woman in Nun's Clothes",
        (
            "#04400F"──it was rang\x01",
            "by that sinner."\x02\x03",
            ""The sinister sounds that echoed,\x01",
            "announced the beginning of the era of chaos..."\x02\x03",
            "#04403F──From the Book of Rader opening verse,\x01",
            ""The Awakening Sounds"...\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(160, 140, -1, -1)

    AnonymousTalk(
        0x101,
        "#00005F(Oh, that person is...)\x02",
    )

    CloseMessageWindow()
    OP_5A()

    AnonymousTalk(
        0x102,
        "#00105F...M-Miss Ries!?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(1000)
    OP_68(-136960, 22000, 130690, 0)
    MoveCamera(20, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(15660, 0)
    OP_0D()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xE, 0xE1, 0x1F4)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xE,
        (
            "You all are...the Special\x01",
            "Support Section, right?\x02",
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
        0x105,
        "#12P#10302FHu hu, long time no see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00205FUhhm, who is she...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FAh, yes...\x01",
            "She's a Sister of the Church\x01",
            "who we just met some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P#04404FMy name is Ries Argent.\x01",
            "Nice to meet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FAnyway, what's a Sister of the\x01",
            "Church doin' in such a place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105FR-Right!\x02\x03",
            "#10106FThis place was sealed\x01",
            "off by the CGF and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P#04403FYes, today I went on a business\x01",
            "trip to the Mining Town area, but...\x02\x03",
            "#04401FActually, I could hear "sounds"\x01",
            "coming from here since before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FSounds...?\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Sound(827, 0, 60, 0)
    Sleep(500)
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
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#6P#00301FHey Lloyd, aren't these...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FYeah...\x01",
            "It seems that the "bell" is ringing.\x02\x03",
            "#00001FTio, can you sense those presences inside?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203F...Faintly, but...\x02\x03",
            "#00201FIt appears that the previous presence of\x01",
            "the "three higher elements" is returning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FN-No way...\x02\x03",
            "#00101FDoes it mean that someone has\x01",
            "activated that bell again!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10303FHmm...\x02\x03",
            "#10302FI presume this is the site of\x01",
            "the "ghost disturbances", eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P#04405FGhost...?\x02\x03",
            "#04400FExcuse me, could you tell\x01",
            "me the details if possible?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00006FY-Yes, actually...\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained about the time\x01",
            "they had investigated the place.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xE,
        (
            "#11P#04403F...I understand.\x01",
            "So that's what happened.\x02\x03",
            "#04408FA profoundly mysterious ruin where\x01",
            "the three higher elements are at work...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xE)

    ChrTalk(
        0x102,
        "#6P#00105F...Miss Ries?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P#04403F...No, it's nothing.\x02\x03",
            "#04400FIf that's the case, then it\x01",
            "seems I need to immediately\x01",
            "stop that "bell" or what it is.\x02\x03",
            "#04403FAnd so, everyone, see you later.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_56A0():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_56A0)
    OP_68(-134870, 22200, 129860, 3500)
    MoveCamera(6, 13, 0, 3500)
    OP_6E(510, 3500)
    SetCameraDistance(14600, 3500)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#6P#00005FHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5P#04403F...Oopsy daisy.\x02",
    )

    CloseMessageWindow()
    Fade(500)
    Sound(802, 0, 100, 0)
    SetChrPos(0xE, -131490, 20000, 137100, 55)
    OP_0D()
    Sound(30, 0, 100, 0)

    def lambda_5735():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5735)
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
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#6P#10111FW-Wait, Miss Ries!?\x01",
            "What in the world are you...\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xE, 1)
    OP_93(0xE, 0xE1, 0x1F4)

    ChrTalk(
        0xE,
        (
            "#11P#04400FWell, I'm thinking to go\x01",
            "stop that bell or what it is.\x02\x03",
            "#04403F...Even appeasing the souls that can't go\x01",
            "to heaven is the role of a clergyman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FBut still, you know...\x02\x03",
            "#00301F...Hey, Lloyd.\x01",
            "Wouldn't it be better if\x01",
            "we took care of this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FRight.\x02\x03",
            "#00200FIf the three higher elements are\x01",
            "at work, it's highly likely those\x01",
            ""demons" are wandering about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FYeah, indeed... It's too dangerous\x01",
            "for a civilian to walk in there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FE-Ehm, but in her case...\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    OP_64(0xE)

    def lambda_5AEF():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5AEF)
    Sleep(50)

    def lambda_5AFF():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5AFF)
    Sleep(50)

    def lambda_5B0F():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5B0F)
    Sleep(50)

    def lambda_5B1F():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5B1F)
    Sleep(50)

    def lambda_5B2F():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5B2F)
    Sleep(300)

    ChrTalk(
        0x101,
        "#11P#00005F...Is something wrong, Elie?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#6P#00103F...N-No.\x01",
            "You're right, it's true that's dangerous.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xE, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#6P#00100FMiss Ries, could you please\x01",
            "leave this place to us?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5C05():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5C05)
    Sleep(50)

    def lambda_5C15():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5C15)
    Sleep(50)

    def lambda_5C25():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5C25)
    Sleep(50)

    def lambda_5C35():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5C35)
    Sleep(50)

    def lambda_5C45():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5C45)
    Sleep(300)

    ChrTalk(
        0xE,
        (
            "#11P#04403F...Then...\x02\x03",
            "#04401FBy all means, could you\x01",
            "let me accompany you?\x02\x03",
            "Since I have more or less\x01",
            "knowledge about Thaumaturgy,\x01",
            "I think I won't hindrance you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#N#10309FUh uh, what a pretty stubborn lady.\x02\x03",
            "#10300FWhat do we do?\x01",
            "It seems she has no intention\x01",
            "to give up at all about this.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#6P#00003F...It can't be helped.\x01",
            "In this case, she'll\x01",
            "accompany us.\x02\x03",
            "#00000FWe have investigated this place before,\x01",
            "so we should make it in a way or another.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00000FThat said...\x01",
            "Elie, will you be fine?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#6P#00113FE-Enough.\x01",
            "You don't need to worry.\x02\x03",
            "#00111FIt's a place I've entered in once already,\x01",
            "if I just prepare well mentally...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00012F(That means you\x01",
            "aren't fine at all...)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#6P#00004FA-At any rate, Miss Ries,\x01",
            "are you okay with this too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P#04400F...Yes, understood.\x01",
            "It is nice working with you.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [The Temple of Moon Investigation]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Sister Ries has joined as an escorted character.\x01",
            "If her HP becomes 0, it will be Game Over.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddParty(0x8C, 0xFF, 0xFF)
    SetChrFlags(0xE, 0x80)
    OP_37()
    OP_CC(0x1, 0xFF, 0x0)
    SetChrPos(0x0, -124480, 19000, 147110, 55)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_29(0x7C, 0x4, 0x2)
    OP_29(0x7C, 0x1, 0x0)
    ClearScenarioFlags(0x150, 4)
    SetBarrier(0x3, 0x0, 0x1)
    ClearMapObjFlags(0x1, 0x10)
    OP_66(0x4, 0x1)
    ModifyEventFlags(0, 4, 0x80)
    OP_69(0xFF, 0x0)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_28_4C2A end

    def Function_29_60FE(): pass

    label("Function_29_60FE")

    EventBegin(0x0)
    Fade(500)
    OP_E2(0x3)
    OP_68(-130080, 21250, 139610, 0)
    MoveCamera(19, 28, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18810, 0)
    SetChrPos(0x101, -129729, 19750, 140230, 223)
    SetChrPos(0x102, -128590, 19750, 139960, 223)
    SetChrPos(0x103, -129550, 19710, 141680, 223)
    SetChrPos(0x104, -128229, 19590, 141260, 223)
    SetChrPos(0x109, -127000, 19450, 141150, 223)
    SetChrPos(0x105, -128440, 19430, 142730, 223)
    OP_4B(0xE, 0xFF)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -131050, 20000, 138750, 55)
    RemoveParty(0x8C, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6469")

    ChrTalk(
        0xE,
        "#6P#04405FAre we quitting the "Temple" investigation?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00000FNo, I was only thinking to\x01",
            "prepare a little somewhere else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#6P#04403FIn that case, I will stay here on watch\x01",
            "so that people don't enter inside.\x02\x03",
            "#04400FPlease prepare well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00005FUhhm, if possible, I'd\x01",
            "like for Miss Ries to\x01",
            "come along too...\x02\x03",
            "#00003FAs you can expect, we\x01",
            "can't leave you alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#6P#04403F...No.\x01",
            "This is my job.\x02\x03",
            "#04400FIn case, I could even\x01",
            "investigate alone...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006F...Please don't do that.\x02\x03",
            "#00001Fwe'll come back later,\x01",
            "so please don't enter\x01",
            "inside alone by all means.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#6P#04403F...I understand.\x01",
            "I will wait for you.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x157, 5)
    Jump("loc_653B")

    label("loc_6469")


    ChrTalk(
        0xE,
        "#6P#04400FAre we quitting the "Temple" investigation?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00000FWe'll go prepare for a little while.\x02\x03",
            "Miss Ries, I'm sorry\x01",
            "but please wait here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#6P#04403F...I understand.\x01",
            "I will wait for you.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_653B")

    Fade(500)
    SetChrPos(0xE, -133420, 20000, 135100, 55)
    OP_4C(0xE, 0xFF)
    OP_37()
    SetChrPos(0x0, -135420, 20000, 126370, 190)
    OP_68(-135420, 23500, 126370, 0)
    MoveCamera(45, 0, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(25000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    OP_E2(0x2)
    OP_0D()
    OP_29(0x7C, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_29_60FE end

    def Function_30_65B9(): pass

    label("Function_30_65B9")

    EventBegin(0x0)
    Fade(500)
    OP_E2(0x3)
    OP_68(-136960, 22000, 130690, 0)
    MoveCamera(20, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(15660, 0)
    SetChrPos(0x101, -136050, 20000, 132320, 45)
    SetChrPos(0x102, -137070, 20000, 133060, 45)
    SetChrPos(0x103, -135790, 20000, 131260, 45)
    SetChrPos(0x104, -137600, 20000, 131410, 45)
    SetChrPos(0x109, -138640, 20000, 131920, 45)
    SetChrPos(0x105, -137150, 20000, 130120, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xE, 0xFF)
    OP_93(0xE, 0xE1, 0x0)
    OP_0D()

    ChrTalk(
        0xE,
        (
            "#11P#04400FI have been waiting for you.\x02\x03",
            "#04403FThen, let's resume the investigation.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    AddParty(0x8C, 0xFF, 0xFF)
    SetChrFlags(0xE, 0x80)
    OP_37()
    SetChrPos(0x0, -124480, 19000, 147110, 55)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    OP_E2(0x2)
    OP_29(0x7C, 0x2, 0x1)
    EventEnd(0x5)
    Return()

    # Function_30_65B9 end

    def Function_31_671B(): pass

    label("Function_31_671B")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The gate is firmly shut.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00005F...It seems it's shut.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18D,
        "#04400FIt would be better to look for a different entrance.\x02",
    )

    CloseMessageWindow()
    OP_29(0x7C, 0x1, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_31_671B end

    def Function_32_67B1(): pass

    label("Function_32_67B1")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※　Authorised Personnel Only    ※\x01",
            "※　　　　Crossbell CGF　　　  ※\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_32_67B1 end

    SaveToFile()

Try(main)
