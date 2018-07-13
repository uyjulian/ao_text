from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m0309.bin",                # FileName
        "m0309",                    # MapName
        "m0309",                    # Location
        0x00A8,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 168, 0, 0, 0, 1],
    )

    BuildStringList((
        "m0309",                  # 0
        "新型装甲車",             # 1
        "Terrorist Leader",       # 2
        "Terrorist",              # 3
        "Terrorist",              # 4
        "Terrorist",              # 5
        "Terrorist",              # 6
        "Terrorist",              # 7
        "Terrorist",              # 8
        "Terrorist",              # 9
        "Ogre Sigmund",           # 10
        "Shirley",                # 11
        "Jaeger Gareth",          # 12
        "新型装甲車",             # 13
        "通信機",                 # 14
        "イベント用モンスター",   # 15
        "イベント用モンスター",   # 16
        "イベント用モンスター",   # 17
        "イベント用モンスター",   # 18
        "Jaeger",                 # 19
        "Jaeger",                 # 20
        "Jaeger",                 # 21
        "Jaeger",                 # 22
        "Jaeger",                 # 23
        "ダミー影",               # 24
        "SE制御",                 # 25
        "bm0320",                 # 26
        "bm0320",                 # 27
        "bm0320",                 # 28
    ))

    ATBonus("ATBonus_4D8", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)
    ATBonus("ATBonus_4B8", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_4F8", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_4FC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_500", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_504", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_508", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_50C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_510", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_514", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_578", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_57C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_580", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_584", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_588", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_58C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_590", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_594", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_598", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_59C", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A0", 11, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A4", 6, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A8", 2, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_5AC", 10, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_5B0", 14, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_5B4", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_5B8", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5BC", 2, 8, 135)
    MonsterBattlePostion("MonsterBattlePostion_5C0", 4, 10, 135)
    MonsterBattlePostion("MonsterBattlePostion_5C4", 0, 9, 135)
    MonsterBattlePostion("MonsterBattlePostion_5C8", 2, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_5CC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_5D0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_5D4", 0, 0, 180)

    # monster count: 1

    BattleInfo(
        "BattleInfo_660", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "bm0320", 0x00000000, 100, 0, 0, 0,
        (
            ("ms66100.dat", "ms66100.dat", "ms66100.dat", "ms66100.dat", "ms66100.dat", "ms66100.dat", 0, 0, "MonsterBattlePostion_4F8", "MonsterBattlePostion_578", "ed7451", "ed7453", "ATBonus_4D8"),
            (),
            (),
            (),
        )
    )

    # event battle count: 3

    BattleInfo(
        "BattleInfo_5D8", 0x0042, 3, 6, 45, 3, 3, 30, 0, "bm0320", 0x00000000, 100, 0, 0, 0,
        (
            ("ms42200.dat", "ms42200.dat", "ms42200.dat", "ms42300.dat", "ms42300.dat", "ms42300.dat", "ms42300.dat", "ms42200.dat", "MonsterBattlePostion_598", "MonsterBattlePostion_578", "ed7452", "ed7453", "ATBonus_4B8"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_61C", 0x0052, 3, 6, 45, 3, 3, 30, 0, "bm0320", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88600.dat", "ms84100.dat", "ms84100.dat", "ms84300.dat", "ms84300.dat", 0, "ms84300.dat", 0, "MonsterBattlePostion_5B8", "MonsterBattlePostion_578", "ed7586", "ed7453", "ATBonus_4B8"),
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
        "monster/ch66150.itc",               # 10
        "monster/ch66150.itc",               # 11
    ))

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
    DeclNpc(0,       0,       0,       0,    503,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(0,       0,       750,     0x185005A,    "BattleInfo_660", 0,   16,  0xFFFF, 0,  1)

    DeclEvent(0x0040, 0, 54,  0.0,                   0.0,                   -1.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -0.0,                  -0.0,                  0.25,                  1.0])

    DeclActor(5800,    50,      398500,  1200,    5800,    1050,    398500,  0x007C, 0,  3,  0x0000)
    DeclActor(4294671796, 0,       500,     1200,    4294671796, 1000,    500,     0x007C, 0,  5,  0x0000)
    DeclActor(301800,  0,       19500,   1200,    301800,  1000,    19500,   0x007C, 0,  7,  0x0000)
    DeclActor(4294832796, 0,       3000,    1200,    4294832796, 1500,    3000,    0x007C, 0,  2,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 1

    ScpFunction((
        "Function_0_79C",          # 00, 0
        "Function_1_83C",          # 01, 1
        "Function_2_B2A",          # 02, 2
        "Function_3_C20",          # 03, 3
        "Function_4_D8C",          # 04, 4
        "Function_5_E9B",          # 05, 5
        "Function_6_1007",         # 06, 6
        "Function_7_1116",         # 07, 7
        "Function_8_1270",         # 08, 8
        "Function_9_137F",         # 09, 9
        "Function_10_26C8",        # 0A, 10
        "Function_11_2713",        # 0B, 11
        "Function_12_274D",        # 0C, 12
        "Function_13_277B",        # 0D, 13
        "Function_14_27AF",        # 0E, 14
        "Function_15_27DD",        # 0F, 15
        "Function_16_2811",        # 10, 16
        "Function_17_283F",        # 11, 17
        "Function_18_2879",        # 12, 18
        "Function_19_28A7",        # 13, 19
        "Function_20_28B7",        # 14, 20
        "Function_21_38E4",        # 15, 21
        "Function_22_3917",        # 16, 22
        "Function_23_3956",        # 17, 23
        "Function_24_3995",        # 18, 24
        "Function_25_39C4",        # 19, 25
        "Function_26_39F3",        # 1A, 26
        "Function_27_3A35",        # 1B, 27
        "Function_28_3A77",        # 1C, 28
        "Function_29_3AAD",        # 1D, 29
        "Function_30_3B02",        # 1E, 30
        "Function_31_3B57",        # 1F, 31
        "Function_32_3BAC",        # 20, 32
        "Function_33_3C04",        # 21, 33
        "Function_34_3C4C",        # 22, 34
        "Function_35_3C94",        # 23, 35
        "Function_36_3CDC",        # 24, 36
        "Function_37_3D24",        # 25, 37
        "Function_38_3D6C",        # 26, 38
        "Function_39_3DBA",        # 27, 39
        "Function_40_4504",        # 28, 40
        "Function_41_6915",        # 29, 41
        "Function_42_6FE2",        # 2A, 42
        "Function_43_7391",        # 2B, 43
        "Function_44_754D",        # 2C, 44
        "Function_45_757B",        # 2D, 45
        "Function_46_75A8",        # 2E, 46
        "Function_47_75CE",        # 2F, 47
        "Function_48_7612",        # 30, 48
        "Function_49_7664",        # 31, 49
        "Function_50_76A8",        # 32, 50
        "Function_51_76FA",        # 33, 51
        "Function_52_773E",        # 34, 52
        "Function_53_775D",        # 35, 53
        "Function_54_7784",        # 36, 54
        "Function_55_7C12",        # 37, 55
    ))


    def Function_0_79C(): pass

    label("Function_0_79C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B6")
    Event(0, 9)

    label("loc_7B6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D0")
    Event(0, 40)

    label("loc_7D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_7E7")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 20)
    Jump("loc_7F6")

    label("loc_7E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_7F6")
    ClearScenarioFlags(0x22, 1)
    Event(0, 39)

    label("loc_7F6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80D")
    Event(0, 4)

    label("loc_80D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_824")
    Event(0, 6)

    label("loc_824")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83B")
    Event(0, 8)

    label("loc_83B")

    Return()

    # Function_0_79C end

    def Function_1_83C(): pass

    label("Function_1_83C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_868")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_863")
    ClearChrFlags(0x21, 0x80)
    ModifyEventFlags(1, 0, 0x80)
    SetChrFlags(0x21, 0x8000)

    label("loc_863")

    Jump("loc_872")

    label("loc_868")

    SetChrFlags(0x21, 0x80)
    ModifyEventFlags(0, 0, 0x80)

    label("loc_872")

    OP_52(0x21, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrBattleFlags(0x21, 0x100)
    OP_52(0x21, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_10(0x0, 0x0)
    OP_10(0x7, 0x0)
    OP_10(0x8, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D4")
    SetMapObjFrame(0x3, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x3, "Null_color2", 0x1, 0x1)
    Jump("loc_8F9")

    label("loc_8D4")

    SetMapObjFrame(0x3, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x3, "Null_color2", 0x0, 0x1)

    label("loc_8F9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_937")
    SetMapObjFrame(0x4, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x4, "Null_color2", 0x1, 0x1)
    Jump("loc_95C")

    label("loc_937")

    SetMapObjFrame(0x4, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x4, "Null_color2", 0x0, 0x1)

    label("loc_95C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_99A")
    SetMapObjFrame(0x5, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x5, "Null_color2", 0x0, 0x1)
    Jump("loc_9BF")

    label("loc_99A")

    SetMapObjFrame(0x5, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x5, "Null_color2", 0x1, 0x1)

    label("loc_9BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A17")
    SetMapObjFrame(0x3, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x3, "Null_color2", 0x0, 0x1)
    SetMapObjFrame(0x4, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x4, "Null_color2", 0x0, 0x1)

    label("loc_A17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A7C")
    ClearMapObjFlags(0x9, 0x4)
    OP_78(0x9, 0x8)
    SetMapObjFlags(0x9, 0x1000)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 2000, 0, 1000, 180)
    OP_D5(0x8, 0x0, 0x222E0, 0x0, 0x0)
    OP_74(0x9, 0x1E)
    OP_71(0x9, 0x79, 0xF0, 0x0, 0x20)
    SetMapObjFrame(0x9, "mark00", 0x1, 0x1)

    label("loc_A7C")

    SetMapObjFlags(0x8, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_AD6")
    LoadEffect(0x9, "event\\ev12003.eff")
    PlayEffect(0x9, 0xFF, 0xFF, 0x0, 169200, 0, 13900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_AD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B29")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B0C")
    Sound(863, 1, 50, 0)
    Sound(864, 1, 50, 0)
    Jump("loc_B29")

    label("loc_B0C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B29")
    OP_24(0x35F)
    OP_24(0x360)

    label("loc_B29")

    Return()

    # Function_1_83C end

    def Function_2_B2A(): pass

    label("Function_2_B2A")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is an orbment charging station.\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest Here\x01",      # 0
            "Quit\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C11")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x7, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x7, 0x0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x7)
    OP_71(0x7, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0x7, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_C11")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_2_B2A end

    def Function_3_C20(): pass

    label("Function_3_C20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C32")
    Call(0, 55)
    Return()

    label("loc_C32")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)
    SoundLoad(150)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a lift control panel.\x01",
            "Operate it?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D84")
    Fade(500)
    SetChrPos(0x0, 5200, 50, 397000, 0)
    SetChrPos(0x1, 6200, 50, 397000, 0)
    SetChrPos(0x2, 5200, 50, 396000, 0)
    SetChrPos(0x3, 6200, 50, 396000, 0)
    OP_68(5200, 1550, 392980, 0)
    MoveCamera(24, 45, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_71(0x3, 0xA, 0xC8, 0x0, 0x0)
    Sleep(200)
    OP_68(6000, 2000, 410000, 3800)
    MoveCamera(22, 49, 0, 3800)
    Sleep(1800)
    Sound(150, 2, 100, 0)
    Sleep(200)
    FadeToDark(500, 0, -1)
    Sleep(4000)
    StopSound(150, 1000, 100)
    Sleep(1000)
    OP_0D()
    NewScene("m0300", 101, 0, 0)
    IdleLoop()

    label("loc_D84")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_3_C20 end

    def Function_4_D8C(): pass

    label("Function_4_D8C")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_70(0x3, 0x64)
    Sleep(1)
    OP_68(4710, 4300, 403470, 0)
    MoveCamera(23, 36, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_90(0x0, 3500, 2800, 409000, 270)
    OP_90(0x1, 3500, 2800, 408000, 270)
    OP_90(0x2, 4500, 2800, 409000, 270)
    OP_90(0x3, 4500, 2800, 408000, 270)
    Sound(145, 0, 100, 0)
    OP_68(4830, 50, 394970, 3200)
    MoveCamera(45, 44, 0, 3200)
    OP_71(0x3, 0x64, 0xA, 0x0, 0x0)
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x3)
    OP_6F(0x1)
    Sleep(500)
    SetMapObjFrame(0x3, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x3, "Null_color2", 0x0, 0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_4_D8C end

    def Function_5_E9B(): pass

    label("Function_5_E9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EAD")
    Call(0, 55)
    Return()

    label("loc_EAD")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)
    SoundLoad(150)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a lift control panel.\x01",
            "Operate it?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FFF")
    Fade(500)
    SetChrPos(0x0, -296500, 0, 0, 90)
    SetChrPos(0x1, -296500, 0, 1000, 90)
    SetChrPos(0x2, -297500, 0, 0, 90)
    SetChrPos(0x3, -297500, 0, 1000, 90)
    OP_68(-300940, 1500, 840, 0)
    MoveCamera(58, 54, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_71(0x4, 0xA, 0xC8, 0x0, 0x0)
    Sleep(200)
    OP_68(-282200, 3500, 820, 3200)
    MoveCamera(50, 20, 0, 3200)
    Sleep(1800)
    Sound(150, 2, 100, 0)
    Sleep(200)
    FadeToDark(500, 0, -1)
    Sleep(4000)
    StopSound(150, 1000, 100)
    Sleep(1000)
    OP_0D()
    NewScene("m0301", 121, 0, 0)
    IdleLoop()

    label("loc_FFF")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_5_E9B end

    def Function_6_1007(): pass

    label("Function_6_1007")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_70(0x4, 0x64)
    Sleep(1)
    OP_68(-287810, 4250, 240, 0)
    MoveCamera(70, 33, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_90(0x0, -285000, 2750, -1500, 180)
    OP_90(0x1, -286000, 2750, -1500, 180)
    OP_90(0x2, -285000, 2750, -500, 180)
    OP_90(0x3, -286000, 2750, -500, 180)
    Sound(145, 0, 100, 0)
    OP_68(-299340, 1500, -3660, 3200)
    MoveCamera(32, 46, 0, 3200)
    OP_71(0x4, 0x64, 0xA, 0x0, 0x0)
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x4)
    OP_6F(0x1)
    Sleep(500)
    SetMapObjFrame(0x4, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x4, "Null_color2", 0x0, 0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_6_1007 end

    def Function_7_1116(): pass

    label("Function_7_1116")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)
    SoundLoad(150)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a lift control panel.\x01",
            "Operate it?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1268")
    Fade(500)
    SetChrPos(0x0, 301300, 0, 20500, 180)
    SetChrPos(0x1, 302300, 0, 20500, 180)
    SetChrPos(0x2, 301300, 0, 21500, 180)
    SetChrPos(0x3, 302300, 0, 21500, 180)
    OP_68(300400, 1500, 21470, 0)
    MoveCamera(37, 51, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_71(0x5, 0x2F8, 0x3B6, 0x0, 0x0)
    Sleep(200)
    OP_68(301740, -1000, 14430, 3200)
    MoveCamera(33, 42, 0, 3200)
    Sleep(1800)
    Sound(150, 2, 100, 0)
    Sleep(200)
    FadeToDark(500, 0, -1)
    Sleep(4000)
    StopSound(150, 1000, 100)
    Sleep(1000)
    OP_0D()
    NewScene("m0302", 115, 0, 0)
    IdleLoop()

    label("loc_1268")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_7_1116 end

    def Function_8_1270(): pass

    label("Function_8_1270")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_70(0x5, 0x352)
    Sleep(1)
    OP_68(299320, -1000, 7960, 0)
    MoveCamera(24, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_90(0x0, 299500, -2500, 9500, 270)
    OP_90(0x1, 299500, -2500, 8500, 270)
    OP_90(0x2, 300500, -2500, 9500, 270)
    OP_90(0x3, 300500, -2500, 8500, 270)
    Sound(145, 0, 100, 0)
    OP_68(299490, 1500, 24190, 3200)
    MoveCamera(60, 27, 0, 3200)
    OP_71(0x5, 0x352, 0x2F8, 0x0, 0x0)
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x5)
    OP_6F(0x1)
    Sleep(500)
    SetMapObjFrame(0x5, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x5, "Null_color2", 0x1, 0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_8_1270 end

    def Function_9_137F(): pass

    label("Function_9_137F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch42200.itc", 0x1E)
    LoadChrToIndex("chr/ch42250.itc", 0x1F)
    LoadChrToIndex("chr/ch42251.itc", 0x20)
    LoadChrToIndex("chr/ch42300.itc", 0x21)
    LoadChrToIndex("chr/ch42350.itc", 0x22)
    LoadChrToIndex("chr/ch42351.itc", 0x23)
    LoadChrToIndex("chr/ch42352.itc", 0x24)
    LoadChrToIndex("chr/ch00050.itc", 0x25)
    LoadChrToIndex("chr/ch00051.itc", 0x26)
    LoadChrToIndex("chr/ch00150.itc", 0x27)
    LoadChrToIndex("chr/ch00151.itc", 0x28)
    LoadChrToIndex("chr/ch00250.itc", 0x29)
    LoadChrToIndex("chr/ch00251.itc", 0x2A)
    LoadChrToIndex("chr/ch00350.itc", 0x2B)
    LoadChrToIndex("chr/ch00351.itc", 0x2C)
    LoadChrToIndex("chr/ch02950.itc", 0x2D)
    LoadChrToIndex("chr/ch02951.itc", 0x2E)
    LoadChrToIndex("chr/ch03050.itc", 0x2F)
    LoadChrToIndex("chr/ch03051.itc", 0x30)
    LoadChrToIndex("apl/ch51243.itc", 0x31)
    LoadChrToIndex("apl/ch50014.itc", 0x32)
    LoadChrToIndex("chr/ch42254.itc", 0x33)
    LoadEffect(0x1, "event/ev10016.eff")
    SetChrPos(0x101, -38000, -8000, -600, 90)
    SetChrPos(0x102, -38000, -8000, 600, 90)
    SetChrPos(0x103, -39000, -8000, -1000, 90)
    SetChrPos(0x104, -39200, -8000, 1000, 90)
    SetChrPos(0x109, -40200, -8000, -600, 90)
    SetChrPos(0x105, -40200, -8000, 600, 90)
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
    SetChrChipByIndex(0x9, 0x31)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 900, 0, 900, 225)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -1700, 0, -200, 90)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -200, 0, -1700, 0)
    SetChrChipByIndex(0xC, 0x21)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -1200, 0, 1200, 135)
    SetChrChipByIndex(0xD, 0x21)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 1200, 0, -1200, 315)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -1300, 0, -1300, 45)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -2600, 0, 300, 90)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 300, 0, -2600, 0)
    ClearChrFlags(0x15, 0x80)
    OP_78(0x8, 0x15)
    OP_49()
    ClearMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x8, 0x1000)
    SetChrPos(0x15, 400, 150, 400, 0)
    OP_D5(0x15, 0x0, 0x36EE8, 0x0, 0x0)
    OP_68(-34500, -7100, 0, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(16500, 0)
    OP_68(-30500, -7100, 0, 4000)
    FadeToBright(2000, 0)

    def lambda_1680():
        OP_97(0x101, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1680)
    Sleep(150)

    def lambda_169D():
        OP_97(0x102, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_169D)
    Sleep(150)

    def lambda_16BA():
        OP_97(0x103, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_16BA)
    Sleep(150)

    def lambda_16D7():
        OP_97(0x104, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_16D7)
    Sleep(150)

    def lambda_16F4():
        OP_97(0x109, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_16F4)
    Sleep(150)

    def lambda_1711():
        OP_97(0x105, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1711)
    Sleep(500)

    def lambda_172E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_172E)
    Sleep(300)

    def lambda_1742():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1742)
    Sleep(500)

    def lambda_1756():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1756)
    Sleep(300)

    def lambda_176A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_176A)
    Sleep(500)

    def lambda_177E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_177E)
    Sleep(300)

    def lambda_1792():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1792)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
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
    Sleep(1000)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#6P#00007F(Those are...!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00201F(Somehow it looks like we managed\x01",
            "to catch up with them.)\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, 900, 0, 4000)
    MoveCamera(45, 33, 0, 4000)
    SetCameraDistance(15500, 4000)
    BeginChrThread(0x15, 3, 0, 10)
    OP_6F(0x79)
    Sound(867, 0, 100, 0)

    ChrTalk(
        0x9,
        "...Kh, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In the end, the tower blow up\x01",
            "has been prevented, eh...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#3P...Kh, damn it all...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#4POur good chance to get rid of the\x01",
            "heinous "Blood and Iron Chancellor"...!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#6PAlthough we went to the trouble to\x01",
            "join hands with the Republicans...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(812, 0, 100, 0)
    EndChrThread(0x15, 0x3)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    OP_0D()
    Sleep(300)
    OP_82(0x32, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0x9,
        "Keep your spirits up, comrades!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Our allies are many!\x01",
            "Starting with Duke Cayenne, those\x01",
            "guys will help us once again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If we can get out of this place,\x01",
            "another opportunity will──\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sound(2090, 255, 100, 0)

    NpcTalk(
        0x101,
        "Lloyd's Voice",
        "Freeze...!\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1BF4():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1BF4)

    def lambda_1C01():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_1C01)
    Sleep(50)

    def lambda_1C11():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1C11)

    def lambda_1C1E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1C1E)
    Sleep(50)

    def lambda_1C2E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1C2E)

    def lambda_1C3B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_1C3B)
    Sleep(50)

    def lambda_1C4B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1C4B)

    def lambda_1C58():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1C58)
    WaitChrThread(0x10, 2)
    Fade(500)
    OP_68(-9800, -300, -700, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(18000, 0)
    SetChrFlags(0x15, 0x80)
    SetMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x8, 0x1000)
    OP_68(-4800, 700, 0, 2500)
    SetCameraDistance(16000, 2500)
    SetChrChipByIndex(0x101, 0x25)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x27)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x29)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x2B)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x2D)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x2F)
    SetChrSubChip(0x105, 0x0)
    OP_90(0x101, -17200, 0, 0, 90)
    OP_90(0x102, -18000, 0, -1700, 90)
    OP_90(0x103, -19500, 0, 1300, 90)
    OP_90(0x104, -18000, 0, 1700, 90)
    OP_90(0x109, -19500, 0, -1300, 90)
    OP_90(0x105, -18900, 0, 0, 90)

    def lambda_1D5D():
        OP_97(0x101, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1D5D)
    Sleep(100)

    def lambda_1D7A():
        OP_97(0x104, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1D7A)
    Sleep(100)

    def lambda_1D97():
        OP_97(0x102, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1D97)
    Sleep(100)

    def lambda_1DB4():
        OP_97(0x105, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1DB4)
    Sleep(100)

    def lambda_1DD1():
        OP_97(0x109, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1DD1)
    Sleep(100)

    def lambda_1DEE():
        OP_97(0x103, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1DEE)
    BeginChrThread(0x20, 1, 0, 19)
    BeginChrThread(0xF, 3, 0, 17)
    Sleep(100)
    BeginChrThread(0xA, 3, 0, 12)
    Sleep(100)
    BeginChrThread(0xE, 3, 0, 16)
    Sleep(400)
    BeginChrThread(0xB, 3, 0, 13)
    Sleep(100)
    BeginChrThread(0xC, 3, 0, 14)
    Sleep(100)
    BeginChrThread(0xD, 3, 0, 15)
    Sleep(100)
    BeginChrThread(0x10, 3, 0, 18)
    Sleep(400)
    BeginChrThread(0x9, 3, 0, 11)
    WaitChrThread(0x9, 3)

    ChrTalk(
        0xA,
        "#11PWha...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#11PThe brats from before!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Impossible...!\x01",
            "The pursuit route should've been destroyed!!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x104,
        (
            "#00304F#6PSorry for you, but we chased you\x01",
            "down from a different route.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00202FI don't know what data you\x01",
            "acquired, but it seems it\x01",
            "wasn't accurate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PKh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PWho the heck are you,\x01",
            "you damn brats...!?\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    Sound(802, 0, 100, 0)
    Sound(805, 0, 50, 0)
    SetChrChipByIndex(0x101, 0x32)
    SetChrSubChip(0x101, 0x0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#6P#00003FCrossbell Police, Special Support Section.\x02\x03",
            "#00013FWe're taking you in with the charges of terrorist \x01",
            "activities, flagrante delicto of sabotage as well \x01",
            "as magnicide, mass murder attempt and others.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x50, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xA,
        "#11PPolice...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PAs if the mere likes of an autonomous state\x01",
            "police could thwart our great cause!!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x109,
        (
            "#6P#10107F#4SD-Don't joke around!!\x02\x03",
            "#10110FHow many people were you\x01",
            "planning to involve!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10306FOh boy, there're those like them.\x02\x03",
            "#10300FGuys who can't see what's around them by \x01",
            "drunkening themselves with a "just cause".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PS-Silence!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "You damn ignorant people only lusting for a\x01",
            "futile flourishing and who forgot their pride!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108F......!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203F...Looks like they have zero intention\x01",
            "to reflect on what they did.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Fade(250)
    Sound(805, 0, 80, 0)
    SetChrChipByIndex(0x101, 0x25)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(1750)
    OP_64(0x9)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#11P──It's not even our real intention\x01",
            "to involve unrelated people in it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PHowever, if we leave that man alone more than\x01",
            "this, the Empire will become a giant mess...\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7452", 0)
    SetChrSubChip(0x9, 0x3)
    Sleep(100)
    SetChrSubChip(0x9, 0x4)
    Sound(802, 0, 100, 0)
    Sound(534, 0, 60, 0)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x9,
        (
            "#11PWe won't show any mercy to\x01",
            "whom will try to hindrance us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00013FKh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00307FNo use talkin'!\x01",
            "Anyway, let's pummel 'em down!\x02",
        )
    )

    CloseMessageWindow()
    BlurSwitch(0x190, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(13500, 400)

    def lambda_2599():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2599)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    Sleep(30)

    def lambda_25BE():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_25BE)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)

    def lambda_25E0():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_25E0)
    SetChrChipByIndex(0xF, 0x20)
    SetChrSubChip(0xF, 0x0)
    Sleep(30)

    def lambda_2605():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2605)
    SetChrChipByIndex(0xB, 0x23)
    SetChrSubChip(0xB, 0x0)

    def lambda_2627():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2627)
    SetChrChipByIndex(0xD, 0x23)
    SetChrSubChip(0xD, 0x0)
    Sleep(30)

    def lambda_264C():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_264C)
    SetChrChipByIndex(0xC, 0x23)
    SetChrSubChip(0xC, 0x0)

    def lambda_266E():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_266E)
    SetChrChipByIndex(0x10, 0x23)
    SetChrSubChip(0x10, 0x0)
    Sleep(310)
    EndChrThread(0xA, 0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0xB, 0x1)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xC, 0x1)
    EndChrThread(0x10, 0x1)
    Battle("BattleInfo_5D8", 0x0, 0x0, 0x100, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 20)
    Return()

    # Function_9_137F end

    def Function_10_26C8(): pass

    label("Function_10_26C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2712")
    PlayEffect(0x1, 0xFF, 0x15, 0x1, -600, 1150, 0, 0, 0, 0, 200, 200, 200, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Jump("Function_10_26C8")

    label("loc_2712")

    Return()

    # Function_10_26C8 end

    def Function_11_2713(): pass

    label("Function_11_2713")


    def lambda_2718():
        OP_95(0xFE, 700, 0, -500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2718)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sound(531, 0, 70, 0)
    Sound(540, 0, 50, 0)
    SetChrChipByIndex(0x9, 0x33)
    SetChrSubChip(0x9, 0x0)
    Return()

    # Function_11_2713 end

    def Function_12_274D(): pass

    label("Function_12_274D")


    def lambda_2752():
        OP_95(0xFE, -3000, 0, 0, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2752)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    Return()

    # Function_12_274D end

    def Function_13_277B(): pass

    label("Function_13_277B")


    def lambda_2780():
        OP_95(0xFE, -1500, 0, 700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2780)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xB, 0x24)
    SetChrSubChip(0xB, 0x2)
    Return()

    # Function_13_277B end

    def Function_14_27AF(): pass

    label("Function_14_27AF")


    def lambda_27B4():
        OP_95(0xFE, -900, 0, 2500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_27B4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    SetChrChipByIndex(0xC, 0x24)
    SetChrSubChip(0xC, 0x2)
    Return()

    # Function_14_27AF end

    def Function_15_27DD(): pass

    label("Function_15_27DD")


    def lambda_27E2():
        OP_95(0xFE, -1500, 0, -700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_27E2)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xD, 0x24)
    SetChrSubChip(0xD, 0x2)
    Return()

    # Function_15_27DD end

    def Function_16_2811(): pass

    label("Function_16_2811")


    def lambda_2816():
        OP_95(0xFE, -2700, 0, -1900, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2816)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    Return()

    # Function_16_2811 end

    def Function_17_283F(): pass

    label("Function_17_283F")


    def lambda_2844():
        OP_95(0xFE, -2700, 0, 1900, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2844)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sound(531, 0, 70, 0)
    Sound(540, 0, 50, 0)
    SetChrChipByIndex(0xF, 0x1F)
    SetChrSubChip(0xF, 0x0)
    Return()

    # Function_17_283F end

    def Function_18_2879(): pass

    label("Function_18_2879")


    def lambda_287E():
        OP_95(0xFE, -900, 0, -2500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_287E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    SetChrChipByIndex(0x10, 0x24)
    SetChrSubChip(0x10, 0x2)
    Return()

    # Function_18_2879 end

    def Function_19_28A7(): pass

    label("Function_19_28A7")

    Sleep(2000)
    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    Return()

    # Function_19_28A7 end

    def Function_20_28B7(): pass

    label("Function_20_28B7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch42200.itc", 0x1E)
    LoadChrToIndex("chr/ch42250.itc", 0x1F)
    LoadChrToIndex("chr/ch42251.itc", 0x20)
    LoadChrToIndex("chr/ch42300.itc", 0x21)
    LoadChrToIndex("chr/ch42350.itc", 0x22)
    LoadChrToIndex("chr/ch42351.itc", 0x23)
    LoadChrToIndex("chr/ch42353.itc", 0x24)
    LoadChrToIndex("chr/ch00050.itc", 0x25)
    LoadChrToIndex("chr/ch00051.itc", 0x26)
    LoadChrToIndex("chr/ch00150.itc", 0x27)
    LoadChrToIndex("chr/ch00151.itc", 0x28)
    LoadChrToIndex("chr/ch00250.itc", 0x29)
    LoadChrToIndex("chr/ch00251.itc", 0x2A)
    LoadChrToIndex("chr/ch00350.itc", 0x2B)
    LoadChrToIndex("chr/ch00351.itc", 0x2C)
    LoadChrToIndex("chr/ch02950.itc", 0x2D)
    LoadChrToIndex("chr/ch02951.itc", 0x2E)
    LoadChrToIndex("chr/ch03050.itc", 0x2F)
    LoadChrToIndex("chr/ch03051.itc", 0x30)
    LoadChrToIndex("chr/ch42253.itc", 0x31)
    LoadChrToIndex("monster/ch84150.itc", 0x32)
    LoadChrToIndex("monster/ch84350.itc", 0x33)
    LoadChrToIndex("chr/ch00056.itc", 0x34)
    LoadChrToIndex("chr/ch00156.itc", 0x35)
    LoadChrToIndex("chr/ch00256.itc", 0x36)
    LoadChrToIndex("chr/ch00356.itc", 0x37)
    LoadChrToIndex("chr/ch0295F.itc", 0x38)
    LoadChrToIndex("chr/ch0305F.itc", 0x39)
    LoadEffect(0x1, "event/ev12036.eff")
    LoadEffect(0x2, "event/eva03_01.eff")
    SoundLoad(943)
    SetChrChipByIndex(0x101, 0x25)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x27)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x29)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x2B)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x2D)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x2F)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x101, -200, 0, 0, 90)
    SetChrPos(0x102, -1000, 0, -1700, 90)
    SetChrPos(0x103, -2500, 0, 1300, 90)
    SetChrPos(0x104, -1000, 0, 1700, 90)
    SetChrPos(0x109, -2500, 0, -1300, 90)
    SetChrPos(0x105, -1900, 0, 0, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 3100, 0, 0, 270)
    SetChrChipByIndex(0xA, 0x31)
    SetChrSubChip(0xA, 0x3)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 3600, 0, 1900, 270)
    SetChrChipByIndex(0xB, 0x24)
    SetChrSubChip(0xB, 0x3)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 7200, 0, -1300, 270)
    SetChrChipByIndex(0xC, 0x22)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 7200, 0, 1300, 270)
    SetChrChipByIndex(0xD, 0x24)
    SetChrSubChip(0xD, 0x3)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 5200, 0, 2700, 270)
    SetChrChipByIndex(0xE, 0x31)
    SetChrSubChip(0xE, 0x3)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 3600, 0, -1900, 270)
    SetChrChipByIndex(0xF, 0x31)
    SetChrSubChip(0xF, 0x3)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 6200, 0, 0, 270)
    SetChrChipByIndex(0x10, 0x22)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 5200, 0, -2700, 270)
    SetChrChipByIndex(0x16, 0x32)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 0, 0, 30000, 180)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x17, 0x32)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 0, 0, 30000, 180)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x18, 0x33)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 0, 0, 30000, 180)
    OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x19, 0x33)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 0, 0, 30000, 180)
    OP_A7(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x14, 0x80)
    OP_78(0x6, 0x14)
    OP_49()
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x6, 0x1000)
    SetMapObjFrame(0x6, "light", 0x0, 0x1)
    SetMapObjFrame(0x6, "mark00", 0x1, 0x1)
    OP_74(0x6, 0x1E)
    OP_71(0x6, 0xB5, 0xF0, 0x0, 0x20)
    SetChrPos(0x14, 0, 0, 35000, 180)
    OP_D5(0x14, 0x0, 0x2BF20, 0x0, 0x0)
    OP_68(1800, 900, 0, 0)
    MoveCamera(53, 19, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(15500, 0)
    SetCameraDistance(16500, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)

    def lambda_2CC4():
        OP_96(0xFE, 0x1004, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2CC4)
    WaitChrThread(0x9, 1)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    OP_64(0x9)

    def lambda_2CED():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2CED)
    Sleep(500)

    ChrTalk(
        0xA,
        "Kh...impossible!?\x02",
    )

    CloseMessageWindow()

    def lambda_2D20():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2D20)
    Sleep(500)

    ChrTalk(
        0xB,
        (
            "To think some mere police from an\x01",
            "autonomous state could be so good...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006F──It's true that Crossbell\x01",
            "is enjoying prosperity.\x02\x03",
            "#00013FHowever, we didn't get drowned\x01",
            "in it and lost sight of our pride!\x02\x03",
            "#00007FWe have many restraints and pressures...\x01",
            "And although we're squashed by them,\x01",
            "we're struggling to try to get over those barriers!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00102FLloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10100FMr. Lloyd...\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xA, 3, 0, 22)
    Sleep(200)
    BeginChrThread(0xB, 3, 0, 23)
    Sleep(200)
    BeginChrThread(0xD, 3, 0, 23)
    Sleep(200)
    Sound(540, 0, 20, 0)
    BeginChrThread(0xE, 3, 0, 22)
    Sleep(200)
    BeginChrThread(0xF, 3, 0, 22)
    Sound(531, 0, 30, 0)
    WaitChrThread(0xF, 3)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#11P...It looks like I had made\x01",
            "light of you a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI admit that trying to blow up \x01",
            "the tower was going too far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FThen...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x9,
        (
            "#11P──However, we can't get\x01",
            "caught until we have killed the\x01",
            ""Blood and Iron Chancellor"!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x103, 0x0, 0x1F4)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x103,
        "#12P#00207FEveryone...!\x02",
    )

    CloseMessageWindow()
    OP_93(0x104, 0x0, 0x1F4)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x104,
        "#00307F#11PIncomin', back away!\x02",
    )

    CloseMessageWindow()
    OP_68(0, 900, 17000, 1500)
    MoveCamera(37, 15, 0, 1500)
    SetCameraDistance(14500, 1500)

    def lambda_30D1():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_30D1)
    BeginChrThread(0x9, 3, 0, 24)
    Sleep(50)

    def lambda_30E7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_30E7)
    BeginChrThread(0xA, 3, 0, 24)
    Sleep(50)

    def lambda_30FD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_30FD)
    BeginChrThread(0xE, 3, 0, 24)
    Sleep(50)

    def lambda_3113():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3113)
    BeginChrThread(0xD, 3, 0, 25)
    BeginChrThread(0x10, 3, 0, 25)
    Sleep(50)
    BeginChrThread(0xF, 3, 0, 24)
    BeginChrThread(0xB, 3, 0, 25)
    BeginChrThread(0xC, 3, 0, 25)
    OP_6F(0x79)
    StopBGM(0x1388)
    Sound(598, 0, 50, 0)
    Sound(623, 0, 100, 0)
    PlayEffect(0x1, 0x1, 0xFF, 0x0, 0, 1000, 30000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0x2, 0xFF, 0x0, 1000, 1500, 30000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0x3, 0xFF, 0x0, -1000, 1500, 30000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x14, 3, 0, 21)
    Sleep(500)
    Sound(869, 0, 50, 0)
    OP_68(-2600, 900, 0, 1000)
    MoveCamera(53, 19, 0, 1000)
    SetCameraDistance(17500, 1000)
    Sleep(200)
    BeginChrThread(0x103, 3, 0, 38)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 35)
    BeginChrThread(0x105, 3, 0, 36)
    Sleep(50)
    BeginChrThread(0x101, 3, 0, 33)
    BeginChrThread(0x109, 3, 0, 37)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 34)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x14, 3)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00007F#6P#NWha...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        "#10110F#6P#NS-Smart missiles!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7586", 0)
    Fade(250)
    OP_68(0, 1000, 25000, 0)
    MoveCamera(25, 25, 21, 0)
    OP_6E(700, 0)
    SetCameraDistance(13500, 0)
    OP_68(1500, 1250, 1000, 3000)
    MoveCamera(50, 15, 11, 3000)
    SetCameraDistance(15500, 3000)
    Sound(486, 0, 100, 0)
    Sound(494, 0, 100, 0)
    ClearMapObjFlags(0x6, 0x4)
    PlayEffect(0x2, 0x4, 0x14, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x5, 0x14, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x6, 0x14, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_33C8():
        OP_96(0xFE, 0x0, 0x0, 0x0, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_33C8)
    Sleep(2500)

    def lambda_33E5():
        OP_D5(0xFE, 0x0, 0x30D40, 0x0, 0x2BC)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_33E5)
    OP_71(0x6, 0x5B, 0x78, 0x0, 0x0)
    Sound(487, 0, 100, 0)
    WaitChrThread(0x14, 1)
    StopEffect(0x4, 0x2)
    StopEffect(0x5, 0x2)
    StopEffect(0x6, 0x2)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    OP_79(0x6)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(-2300, 1100, 0, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14500, 0)
    OP_68(-4300, 1100, 0, 1500)
    SetCameraDistance(16000, 1500)
    OP_0D()
    Sound(145, 2, 100, 0)
    OP_74(0x6, 0xF)
    OP_71(0x6, 0xF1, 0xFD, 0x0, 0x0)
    OP_79(0x6)
    OP_24(0x91)
    Sound(143, 0, 100, 0)
    OP_74(0x6, 0x1E)
    OP_6F(0x79)

    ChrTalk(
        0x109,
        "#6P#N#10111FAh...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        "#6P#N#00101FFrom the Crossbell CGF...!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00307F#6P#NBastards...\x01",
            "Where the heck did you get that from!?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xE,
        (
            "#12PHa ha, we have quite the\x01",
            "useful accomplice, you see!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You can play with that\x01",
            "as much as you want!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PNo use in arguing more than this!\x01",
            "──Withdraw!\x02",
        )
    )

    CloseMessageWindow()
    Sound(943, 2, 50, 0)
    BeginChrThread(0x16, 0, 0, 28)
    BeginChrThread(0xB, 3, 0, 27)
    BeginChrThread(0xC, 3, 0, 27)
    Sleep(100)
    BeginChrThread(0xF, 3, 0, 26)
    Sleep(100)
    BeginChrThread(0xD, 3, 0, 27)
    BeginChrThread(0x10, 3, 0, 27)
    Sleep(100)
    BeginChrThread(0x9, 3, 0, 26)
    Sleep(100)
    BeginChrThread(0xA, 3, 0, 26)
    BeginChrThread(0xE, 3, 0, 26)
    WaitChrThread(0x16, 3)

    def lambda_3629():
        OP_A6(0xFE, 0x0, 0x32, 0x2EE, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3629)
    Sleep(50)

    def lambda_3645():
        OP_A6(0xFE, 0x0, 0x32, 0x2EE, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3645)
    Sleep(50)

    def lambda_3661():
        OP_A6(0xFE, 0x0, 0x32, 0x2EE, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3661)
    Sleep(50)

    def lambda_367D():
        OP_A6(0xFE, 0x0, 0x32, 0x2EE, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_367D)
    Sleep(50)

    def lambda_3699():
        OP_A6(0xFE, 0x0, 0x32, 0x2EE, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3699)
    Sleep(50)

    def lambda_36B5():
        OP_A6(0xFE, 0x0, 0x32, 0x2EE, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_36B5)
    Sleep(250)
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x25)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x27)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x29)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x2B)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x2D)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x2F)
    SetChrSubChip(0x105, 0x0)
    OP_0D()
    WaitChrThread(0x19, 3)

    ChrTalk(
        0x101,
        (
            "#6P#00010FKh... \x01",
            "Everyone, can you move!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#N#00107FYes...somehow.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00201F#6PI can too...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FWell, we could crush it\x01",
            "with some luck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#N#10107FAt any rate, it's a sturdy vehicle!\x01",
            "It's resistant to Arts too!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00307F#6PFirst of all, let's move and watch for a chance!\x02",
    )

    CloseMessageWindow()
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(14000, 500)
    Sleep(500)
    EndChrThread(0x9, 0xFF)
    EndChrThread(0xA, 0xFF)
    EndChrThread(0xB, 0xFF)
    EndChrThread(0xC, 0xFF)
    EndChrThread(0xD, 0xFF)
    EndChrThread(0xE, 0xFF)
    EndChrThread(0xF, 0xFF)
    EndChrThread(0x10, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    OP_24(0x91)
    OP_24(0x3AF)
    Battle("BattleInfo_61C", 0x0, 0x0, 0x100, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    Call(0, 39)
    Return()

    # Function_20_28B7 end

    def Function_21_38E4(): pass

    label("Function_21_38E4")

    Sleep(1500)
    OP_82(0x1F4, 0x1F4, 0xBB8, 0x3E8)
    Sound(196, 0, 100, 0)
    Sound(598, 0, 80, 0)
    Sleep(250)
    Sound(556, 0, 100, 0)
    Sound(250, 0, 100, 0)
    Sleep(750)
    Return()

    # Function_21_38E4 end

    def Function_22_3917(): pass

    label("Function_22_3917")


    def lambda_391C():
        OP_A6(0xFE, 0x0, 0x32, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_391C)
    Sleep(500)
    SetChrSubChip(0xFE, 0x2)
    Sleep(80)
    SetChrSubChip(0xFE, 0x1)
    Sleep(80)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_0D()
    Return()

    # Function_22_3917 end

    def Function_23_3956(): pass

    label("Function_23_3956")


    def lambda_395B():
        OP_A6(0xFE, 0x0, 0x32, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_395B)
    Sleep(500)
    SetChrSubChip(0xFE, 0x2)
    Sleep(80)
    SetChrSubChip(0xFE, 0x1)
    Sleep(80)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_0D()
    Return()

    # Function_23_3956 end

    def Function_24_3995(): pass

    label("Function_24_3995")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)

    def lambda_39A2():
        OP_98(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_39A2)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_24_3995 end

    def Function_25_39C4(): pass

    label("Function_25_39C4")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)

    def lambda_39D1():
        OP_98(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_39D1)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_25_39C4 end

    def Function_26_39F3(): pass

    label("Function_26_39F3")

    OP_93(0xFE, 0x5A, 0x1F4)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3A07():
        OP_98(0xFE, 0x9C40, 0x0, 0x0, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3A07)
    Sleep(5000)

    def lambda_3A24():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3A24)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_26_39F3 end

    def Function_27_3A35(): pass

    label("Function_27_3A35")

    OP_93(0xFE, 0x5A, 0x1F4)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3A49():
        OP_98(0xFE, 0x9C40, 0x0, 0x0, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3A49)
    Sleep(5000)

    def lambda_3A66():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3A66)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_27_3A35 end

    def Function_28_3A77(): pass

    label("Function_28_3A77")

    ClearChrFlags(0x16, 0x80)
    BeginChrThread(0x16, 3, 0, 29)
    Sleep(500)
    ClearChrFlags(0x18, 0x80)
    BeginChrThread(0x18, 3, 0, 31)
    Sleep(500)
    ClearChrFlags(0x17, 0x80)
    BeginChrThread(0x17, 3, 0, 30)
    Sleep(500)
    ClearChrFlags(0x19, 0x80)
    BeginChrThread(0x19, 3, 0, 32)
    Return()

    # Function_28_3A77 end

    def Function_29_3AAD(): pass

    label("Function_29_3AAD")


    def lambda_3AB2():
        OP_96(0xFE, 0x0, 0x0, 0x2710, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3AB2)

    def lambda_3ACC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3ACC)
    WaitChrThread(0xFE, 1)

    def lambda_3AE1():
        OP_95(0xFE, -1500, 0, 5300, 5500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3AE1)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_29_3AAD end

    def Function_30_3B02(): pass

    label("Function_30_3B02")


    def lambda_3B07():
        OP_96(0xFE, 0x0, 0x0, 0x2710, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B07)

    def lambda_3B21():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3B21)
    WaitChrThread(0xFE, 1)

    def lambda_3B36():
        OP_95(0xFE, -2700, 0, 6700, 5500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B36)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_30_3B02 end

    def Function_31_3B57(): pass

    label("Function_31_3B57")


    def lambda_3B5C():
        OP_96(0xFE, 0x0, 0x0, 0x2710, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B5C)

    def lambda_3B76():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3B76)
    WaitChrThread(0xFE, 1)

    def lambda_3B8B():
        OP_95(0xFE, 400, 0, 6000, 5500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B8B)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_31_3B57 end

    def Function_32_3BAC(): pass

    label("Function_32_3BAC")


    def lambda_3BB1():
        OP_96(0xFE, 0x0, 0x0, 0x2710, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3BB1)

    def lambda_3BCB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3BCB)
    WaitChrThread(0xFE, 1)

    def lambda_3BE0():
        OP_95(0xFE, -800, 0, 7400, 5500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3BE0)
    WaitChrThread(0xFE, 1)
    OP_24(0x3AF)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_32_3BAC end

    def Function_33_3C04(): pass

    label("Function_33_3C04")


    def lambda_3C09():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3C09)
    Sleep(200)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0x101, 0x34)
    SetChrSubChip(0x101, 0x2)

    def lambda_3C26():
        OP_9C(0xFE, 0xFFFFE69C, 0x0, 0x0, 0x258, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C26)
    WaitChrThread(0x101, 1)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_33_3C04 end

    def Function_34_3C4C(): pass

    label("Function_34_3C4C")


    def lambda_3C51():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3C51)
    Sleep(200)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0x102, 0x35)
    SetChrSubChip(0x102, 0x2)

    def lambda_3C6E():
        OP_9C(0xFE, 0xFFFFE958, 0x0, 0xFFFFFCE0, 0x258, 0x7D0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3C6E)
    WaitChrThread(0x102, 1)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_34_3C4C end

    def Function_35_3C94(): pass

    label("Function_35_3C94")


    def lambda_3C99():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3C99)
    Sleep(200)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0x104, 0x37)
    SetChrSubChip(0x104, 0x2)

    def lambda_3CB6():
        OP_9C(0xFE, 0xFFFFE958, 0x0, 0x320, 0x258, 0x7D0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3CB6)
    WaitChrThread(0x104, 1)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_35_3C94 end

    def Function_36_3CDC(): pass

    label("Function_36_3CDC")


    def lambda_3CE1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3CE1)
    Sleep(200)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0x105, 0x39)
    SetChrSubChip(0x105, 0x2)

    def lambda_3CFE():
        OP_9C(0xFE, 0xFFFFE570, 0x0, 0x0, 0x258, 0x7D0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3CFE)
    WaitChrThread(0x105, 1)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_36_3CDC end

    def Function_37_3D24(): pass

    label("Function_37_3D24")


    def lambda_3D29():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3D29)
    Sleep(200)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0x109, 0x38)
    SetChrSubChip(0x109, 0x2)

    def lambda_3D46():
        OP_9C(0xFE, 0xFFFFEA20, 0x0, 0xFFFFFE70, 0x258, 0x7D0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3D46)
    WaitChrThread(0x109, 1)
    SetChrSubChip(0x109, 0x0)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_37_3D24 end

    def Function_38_3D6C(): pass

    label("Function_38_3D6C")


    def lambda_3D71():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3D71)
    Sleep(200)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0x103, 0x36)
    SetChrSubChip(0x103, 0x2)
    Sound(809, 0, 100, 0)

    def lambda_3D94():
        OP_9C(0xFE, 0xFFFFEA20, 0x0, 0x190, 0x258, 0x7D0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3D94)
    WaitChrThread(0x103, 1)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_38_3D6C end

    def Function_39_3DBA(): pass

    label("Function_39_3DBA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch02950.itc", 0x22)
    LoadChrToIndex("chr/ch03050.itc", 0x23)
    LoadEffect(0x0, "battle\\ms00103.eff ")
    SoundLoad(863)
    SoundLoad(864)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x101, -4700, 0, 0, 90)
    SetChrPos(0x102, -4800, 0, -2500, 90)
    SetChrPos(0x103, -6100, 0, 1700, 90)
    SetChrPos(0x104, -4800, 0, 2500, 90)
    SetChrPos(0x109, -6100, 0, -1700, 90)
    SetChrPos(0x105, -6700, 0, 0, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x6, 0x1000)
    SetChrFlags(0x8, 0x80)
    OP_78(0x9, 0x8)
    OP_49()
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x1000)
    OP_74(0x9, 0x1E)
    OP_71(0x9, 0x79, 0xF0, 0x0, 0x20)
    SetMapObjFrame(0x9, "mark00", 0x1, 0x1)
    SetChrPos(0x8, 2000, 0, 1000, 180)
    OP_D5(0x8, 0x0, 0x222E0, 0x0, 0x0)
    OP_68(1500, 2100, 500, 0)
    MoveCamera(33, 37, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    SetCameraDistance(15500, 2000)
    OP_82(0x12C, 0x12C, 0xBB8, 0x5DC)
    Sound(196, 0, 100, 0)
    Sound(598, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 2000, 1500, 1500, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    CancelBlur(1500)
    Sleep(200)
    Sound(556, 0, 100, 0)
    Sound(200, 0, 100, 0)
    Sleep(1300)
    OP_6F(0x79)
    OP_68(-2300, 900, 0, 2000)
    MoveCamera(50, 19, 0, 2000)
    SetCameraDistance(16000, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#6P#00013FAlright...did we make it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00107FWe must save the people\x01",
            "on board quick, or else...!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#6P#00206F...No. There were no vital\x01",
            "reactions from the inside.\x02\x03",
            "#00201FIt looks like it was operated\x01",
            "on autopilot.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x109,
        "#6P#N#10111FEEH!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    OP_0D()

    def lambda_4144():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4144)
    Sleep(50)

    def lambda_4154():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4154)
    Sleep(50)

    def lambda_4164():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4164)
    Sleep(50)

    def lambda_4174():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4174)
    Sleep(50)

    def lambda_4184():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4184)
    Sleep(50)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x104,
        "#00306F#5PHey now, for real...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10301FAnd they had archaisms too.\x01",
            "It appears they have the\x01",
            "help of some strange guys.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#5P#00003F...Tch, let's leave the talks for later!\x02\x03",
            "#00013FIn any case, we must chase the guys who──\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1770)
    Sound(863, 2, 50, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
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
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_434A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_434A)

    def lambda_4357():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4357)

    def lambda_4364():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4364)

    def lambda_4371():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4371)

    def lambda_437E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_437E)
    OP_68(32500, 900, 0, 3000)
    OP_6F(0x79)
    MoveCamera(55, 23, 0, 4500)
    SetCameraDistance(19500, 4000)
    Sound(864, 2, 60, 0)
    OP_82(0x32, 0x32, 0xBB8, 0x1F4)
    Sleep(1500)
    OP_82(0x32, 0x32, 0xBB8, 0x1F4)
    Sleep(1500)
    OP_82(0x32, 0x32, 0xBB8, 0x1F4)
    Sleep(1500)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00010F#6P#N!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00210F#6P#N......\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        "#10107F#6P#NA firefight sounds!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00108F#6P#NWhat in the world is going on...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00307F#6P#N...Anyway, let's go!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x14, 0x80)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_37()
    SetChrPos(0x0, -4000, 0, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x143, 7)
    OP_29(0xA4, 0x1, 0x9)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7561", 0)
    ReplaceBGM("ed7300", "ed7561")
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_39_3DBA end

    def Function_40_4504(): pass

    label("Function_40_4504")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch42300.itc", 0x1E)
    LoadChrToIndex("chr/ch42351.itc", 0x1F)
    LoadChrToIndex("chr/ch42352.itc", 0x20)
    LoadChrToIndex("chr/ch42353.itc", 0x21)
    LoadChrToIndex("chr/ch03300.itc", 0x22)
    LoadChrToIndex("chr/ch03400.itc", 0x23)
    LoadChrToIndex("chr/ch41900.itc", 0x24)
    LoadChrToIndex("chr/ch41950.itc", 0x25)
    LoadChrToIndex("chr/ch41951.itc", 0x26)
    LoadChrToIndex("chr/ch41952.itc", 0x27)
    LoadChrToIndex("apl/ch51244.itc", 0x28)
    LoadChrToIndex("apl/ch51217.itc", 0x29)
    LoadChrToIndex("apl/ch51221.itc", 0x2A)
    LoadChrToIndex("chr/ch02952.itc", 0x2B)
    LoadChrToIndex("chr/ch42253.itc", 0x2C)
    LoadChrToIndex("apl/ch51246.itc", 0x2D)
    LoadChrToIndex("apl/ch51247.itc", 0x2E)
    LoadChrToIndex("apl/ch51248.itc", 0x2F)
    LoadChrToIndex("apl/ch51249.itc", 0x30)
    LoadChrToIndex("apl/ch51250.itc", 0x31)
    LoadChrToIndex("apl/ch51251.itc", 0x32)
    LoadChrToIndex("apl/ch51252.itc", 0x33)
    LoadChrToIndex("apl/ch51253.itc", 0x34)
    LoadChrToIndex("apl/ch51254.itc", 0x35)
    LoadChrToIndex("apl/ch51219.itc", 0x36)
    LoadEffect(0x0, "event/ev12000.eff")
    LoadEffect(0x1, "battle/btgun00.eff")
    LoadEffect(0x2, "event/ev606_00.eff")
    LoadEffect(0x3, "event/eva00_00.eff")
    LoadEffect(0x4, "event/ev12002.eff")
    SoundLoad(860)
    SoundLoad(861)
    SoundLoad(2754)
    SoundLoad(2755)
    SoundLoad(4117)
    SoundLoad(3950)
    SoundLoad(3951)
    SoundLoad(3952)
    SetChrPos(0x101, 116000, 0, -700, 90)
    SetChrPos(0x102, 114900, 0, 1300, 90)
    SetChrPos(0x103, 114900, 0, -1200, 90)
    SetChrPos(0x104, 116000, 0, 600, 90)
    SetChrPos(0x109, 113800, 0, -700, 90)
    SetChrPos(0x105, 113800, 0, 600, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x9, 0x2C)
    SetChrSubChip(0x9, 0x3)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 171200, 0, 10000, 180)
    SetChrChipByIndex(0xA, 0x28)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 168700, 0, 12900, 270)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x2)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 167800, 0, 10200, 150)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xC, 0x28)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 169900, 0, 11400, 170)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xD, 0x28)
    SetChrSubChip(0xD, 0x1)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 173000, 0, 10800, 305)
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xE, 0x28)
    SetChrSubChip(0xE, 0x1)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 173400, 0, 12700, 90)
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xF, 0x28)
    SetChrSubChip(0xF, 0x3)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 166300, 0, 12100, 90)
    OP_52(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 178800, 0, 12500, 180)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x11, 0x22)
    SetChrSubChip(0x11, 0x0)
    SetChrPos(0x11, 170300, 0, 2300, 0)
    OP_52(0x11, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0x23)
    SetChrSubChip(0x12, 0x0)
    SetChrPos(0x12, 171400, 0, 1500, 0)
    OP_52(0x12, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    SetChrPos(0x13, 169200, 0, 1100, 0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1A, 0x27)
    SetChrSubChip(0x1A, 0x1)
    SetChrPos(0x1A, 171200, 0, 5400, 0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1B, 0x27)
    SetChrSubChip(0x1B, 0x1)
    SetChrPos(0x1B, 167900, 0, 4800, 0)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1C, 0x27)
    SetChrSubChip(0x1C, 0x1)
    SetChrPos(0x1C, 172000, 0, 3900, 0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1D, 0x27)
    SetChrSubChip(0x1D, 0x1)
    SetChrPos(0x1D, 169200, 0, 3700, 0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1E, 0x27)
    SetChrSubChip(0x1E, 0x1)
    SetChrPos(0x1E, 173700, 0, 5300, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 169200, 0, 13900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x0, 0x1A, 0x3, -100, 1100, 1150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x1, 0x1B, 0x3, -100, 1100, 1150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x2, 0x1C, 0x3, -100, 1100, 1150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x3, 0x1D, 0x3, -100, 1100, 1150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x4, 0x1E, 0x3, -100, 1100, 1150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_68(121500, 1300, 0, 0)
    MoveCamera(35, 19, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17500, 0)

    def lambda_4ABA():
        OP_97(0xFE, 0x2EE0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4ABA)
    Sleep(200)

    def lambda_4AD7():
        OP_97(0x101, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4AD7)
    Sleep(150)

    def lambda_4AF4():
        OP_97(0x102, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4AF4)
    Sleep(150)

    def lambda_4B11():
        OP_97(0x103, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4B11)
    Sleep(150)

    def lambda_4B2E():
        OP_97(0x105, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4B2E)
    Sleep(150)

    def lambda_4B4B():
        OP_97(0x109, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4B4B)
    OP_68(126500, 1300, 0, 2000)
    SetCameraDistance(16500, 2000)
    BeginChrThread(0x20, 1, 0, 53)
    FadeToBright(1000, 0)
    StopBGM(0x7D0)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x104,
        "#5P#00305F......!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x103,
        "#6P#00210F......Agh......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007F#6PWha──!\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7582", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x246), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    StopSound(863, 2000, 100)
    OP_68(146500, 1300, 0, 3000)
    Sleep(2000)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(169500, 900, 11500, 0)
    MoveCamera(65, 15, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    MoveCamera(50, 30, 0, 9000)
    SetCameraDistance(17000, 9000)
    FadeToBright(2000, 0)
    OP_6F(0x79)
    Fade(1000)
    OP_68(170500, 700, 9000, 0)
    MoveCamera(0, 17, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    SetCameraDistance(21000, 4000)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(171160, 900, 8200, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)
    BeginChrThread(0xF, 3, 0, 52)
    OP_68(171200, 900, 7200, 1500)
    OP_0D()
    OP_6F(0x79)

    def lambda_4CFA():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4CFA)
    Sleep(500)

    ChrTalk(
        0x9,
        "#5P#50W#2S...*gwah*...*cough cough*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#50W#2SThe "Red Constellation"...\x01",
            "...Why are you here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#11P#04504FWell, this too is in the contract.\x02\x03",
            "#04502FWe also sent to Aidios the guys who\x01",
            "destroyed the anti-aircraft radars.\x02\x03",
            "Die free from care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P#60W#2S...H-How...regrettable...\x02",
    )

    CloseMessageWindow()

    def lambda_4E44():
        OP_A6(0xFE, 0x0, 0x32, 0x2EE, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4E44)
    Sleep(500)
    Fade(250)
    Sound(514, 0, 100, 0)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x2)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)

    ChrTalk(
        0x11,
        (
            "#11P#04504FShirley.\x01",
            "You can kill the remaining one too.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x11, 500)

    ChrTalk(
        0x12,
        "#04602F#11PEhehe, can I?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "Voice",
        "#2SEek...!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x10, 3, 0, 45)
    OP_68(178800, 1100, 9750, 3000)
    MoveCamera(13, 13, 0, 3000)
    SetCameraDistance(19000, 3000)
    OP_92(0x12, 0x2BA70, 0x1770, 0x1F4)

    def lambda_4F31():
        OP_95(0xFE, 178800, 0, 6000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4F31)
    Sleep(1000)
    BeginChrThread(0x1E, 3, 0, 44)
    WaitChrThread(0x12, 1)

    def lambda_4F58():
        OP_95(0xFE, 178800, 0, 7000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4F58)
    WaitChrThread(0x12, 1)
    OP_6F(0x79)
    SetChrChipByIndex(0x1A, 0x24)
    SetChrSubChip(0x1A, 0x0)
    SetChrPos(0x1A, 170200, 0, 5400, 90)
    SetChrChipByIndex(0x1C, 0x24)
    SetChrSubChip(0x1C, 0x0)
    SetChrPos(0x1C, 171000, 0, 3900, 90)
    Sound(859, 0, 100, 0)
    Sound(802, 0, 100, 0)
    PlayEffect(0x3, 0x0, 0x12, 0x3, 600, 1000, 100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0x12, 0x2)
    SetChrFlags(0x12, 0x10)
    SetChrFlags(0x12, 0x20)
    SetChrChipByIndex(0x12, 0x2D)
    SetChrSubChip(0x12, 0x0)
    Sleep(500)
    StopEffect(0x0, 0x2)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x12,
        (
            "#12P#04611F#3950V#30WUh uh, what's wrong?\x02\x03",
            "#04602F#3951VThe others won't interfere, so why don't \x01",
            "you come at me with all you've got?\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF6F)
    OP_C9(0x1, 0x80000000)

    ChrTalk(
        0x10,
        "#5PU-Uuuh...\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x10, 0x3)
    Sleep(500)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    Sleep(100)
    Sound(531, 0, 100, 0)
    SetChrSubChip(0x10, 0x1)
    Sleep(100)
    SetChrSubChip(0x10, 0x2)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x10,
        "#4S#5PUwaaaah!!!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x11, 3, 0, 42)
    BeginChrThread(0x10, 3, 0, 41)
    BeginChrThread(0x12, 3, 0, 43)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x12, 3)
    Sound(859, 0, 100, 0)
    PlayEffect(0x3, 0x0, 0x12, 0x3, 300, 900, 800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    StopEffect(0x0, 0x2)

    ChrTalk(
        0x10,
        "#12PAh──\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(14000, 500)
    Sleep(200)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0x12, 0x1)
    OP_6F(0x79)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x12,
        (
            "#04609F#3952V#5P#40WUh uh.\x01",
            "It's bye bye then──\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF70)
    OP_57(0x0)
    OP_5A()
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x104,
        "#00310F#2754V#4S#6P#NStooop!!\x02",
    )

    CloseMessageWindow()
    OP_24(0xAC2)
    OP_C9(0x1, 0x80000000)
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(158000, 1100, 2500, 0)
    MoveCamera(43, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15500, 0)
    SetChrChipByIndex(0x1A, 0x24)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x24)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x24)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x24)
    SetChrSubChip(0x1D, 0x0)
    SetChrChipByIndex(0x1E, 0x24)
    SetChrSubChip(0x1E, 0x0)
    SetChrPos(0x1A, 171200, 0, 5400, 0)
    SetChrPos(0x1B, 168400, 0, 4800, 0)
    SetChrPos(0x1C, 172000, 0, 3900, 0)
    SetChrPos(0x1D, 169700, 0, 3700, 0)
    SetChrPos(0x1E, 173200, 0, 5300, 0)

    def lambda_52C9():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_52C9)

    def lambda_52D6():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_52D6)

    def lambda_52E3():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_52E3)

    def lambda_52F0():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_52F0)

    def lambda_52FD():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_52FD)
    SetChrSubChip(0x12, 0x2)
    SetChrPos(0x101, 150000, 0, 2000, 90)
    SetChrPos(0x102, 150000, 0, 4000, 90)
    SetChrPos(0x103, 150000, 0, 3800, 90)
    SetChrPos(0x104, 150000, 0, 2600, 90)
    SetChrPos(0x109, 150000, 0, 5100, 90)
    SetChrPos(0x105, 150000, 0, 4600, 90)
    OP_68(166000, 1100, 4500, 4000)
    MoveCamera(43, 16, 0, 4000)
    SetCameraDistance(16500, 4000)

    def lambda_5399():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_5399)

    def lambda_53A6():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_53A6)
    BeginChrThread(0x104, 3, 0, 46)
    Sleep(600)
    BeginChrThread(0x101, 3, 0, 47)
    Sleep(200)
    BeginChrThread(0x109, 3, 0, 49)

    def lambda_53CB():
        OP_96(0xFE, 0x28E4C, 0x0, 0xA28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_53CB)
    Sleep(400)
    BeginChrThread(0x102, 3, 0, 48)
    Sleep(400)
    BeginChrThread(0x105, 3, 0, 50)
    Sleep(400)
    BeginChrThread(0x103, 3, 0, 51)

    def lambda_5400():
        OP_96(0xFE, 0x29234, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_5400)
    Sleep(1600)

    ChrTalk(
        0x12,
        "#04605F#12PMy, I was interrupted.\x02",
    )

    WaitChrThread(0x103, 3)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x13, 1)

    ChrTalk(
        0x13,
        "#11PYoung master...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x11, 1)

    ChrTalk(
        0x11,
        "#04504F#11PEh eh, took you long enough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00311F#30WUncle... Shirley...\x02\x03",
            "#30W...What the heck...\x01",
            "Are you doin' here...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00108FI-It's no use...\x02",
    )

    CloseMessageWindow()

    def lambda_5510():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5510)
    Sleep(50)

    def lambda_5520():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_5520)

    ChrTalk(
        0x105,
        (
            "#5P#10303F...It looks like\x01",
            "they're all dead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00210F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10110F#12PKh...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x11, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#6P#00015F#30W...What's wrong with you all...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x101,
        "#6P#00007F#4SWhy did you do such a cruel thing!?\x02",
    )

    CloseMessageWindow()

    def lambda_5618():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5618)

    def lambda_5625():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_5625)

    ChrTalk(
        0x11,
        (
            "#04504F#11PDidn't I tell you? It's business.\x02\x03",
            "We executed outrageous terrorists who aimed at\x01",
            "the Empire's Chancellor and royal family lives...\x02\x03",
            "#04502FIt means that this time we accepted a\x01",
            "request from the Imperial government.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00011F......!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)

    def lambda_573D():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_573D)
    Sound(812, 0, 100, 0)
    Sleep(100)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    TurnDirection(0x105, 0x11, 500)

    ChrTalk(
        0x102,
        "#5P#00107FI-Impossible...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#04609F#12PNope, we properly have a letter of\x01",
            "authorization from the Imperial government.\x02\x03",
            "#04611FSince we have this, you can't\x01",
            "touch Shirley and the others, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x109,
        "#10108F#5PN-No way...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00108FAutonomous state law, article 19, paragraph 3...\x02\x03",
            "#00110FPublic power in Crossbell\x01",
            "from the Imperial and Republican\x01",
            "governments is accepted...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#04504FEh eh, exactly.\x02\x03",
            "#04500FIn other words, regarding this matter,\x01",
            "we're Imperial governments proxies...\x02\x03",
            "We're official executioners.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00010FKh......!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#5P#10301FThoroughly prepared, aren't you...?\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x104,
        "#6P#00310F#2755V#4S#10A──Uncleee!!\x02",
    )

    Sleep(500)
    OP_68(167150, 1100, 2600, 1000)
    MoveCamera(34, 19, 0, 1000)
    SetCameraDistance(14000, 1000)

    def lambda_5A29():
        OP_95(0xFE, 166800, 0, 2600, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5A29)
    WaitChrThread(0x104, 1)
    Sound(802, 0, 100, 0)
    Fade(100)
    Sound(811, 0, 100, 0)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x10)
    SetChrFlags(0x104, 0x20)
    SetChrChipByIndex(0x104, 0x30)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x11, 0x2)
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0x11, 0x20)
    SetChrChipByIndex(0x11, 0x31)
    SetChrSubChip(0x11, 0x0)

    def lambda_5A86():

        label("loc_5A86")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_5A86")

    QueueWorkItem2(0x101, 2, lambda_5A86)

    def lambda_5A98():

        label("loc_5A98")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_5A98")

    QueueWorkItem2(0x102, 2, lambda_5A98)

    def lambda_5AAA():

        label("loc_5AAA")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_5AAA")

    QueueWorkItem2(0x103, 2, lambda_5AAA)

    def lambda_5ABC():

        label("loc_5ABC")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_5ABC")

    QueueWorkItem2(0x109, 2, lambda_5ABC)

    def lambda_5ACE():

        label("loc_5ACE")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_5ACE")

    QueueWorkItem2(0x105, 2, lambda_5ACE)

    def lambda_5AE0():

        label("loc_5AE0")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_5AE0")

    QueueWorkItem2(0x13, 2, lambda_5AE0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_6F(0x79)
    OP_C9(0x1, 0x80000000)

    ChrTalk(
        0x104,
        (
            "#6P#00307FWhy did you kill them!?\x01",
            "Why the fuck did you kill them!?\x02\x03",
            "Guys like you could've neutralized\x01",
            "them without killin' them, right!?\x02\x03",
            "So, why did you...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#11P#04501F............\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(13000, 800)
    OP_57(0x0)
    OP_5A()
    Fade(300)
    Sound(802, 0, 100, 0)
    Sound(3824, 255, 100, 0)
    SetChrChipByIndex(0x11, 0x32)
    SetChrSubChip(0x11, 0x0)
    OP_6F(0x79)
    Sleep(150)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sound(534, 0, 100, 0)
    SetChrSubChip(0x11, 0x1)
    Sleep(60)
    Sound(815, 0, 100, 0)
    SetChrSubChip(0x11, 0x2)
    OP_82(0xC8, 0xC8, 0xBB8, 0x12C)
    OP_68(165800, 1100, 2600, 500)
    SetCameraDistance(14500, 500)
    SetChrChipByIndex(0x104, 0x33)
    SetChrSubChip(0x104, 0x2)
    Sound(809, 0, 100, 0)

    def lambda_5CC3():
        OP_9D(0xFE, 0x28104, 0x0, 0x8FC, 0x12C, 0x5DC)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5CC3)
    WaitChrThread(0x104, 1)
    Sound(862, 0, 100, 0)
    CancelBlur(0)
    SetChrChipByIndex(0x1F, 0x33)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, 164400, -50, 2800, 0)
    OP_52(0x1F, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    SetChrSubChip(0x104, 0x0)
    OP_52(0x104, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x104, 0x1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x13, 0x2)

    def lambda_5D75():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5D75)
    Sleep(50)
    Sound(811, 0, 100, 0)
    Sleep(150)
    Sound(2764, 255, 100, 0)

    ChrTalk(
        0x104,
        "#6P#8AGuargh...\x02",
    )

    CloseMessageWindow()

    def lambda_5DB5():
        OP_95(0xFE, 164000, 0, 3900, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5DB5)
    Sleep(100)

    def lambda_5DD2():
        OP_95(0xFE, 162800, 0, 3000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5DD2)
    WaitChrThread(0x101, 1)

    def lambda_5DF0():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5DF0)
    WaitChrThread(0x103, 1)
    TurnDirection(0x103, 0x104, 500)

    ChrTalk(
        0x101,
        "#00007F#5PRandy...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10111FSenior!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5P#00201FMr. Randy...!\x02",
    )

    CloseMessageWindow()
    Sound(802, 0, 100, 0)

    def lambda_5E5B():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5E5B)
    Sleep(500)
    SetChrSubChip(0x104, 0x1)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x11, 0x22)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x2)
    ClearChrFlags(0x11, 0x10)
    ClearChrFlags(0x11, 0x20)
    OP_0D()

    ChrTalk(
        0x11,
        (
            "#04503F#11PDidn't I tell you?  \x01",
            "We contracted an "execution".\x02\x03",
            "#04501FBesides, is it this kind of war of\x01",
            "extermination even rare for you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00310F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#04503F#11PAnd to begin with, if you had\x01",
            "caught these guys immediately,\x01",
            "it wouldn't have ended this way.\x02\x03",
            "#04502F──This result will be used politically\x01",
            "by the "Blood And Iron" too.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6002():
        TurnDirection(0x101, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6002)
    Sleep(50)

    def lambda_6012():
        TurnDirection(0x102, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6012)
    Sleep(50)

    def lambda_6022():
        TurnDirection(0x109, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6022)
    Sleep(50)

    def lambda_6032():
        TurnDirection(0x103, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_6032)
    Sleep(50)

    def lambda_6042():
        TurnDirection(0x105, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6042)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    OP_82(0x32, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0x101,
        "#00007F#5P!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#N#00108FNo...there's no way...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x11,
        (
            "#04504F#11PUh uh, as a minimal compassion\x01",
            "I'm going to overlook one of them.\x02\x03",
            "#04500FShirley, let him go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#04606FEeh, what a waste.\x02\x03",
            "#04600FWell, whatever.\x01",
            "No worth in playing with a smallfry.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(174300, 1100, 7300, 0)
    MoveCamera(47, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18500, 0)
    ClearChrFlags(0x12, 0x2)
    ClearChrFlags(0x12, 0x10)
    ClearChrFlags(0x12, 0x20)
    SetChrChipByIndex(0x12, 0x23)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x10, 177000, 0, 6500, 180)

    def lambda_61F0():

        label("loc_61F0")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_61F0")

    QueueWorkItem2(0x109, 2, lambda_61F0)

    def lambda_6202():

        label("loc_6202")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_6202")

    QueueWorkItem2(0x102, 2, lambda_6202)

    def lambda_6214():

        label("loc_6214")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_6214")

    QueueWorkItem2(0x105, 2, lambda_6214)
    OP_0D()
    OP_68(169300, 1100, 7600, 3500)
    SetCameraDistance(20500, 3500)

    def lambda_6241():
        OP_9E(0xFE, 0x2B368, 0x1C84, 0x15F90, 0x1388, 0x3)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6241)

    def lambda_625C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_625C)
    Sound(802, 0, 100, 0)
    WaitChrThread(0x10, 1)

    def lambda_6273():
        OP_98(0xFE, 0xFFFFE890, 0x0, 0x12C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6273)

    def lambda_628D():
        OP_98(0xFE, 0xFFFFE890, 0x0, 0x12C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_628D)
    WaitChrThread(0x10, 1)
    WaitChrThread(0x12, 1)
    OP_52(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0x10, 0x12, 0)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    Sound(809, 0, 100, 0)
    Sound(811, 0, 100, 0)

    def lambda_62D5():
        OP_9D(0xFE, 0x28AC8, 0x0, 0x1E14, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_62D5)
    WaitChrThread(0x10, 1)
    Sound(862, 0, 80, 0)
    OP_82(0x64, 0x64, 0xBB8, 0x12C)
    OP_93(0x10, 0x10E, 0x0)
    SetChrChipByIndex(0x10, 0x28)
    SetChrSubChip(0x10, 0x3)
    OP_52(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x578), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x578), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)

    ChrTalk(
        0x12,
        (
            "#11P#04612FHere, he's yours.\x01",
            "Don't run away, ok?\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x10, 0x2)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0x10, 0x20)
    SetChrChipByIndex(0x10, 0x34)
    SetChrSubChip(0x10, 0x0)

    def lambda_638D():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_638D)

    ChrTalk(
        0x10,
        "#5PE-Eeeek...\x02",
    )

    CloseMessageWindow()

    def lambda_63B9():
        OP_96(0xFE, 0x288D4, 0x0, 0x1964, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_63B9)
    WaitChrThread(0x109, 1)

    def lambda_63D7():
        OP_96(0xFE, 0x28EB0, 0x0, 0x1D4C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_63D7)
    WaitChrThread(0x109, 1)

    def lambda_63F5():

        label("loc_63F5")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_63F5")

    QueueWorkItem2(0x109, 2, lambda_63F5)

    ChrTalk(
        0x109,
        "#6P#10110FKh...\x02",
    )

    CloseMessageWindow()
    OP_68(165800, 1500, 2600, 2000)
    MoveCamera(34, 19, 0, 2000)
    OP_6E(650, 2000)
    SetCameraDistance(14500, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00013F#6P............\x02",
    )

    CloseMessageWindow()
    OP_93(0x11, 0x2D, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x11,
        (
            "#6P#04504FWell then, let's pull out.\x02\x03",
            "#04512FWe got our reward too, so\x01",
            "tonight we'll have a blast.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_64DA():
        TurnDirection(0x13, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_64DA)
    Sleep(50)

    def lambda_64EA():
        TurnDirection(0x1A, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_64EA)
    Sleep(50)

    def lambda_64FA():
        TurnDirection(0x1B, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_64FA)
    Sleep(50)

    def lambda_650A():
        TurnDirection(0x1C, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_650A)
    Sleep(50)

    def lambda_651A():
        TurnDirection(0x1D, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_651A)
    Sleep(50)

    def lambda_652A():
        TurnDirection(0x1E, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_652A)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x1A, 0)
    WaitChrThread(0x1B, 0)
    WaitChrThread(0x1C, 0)
    WaitChrThread(0x1D, 0)
    WaitChrThread(0x1E, 0)
    Sleep(100)
    SetMessageWindowPos(300, 40, -1, -1)
    SetChrName("Jaegers")
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    AnonymousTalk(
        0xFF,
        "#4SJaー!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x12,
        "#11P#N#04609FThen, see you lateeer!\x02",
    )

    CloseMessageWindow()
    OP_93(0x13, 0x10E, 0x1F4)

    ChrTalk(
        0x13,
        "#11PExcuse us, young master.\x02",
    )

    CloseMessageWindow()
    OP_93(0x1B, 0x10E, 0x1F4)

    NpcTalk(
        0x1B,
        "Jaeger Sachs",
        (
            "#11PSee ya,\x01",
            "Captain Randolph.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6618():

        label("loc_6618")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_6618")

    QueueWorkItem2(0x101, 2, lambda_6618)

    def lambda_662A():

        label("loc_662A")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_662A")

    QueueWorkItem2(0x102, 2, lambda_662A)

    def lambda_663C():

        label("loc_663C")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_663C")

    QueueWorkItem2(0x103, 2, lambda_663C)

    def lambda_664E():

        label("loc_664E")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_664E")

    QueueWorkItem2(0x105, 2, lambda_664E)
    OP_93(0x11, 0xB4, 0x1F4)
    OP_68(165800, 1500, -400, 5000)
    MoveCamera(23, 13, 0, 5000)

    def lambda_6683():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6683)
    Sleep(1300)

    def lambda_66A0():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_66A0)

    def lambda_66BA():
        OP_97(0x1A, 0x0, 0x0, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_66BA)
    Sleep(100)

    def lambda_66D7():
        OP_97(0x1B, 0x0, 0x0, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_66D7)
    Sleep(100)

    def lambda_66F4():
        OP_97(0x1C, 0x0, 0x0, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_66F4)
    Sleep(100)

    def lambda_6711():
        OP_97(0x1D, 0x0, 0x0, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_6711)
    Sleep(100)

    def lambda_672E():
        OP_97(0x1E, 0x0, 0x0, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_672E)

    def lambda_6748():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6748)
    WaitChrThread(0x11, 1)
    WaitChrThread(0x13, 1)
    WaitChrThread(0x12, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    OP_68(164100, 1000, 2300, 2000)
    MoveCamera(23, 23, 0, 2000)
    SetCameraDistance(14000, 2000)
    Sleep(1750)

    def lambda_67D2():
        OP_A6(0xFE, 0x0, 0x32, 0x4E2, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_67D2)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x104, 0x36)
    SetChrSubChip(0x104, 0x3)
    SetChrFlags(0x104, 0x1)
    OP_52(0x104, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x1F, 0x80)
    OP_0D()
    Sleep(500)
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x104, 0x35)
    SetChrSubChip(0x104, 0x0)

    def lambda_6827():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6827)
    OP_0D()
    Sleep(800)

    ChrTalk(
        0x104,
        (
            "#5P#00313F#60W...Don't screw with me...\x01",
            "...For what...did I...\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 2)
    SetChrSubChip(0x104, 0x1)
    SetCameraDistance(50000, 4000)
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0xBB8)
    OP_C9(0x0, 0x80000000)
    Sound(4117, 255, 100, 0)

    ChrTalk(
        0x104,
        "#5P#5S#20A#40WOOOOOOOOH!!!!\x02",
    )

    Sleep(1000)
    OP_C9(0x1, 0x80000000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x104, 0x2)
    ClearChrFlags(0x104, 0x10)
    ClearChrFlags(0x104, 0x20)
    OP_24(0x35C)
    OP_24(0x35D)
    Sleep(1000)
    SetScenarioFlags(0x22, 1)
    NewScene("m0200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_40_4504 end

    def Function_41_6915(): pass

    label("Function_41_6915")

    OP_82(0x64, 0x64, 0xBB8, 0x384)

    def lambda_692B():
        OP_A6(0xFE, 0x0, 0x1E, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_692B)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_68(178300, 1100, 5650, 1300)
    MoveCamera(13, 13, -15, 1300)
    SetCameraDistance(19500, 1300)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)

    def lambda_6B7B():
        OP_95(0xFE, 178800, 0, 8500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6B7B)
    WaitChrThread(0x10, 1)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    Sleep(100)
    SetChrSubChip(0x10, 0x1)
    Sleep(100)
    SetChrSubChip(0x10, 0x2)
    Sleep(100)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)

    def lambda_6BC3():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6BC3)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)

    def lambda_6D06():
        OP_95(0xFE, 177200, 0, 6600, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6D06)
    WaitChrThread(0x10, 1)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    Sleep(100)
    SetChrSubChip(0x10, 0x1)
    Sleep(100)
    SetChrSubChip(0x10, 0x2)
    Sleep(100)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)

    def lambda_6D4E():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6D4E)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrFlags(0xFE, 0x20)
    OP_93(0x10, 0xA0, 0x12C)
    ClearChrFlags(0xFE, 0x20)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)

    def lambda_6EAB():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6EAB)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Return()

    # Function_41_6915 end

    def Function_42_6FE2(): pass

    label("Function_42_6FE2")

    Sleep(100)
    Sound(860, 2, 100, 0)
    Sound(861, 2, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 178800, 0, 7000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 178100, 0, 7500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 179200, 0, 7900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 178600, 0, 7200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopSound(860, 500, 100)
    StopSound(861, 500, 100)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 178200, 0, 6800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1300)
    Sound(860, 2, 100, 0)
    Sound(861, 2, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 179000, 0, 3000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 178500, 0, 3700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 178800, 0, 3200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopSound(860, 500, 100)
    StopSound(861, 500, 100)
    Sleep(800)
    Sound(860, 2, 100, 0)
    Sound(861, 2, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 174500, 0, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 175300, 0, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 175000, 0, 2300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 176600, 0, 1300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 177800, 0, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 178800, 0, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 178300, 0, 900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopSound(860, 500, 100)
    StopSound(861, 500, 100)
    Return()

    # Function_42_6FE2 end

    def Function_43_7391(): pass

    label("Function_43_7391")

    SetCameraDistance(20500, 500)
    ClearChrFlags(0x12, 0x2)
    ClearChrFlags(0x12, 0x10)
    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    SetChrChipByIndex(0x12, 0x2E)
    SetChrSubChip(0x12, 0x3)
    Sound(844, 0, 100, 0)

    def lambda_73BF():
        OP_9D(0xFE, 0x2BA70, 0x0, 0xC80, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_73BF)
    WaitChrThread(0x12, 1)
    SetChrSubChip(0x12, 0x1)
    Sleep(100)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrSubChip(0x12, 0x0)
    Sleep(1500)
    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    SetChrSubChip(0x12, 0x3)

    def lambda_7402():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_7402)
    Sound(844, 0, 100, 0)

    def lambda_7415():
        OP_9D(0xFE, 0x2A9A4, 0x0, 0x5DC, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7415)
    WaitChrThread(0x12, 1)
    SetChrSubChip(0x12, 0x1)
    Sleep(200)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrSubChip(0x12, 0x0)
    Sleep(500)
    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    SetChrSubChip(0x12, 0x3)

    def lambda_7458():
        OP_93(0xFE, 0x154, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_7458)
    Sound(844, 0, 100, 0)

    def lambda_746B():
        OP_9D(0xFE, 0x2BA70, 0x0, 0x1F4, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_746B)
    WaitChrThread(0x12, 1)
    SetChrSubChip(0x12, 0x1)
    Sleep(100)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrSubChip(0x12, 0x0)
    Sleep(300)
    OP_68(177000, 1100, 7100, 1000)
    MoveCamera(27, 13, 5, 1000)
    SetCameraDistance(14500, 1000)
    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    SetChrSubChip(0x12, 0x2)
    Sound(844, 0, 100, 0)

    def lambda_74D9():
        OP_9D(0xFE, 0x2B368, 0x0, 0x1C84, 0xDAC, 0xFA0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_74D9)
    Sleep(400)
    Sound(326, 0, 100, 0)
    OP_93(0x12, 0xA0, 0x0)
    SetChrSubChip(0x12, 0x3)
    WaitChrThread(0x12, 1)
    Sound(326, 0, 100, 0)
    SetChrSubChip(0x12, 0x1)
    Sleep(100)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrFlags(0x12, 0x2)
    SetChrFlags(0x12, 0x10)
    SetChrFlags(0x12, 0x20)
    SetChrChipByIndex(0x12, 0x2F)
    SetChrSubChip(0x12, 0x0)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_0D()
    Return()

    # Function_43_7391 end

    def Function_44_754D(): pass

    label("Function_44_754D")

    SetChrChipByIndex(0x1E, 0x24)
    SetChrSubChip(0x1E, 0x0)
    OP_93(0x1E, 0x5A, 0x1F4)

    def lambda_7561():
        OP_96(0xFE, 0x29B94, 0x0, 0x1CE8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_7561)
    WaitChrThread(0x1E, 1)
    Return()

    # Function_44_754D end

    def Function_45_757B(): pass

    label("Function_45_757B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_75A7")

    def lambda_758B():
        OP_A6(0xFE, 0x0, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_758B)
    Sleep(500)
    Jump("Function_45_757B")

    label("loc_75A7")

    Return()

    # Function_45_757B end

    def Function_46_75A8(): pass

    label("Function_46_75A8")


    def lambda_75AD():
        OP_95(0xFE, 162900, 0, 2600, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_75AD)
    WaitChrThread(0x104, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_46_75A8 end

    def Function_47_75CE(): pass

    label("Function_47_75CE")


    def lambda_75D3():
        OP_95(0xFE, 160000, 0, 2000, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_75D3)
    WaitChrThread(0x101, 1)

    def lambda_75F1():
        OP_95(0xFE, 162900, 0, 4800, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_75F1)
    WaitChrThread(0x101, 1)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_47_75CE end

    def Function_48_7612(): pass

    label("Function_48_7612")


    def lambda_7617():
        OP_95(0xFE, 160000, 0, 4000, 4500, 0x1)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7617)
    WaitChrThread(0x102, 1)

    def lambda_7635():
        OP_95(0xFE, 166600, 0, 9900, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7635)
    WaitChrThread(0x102, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    SetChrChipByIndex(0x102, 0x29)
    SetChrSubChip(0x102, 0x0)
    Sound(812, 0, 100, 0)
    Return()

    # Function_48_7612 end

    def Function_49_7664(): pass

    label("Function_49_7664")


    def lambda_7669():
        OP_95(0xFE, 159000, 0, 5100, 4500, 0x1)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7669)
    WaitChrThread(0x109, 1)

    def lambda_7687():
        OP_95(0xFE, 165300, 0, 7100, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7687)
    WaitChrThread(0x109, 1)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_49_7664 end

    def Function_50_76A8(): pass

    label("Function_50_76A8")


    def lambda_76AD():
        OP_95(0xFE, 159000, 0, 4600, 4500, 0x1)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_76AD)
    WaitChrThread(0x105, 1)

    def lambda_76CB():
        OP_95(0xFE, 165600, 0, 11400, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_76CB)
    WaitChrThread(0x105, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    SetChrChipByIndex(0x105, 0x2A)
    SetChrSubChip(0x105, 0x0)
    Sound(812, 0, 100, 0)
    Return()

    # Function_50_76A8 end

    def Function_51_76FA(): pass

    label("Function_51_76FA")


    def lambda_76FF():
        OP_95(0xFE, 157000, 0, 3800, 4500, 0x1)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_76FF)
    WaitChrThread(0x103, 1)

    def lambda_771D():
        OP_95(0xFE, 161800, 0, 6100, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_771D)
    WaitChrThread(0x103, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_51_76FA end

    def Function_52_773E(): pass

    label("Function_52_773E")

    Sleep(1000)
    StopEffect(0x0, 0x2)
    Sleep(1000)
    StopEffect(0x2, 0x2)
    Sleep(1000)
    StopEffect(0x4, 0x2)
    Sleep(1000)
    StopEffect(0x1, 0x2)
    Sleep(1000)
    StopEffect(0x3, 0x2)
    Return()

    # Function_52_773E end

    def Function_53_775D(): pass

    label("Function_53_775D")

    StopSound(864, 2000, 50)
    OP_25(0x35F, 0x3C)
    Sleep(100)
    OP_25(0x35F, 0x46)
    Sleep(100)
    OP_25(0x35F, 0x50)
    Sleep(100)
    OP_25(0x35F, 0x5A)
    Sleep(100)
    OP_25(0x35F, 0x64)
    Return()

    # Function_53_775D end

    def Function_54_7784(): pass

    label("Function_54_7784")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21C, 7)), scpexpr(EXPR_END)), "loc_778E")
    Return()

    label("loc_778E")

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
        (1, "loc_786A"),
        (SWITCH_DEFAULT, "loc_7883"),
    )


    label("loc_786A")

    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, 4970, 0, 0, 90)
    EventEnd(0x5)
    Return()

    label("loc_7883")

    Battle("BattleInfo_660", 0x0, 0x0, 0x100, 0xC, 0xFF)
    OP_E2(0x2)
    EventBegin(0x1)
    OP_68(4970, 1000, 0, 0)
    OP_90(0x0, 4970, 0, 0, 90)
    OP_90(0x1, 4970, 0, 0, 90)
    OP_90(0x2, 4970, 0, 0, 90)
    OP_90(0x3, 4970, 0, 0, 90)
    OP_90(0x4, 4970, 0, 0, 90)
    OP_90(0x5, 4970, 0, 0, 90)
    OP_90(0x6, 4970, 0, 0, 90)
    OP_90(0x7, 4970, 0, 0, 90)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_7945"),
        (1, "loc_794A"),
        (SWITCH_DEFAULT, "loc_794D"),
    )


    label("loc_7945")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    label("loc_794A")

    OP_B9(0x0)
    Return()

    label("loc_794D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(510, 0, 870, 0)
    MoveCamera(44, 39, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13070, 0)
    SetChrFlags(0x21, 0x80)
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
            scpstr(SCPSTR_CODE_ITEM, 0x11),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddItemNumber(0x11, 1)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 2500, 0, 0, 270)
    SetChrPos(0x102, -2500, 0, 0, 90)
    SetChrPos(0x103, -1200, 0, -1700, 45)
    SetChrPos(0x104, 1200, 0, -1700, 0)
    SetChrPos(0x109, -1200, 0, 1700, 180)
    SetChrPos(0x105, 1200, 0, 1700, 180)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#00000FA Craft Book...\x01",
            "It looks one that Tio and Wazy could handle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FMr. Wazy, is it fine with you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FYeah, let's try it now.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(517, 0, 100, 0)
    AddCraft(0x2, 0x191)
    AddCraft(0x4, 0x191)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Tio and Wazy have learned the\x01\x07\x02",
            ""Sigma Ascension"\x07\x05",
            " Combi Craft.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "By each expending 100 CP, a powerful\x01",
            "combination attack can be unleashed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x21C, 7)
    OP_29(0x8C, 0x4, 0x10)
    OP_29(0x8C, 0x4, 0x2)
    OP_29(0x8C, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_E2(0x2)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_54_7784 end

    def Function_55_7C12(): pass

    label("Function_55_7C12")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It appears the orbal energy is down.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x194, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DCA")

    ChrTalk(
        0x101,
        (
            "#00003FIt looks like we can't\x01",
            "advance further than this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIt appears that following the Trade\x01",
            "Conference terrorist incident, a part of\x01",
            "the routes in the city have been sealed.\x02\x03",
            "#00203FI feel it's a proper\x01",
            "or natural decision.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FWell, it's not that we have special\x01",
            "business this further inside, so\x01",
            "should we retrace our steps quietly?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x194, 4)

    label("loc_7DCA")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_55_7C12 end

    SaveToFile()

Try(main)
