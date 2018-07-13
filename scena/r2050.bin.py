from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r2050.bin",                # FileName
        "r2050",                    # MapName
        "r2050",                    # Location
        0x0062,                     # MapIndex
        "ed7202",
        0x00000000,                 # Flags
        ("r2050", "r0000_1", "", "", "", ""),   # include
        0x03,                       # PlaceNameNumber
        0x15,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 98, 0, 5, 0, 6],
    )

    BuildStringList((
        "r2050",                  # 0
        "マダラマーダー",         # 1
        "マダラマーダー",         # 2
        "鉄鋼ドリュー",           # 3
        "鉄鋼ドリュー",           # 4
        "アカマダラマーダー",     # 5
        " ",                      # 6
        "CGF Member",             # 7
        "CGF Member",             # 8
        "Jaeger",                 # 9
        "Jaeger",                 # 10
        "Jaeger",                 # 11
        "Jaeger",                 # 12
        "Jaeger",                 # 13
        "Shirley",                # 14
        "Armored Vehicle",        # 15
        "Armored Vehicle",        # 16
        "Armored Vehicle",        # 17
        "br2040",                 # 18
        "br2050",                 # 19
        "br2050",                 # 20
        "br2050",                 # 21
        "br2040",                 # 22
        "br2050",                 # 23
        "br2040",                 # 24
        "br2040",                 # 25
        "br2040",                 # 26
        "br2040",                 # 27
        "To Crossbell City",      # 28
        "To Mining Town Mainz",   # 29
        "To Temple of Moon",      # 30
    ))

    ATBonus("ATBonus_668", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_688", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_4CEF", 0,   4,   0,   4,   2,   2,   2)
    Sepith("Sepith_4CDF", 5,   2,   0,   1,   2,   3,   2)
    Sepith("Sepith_4CE7", 4,   0,   4,   0,   4,   1,   3)
    Sepith("Sepith_4CD7", 0,   0,   0,   5,   5,   5,   3)
    Sepith("Sepith_4CCF", 11,  3,   6,   4,   6,   10,  8)

    MonsterBattlePostion("MonsterBattlePostion_6C8", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_6CC", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_6D0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_6D4", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6D8", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6DC", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_6E0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6E4", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_728", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_72C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_730", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_734", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_738", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_73C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_740", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_744", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_6A8", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_6AC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_6B0", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_6B4", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_6B8", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6BC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6C0", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6C4", 2, 13, 180)

    # monster count: 12

    BattleInfo(
        "BattleInfo_9A0", 0x0000, 53, 6, 60, 10, 1, 40, 0, "br2050", "Sepith_4CEF", 30, 40, 20, 10,
        (
            ("ms69100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6C8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
            ("ms69100.dat", "ms69100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6C8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
            ("ms69100.dat", "ms69100.dat", "ms69100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6C8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
            ("ms69100.dat", "ms69100.dat", "ms69100.dat", "ms69100.dat", 0, 0, 0, 0, "MonsterBattlePostion_6C8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
        )
    )

    BattleInfo(
        "BattleInfo_810", 0x0000, 53, 6, 60, 10, 1, 50, 0, "br2050", "Sepith_4CDF", 30, 40, 20, 10,
        (
            ("ms68100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6C8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
            ("ms68100.dat", "ms68100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6A8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
            ("ms68100.dat", "ms71700.dat", "ms68100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6C8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
            ("ms68100.dat", "ms68100.dat", "ms71700.dat", "ms68100.dat", 0, 0, 0, 0, "MonsterBattlePostion_6A8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
        )
    )

    BattleInfo(
        "BattleInfo_8D8", 0x0000, 53, 6, 60, 10, 1, 50, 0, "br2050", "Sepith_4CE7", 30, 40, 20, 10,
        (
            ("ms72800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6C8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
            ("ms72800.dat", "ms68100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6A8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
            ("ms72800.dat", "ms68100.dat", "ms68100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6C8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
            ("ms72800.dat", "ms68100.dat", "ms68100.dat", "ms68100.dat", 0, 0, 0, 0, "MonsterBattlePostion_6A8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
        )
    )

    BattleInfo(
        "BattleInfo_748", 0x0000, 53, 6, 60, 10, 1, 30, 0, "br2040", "Sepith_4CD7", 30, 40, 20, 10,
        (
            ("ms71700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6C8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
            ("ms71700.dat", "ms71700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6A8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
            ("ms71700.dat", "ms65900.dat", "ms71700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6C8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
            ("ms71700.dat", "ms71700.dat", "ms65900.dat", "ms71700.dat", 0, 0, 0, 0, "MonsterBattlePostion_6A8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
        )
    )

    BattleInfo(
        "BattleInfo_B04", 0x0000, 82, 6, 45, 6, 1, 30, 0, "br2050", "Sepith_4CCF", 40, 35, 25, 0,
        (
            ("ms76001.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6C8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
            ("ms76001.dat", "ms76001.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6A8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
            ("ms76001.dat", "ms76001.dat", "ms76001.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6C8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_C28", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "br2040", 0x00000000, 100, 0, 0, 0,
        (
            ("ms79501.dat", "ms79501.dat", "ms79501.dat", "ms79501.dat", "ms79501.dat", "ms79501.dat", 0, 0, "MonsterBattlePostion_6A8", "MonsterBattlePostion_728", "ed7451", "ed7453", "ATBonus_688"),
            (),
            (),
            (),
        )
    )

    # event battle count: 6

    BattleInfo(
        "BattleInfo_C6C", 0x0000, 50, 6, 45, 0, 1, 0, 0, "br2040", 0x00000000, 100, 0, 0, 0,
        (
            ("ms72800.dat", "ms72800.dat", "ms72800.dat", "ms72800.dat", "ms72800.dat", "ms72800.dat", "ms72800.dat", "ms72800.dat", "MonsterBattlePostion_6A8", "MonsterBattlePostion_728", "ed7451", "ed7453", "ATBonus_668"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_BA0", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br2040", 0x00000000, 100, 0, 0, 0,
        (
            ("ms68100.dat", "ms68100.dat", "ms68100.dat", "ms68100.dat", "ms68100.dat", "ms68100.dat", "ms68100.dat", "ms68100.dat", "MonsterBattlePostion_6A8", "MonsterBattlePostion_728", "ed7453", "ed7453", "ATBonus_668"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_BE4", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br2040", 0x00000000, 100, 0, 0, 0,
        (
            ("ms76001.dat", "ms76001.dat", "ms76001.dat", "ms76001.dat", "ms76001.dat", "ms76001.dat", 0, 0, "MonsterBattlePostion_6A8", "MonsterBattlePostion_728", "ed7453", "ed7453", "ATBonus_668"),
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
        "monster/ch71750.itc",               # 10
        "monster/ch71751.itc",               # 11
        "monster/ch68150.itc",               # 12
        "monster/ch68151.itc",               # 13
        "monster/ch72850.itc",               # 14
        "monster/ch72851.itc",               # 15
        "monster/ch69150.itc",               # 16
        "monster/ch69151.itc",               # 17
        "monster/ch76050.itc",               # 18
        "monster/ch76051.itc",               # 19
        "monster/ch79550.itc",               # 1A
        "monster/ch79551.itc",               # 1B
    ))

    DeclNpc(4294945956, 0,       45409,   270,  484,  0x0, 0,   18,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(4294943196, 8000,    147860,  270,  484,  0x0, 0,   18,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(4294945956, 0,       45409,   270,  484,  0x0, 0,   24,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(4294943196, 8000,    147860,  270,  484,  0x0, 0,   24,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(4294954366, 8500,    127330,  0,    484,  0x0, 0,   20,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    192,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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

    DeclMonster(4294955506, 32470,   0,       0x1010000,    "BattleInfo_9A0", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(4294919036, 51700,   0,       0x1010000,    "BattleInfo_810", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294908966, 102750,  0,       0x1010000,    "BattleInfo_8D8", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4294863856, 89080,   4294953296, 0x1010000,    "BattleInfo_748", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294909986, 146680,  0,       0x1010000,    "BattleInfo_9A0", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(4294941566, 141040,  8000,    0x1010000,    "BattleInfo_748", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294884026, 179260,  0,       0x1010000,    "BattleInfo_810", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294933946, 41540,   0,       0x1010000,    "BattleInfo_B04", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(4294904826, 119400,  0,       0x1010000,    "BattleInfo_B04", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(4294884356, 170350,  0,       0x1010000,    "BattleInfo_B04", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(4294892806, 81330,   4294961316, 0x1010000,    "BattleInfo_B04", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(4294944576, 140300,  7990,    0x185010E,    "BattleInfo_C28", 0,   26,  0xFFFF, 10, 11)

    DeclEvent(0x0040, 0, 16,  -22.719999313354492,   140.3000030517578,     7.989999771118164,     16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   2.8399999141693115,    -17.537500381469727,   -1.997499942779541,    1.0])
    DeclEvent(0x0000, 0, 22,  -70.0,                 94.33999633789062,     -1.0800000429153442,   506.25,                [0.06666667014360428,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   4.6666669845581055,    -31.446666717529297,   0.2160000056028366,    1.0])

    DeclActor(4294946196, 8000,    145620,  1200,    4294946196, 9000,    145620,  0x007C, 0,  7,  0x0000)
    DeclActor(4294954366, 8000,    127330,  1200,    4294954366, 9000,    127330,  0x007C, 0,  8,  0x0000)
    DeclActor(4294848456, 4294958296, 105750,  1200,    4294848456, 4294959296, 105750,  0x007C, 0,  9,  0x0000)
    DeclActor(4294945956, 0,       45410,   1200,    4294945956, 0,       45410,   0x007C, 0,  10, 0x0000)
    DeclActor(4294943196, 8000,    147860,  1200,    4294943196, 8000,    147860,  0x007C, 0,  11, 0x0000)
    DeclActor(4294912016, 0,       138630,  1200,    4294912016, 2000,    138630,  0x007C, 0,  14, 0x0000)
    DeclActor(4294913296, 0,       138000,  1200,    4294913296, 2000,    138000,  0x007C, 0,  14, 0x0000)

    PlaceName(-6.0, 0.0, -16.989999771118164, 0x0000, 0x0000, "To Crossbell City")
    PlaceName(-86.0, 0.0, 229.97999572753906, 0x0000, 0x0000, "To Mining Town Mainz")
    PlaceName(-151.4199981689453, 0.0, 100.58000183105469, 0x0000, 0x0000, "To Temple of Moon")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 3])                         # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 9
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 2, 1])                   # 10
    ChipFrameInfo(899, 0, [0, 1, 2, 3, 4])                       # 11

    ScpFunction((
        "Function_0_D9C",          # 00, 0
        "Function_1_DBB",          # 01, 1
        "Function_2_DDA",          # 02, 2
        "Function_3_DF9",          # 03, 3
        "Function_4_E16",          # 04, 4
        "Function_5_135B",         # 05, 5
        "Function_6_18B1",         # 06, 6
        "Function_7_1FD8",         # 07, 7
        "Function_8_212A",         # 08, 8
        "Function_9_2346",         # 09, 9
        "Function_10_24A0",        # 0A, 10
        "Function_11_27FE",        # 0B, 11
        "Function_12_2B5C",        # 0C, 12
        "Function_13_2B7F",        # 0D, 13
        "Function_14_2B83",        # 0E, 14
        "Function_15_2EBC",        # 0F, 15
        "Function_16_2F50",        # 10, 16
        "Function_17_31BA",        # 11, 17
        "Function_18_3607",        # 12, 18
        "Function_19_39FB",        # 13, 19
        "Function_20_3F02",        # 14, 20
        "Function_21_489D",        # 15, 21
        "Function_22_48DF",        # 16, 22
    ))


    def Function_0_D9C(): pass

    label("Function_0_D9C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DBA")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_0_D9C")

    label("loc_DBA")

    Return()

    # Function_0_D9C end

    def Function_1_DBB(): pass

    label("Function_1_DBB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DD9")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_DBB")

    label("loc_DD9")

    Return()

    # Function_1_DBB end

    def Function_2_DDA(): pass

    label("Function_2_DDA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DF8")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_2_DDA")

    label("loc_DF8")

    Return()

    # Function_2_DDA end

    def Function_3_DF9(): pass

    label("Function_3_DF9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E15")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x2, 0x1)
    Jump("Function_3_DF9")

    label("loc_E15")

    Return()

    # Function_3_DF9 end

    def Function_4_E16(): pass

    label("Function_4_E16")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_135A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E77")
    SetScenarioFlags(0x0, 1)
    PlayEffect(0xA, 0xFF, 0xFF, 0x20, -88800, -1000, 192450, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    label("loc_E77")

    SetScenarioFlags(0x0, 1)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x5, 0x800000)
    OP_C4(0x0, 0x1, 0x1, 0x0)

    label("loc_E8D")

    Sleep(15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EE6")
    SetScenarioFlags(0x0, 2)
    PlayEffect(0xA, 0xFF, 0xFF, 0x20, -90600, -1000, 184350, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    label("loc_EE6")

    SetScenarioFlags(0x0, 2)
    SetMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x6, 0x800000)
    OP_C4(0x1, 0x1, 0x1, 0x0)

    label("loc_EFC")

    Sleep(15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F55")
    SetScenarioFlags(0x0, 3)
    PlayEffect(0xA, 0xFF, 0xFF, 0x20, -85120, -1000, 181010, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    label("loc_F55")

    SetScenarioFlags(0x0, 3)
    SetMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x7, 0x800000)
    OP_C4(0x2, 0x1, 0x1, 0x0)

    label("loc_F6B")

    Sleep(15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_FDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FC4")
    SetScenarioFlags(0x0, 4)
    PlayEffect(0xA, 0xFF, 0xFF, 0x20, -79990, -1000, 163480, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    label("loc_FC4")

    SetScenarioFlags(0x0, 4)
    SetMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x8, 0x800000)
    OP_C4(0x3, 0x1, 0x1, 0x0)

    label("loc_FDA")

    Sleep(15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1049")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1033")
    SetScenarioFlags(0x0, 5)
    PlayEffect(0xA, 0xFF, 0xFF, 0x20, -66570, -1000, 155940, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    label("loc_1033")

    SetScenarioFlags(0x0, 5)
    SetMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0x9, 0x800000)
    OP_C4(0x4, 0x1, 0x1, 0x0)

    label("loc_1049")

    Sleep(15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10A2")
    SetScenarioFlags(0x0, 6)
    PlayEffect(0xA, 0xFF, 0xFF, 0x20, -70370, -1000, 145190, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    label("loc_10A2")

    SetScenarioFlags(0x0, 6)
    SetMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xA, 0x800000)
    OP_C4(0x5, 0x1, 0x1, 0x0)

    label("loc_10B8")

    Sleep(15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1127")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1111")
    SetScenarioFlags(0x0, 7)
    PlayEffect(0xA, 0xFF, 0xFF, 0x20, -62710, -1000, 124440, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    label("loc_1111")

    SetScenarioFlags(0x0, 7)
    SetMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xB, 0x800000)
    OP_C4(0x6, 0x1, 0x1, 0x0)

    label("loc_1127")

    Sleep(15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1196")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1180")
    SetScenarioFlags(0x1, 0)
    PlayEffect(0xA, 0xFF, 0xFF, 0x20, -61700, -1000, 106350, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    label("loc_1180")

    SetScenarioFlags(0x1, 0)
    SetMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xC, 0x800000)
    OP_C4(0x7, 0x1, 0x1, 0x0)

    label("loc_1196")

    Sleep(15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1205")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11EF")
    SetScenarioFlags(0x1, 1)
    PlayEffect(0xA, 0xFF, 0xFF, 0x20, -54430, -1000, 89830, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    label("loc_11EF")

    SetScenarioFlags(0x1, 1)
    SetMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xD, 0x800000)
    OP_C4(0x8, 0x1, 0x1, 0x0)

    label("loc_1205")

    Sleep(15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1274")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_125E")
    SetScenarioFlags(0x1, 2)
    PlayEffect(0xA, 0xFF, 0xFF, 0x20, -54220, -1000, 58200, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    label("loc_125E")

    SetScenarioFlags(0x1, 2)
    SetMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xE, 0x800000)
    OP_C4(0x9, 0x1, 0x1, 0x0)

    label("loc_1274")

    Sleep(15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_12E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12CD")
    SetScenarioFlags(0x1, 3)
    PlayEffect(0xA, 0xFF, 0xFF, 0x20, -32170, -1000, 41830, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    label("loc_12CD")

    SetScenarioFlags(0x1, 3)
    SetMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0xF, 0x800000)
    OP_C4(0xA, 0x1, 0x1, 0x0)

    label("loc_12E3")

    Sleep(15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1352")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_133C")
    SetScenarioFlags(0x1, 4)
    PlayEffect(0xA, 0xFF, 0xFF, 0x20, -5660, -1000, 24900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    label("loc_133C")

    SetScenarioFlags(0x1, 4)
    SetMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x10, 0x800000)
    OP_C4(0xB, 0x1, 0x1, 0x0)

    label("loc_1352")

    Sleep(15)
    Jump("Function_4_E16")

    label("loc_135A")

    Return()

    # Function_4_E16 end

    def Function_5_135B(): pass

    label("Function_5_135B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_136F")
    ClearScenarioFlags(0x22, 0)
    Event(0, 17)
    Jump("loc_137E")

    label("loc_136F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_137E")
    ClearScenarioFlags(0x22, 1)
    Event(0, 18)

    label("loc_137E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1394")
    SetMapFlags(0x10000000)
    Event(0, 20)

    label("loc_1394")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1838")
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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1421")
    SetScenarioFlags(0x38, 0)

    label("loc_1421")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1437")
    SetScenarioFlags(0x38, 1)

    label("loc_1437")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_144D")
    SetScenarioFlags(0x38, 2)

    label("loc_144D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1463")
    SetScenarioFlags(0x38, 3)

    label("loc_1463")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1479")
    SetScenarioFlags(0x38, 4)

    label("loc_1479")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_148F")
    SetScenarioFlags(0x38, 5)

    label("loc_148F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14A5")
    SetScenarioFlags(0x38, 6)

    label("loc_14A5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14BB")
    SetScenarioFlags(0x38, 7)

    label("loc_14BB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D1")
    SetScenarioFlags(0x39, 0)

    label("loc_14D1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14E7")
    SetScenarioFlags(0x39, 1)

    label("loc_14E7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14FD")
    SetScenarioFlags(0x39, 2)

    label("loc_14FD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1513")
    SetScenarioFlags(0x39, 3)

    label("loc_1513")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1529")
    SetScenarioFlags(0x39, 4)

    label("loc_1529")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_153F")
    SetScenarioFlags(0x39, 5)

    label("loc_153F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1555")
    SetScenarioFlags(0x39, 6)

    label("loc_1555")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_156B")
    SetScenarioFlags(0x39, 7)

    label("loc_156B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1581")
    SetScenarioFlags(0x3A, 0)

    label("loc_1581")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1597")
    SetScenarioFlags(0x3A, 1)

    label("loc_1597")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15AD")
    SetScenarioFlags(0x3A, 2)

    label("loc_15AD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15C3")
    SetScenarioFlags(0x3A, 3)

    label("loc_15C3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15D9")
    SetScenarioFlags(0x3A, 4)

    label("loc_15D9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15EF")
    SetScenarioFlags(0x3A, 5)

    label("loc_15EF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1605")
    SetScenarioFlags(0x3A, 6)

    label("loc_1605")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_161B")
    SetScenarioFlags(0x3A, 7)

    label("loc_161B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1631")
    SetScenarioFlags(0x3B, 0)

    label("loc_1631")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1647")
    SetScenarioFlags(0x3B, 1)

    label("loc_1647")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_165D")
    SetScenarioFlags(0x3B, 2)

    label("loc_165D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1673")
    SetScenarioFlags(0x3B, 3)

    label("loc_1673")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1689")
    SetScenarioFlags(0x3B, 4)

    label("loc_1689")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_169F")
    SetScenarioFlags(0x3B, 5)

    label("loc_169F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16B5")
    SetScenarioFlags(0x3B, 6)

    label("loc_16B5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16CB")
    SetScenarioFlags(0x3B, 7)

    label("loc_16CB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16E1")
    SetScenarioFlags(0x3D, 5)

    label("loc_16E1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16F7")
    SetScenarioFlags(0x3D, 6)

    label("loc_16F7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_170D")
    SetScenarioFlags(0x3D, 7)

    label("loc_170D")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1748")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_1838")

    label("loc_1748")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_176B")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_1838")

    label("loc_176B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_178E")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_1838")

    label("loc_178E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17B1")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_1838")

    label("loc_17B1")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17D4")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_1838")

    label("loc_17D4")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17F7")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_1838")

    label("loc_17F7")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_181A")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_1838")

    label("loc_181A")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1838")
    SetScenarioFlags(0x3C, 7)

    label("loc_1838")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_186A")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_186A")
    SetChrPos(0x0, -56050, 0, 138420, 270)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 15)

    label("loc_186A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_189D")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_189D")
    SetChrPos(0x0, -54000, 0, 138000, 270)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_189D")

    Call(0, 12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18B0")
    OP_E2(0x1)

    label("loc_18B0")

    Return()

    # Function_5_135B end

    def Function_6_18B1(): pass

    label("Function_6_18B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_18C3")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_18EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18E5")
    ClearChrFlags(0x24, 0x80)
    ModifyEventFlags(1, 0, 0x80)
    SetChrFlags(0x24, 0x8000)

    label("loc_18E5")

    ClearChrBattleFlags(0x24, 0x8000)
    Jump("loc_18F9")

    label("loc_18EF")

    SetChrFlags(0x24, 0x80)
    ModifyEventFlags(0, 0, 0x80)

    label("loc_18F9")

    OP_52(0x20, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0x24, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MiniGame(0x2F, 0x5, 0x6, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E8D")
    OP_70(0x0, 0x0)
    Jump("loc_1E91")

    label("loc_1E8D")

    OP_70(0x0, 0x1E)

    label("loc_1E91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EA4")
    OP_70(0x1, 0x0)
    Jump("loc_1EA8")

    label("loc_1EA4")

    OP_70(0x1, 0x1E)

    label("loc_1EA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EBB")
    OP_70(0x2, 0x0)
    Jump("loc_1EBF")

    label("loc_1EBB")

    OP_70(0x2, 0x1E)

    label("loc_1EBF")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F20")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, -21340, 0, 45410, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)

    label("loc_1F20")

    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F6C")
    PlayEffect(0x10, 0xA, 0xFF, 0x0, -24100, 8000, 147860, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x4, 0x1)

    label("loc_1F6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FA1")
    LoadEffect(0xA, "map/mpr2050.eff")
    LoadEffect(0x9, "map/mpcave2.eff")
    Call(0, 19)

    label("loc_1FA1")

    OP_1C(0x0, 0x15, 0x0, 0x32, 0x0, 0xD, 0x0, 0x0)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FC4")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_1FC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FD7")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_1FD7")

    Return()

    # Function_6_18B1 end

    def Function_7_1FD8(): pass

    label("Function_7_1FD8")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20D4")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x46, 1)"), scpexpr(EXPR_END)), "loc_205D")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x46),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E7, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_20CF")

    label("loc_205D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x46),
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

    label("loc_20CF")

    Jump("loc_211E")

    label("loc_20D4")

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

    label("loc_211E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1FD8 end

    def Function_8_212A(): pass

    label("Function_8_212A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22FB")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x216, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_222D")
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xC, 0x0, 0)
    OP_98(0xC, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_2187():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2187)

    def lambda_21A1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_21A1)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xC, 1)
    Battle("BattleInfo_C6C", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_220E"),
        (2, "loc_221D"),
        (1, "loc_222A"),
        (SWITCH_DEFAULT, "loc_222D"),
    )


    label("loc_220E")

    SetScenarioFlags(0x216, 2)
    OP_70(0x1, 0x1E)
    Sleep(500)
    Jump("loc_222D")

    label("loc_221D")

    OP_70(0x1, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_222A")

    OP_B9(0x0)
    Return()

    label("loc_222D")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x8C, 1)"), scpexpr(EXPR_END)), "loc_2286")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x8C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E7, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_22F6")

    label("loc_2286")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x8C),
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

    label("loc_22F6")

    Jump("loc_233A")

    label("loc_22FB")

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

    label("loc_233A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_212A end

    def Function_9_2346(): pass

    label("Function_9_2346")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2470")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x2, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 60)
    AddSepith(0x1, 60)
    AddSepith(0x2, 60)
    AddSepith(0x3, 60)
    AddSepith(0x4, 60)
    AddSepith(0x5, 60)
    AddSepith(0x6, 60)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56IEarth Sepith x60\x01\x07\x02",
            "#57IWater Sepith x60\x01\x07\x02",
            "#58IFire Sepith x60\x01\x07\x02",
            "#59IWind Sepith x60\x01\x07\x02",
            "#60ITime Sepith x60\x01\x07\x02",
            "#61ISpace Sepith x60\x01\x07\x02",
            "#62IMirage Sepith x60\x01\x07\x00",
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1E7, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_248E")

    label("loc_2470")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The chest is empty.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_248E")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_2346 end

    def Function_10_24A0(): pass

    label("Function_10_24A0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2658")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 1)), scpexpr(EXPR_END)), "loc_2639")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2634")
    ClearScenarioFlags(0x3B, 1)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 1)), scpexpr(EXPR_END)), "loc_2631")
    ClearScenarioFlags(0x39, 1)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2556():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2556)
    TurnDirection(0x8, 0x0, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    PlayEffect(0x7, 0x1, 0x8, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_BA0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_262C")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2613")
    Call(1, 5)
    Jump("loc_262C")

    label("loc_2613")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2629")
    Call(1, 4)
    Jump("loc_262C")

    label("loc_2629")

    Call(1, 3)

    label("loc_262C")

    Jump("loc_2634")

    label("loc_2631")

    Call(1, 1)

    label("loc_2634")

    Jump("loc_264F")

    label("loc_2639")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 1)), scpexpr(EXPR_END)), "loc_264F")
    ClearScenarioFlags(0x39, 1)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_264F")

    TalkEnd(0xFF)
    Return()

    label("loc_2658")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 1)), scpexpr(EXPR_END)), "loc_27E3")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27DE")
    ClearScenarioFlags(0x3B, 1)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 1)), scpexpr(EXPR_END)), "loc_27DB")
    ClearScenarioFlags(0x39, 1)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2700():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2700)
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
    Battle("BattleInfo_BE4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27D6")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_27BD")
    Call(1, 5)
    Jump("loc_27D6")

    label("loc_27BD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_27D3")
    Call(1, 4)
    Jump("loc_27D6")

    label("loc_27D3")

    Call(1, 3)

    label("loc_27D6")

    Jump("loc_27DE")

    label("loc_27DB")

    Call(1, 1)

    label("loc_27DE")

    Jump("loc_27F9")

    label("loc_27E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 1)), scpexpr(EXPR_END)), "loc_27F9")
    ClearScenarioFlags(0x39, 1)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_27F9")

    TalkEnd(0xFF)
    Return()

    # Function_10_24A0 end

    def Function_11_27FE(): pass

    label("Function_11_27FE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_29B6")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 2)), scpexpr(EXPR_END)), "loc_2997")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2992")
    ClearScenarioFlags(0x3B, 2)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 2)), scpexpr(EXPR_END)), "loc_298F")
    ClearScenarioFlags(0x39, 2)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_28B4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_28B4)
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
    Battle("BattleInfo_BA0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_298A")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2971")
    Call(1, 5)
    Jump("loc_298A")

    label("loc_2971")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2987")
    Call(1, 4)
    Jump("loc_298A")

    label("loc_2987")

    Call(1, 3)

    label("loc_298A")

    Jump("loc_2992")

    label("loc_298F")

    Call(1, 1)

    label("loc_2992")

    Jump("loc_29AD")

    label("loc_2997")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 2)), scpexpr(EXPR_END)), "loc_29AD")
    ClearScenarioFlags(0x39, 2)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_29AD")

    TalkEnd(0xFF)
    Return()

    label("loc_29B6")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 2)), scpexpr(EXPR_END)), "loc_2B41")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B3C")
    ClearScenarioFlags(0x3B, 2)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 2)), scpexpr(EXPR_END)), "loc_2B39")
    ClearScenarioFlags(0x39, 2)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2A5E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2A5E)
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
    Battle("BattleInfo_BE4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B34")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2B1B")
    Call(1, 5)
    Jump("loc_2B34")

    label("loc_2B1B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2B31")
    Call(1, 4)
    Jump("loc_2B34")

    label("loc_2B31")

    Call(1, 3)

    label("loc_2B34")

    Jump("loc_2B3C")

    label("loc_2B39")

    Call(1, 1)

    label("loc_2B3C")

    Jump("loc_2B57")

    label("loc_2B41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 2)), scpexpr(EXPR_END)), "loc_2B57")
    ClearScenarioFlags(0x39, 2)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_2B57")

    TalkEnd(0xFF)
    Return()

    # Function_11_27FE end

    def Function_12_2B5C(): pass

    label("Function_12_2B5C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2B7E")
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)

    label("loc_2B7E")

    Return()

    # Function_12_2B5C end

    def Function_13_2B7F(): pass

    label("Function_13_2B7F")

    Call(1, 6)
    Return()

    # Function_13_2B7F end

    def Function_14_2B83(): pass

    label("Function_14_2B83")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BB5")
    SetScenarioFlags(0x31, 2)

    label("loc_2BB5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2BFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_2BF5")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2BEA")
    Sound(2499, 255, 100, 0)
    Jump("loc_2BF0")

    label("loc_2BEA")

    Sound(3537, 255, 100, 0)

    label("loc_2BF0")

    Jump("loc_2BFB")

    label("loc_2BF5")

    Sound(3344, 255, 100, 0)

    label("loc_2BFB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_2C6E")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2C4E"),
        (SWITCH_DEFAULT, "loc_2C5F"),
    )


    label("loc_2C4E")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_2C69")

    label("loc_2C5F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C69")

    Jump("loc_2EA9")

    label("loc_2C6E")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_2CA0")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_2CA0")

    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2CD2"),
        (1, "loc_2DD6"),
        (2, "loc_2E67"),
        (SWITCH_DEFAULT, "loc_2E9F"),
    )


    label("loc_2CD2")

    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    OP_74(0x3, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D03")
    OP_70(0x3, 0x12C)
    OP_71(0x3, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_2D13")

    label("loc_2D03")

    OP_70(0x3, 0xF0)
    OP_71(0x3, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_2D13")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D69")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D69")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D8C")
    Sound(461, 0, 100, 0)

    label("loc_2D8C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2DAC")
    OP_70(0x3, 0x14A)
    OP_71(0x3, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_2DBC")

    label("loc_2DAC")

    OP_70(0x3, 0x10E)
    OP_71(0x3, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_2DBC")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x3, "light", 0x1, 0x1)
    OP_70(0x3, 0x0)
    Jump("loc_2BFB")

    label("loc_2DD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_2E48")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_2E0B")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_2E23")

    label("loc_2E0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2E1E")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_2E23")

    label("loc_2E1E")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_2E23")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E62")

    label("loc_2E48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2E58")
    OP_AF(0xFB)
    Jump("loc_2E62")

    label("loc_2E58")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E62")

    Jump("loc_2EA9")

    label("loc_2E67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E80")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E9A")

    label("loc_2E80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2E90")
    OP_AF(0xFB)
    Jump("loc_2E9A")

    label("loc_2E90")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E9A")

    Jump("loc_2EA9")

    label("loc_2E9F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2EA9")

    Jump("loc_2BFB")

    label("loc_2EAE")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_14_2B83 end

    def Function_15_2EBC(): pass

    label("Function_15_2EBC")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_2F17")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2F0C")
    Sound(2502, 255, 100, 0)
    Jump("loc_2F12")

    label("loc_2F0C")

    Sound(2503, 255, 100, 0)

    label("loc_2F12")

    Jump("loc_2F3B")

    label("loc_2F17")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2F35")
    Sound(3347, 255, 100, 0)
    Jump("loc_2F3B")

    label("loc_2F35")

    Sound(3348, 255, 100, 0)

    label("loc_2F3B")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_15_2EBC end

    def Function_16_2F50(): pass

    label("Function_16_2F50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21D, 4)), scpexpr(EXPR_END)), "loc_2F5A")
    Return()

    label("loc_2F5A")

    EventBegin(0x1)
    OP_52(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    SetChrSubChip(0x4, 0x0)
    SetChrSubChip(0x5, 0x0)
    SetChrSubChip(0x6, 0x0)
    SetChrSubChip(0x7, 0x0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A large monster is wandering about.\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Exterminate]\x01",      # 0
            "[Quit]\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_3036"),
        (SWITCH_DEFAULT, "loc_304F"),
    )


    label("loc_3036")

    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, -27610, 7990, 141110, 270)
    EventEnd(0x5)
    Return()

    label("loc_304F")

    Battle("BattleInfo_C28", 0x0, 0x0, 0x100, 0xC, 0xFF)
    OP_E2(0x2)
    EventBegin(0x1)
    OP_68(-27610, 8990, 141110, 0)
    OP_90(0x0, -27610, 7990, 141110, 270)
    OP_90(0x1, -27610, 7990, 141110, 270)
    OP_90(0x2, -27610, 7990, 141110, 270)
    OP_90(0x3, -27610, 7990, 141110, 270)
    OP_90(0x4, -27610, 7990, 141110, 270)
    OP_90(0x5, -27610, 7990, 141110, 270)
    OP_90(0x6, -27610, 7990, 141110, 270)
    OP_90(0x7, -27610, 7990, 141110, 270)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_3111"),
        (1, "loc_3116"),
        (SWITCH_DEFAULT, "loc_3119"),
    )


    label("loc_3111")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    label("loc_3116")

    OP_B9(0x0)
    Return()

    label("loc_3119")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x24, 0x80)
    OP_E2(0x3)
    Sleep(400)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Wanted Monster exterminated!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x67),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddItemNumber(0x67, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x21D, 4)
    OP_29(0x98, 0x4, 0x2)
    OP_29(0x98, 0x4, 0x10)
    OP_29(0x98, 0x1, 0x0)
    OP_E2(0x2)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_16_2F50 end

    def Function_17_31BA(): pass

    label("Function_17_31BA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("apl/ch50515.itc", 0x1E)
    LoadEffect(0x0, "event/ev14001.eff")
    SoundLoad(868)
    SoundLoad(863)
    SoundLoad(864)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xF, 0x1E)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    OP_52(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x16, 0x80)
    OP_78(0x11, 0x16)
    OP_49()
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x11, 0x1000)
    OP_74(0x11, 0x1E)
    OP_71(0x11, 0x3D, 0x78, 0x0, 0x20)
    ClearChrFlags(0x17, 0x80)
    OP_78(0x12, 0x17)
    OP_49()
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x12, 0x1000)
    OP_74(0x12, 0x1E)
    OP_71(0x12, 0x3D, 0x78, 0x0, 0x20)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x13, 0x18)
    OP_49()
    ClearMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x13, 0x1000)
    OP_74(0x13, 0x1E)
    OP_71(0x13, 0x3D, 0x78, 0x0, 0x20)
    OP_7D(0xFF, 0xA0, 0x96, 0x0, 0x0)
    SetChrPos(0x16, -89850, 0, 202000, 270)
    SetChrPos(0xE, -90000, 0, 206650, 0)
    PlayEffect(0x0, 0x0, 0xE, 0x5, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0xF, 0x5, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_68(-90100, 1100, 205600, 0)
    MoveCamera(50, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20000, 0)
    OP_68(-89900, 2000, 201900, 3000)
    MoveCamera(65, 30, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(21500, 3000)
    Sound(868, 2, 50, 0)
    Sound(863, 2, 50, 0)
    Sound(864, 2, 50, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    SetMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x11, 0x1000)
    SetChrPos(0x18, -71000, 0, 152150, 275)
    SetChrPos(0xE, -72000, 0, 157200, 315)
    SetChrPos(0xF, -68850, 0, 147550, 90)
    PlayEffect(0x0, 0x0, 0xE, 0x5, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0xF, 0x5, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_68(-73500, 1400, 156000, 0)
    MoveCamera(50, 18, -5, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    OP_68(-69500, 1400, 153700, 4000)
    MoveCamera(50, 18, -5, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(16500, 4000)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    SetMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x13, 0x1000)
    SetChrPos(0x17, -32900, 0, 42000, 225)
    SetChrPos(0xE, -33200, 0, 38100, 315)
    SetChrPos(0xF, -30450, 0, 40200, 90)
    PlayEffect(0x0, 0x0, 0xE, 0x5, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0xF, 0x5, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_68(-33700, 1700, 41100, 0)
    MoveCamera(355, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    OP_68(-33150, 1700, 41650, 3000)
    MoveCamera(15, 20, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(15500, 3000)
    Sleep(2000)
    StopSound(863, 1000, 50)
    StopSound(864, 1000, 50)
    OP_24(0x364)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("r2030", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_31BA end

    def Function_18_3607(): pass

    label("Function_18_3607")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch41900.itc", 0x23)
    LoadChrToIndex("chr/ch41950.itc", 0x24)
    LoadChrToIndex("chr/ch41951.itc", 0x25)
    LoadChrToIndex("chr/ch03400.itc", 0x28)
    LoadChrToIndex("chr/ch03450.itc", 0x29)
    LoadChrToIndex("chr/ch03451.itc", 0x2A)
    SoundLoad(863)
    SoundLoad(864)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrChipByIndex(0x10, 0x23)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x24)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x24)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x28)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    OP_7D(0xFF, 0xA0, 0x96, 0x0, 0x0)
    SetMapObjFrame(0xFF, "glow_3", 0x0, 0x1)
    ClearMapObjFlags(0x14, 0x4)
    SetChrPos(0x15, -2000, 0, -3500, 180)
    SetChrPos(0x10, -2000, 0, -1000, 180)
    SetChrPos(0x11, -1000, 0, 1000, 180)
    SetChrPos(0x12, -3000, 0, 1000, 180)
    SetChrPos(0x13, -1000, 0, 2500, 180)
    SetChrPos(0x14, -3000, 0, 2500, 180)
    OP_68(-2000, 1000, -5500, 0)
    MoveCamera(50, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20000, 0)
    OP_68(-2000, 1000, -2500, 2000)
    MoveCamera(50, 25, 0, 2000)
    SetCameraDistance(19000, 2000)
    Sound(863, 2, 50, 0)
    Sound(864, 2, 50, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x10,
        (
            "#5P...Captain.\x01",
            "What do we do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#04606F#5PHmm, right.\x02\x03",
            "#04600FStanding firm here is annoying,\x01",
            "so I'll go have fun a little.\x02\x03",
            "Please follow me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#5PJaー.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5PFollow the Captain.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-2000, 1000, -3500, 800)
    SetCameraDistance(14700, 800)
    Sleep(300)
    Sound(358, 0, 100, 0)
    SetChrChipByIndex(0x15, 0x29)
    SetChrSubChip(0x15, 0x0)
    OP_0D()
    Sound(531, 0, 100, 0)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x15,
        (
            "#04604F#5PWell now, "Testa-Rossa".\x01",
            "There're still prey remaining...\x02\x03",
            "#04602FLet's have a ton\x01",
            "of fun together!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrChipByIndex(0x15, 0x2A)

    def lambda_392C():
        OP_9B(0x0, 0x15, 0x0, 0x2710, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_392C)
    OP_93(0x10, 0xB4, 0x1F4)
    SetChrChipByIndex(0x10, 0x25)
    SetChrChipByIndex(0x11, 0x25)
    SetChrChipByIndex(0x12, 0x25)
    SetChrChipByIndex(0x13, 0x25)
    SetChrChipByIndex(0x14, 0x25)
    FadeToDark(500, 0, -1)

    def lambda_3966():
        OP_9B(0x0, 0x10, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_3966)
    Sleep(50)

    def lambda_397E():
        OP_9B(0x0, 0x11, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_397E)
    Sleep(50)

    def lambda_3996():
        OP_9B(0x0, 0x12, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_3996)
    Sleep(50)

    def lambda_39AE():
        OP_9B(0x0, 0x13, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_39AE)
    Sleep(50)

    def lambda_39C6():
        OP_9B(0x0, 0x14, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_39C6)
    Sleep(50)
    WaitChrThread(0x10, 0)
    WaitChrThread(0x11, 0)
    WaitChrThread(0x12, 0)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x14, 0)
    OP_0D()
    SetScenarioFlags(0x22, 4)
    NewScene("r2030", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_18_3607 end

    def Function_19_39FB(): pass

    label("Function_19_39FB")

    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_11(0x0, 0x0, 0x0, 0x19, 0x28, 0x0)
    SetMapObjFrame(0xFF, "object09_lantern", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model07_light", 0x0, 0x1)
    BeginChrThread(0xD, 0, 0, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 4)), scpexpr(EXPR_END)), "loc_3A81")
    SetScenarioFlags(0x0, 1)

    label("loc_3A81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AD6")
    OP_C3(0x0, 0x3, 0x2, 0x1194, 0x6E, 0x1, -88800, -1000, 192450, 2000, 2000, 0)
    OP_C4(0x0, 0x2, 0x3, 0xD90)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x5, 0x10000000)
    SetMapObjFlags(0x5, 0x800000)
    OP_1C(0x0, 0x5, 0x0, 0x0, 0x0, 0x0, 0xD9C, 0x0)

    label("loc_3AD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 5)), scpexpr(EXPR_END)), "loc_3AE2")
    SetScenarioFlags(0x0, 2)

    label("loc_3AE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B37")
    OP_C3(0x1, 0x3, 0x2, 0x1194, 0x6E, 0x1, -90600, -1000, 184350, 2000, 2000, 0)
    OP_C4(0x1, 0x2, 0x3, 0xD91)
    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x6, 0x10000000)
    SetMapObjFlags(0x6, 0x800000)
    OP_1C(0x0, 0x6, 0x0, 0x0, 0x0, 0x0, 0xD9D, 0x0)

    label("loc_3B37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 6)), scpexpr(EXPR_END)), "loc_3B43")
    SetScenarioFlags(0x0, 3)

    label("loc_3B43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B98")
    OP_C3(0x2, 0x3, 0x2, 0x1194, 0x6E, 0x1, -85120, -1000, 181010, 2000, 2000, 0)
    OP_C4(0x2, 0x2, 0x3, 0xD92)
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x7, 0x10000000)
    SetMapObjFlags(0x7, 0x800000)
    OP_1C(0x0, 0x7, 0x0, 0x0, 0x0, 0x0, 0xD9E, 0x0)

    label("loc_3B98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 7)), scpexpr(EXPR_END)), "loc_3BA4")
    SetScenarioFlags(0x0, 4)

    label("loc_3BA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BF9")
    OP_C3(0x3, 0x3, 0x2, 0x1194, 0x6E, 0x1, -79990, -1000, 163480, 2000, 2000, 0)
    OP_C4(0x3, 0x2, 0x3, 0xD93)
    ClearMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x8, 0x10000000)
    SetMapObjFlags(0x8, 0x800000)
    OP_1C(0x0, 0x8, 0x0, 0x0, 0x0, 0x0, 0xD9F, 0x0)

    label("loc_3BF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 0)), scpexpr(EXPR_END)), "loc_3C05")
    SetScenarioFlags(0x0, 5)

    label("loc_3C05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C5A")
    OP_C3(0x4, 0x3, 0x2, 0x1194, 0x6E, 0x1, -66570, -1000, 155940, 2000, 2000, 0)
    OP_C4(0x4, 0x2, 0x3, 0xD94)
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x10000000)
    SetMapObjFlags(0x9, 0x800000)
    OP_1C(0x0, 0x9, 0x0, 0x0, 0x0, 0x0, 0xDA0, 0x0)

    label("loc_3C5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 1)), scpexpr(EXPR_END)), "loc_3C66")
    SetScenarioFlags(0x0, 6)

    label("loc_3C66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3CBB")
    OP_C3(0x5, 0x3, 0x2, 0x1194, 0x6E, 0x1, -70370, -1000, 145190, 2000, 2000, 0)
    OP_C4(0x5, 0x2, 0x3, 0xD95)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x10000000)
    SetMapObjFlags(0xA, 0x800000)
    OP_1C(0x0, 0xA, 0x0, 0x0, 0x0, 0x0, 0xDA1, 0x0)

    label("loc_3CBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 2)), scpexpr(EXPR_END)), "loc_3CC7")
    SetScenarioFlags(0x0, 7)

    label("loc_3CC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D1C")
    OP_C3(0x6, 0x3, 0x2, 0x1194, 0x6E, 0x1, -62710, -1000, 124440, 2000, 2000, 0)
    OP_C4(0x6, 0x2, 0x3, 0xD96)
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xB, 0x10000000)
    SetMapObjFlags(0xB, 0x800000)
    OP_1C(0x0, 0xB, 0x0, 0x0, 0x0, 0x0, 0xDA2, 0x0)

    label("loc_3D1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 3)), scpexpr(EXPR_END)), "loc_3D28")
    SetScenarioFlags(0x1, 0)

    label("loc_3D28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D7D")
    OP_C3(0x7, 0x3, 0x2, 0x1194, 0x6E, 0x1, -61700, -1000, 106350, 2000, 2000, 0)
    OP_C4(0x7, 0x2, 0x3, 0xD97)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x10000000)
    SetMapObjFlags(0xC, 0x800000)
    OP_1C(0x0, 0xC, 0x0, 0x0, 0x0, 0x0, 0xDA3, 0x0)

    label("loc_3D7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 4)), scpexpr(EXPR_END)), "loc_3D89")
    SetScenarioFlags(0x1, 1)

    label("loc_3D89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DDE")
    OP_C3(0x8, 0x3, 0x2, 0x1194, 0x6E, 0x1, -54430, -1000, 89830, 2000, 2000, 0)
    OP_C4(0x8, 0x2, 0x3, 0xD98)
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x10000000)
    SetMapObjFlags(0xD, 0x800000)
    OP_1C(0x0, 0xD, 0x0, 0x0, 0x0, 0x0, 0xDA4, 0x0)

    label("loc_3DDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 5)), scpexpr(EXPR_END)), "loc_3DEA")
    SetScenarioFlags(0x1, 2)

    label("loc_3DEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E3F")
    OP_C3(0x9, 0x3, 0x2, 0x1194, 0x6E, 0x1, -54220, -1000, 58200, 2000, 2000, 0)
    OP_C4(0x9, 0x2, 0x3, 0xD99)
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x10000000)
    SetMapObjFlags(0xE, 0x800000)
    OP_1C(0x0, 0xE, 0x0, 0x0, 0x0, 0x0, 0xDA5, 0x0)

    label("loc_3E3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 6)), scpexpr(EXPR_END)), "loc_3E4B")
    SetScenarioFlags(0x1, 3)

    label("loc_3E4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EA0")
    OP_C3(0xA, 0x3, 0x2, 0x1194, 0x6E, 0x1, -32170, -1000, 41830, 2000, 2000, 0)
    OP_C4(0xA, 0x2, 0x3, 0xD9A)
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xF, 0x10000000)
    SetMapObjFlags(0xF, 0x800000)
    OP_1C(0x0, 0xF, 0x0, 0x0, 0x0, 0x0, 0xDA6, 0x0)

    label("loc_3EA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 7)), scpexpr(EXPR_END)), "loc_3EAC")
    SetScenarioFlags(0x1, 4)

    label("loc_3EAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F01")
    OP_C3(0xB, 0x3, 0x2, 0x1194, 0x6E, 0x1, -5660, -1000, 24900, 2000, 2000, 0)
    OP_C4(0xB, 0x2, 0x3, 0xD9B)
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x10, 0x10000000)
    SetMapObjFlags(0x10, 0x800000)
    OP_1C(0x0, 0x10, 0x0, 0x0, 0x0, 0x0, 0xDA7, 0x0)

    label("loc_3F01")

    Return()

    # Function_19_39FB end

    def Function_20_3F02(): pass

    label("Function_20_3F02")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    OP_E2(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F26")
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)

    label("loc_3F26")

    LoadChrToIndex("chr/ch03256.itc", 0x1E)
    LoadChrToIndex("apl/ch51608.itc", 0x1F)
    LoadEffect(0x0, "event/ev17049.eff")
    SetChrPos(0x101, -2000, 0, 1000, 0)
    SetChrPos(0x106, -1150, 0, 0, 0)
    SetChrPos(0x103, -3350, 0, -1000, 0)
    SetChrPos(0x107, -4600, 0, -1750, 0)
    SetChrPos(0x105, -2000, 0, -2450, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(-2000, 1000, 0, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20000, 0)
    OP_68(-2000, 1000, 2500, 2500)
    MoveCamera(45, 25, 0, 2500)
    OP_6E(510, 2500)
    SetCameraDistance(18860, 2500)

    def lambda_4006():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4006)
    Sleep(50)

    def lambda_401E():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_401E)
    Sleep(50)

    def lambda_4036():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4036)
    Sleep(50)

    def lambda_404E():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_404E)
    Sleep(50)

    def lambda_4066():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_4066)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    BeginChrThread(0x101, 2, 0, 21)
    WaitChrThread(0x106, 1)
    BeginChrThread(0x106, 2, 0, 21)
    WaitChrThread(0x103, 1)
    BeginChrThread(0x103, 2, 0, 21)
    WaitChrThread(0x105, 1)
    BeginChrThread(0x105, 2, 0, 21)
    WaitChrThread(0x107, 1)
    SetChrSubChip(0x107, 0x5)
    OP_0D()
    Sleep(2000)
    EndChrThread(0x101, 0x2)

    def lambda_40BD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_40BD)
    EndChrThread(0x106, 0x2)

    def lambda_40CE():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_40CE)
    EndChrThread(0x103, 0x2)

    def lambda_40DF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_40DF)
    EndChrThread(0x105, 0x2)

    def lambda_40F0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_40F0)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x106, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x105, 2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00011F#11PWhat...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10408F#12PIt looks like the illumination\x01",
            "was cut...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10701F#11P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#12P...? (This is...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#01201F#12P#3CHmm...\x02",
    )

    CloseMessageWindow()

    def lambda_41BC():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_41BC)
    OP_68(-2009, 1000, 4600, 2000)
    MoveCamera(43, 24, 0, 2000)
    OP_6E(510, 2000)
    SetCameraDistance(17000, 2000)
    Sleep(1000)
    Sound(853, 0, 100, 0)
    Sleep(500)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    EndChrThread(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(2087, 255, 100, 0)

    ChrTalk(
        0x101,
        "#00011F#11P#5AHuh──\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00207F#12P#5A#NMr. Lloyd!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(540, 0, 50, 0)

    def lambda_42C9():

        label("loc_42C9")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_42C9")

    QueueWorkItem2(0x106, 2, lambda_42C9)
    SetChrChipByIndex(0x106, 0x1E)
    SetChrSubChip(0x106, 0x4)
    Sound(3204, 255, 80, 0)

    ChrTalk(
        0x106,
        "#10707F#11P#5AKh...\x02",
    )

    Sleep(500)
    Sound(250, 0, 40, 0)
    Sound(307, 0, 100, 0)
    SetChrSubChip(0x106, 0x2)
    PlayEffect(0x0, 0x0, 0x106, 0x5, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0x101, 0, 0, 0, 0)
    Sleep(500)
    EndChrThread(0x101, 0x1)
    Sound(308, 0, 100, 0)
    OP_82(0x190, 0x190, 0xBB8, 0x3E8)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    PlayEffect(0xA, 0xFF, 0x101, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(196, 0, 100, 0)
    OP_68(-1660, 1000, 3060, 800)
    MoveCamera(40, 25, 0, 800)
    OP_6E(510, 800)

    def lambda_43D7():
        OP_9A(0xFE, 0x106, 0x1F4, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_43D7)

    def lambda_43EB():
        OP_95(0xFE, -3500, 0, 3000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_43EB)
    Sound(2031, 255, 100, 0)

    ChrTalk(
        0x101,
        "#00015F#11P#6AUoh...!\x02",
    )

    WaitChrThread(0x101, 1)
    EndChrThread(0x106, 0x2)
    CancelBlur(500)
    Sound(811, 0, 60, 0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x106, 0x4)
    Sleep(1000)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)

    def lambda_4454():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4454)
    Sleep(50)

    def lambda_4464():
        TurnDirection(0x107, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_4464)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x107, 0)
    SetChrSubChip(0x107, 0x5)

    ChrTalk(
        0x103,
        "#00207F#6PMr. Lloyd...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5P#30WKh...I'm fine.\x02\x03",
            "#00008F...Thank you.\x01",
            "You saved me, Rixia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10710F#11PNo...\x01",
            "I'm glad I made it in time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#12P*sigh*, oh boy.\x02\x03",
            "#10401FStill...was that one a mine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6PYes...it seemed a contact\x01",
            "type orbal mine.\x02\x03",
            "#00201FThe explosive power was weak, so\x01",
            "I think it was an antipersonnel one...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01201F#6P#3CIt looks like they're scattered\x01",
            "throughout the entire tunnel.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(802, 0, 100, 0)
    OP_93(0x101, 0x10E, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    OP_0D()

    def lambda_465E():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_465E)
    OP_9B(0x1, 0x106, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)

    ChrTalk(
        0x101,
        (
            "#00006F#5PKh, to set such things\x01",
            "on a public road...\x02\x03",
            "#00013FMaybe they're meant to cut off\x01",
            "the Resistance's retreat?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10703F#11PIt's very likely.\x02\x03",
            "#10708FIt was set up in earnest with\x01",
            "the intention of mopping them up...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#5P──We don't have time.\x01",
            "Let's get through this.\x02\x03",
            "#00007FLet's advance with prudence but quickly,\x01",
            "paying attention to where we put our feet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#6PRoger that...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#12POh boy.\x01",
            "What a pain this is.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_49()
    OP_37()
    SetChrPos(0x0, -2000, 0, 4000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A2, 4)
    OP_29(0xAF, 0x1, 0xB)
    ClearMapFlags(0x10000000)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_20_3F02 end

    def Function_21_489D(): pass

    label("Function_21_489D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48BA")
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(500)

    label("loc_48BA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_48DE")
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(500)
    Jump("loc_48BA")

    label("loc_48DE")

    Return()

    # Function_21_489D end

    def Function_22_48DF(): pass

    label("Function_22_48DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_495A")
    EventBegin(0x1)
    OP_E2(0x3)

    ChrTalk(
        0x101,
        (
            "#00000FThe "Temple" area is this way.\x01",
            "Let's hurry up to the Mainz region now.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -70120, 0, 99240, 0)
    OP_E2(0x2)
    EventEnd(0x4)

    label("loc_495A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BCC")
    EventBegin(0x0)
    Fade(500)
    OP_E2(0x3)
    OP_68(-72420, 2500, 95810, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21210, 0)
    SetChrPos(0x0, -70560, 0, 97340, 179)
    SetChrPos(0x1, -68710, 0, 98170, 179)
    SetChrPos(0x2, -71980, 0, 98170, 179)
    SetChrPos(0x3, -69810, 0, 99060, 179)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FIf we proceed on this road...\x01",
            "There should be the ruins of  the\x01",
            "Middle Ages "Temple of Moon", right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYes, previously I was allowed to\x01",
            "investigate it together with you all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FEeh, that happened?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FAt any rate, at present we also\x01",
            "have a request from the Town Mayor.\x02\x03",
            "We don't have the time on our hands\x01",
            "to explore the area over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYou're right, let's come another time\x01",
            "even just to see how the situation is.\x02",
        )
    )

    CloseMessageWindow()
    OP_E2(0x2)
    SetScenarioFlags(0x0, 0)
    EventEnd(0x5)
    Jump("loc_4C5E")

    label("loc_4BCC")

    EventBegin(0x1)
    OP_E2(0x3)

    ChrTalk(
        0x101,
        (
            "#00000FIt looks like we don't have the leisure\x01",
            "to explore the ruins area.\x02\x03",
            "Let's explore them on another occasion.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -70120, 0, 99240, 0)
    OP_E2(0x2)
    EventEnd(0x4)

    label("loc_4C5E")

    Return()

    # Function_22_48DF end

    SaveToFile()

Try(main)
