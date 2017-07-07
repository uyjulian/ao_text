from ScenarioHelper import *

def main():
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
        "Falsehood",               # 1
        "僐僷 儞",                 # 2
        "Penetrating",         # 3
        "儗僀 僋儘 乕僪 嘨悽",       # 4
        "棾媨 僇僌 儎",             # 5
        "僢僔 儍乕 insertion",       # 6
        "尪廱",                   # 7
        "尪廱",                   # 8
        "尪廱",                   # 9
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
        "Function_4_1346",         # 04, 4
        "Function_5_1E14",         # 05, 5
        "Function_6_23A3",         # 06, 6
        "Function_7_2463",         # 07, 7
        "Function_8_25E2",         # 08, 8
        "Function_9_26A7",         # 09, 9
        "Function_10_2755",        # 0A, 10
        "Function_11_286B",        # 0B, 11
        "Function_12_293F",        # 0C, 12
        "Function_13_2979",        # 0D, 13
        "Function_14_2CBC",        # 0E, 14
        "Function_15_2D50",        # 0F, 15
        "Function_16_2F23",        # 10, 16
        "Function_17_36C0",        # 11, 17
        "Function_18_3B25",        # 12, 18
        "Function_19_43B0",        # 13, 19
        "Function_20_5684",        # 14, 20
        "Function_21_5975",        # 15, 21
        "Function_22_641D",        # 16, 22
        "Function_23_6FF8",        # 17, 23
        "Function_24_7706",        # 18, 24
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

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1342")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1138")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_118C")

    label("loc_1138")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_118C")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_118C")

    label("loc_118C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 5)), scpexpr(EXPR_END)), "loc_11AB")
    OP_AF(0x37)
    Jump("loc_11AD")

    label("loc_11AB")

    OP_AF(0x36)

    label("loc_11AD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_133D")

    label("loc_11BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_133D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_12CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11F0")
    Call(0, 7)
    Jump("loc_12BE")

    label("loc_11F0")


    ChrTalk(
        0xA,
        (
            "But … in this cabin\x01",
            "To live nearly a month\x01",
            "You really are a strong guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Apparently I made dried fish,\x01",
            "Take something like wild grass to eat\x01",
            "It seems to have surpassed … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I'm totally looking up at the guts.\x02",
    )

    CloseMessageWindow()

    label("loc_12BE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_133D")

    label("loc_12CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_133D")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        "Members of Lloyd, please be careful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We are here\x01",
            "Because I will keep you waiting,\x01",
            "I have entrusted the eidolon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_133D")

    Jump("loc_1111")

    label("loc_1342")

    TalkEnd(0xFE)
    Return()

    # Function_3_1104 end

    def Function_4_1346(): pass

    label("Function_4_1346")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_137F")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('绀碧竿', 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber('琥珀轴', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('翡翠线', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('红莲钩', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_137F")
    Call(0, 23)
    Return()

    label("loc_137F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1740")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('绀碧竿', 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber('琥珀轴', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('翡翠线', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('红莲钩', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13B3")
    Jump("loc_1740")

    label("loc_13B3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('绀碧竿', 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber('琥珀轴', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('翡翠线', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('红莲钩', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1740")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 500)

    ChrTalk(
        0xFE,
        "Lloyd, that is … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah, definitely fishing tackle\x01",
            "I think it is a part,\x01",
            "It is very beautiful, is not it?\x02\x03",
            "#00000FAt the fishing spot recovered from the four heavenly kings\x01",
            "I caught an unusual fish ….\x01",
            "That fish spit out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……There is no mistake.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was once a great fighter of travel\x01",
            "It is a part of the legendary fishing gear that I was using.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When he leaves the crossbell,\x01",
            "It was sealed in this place\x01",
            "I was listening … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No way,\x01",
            "What you can find out like this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FWell, so much\x01",
            "Was it amazing ……\x02\x03",
            "#00003FBut what shall I do.\x01",
            "If you return to that person … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "No, that is not necessary.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… … because he said.\x01",
            "The fishing tackle can be used by those who found it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lloyd,\x01",
            "There are four parts in all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you get all that\x01",
            "Please come to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I am using that part\x01",
            "It can be assembled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FI see, I see … ….\x01",
            "Okay, I will remember.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x1C0, 1)
    TalkEnd(0xFE)
    Return()

    label("loc_1740")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_17C7")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "Legendary fishing tackle sealed once\x01",
            "What is said to appear at such times …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, Lloyd.\x01",
            "This may be destiny, is not it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E10")

    label("loc_17C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_17D5")
    Jump("loc_1E10")

    label("loc_17D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_19B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1907")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_189F")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('绀碧竿', 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber('琥珀轴', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('翡翠线', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('红莲钩', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1814")
    Jump("loc_189A")

    label("loc_1814")


    ChrTalk(
        0xFE,
        (
            "Well, I can not wait to meet that person\x01",
            "I can not wait to have fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhufu, everyone in the Emperor 's Club,\x01",
            "It is inside of now that I can laugh.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_189A")

    Jump("loc_1902")

    label("loc_189F")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "Lloyd, with that aqua ruler\x01",
            "Defeat Lake Road!\x01",
            "- Thank you!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1902")

    Jump("loc_19AB")

    label("loc_1907")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "\"Emperor Slayer\" Lloyd teacher.\x01",
            "This time is really wonderful\x01",
            "Thank you for your active participation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ufufu, this time the battle for bombing,\x01",
            "You will be handed down until the last days.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19AB")

    Jump("loc_1E10")

    label("loc_19B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_19BE")
    Jump("loc_1E10")

    label("loc_19BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_19CC")
    Jump("loc_1E10")

    label("loc_19CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_19DA")
    Jump("loc_1E10")

    label("loc_19DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1A54")

    ChrTalk(
        0xFE,
        (
            "Branch chief and Copan\x01",
            "I will not win, no matter how many times I challenge ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As if it were a bad dream\x01",
            "I feel like I'm being seen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E10")

    label("loc_1A54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1C1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AE8")

    ChrTalk(
        0xFE,
        (
            "Everyone came,\x01",
            "I was relieved from the bottom of my heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When will it attack from yesterday,\x01",
            "I was worried because I did not get it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C19")

    label("loc_1AE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BA7")

    ChrTalk(
        0xFE,
        (
            "Well, I also want to train Bosscho.\x01",
            "Shall I restart it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As yet one of the four heavenly kings\x01",
            "I am the only one who can not be defeated … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is about time, seriously.\x01",
            "I will have you return the stigma.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C19")

    label("loc_1BA7")


    ChrTalk(
        0xFE,
        (
            "As yet one of the four heavenly kings\x01",
            "I am the only one who can not be defeated … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is about time, seriously.\x01",
            "I will let you return the stigma.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C19")

    Jump("loc_1E10")

    label("loc_1C1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1CBC")

    ChrTalk(
        0xFE,
        (
            "Kopan … …\x01",
            "With that vision Noble Carb\x01",
            "You can only catch that one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, as early as possible\x01",
            "Is it the result of training?\x01",
            "I can not lose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E10")

    label("loc_1CBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1D64")

    ChrTalk(
        0xFE,
        (
            "Well, I am a little too\x01",
            "It seems to be helpful to everyone\x01",
            "Shall I brush my arms?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At the very least \"classmaker\" class\x01",
            "If it does not, survival also\x01",
            "I can not do it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E10")

    label("loc_1D64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1DF9")

    ChrTalk(
        0xFE,
        (
            "Signboard of the fishing public division ……\x01",
            "To the original office again as anything\x01",
            "I have to raise it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this way, as our headmaster\x01",
            "I'm sorry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E10")

    label("loc_1DF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1E07")
    Jump("loc_1E10")

    label("loc_1E07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1E10")

    label("loc_1E10")

    TalkEnd(0xFE)
    Return()

    # Function_4_1346 end

    def Function_5_1E14(): pass

    label("Function_5_1E14")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1E25")
    Jump("loc_239F")

    label("loc_1E25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1F04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EA7")

    ChrTalk(
        0xFE,
        (
            "Fishing public division's\x01",
            "Lethal Weeponz …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have never met, though,\x01",
            "What kind of person are you ~.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EFF")

    label("loc_1EA7")


    ChrTalk(
        0xFE,
        (
            "Okay baby\x01",
            "I will not be defeated!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Someday,\x01",
            "Revenge for the crown club!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EFF")

    Jump("loc_239F")

    label("loc_1F04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1F12")
    Jump("loc_239F")

    label("loc_1F12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1F76")

    ChrTalk(
        0xFE,
        (
            "I am more ……\x01",
            "You should be able to do more!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is frustrating …\x01",
            "It's a really regrettable experience!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_239F")

    label("loc_1F76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1F84")
    Jump("loc_239F")

    label("loc_1F84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2008")

    ChrTalk(
        0xFE,
        (
            "Wow ~, why do I try any number of times\x01",
            "You can not win \"Ryugu\"!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What's up with me ……\x01",
            "What a bad thing! Is it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_239F")

    label("loc_2008")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_20E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2094")

    ChrTalk(
        0xFE,
        (
            "Even so,\x01",
            "The more you look, the more it is creepy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Besides it's okay … …\x01",
            "I want you to give me some more time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20DE")

    label("loc_2094")


    ChrTalk(
        0xFE,
        "Now, it's time to get back the late.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Aim for, \"Ryugu killer\" Ss!\x02",
    )

    CloseMessageWindow()

    label("loc_20DE")

    Jump("loc_239F")

    label("loc_20E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2219")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_219F")

    ChrTalk(
        0xFE,
        (
            "Wow, noble carve\x01",
            "Something I fished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is considerable in crossbell\x01",
            "Rare fish should not be … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, after all something\x01",
            "It's a funny feeling.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2214")

    label("loc_219F")


    ChrTalk(
        0xFE,
        (
            "Noble carve,\x01",
            "Compared to something before\x01",
            "I feel like the number has increased …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell's ecosystem\x01",
            "Is something happening?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2214")

    Jump("loc_239F")

    label("loc_2219")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2330")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22D4")

    ChrTalk(
        0xFE,
        "213, 214, 215 …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Before putting on food first today,\x01",
            "Rod's swing from 1000 times!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This special training, pretty\x01",
            "You may be able to train your strength!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_232B")

    label("loc_22D4")


    ChrTalk(
        0xFE,
        (
            "For those who neglect their efforts\x01",
            "Because the goddess does not smile ~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Fishermen just have to devote everyday!\x02",
    )

    CloseMessageWindow()

    label("loc_232B")

    Jump("loc_239F")

    label("loc_2330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2388")

    ChrTalk(
        0xFE,
        "Come on, fishery training begins immediately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Look now, the crown clubs!\x02",
    )

    CloseMessageWindow()
    Jump("loc_239F")

    label("loc_2388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2396")
    Jump("loc_239F")

    label("loc_2396")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_239F")

    label("loc_239F")

    TalkEnd(0xFE)
    Return()

    # Function_5_1E14 end

    def Function_6_23A3(): pass

    label("Function_6_23A3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_243A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23C1")
    Call(0, 7)
    Jump("loc_2435")

    label("loc_23C1")


    ChrTalk(
        0xB,
        (
            "Damn, even though I'm an enemy\x01",
            "Why is this so much\x01",
            "It's friendly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Do you recognize such a rare phenomenon!\x02",
    )

    CloseMessageWindow()

    label("loc_2435")

    Jump("loc_245F")

    label("loc_243A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2448")
    Jump("loc_245F")

    label("loc_2448")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_2456")
    Jump("loc_245F")

    label("loc_2456")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_245F")

    label("loc_245F")

    TalkEnd(0xFE)
    Return()

    # Function_6_23A3 end

    def Function_7_2463(): pass

    label("Function_7_2463")

    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xA,
        (
            "No way Lake Road,\x01",
            "Whoa, you are here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hun, if you can use here\x01",
            "I guess you said what you said.\x01",
            "… … I will not complain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Of course, that promise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "However, there are many inconveniences here.\x01",
            "You always came to the branch\x01",
            "Is not it good?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xB)

    ChrTalk(
        0xB,
        (
            "Fun …\x01",
            "We are so caring for you\x01",
            "I have not fallen.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xA, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_7_2463 end

    def Function_8_25E2(): pass

    label("Function_8_25E2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_267E")

    ChrTalk(
        0xC,
        (
            "Fuu … … I forgot it\x01",
            "In this hut there is a man named Seldan\x01",
            "You borrowed it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Two people's time …\x01",
            "I will forgive you!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26A3")

    label("loc_267E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_268C")
    Jump("loc_26A3")

    label("loc_268C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_269A")
    Jump("loc_26A3")

    label("loc_269A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_26A3")

    label("loc_26A3")

    TalkEnd(0xFE)
    Return()

    # Function_8_25E2 end

    def Function_9_26A7(): pass

    label("Function_9_26A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 4)), scpexpr(EXPR_END)), "loc_26D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 6)), scpexpr(EXPR_END)), "loc_26C1")
    Call(0, 20)
    Jump("loc_26CE")

    label("loc_26C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26CE")
    Call(0, 19)

    label("loc_26CE")

    Jump("loc_2754")

    label("loc_26D3")

    EventBegin(0x2)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Blue flowers are in bloom.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00000F(What a way, it's a beautiful flower.\x01",
            "It seems to be shining faintly ….)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x168, 4)
    EventEnd(0x3)

    label("loc_2754")

    Return()

    # Function_9_26A7 end

    def Function_10_2755(): pass

    label("Function_10_2755")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00003F(With this, both eidolids\x01",
            "I took it down … ….\x01",
            "I do not care about something. )\x02\x03",
            "#00000FEveryone, a little scene\x01",
            "Can I investigate it again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FCertainly, what I have to do here is\x01",
            "I think that it seems likely to be still.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FLet's go back and investigate quickly.\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 91500, 0, 0, 90)
    EventEnd(0x4)
    Return()

    # Function_10_2755 end

    def Function_11_286B(): pass

    label("Function_11_286B")

    EventBegin(0x1)
    Sound(2094, 255, 100, 0)

    ChrTalk(
        0x101,
        "#0000FI'm going to catch you here.\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_293A")
    OP_E2(0x2)
    MiniGame(0x6, 0x18, 0x73D2, 0x0, 0xD2, 0x5A, 0x933A, 0xFFFFFC18, 0x76C)

    label("loc_293A")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_11_286B end

    def Function_12_293F(): pass

    label("Function_12_293F")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked firmly.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_12_293F end

    def Function_13_2979(): pass

    label("Function_13_2979")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29AB")
    SetScenarioFlags(0x31, 2)

    label("loc_29AB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_29F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_29EB")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_29E0")
    Sound(2499, 255, 100, 0)
    Jump("loc_29E6")

    label("loc_29E0")

    Sound(3537, 255, 100, 0)

    label("loc_29E6")

    Jump("loc_29F1")

    label("loc_29EB")

    Sound(3344, 255, 100, 0)

    label("loc_29F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_2A6A")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Mercapa")
    MenuCmd(1, 0, "quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2A4A"),
        (SWITCH_DEFAULT, "loc_2A5B"),
    )


    label("loc_2A4A")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_2A65")

    label("loc_2A5B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2A65")

    Jump("loc_2CA9")

    label("loc_2A6A")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Travel with a driving car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_2A9E")
    MenuCmd(1, 0, "Take a break with a driving car")

    label("loc_2A9E")

    MenuCmd(1, 0, "quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2AD2"),
        (1, "loc_2BD6"),
        (2, "loc_2C67"),
        (SWITCH_DEFAULT, "loc_2C9F"),
    )


    label("loc_2AD2")

    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    OP_74(0x8, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B03")
    OP_70(0x8, 0x12C)
    OP_71(0x8, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_2B13")

    label("loc_2B03")

    OP_70(0x8, 0xF0)
    OP_71(0x8, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_2B13")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B69")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2B69")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B8C")
    Sound(461, 0, 100, 0)

    label("loc_2B8C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2BAC")
    OP_70(0x8, 0x14A)
    OP_71(0x8, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_2BBC")

    label("loc_2BAC")

    OP_70(0x8, 0x10E)
    OP_71(0x8, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_2BBC")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x8, "light", 0x1, 0x1)
    OP_70(0x8, 0x0)
    Jump("loc_29F1")

    label("loc_2BD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_2C48")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_2C0B")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_2C23")

    label("loc_2C0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2C1E")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_2C23")

    label("loc_2C1E")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_2C23")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C62")

    label("loc_2C48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2C58")
    OP_AF(0xFB)
    Jump("loc_2C62")

    label("loc_2C58")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C62")

    Jump("loc_2CA9")

    label("loc_2C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C80")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C9A")

    label("loc_2C80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2C90")
    OP_AF(0xFB)
    Jump("loc_2C9A")

    label("loc_2C90")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C9A")

    Jump("loc_2CA9")

    label("loc_2C9F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2CA9")

    Jump("loc_29F1")

    label("loc_2CAE")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_13_2979 end

    def Function_14_2CBC(): pass

    label("Function_14_2CBC")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_2D17")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2D0C")
    Sound(2502, 255, 100, 0)
    Jump("loc_2D12")

    label("loc_2D0C")

    Sound(2503, 255, 100, 0)

    label("loc_2D12")

    Jump("loc_2D3B")

    label("loc_2D17")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2D35")
    Sound(3347, 255, 100, 0)
    Jump("loc_2D3B")

    label("loc_2D35")

    Sound(3348, 255, 100, 0)

    label("loc_2D3B")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_14_2CBC end

    def Function_15_2D50(): pass

    label("Function_15_2D50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2D5A")
    Return()

    label("loc_2D5A")

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
            "Large monsters wandering around#4RIt is alright#doing.\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【Exterminate】\x01",      # 0
            "【quit】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_2E3C"),
        (SWITCH_DEFAULT, "loc_2E55"),
    )


    label("loc_2E3C")

    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, 106900, 0, 4400, 90)
    EventEnd(0x5)
    Return()

    label("loc_2E55")

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
        (2, "loc_2F17"),
        (1, "loc_2F1C"),
        (SWITCH_DEFAULT, "loc_2F1F"),
    )


    label("loc_2F17")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    label("loc_2F1C")

    OP_B9(0x0)
    Return()

    label("loc_2F1F")

    Call(0, 18)
    Return()

    # Function_15_2D50 end

    def Function_16_2F23(): pass

    label("Function_16_2F23")

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

    def lambda_300F():
        OP_9B(0x0, 0x101, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_300F)
    Sleep(0)

    def lambda_3027():
        OP_9B(0x0, 0x102, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3027)
    Sleep(0)

    def lambda_303F():
        OP_9B(0x0, 0x103, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_303F)
    Sleep(0)

    def lambda_3057():
        OP_9B(0x0, 0x104, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3057)
    Sleep(0)

    def lambda_306F():
        OP_9B(0x0, 0x109, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_306F)
    Sleep(0)

    def lambda_3087():
        OP_9B(0x0, 0x105, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3087)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31A0")

    ChrTalk(
        0x109,
        "#10111F#6P(Ah……!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#5P(Is that a \"phantom beast\" …?!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_31DE")

    label("loc_31A0")


    ChrTalk(
        0x105,
        "#10305F#6P(Oops ……)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#5P(Is there……!)\x02",
    )

    CloseMessageWindow()

    label("loc_31DE")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34EC")

    ChrTalk(
        0x104,
        (
            "#00303F#9P(As reported, it's pretty decent …).\x02\x03",
            "#00301F(Thio, how is distortion in the field?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#9P(Hour · sky · vision … …\x01",
            "We confirmed the expression of the top three attributes. )\x02\x03",
            "#00201F(The cause is unknown for now.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#9P(so……)\x02",
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

    def lambda_33A3():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_33A3)
    Sleep(0)

    def lambda_33B3():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_33B3)
    Sleep(0)

    def lambda_33C3():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_33C3)
    Sleep(0)

    def lambda_33D3():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_33D3)
    Sleep(0)

    def lambda_33E3():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_33E3)
    Sleep(0)

    def lambda_33F3():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_33F3)
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
            "#10301F#6P(So ….\x01",
            "What will you do after all? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11P(In the report of the guard\x01",
            "It looks like a pretty dangerous type … …)\x02\x03",
            "#00013F(If you want to get rid of it, leave it carefully.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#12P(OK……!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_3685")

    label("loc_34EC")


    ChrTalk(
        0x102,
        (
            "#00101F#9P(Tio-chan ……\x01",
            "How is the distortion of the place? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#9P(Also confirm the expression of the top three attributes … …)\x02\x03",
            "#00201F(Again the cause is unknown.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#9P(After all ……)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10308F#9P(Apparently the phantom beast itself\x01",
            "It seems not to be the cause … …)\x02",
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
            "#10101F#6P(Mr. Lloyd ……\x01",
            "Can you get on the set? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#5P(Oh, let's go carefully … …!)\x02",
    )

    CloseMessageWindow()

    label("loc_3685")

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

    # Function_16_2F23 end

    def Function_17_36C0(): pass

    label("Function_17_36C0")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A73")
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
    Jump("loc_3A8D")

    label("loc_3A73")

    OP_75(0x6, 0x2, 0x0)
    OP_75(0x7, 0x2, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    label("loc_3A8D")

    Battle("BattleInfo_4EC", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetScenarioFlags(0x168, 1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B21")
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
    Jump("loc_3B24")

    label("loc_3B21")

    Call(0, 18)

    label("loc_3B24")

    Return()

    # Function_17_36C0 end

    def Function_18_3B25(): pass

    label("Function_18_3B25")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EF5")

    ChrTalk(
        0x101,
        (
            "#00006F#5PDamn\x01",
            "It was truly tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6PAfter all …\x01",
            "I did a mysterious disappearance.\x02",
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

    def lambda_3D50():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3D50)
    Sleep(50)

    def lambda_3D60():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3D60)
    Sleep(50)

    def lambda_3D70():
        TurnDirection(0x103, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3D70)
    Sleep(50)

    def lambda_3D80():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3D80)
    Sleep(50)

    def lambda_3D90():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3D90)
    Sleep(50)

    def lambda_3DA0():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3DA0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x109,
        (
            "#10108F#12PTio-chan.\x01",
            "Who is the \"distortion of the place\"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6P……No good.\x01",
            "The top three attributes are still working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#5PGeez……\x01",
            "What is the cause?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#11PApparently \"The eidolome\" itself\x01",
            "It seems not to be the cause … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00013F#11P…… After all the other\x01",
            "It seems necessary to try it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_430C")

    label("loc_3EF5")


    ChrTalk(
        0x105,
        (
            "#10306F#6PWhew ……\x01",
            "This person was also tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#6PHowever, the way of disappearing is the same …\x02",
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

    def lambda_3F99():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3F99)
    Sleep(50)

    def lambda_3FA9():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3FA9)
    Sleep(50)

    def lambda_3FB9():
        TurnDirection(0x103, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3FB9)
    Sleep(50)

    def lambda_3FC9():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3FC9)
    Sleep(50)

    def lambda_3FD9():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3FD9)
    Sleep(50)

    def lambda_3FE9():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3FE9)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x104,
        (
            "#00301F#5PAfter all the \"distortion of the place\" is\x01",
            "Would you keep on continuing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#6PI agree……\x02\x03",
            "#00201FHowever, something specific cause\x01",
            "I feel like it is likely.\x02",
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
            "#00005F#11PSpecific cause …\x01",
            "For example?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6P……That……\x01",
            "My feelings from the previous time\x01",
            "Distorted by \"distortion\" … …\x02\x03",
            "#00200FRather, you are the cause\x01",
            "It may be found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#5PIs that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11PAlright ……\x01",
            "Let's search around this area.\x02\x03",
            "#00000FWhat is bringing \"distortion of the place\"\x01",
            "There must be sure.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_424C():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_424C)
    Sleep(50)

    def lambda_425C():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_425C)
    Sleep(50)

    def lambda_426C():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_426C)
    Sleep(50)

    def lambda_427C():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_427C)
    Sleep(50)

    def lambda_428C():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_428C)
    Sleep(50)

    def lambda_429C():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_429C)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x109,
        "#10100F#6POK!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300F#5PRandomly, looking for Mika!\x02",
    )

    CloseMessageWindow()
    OP_29(0xA6, 0x1, 0x3)

    label("loc_430C")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Defeated the eidolobes in the direction of the East Crossbell Highway!\x07\x00\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43A0")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_43A0")

    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_37()
    EventEnd(0x5)
    Return()

    # Function_18_3B25 end

    def Function_19_43B0(): pass

    label("Function_19_43B0")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4791")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(300)

    AnonymousTalk(
        0x101,
        "#00005FThis flower ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 3)), scpexpr(EXPR_END)), "loc_45BF")

    AnonymousTalk(
        0x102,
        (
            "#00108FIndeed, in the Ursula intermittent direction\x01",
            "It seems like it was blooming on the banks …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        "#00305FOh, I saw that.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4663")

    label("loc_45BF")


    AnonymousTalk(
        0x105,
        (
            "#10302FIndeed, in the Ursula intermittent direction\x01",
            "Did not it bloom even on the bank?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#00011FWas that right?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00108FYeah, surely me too\x01",
            "I feel like I saw it ….\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4663")


    AnonymousTalk(
        0x109,
        (
            "#10109FIt is a very beautiful flower …\x02\x03",
            "#10102F…… I have never seen it before, but\x01",
            "What is his name?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#00001FWell …\x02",
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
            "#00003F#11P(… … I do not care about it … …)\x02\x03",
            "#00001F(No, is it worth a try?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x161, 2)
    OP_29(0xA6, 0x1, 0x4)
    Jump("loc_4847")

    label("loc_4791")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(300)

    AnonymousTalk(
        0x101,
        (
            "#00003F#11P(… … I do not care about it … …)\x02\x03",
            "#00001F(No, is it worth a try?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    label("loc_4847")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Pick a blue flower\x01",      # 0
            "To stop\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_489F"),
        (1, "loc_5644"),
        (SWITCH_DEFAULT, "loc_5683"),
    )


    label("loc_489F")

    OP_9B(0x0, 0x101, 0x0, 0x2EE, 0x3E8, 0x0)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_0D()

    ChrTalk(
        0x102,
        "#00105FLloyd …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F#6PWhat, that flower\x01",
            "Are you going to pick it up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11PAh……\x01",
            "It's a bit sad but ──\x02",
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
        "#00301F#5PWhat! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#12Pthis is……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#11PCut …!\x02",
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
        "#00013F#11P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10111F#5PWell, now ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108FSomething like a space shaking …\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x103, 500)

    ChrTalk(
        0x105,
        (
            "#10308F#6P…… Tio.\x01",
            "Who is the \"distortion of the place\"?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)

    ChrTalk(
        0x103,
        (
            "#00203F#12P…… Top three attributes\x01",
            "The sign has disappeared.\x02\x03",
            "#00201FAlready this part\x01",
            "I can not feel any abnormality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#11PReally……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#5PWait a moment.\x02\x03",
            "#00307FNo doubt that the blue flower\x01",
            "I wonder what caused the abnormality! Is it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    ChrTalk(
        0x105,
        (
            "#10304F#6PWell, that's probably not.\x02\x03",
            "#10300F…… to that small size flower\x01",
            "I do not think there is such power.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101FAnd I can not believe it … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#5PAll\x01",
            "What kind of flower is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#12P…… Already from that flower\x01",
            "I do not feel a funny sign … …\x02\x03",
            "#00200FTentatively somewhere\x01",
            "Who should I check?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#11PThat's right.\x02\x03",
            "#00003F…… Also around medical school\x01",
            "The specialty will be slightly different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FAnd, do not lose it anyway\x01",
            "Let's keep it.\x02\x03",
            "If you find something\x01",
            "Why do not you check it out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#11POh, would you?\x02",
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
        "#10303F#6P……HM………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_5025():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5025)
    Sleep(50)

    def lambda_5035():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5035)
    Sleep(50)

    def lambda_5045():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5045)
    Sleep(50)

    def lambda_5055():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5055)
    Sleep(50)

    def lambda_5065():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5065)
    Sleep(50)

    def lambda_5075():
        TurnDirection(0x105, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5075)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#11PWasi …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#5PIs there something in mind too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#6PDisagreeable……\x01",
            "I may remember my uro, though.\x02\x03",
            "#10301FIn the church's scriptures, a mysterious blue flower\x01",
            "I feel like there was a legend.\x02",
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
        "#00011F#11Peh……! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F#5PHey hey, are you serious! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#6PNo, when I did shedding before Oita\x01",
            "I feel like I saw him ……\x02\x03",
            "#10300FIs not there such as Ely?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00112F#11PTo me as well as to all of the scriptures\x01",
            "I can not see my eyes … ….\x02\x03",
            "#00103F… but it certainly is\x01",
            "I feel like I read such a descent.\x02\x03",
            "#00108FHe says he has a magical power\x01",
            "The legend of 'Aoi Hana' ……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)

    ChrTalk(
        0x109,
        (
            "#10111F#6PWell, that is ….\x01",
            "Is not it a bingo?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#00201F#12PTo at least church officials\x01",
            "It is likely to be worth checking.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_53D6():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_53D6)
    Sleep(50)

    def lambda_53E6():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_53E6)
    Sleep(50)

    def lambda_53F6():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_53F6)
    Sleep(50)

    def lambda_5406():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5406)
    Sleep(50)

    def lambda_5416():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5416)
    Sleep(50)

    def lambda_5426():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5426)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_54E4")

    ChrTalk(
        0x101,
        (
            "#00003F#11P… … That's right.\x02\x03",
            "#00000FDr. Marble or Lease's\x01",
            "Would you like to consult with either one?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FI see …\x01",
            "I think both are qualified.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5593")

    label("loc_54E4")


    ChrTalk(
        0x101,
        (
            "#00003F#11P… … That's right.\x02\x03",
            "#00000FAfter all the marble teacher\x01",
            "It may be easiest to consult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FYeah, I think that's qualified.\x02\x03",
            "#00108F(It seems to be able to talk to \"her\" though …).\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5593")


    ChrTalk(
        0x104,
        (
            "#00300F#5PHaha, that's right.\x01",
            "Will you head for Crossbell Cathedral!\x02",
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
    AddItemNumber('蓝花', 1)
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
    Jump("loc_5683")

    label("loc_5644")

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
    Jump("loc_5683")

    label("loc_5683")

    Return()

    # Function_19_43B0 end

    def Function_20_5684(): pass

    label("Function_20_5684")

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
            "#10100FThat's right. …\x02\x03",
            "This flower too\x01",
            "Should I pick it up?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00000FDisagreeable……\x01",
            "Let's see how this person is.\x02\x03",
            "Possibly precious\x01",
            "It may be a sample.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        (
            "#00200F……surely.\x01",
            "I seem to lose power when I pick it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00100FBut … … If a phantom beast appears again\x01",
            "You may have to pick it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        "#00300FWell, that time is right.\x02",
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

    # Function_20_5684 end

    def Function_21_5975(): pass

    label("Function_21_5975")

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
            "Well, but\x01",
            "It is a creepy monster that is creepy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6POh, if those of you come over here\x01",
            "There is no one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Oh, when that happens\x01",
            "I have to evacuate by haste.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But for now\x01",
            "Wait for the guard to come ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        "Oh, you … … Lloyd members!\x02",
    )

    CloseMessageWindow()
    OP_68(37180, 1400, -14790, 4000)
    MoveCamera(33, 33, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(14430, 4000)

    def lambda_5B21():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5B21)

    def lambda_5B2E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5B2E)
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

    def lambda_5BBC():
        OP_95(0xFE, 36720, 0, -14030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5BBC)
    Sleep(300)

    def lambda_5BD9():
        OP_95(0xFE, 36720, 0, -15170, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5BD9)
    Sleep(300)

    def lambda_5BF6():
        OP_95(0xFE, 35680, 0, -13860, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5BF6)
    Sleep(300)

    def lambda_5C13():
        OP_95(0xFE, 35680, 0, -15050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5C13)
    Sleep(300)

    def lambda_5C30():
        OP_95(0xFE, 34560, 0, -13930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5C30)
    Sleep(300)

    def lambda_5C4D():
        OP_95(0xFE, 34700, 0, -14930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5C4D)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)

    ChrTalk(
        0x101,
        (
            "#6P#00003FLong time no see, Serdan branch chief.\x02\x03",
            "#00001FA large magical beast that is magical to this person,\x01",
            "I heard that \"Phantom Beast\" appeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "\"Phantom beast\" ……\x01",
            "Hmm, it's a strange expression to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Oh, in fact that 's phantom beast'\x01",
            "Yesterday evening, suddenly appeared in the back of the marshes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We and the people to the guard\x01",
            "I had you contact me ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PPerhaps,\x01",
            "Lloyd Kimita Special Support Division\x01",
            "Did you come to cope?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FYes, receiving a request from the guard.\x02\x03",
            "#00101FDetailed situation\x01",
            "Can you tell me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Oh, as I said earlier\x01",
            "First I confirmed\x01",
            "It was about yesterday evening …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "There was no warning in truth,\x01",
            "Suddenly something like a strange cry\x01",
            "You did not hear it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PTo the far side of the marshes that had been blocked for a long time\x01",
            "Doubtful shadow flickered ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12PEveryone, I approached carefully.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThen, that mysterious\x01",
            "You found a guy with \"Phantom beast\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PSo, in a panic and into the guard\x01",
            "I got it reported.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We tried to escape soon\x01",
            "I thought … … \"Phantom beast\"\x01",
            "I do not have a sign of moving from the spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Anyway, I switched from yesterday\x01",
            "I was watching the situation looking up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00203F… … It was a hard work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FWhile watching, something\x01",
            "Did you have anything unusual?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "No, that is also\x01",
            "There is nothing extravagant to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I was hostile while wounds close\x01",
            "I feel something like a will … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PWhat kind of … ….\x01",
            "I do not move, I can not move\x01",
            "It looks like a touch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PFor further information\x01",
            "I do not understand well but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303FI see, suddenly it appears\x01",
            "I will not leave the place further ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FSome kind, obviously\x01",
            "What is \"distortion of the place\"\x01",
            "It seems to be related.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FOh, it is no doubt.\x02\x03",
            "#00013FWell then, Serdan chief.\x01",
            "I want to go back to this place immediately …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Oh, you guys\x01",
            "It was going to get rid of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Let's open the key now.\x02",
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
            "Now, this is fine.\x01",
            "I asked for your kindness afterwards.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYes, I understand.\x02",
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

    # Function_21_5975 end

    def Function_22_641D(): pass

    label("Function_22_641D")

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
            "#6POh, Lloyd Members.\x01",
            "Have you been able to get rid of \"Phantom Beast\"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PYeah, somehow.\x02\x03",
            "#00000FI think that attention is necessary,\x01",
            "Perhaps it will reappear for a while\x01",
            "I do not think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PMagis?\x01",
            "That was good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PHuhu, this for fishing again\x01",
            "You can concentrate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#6POh, I was really saved.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_695D")

    ChrTalk(
        0x8,
        "#6POh yeah, then Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PWhat is to say thank you,\x01",
            "Will you accept this?\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '钢竿侵略者'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('钢竿侵略者', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00005F#11PIs this … … a new fishing rod?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PYes, for vs. the Ace of club\x01",
            "It is a rod I built up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PWith this, larger fish\x01",
            "You should be able to fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#11PPeter said this … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PHaha, this looks like Peter\x01",
            "I am good at tooling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PSometimes like this,\x01",
            "Or remodeling ready-made items\x01",
            "I will make new fishing gear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PTo this, the skill of fishing with this\x01",
            "Because it is clear,\x01",
            "What a mysterious story!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PThere, Copan.\x01",
            "Do not say unnecessary things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11PHaha ……\x02\x03",
            "#00000FBut indeed, such a good thing\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F91")

    label("loc_695D")


    ChrTalk(
        0xA,
        "#6PYes, members of Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PI did not tell you,\x01",
            "\"Bombing with the Emperor 's Club#4REmbankment#About the game\x01",
            "I would like to explain … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#11PWell, \"Bomb victory\" is … ….?\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00003F#11PIndeed, the crown club's\x01",
            "\"Members of the bombing fight\" with five members … …\x02\x03",
            "If you win the freedom of the office and the fishing spot\x01",
            "I can regain it … ….\x02\x03",
            "#00001FIf you lose, do not you say the other party?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#6POh, that's it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PWell, I tentatively\x01",
            "The way of winning is ours\x01",
            "I'm going to do something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PMembers of Lloyd are the main business\x01",
            "Because I will be busy,\x01",
            "You do not mind if you care about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#11PYes, I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#6POh yeah, then Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PWhat is to say thank you,\x01",
            "Will you accept this?\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '钢竿侵略者'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('钢竿侵略者', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00005F#11PIs this … … a new fishing rod?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PYes, for vs. the Ace of club\x01",
            "It is a rod I built up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PWith this, larger fish\x01",
            "You should be able to fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#11PPeter said this … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PHaha, this looks like Peter\x01",
            "I am good at tooling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#6PSometimes like this,\x01",
            "Or remodeling ready-made items\x01",
            "I will make new fishing gear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PTo this, the skill of fishing with this\x01",
            "Because it is clear,\x01",
            "What a mysterious story!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PThere, Copan.\x01",
            "Do not say unnecessary things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11PHaha ……\x02\x03",
            "#00000FBut indeed, such a good thing\x01",
            "Thank you very much.\x02",
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
            "To the members of the Emperor 's Club,\x01",
            "I began to challenge \"bomb victory\".\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Detailed information on the game is,\x01",
            "I am in 'The Emperor' s Club at East Street '\x01",
            "You can hear from the receptionist Sailram.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1C0, 0)

    label("loc_6F91")

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

    # Function_22_641D end

    def Function_23_6FF8(): pass

    label("Function_23_6FF8")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 1)), scpexpr(EXPR_END)), "loc_7163")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 500)

    ChrTalk(
        0x8,
        (
            "Lloyd, finally\x01",
            "I got all the parts!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FYeah, I managed to collect it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, immediately\x01",
            "Let's build up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7497")

    label("loc_7163")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 500)

    ChrTalk(
        0x8,
        "Lloyd, that is … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah, definitely fishing tackle\x01",
            "I think it is a part,\x01",
            "It is very beautiful, is not it?\x02\x03",
            "#00000FAt the fishing spot recovered from the four heavenly kings\x01",
            "I caught an unusual fish ….\x01",
            "That fish spit out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "……There is no mistake.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It was once a great fighter of travel\x01",
            "It is a part of the legendary fishing gear that I was using.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When he leaves the crossbell,\x01",
            "It was sealed in this place\x01",
            "I was listening … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No way,\x01",
            "What you can find out like this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FWell, so much\x01",
            "Was it amazing ……\x02\x03",
            "#00003FBut what shall I do.\x01",
            "If you return to that person … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "No, that is not necessary.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "… … because he said.\x01",
            "The fishing tackle can be used by those who found it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And, there are 4 parts in all … …\x01",
            "Is not it already complete?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Let's build up at once.\x01",
            "Is that good, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FYes.\x02",
    )

    CloseMessageWindow()

    label("loc_7497")

    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "Oh, it's beautiful.\x01",
            "This is a legend …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FSurely …\x01",
            "It is terribly beautiful and cool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, then, Lloyd.\x01",
            "Please receive firmly.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '水中支配者'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('水中支配者', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SubItemNumber('绀碧竿', 1)
    SubItemNumber('琥珀轴', 1)
    SubItemNumber('翡翠线', 1)
    SubItemNumber('红莲钩', 1)

    ChrTalk(
        0x101,
        "#00005FO, can I use it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uhufu, what are you saying?\x01",
            "It is natural that Lloyd found it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Apparently, Lloyd's\x01",
            "Fishing Jie Four Shitenno kings all seemed to be defeated … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Shake that rod altogether\x01",
            "Please defeat the remaining Lake Road!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FIs that … Yes, I understand!\x02",
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

    # Function_23_6FF8 end

    def Function_24_7706(): pass

    label("Function_24_7706")

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
            "Members of Lloyd ……\x01",
            "No, \"Emperor Slayer\" Master Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Thank you so much for this time.\x01",
            "I can not thank you enough for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Seriously, Mr. Lloyd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hmm, the fishing public division · crossbell branch\x01",
            "What was protected by the hands of young people\x01",
            "It is truly delightfully proud.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ufufu, this time the battle for bombing,\x01",
            "You will be handed down until the last days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FWell, that's exaggeration.\x02",
    )

    CloseMessageWindow()
    OP_68(2190, 1200, -8070, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        "#00102F(Well, I guess it will be greatly praised.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103F(I'm not sure why ….\x01",
            "It is exactly like a hero. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F(\"Emperor Slayer\" ……\x01",
            "It may be a little cool. )\x02",
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

    # Function_24_7706 end

    SaveToFile()

Try(main)
