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
        "Function_4_1345",         # 04, 4
        "Function_5_1EF9",         # 05, 5
        "Function_6_251B",         # 06, 6
        "Function_7_25E7",         # 07, 7
        "Function_8_276E",         # 08, 8
        "Function_9_282D",         # 09, 9
        "Function_10_28E2",        # 0A, 10
        "Function_11_2A05",        # 0B, 11
        "Function_12_2ACC",        # 0C, 12
        "Function_13_2B04",        # 0D, 13
        "Function_14_2E41",        # 0E, 14
        "Function_15_2ED5",        # 0F, 15
        "Function_16_30A4",        # 10, 16
        "Function_17_389D",        # 11, 17
        "Function_18_3D02",        # 12, 18
        "Function_19_45D3",        # 13, 19
        "Function_20_59A4",        # 14, 20
        "Function_21_5CC2",        # 15, 21
        "Function_22_6833",        # 16, 22
        "Function_23_74A3",        # 17, 23
        "Function_24_7C0B",        # 18, 24
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

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1341")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1138")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1180")

    label("loc_1138")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1180")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_1180")

    label("loc_1180")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 5)), scpexpr(EXPR_END)), "loc_119F")
    OP_AF(0x37)
    Jump("loc_11A1")

    label("loc_119F")

    OP_AF(0x36)

    label("loc_11A1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_133C")

    label("loc_11B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_133C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_12CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11E4")
    Call(0, 7)
    Jump("loc_12BD")

    label("loc_11E4")


    ChrTalk(
        0xA,
        (
            "Anyhow... To think they lived in\x01",
            "this shed for a whole month...\x01",
            "They're really tough guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He said they held out by making\x01",
            "dried food and gathering edible\x01",
            "wild grasses...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Honestly, what guts they\x01",
            "have.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12BD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_133C")

    label("loc_12CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_133C")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "Member Lloyd, be\x01",
            "careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We'll be waiting for you\x01",
            "here. We leave the\x01",
            "cryptid to you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_133C")

    Jump("loc_1111")

    label("loc_1341")

    TalkEnd(0xFE)
    Return()

    # Function_3_1104 end

    def Function_4_1345(): pass

    label("Function_4_1345")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_137E")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x344, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x345, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x346, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x347, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_137E")
    Call(0, 23)
    Return()

    label("loc_137E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1765")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x344, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x345, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x346, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x347, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13B2")
    Jump("loc_1765")

    label("loc_13B2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x344, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x345, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x346, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x347, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1765")
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
            "#00004FYes, there's no mistaking it. It's\x01",
            "a fishing gear part. And a very\x01",
            "pretty one at that.\x02\x03",
            "#00000FI caught a rare fish from a fishing\x01",
            "spot I recovered from the Elite\x01",
            "Four... The fish spat that out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...No doubt.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's a part of the legendary\x01",
            "gear that was once used by a\x01",
            "remarkable wandering angler.\x02",
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
            "To think you found it\x01",
            "like that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FI-Is it that amazing?\x02\x03",
            "#00003FThen, what do we do? We\x01",
            "should give it back to\x01",
            "him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, there's no need for\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Because he said that\x01",
            "he who finds his fishing\x01",
            "gear, may use it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lloyd, there are 4 parts\x01",
            "in total.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please come to my place\x01",
            "if you manage to obtain\x01",
            "all of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I should be able to put\x01",
            "the parts together for\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FI-I see... I understand,\x01",
            "I'll keep that in mind.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x1C0, 1)
    TalkEnd(0xFE)
    Return()

    label("loc_1765")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_17F8")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "To think that the once sealed\x01",
            "legendary fishing gear would\x01",
            "appear at a time like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lloyd, could this be\x01",
            "fate?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EF5")

    label("loc_17F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1806")
    Jump("loc_1EF5")

    label("loc_1806")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_19DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_192B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18D4")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x344, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x345, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x346, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x347, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1845")
    Jump("loc_18CF")

    label("loc_1845")


    ChrTalk(
        0xFE,
        (
            "Well, I can't help but\x01",
            "look forward to meeting\x01",
            "him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu, people of the\x01",
            "Imperial Fishing Club. Laugh\x01",
            "now, while you still can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18CF")

    Jump("loc_1926")

    label("loc_18D4")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "Lloyd, please destroy\x01",
            "Lakelord with that Aqua\x01",
            "Ruler! ...I beg of you!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1926")

    Jump("loc_19D7")

    label("loc_192B")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "Master Lloyd, Fishing Emperor\x01",
            "Slayer. Thank you so much for\x01",
            "your outstanding recent deeds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu. I will pass down\x01",
            "these Angler Duels\x01",
            "orally for eternity.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19D7")

    Jump("loc_1EF5")

    label("loc_19DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_19EA")
    Jump("loc_1EF5")

    label("loc_19EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_19F8")
    Jump("loc_1EF5")

    label("loc_19F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1A06")
    Jump("loc_1EF5")

    label("loc_1A06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1AA3")

    ChrTalk(
        0xFE,
        (
            "No matter how many times the branch\x01",
            "manager or Coppen challenged them,\x01",
            "they couldn't win...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It felt like we were\x01",
            "having a nightmare.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EF5")

    label("loc_1AA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1CD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B5B")

    ChrTalk(
        0xFE,
        (
            "When you came for us, I\x01",
            "felt relieved from the\x01",
            "bottom of my heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I couldn't help but feel uneasy\x01",
            "since yesterday, thinking it\x01",
            "might come to attack.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CD2")

    label("loc_1B5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C41")

    ChrTalk(
        0xFE,
        (
            "Well then, I think I'll\x01",
            "gradually restart my\x01",
            "training too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm the only one who\x01",
            "hasn't yet beaten a single\x01",
            "one of the Elite Four...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's time I made a\x01",
            "serious effort and rid\x01",
            "myself of my dishonor.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CD2")

    label("loc_1C41")


    ChrTalk(
        0xFE,
        (
            "I'm the only one who\x01",
            "hasn't yet beaten a single\x01",
            "one of the Elite Four...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's time I make a\x01",
            "serious effort and get\x01",
            "rid of my dishonor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CD2")

    Jump("loc_1EF5")

    label("loc_1CD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1D6B")

    ChrTalk(
        0xFE,
        (
            "That Coppen... How did\x01",
            "he fish up that dreamy\x01",
            "Noble Carp, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, could his training\x01",
            "have paid off already? I\x01",
            "can't lose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EF5")

    label("loc_1D6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1E26")

    ChrTalk(
        0xFE,
        (
            "Well then, I'll polish my\x01",
            "skills so as to be a little\x01",
            "more useful to everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I don't at least get to\x01",
            ""Occupational Angler" class,\x01",
            "I won't be able to survive.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EF5")

    label("loc_1E26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1EDE")

    ChrTalk(
        0xFE,
        (
            "The Fisherman's Guild signboard...\x01",
            "I must put it back on the former\x01",
            "office again no matter what.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At this rate, it would\x01",
            "be inexcusable towards\x01",
            "our manager too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EF5")

    label("loc_1EDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1EEC")
    Jump("loc_1EF5")

    label("loc_1EEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1EF5")

    label("loc_1EF5")

    TalkEnd(0xFE)
    Return()

    # Function_4_1345 end

    def Function_5_1EF9(): pass

    label("Function_5_1EF9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1F0A")
    Jump("loc_2517")

    label("loc_1F0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2002")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F96")

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
            "I've never met him, so I\x01",
            "wonder what kind of\x01",
            "person he is?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FFD")

    label("loc_1F96")


    ChrTalk(
        0xFE,
        (
            "Aaallright, I won't\x01",
            "lose!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Someday I'll get my\x01",
            "revenge on the Imperial\x01",
            "Fishing Club for sure!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FFD")

    Jump("loc_2517")

    label("loc_2002")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2010")
    Jump("loc_2517")

    label("loc_2010")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2085")

    ChrTalk(
        0xFE,
        (
            "I should... I should be\x01",
            "able to do more, way\x01",
            "more!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How frustrating... How\x01",
            "very frustrating!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2517")

    label("loc_2085")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2093")
    Jump("loc_2517")

    label("loc_2093")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2131")

    ChrTalk(
        0xFE,
        (
            "Ooh, why is it that no matter\x01",
            "how many times I challenge the\x01",
            "Dragon Queen, I can't win!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What the... What the\x01",
            "hell is wrong with me!?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2517")

    label("loc_2131")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2230")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21D8")

    ChrTalk(
        0xFE,
        (
            "Even so, that monster...\x01",
            "The more you look at it,\x01",
            "the more ghastly it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And its size on top of\x01",
            "that... Give me a break\x01",
            "already.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_222B")

    label("loc_21D8")


    ChrTalk(
        0xFE,
        (
            "Come now, I'll get back\x01",
            "what I've lost!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aim for the Dragon Queen\x01",
            "Killer!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_222B")

    Jump("loc_2517")

    label("loc_2230")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_235F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22CF")

    ChrTalk(
        0xFE,
        (
            "Whoa, I caught a another\x01",
            "Noble Carp.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're quite rare in\x01",
            "Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. As I thought, I\x01",
            "feel something's amiss.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_235A")

    label("loc_22CF")


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
            "Could something be\x01",
            "happening to the\x01",
            "Crossbell ecosystem?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_235A")

    Jump("loc_2517")

    label("loc_235F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2499")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2425")

    ChrTalk(
        0xFE,
        "213, 214, 215...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Before attaching bait,\x01",
            "I'll do 1000 down thrusts\x01",
            "with the rod again today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This special training\x01",
            "builds up your arm\x01",
            "strength quite a bit!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2494")

    label("loc_2425")


    ChrTalk(
        0xFE,
        (
            "The Goddess doesn't\x01",
            "smile on those who don't\x01",
            "work hard!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "An angler must be\x01",
            "diligent every single\x01",
            "day!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2494")

    Jump("loc_2517")

    label("loc_2499")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2500")

    ChrTalk(
        0xFE,
        (
            "C'mon, let's start the\x01",
            "training at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just you wait, Imperial\x01",
            "Fishing Club!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2517")

    label("loc_2500")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_250E")
    Jump("loc_2517")

    label("loc_250E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2517")

    label("loc_2517")

    TalkEnd(0xFE)
    Return()

    # Function_5_1EF9 end

    def Function_6_251B(): pass

    label("Function_6_251B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_25BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2539")
    Call(0, 7)
    Jump("loc_25B9")

    label("loc_2539")


    ChrTalk(
        0xB,
        (
            "Damn. Even though I'm\x01",
            "the enemy, why is this\x01",
            "guy being so friendly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As if I'll ever approve\x01",
            "of such strange\x01",
            "behavior!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25B9")

    Jump("loc_25E3")

    label("loc_25BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_25CC")
    Jump("loc_25E3")

    label("loc_25CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_25DA")
    Jump("loc_25E3")

    label("loc_25DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_25E3")

    label("loc_25E3")

    TalkEnd(0xFE)
    Return()

    # Function_6_251B end

    def Function_7_25E7(): pass

    label("Function_7_25E7")

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
            "Hmph, wasn't it you who\x01",
            "said we could use this\x01",
            "place? ...Don't complain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Of course, I promised\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "However, this place is pretty\x01",
            "inconvenient sometimes. You can come to\x01",
            "the branch whenever you want, you know?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xB)

    ChrTalk(
        0xB,
        (
            "H-Hmph... We haven't\x01",
            "fallen so low as to be\x01",
            "cared about by you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xA, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_7_25E7 end

    def Function_8_276E(): pass

    label("Function_8_276E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2804")

    ChrTalk(
        0xC,
        (
            "*sigh*... I'd forgotten about\x01",
            "it, but we're borrowing this\x01",
            "shed from him, Celdan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Our time alone\x01",
            "together...\x01",
            "Unforgivable!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2829")

    label("loc_2804")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2812")
    Jump("loc_2829")

    label("loc_2812")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_2820")
    Jump("loc_2829")

    label("loc_2820")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2829")

    label("loc_2829")

    TalkEnd(0xFE)
    Return()

    # Function_8_276E end

    def Function_9_282D(): pass

    label("Function_9_282D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 4)), scpexpr(EXPR_END)), "loc_2859")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 6)), scpexpr(EXPR_END)), "loc_2847")
    Call(0, 20)
    Jump("loc_2854")

    label("loc_2847")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2854")
    Call(0, 19)

    label("loc_2854")

    Jump("loc_28E1")

    label("loc_2859")

    EventBegin(0x2)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Azure flowers are\x01",
            "blooming.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00000F(What pretty flowers.\x01",
            "They seem to be faintly\x01",
            "glowing, though...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x168, 4)
    EventEnd(0x3)

    label("loc_28E1")

    Return()

    # Function_9_282D end

    def Function_10_28E2(): pass

    label("Function_10_28E2")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00003F(With this we've beaten\x01",
            "the two Cryptids, but...\x01",
            "Something's bothering me.)\x02\x03",
            "#00000FEveryone, could we go back\x01",
            "to the scene to\x01",
            "investigate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIndeed, I too feel\x01",
            "there's something we\x01",
            "must do here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FThen, let's head back\x01",
            "and investigate.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 91500, 0, 0, 90)
    EventEnd(0x4)
    Return()

    # Function_10_28E2 end

    def Function_11_2A05(): pass

    label("Function_11_2A05")

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
            "Fish\x01",        # 0
            "Cancel\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AC7")
    OP_E2(0x2)
    MiniGame(0x6, 0x18, 0x73D2, 0x0, 0xD2, 0x5A, 0x933A, 0xFFFFFC18, 0x76C)

    label("loc_2AC7")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_11_2A05 end

    def Function_12_2ACC(): pass

    label("Function_12_2ACC")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The doors are firmly\x01",
            "locked.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_12_2ACC end

    def Function_13_2B04(): pass

    label("Function_13_2B04")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B36")
    SetScenarioFlags(0x31, 2)

    label("loc_2B36")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2B7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_2B76")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2B6B")
    Sound(2499, 255, 100, 0)
    Jump("loc_2B71")

    label("loc_2B6B")

    Sound(3537, 255, 100, 0)

    label("loc_2B71")

    Jump("loc_2B7C")

    label("loc_2B76")

    Sound(3344, 255, 100, 0)

    label("loc_2B7C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_2BF1")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2BD1"),
        (SWITCH_DEFAULT, "loc_2BE2"),
    )


    label("loc_2BD1")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_2BEC")

    label("loc_2BE2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2BEC")

    Jump("loc_2E2E")

    label("loc_2BF1")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_2C23")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_2C23")

    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2C57"),
        (1, "loc_2D5B"),
        (2, "loc_2DEC"),
        (SWITCH_DEFAULT, "loc_2E24"),
    )


    label("loc_2C57")

    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    OP_74(0x8, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2C88")
    OP_70(0x8, 0x12C)
    OP_71(0x8, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_2C98")

    label("loc_2C88")

    OP_70(0x8, 0xF0)
    OP_71(0x8, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_2C98")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CEE")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2CEE")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D11")
    Sound(461, 0, 100, 0)

    label("loc_2D11")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D31")
    OP_70(0x8, 0x14A)
    OP_71(0x8, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_2D41")

    label("loc_2D31")

    OP_70(0x8, 0x10E)
    OP_71(0x8, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_2D41")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x8, "light", 0x1, 0x1)
    OP_70(0x8, 0x0)
    Jump("loc_2B7C")

    label("loc_2D5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_2DCD")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_2D90")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_2DA8")

    label("loc_2D90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2DA3")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_2DA8")

    label("loc_2DA3")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_2DA8")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2DE7")

    label("loc_2DCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2DDD")
    OP_AF(0xFB)
    Jump("loc_2DE7")

    label("loc_2DDD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2DE7")

    Jump("loc_2E2E")

    label("loc_2DEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E05")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E1F")

    label("loc_2E05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2E15")
    OP_AF(0xFB)
    Jump("loc_2E1F")

    label("loc_2E15")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E1F")

    Jump("loc_2E2E")

    label("loc_2E24")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E2E")

    Jump("loc_2B7C")

    label("loc_2E33")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_13_2B04 end

    def Function_14_2E41(): pass

    label("Function_14_2E41")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_2E9C")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2E91")
    Sound(2502, 255, 100, 0)
    Jump("loc_2E97")

    label("loc_2E91")

    Sound(2503, 255, 100, 0)

    label("loc_2E97")

    Jump("loc_2EC0")

    label("loc_2E9C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2EBA")
    Sound(3347, 255, 100, 0)
    Jump("loc_2EC0")

    label("loc_2EBA")

    Sound(3348, 255, 100, 0)

    label("loc_2EC0")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_14_2E41 end

    def Function_15_2ED5(): pass

    label("Function_15_2ED5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2EDF")
    Return()

    label("loc_2EDF")

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
            "A large monster is\x01",
            "wandering about.\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Exterminate]\x01",      # 0
            "[Cancel]\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_2FBD"),
        (SWITCH_DEFAULT, "loc_2FD6"),
    )


    label("loc_2FBD")

    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, 106900, 0, 4400, 90)
    EventEnd(0x5)
    Return()

    label("loc_2FD6")

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
        (2, "loc_3098"),
        (1, "loc_309D"),
        (SWITCH_DEFAULT, "loc_30A0"),
    )


    label("loc_3098")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    label("loc_309D")

    OP_B9(0x0)
    Return()

    label("loc_30A0")

    Call(0, 18)
    Return()

    # Function_15_2ED5 end

    def Function_16_30A4(): pass

    label("Function_16_30A4")

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

    def lambda_3190():
        OP_9B(0x0, 0x101, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3190)
    Sleep(0)

    def lambda_31A8():
        OP_9B(0x0, 0x102, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_31A8)
    Sleep(0)

    def lambda_31C0():
        OP_9B(0x0, 0x103, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_31C0)
    Sleep(0)

    def lambda_31D8():
        OP_9B(0x0, 0x104, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_31D8)
    Sleep(0)

    def lambda_31F0():
        OP_9B(0x0, 0x109, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_31F0)
    Sleep(0)

    def lambda_3208():
        OP_9B(0x0, 0x105, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3208)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_331C")

    ChrTalk(
        0x109,
        "#10111F#6P(Ah...!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00013F#5P(That's a Cryptid,\x01",
            "huh!?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3353")

    label("loc_331C")


    ChrTalk(
        0x105,
        "#10305F#6P(Whoa...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#5P(There it is!)\x02",
    )

    CloseMessageWindow()

    label("loc_3353")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3691")

    ChrTalk(
        0x104,
        (
            "#00303F#9P(Like the report said,\x01",
            "it's quite huge...)\x02\x03",
            "#00301F(PeTiote, how about the\x01",
            "spatial distortion?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#9P(Time, Space, Mirage...\x01",
            "Manifestation of the higher\x01",
            "elements confirmed.)\x02\x03",
            "#00201F(The cause is unclear at\x01",
            "present.)\x02",
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

    def lambda_3543():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3543)
    Sleep(0)

    def lambda_3553():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3553)
    Sleep(0)

    def lambda_3563():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3563)
    Sleep(0)

    def lambda_3573():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3573)
    Sleep(0)

    def lambda_3583():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3583)
    Sleep(0)

    def lambda_3593():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3593)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_93(0x101, 0x10E, 0x1F4)

    ChrTalk(
        0x105,
        "#10301F#6P(So... What do we do?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11P(According to the CGF\x01",
            "report, it seems pretty\x01",
            "dangerous...)\x02\x03",
            "#00013F(If we're going to\x01",
            "eliminate it, let's make\x01",
            "sure we're ready.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#12P(Roger!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_3862")

    label("loc_3691")


    ChrTalk(
        0x102,
        (
            "#00101F#9P(Tio... How's the\x01",
            "spatial distortion?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#9P(I've confirmed\x01",
            "manifestation of the higher\x01",
            "elements here as well...)\x02\x03",
            "#00201F(The cause of this\x01",
            "distortion is unknown as\x01",
            "well.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#9P(I knew it...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10308F#9P(It seems the Cryptid\x01",
            "itself isn't causing it,\x01",
            "though...)\x02",
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
            "#10101F#6P(Lloyd... Are we\x01",
            "fighting it\x01",
            "immediately?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00013F#5P(Yeah, let's proceed\x01",
            "with caution!)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3862")

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

    # Function_16_30A4 end

    def Function_17_389D(): pass

    label("Function_17_389D")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C50")
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
    Jump("loc_3C6A")

    label("loc_3C50")

    OP_75(0x6, 0x2, 0x0)
    OP_75(0x7, 0x2, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    label("loc_3C6A")

    Battle("BattleInfo_4EC", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetScenarioFlags(0x168, 1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CFE")
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
    Jump("loc_3D01")

    label("loc_3CFE")

    Call(0, 18)

    label("loc_3D01")

    Return()

    # Function_17_389D end

    def Function_18_3D02(): pass

    label("Function_18_3D02")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40DA")

    ChrTalk(
        0x101,
        (
            "#00006F#5PGuh... As expected, it\x01",
            "was strong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6PAnd also... It vanished\x01",
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

    def lambda_3F2F():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3F2F)
    Sleep(50)

    def lambda_3F3F():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3F3F)
    Sleep(50)

    def lambda_3F4F():
        TurnDirection(0x103, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3F4F)
    Sleep(50)

    def lambda_3F5F():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3F5F)
    Sleep(50)

    def lambda_3F6F():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3F6F)
    Sleep(50)

    def lambda_3F7F():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3F7F)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x109,
        (
            "#10108F#12PTio. How's the "spatial\x01",
            "distortion"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6P...It's no good. The\x01",
            "higher elements are\x01",
            "still at work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#5PJeez... What the heck is\x01",
            "causin' it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#11PIt seems the Cryptid\x01",
            "itself isn't the cause,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00013F#11PLooks like we need to\x01",
            "check the other one too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4527")

    label("loc_40DA")


    ChrTalk(
        0x105,
        (
            "#10306F#6POh man... This one was\x01",
            "strong too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#6PHowever, it vanished in\x01",
            "the same way...\x02",
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

    def lambda_418A():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_418A)
    Sleep(50)

    def lambda_419A():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_419A)
    Sleep(50)

    def lambda_41AA():
        TurnDirection(0x103, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_41AA)
    Sleep(50)

    def lambda_41BA():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_41BA)
    Sleep(50)

    def lambda_41CA():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_41CA)
    Sleep(50)

    def lambda_41DA():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_41DA)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x104,
        (
            "#00301F#5PThe "spatial distortion"\x01",
            "is still here, isn't it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#6PThat's right...\x02\x03",
            "#00201FIt's just, I feel like\x01",
            "there's some kind of\x01",
            "specific cause.\x02",
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
            "#00005F#11PA specific cause? Like\x01",
            "what?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6P...Well... My senses have been\x01",
            "disturbed by the "distortion"\x01",
            "for some time now...\x02\x03",
            "#00200FInstead, you all may be able\x01",
            "to find the cause.\x02",
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
            "#00003F#11PAll right... Let's\x01",
            "search the area.\x02\x03",
            "#00000FWhatever's causing the\x01",
            ""spatial distortion" is\x01",
            "definitely nearby.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_445D():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_445D)
    Sleep(50)

    def lambda_446D():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_446D)
    Sleep(50)

    def lambda_447D():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_447D)
    Sleep(50)

    def lambda_448D():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_448D)
    Sleep(50)

    def lambda_449D():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_449D)
    Sleep(50)

    def lambda_44AD():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_44AD)
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
        (
            "#00300F#5PLet's search whatever we\x01",
            "can get our hands on!\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0xA6, 0x1, 0x3)

    label("loc_4527")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Defeated the East\x01",
            "Crossbell Highway\x01",
            "Cryptid!\x07\x00\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_45C3")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_45C3")

    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_37()
    EventEnd(0x5)
    Return()

    # Function_18_3D02 end

    def Function_19_45D3(): pass

    label("Function_19_45D3")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49F1")
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 3)), scpexpr(EXPR_END)), "loc_4808")

    AnonymousTalk(
        0x102,
        (
            "#00108FThey seem similar to the ones\x01",
            "that were blooming at St.\x01",
            "Ursula Byroad sandbank...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        (
            "#00305FYeah, we saw 'em there,\x01",
            "alright.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_48AA")

    label("loc_4808")


    AnonymousTalk(
        0x105,
        (
            "#10302FDidn't we see these\x01",
            "blooming at St. Ursula\x01",
            "Byroad sandbank?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#00011FY-You think so?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00108FYes, I feel like I saw\x01",
            "them there too...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_48AA")


    AnonymousTalk(
        0x109,
        (
            "#10109FThey're very pretty\x01",
            "flowers...\x02\x03",
            "#10102FBut I don't think I've ever\x01",
            "seen them before. I wonder\x01",
            "what they're called.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#00001FHmm...\x02",
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
            "#00003F#11P(...I think it's\x01",
            "unlikely, but...)\x02\x03",
            "#00001F(Well, maybe it's worth\x01",
            "a try?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x161, 2)
    OP_29(0xA6, 0x1, 0x4)
    Jump("loc_4AAE")

    label("loc_49F1")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(300)

    AnonymousTalk(
        0x101,
        (
            "#00003F#11P(...I think it's\x01",
            "unlikely, but...)\x02\x03",
            "#00001F(Well, maybe it's worth\x01",
            "a try?)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    label("loc_4AAE")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Try picking the azure flowers\x01",      # 0
            "Cancel\x01",                             # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4B0D"),
        (1, "loc_5964"),
        (SWITCH_DEFAULT, "loc_59A3"),
    )


    label("loc_4B0D")

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
            "#10305F#6PWhat, you're picking\x01",
            "these flowers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11PYeah... Though I feel a\x01",
            "little sorry for them─\x02",
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
        "#00301F#5PW-What!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#12PThis is...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#11PGuh!\x02",
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
        "#10111F#5PW-What was that...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FIt's almost like the air\x01",
            "was shaking...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x103, 500)

    ChrTalk(
        0x105,
        (
            "#10308F#6P...Tio. How's the\x01",
            ""spatial distortion"?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)

    ChrTalk(
        0x103,
        (
            "#00203F#12PPresence of the higher\x01",
            "elements have\x01",
            "disappeared.\x02\x03",
            "#00201FI can't sense any\x01",
            "disturbances in this\x01",
            "entire area any longer.\x02",
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
            "#00307FYou're tellin' me those\x01",
            "azure flowers were\x01",
            "causin' the anomaly!?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    ChrTalk(
        0x105,
        (
            "#10304F#6PWell, that must be it.\x02\x03",
            "#10300FThough I can't think\x01",
            "those tiny flowers have\x01",
            "that kind of power.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101FU-Unbelievable...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#5PW-What kind of flowers\x01",
            "are these?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#12PI don't sense a strange\x01",
            "presence from those\x01",
            "flowers any longer, but...\x02\x03",
            "#00200FFor now, perhaps we should\x01",
            "have them investigated\x01",
            "somewhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#11PThat's right...\x02\x03",
            "#00003F...It's probably a bit of a\x01",
            "different field than the\x01",
            "medical college specializes in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FA-Anyway, let's hang on to\x01",
            "them so we don't lose them.\x02\x03",
            "If we come up with some\x01",
            "idea about them, we'll have\x01",
            "them investigated, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#11PYeah, sounds good.\x02",
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
        "#10303F#6P...Hmm...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_5315():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5315)
    Sleep(50)

    def lambda_5325():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5325)
    Sleep(50)

    def lambda_5335():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5335)
    Sleep(50)

    def lambda_5345():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5345)
    Sleep(50)

    def lambda_5355():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5355)
    Sleep(50)

    def lambda_5365():
        TurnDirection(0x105, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5365)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#11PWazy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#5PDo you have an idea?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#6PWell... Maybe it's a faint\x01",
            "memory of mine.\x02\x03",
            "#10301FI feel like there's legend\x01",
            "about a mysterious azure flower\x01",
            "in the church Testaments.\x02",
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
        "#00011F#11PHUH!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F#5PWhoa, seriously!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#6PWell, I feel like I saw\x01",
            "it when I skimmed them a\x01",
            "long time ago, but...\x02\x03",
            "#10300FAny ideas, Elie?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00112F#11PAs you might imagine, I\x01",
            "haven't read through the\x01",
            "entire Testaments, but...\x02\x03",
            "#00103FIndeed, I feel like I\x01",
            "read such a passage.\x02\x03",
            "#00108FA legend of an "azure\x01",
            "flower" with mysterious\x01",
            "powers...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)

    ChrTalk(
        0x109,
        (
            "#10111F#6PThat's... Bingo, isn't\x01",
            "it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#00201F#12PIt seems there's value in\x01",
            "confirming it with a\x01",
            "Church official, at least.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_56E5():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_56E5)
    Sleep(50)

    def lambda_56F5():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_56F5)
    Sleep(50)

    def lambda_5705():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5705)
    Sleep(50)

    def lambda_5715():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5715)
    Sleep(50)

    def lambda_5725():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5725)
    Sleep(50)

    def lambda_5735():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5735)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_57F6")

    ChrTalk(
        0x101,
        (
            "#00003F#11P...Right.\x02\x03",
            "#00000FLet's try asking Miss\x01",
            "Marble or Ries about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FYes... Either of them\x01",
            "would be qualified, I\x01",
            "think.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58B0")

    label("loc_57F6")


    ChrTalk(
        0x101,
        (
            "#00003F#11PRight.\x02\x03",
            "#00000FI think that Miss Marble\x01",
            "would be the easiest to\x01",
            "consult with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FYes, I think she's\x01",
            "qualified.\x02\x03",
            "#00108F(We could consult with\x01",
            ""her" too, but...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58B0")


    ChrTalk(
        0x104,
        (
            "#00300F#5PAlllright, then let's\x01",
            "head to Crossbell\x01",
            "Cathedral!\x02",
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
    Jump("loc_59A3")

    label("loc_5964")

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
    Jump("loc_59A3")

    label("loc_59A3")

    Return()

    # Function_19_45D3 end

    def Function_20_59A4(): pass

    label("Function_20_59A4")

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
            "They might turn out to\x01",
            "be valuable samples.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        (
            "#00200FIndeed. It seems they\x01",
            "lose their powers when\x01",
            "picked.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00100FHowever... if a Cryptid\x01",
            "appears again, maybe we'll\x01",
            "have to pick them up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        (
            "#00300FWell, we'll deal with\x01",
            "that when it happens.\x02",
        )
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

    # Function_20_59A4 end

    def Function_21_5CC2(): pass

    label("Function_21_5CC2")

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
            "Hmm. Anyway, that sure\x01",
            "is a creepy monster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PI-If something like that\x01",
            "were to come here, we'd\x01",
            "be helpless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yeah. If that happens,\x01",
            "we must evacuate right\x01",
            "away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But for now, we'll wait\x01",
            "for the CGF to come...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "Oh... If it isn't Member\x01",
            "Lloyd!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(37180, 1400, -14790, 4000)
    MoveCamera(33, 33, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(14430, 4000)

    def lambda_5E86():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5E86)

    def lambda_5E93():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5E93)
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

    def lambda_5F21():
        OP_95(0xFE, 36720, 0, -14030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F21)
    Sleep(300)

    def lambda_5F3E():
        OP_95(0xFE, 36720, 0, -15170, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5F3E)
    Sleep(300)

    def lambda_5F5B():
        OP_95(0xFE, 35680, 0, -13860, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5F5B)
    Sleep(300)

    def lambda_5F78():
        OP_95(0xFE, 35680, 0, -15050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5F78)
    Sleep(300)

    def lambda_5F95():
        OP_95(0xFE, 34560, 0, -13930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5F95)
    Sleep(300)

    def lambda_5FB2():
        OP_95(0xFE, 34700, 0, -14930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5FB2)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)

    ChrTalk(
        0x101,
        (
            "#6P#00003FLong time no see, Branch\x01",
            "Manager Celdan.\x02\x03",
            "#00001FWe heard that a mysterious\x01",
            "large monster, a Cryptid,\x01",
            "has appeared here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "A Cryptid... Hmm, an\x01",
            "expression that fits\x01",
            "perfectly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yeah. That Cryptid or whatever\x01",
            "appeared suddenly yesterday evening\x01",
            "deep inside the swamp, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We contacted the CGF,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PCould it be that your\x01",
            "Special Support Section has\x01",
            "come to deal with it, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FYes, we took the request\x01",
            "from the CGF.\x02\x03",
            "#00101FCould you tell us the\x01",
            "situation in detail?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yes, like I just told you,\x01",
            "the first time we noticed\x01",
            "it was yesterday evening...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Without any warning at all, we\x01",
            "suddenly heard something that\x01",
            "sounded like an animal cry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PA suspicious shadow flickered in\x01",
            "the deep part of the marsh\x01",
            "that's always been sealed off...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PWe all approached it\x01",
            "cautiously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThen, we spotted that\x01",
            "mysterious Cryptid or\x01",
            "whatever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThen, we hastily made a\x01",
            "report to the CGF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We thought to run away, but...\x01",
            "There's no sign the Cryptid is\x01",
            "moving from that spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Since yesterday, we've been\x01",
            "taking turns watching it and\x01",
            "monitoring the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203F...That was excellent\x01",
            "work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FDid you notice anything\x01",
            "strange while keeping\x01",
            "watch?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, nothing as strange\x01",
            "as the thing itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Even though we surrounded it\x01",
            "from this distance, I feel\x01",
            "like it's hostile, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PHow to say this... I feel\x01",
            "like it's not that it isn't\x01",
            "moving... it's that it can't.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PWe don't know the\x01",
            "details, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303FI see. It suddenly\x01",
            "appeared and is rooted\x01",
            "to the spot, huh...\x02",
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
            "#00013FThen, Branch Manager\x01",
            "Celdan. I'd like to go\x01",
            "inside immediately...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Oh, you're going to\x01",
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
            "All right, you're all\x01",
            "set. We leave the rest\x01",
            "to you.\x02",
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

    # Function_21_5CC2 end

    def Function_22_6833(): pass

    label("Function_22_6833")

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
            "#6POh, Member Lloyd. Were\x01",
            "you able to exterminate\x01",
            "the Cryptid?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PYes, somehow or other.\x02\x03",
            "#00000FI think you need to be careful,\x01",
            "but I also don't think it will\x01",
            "appear again for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PSeriously? That's good\x01",
            "to hear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PHaha, now we can devote\x01",
            "ourselves to fishing\x01",
            "once again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PYeah, this really helps\x01",
            "us out.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6DA3")

    ChrTalk(
        0x8,
        "#6POh, right, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PCould you accept this as\x01",
            "thanks?\x02",
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
        (
            "#00005F#11PIs this... a new fishing\x01",
            "rod?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PYes, I put it together\x01",
            "to oppose the Imperial\x01",
            "Fishing Club.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PIf you have this, you\x01",
            "should be able pull in\x01",
            "much larger fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#11PPeter, you did this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PHaha. He doesn't look it,\x01",
            "but Peter's forte is\x01",
            "messing around with tools.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PEvery now and then, he makes new\x01",
            "fishing gear by modding off-the-\x01",
            "shelf stuff, just like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PHehe, it's a wonderful story\x01",
            "somehow, since he's not at\x01",
            "all strong at fishing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PStop it, Coppen. That\x01",
            "was uncalled for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11PAhaha...\x02\x03",
            "#00000FBut really, thanks for\x01",
            "giving me such a nice\x01",
            "rod.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_743C")

    label("loc_6DA3")


    ChrTalk(
        0xA,
        (
            "#6POh, that's right, Member\x01",
            "Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PI didn't tell you, but I'd like\x01",
            "to explain about Angler Duels\x01",
            "with the Imperial Fishing Club...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#11PA-Angler Duels...?\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00003F#11PI see, Angler Duels against\x01",
            "the five members of the\x01",
            "Imperial Fishing Club...\x02\x03",
            "If I win, we'll get back\x01",
            "the office and the occupied\x01",
            "fishing spots...\x02\x03",
            "#00001FAnd if I lose, we'll be at\x01",
            "their mercy, right?\x02",
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
            "#6PWell for now, we plan to\x01",
            "do something about the\x01",
            "matches in our own way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PMember Lloyd, you're probably busy\x01",
            "with your job, so I don't mind if\x01",
            "you merely keep them in mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#11PAlright, understood.\x02",
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
            "#6PCould you accept this as\x01",
            "thanks?\x02",
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
        (
            "#00005F#11PIs this... a new fishing\x01",
            "rod?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PYes, I put it together\x01",
            "to oppose the Imperial\x01",
            "Fishing Club.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PIf you have this, you\x01",
            "should be able pull in\x01",
            "much larger fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#11PPeter, you did this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PHaha. He doesn't look it,\x01",
            "but Peter's forte is\x01",
            "messing around with tools.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PEvery now and then, he makes new\x01",
            "fishing gear by modding off-the-\x01",
            "shelf stuff, just like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PHehe, it's a wonderful story\x01",
            "somehow, since he's not at\x01",
            "all strong at fishing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PStop it, Coppen. That\x01",
            "was uncalled for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11PAhaha...\x02\x03",
            "#00000FBut really, thanks for\x01",
            "giving me such a nice\x01",
            "rod.\x02",
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
            "You are now able to challenge\x01",
            "Imperial Fishing Club members\x01",
            "to Angler Duels.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You can ask the details of the matches\x01",
            "from Receptionist Sylum at the "East\x01",
            "Street Imperial Fishing Club".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1C0, 0)

    label("loc_743C")

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

    # Function_22_6833 end

    def Function_23_74A3(): pass

    label("Function_23_74A3")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 1)), scpexpr(EXPR_END)), "loc_7620")
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
        (
            "#00002FYes, somehow I've\x01",
            "gathered them all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm. Then, I'll try\x01",
            "putting them together\x01",
            "right now!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_798A")

    label("loc_7620")

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
            "#00004FYes, there's no mistaking it. It's\x01",
            "a fishing gear part. And a very\x01",
            "pretty one at that.\x02\x03",
            "#00000FI caught a rare fish from a fishing\x01",
            "spot I recovered from the Elite\x01",
            "Four... The fish spat that out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "...No doubt.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That's a part of the legendary\x01",
            "gear that was once used by a\x01",
            "remarkable wandering angler.\x02",
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
            "To think you found it\x01",
            "like that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FI-Is it that amazing?\x02\x03",
            "#00003FThen, what do we do? We\x01",
            "should give it back to\x01",
            "him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No, there's no need for\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Because he said that\x01",
            "he who finds his fishing\x01",
            "gear, may use it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Also, there are 4 parts in\x01",
            "total... Wait, you've already\x01",
            "collected them all, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then, I'll try putting\x01",
            "them together right now.\x01",
            "Is that all right, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FY-Yes, sir.\x02",
    )

    CloseMessageWindow()

    label("loc_798A")

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
            "#00004FIndeed... All put\x01",
            "together like this, it's\x01",
            "amazing and cool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, well then, Lloyd.\x01",
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
        (
            "#00005FI-Is it all right for me\x01",
            "to use it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uhuhu, what are you saying?\x01",
            "You're the one who found\x01",
            "it, so it's only natural.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It appears you've\x01",
            "defeated all of the\x01",
            "Elite Four...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please go defeat the\x01",
            "remaining Lakelord while\x01",
            "freely swinging that rod!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FR-Right... Understood!\x02",
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

    # Function_23_74A3 end

    def Function_24_7C0B(): pass

    label("Function_24_7C0B")

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
            "Member Lloyd... No,\x01",
            "Master Lloyd, the\x01",
            "Fishing Emperor Slayer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Thank you so much for what you\x01",
            "did. No matter how much I thank\x01",
            "you, it won't ever be enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You've were really\x01",
            "amazing, Master Lloyd!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hmm. That the Crossbell Branch of the Fishermen's\x01",
            "Guild was defended at the hands of one so young makes\x01",
            "me happy and proud from the bottom of my heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uhuhu. I will pass down\x01",
            "these Angler Duels\x01",
            "orally for eternity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FN-No way, you're\x01",
            "exaggerating.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(2190, 1200, -8070, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        (
            "#00102F(Hmm, they're really\x01",
            "praising him a lot.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103F(I don't really get it,\x01",
            "but... It seems he's a\x01",
            "true hero.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F(The Fishing Emperor\x01",
            "Slayer... Maybe he's\x01",
            "just a little bit cool.)\x02",
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

    # Function_24_7C0B end

    SaveToFile()

Try(main)
