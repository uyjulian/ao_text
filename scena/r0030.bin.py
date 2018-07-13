from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r0030.bin",                # FileName
        "r0030",                    # MapName
        "r0030",                    # Location
        0x005E,                     # MapIndex
        "ed7204",
        0x00000000,                 # Flags
        ("r0030", "r0000_1", "", "", "", ""),   # include
        0x04,                       # PlaceNameNumber
        0x03,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 94, 0, 3, 0, 4],
    )

    BuildStringList((
        "r0030",                  # 0
        "バス",                   # 1
        "メタルソーサー",         # 2
        "メタルソーサー",         # 3
        "サベージホーン",         # 4
        "サベージホーン",         # 5
        "グラスドローメ",         # 6
        "Cryptid",                # 7
        "装甲車01",               # 8
        "装甲車02",               # 9
        "装甲車03",               # 10
        "SE制御",                 # 11
        "br0000",                 # 12
        "br0000",                 # 13
        "br0000",                 # 14
        "br0000",                 # 15
        "br0000",                 # 16
        "br0000",                 # 17
        "br0000",                 # 18
        "br0000",                 # 19
        "br0000",                 # 20
        "To Crossbell City",      # 21
        "To Tangram Gate",        # 22
        "To Armorica Village",    # 23
    ))

    ATBonus("ATBonus_674", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_694", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_3964", 7,   4,   5,   0,   0,   5,   0)
    Sepith("Sepith_397C", 7,   0,   3,   9,   0,   0,   2)
    Sepith("Sepith_396C", 2,   7,   0,   5,   4,   2,   2)
    Sepith("Sepith_3984", 3,   4,   11,  0,   3,   4,   0)
    Sepith("Sepith_39A4", 7,   9,   15,  5,   6,   3,   5)

    MonsterBattlePostion("MonsterBattlePostion_6D4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_6D8", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_6DC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_6E0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6E4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6E8", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_6EC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6F0", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_734", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_738", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_73C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_740", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_744", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_748", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_74C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_750", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_6B4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_6B8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_6BC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_6C0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_6C4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6C8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6CC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6D0", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_754", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_758", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_75C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_760", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_764", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_768", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_76C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_770", 0, 0, 180)

    # monster count: 15

    BattleInfo(
        "BattleInfo_774", 0x0000, 59, 6, 45, 6, 1, 25, 0, "br0000", "Sepith_3964", 30, 45, 25, 0,
        (
            ("ms66500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6D4", "MonsterBattlePostion_734", "ed7450", "ed7453", "ATBonus_674"),
            ("ms66500.dat", "ms63000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6B4", "MonsterBattlePostion_734", "ed7450", "ed7453", "ATBonus_674"),
            ("ms66500.dat", "ms63000.dat", "ms66500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6D4", "MonsterBattlePostion_734", "ed7450", "ed7453", "ATBonus_674"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_810", 0x0000, 59, 6, 45, 6, 1, 75, 0, "br0000", "Sepith_397C", 30, 45, 25, 0,
        (
            ("ms61000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6D4", "MonsterBattlePostion_734", "ed7450", "ed7453", "ATBonus_674"),
            ("ms61000.dat", "ms61000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6B4", "MonsterBattlePostion_734", "ed7450", "ed7453", "ATBonus_674"),
            ("ms61000.dat", "ms66500.dat", "ms63000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6D4", "MonsterBattlePostion_734", "ed7450", "ed7453", "ATBonus_674"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_8AC", 0x0000, 59, 6, 45, 6, 1, 25, 0, "br0000", "Sepith_396C", 30, 45, 25, 0,
        (
            ("ms69900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6D4", "MonsterBattlePostion_734", "ed7450", "ed7453", "ATBonus_674"),
            ("ms69900.dat", "ms69900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6B4", "MonsterBattlePostion_734", "ed7450", "ed7453", "ATBonus_674"),
            ("ms69900.dat", "ms63000.dat", "ms69900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6D4", "MonsterBattlePostion_734", "ed7450", "ed7453", "ATBonus_674"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_948", 0x0000, 60, 6, 45, 6, 1, 50, 0, "br0000", "Sepith_3984", 30, 45, 25, 0,
        (
            ("ms64000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6D4", "MonsterBattlePostion_734", "ed7450", "ed7453", "ATBonus_674"),
            ("ms64000.dat", "ms64000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6B4", "MonsterBattlePostion_734", "ed7450", "ed7453", "ATBonus_674"),
            ("ms64000.dat", "ms64000.dat", "ms64000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6D4", "MonsterBattlePostion_734", "ed7450", "ed7453", "ATBonus_674"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_9E4", 0x0000, 77, 6, 45, 6, 1, 40, 0, "br0000", "Sepith_39A4", 40, 35, 25, 0,
        (
            ("ms63701.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6D4", "MonsterBattlePostion_734", "ed7450", "ed7453", "ATBonus_674"),
            ("ms63701.dat", "ms63701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6B4", "MonsterBattlePostion_734", "ed7450", "ed7453", "ATBonus_674"),
            ("ms63701.dat", "ms63701.dat", "ms63701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6D4", "MonsterBattlePostion_734", "ed7450", "ed7453", "ATBonus_674"),
            (),
        )
    )

    # event battle count: 6

    BattleInfo(
        "BattleInfo_B08", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br0000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms69900.dat", "ms69900.dat", "ms69900.dat", "ms69900.dat", "ms69900.dat", "ms69900.dat", "ms69900.dat", "ms69900.dat", "MonsterBattlePostion_6D4", "MonsterBattlePostion_734", "ed7451", "ed7453", "ATBonus_674"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_A80", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br0000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms61000.dat", "ms61000.dat", "ms61000.dat", "ms61000.dat", "ms61000.dat", "ms61000.dat", "ms61000.dat", "ms61000.dat", "MonsterBattlePostion_6D4", "MonsterBattlePostion_734", "ed7453", "ed7453", "ATBonus_674"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_AC4", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br0000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms63701.dat", "ms63701.dat", "ms63701.dat", "ms63701.dat", "ms63701.dat", "ms63701.dat", "ms63701.dat", "ms63701.dat", "MonsterBattlePostion_6D4", "MonsterBattlePostion_734", "ed7453", "ed7453", "ATBonus_674"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_B4C", 0x0040, 255, 6, 45, 10, 1, 30, 0, "br0000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88901.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_754", "MonsterBattlePostion_734", "ed7454", "ed7453", "ATBonus_694"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00000.itc",                   # 00
        "chr/ch00000.itc",                   # 01
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
        "monster/ch66550.itc",               # 10
        "monster/ch66551.itc",               # 11
        "monster/ch61050.itc",               # 12
        "monster/ch61050.itc",               # 13
        "monster/ch69950.itc",               # 14
        "monster/ch69950.itc",               # 15
        "monster/ch64050.itc",               # 16
        "monster/ch64051.itc",               # 17
        "monster/ch63750.itc",               # 18
        "monster/ch63751.itc",               # 19
    ))

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(47229,   2000,    4294956357, 270,  484,  0x0, 0,   18,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(96959,   4000,    4294918166, 270,  484,  0x0, 0,   18,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(47229,   2000,    4294956357, 270,  484,  0x0, 0,   24,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(96959,   4000,    4294918166, 270,  484,  0x0, 0,   24,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(117610,  4500,    32000,   0,    484,  0x0, 0,   20,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(12880,   15780,   920,     0x1010000,    "BattleInfo_774", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(37140,   15560,   2450,    0x1010000,    "BattleInfo_810", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(54520,   6080,    3000,    0x1010000,    "BattleInfo_8AC", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(47250,   4294957406, 2000,    0x1010000,    "BattleInfo_810", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(40910,   4294939606, 2000,    0x1010000,    "BattleInfo_774", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(24140,   4294957026, 2000,    0x1010000,    "BattleInfo_8AC", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(87050,   4294928986, 4000,    0x1010000,    "BattleInfo_774", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(119910,  4294933016, 4000,    0x1010000,    "BattleInfo_774", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(124190,  5590,    4000,    0x1010000,    "BattleInfo_810", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(116730,  27220,   4000,    0x1010000,    "BattleInfo_8AC", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(103280,  23510,   4000,    0x1010000,    "BattleInfo_774", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(94990,   4294966986, 4000,    0x1010000,    "BattleInfo_948", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(34320,   4294951686, 2000,    0x1010000,    "BattleInfo_9E4", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(98270,   4294935726, 4000,    0x1010000,    "BattleInfo_9E4", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(103030,  8630,    4000,    0x1010000,    "BattleInfo_9E4", 0,   24,  0xFFFF, 8,  9)

    DeclEvent(0x0040, 0, 21,  53.88999938964844,     6.400000095367432,     1.850000023841858,     16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -6.736249923706055,    -0.800000011920929,    -0.4625000059604645,   1.0])
    DeclEvent(0x0000, 0, 22,  101.54000091552734,    -16.450000762939453,   4.0,                   576.0,                 [0.0625,               -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -6.346250057220459,    5.483333587646484,     -0.8000000715255737,   1.0])

    DeclActor(105110,  4000,    4294939766, 1200,    105110,  5000,    4294939766, 0x007C, 0,  20, 0x0000)
    DeclActor(41520,   3000,    20360,   1200,    41520,   4000,    20360,   0x007C, 0,  5,  0x0000)
    DeclActor(22730,   2000,    4294958286, 1200,    22730,   3000,    4294958286, 0x007C, 0,  6,  0x0000)
    DeclActor(47230,   2000,    4294956356, 1200,    47230,   2000,    4294956356, 0x007C, 0,  8,  0x0000)
    DeclActor(96960,   4000,    4294918166, 1200,    96960,   4000,    4294918166, 0x007C, 0,  9,  0x0000)
    DeclActor(109280,  4000,    4294936236, 1500,    109280,  6000,    4294936236, 0x007C, 0,  19, 0x0000)
    DeclActor(107970,  4000,    4294937776, 1500,    107970,  6000,    4294937776, 0x007C, 0,  19, 0x0000)
    DeclActor(117610,  4000,    32000,   1200,    117610,  5000,    32000,   0x007C, 0,  7,  0x0000)
    DeclActor(94410,   4000,    4294945176, 1500,    94410,   5700,    4294945176, 0x007C, 0,  26, 0x0000)

    PlaceName(-17.0, 0.0, -10.0, 0x0000, 0x0000, "To Crossbell City")
    PlaceName(152.0, 0.0, -82.0, 0x0000, 0x0000, "To Tangram Gate")
    PlaceName(79.0, 0.0, 66.0, 0x0000, 0x0000, "To Armorica Village")
    PlaceName(105.5999984741211, 0.0, -27.200000762939453, 0x0000, 0x0055, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(2500, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 4
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 9

    ScpFunction((
        "Function_0_C74",          # 00, 0
        "Function_1_C90",          # 01, 1
        "Function_2_CAF",          # 02, 2
        "Function_3_CCC",          # 03, 3
        "Function_4_11FE",         # 04, 4
        "Function_5_1D64",         # 05, 5
        "Function_6_1EB6",         # 06, 6
        "Function_7_2008",         # 07, 7
        "Function_8_2224",         # 08, 8
        "Function_9_2582",         # 09, 9
        "Function_10_28E0",        # 0A, 10
        "Function_11_2908",        # 0B, 11
        "Function_12_290C",        # 0C, 12
        "Function_13_2A04",        # 0D, 13
        "Function_14_2B31",        # 0E, 14
        "Function_15_2C3E",        # 0F, 15
        "Function_16_2C74",        # 10, 16
        "Function_17_2DA1",        # 11, 17
        "Function_18_2DF2",        # 12, 18
        "Function_19_2E86",        # 13, 19
        "Function_20_31BF",        # 14, 20
        "Function_21_3213",        # 15, 21
        "Function_22_328F",        # 16, 22
        "Function_23_37B3",        # 17, 23
        "Function_24_3808",        # 18, 24
        "Function_25_387C",        # 19, 25
        "Function_26_389F",        # 1A, 26
    ))


    def Function_0_C74(): pass

    label("Function_0_C74")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C8F")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_C74")

    label("loc_C8F")

    Return()

    # Function_0_C74 end

    def Function_1_C90(): pass

    label("Function_1_C90")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CAE")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_C90")

    label("loc_CAE")

    Return()

    # Function_1_C90 end

    def Function_2_CAF(): pass

    label("Function_2_CAF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CCB")
    OP_A1(0xFE, 0x1F4, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_2_CAF")

    label("loc_CCB")

    Return()

    # Function_2_CAF end

    def Function_3_CCC(): pass

    label("Function_3_CCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E, 0)), scpexpr(EXPR_END)), "loc_CDB")
    ClearScenarioFlags(0x3E, 0)
    Event(0, 17)

    label("loc_CDB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_117F")
    ClearScenarioFlags(0x38, 0)
    ClearScenarioFlags(0x38, 1)
    ClearScenarioFlags(0x38, 2)
    ClearScenarioFlags(0x38, 3)
    ClearScenarioFlags(0x38, 4)
    ClearScenarioFlags(0x38, 5)
    ClearScenarioFlags(0x38, 6)
    ClearScenarioFlags(0x38, 7)
    ClearScenarioFlags(0x39, 0)
    ClearScenarioFlags(0x39, 1)
    ClearScenarioFlags(0x39, 2)
    ClearScenarioFlags(0x39, 3)
    ClearScenarioFlags(0x39, 4)
    ClearScenarioFlags(0x39, 5)
    ClearScenarioFlags(0x39, 6)
    ClearScenarioFlags(0x39, 7)
    ClearScenarioFlags(0x3A, 0)
    ClearScenarioFlags(0x3A, 1)
    ClearScenarioFlags(0x3A, 2)
    ClearScenarioFlags(0x3A, 3)
    ClearScenarioFlags(0x3A, 4)
    ClearScenarioFlags(0x3A, 5)
    ClearScenarioFlags(0x3A, 6)
    ClearScenarioFlags(0x3A, 7)
    ClearScenarioFlags(0x3B, 0)
    ClearScenarioFlags(0x3B, 1)
    ClearScenarioFlags(0x3B, 2)
    ClearScenarioFlags(0x3B, 3)
    ClearScenarioFlags(0x3B, 4)
    ClearScenarioFlags(0x3B, 5)
    ClearScenarioFlags(0x3B, 6)
    ClearScenarioFlags(0x3B, 7)
    ClearScenarioFlags(0x3D, 5)
    ClearScenarioFlags(0x3D, 6)
    ClearScenarioFlags(0x3D, 7)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D68")
    SetScenarioFlags(0x38, 0)

    label("loc_D68")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D7E")
    SetScenarioFlags(0x38, 1)

    label("loc_D7E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D94")
    SetScenarioFlags(0x38, 2)

    label("loc_D94")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DAA")
    SetScenarioFlags(0x38, 3)

    label("loc_DAA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DC0")
    SetScenarioFlags(0x38, 4)

    label("loc_DC0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DD6")
    SetScenarioFlags(0x38, 5)

    label("loc_DD6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DEC")
    SetScenarioFlags(0x38, 6)

    label("loc_DEC")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E02")
    SetScenarioFlags(0x38, 7)

    label("loc_E02")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E18")
    SetScenarioFlags(0x39, 0)

    label("loc_E18")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E2E")
    SetScenarioFlags(0x39, 1)

    label("loc_E2E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E44")
    SetScenarioFlags(0x39, 2)

    label("loc_E44")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E5A")
    SetScenarioFlags(0x39, 3)

    label("loc_E5A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E70")
    SetScenarioFlags(0x39, 4)

    label("loc_E70")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E86")
    SetScenarioFlags(0x39, 5)

    label("loc_E86")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E9C")
    SetScenarioFlags(0x39, 6)

    label("loc_E9C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EB2")
    SetScenarioFlags(0x39, 7)

    label("loc_EB2")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC8")
    SetScenarioFlags(0x3A, 0)

    label("loc_EC8")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EDE")
    SetScenarioFlags(0x3A, 1)

    label("loc_EDE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF4")
    SetScenarioFlags(0x3A, 2)

    label("loc_EF4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F0A")
    SetScenarioFlags(0x3A, 3)

    label("loc_F0A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F20")
    SetScenarioFlags(0x3A, 4)

    label("loc_F20")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F36")
    SetScenarioFlags(0x3A, 5)

    label("loc_F36")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F4C")
    SetScenarioFlags(0x3A, 6)

    label("loc_F4C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F62")
    SetScenarioFlags(0x3A, 7)

    label("loc_F62")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F78")
    SetScenarioFlags(0x3B, 0)

    label("loc_F78")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F8E")
    SetScenarioFlags(0x3B, 1)

    label("loc_F8E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FA4")
    SetScenarioFlags(0x3B, 2)

    label("loc_FA4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FBA")
    SetScenarioFlags(0x3B, 3)

    label("loc_FBA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FD0")
    SetScenarioFlags(0x3B, 4)

    label("loc_FD0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE6")
    SetScenarioFlags(0x3B, 5)

    label("loc_FE6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FFC")
    SetScenarioFlags(0x3B, 6)

    label("loc_FFC")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1012")
    SetScenarioFlags(0x3B, 7)

    label("loc_1012")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1028")
    SetScenarioFlags(0x3D, 5)

    label("loc_1028")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_103E")
    SetScenarioFlags(0x3D, 6)

    label("loc_103E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1054")
    SetScenarioFlags(0x3D, 7)

    label("loc_1054")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_108F")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_117F")

    label("loc_108F")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10B2")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_117F")

    label("loc_10B2")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10D5")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_117F")

    label("loc_10D5")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F8")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_117F")

    label("loc_10F8")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_111B")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_117F")

    label("loc_111B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_113E")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_117F")

    label("loc_113E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1161")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_117F")

    label("loc_1161")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_117F")
    SetScenarioFlags(0x3C, 7)

    label("loc_117F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x35, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1195")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1195")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11C7")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11C7")
    SetChrPos(0x0, 107670, 4000, -30320, 225)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 18)

    label("loc_11C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_11FA")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11FA")
    SetChrPos(0x0, 107970, 4000, -29520, 270)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_11FA")

    Call(0, 10)
    Return()

    # Function_3_CCC end

    def Function_4_11FE(): pass

    label("Function_4_11FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_1210")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1210")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1237")
    ModifyEventFlags(0, 0, 0x80)
    SetMapObjFlags(0x5, 0x4)
    Jump("loc_12A0")

    label("loc_1237")

    OP_78(0x5, 0xE)
    ClearMapObjFlags(0x5, 0x4)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xE, 0x8)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xE, 0x1)
    SetChrPos(0xE, 53890, 3000, 6400, 270)
    OP_93(0xE, 0x10E, 0x0)
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F40), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetBarrier(0x0, 0x0, 0x2, 0x0, 53890, 2000, 6400, 3000, 3000, 90000)

    label("loc_12A0")

    OP_52(0x14, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1AB1")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    SetMapObjFrame(0xFF, "obj_shadow0", 0x0, 0x1)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x6E, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_1AB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_1B7B")
    SetMapObjFrame(0xFF, "obj_shadow0", 0x0, 0x1)
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x6E, 0x0)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x16, 0x4)
    ClearMapObjFlags(0x17, 0x4)
    ClearMapObjFlags(0x18, 0x4)
    ClearMapObjFlags(0x19, 0x4)
    ClearMapObjFlags(0x1A, 0x4)
    ClearMapObjFlags(0x1B, 0x4)
    ClearMapObjFlags(0x1C, 0x4)
    ClearMapObjFlags(0x1D, 0x4)
    ClearMapObjFlags(0x1E, 0x4)
    Jump("loc_1C0B")

    label("loc_1B7B")

    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x16, 0x4)
    SetMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x18, 0x4)
    SetMapObjFlags(0x19, 0x4)
    SetMapObjFlags(0x1A, 0x4)
    SetMapObjFlags(0x1B, 0x4)
    SetMapObjFlags(0x1C, 0x4)
    SetMapObjFlags(0x1D, 0x4)
    SetMapObjFlags(0x1E, 0x4)

    label("loc_1C0B")

    MiniGame(0x2F, 0x5, 0x6, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x8, 0x80)
    SetMapObjFlags(0x2, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C4B")
    OP_70(0x0, 0x0)
    Jump("loc_1C4F")

    label("loc_1C4B")

    OP_70(0x0, 0x1E)

    label("loc_1C4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C62")
    OP_70(0x1, 0x0)
    Jump("loc_1C66")

    label("loc_1C62")

    OP_70(0x1, 0x1E)

    label("loc_1C66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C79")
    OP_70(0x6, 0x0)
    Jump("loc_1C7D")

    label("loc_1C79")

    OP_70(0x6, 0x1E)

    label("loc_1C7D")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1CDE")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, 47230, 2000, -10940, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)

    label("loc_1CDE")

    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1D2A")
    PlayEffect(0x10, 0xA, 0xFF, 0x0, 96960, 4000, -49130, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x4, 0x1)

    label("loc_1D2A")

    OP_1C(0x0, 0x1F, 0x0, 0x32, 0x0, 0xB, 0x0, 0x0)
    OP_1C(0x0, 0x20, 0x0, 0x32, 0x0, 0xB, 0x0, 0x0)
    OP_1C(0x0, 0x21, 0x0, 0x32, 0x0, 0xB, 0x0, 0x0)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D63")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_1D63")

    Return()

    # Function_4_11FE end

    def Function_5_1D64(): pass

    label("Function_5_1D64")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E60")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_1DE9")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E8, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_1E5B")

    label("loc_1DE9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1E5B")

    Jump("loc_1EAA")

    label("loc_1E60")

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

    label("loc_1EAA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1D64 end

    def Function_6_1EB6(): pass

    label("Function_6_1EB6")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FB2")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_1F3B")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
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
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E8, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_1FAD")

    label("loc_1F3B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1FAD")

    Jump("loc_1FFC")

    label("loc_1FB2")

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

    label("loc_1FFC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1EB6 end

    def Function_7_2008(): pass

    label("Function_7_2008")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21D9")
    Sound(14, 0, 100, 0)
    OP_74(0x6, 0x1E)
    OP_71(0x6, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x216, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_210B")
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xD, 0x0, 0)
    OP_98(0xD, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_2065():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2065)

    def lambda_207F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_207F)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xD, 1)
    Battle("BattleInfo_B08", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_20EC"),
        (2, "loc_20FB"),
        (1, "loc_2108"),
        (SWITCH_DEFAULT, "loc_210B"),
    )


    label("loc_20EC")

    SetScenarioFlags(0x216, 4)
    OP_70(0x6, 0x1E)
    Sleep(500)
    Jump("loc_210B")

    label("loc_20FB")

    OP_70(0x6, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_2108")

    OP_B9(0x0)
    Return()

    label("loc_210B")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xB3, 1)"), scpexpr(EXPR_END)), "loc_2164")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xB3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E9, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_21D4")

    label("loc_2164")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xB3),
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

    label("loc_21D4")

    Jump("loc_2218")

    label("loc_21D9")

    FadeToDark(300, 0, 100)

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

    label("loc_2218")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_2008 end

    def Function_8_2224(): pass

    label("Function_8_2224")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_23DC")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 3)), scpexpr(EXPR_END)), "loc_23BD")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23B8")
    ClearScenarioFlags(0x3A, 3)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 3)), scpexpr(EXPR_END)), "loc_23B5")
    ClearScenarioFlags(0x38, 3)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_22DA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_22DA)
    TurnDirection(0x9, 0x0, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    PlayEffect(0x7, 0x1, 0x9, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_A80", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23B0")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2397")
    Call(1, 5)
    Jump("loc_23B0")

    label("loc_2397")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_23AD")
    Call(1, 4)
    Jump("loc_23B0")

    label("loc_23AD")

    Call(1, 3)

    label("loc_23B0")

    Jump("loc_23B8")

    label("loc_23B5")

    Call(1, 1)

    label("loc_23B8")

    Jump("loc_23D3")

    label("loc_23BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 3)), scpexpr(EXPR_END)), "loc_23D3")
    ClearScenarioFlags(0x38, 3)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_23D3")

    TalkEnd(0xFF)
    Return()

    label("loc_23DC")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 3)), scpexpr(EXPR_END)), "loc_2567")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2562")
    ClearScenarioFlags(0x3A, 3)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 3)), scpexpr(EXPR_END)), "loc_255F")
    ClearScenarioFlags(0x38, 3)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2484():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2484)
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
    Battle("BattleInfo_AC4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_255A")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2541")
    Call(1, 5)
    Jump("loc_255A")

    label("loc_2541")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2557")
    Call(1, 4)
    Jump("loc_255A")

    label("loc_2557")

    Call(1, 3)

    label("loc_255A")

    Jump("loc_2562")

    label("loc_255F")

    Call(1, 1)

    label("loc_2562")

    Jump("loc_257D")

    label("loc_2567")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 3)), scpexpr(EXPR_END)), "loc_257D")
    ClearScenarioFlags(0x38, 3)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_257D")

    TalkEnd(0xFF)
    Return()

    # Function_8_2224 end

    def Function_9_2582(): pass

    label("Function_9_2582")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_273A")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 4)), scpexpr(EXPR_END)), "loc_271B")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2716")
    ClearScenarioFlags(0x3A, 4)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 4)), scpexpr(EXPR_END)), "loc_2713")
    ClearScenarioFlags(0x38, 4)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2638():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2638)
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
    Battle("BattleInfo_A80", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_270E")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_26F5")
    Call(1, 5)
    Jump("loc_270E")

    label("loc_26F5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_270B")
    Call(1, 4)
    Jump("loc_270E")

    label("loc_270B")

    Call(1, 3)

    label("loc_270E")

    Jump("loc_2716")

    label("loc_2713")

    Call(1, 1)

    label("loc_2716")

    Jump("loc_2731")

    label("loc_271B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 4)), scpexpr(EXPR_END)), "loc_2731")
    ClearScenarioFlags(0x38, 4)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_2731")

    TalkEnd(0xFF)
    Return()

    label("loc_273A")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 4)), scpexpr(EXPR_END)), "loc_28C5")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28C0")
    ClearScenarioFlags(0x3A, 4)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 4)), scpexpr(EXPR_END)), "loc_28BD")
    ClearScenarioFlags(0x38, 4)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_27E2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_27E2)
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
    Battle("BattleInfo_AC4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28B8")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_289F")
    Call(1, 5)
    Jump("loc_28B8")

    label("loc_289F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_28B5")
    Call(1, 4)
    Jump("loc_28B8")

    label("loc_28B5")

    Call(1, 3)

    label("loc_28B8")

    Jump("loc_28C0")

    label("loc_28BD")

    Call(1, 1)

    label("loc_28C0")

    Jump("loc_28DB")

    label("loc_28C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 4)), scpexpr(EXPR_END)), "loc_28DB")
    ClearScenarioFlags(0x38, 4)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_28DB")

    TalkEnd(0xFF)
    Return()

    # Function_9_2582 end

    def Function_10_28E0(): pass

    label("Function_10_28E0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2902")
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    Jump("loc_2907")

    label("loc_2902")

    SetChrFlags(0x15, 0x80)

    label("loc_2907")

    Return()

    # Function_10_28E0 end

    def Function_11_2908(): pass

    label("Function_11_2908")

    Call(1, 6)
    Return()

    # Function_11_2908 end

    def Function_12_290C(): pass

    label("Function_12_290C")

    EventBegin(0x2)
    SetMapFlags(0x8000000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KThere is a bus stop.\x01",
            "Move by bus?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Crossbell City East Entrance\x01",      # 0
            "Armorica Village\x01",                  # 1
            "Tangram Gate\x01",                      # 2
            "Quit\x01",                              # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29B7")
    Call(0, 13)
    ClearMapFlags(0x8000000)
    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_29FC")

    label("loc_29B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29DC")
    Call(0, 14)
    ClearMapFlags(0x8000000)
    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_29FC")

    label("loc_29DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29FC")
    Call(0, 16)
    ClearMapFlags(0x8000000)
    NewScene("t2500", 0, 0, 0)
    IdleLoop()

    label("loc_29FC")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_12_290C end

    def Function_13_2A04(): pass

    label("Function_13_2A04")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_2B2D")
    Fade(500)
    OP_68(101630, 4600, -27310, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(25000, 0)
    OP_E2(0x1)
    SetChrPos(0x0, 106370, 4000, -27960, 225)
    SetChrPos(0x1, 107160, 4000, -28700, 225)
    SetChrPos(0x2, 107820, 4000, -29500, 225)
    SetChrPos(0x3, 108390, 4000, -30200, 225)
    ClearChrFlags(0x8, 0x80)
    ClearMapObjFlags(0x2, 0x4)
    OP_78(0x2, 0x8)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x8, 102740, 4000, -11580, 180)
    OP_D5(0x8, 0x0, 0x2EFF4, 0x0, 0x0)
    SetMapObjFlags(0x2, 0x1000)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x79, 0xB4, 0x0, 0x20)

    def lambda_2AE4():
        OP_95(0xFE, 99960, 4000, -24090, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2AE4)
    OP_0D()
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x8, 1)
    OP_71(0x2, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x2)
    Sleep(300)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetEventSkip(0x1, 0x0)

    label("loc_2B2D")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_13_2A04 end

    def Function_14_2B31(): pass

    label("Function_14_2B31")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_2C3A")
    Fade(500)
    OP_68(100290, 4600, -28120, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(29500, 0)
    OP_E2(0x1)
    SetChrPos(0x0, 106370, 4000, -27960, 225)
    SetChrPos(0x1, 107160, 4000, -28700, 225)
    SetChrPos(0x2, 107820, 4000, -29500, 225)
    SetChrPos(0x3, 108390, 4000, -30200, 225)
    ClearChrFlags(0x8, 0x80)
    ClearMapObjFlags(0x2, 0x4)
    OP_78(0x2, 0x8)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x8, 86660, 4000, -28070, 90)
    OP_D5(0x8, 0x0, 0x16184, 0x0, 0x0)
    SetMapObjFlags(0x2, 0x1000)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x79, 0xB4, 0x0, 0x20)
    BeginChrThread(0x8, 1, 0, 15)
    OP_0D()
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x8, 1)
    OP_79(0x2)
    Sleep(300)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetEventSkip(0x1, 0x0)

    label("loc_2C3A")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_14_2B31 end

    def Function_15_2C3E(): pass

    label("Function_15_2C3E")

    OP_95(0x8, 92660, 4000, -29500, 4000, 0x0)
    OP_9E(0x8, 0x16EFE, 0xFFFFA560, 0xFFFEA840, 0xFA0, 0x1)
    OP_71(0x2, 0x5B, 0x78, 0x0, 0x0)
    Return()

    # Function_15_2C3E end

    def Function_16_2C74(): pass

    label("Function_16_2C74")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_2D9D")
    Fade(500)
    OP_68(103530, 4600, -32380, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(26000, 0)
    OP_E2(0x1)
    SetChrPos(0x0, 106370, 4000, -27960, 225)
    SetChrPos(0x1, 107160, 4000, -28700, 225)
    SetChrPos(0x2, 107820, 4000, -29500, 225)
    SetChrPos(0x3, 108390, 4000, -30200, 225)
    ClearChrFlags(0x8, 0x80)
    ClearMapObjFlags(0x2, 0x4)
    OP_78(0x2, 0x8)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x8, 91520, 4000, -26730, 135)
    OP_D5(0x8, 0x0, 0x16184, 0x0, 0x0)
    SetMapObjFlags(0x2, 0x1000)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x79, 0xB4, 0x0, 0x20)

    def lambda_2D54():
        OP_95(0xFE, 100900, 4000, -36100, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2D54)
    OP_0D()
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x8, 1)
    OP_71(0x2, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x2)
    Sleep(300)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetEventSkip(0x1, 0x0)

    label("loc_2D9D")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_16_2C74 end

    def Function_17_2DA1(): pass

    label("Function_17_2DA1")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetChrPos(0x0, 106740, 4000, -28000, 225)
    OP_31(0x1)
    OP_68(106740, 4600, -28000, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(24000, 0)
    EventEnd(0x5)
    Return()

    # Function_17_2DA1 end

    def Function_18_2DF2(): pass

    label("Function_18_2DF2")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_2E4D")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2E42")
    Sound(2502, 255, 100, 0)
    Jump("loc_2E48")

    label("loc_2E42")

    Sound(2503, 255, 100, 0)

    label("loc_2E48")

    Jump("loc_2E71")

    label("loc_2E4D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2E6B")
    Sound(3347, 255, 100, 0)
    Jump("loc_2E71")

    label("loc_2E6B")

    Sound(3348, 255, 100, 0)

    label("loc_2E71")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_18_2DF2 end

    def Function_19_2E86(): pass

    label("Function_19_2E86")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2EB8")
    SetScenarioFlags(0x31, 2)

    label("loc_2EB8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2EFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_2EF8")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2EED")
    Sound(2499, 255, 100, 0)
    Jump("loc_2EF3")

    label("loc_2EED")

    Sound(3537, 255, 100, 0)

    label("loc_2EF3")

    Jump("loc_2EFE")

    label("loc_2EF8")

    Sound(3344, 255, 100, 0)

    label("loc_2EFE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_2F71")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2F51"),
        (SWITCH_DEFAULT, "loc_2F62"),
    )


    label("loc_2F51")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_2F6C")

    label("loc_2F62")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2F6C")

    Jump("loc_31AC")

    label("loc_2F71")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_2FA3")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_2FA3")

    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2FD5"),
        (1, "loc_30D9"),
        (2, "loc_316A"),
        (SWITCH_DEFAULT, "loc_31A2"),
    )


    label("loc_2FD5")

    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    OP_74(0x3, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_3006")
    OP_70(0x3, 0x12C)
    OP_71(0x3, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_3016")

    label("loc_3006")

    OP_70(0x3, 0xF0)
    OP_71(0x3, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_3016")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_306C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_306C")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_308F")
    Sound(461, 0, 100, 0)

    label("loc_308F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_30AF")
    OP_70(0x3, 0x14A)
    OP_71(0x3, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_30BF")

    label("loc_30AF")

    OP_70(0x3, 0x10E)
    OP_71(0x3, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_30BF")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x3, "light", 0x1, 0x1)
    OP_70(0x3, 0x0)
    Jump("loc_2EFE")

    label("loc_30D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_314B")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_310E")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_3126")

    label("loc_310E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_3121")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_3126")

    label("loc_3121")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_3126")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3165")

    label("loc_314B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_315B")
    OP_AF(0xFB)
    Jump("loc_3165")

    label("loc_315B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3165")

    Jump("loc_31AC")

    label("loc_316A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3183")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_319D")

    label("loc_3183")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_3193")
    OP_AF(0xFB)
    Jump("loc_319D")

    label("loc_3193")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_319D")

    Jump("loc_31AC")

    label("loc_31A2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_31AC")

    Jump("loc_2EFE")

    label("loc_31B1")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_19_2E86 end

    def Function_20_31BF(): pass

    label("Function_20_31BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_320F")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It seems the orbal bus service is not running.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_320F")

    Call(0, 12)
    Return()

    # Function_20_31BF end

    def Function_21_3213(): pass

    label("Function_21_3213")

    Battle("BattleInfo_B4C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    OP_E2(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_325A")
    OP_90(0x0, 46050, 3000, 7180, 270)
    EventEnd(0x5)
    SetChrFlags(0xE, 0x8000)
    Jump("loc_328E")

    label("loc_325A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_326D")
    Jump("loc_328E")

    label("loc_326D")

    ModifyEventFlags(0, 0, 0x80)
    SetMapObjFlags(0x5, 0x4)
    SetBarrier(0x2, 0x0, 0x1)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8)
    SetScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x3C, 1)
    EventEnd(0x5)

    label("loc_328E")

    Return()

    # Function_21_3213 end

    def Function_22_328F(): pass

    label("Function_22_328F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36EE")
    EventBegin(0x0)
    OP_E2(0x3)
    Fade(500)
    OP_68(103210, 4600, -12110, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21820, 0)
    SoundLoad(469)
    SetChrPos(0x101, 103020, 4000, -13240, 180)
    SetChrPos(0x103, 101880, 4000, -12970, 180)
    SetChrPos(0x105, 103970, 4000, -11920, 180)
    SetChrPos(0x107, 102810, 4000, -11480, 180)
    OP_0D()
    BeginChrThread(0x12, 1, 0, 25)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00205F#6PThese seem...\x01",
            "The noises of armed vehicles on the move.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FThis is bad...\x01",
            "Let's get away for now!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    SetChrPos(0x101, 111800, 4000, 290, 180)
    SetChrPos(0x103, 112960, 4000, -40, 180)
    SetChrPos(0x105, 113660, 4000, 1300, 180)
    SetChrPos(0x107, 112480, 4000, 2080, 180)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xF, 0x4)
    OP_78(0x22, 0xF)
    SetMapObjFlags(0x22, 0x1000)
    ClearMapObjFlags(0x22, 0x4)
    SetMapObjFrame(0x22, "light", 0x0, 0x1)
    SetMapObjFrame(0x22, "mark00", 0x0, 0x1)
    OP_71(0x22, 0x79, 0xB4, 0x0, 0x20)
    OP_74(0x22, 0x19)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x10, 0x4)
    OP_78(0x23, 0x10)
    SetMapObjFlags(0x23, 0x1000)
    ClearMapObjFlags(0x23, 0x4)
    SetMapObjFrame(0x23, "light", 0x0, 0x1)
    SetMapObjFrame(0x23, "mark00", 0x0, 0x1)
    OP_71(0x23, 0x79, 0xB4, 0x0, 0x20)
    OP_74(0x23, 0x19)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x11, 0x4)
    OP_78(0x24, 0x11)
    SetMapObjFlags(0x24, 0x1000)
    ClearMapObjFlags(0x24, 0x4)
    SetMapObjFrame(0x24, "light", 0x0, 0x1)
    SetMapObjFrame(0x24, "mark00", 0x0, 0x1)
    OP_71(0x24, 0x79, 0xB4, 0x0, 0x20)
    OP_74(0x24, 0x19)
    BeginChrThread(0xF, 2, 0, 23)
    OP_68(104440, 4600, -37320, 0)
    MoveCamera(64, 19, 0, 0)
    OP_6E(670, 0)
    SetCameraDistance(18910, 0)
    OP_68(94850, 4600, -32040, 12000)
    MoveCamera(353, 33, 0, 12000)
    OP_6E(670, 12000)
    SetCameraDistance(18910, 12000)
    Sleep(12000)
    StopSound(469, 3000, 70)
    WaitChrThread(0xF, 2)
    Fade(500)
    OP_68(113160, 4600, 1030, 0)
    MoveCamera(62, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21180, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#00006F#6PThey're gone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIt appears they were on patrol.\x02\x03",
            "#00203FAt present, it seems dangerous going back and\x01",
            "fort the East Crossbell Highway without purpose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#6PYeah, it appears that it's better to go\x01",
            "back to the Armorica Old Road area.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_24(0x1D5)
    SetChrPos(0x0, 112030, 4000, -380, 180)
    SetScenarioFlags(0x1BC, 4)
    OP_E2(0x2)
    EventEnd(0x5)
    Jump("loc_37B2")

    label("loc_36EE")

    EventBegin(0x1)
    OP_E2(0x3)
    Fade(500)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00003FAt present, going back and forth the\x01",
            "East Crossbell Highway is dangerous.\x02\x03",
            "#00001FIt appears that it's better to go\x01",
            "back to the Armorica Old Road area.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 102640, 4000, -12890, 0)
    OP_E2(0x2)
    EventEnd(0x4)

    label("loc_37B2")

    Return()

    # Function_22_328F end

    def Function_23_37B3(): pass

    label("Function_23_37B3")

    Sound(465, 0, 100, 0)
    BeginChrThread(0xF, 1, 0, 24)
    Sleep(2200)
    BeginChrThread(0x10, 1, 0, 24)
    Sleep(2200)
    Sound(471, 0, 100, 0)
    BeginChrThread(0x11, 1, 0, 24)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x10, 1)
    WaitChrThread(0x11, 1)
    ClearMapObjFlags(0x22, 0x1000)
    SetMapObjFlags(0x22, 0x4)
    ClearMapObjFlags(0x23, 0x1000)
    SetMapObjFlags(0x23, 0x4)
    ClearMapObjFlags(0x24, 0x1000)
    SetMapObjFlags(0x24, 0x4)
    Return()

    # Function_23_37B3 end

    def Function_24_3808(): pass

    label("Function_24_3808")

    SetChrPos(0xFE, 117230, 4000, -51140, 315)
    OP_D5(0xFE, 0x0, 0x4CE78, 0x0, 0x0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 102560, 4000, -36380)
    OP_9F(0x1, 95450, 4000, -31770)
    OP_9F(0x1, 85860, 4000, -28370)
    OP_9F(0x1, 68230, 4000, -27150)
    OP_9F(0x2, 0xFE, 5000, 0x2)
    SetChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_24_3808 end

    def Function_25_387C(): pass

    label("Function_25_387C")

    Sound(469, 2, 30, 0)
    Sleep(500)
    OP_25(0x1D5, 0x28)
    Sleep(500)
    OP_25(0x1D5, 0x32)
    Sleep(300)
    OP_25(0x1D5, 0x3C)
    Sleep(300)
    OP_25(0x1D5, 0x46)
    Return()

    # Function_25_387C end

    def Function_26_389F(): pass

    label("Function_26_389F")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "West - Crossbell City  108 selge\x01",
            "North - Armorica Village  166 selge\x01",
            "South-East - Tangram Gate  98 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_26_389F end

    SaveToFile()

Try(main)
