from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r0200.bin",                # FileName
        "r0200",                    # MapName
        "r0200",                    # Location
        0x00A5,                     # MapIndex
        "ed7121",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x34,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 460, 0, 34470, 180, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "r0200",                  # 0
        "Peter",                  # 1
        "Coppen",                 # 2
        "Branch Manager Celdan",  # 3
        "Lakelord III",           # 4
        "Kaguya, the Dragon Queen",# 5
        "Leader Fisher",          # 6
        "Cryptid",                # 7
        "Cryptid",                # 8
        "Cryptid",                # 9
        "br0200",                 # 10
    ))

    ATBonus("ATBonus_40C", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_4CC", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_4D0", 3, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_4D4", 13, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_4D8", 2, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_4DC", 14, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_4E0", 2, 8, 135)
    MonsterBattlePostion("MonsterBattlePostion_4E4", 14, 8, 225)
    MonsterBattlePostion("MonsterBattlePostion_4E8", 0, 0, 180)

    # monster count: 0

    # event battle count: 2

    BattleInfo(
        "BattleInfo_4EC", 0x0042, 255, 6, 45, 10, 1, 30, 0, "br0200", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88700.dat", "ms88800.dat", "ms88800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4CC", "MonsterBattlePostion_4CC", "ed7454", "ed7453", "ATBonus_40C"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch24200.itc",                   # 00
        "chr/ch23600.itc",                   # 01
        "chr/ch32200.itc",                   # 02
        "apl/ch50166.itc",                   # 03
        "chr/ch45600.itc",                   # 04
        "apl/ch51009.itc",                   # 05
    ))

    DeclNpc(17129,   0,       4294956847, 0,    261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(28979,   0,       4010,    0,    277,  0x0, 0,   3,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(17819,   0,       4294957187, 270,  389,  0x0, 0,   4,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(29600,   9,       1799,    90,   407,  0x0, 0,   5,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 16,  92.0,                  0.0,                   0.0,                   256.0,                 [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -23.0,                 -0.0,                  -0.0,                  1.0])
    DeclEvent(0x0040, 0, 17,  113.4000015258789,     3.7699999809265137,    0.0,                   14.0625,               [0.13333334028720856,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.13333334028720856,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   0.0,                   -15.120000839233398,   -0.502666711807251,    -0.0,                  1.0])
    DeclEvent(0x0000, 0, 21,  24.670000076293945,    -12.6899995803833,     -0.5,                  4.0,                   [-0.17677687108516693, 0.7071061134338379,    0.0,                   0.0,                   -0.17677652835845947,  -0.7071074843406677,   0.0,                   0.0,                   0.0,                   -0.0,                  0.5,                   0.0,                   2.1177914142608643,    -26.41750144958496,    0.25,                  1.0])
    DeclEvent(0x0000, 0, 10,  88.0,                  0.6000000238418579,    0.0,                   256.0,                 [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -22.0,                 -0.07500000298023224,  -0.0,                  1.0])

    DeclActor(119750,  0,       2850,    2000,    119750,  1000,    2850,    0x007C, 0,  9,  0x0000)
    DeclActor(29650,   0,       210,     1200,    37690,   4294966296, 1900,    0x007C, 0,  11, 0x0000)
    DeclActor(39850,   0,       4294953236, 1000,    39850,   1000,    4294953236, 0x007C, 0,  12, 0x0000)
    DeclActor(4294963237, 0,       4294965606, 1500,    4294963237, 2000,    4294965606, 0x007C, 0,  13, 0x0000)
    DeclActor(102780,  0,       1670,    1500,    102780,  2000,    1670,    0x007C, 0,  13, 0x0000)

    ChipFrameInfo(1428, 0)                                       # 0

    ScpFunction((
        "Function_0_594",          # 00, 0
        "Function_1_644",          # 01, 1
        "Function_2_D8C",          # 02, 2
        "Function_3_1104",         # 03, 3
        "Function_4_134E",         # 04, 4
        "Function_5_1F27",         # 05, 5
        "Function_6_254D",         # 06, 6
        "Function_7_2611",         # 07, 7
        "Function_8_279E",         # 08, 8
        "Function_9_2864",         # 09, 9
        "Function_10_2922",        # 0A, 10
        "Function_11_2A5B",        # 0B, 11
        "Function_12_2B20",        # 0C, 12
        "Function_13_2B5F",        # 0D, 13
        "Function_14_2E98",        # 0E, 14
        "Function_15_2F2C",        # 0F, 15
        "Function_16_30F9",        # 10, 16
        "Function_17_38E0",        # 11, 17
        "Function_18_3D45",        # 12, 18
        "Function_19_4646",        # 13, 19
        "Function_20_5A5E",        # 14, 20
        "Function_21_5D8E",        # 15, 21
        "Function_22_6941",        # 16, 22
        "Function_23_763B",        # 17, 23
        "Function_24_7D94",        # 18, 24
    ))


    def Function_0_594(): pass

    label("Function_0_594")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_5CC"),
        (1, "loc_5D8"),
        (2, "loc_5E4"),
        (3, "loc_5F0"),
        (4, "loc_5FC"),
        (5, "loc_608"),
        (6, "loc_614"),
        (SWITCH_DEFAULT, "loc_620"),
    )


    label("loc_5CC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_62C")

    label("loc_5D8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_62C")

    label("loc_5E4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_62C")

    label("loc_5F0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_62C")

    label("loc_5FC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_62C")

    label("loc_608")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_62C")

    label("loc_614")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_62C")

    label("loc_620")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_62C")

    label("loc_62C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_643")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_62C")

    label("loc_643")

    Return()

    # Function_0_594 end

    def Function_1_644(): pass

    label("Function_1_644")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE8")
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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D1")
    SetScenarioFlags(0x38, 0)

    label("loc_6D1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E7")
    SetScenarioFlags(0x38, 1)

    label("loc_6E7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FD")
    SetScenarioFlags(0x38, 2)

    label("loc_6FD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_713")
    SetScenarioFlags(0x38, 3)

    label("loc_713")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_729")
    SetScenarioFlags(0x38, 4)

    label("loc_729")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73F")
    SetScenarioFlags(0x38, 5)

    label("loc_73F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_755")
    SetScenarioFlags(0x38, 6)

    label("loc_755")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76B")
    SetScenarioFlags(0x38, 7)

    label("loc_76B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_781")
    SetScenarioFlags(0x39, 0)

    label("loc_781")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_797")
    SetScenarioFlags(0x39, 1)

    label("loc_797")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AD")
    SetScenarioFlags(0x39, 2)

    label("loc_7AD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C3")
    SetScenarioFlags(0x39, 3)

    label("loc_7C3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D9")
    SetScenarioFlags(0x39, 4)

    label("loc_7D9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EF")
    SetScenarioFlags(0x39, 5)

    label("loc_7EF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_805")
    SetScenarioFlags(0x39, 6)

    label("loc_805")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81B")
    SetScenarioFlags(0x39, 7)

    label("loc_81B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_831")
    SetScenarioFlags(0x3A, 0)

    label("loc_831")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_847")
    SetScenarioFlags(0x3A, 1)

    label("loc_847")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_85D")
    SetScenarioFlags(0x3A, 2)

    label("loc_85D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_873")
    SetScenarioFlags(0x3A, 3)

    label("loc_873")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_889")
    SetScenarioFlags(0x3A, 4)

    label("loc_889")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89F")
    SetScenarioFlags(0x3A, 5)

    label("loc_89F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B5")
    SetScenarioFlags(0x3A, 6)

    label("loc_8B5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CB")
    SetScenarioFlags(0x3A, 7)

    label("loc_8CB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E1")
    SetScenarioFlags(0x3B, 0)

    label("loc_8E1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F7")
    SetScenarioFlags(0x3B, 1)

    label("loc_8F7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90D")
    SetScenarioFlags(0x3B, 2)

    label("loc_90D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_923")
    SetScenarioFlags(0x3B, 3)

    label("loc_923")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_939")
    SetScenarioFlags(0x3B, 4)

    label("loc_939")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94F")
    SetScenarioFlags(0x3B, 5)

    label("loc_94F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_965")
    SetScenarioFlags(0x3B, 6)

    label("loc_965")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97B")
    SetScenarioFlags(0x3B, 7)

    label("loc_97B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_991")
    SetScenarioFlags(0x3D, 5)

    label("loc_991")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A7")
    SetScenarioFlags(0x3D, 6)

    label("loc_9A7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BD")
    SetScenarioFlags(0x3D, 7)

    label("loc_9BD")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F8")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_AE8")

    label("loc_9F8")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1B")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_AE8")

    label("loc_A1B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3E")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_AE8")

    label("loc_A3E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A61")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_AE8")

    label("loc_A61")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A84")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_AE8")

    label("loc_A84")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA7")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_AE8")

    label("loc_AA7")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACA")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_AE8")

    label("loc_ACA")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE8")
    SetScenarioFlags(0x3C, 7)

    label("loc_AE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2F, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AFE")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x34), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B30")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B30")
    SetChrPos(0x0, -2090, 0, -1280, 89)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 14)

    label("loc_B30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_B63")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B63")
    SetChrPos(0x0, 102780, 0, 1670, 270)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_B63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_BAF")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 16430, 0, -10160, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B9B")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xA, 0x10)

    label("loc_B9B")

    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_D4E")

    label("loc_BAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_BC7")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_D4E")

    label("loc_BC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BD5")
    Jump("loc_D4E")

    label("loc_BD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_BE3")
    Jump("loc_D4E")

    label("loc_BE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_BF6")
    SetChrFlags(0x8, 0x80)
    Jump("loc_D4E")

    label("loc_BF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_C04")
    Jump("loc_D4E")

    label("loc_C04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C12")
    Jump("loc_D4E")

    label("loc_C12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_CCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C75")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 39460, 0, -14300, 270)
    SetChrPos(0x8, 38260, 0, -13900, 135)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x10)
    SetChrPos(0x9, 38260, 0, -15100, 45)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_CCA")

    label("loc_C75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CCA")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 34370, 0, -14100, 225)
    SetChrPos(0x8, 33010, 0, -14380, 90)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x10)
    SetChrPos(0x9, 33520, 0, -15630, 0)
    BeginChrThread(0x9, 0, 0, 0)

    label("loc_CCA")

    Jump("loc_D4E")

    label("loc_CCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_CDD")
    Jump("loc_D4E")

    label("loc_CDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_CEB")
    Jump("loc_D4E")

    label("loc_CEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_D23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D0D")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_D1E")

    label("loc_D0D")

    SetChrPos(0x8, 7910, 0, -5530, 90)

    label("loc_D1E")

    Jump("loc_D4E")

    label("loc_D23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_D3B")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_D4E")

    label("loc_D3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_D4E")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)

    label("loc_D4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_D62")
    ClearScenarioFlags(0x22, 0)
    Event(0, 18)
    Jump("loc_D71")

    label("loc_D62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_D71")
    ClearScenarioFlags(0x22, 1)
    Event(0, 24)

    label("loc_D71")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D8B")
    Event(0, 22)

    label("loc_D8B")

    Return()

    # Function_1_644 end

    def Function_2_D8C(): pass

    label("Function_2_D8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_DA3")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DF6")

    label("loc_DA3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DCD")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x23D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DF6")

    label("loc_DCD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DF6")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x79), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DF6")

    SoundDistance(0x7B, 0x230A, 0x0, 0xFFFF7356, 0x3A98, 0xC350, 0x64, 0x0)
    OP_E3(0x73AA, 0x96, 0xFFFFE840)
    OP_E3(0x1DC9A, 0x0, 0x4A38)
    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, 37690, -1000, 1900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F16")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Sound(128, 1, 100, 0)
    Jump("loc_F2E")

    label("loc_F16")

    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)

    label("loc_F2E")

    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x9, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_F6E")
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x9, 0x4)
    Jump("loc_FA1")

    label("loc_F6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 3)), scpexpr(EXPR_END)), "loc_F92")
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFrame(0x2, "flower04", 0x0, 0x1)
    Jump("loc_FA1")

    label("loc_F92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_FA1")
    ClearMapObjFlags(0x2, 0x4)

    label("loc_FA1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_FC2")
    SetMapObjFrame(0xFF, "turi00", 0x0, 0x1)
    Jump("loc_FD0")

    label("loc_FC2")

    SetMapObjFrame(0xFF, "turi01", 0x0, 0x1)

    label("loc_FD0")

    MiniGame(0x2F, 0x3, 0x4, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_100A")
    ClearMapFlags(0x2000)
    Jump("loc_100F")

    label("loc_100A")

    SetMapFlags(0x2000)

    label("loc_100F")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1027")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1027")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1044")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_1044")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_105F")
    OP_66(0x0, 0x1)

    label("loc_105F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 1)), scpexpr(EXPR_END)), "loc_1089")
    SetChrFlags(0xE, 0x80)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    ModifyEventFlags(0, 1, 0x80)
    Jump("loc_10BC")

    label("loc_1089")

    ClearChrFlags(0xE, 0x80)
    ClearMapObjFlags(0x5, 0x4)
    OP_78(0x5, 0xE)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetChrPos(0xE, 113400, 0, 3770, 180)
    OP_93(0xE, 0x10E, 0x0)

    label("loc_10BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 0)), scpexpr(EXPR_END)), "loc_10D8")
    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0xA)
    OP_65(0x2, 0x1)
    Jump("loc_10E2")

    label("loc_10D8")

    ClearMapObjFlags(0x0, 0x10)
    OP_66(0x2, 0x1)

    label("loc_10E2")

    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1103")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_1103")

    Return()

    # Function_2_D8C end

    def Function_3_1104(): pass

    label("Function_3_1104")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1111")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_134A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1138")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_117E")

    label("loc_1138")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_117E")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_117E")

    label("loc_117E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 5)), scpexpr(EXPR_END)), "loc_119D")
    OP_AF(0x37)
    Jump("loc_119F")

    label("loc_119D")

    OP_AF(0x36)

    label("loc_119F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1345")

    label("loc_11AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1345")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_12D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11E2")
    Call(0, 7)
    Jump("loc_12C4")

    label("loc_11E2")


    ChrTalk(
        0xA,
        (
            "At any rate...living in this\x01",
            "shed for about a month... \x01",
            "They're really strong guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It seems they have endured by\x01",
            "making dried food and picking\x01",
            "up edible wild grasses...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Honestly, what admirable guts they have.\x02",
    )

    CloseMessageWindow()

    label("loc_12C4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1345")

    label("loc_12D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1345")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        "Member Lloyd, be careful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We will be waiting\x01",
            "for you here. We leave\x01",
            "the Cryptid to you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1345")

    Jump("loc_1111")

    label("loc_134A")

    TalkEnd(0xFE)
    Return()

    # Function_3_1104 end

    def Function_4_134E(): pass

    label("Function_4_134E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1387")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x344, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x345, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x346, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x347, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1387")
    Call(0, 23)
    Return()

    label("loc_1387")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1784")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x344, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x345, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x346, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x347, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13BB")
    Jump("loc_1784")

    label("loc_13BB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x344, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x345, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x346, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x347, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1784")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 500)

    ChrTalk(
        0xFE,
        "Lloyd, that's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYes, it's a part of a fishing\x01",
            "gear without a doubt...\x01",
            "It's very beautiful.\x02\x03",
            "#00000FI caught a rare fish from a fishing spot\x01",
            "I recovered from the Elite Fours...\x01",
            "It was that fish that spat it out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...No doubt. \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's a part of the legendary gear that was\x01",
            "used by a wandering remarkable angler, once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard he sealed it in\x01",
            "this land when he left\x01",
            "Crossbell, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To think it was\x01",
            "found like that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FI-Is it such an\x01",
            "amazing thing...?\x02\x03",
            "#00003FThen, what do we do?\x01",
            "We should give it back to that person...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "No, there is no need for that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Because that person said that who\x01",
            "finds that fishing gear, can use it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lloyd, there are\x01",
            "4 parts in total.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When you have obtained all of them,\x01",
            "please come to my place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I should be able to\x01",
            "put those parts together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FI-I see...\x01",
            "I understand, I'll keep it in mind.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x1C0, 1)
    TalkEnd(0xFE)
    Return()

    label("loc_1784")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1816")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "To think that the once sealed legendary\x01",
            "fishing gear would appear at such a time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hm, Lloyd.\x01",
            "Could this be fate?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F23")

    label("loc_1816")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1824")
    Jump("loc_1F23")

    label("loc_1824")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1A06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_194F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18F8")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x344, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x345, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x346, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x347, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1863")
    Jump("loc_18F3")

    label("loc_1863")


    ChrTalk(
        0xFE,
        (
            "Well, I can't help but looking\x01",
            "forward to meet that person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu, people of the Fishing Emperor Club,\x01",
            "laugh now, that you still can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18F3")

    Jump("loc_194A")

    label("loc_18F8")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "Lloyd, please destroy Lakelord\x01",
            "with that Aqua Ruler!\x01",
            "...I beg of you!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_194A")

    Jump("loc_1A01")

    label("loc_194F")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "Master Lloyd, "Fishing Emperor Slayer".\x01",
            "Thank you very much for having\x01",
            "done an amazing deed recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu, I will orally hand down\x01",
            "forever these Angler Duels.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A01")

    Jump("loc_1F23")

    label("loc_1A06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1A14")
    Jump("loc_1F23")

    label("loc_1A14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1A22")
    Jump("loc_1F23")

    label("loc_1A22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1A30")
    Jump("loc_1F23")

    label("loc_1A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1ACD")

    ChrTalk(
        0xFE,
        (
            "No matter how many times the branch manager\x01",
            "or Koppen challenged them, they could not win...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I felt like we were having\x01",
            "a nightmare.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F23")

    label("loc_1ACD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1D08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B93")

    ChrTalk(
        0xFE,
        (
            "With everyone coming for us,\x01",
            "I was relieved from the bottom of my heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I couldn't help to feel uneasy since yesterday,\x01",
            "thinking about if it could come to attack.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D03")

    label("loc_1B93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C75")

    ChrTalk(
        0xFE,
        (
            "Well then, I think I will gradually\x01",
            "restart my training too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am the only one who wasn't able\x01",
            "to beat a single Elite Four yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is time I make a serious effort\x01",
            "and clean up this dishonor.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D03")

    label("loc_1C75")


    ChrTalk(
        0xFE,
        (
            "I am the only one who wasn't able\x01",
            "to beat a single Elite Four yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is time I make a serious effort\x01",
            "and clean up this dishonor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D03")

    Jump("loc_1F23")

    label("loc_1D08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1D9A")

    ChrTalk(
        0xFE,
        (
            "Coppen...\x01",
            "How could he fish that\x01",
            "dreamy Noble Carp, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, could it be already\x01",
            "the fruit of the training?\x01",
            "I can't lose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F23")

    label("loc_1D9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1E54")

    ChrTalk(
        0xFE,
        (
            "Well then, I will polish\x01",
            "my skill to be a little\x01",
            "useful to the everyone too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I don't get at least to "Occupation: \x01",
            "Angler" class, I won't be able to survive.\x01\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F23")

    label("loc_1E54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1F0C")

    ChrTalk(
        0xFE,
        (
            "The Fisherman's Guild signboard...\x01",
            "I must put it back again on the\x01",
            "former office no matter what.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At this rate, it would be inexcusable\x01",
            "towards our captain too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F23")

    label("loc_1F0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1F1A")
    Jump("loc_1F23")

    label("loc_1F1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1F23")

    label("loc_1F23")

    TalkEnd(0xFE)
    Return()

    # Function_4_134E end

    def Function_5_1F27(): pass

    label("Function_5_1F27")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1F38")
    Jump("loc_2549")

    label("loc_1F38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2030")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FC5")

    ChrTalk(
        0xFE,
        (
            "The lethal weapon of the\x01",
            "Fisherman's Guild...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've never met him, so I wonder \x01",
            "what kind of person he is?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_202B")

    label("loc_1FC5")


    ChrTalk(
        0xFE,
        (
            "Aaallright,\x01",
            "I won't lose!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Someday I'll get my revenge on\x01",
            "the Fishing Emperor Club for sure!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_202B")

    Jump("loc_2549")

    label("loc_2030")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_203E")
    Jump("loc_2549")

    label("loc_203E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_20B5")

    ChrTalk(
        0xFE,
        (
            "I should... I should be able\x01",
            "to do more, way more!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How frustrating...\x01",
            "How really frustrating!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2549")

    label("loc_20B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_20C3")
    Jump("loc_2549")

    label("loc_20C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2169")

    ChrTalk(
        0xFE,
        (
            "Uuh, why is it that no matter how many times I\x01",
            "challenge the "Dragon Queen", I can't win!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is there... Is there anything\x01",
            "in me that's wrong!?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2549")

    label("loc_2169")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2254")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21FD")

    ChrTalk(
        0xFE,
        (
            "Even so, that monster...\x01",
            "The more you look at it, the more it's ghastly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Plus, huge...\x01",
            "Cut me some slack already.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_224F")

    label("loc_21FD")


    ChrTalk(
        0xFE,
        "Come now, I'll get back what I lost!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Aim for the "Dragon Queen Killer"!\x02",
    )

    CloseMessageWindow()

    label("loc_224F")

    Jump("loc_2549")

    label("loc_2254")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2396")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2306")

    ChrTalk(
        0xFE,
        (
            "Whoa, again, I've caught\x01",
            "a Noble Carp.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It should be quite a rare\x01",
            "fish in Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uuh, as I thought, I feel\x01",
            "that something's amiss.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2391")

    label("loc_2306")


    ChrTalk(
        0xFE,
        (
            "I feel that the Noble Carp\x01",
            "numbers have increased\x01",
            "compared to before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Could something be happening\x01",
            "to the Crossbell ecosystem?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2391")

    Jump("loc_2549")

    label("loc_2396")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_24C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2455")

    ChrTalk(
        0xFE,
        "213, 214, 215...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today too, before attaching the baits,\x01",
            "I'll do 1000 down thrusts with the rod!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This special training quite\x01",
            "builds up arm strength!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_24C4")

    label("loc_2455")


    ChrTalk(
        0xFE,
        (
            "The Goddess doesn't smile to\x01",
            "those who neglect efforts!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "An angler must be diligent every single day!\x02",
    )

    CloseMessageWindow()

    label("loc_24C4")

    Jump("loc_2549")

    label("loc_24C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2532")

    ChrTalk(
        0xFE,
        "Come now, let's start the training at once.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Just you wait, Fishing Emperor Club!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2549")

    label("loc_2532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2540")
    Jump("loc_2549")

    label("loc_2540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2549")

    label("loc_2549")

    TalkEnd(0xFE)
    Return()

    # Function_5_1F27 end

    def Function_6_254D(): pass

    label("Function_6_254D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_25E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_256B")
    Call(0, 7)
    Jump("loc_25E3")

    label("loc_256B")


    ChrTalk(
        0xB,
        (
            "Damn, although I'm the enemy,\x01",
            "why is this guy so friendly?\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "As if I'll ever approve of such strange behavior!\x02",
    )

    CloseMessageWindow()

    label("loc_25E3")

    Jump("loc_260D")

    label("loc_25E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_25F6")
    Jump("loc_260D")

    label("loc_25F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_2604")
    Jump("loc_260D")

    label("loc_2604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_260D")

    label("loc_260D")

    TalkEnd(0xFE)
    Return()

    # Function_6_254D end

    def Function_7_2611(): pass

    label("Function_7_2611")

    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xA,
        (
            "To think I'd find you\x01",
            "here, Lakelord.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hmph, wasn't it you who said\x01",
            "we could use this place?\x01",
            "...Don't complain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Of course, I promised you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "However, this place has a lot of inconveniences. \x01",
            "You can come at the branch whenever you want, \x01",
            "you know?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xB)

    ChrTalk(
        0xB,
        (
            "H-Hmph...\x01",
            "We haven't fallen so low to have\x01",
            "to receive concerns from you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xA, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_7_2611 end

    def Function_8_279E(): pass

    label("Function_8_279E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_283B")

    ChrTalk(
        0xC,
        (
            "*sigh*...I had forgotten about it,\x01",
            "but we are borrowing this shed\x01",
            "from that man, Celdan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Our time alone together...\x01",
            "Unforgivable!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2860")

    label("loc_283B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2849")
    Jump("loc_2860")

    label("loc_2849")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_2857")
    Jump("loc_2860")

    label("loc_2857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2860")

    label("loc_2860")

    TalkEnd(0xFE)
    Return()

    # Function_8_279E end

    def Function_9_2864(): pass

    label("Function_9_2864")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 4)), scpexpr(EXPR_END)), "loc_2890")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 6)), scpexpr(EXPR_END)), "loc_287E")
    Call(0, 20)
    Jump("loc_288B")

    label("loc_287E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_288B")
    Call(0, 19)

    label("loc_288B")

    Jump("loc_2921")

    label("loc_2890")

    EventBegin(0x2)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Azure Flowers are blooming.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00000F(What pretty flowers they're.\x01",
            "It seems they're faintly glowing, though...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x168, 4)
    EventEnd(0x3)

    label("loc_2921")

    Return()

    # Function_9_2864 end

    def Function_10_2922(): pass

    label("Function_10_2922")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00003F(With this we've beaten\x01",
            "two Cryptids, but...\x01",
            "Something's bothering me.)\x02\x03",
            "#00000FEveryone, could we go back\x01",
            "again to the scene to investigate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIndeed, I too feel like there should be\x01",
            "something else we must do here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FThen, let's go back now and investigate.\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 91500, 0, 0, 90)
    EventEnd(0x4)
    Return()

    # Function_10_2922 end

    def Function_11_2A5B(): pass

    label("Function_11_2A5B")

    EventBegin(0x1)
    Sound(2094, 255, 100, 0)

    ChrTalk(
        0x101,
        "#0000FIt seems I can fish here.\x02",
    )

    CloseMessageWindow()
    OP_68(32130, 1200, -50, 1500)
    MoveCamera(25, 31, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(20500, 1500)
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
            "Fish \x01",      # 0
            "Quit\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B1B")
    OP_E2(0x2)
    MiniGame(0x6, 0x18, 0x73D2, 0x0, 0xD2, 0x5A, 0x933A, 0xFFFFFC18, 0x76C)

    label("loc_2B1B")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_11_2A5B end

    def Function_12_2B20(): pass

    label("Function_12_2B20")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The wooden doors are firmly locked.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_12_2B20 end

    def Function_13_2B5F(): pass

    label("Function_13_2B5F")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B91")
    SetScenarioFlags(0x31, 2)

    label("loc_2B91")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2BD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_2BD1")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2BC6")
    Sound(2499, 255, 100, 0)
    Jump("loc_2BCC")

    label("loc_2BC6")

    Sound(3537, 255, 100, 0)

    label("loc_2BCC")

    Jump("loc_2BD7")

    label("loc_2BD1")

    Sound(3344, 255, 100, 0)

    label("loc_2BD7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_2C4A")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2C2A"),
        (SWITCH_DEFAULT, "loc_2C3B"),
    )


    label("loc_2C2A")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_2C45")

    label("loc_2C3B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C45")

    Jump("loc_2E85")

    label("loc_2C4A")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_2C7C")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_2C7C")

    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2CAE"),
        (1, "loc_2DB2"),
        (2, "loc_2E43"),
        (SWITCH_DEFAULT, "loc_2E7B"),
    )


    label("loc_2CAE")

    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    OP_74(0x8, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2CDF")
    OP_70(0x8, 0x12C)
    OP_71(0x8, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_2CEF")

    label("loc_2CDF")

    OP_70(0x8, 0xF0)
    OP_71(0x8, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_2CEF")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D45")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D45")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D68")
    Sound(461, 0, 100, 0)

    label("loc_2D68")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D88")
    OP_70(0x8, 0x14A)
    OP_71(0x8, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_2D98")

    label("loc_2D88")

    OP_70(0x8, 0x10E)
    OP_71(0x8, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_2D98")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x8, "light", 0x1, 0x1)
    OP_70(0x8, 0x0)
    Jump("loc_2BD7")

    label("loc_2DB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_2E24")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_2DE7")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_2DFF")

    label("loc_2DE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2DFA")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_2DFF")

    label("loc_2DFA")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_2DFF")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E3E")

    label("loc_2E24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2E34")
    OP_AF(0xFB)
    Jump("loc_2E3E")

    label("loc_2E34")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E3E")

    Jump("loc_2E85")

    label("loc_2E43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E5C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E76")

    label("loc_2E5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2E6C")
    OP_AF(0xFB)
    Jump("loc_2E76")

    label("loc_2E6C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E76")

    Jump("loc_2E85")

    label("loc_2E7B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E85")

    Jump("loc_2BD7")

    label("loc_2E8A")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_13_2B5F end

    def Function_14_2E98(): pass

    label("Function_14_2E98")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_2EF3")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2EE8")
    Sound(2502, 255, 100, 0)
    Jump("loc_2EEE")

    label("loc_2EE8")

    Sound(2503, 255, 100, 0)

    label("loc_2EEE")

    Jump("loc_2F17")

    label("loc_2EF3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2F11")
    Sound(3347, 255, 100, 0)
    Jump("loc_2F17")

    label("loc_2F11")

    Sound(3348, 255, 100, 0)

    label("loc_2F17")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_14_2E98 end

    def Function_15_2F2C(): pass

    label("Function_15_2F2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2F36")
    Return()

    label("loc_2F36")

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
        (1, "loc_3012"),
        (SWITCH_DEFAULT, "loc_302B"),
    )


    label("loc_3012")

    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, 106900, 0, 4400, 90)
    EventEnd(0x5)
    Return()

    label("loc_302B")

    Battle("BattleInfo_4EC", 0x0, 0x0, 0x100, 0xC, 0xFF)
    OP_E2(0x2)
    EventBegin(0x1)
    OP_68(106900, 1000, 4400, 0)
    OP_90(0x0, 106900, 0, 4400, 90)
    OP_90(0x1, 106900, 0, 4400, 90)
    OP_90(0x2, 106900, 0, 4400, 90)
    OP_90(0x3, 106900, 0, 4400, 90)
    OP_90(0x4, 106900, 0, 4400, 90)
    OP_90(0x5, 106900, 0, 4400, 90)
    OP_90(0x6, 106900, 0, 4400, 90)
    OP_90(0x7, 106900, 0, 4400, 90)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_30ED"),
        (1, "loc_30F2"),
        (SWITCH_DEFAULT, "loc_30F5"),
    )


    label("loc_30ED")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    label("loc_30F2")

    OP_B9(0x0)
    Return()

    label("loc_30F5")

    Call(0, 18)
    Return()

    # Function_15_2F2C end

    def Function_16_30F9(): pass

    label("Function_16_30F9")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_68(90650, 1000, 0, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    OP_68(91800, 1100, 0, 1300)
    SetChrPos(0x101, 92650, 0, 0, 90)
    SetChrPos(0x102, 92200, 0, 900, 90)
    SetChrPos(0x103, 91050, 0, 900, 90)
    SetChrPos(0x104, 90750, 0, 1900, 90)
    SetChrPos(0x109, 91300, 0, -900, 90)
    SetChrPos(0x105, 90300, 0, -500, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    StopBGM(0xFA0)
    FadeToBright(1000, 0)

    def lambda_31E5():
        OP_9B(0x0, 0x101, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_31E5)
    Sleep(0)

    def lambda_31FD():
        OP_9B(0x0, 0x102, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_31FD)
    Sleep(0)

    def lambda_3215():
        OP_9B(0x0, 0x103, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3215)
    Sleep(0)

    def lambda_322D():
        OP_9B(0x0, 0x104, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_322D)
    Sleep(0)

    def lambda_3245():
        OP_9B(0x0, 0x109, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3245)
    Sleep(0)

    def lambda_325D():
        OP_9B(0x0, 0x105, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_325D)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_0D()
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3370")

    ChrTalk(
        0x109,
        "#10111F#6P(Ah...!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#5P(That's a "Cryptid"...!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_33AA")

    label("loc_3370")


    ChrTalk(
        0x105,
        "#10305F#6P(Whoa...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#5P(There it is...!)\x02",
    )

    CloseMessageWindow()

    label("loc_33AA")

    WaitBGM()
    Sleep(10)
    PlayBGM("ed7573", 0)
    OP_68(114100, 1600, 4200, 3000)
    MoveCamera(55, 12, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(17580, 4000)
    OP_6F(0x79)
    Fade(500)
    OP_68(115110, 1200, 5490, 0)
    MoveCamera(38, 33, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19330, 0)
    OP_68(115110, 1200, 3580, 5000)
    MoveCamera(90, 16, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(19330, 5000)
    OP_6F(0x79)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36E0")

    ChrTalk(
        0x104,
        (
            "#00303F#9P(Like the report said, it's quite huge...)\x02\x03",
            "#00301F(peTiote, how about the spatial distortion?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#9P(Time, Space, Mirage... I confirm that\x01",
            "the three higher elements are at work.)\x02\x03",
            "#00201F(Currently, the cause is unknown.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#9P(I see...)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(91800, 1100, 0, 0)
    MoveCamera(45, 26, 0, 0)
    SetCameraDistance(18500, 0)
    OP_6E(500, 0)
    OP_0D()

    def lambda_35A0():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_35A0)
    Sleep(0)

    def lambda_35B0():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_35B0)
    Sleep(0)

    def lambda_35C0():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_35C0)
    Sleep(0)

    def lambda_35D0():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_35D0)
    Sleep(0)

    def lambda_35E0():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_35E0)
    Sleep(0)

    def lambda_35F0():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_35F0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_93(0x101, 0x10E, 0x1F4)

    ChrTalk(
        0x105,
        (
            "#10301F#6P(So...\x01",
            "What do we do?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11P(According to the CGF report,\x01",
            "it seems pretty dangerous...)\x02\x03",
            "#00013F(Let's cautiously prepare to exterminate it.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#12P(Roger...!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_38A5")

    label("loc_36E0")


    ChrTalk(
        0x102,
        (
            "#00101F#9P(Tio...\x01",
            "What about the spatial distortion?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#9P(Likewise, the three higher elements are at work...)\x02\x03",
            "#00201F(As suspected, the cause is unknown.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#9P(As we thought, huh...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10308F#9P(It seems that the Cryptid itself\x01",
            "is not the cause, though...)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(91800, 1100, 0, 0)
    MoveCamera(45, 26, 0, 0)
    SetCameraDistance(18500, 0)
    OP_6E(500, 0)
    OP_0D()

    ChrTalk(
        0x109,
        (
            "#10101F#6P(Mr. Lloyd...\x01",
            "Should we prepare now?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#5P(Yeah, let's proceed with caution...!)\x02",
    )

    CloseMessageWindow()

    label("loc_38A5")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 92650, 0, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x161, 0)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_16_30F9 end

    def Function_17_38E0(): pass

    label("Function_17_38E0")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch02950.itc", 0x22)
    LoadChrToIndex("chr/ch03050.itc", 0x23)
    LoadEffect(0x0, "battle\\cr036301.eff")
    ClearChrFlags(0xF, 0x80)
    OP_78(0x6, 0xF)
    OP_49()
    SetChrPos(0xF, 111300, 0, 9000, 225)
    OP_D5(0xF, 0x0, 0x36EE8, 0x0, 0x0)
    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x6, 0x1000)
    OP_75(0x6, 0x1, 0x0)
    ClearChrFlags(0x10, 0x80)
    OP_78(0x7, 0x10)
    OP_49()
    SetChrPos(0x10, 111300, 0, -1000, 315)
    OP_D5(0x10, 0x0, 0x4CE78, 0x0, 0x0)
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x7, 0x1000)
    OP_75(0x7, 0x1, 0x0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrChipByIndex(0x103, 0x20)
    SetChrChipByIndex(0x104, 0x21)
    SetChrChipByIndex(0x109, 0x22)
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x101, 106800, 0, 3750, 90)
    SetChrPos(0x102, 105500, 0, 4400, 90)
    SetChrPos(0x103, 104050, 0, 3550, 90)
    SetChrPos(0x104, 106600, 0, 4900, 90)
    SetChrPos(0x109, 105600, 0, 3000, 90)
    SetChrPos(0x105, 106500, 0, 2400, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0xE, 113400, 0, 3750, 180)
    OP_68(110400, 1000, 3750, 0)
    MoveCamera(90, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(23000, 0)
    OP_68(113400, 1000, 3750, 3000)
    SetCameraDistance(26000, 3000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C93")
    FadeToBright(1000, 0)
    OP_0D()
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sound(919, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xF, 0x0, 0, 1500, 0, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 500)
    PlayEffect(0x0, 0xFF, 0x10, 0x0, 0, 1500, 0, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 500)
    Sleep(1000)
    OP_75(0x6, 0x2, 0x3E8)
    OP_75(0x7, 0x2, 0x3E8)
    CancelBlur(1000)
    Sleep(1000)
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
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_6F(0x79)
    Sleep(500)
    OP_74(0x5, 0x14)
    OP_74(0x6, 0x14)
    OP_74(0x7, 0x14)
    OP_71(0x5, 0x5B, 0x69, 0xFA, 0x8)
    OP_71(0x6, 0x8D, 0xA0, 0xFA, 0x8)
    OP_71(0x7, 0x8D, 0xA0, 0xFA, 0x8)
    OP_79(0x5)
    OP_79(0x6)
    OP_79(0x7)
    Sound(842, 0, 100, 0)
    BlurSwitch(0x64, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(22500, 1000)
    OP_74(0x5, 0x1E)
    OP_74(0x6, 0x1E)
    OP_74(0x7, 0x1E)
    OP_71(0x5, 0x69, 0x73, 0x0, 0x8)
    OP_71(0x6, 0xA1, 0xAA, 0x0, 0x8)
    OP_71(0x7, 0xA1, 0xAA, 0x0, 0x8)
    Sleep(500)
    Jump("loc_3CAD")

    label("loc_3C93")

    OP_75(0x6, 0x2, 0x0)
    OP_75(0x7, 0x2, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    label("loc_3CAD")

    Battle("BattleInfo_4EC", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetScenarioFlags(0x168, 1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D41")
    SetChrChipByIndex(0x0, 0xFF)
    SetChrChipByIndex(0x1, 0xFF)
    SetChrChipByIndex(0x2, 0xFF)
    SetChrChipByIndex(0x3, 0xFF)
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_49()
    OP_37()
    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, 106900, 0, 4400, 90)
    EventEnd(0x5)
    Jump("loc_3D44")

    label("loc_3D41")

    Call(0, 18)

    label("loc_3D44")

    Return()

    # Function_17_38E0 end

    def Function_18_3D45(): pass

    label("Function_18_3D45")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch02950.itc", 0x22)
    LoadChrToIndex("chr/ch03050.itc", 0x23)
    OP_68(114100, 1600, 4200, 0)
    MoveCamera(50, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    OP_68(108700, 1300, 3200, 3000)
    MoveCamera(45, 25, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(17100, 3000)
    SetChrPos(0x101, 109900, 0, 3750, 90)
    SetChrPos(0x102, 108500, 0, 4700, 90)
    SetChrPos(0x103, 107050, 0, 3550, 90)
    SetChrPos(0x104, 109600, 0, 4900, 90)
    SetChrPos(0x109, 108600, 0, 3200, 90)
    SetChrPos(0x105, 109500, 0, 2400, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrChipByIndex(0x103, 0x20)
    SetChrChipByIndex(0x104, 0x21)
    SetChrChipByIndex(0x109, 0x22)
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    ModifyEventFlags(0, 1, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_29(0xA6, 0x1, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_413A")

    ChrTalk(
        0x101,
        (
            "#00006F#5PKh...\x01",
            "As expected, it was strong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6PAlso, it really...vanished\x01",
            "in a mysterious way.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    OP_0D()

    def lambda_3F74():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3F74)
    Sleep(50)

    def lambda_3F84():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3F84)
    Sleep(50)

    def lambda_3F94():
        TurnDirection(0x103, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3F94)
    Sleep(50)

    def lambda_3FA4():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3FA4)
    Sleep(50)

    def lambda_3FB4():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3FB4)
    Sleep(50)

    def lambda_3FC4():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3FC4)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x109,
        (
            "#10108F#12PTio.\x01",
            "What about the "spatial distortion"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6P...No good.\x01",
            "The three higher elements are still at work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#5PJeez...\x01",
            "What the heck is the cause?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#11PIt seems that the "Cryptid" itself\x01",
            "is not the cause, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00013F#11P...As expected, it seems we need\x01",
            "to check the other one too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_459A")

    label("loc_413A")


    ChrTalk(
        0x105,
        (
            "#10306F#6POh boy...\x01",
            "This one was strong too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#6PHowever, it vanished in the same way...\x02",
    )

    CloseMessageWindow()
    Fade(250)
    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    OP_0D()

    def lambda_41EA():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_41EA)
    Sleep(50)

    def lambda_41FA():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_41FA)
    Sleep(50)

    def lambda_420A():
        TurnDirection(0x103, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_420A)
    Sleep(50)

    def lambda_421A():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_421A)
    Sleep(50)

    def lambda_422A():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_422A)
    Sleep(50)

    def lambda_423A():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_423A)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x104,
        (
            "#00301F#5PAs I'm expectin', the "spatial\x01",
            "distortion" is goin' on, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#6PYes...\x02\x03",
            "#00201FI feel like there is some kind\x01",
            "of material cause.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005F#11PA material cause...\x01",
            "What, for instance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6P...Well...\x01",
            "My senses have been stirred by the\x01",
            ""distortion" since a little while...\x02\x03",
            "#00200FRather, maybe you all could\x01",
            "be able to find out the cause.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#5PR-Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11PAll right...\x01",
            "Let's search the vicinity.\x02\x03",
            "#00000FThere's going to be what is causing\x01",
            "the "spatial distortion" for sure.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_44D7():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_44D7)
    Sleep(50)

    def lambda_44E7():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_44E7)
    Sleep(50)

    def lambda_44F7():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_44F7)
    Sleep(50)

    def lambda_4507():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4507)
    Sleep(50)

    def lambda_4517():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4517)
    Sleep(50)

    def lambda_4527():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4527)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x109,
        "#10100F#6PRoger!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300F#5PLet's investigate whatever we can find!\x02",
    )

    CloseMessageWindow()
    OP_29(0xA6, 0x1, 0x3)

    label("loc_459A")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Defeated the East Crossbell Highway Cryptid!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 109900, 0, 3750, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x161, 1)
    OP_66(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4636")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_4636")

    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_37()
    EventEnd(0x5)
    Return()

    # Function_18_3D45 end

    def Function_19_4646(): pass

    label("Function_19_4646")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("apl/ch51216.itc", 0x1E)
    SoundLoad(961)
    SoundLoad(825)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis252.itp")
    LoadEffect(0x0, "event/ev14005.eff")
    LoadEffect(0x1, "event/ev14007.eff")
    SetChrPos(0x101, 121050, 0, 2350, 270)
    SetChrPos(0x102, 121150, 0, 3550, 225)
    SetChrPos(0x103, 120660, 0, 1200, 315)
    SetChrPos(0x104, 120950, 0, 4650, 225)
    SetChrPos(0x109, 119650, 0, 4150, 180)
    SetChrPos(0x105, 118100, 0, 3000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(120250, 1100, 2500, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetCameraDistance(18500, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A6A")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(300)

    AnonymousTalk(
        0x101,
        "#00005FThese flowers...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 3)), scpexpr(EXPR_END)), "loc_486F")

    AnonymousTalk(
        0x102,
        (
            "#00108FAren't these like the ones blooming\x01",
            "at St. Ursula Byroad sandbank...?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        "#00305FYeah, we saw 'em there, alright.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4928")

    label("loc_486F")


    AnonymousTalk(
        0x105,
        (
            "#10302FAren't these like the ones blooming\x01",
            "at St. Ursula Byroad sandbank...?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#00011FI-Is that so?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00108FYes, I'm sure I feel like I\x01",
            "happened to see them too...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4928")


    AnonymousTalk(
        0x109,
        (
            "#10109FWhat very pretty flowers...\x02\x03",
            "#10102F...I don't remember having ever seen them,\x01",
            "I wonder how they're called?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#00001FUhhm...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#11P(...I think it's unlikely, but...)\x02\x03",
            "#00001F(Well, could it be worth a try?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x161, 2)
    OP_29(0xA6, 0x1, 0x4)
    Jump("loc_4B28")

    label("loc_4A6A")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(300)

    AnonymousTalk(
        0x101,
        (
            "#00003F#11P(...I think it's unlikely, but...)\x02\x03",
            "#00001F(Well, could it be worth a try?)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    label("loc_4B28")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Try to Pick Up the Azure Flowers\x01",      # 0
            "Do Not\x01",                                # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4B8A"),
        (1, "loc_5A1E"),
        (SWITCH_DEFAULT, "loc_5A5D"),
    )


    label("loc_4B8A")

    OP_9B(0x0, 0x101, 0x0, 0x2EE, 0x3E8, 0x0)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_0D()

    ChrTalk(
        0x102,
        "#00105FLloyd...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F#6PWhat, do you want to\x01",
            "pick up these flowers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11PYeah...\x01",
            "Although I'm a little sorry for them──\x02",
        )
    )

    CloseMessageWindow()
    Sound(929, 0, 40, 0)
    Sound(828, 2, 30, 0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 119770, 600, 2910, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#00301F#5PW-What the!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#12PThis is...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#11PKh...\x02",
    )

    CloseMessageWindow()
    SetMapObjFrame(0x2, "flower04", 0x0, 0x1)
    StopEffect(0x0, 0x2)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(961, 2, 70, 0)
    Sound(233, 0, 100, 0)
    Sound(929, 0, 60, 0)
    PlayEffect(0x1, 0x1, 0x101, 0x3, 0, 1050, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_7D(0xD7, 0xFF, 0xFF, 0x0, 0x5DC)
    OP_11(0x7B, 0xB4, 0xD5, 0x1E, 0xB4, 0x5DC)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    MoveCamera(45, 23, 10, 3000)
    SetCameraDistance(12000, 3000)
    OP_6E(1000, 3000)
    Sleep(2500)
    Sound(829, 0, 100, 0)
    StopSound(961, 2000, 60)
    StopSound(828, 2000, 20)
    FadeToDark(500, 16777215, -1)
    Sleep(800)
    FadeToBright(300, 16777215)
    CancelBlur(300)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x32)
    OP_11(0xA7, 0xDD, 0xFE, 0x1E, 0xB4, 0x32)
    MoveCamera(45, 21, 0, 50)
    SetCameraDistance(18500, 50)
    OP_6E(500, 50)
    StopEffect(0x1, 0x2)
    Sleep(500)
    OP_6F(0x79)
    StopBGM(0x1770)

    ChrTalk(
        0x101,
        "#00013F#11P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10111F#5PW-What was that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108FSomehow it seems the space warped...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x103, 500)

    ChrTalk(
        0x105,
        (
            "#10308F#6P...Tio.\x01",
            "What about the "spatial distortion"?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)

    ChrTalk(
        0x103,
        (
            "#00203F#12P...The three higher elements\x01",
            "presence has vanished.\x02\x03",
            "#00201FI can't sense any anomaly\x01",
            "in this area anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#11PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#5PW-Wait a sec.\x02\x03",
            "#00307FYou want to tell me that those azure\x01",
            "flowers were causin' the anomaly!?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    ChrTalk(
        0x105,
        (
            "#10304F#6PWell, it's possible.\x02\x03",
            "#10300F...Although I can't think that such \x01",
            "tiny flowers have that kind of power.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101FU-Unbelieveable...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#5PW-What kind of\x01",
            "flowers are these?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#12P...I don't sense any strange \x01",
            "presence from those flowers...\x02\x03",
            "#00200FAt any rate, should we have them\x01",
            "investigated somewhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#11PYou're right...\x02\x03",
            "#00003F...It's probably a different field than\x01",
            "that the medical college delves in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FA-At any rate, let's keep them\x01",
            "stored so we don't lose them.\x02\x03",
            "If we come up with some idea,\x01",
            "we'll have them investigated, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#11PYeah, let's do that.\x02",
    )

    CloseMessageWindow()
    OP_9B(0x1, 0x101, 0xB4, 0x2EE, 0x3E8, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x105)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)

    ChrTalk(
        0x105,
        "#10303F#6P...Hm...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_5389():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5389)
    Sleep(50)

    def lambda_5399():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5399)
    Sleep(50)

    def lambda_53A9():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_53A9)
    Sleep(50)

    def lambda_53B9():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_53B9)
    Sleep(50)

    def lambda_53C9():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_53C9)
    Sleep(50)

    def lambda_53D9():
        TurnDirection(0x105, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_53D9)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#11PWazy...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#5PDo you have any idea?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#6PWell...\x01",
            "Maybe it's a faint memory of mine.\x02\x03",
            "#10301FI feel like there was a legend about a mysterious\x01",
            "azure flower in the Church Testaments.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#11PEH...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F#5PHey there, for real!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#6PWell, I feel I happened to see it when\x01",
            "skimming through them a very long time ago...\x02\x03",
            "#10300FElie or anyone else, do you have any idea?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00112F#11PAs you can imagine, I haven't\x01",
            "looked at all the Testaments, but...\x02\x03",
            "#00103F...But indeed, I feel like I\x01",
            "read such a passage.\x02\x03",
            "#00108FA legend of an "Azure Flower" which\x01",
            "holds a mysterious power...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)

    ChrTalk(
        0x109,
        (
            "#10111F#6PI-Isn't that...\x01",
            "Exactly it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#00201F#12PAt least it appears it's worth it to confirm\x01",
            "with someone belonging to the Church.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_57A0():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_57A0)
    Sleep(50)

    def lambda_57B0():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_57B0)
    Sleep(50)

    def lambda_57C0():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_57C0)
    Sleep(50)

    def lambda_57D0():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_57D0)
    Sleep(50)

    def lambda_57E0():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_57E0)
    Sleep(50)

    def lambda_57F0():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_57F0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_58B0")

    ChrTalk(
        0x101,
        (
            "#00003F#11P...Right.\x02\x03",
            "#00000FLet's try asking for advice to\x01",
            "teacher Marble or Miss Ries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FYes...\x01",
            "They're both suited, I think.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5970")

    label("loc_58B0")


    ChrTalk(
        0x101,
        (
            "#00003F#11P...Right.\x02\x03",
            "#00000FI think that teacher Marble would\x01",
            "be the easiest to consult with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FYes, I think she's competent.\x02\x03",
            "#00108F(We could consult with "her" too, but...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5970")


    ChrTalk(
        0x104,
        (
            "#00300F#5POk, then, let's head\x01",
            "to Crossbell Cathedral!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    OP_49()
    OP_37()
    SetChrPos(0x0, 121050, 0, 2350, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    AddItemNumber(0x333, 1)
    SetScenarioFlags(0x161, 3)
    OP_29(0xA6, 0x1, 0x5)
    OP_65(0x0, 0x1)
    ModifyEventFlags(0, 3, 0x80)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7121", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x79), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x3C1)
    OP_24(0x33C)
    EventEnd(0x5)
    Jump("loc_5A5D")

    label("loc_5A1E")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    OP_49()
    OP_37()
    SetChrPos(0x0, 121050, 0, 2350, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Jump("loc_5A5D")

    label("loc_5A5D")

    Return()

    # Function_19_4646 end

    def Function_20_5A5E(): pass

    label("Function_20_5A5E")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis252.itp")
    OP_68(120250, 1000, 2500, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 121050, 0, 2350, 270)
    SetChrPos(0x102, 121150, 0, 3550, 225)
    SetChrPos(0x103, 120660, 0, 1200, 315)
    SetChrPos(0x104, 120950, 0, 4650, 225)
    SetChrPos(0x109, 119650, 0, 4150, 180)
    SetChrPos(0x105, 118100, 0, 3000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    AnonymousTalk(
        0x109,
        (
            "#10100FB-By the way...\x02\x03",
            "Should we pick up these\x01",
            "flowers too?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00000FNo... Let's wait and see\x01",
            "what happens with these.\x02\x03",
            "Maybe they'll turn to be\x01",
            "valuable samples.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        (
            "#00200F...You are right. It seems that when you\x01",
            "pick them up, they lose strength.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00100FHowever...if a Cryptid appears again,\x01",
            "maybe we'll have to pick them up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        "#00300FWell, we'll think about it if it happens.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetChrPos(0x0, 121050, 0, 2350, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x161, 4)
    EventEnd(0x5)
    Return()

    # Function_20_5A5E end

    def Function_21_5D8E(): pass

    label("Function_21_5D8E")

    EventBegin(0x0)
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(37740, 1200, -14770, 3000)
    SetCameraDistance(17000, 3000)
    OP_6F(0x79)
    Fade(500)
    OP_4B(0xA, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_68(38230, 1200, -14840, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14580, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "Uhhm, at any rate, that's\x01",
            "a creepy monster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PI-If something like that were to\x01",
            "come here, we'd be helpless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yes, if that happens, we must\x01",
            "take refuge right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "However, for the time being\x01",
            "we'll wait for the CGF to come...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        "Ooh...if it isn't Member Lloyd!\x02",
    )

    CloseMessageWindow()
    OP_68(37180, 1400, -14790, 4000)
    MoveCamera(33, 33, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(14430, 4000)

    def lambda_5F63():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5F63)

    def lambda_5F70():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5F70)
    OP_93(0x9, 0x10E, 0x1F4)
    SetChrPos(0x101, 28250, 0, -15760, 90)
    SetChrPos(0x102, 28250, 0, -15760, 90)
    SetChrPos(0x103, 28250, 0, -15760, 90)
    SetChrPos(0x104, 28250, 0, -15760, 90)
    SetChrPos(0x109, 28250, 0, -15760, 90)
    SetChrPos(0x105, 28250, 0, -15760, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    def lambda_5FFE():
        OP_95(0xFE, 36720, 0, -14030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5FFE)
    Sleep(300)

    def lambda_601B():
        OP_95(0xFE, 36720, 0, -15170, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_601B)
    Sleep(300)

    def lambda_6038():
        OP_95(0xFE, 35680, 0, -13860, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6038)
    Sleep(300)

    def lambda_6055():
        OP_95(0xFE, 35680, 0, -15050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6055)
    Sleep(300)

    def lambda_6072():
        OP_95(0xFE, 34560, 0, -13930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6072)
    Sleep(300)

    def lambda_608F():
        OP_95(0xFE, 34700, 0, -14930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_608F)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)

    ChrTalk(
        0x101,
        (
            "#6P#00003FLong time no see, Branch Manager Celdan.\x02\x03",
            "#00001FWe heard that a mysterious large-scale monster,\x01",
            "a "Cryptid", has appeared here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "A "Cryptid"...\x01",
            "Hm, an expression that fits it perfectly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yes, actually that "Cryptid" or whatever appeared\x01",
            "suddenly yesterday evening deep inside the swamp.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We contacted the\x01",
            "CGF, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PCould it be that your Special\x01",
            "Support Section has come to\x01",
            "deal with it, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FYes, we took the request from the CGF.\x02\x03",
            "#00101FCould you please tell us\x01",
            "the situation in detail?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yes, like I just told you,\x01",
            "the first time we noticed it\x01",
            "was yesterday evening...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Really, like a bolt out of the blue,\x01",
            "all of a sudden we heard something\x01",
            "like a bizarre animal cry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PA suspicious shadow flickered in the deep part\x01",
            "of the marsh that's always been sealed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12PWe all got close cautiously.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThen, we spotted that mysterious \x01",
            ""Cryptid" or whatever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThen, we hastily made\x01",
            "a report to the CGF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We thought to run away, but...\x01",
            "There's no sign the "Cryptid"\x01",
            "is moving away from there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "For now we made turns since yesterday\x01",
            "to watch over it and monitor the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00203F...Thank you for your hard work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FWhile you were on watch, has\x01",
            "anything peculiar happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "No, nothing of the sort has.\x01\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Although we surrounded it at a distance, \x01",
            "we felt like he had an hostily will, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PHow to say this...\x01",
            "We felt that it's not that it\x01",
            "doesn't move, it can't.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PWe don't know the\x01",
            "full details, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303FI see. It appeared all of a sudden and\x01",
            "furthermore, it can't leave that place...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FWell, it clearly seems\x01",
            "related to that "spatial\x01",
            "distortion" stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FYeah, no doubt about it.\x02\x03",
            "#00013FThen, Branch Manager Celdan.\x01",
            "I'd like to immediately go further inside...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yes, you're going to\x01",
            "exterminate it, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I'll unlock it now.\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0x5A, 0x1F4)
    Sound(806, 0, 100, 0)
    Sleep(1000)
    Sound(103, 0, 100, 0)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    OP_93(0xA, 0x10E, 0x1F4)

    ChrTalk(
        0xA,
        (
            "All right, now it's fine.\x01",
            "We leave the rest to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYes, understood.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0xA, 34370, 0, -14100, 225)
    SetChrPos(0x8, 33010, 0, -14380, 90)
    SetChrPos(0x9, 33520, 0, -15630, 0)
    ClearChrFlags(0x9, 0x10)
    OP_65(0x2, 0x1)
    ModifyEventFlags(0, 2, 0x80)
    SetScenarioFlags(0x17A, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 37160, 0, -14440, 90)
    OP_69(0xFF, 0x0)
    OP_4C(0xA, 0xFF)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_21_5D8E end

    def Function_22_6941(): pass

    label("Function_22_6941")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0xA, 0xFF)
    OP_4B(0x8, 0xFF)
    EndChrThread(0x9, 0x0)
    OP_68(35180, 1200, -14020, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 34070, 0, -14520, 90)
    SetChrPos(0x8, 34270, 0, -15520, 90)
    SetChrPos(0x9, 34070, 0, -13320, 90)
    SetChrPos(0x101, 35460, 0, -14310, 270)
    SetChrPos(0x102, 35500, 0, -15390, 270)
    SetChrPos(0x104, 36590, 0, -15670, 270)
    SetChrPos(0x109, 36590, 0, -14070, 270)
    SetChrPos(0x103, 37600, 0, -15500, 270)
    SetChrPos(0x105, 37650, 0, -14100, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "#6POoh, Member Lloyd. Were you\x01",
            "able to exterminate the "Cryptid"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PYes, in a way or another.\x02\x03",
            "#00000FI think you need to be careful, but\x01",
            "I also think that maybe it won't\x01",
            "appear again for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PReally...?\x01",
            "That's good to hear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PUh uh, now we can devote ourselves\x01",
            "to fishing once again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#6PYes, they've really helped us.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6EE9")

    ChrTalk(
        0x8,
        "#6POh, right, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PCould you accept\x01",
            "this as thanks?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x17),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x17, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00005F#11PIs this...a new fishing rod?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PYes, this is a fishing rod I put together to\x01",
            "be used against the Fishing Emperor Club.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PIf you have this, you should be able\x01",
            "to fish way larger-scale fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#11PMr. Peter, you did this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PHa ha, he doesn't look like it, but Peter's\x01",
            "forte is tampering with tools.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6POccasionally he does like this,\x01",
            "making new fishing tools by\x01",
            "remodelling ready-made goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PEh eh, it's a wonderful story\x01",
            "somehow, since he's not\x01",
            "strong at all at fishing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PStop it, Coppen.\x01",
            "Don't say unnecessary things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11PAhaha...\x02\x03",
            "#00000FBut really, thank you very much\x01",
            "for this nice article.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_75D4")

    label("loc_6EE9")


    ChrTalk(
        0xA,
        "#6PRight, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PIt wasn't told to you, but I'd like to\x01",
            "tell you about the "Angler Duels"\x01",
            "with the Fishing Emperor Club...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#11P"A-Angler Duels"...?\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00003F#11PI see, "Angler Duels" against the five\x01",
            "members of the Fishing Emperor Club...\x02\x03",
            "If you win, you'll get back the office and\x01",
            "they'll release the occupied fishing spots...\x02\x03",
            "#00001FIf you lose, you'll be at their whims mercy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#6PYeah, that's it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PWell, for now we plan\x01",
            "to do something about\x01",
            "the matches in our way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PMember Lloyd, you're probably\x01",
            "busy with your principal occupation,\x01",
            "so don't pay too much mind to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#11PYes, understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#6POh, right, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PCould you accept\x01",
            "this as thanks?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x17),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x17, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00005F#11PIs this...a new fishing rod?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PYes, this is a fishing rod I put together to\x01",
            "be used against the Fishing Emperor Club.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PIf you have this, you should be able\x01",
            "to fish way larger-scale fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#11PMr. Peter, you did this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PHa ha, he doesn't look like it, but Peter's\x01",
            "forte is tampering with tools.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6POccasionally he does like this,\x01",
            "making new fishing tools by\x01",
            "remodelling ready-made goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PEh eh, it's a wonderful story\x01",
            "somehow, since he's not\x01",
            "strong at all at fishing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PStop it, Coppen.\x01",
            "Don't say unnecessary things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11PAhaha...\x02\x03",
            "#00000FBut really, thank you very much\x01",
            "for this nice article.\x02",
        )
    )

    CloseMessageWindow()
    Sound(814, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You have become able to challenge the Fishing\x01",
            "Emperor Club members to the "Angler Duels".\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You can hear from receptionist Sylum, who\x01",
            "is at the "East Street Fishing Emperor Club",\x01",
            "the detailed contents of the matches.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1C0, 0)

    label("loc_75D4")

    SetScenarioFlags(0x17A, 1)
    SetChrPos(0x8, 17130, 0, -10450, 0)
    SetChrPos(0x9, 28980, 0, 4010, 0)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 36380, 0, -14420, 270)
    OP_69(0xFF, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_22_6941 end

    def Function_23_763B(): pass

    label("Function_23_763B")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    Fade(500)
    OP_68(17140, 1200, -10530, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 16630, 0, -11900, 0)
    SetChrPos(0x102, 17690, 0, -11920, 0)
    SetChrPos(0x103, 16680, 0, -12920, 0)
    SetChrPos(0x104, 17680, 0, -12920, 0)
    SetChrPos(0x109, 16670, 250, -13920, 0)
    SetChrPos(0x105, 17670, 0, -13920, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 1)), scpexpr(EXPR_END)), "loc_77B6")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 500)

    ChrTalk(
        0x8,
        (
            "Lloyd, you've finally\x01",
            "collected all the parts!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FYes, somehow I've gathered them all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hm, then, I'll try to put\x01",
            "them together right now!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B2F")

    label("loc_77B6")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 500)

    ChrTalk(
        0x8,
        "Lloyd, that's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYes, it's a part of a fishing\x01",
            "gear without a doubt...\x01",
            "It's very beautiful.\x02\x03",
            "#00000FI caught a rare fish from a fishing spot\x01",
            "I recovered from the Elite Fours...\x01",
            "It was that fish that spat it out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "...No doubt. \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That's a part of the legendary gear that was\x01",
            "used by a wandering remarkable angler, once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I heard he sealed it in\x01",
            "this land when he left\x01",
            "Crossbell, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To think it was\x01",
            "found like that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FI-Is it such an\x01",
            "amazing thing...?\x02\x03",
            "#00003FThen, what do we do?\x01",
            "We should give it back to that person...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "No, there is no need for that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Because that person said that who\x01",
            "finds that fishing gear, can use it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Also, those parts are 4 in total...\x01",
            "Wait, you've already collected them all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then, I'll try to put them together right now.\x01",
            "All right, Mr. Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FY-Yes.\x02",
    )

    CloseMessageWindow()

    label("loc_7B2F")

    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "Ooh, it's beautiful.\x01",
            "This is the legendary...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FIndeed...put together like this\x01",
            "it's very amazing and cool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hm, then, Lloyd.\x01",
            "Please take it.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x18, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SubItemNumber(0x344, 1)
    SubItemNumber(0x345, 1)
    SubItemNumber(0x346, 1)
    SubItemNumber(0x347, 1)

    ChrTalk(
        0x101,
        "#00005FI-Is it all right for me to use it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uhuhu, what're you saying?\x01",
            "You've found it, so it's obvious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It appears that you've defeated\x01",
            "all of the Elite Four...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please go defeat the remaining \x01",
            "Lakelord freely swinging that rod!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FY-Yes...understood!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x190, 6)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 17060, 0, -12510, 0)
    OP_69(0xFF, 0x0)
    OP_93(0x8, 0x0, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_23_763B end

    def Function_24_7D94(): pass

    label("Function_24_7D94")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch46100.itc", 0x1E)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 5250, 10, -7750, 270)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 5250, 10, -8950, 270)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 6450, 10, -7550, 270)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 6450, 10, -9150, 270)
    OP_4B(0xA, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_68(3810, 2200, -8500, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 3250, 10, -8350, 90)
    SetChrPos(0x102, 1270, 0, -8270, 90)
    SetChrPos(0x103, 1220, 0, -9350, 90)
    SetChrPos(0x104, 1120, 0, -7380, 90)
    SetChrPos(0x109, -70, 0, -8850, 90)
    SetChrPos(0x105, -610, 0, -7900, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(3810, 1200, -8500, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0xA,
        (
            "Member Lloyd...\x01",
            "No, Master Lloyd, the "Fishing Emperor Slayer".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Thank you very much for what you did.\x01",
            "No matter how much I thank you, it won't ever be enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "You've been really amazing, Master Lloyd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hm, that the Fisherman's Guild - Crossbell Branch\x01",
            "has been defended by the hands of a young one makes\x01",
            "me happy and proud from the bottom of my heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uhuhu, I will orally hand down\x01",
            "forever these Angler Duels.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FN-No way, you're exaggerating.\x02",
    )

    CloseMessageWindow()
    OP_68(2190, 1200, -8070, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        "#00102F(Uhhm, it seems they're praising him a lot.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103F(Somehow I don't really get it, but...\x01",
            "It seems he's truly a hero.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F(The "Fishing Emperor Slayer"...\x01",
            "Maybe he is just a little bit cool.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x191, 1)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    SetChrPos(0x8, 17130, 0, -10450, 0)
    SetChrPos(0x9, 28980, 0, 4010, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    OP_49()
    OP_D7(0x1E)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 3250, 10, -8350, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_24_7D94 end

    SaveToFile()

Try(main)
