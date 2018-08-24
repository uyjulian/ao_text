﻿from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1400.bin",                # FileName
        "t1400",                    # MapName
        "t1400",                    # Location
        0x00BB,                     # MapIndex
        "ed7160",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, -30000, 0, 0, 1, 187, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1400",                  # 0
        "Elie",                   # 1
        "Randy",                  # 2
        "Noｱl",                  # 3
        "Wazy",                   # 4
        "KeA",                    # 5
        "Fran",                   # 6
        "Cecil",                  # 7
        "Ilya",                   # 8
        "Rixia",                  # 9
        "Sully",                  # 10
        "Michey",                 # 11
        "Melson",                 # 12
        "Corona",                 # 13
        "Rimah",                  # 14
        "MWL Staff",              # 15
        "Tourist",                # 16
        "Tourist",                # 17
        "Tourist",                # 18
        "Tourist",                # 19
        "Tourist",                # 20
        "Cryptid",                # 21
        "Miichie",                # 22
        "Boy",                    # 23
        "Boy",                    # 24
        "SE制御",                 # 25
        "bt1450",                 # 26
        "To Wonderland Entrance", # 27
    ))

    ATBonus("ATBonus_490", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_550", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_554", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_558", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_55C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_560", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_564", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_568", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_56C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_530", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_534", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_538", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_53C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_540", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_544", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_548", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_54C", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_570", 0x0042, 255, 6, 45, 3, 3, 30, 0, "bt1450", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88101.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_550", "MonsterBattlePostion_530", "ed7454", "ed7000", "ATBonus_490"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00100.itc",                   # 00
        "chr/ch00300.itc",                   # 01
        "chr/ch02900.itc",                   # 02
        "chr/ch03000.itc",                   # 03
        "chr/ch08200.itc",                   # 04
        "chr/ch08500.itc",                   # 05
        "chr/ch07500.itc",                   # 06
        "chr/ch05100.itc",                   # 07
        "chr/ch05200.itc",                   # 08
        "chr/ch10100.itc",                   # 09
        "chr/ch10200.itc",                   # 0A
        "chr/ch26200.itc",                   # 0B
        "chr/ch22700.itc",                   # 0C
        "chr/ch20700.itc",                   # 0D
        "chr/ch44500.itc",                   # 0E
        "chr/ch27600.itc",                   # 0F
        "chr/ch20300.itc",                   # 10
        "chr/ch22300.itc",                   # 11
        "chr/ch33100.itc",                   # 12
        "chr/ch33300.itc",                   # 13
        "chr/ch45400.itc",                   # 14
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

    DeclNpc(1309,    2329,    4294899866, 0,    389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(1309,    2329,    4294899866, 0,    389,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(2109,    2319,    4294899987, 0,    389,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(2609,    2220,    4294901176, 222,  389,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(1309,    2329,    4294899866, 0,    389,  0x0, 0,   4,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(1679,    2299,    4294900237, 42,   389,  0x0, 0,   5,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(2549,    2309,    4294900057, 312,  389,  0x0, 0,   6,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(1200,    2289,    4294900286, 42,   389,  0x0, 0,   7,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(2109,    2319,    4294899987, 0,    389,  0x0, 0,   8,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(2109,    2319,    4294899987, 0,    389,  0x0, 0,   9,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(2240,    2200,    4294901447, 222,  389,  0x0, 0,   10,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(4294965546, 0,       4294940106, 231,  389,  0x0, 0,   11,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(4294964546, 0,       4294939536, 90,   389,  0x0, 0,   12,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(4294965487, 9,       4294938786, 336,  389,  0x0, 0,   13,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(0,       1600,    4294944147, 180,  389,  0x0, 0,   14,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(4294964967, 6010,    4294876877, 0,    389,  0x0, 0,   15,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(4294964527, 5590,    4294878686, 148,  389,  0x0, 0,   16,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(4294966027, 5690,    4294878227, 234,  389,  0x0, 0,   17,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(889,     509,     4294922227, 270,  389,  0x0, 0,   18,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(4294967187, 509,     4294922227, 90,   389,  0x0, 0,   19,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(5420,    9,       4294945346, 180,  389,  0x0, 0,   20,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 27,  0.0,                   -71.0,                 1.7000000476837158,    625.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  14.199999809265137,    -0.3400000035762787,   1.0])

    DeclActor(3680,    1460,    4294944676, 1000,    5420,    1500,    4294945346, 0x007E, 0,  36, 0x0000)

    PlaceName(-0.05999999865889549, 0.0, -140.4499969482422, 0x0000, 0x0000, "To Wonderland Entrance")

    ChipFrameInfo(1620, 0)                                       # 0

    ScpFunction((
        "Function_0_654",          # 00, 0
        "Function_1_70C",          # 01, 1
        "Function_2_7A7",          # 02, 2
        "Function_3_94F",          # 03, 3
        "Function_4_A54",          # 04, 4
        "Function_5_C32",          # 05, 5
        "Function_6_D53",          # 06, 6
        "Function_7_E64",          # 07, 7
        "Function_8_F77",          # 08, 8
        "Function_9_101E",         # 09, 9
        "Function_10_10B2",        # 0A, 10
        "Function_11_116B",        # 0B, 11
        "Function_12_12EB",        # 0C, 12
        "Function_13_1408",        # 0D, 13
        "Function_14_14DC",        # 0E, 14
        "Function_15_1743",        # 0F, 15
        "Function_16_1813",        # 10, 16
        "Function_17_1904",        # 11, 17
        "Function_18_19E4",        # 12, 18
        "Function_19_1AD1",        # 13, 19
        "Function_20_1BB9",        # 14, 20
        "Function_21_1CEE",        # 15, 21
        "Function_22_1D5C",        # 16, 22
        "Function_23_1DC2",        # 17, 23
        "Function_24_1E1B",        # 18, 24
        "Function_25_1EE3",        # 19, 25
        "Function_26_1FC7",        # 1A, 26
        "Function_27_2133",        # 1B, 27
        "Function_28_29D9",        # 1C, 28
        "Function_29_29FE",        # 1D, 29
        "Function_30_2AA9",        # 1E, 30
        "Function_31_2AC9",        # 1F, 31
        "Function_32_2D93",        # 20, 32
        "Function_33_2DB7",        # 21, 33
        "Function_34_3694",        # 22, 34
        "Function_35_3F6C",        # 23, 35
        "Function_36_3FAC",        # 24, 36
        "Function_37_4DAE",        # 25, 37
        "Function_38_6016",        # 26, 38
        "Function_39_6051",        # 27, 39
    ))


    def Function_0_654(): pass

    label("Function_0_654")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_694"),
        (1, "loc_6A0"),
        (2, "loc_6AC"),
        (3, "loc_6B8"),
        (4, "loc_6C4"),
        (5, "loc_6D0"),
        (6, "loc_6DC"),
        (SWITCH_DEFAULT, "loc_6E8"),
    )


    label("loc_694")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6A0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6AC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6B8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6C4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6D0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6DC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6E8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6F4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_70B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_70B")

    Return()

    # Function_0_654 end

    def Function_1_70C(): pass

    label("Function_1_70C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_71A")
    Jump("loc_788")

    label("loc_71A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_728")
    Jump("loc_788")

    label("loc_728")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_736")
    Jump("loc_788")

    label("loc_736")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_747")
    Call(0, 26)
    Jump("loc_788")

    label("loc_747")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_755")
    Jump("loc_788")

    label("loc_755")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_763")
    Jump("loc_788")

    label("loc_763")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_771")
    Jump("loc_788")

    label("loc_771")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_77F")
    Jump("loc_788")

    label("loc_77F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_788")

    label("loc_788")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_797")
    ClearScenarioFlags(0x22, 0)
    Event(0, 37)

    label("loc_797")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_7A6")
    ClearScenarioFlags(0x22, 1)
    Event(0, 34)

    label("loc_7A6")

    Return()

    # Function_1_70C end

    def Function_2_7A7(): pass

    label("Function_2_7A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7B9")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D8")
    OP_24(0x335)
    SoundLoad(918)
    BeginChrThread(0x20, 3, 0, 39)
    Jump("loc_7EF")

    label("loc_7D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_7E9")
    OP_24(0x335)
    Jump("loc_7EF")

    label("loc_7E9")

    Sound(821, 1, 50, 0)

    label("loc_7EF")

    Sound(126, 1, 80, 0)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_80D")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_80D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83A")
    SetMapObjFrame(0xFF, "water", 0x2, "loop_off")
    SetMapObjFrame(0xFF, "main", 0x2, "loop_off")

    label("loc_83A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_89B")
    SetMapObjFrame(0xFF, "sky01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky_y", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky01_y", 0x1, 0x1)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD5, 0x8F, 0x7B, 0x26, 0x1F4, 0x0)
    Jump("loc_8C4")

    label("loc_89B")

    SetMapObjFrame(0xFF, "sky01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky_y", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky01_y", 0x0, 0x1)

    label("loc_8C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8EB")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x14, 0x12C, 0x0)
    Jump("loc_90D")

    label("loc_8EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_90D")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x14, 0x12C, 0x0)

    label("loc_90D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_921")
    ClearMapObjFlags(0x0, 0x10)

    label("loc_921")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_94E")
    OP_66(0x0, 0x1)

    label("loc_94E")

    Return()

    # Function_2_7A7 end

    def Function_3_94F(): pass

    label("Function_3_94F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_968")
    Jump("loc_A50")

    label("loc_968")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97E")
    Jump("loc_A50")

    label("loc_97E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_994")
    Jump("loc_A50")

    label("loc_994")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3F")

    ChrTalk(
        0x8,
        (
            "#00100FI heard the pretty sound\x01",
            "of a bell coming from\x01",
            "the castle earlier.\x02\x03",
            "#00109F*giggle*, I think some\x01",
            "couple is making a wish\x01",
            "to the mirror.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A50")

    label("loc_A3F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A50")

    label("loc_A50")

    TalkEnd(0xFE)
    Return()

    # Function_3_94F end

    def Function_4_A54(): pass

    label("Function_4_A54")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A6D")
    Jump("loc_C2E")

    label("loc_A6D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A83")
    Jump("loc_C2E")

    label("loc_A83")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A99")
    Jump("loc_C2E")

    label("loc_A99")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AAF")
    Jump("loc_C2E")

    label("loc_AAF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B77")

    ChrTalk(
        0x9,
        (
            "#00302FIt seems Mirror Castle is lit up\x01",
            "at night, too.\x02\x03",
            "#00304FTogether with the fireworks and\x01",
            "parade, it really feels like the\x01",
            "closin' of one day at the park.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C2E")

    label("loc_B77")


    ChrTalk(
        0x9,
        (
            "#00302FSince I don't come here often, I\x01",
            "wanted to see the night operations\x01",
            "with a beautiful lady, but...\x02\x03",
            "#00306FWell, we've got the dinner party,\x01",
            "so I guess it can't be helped.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C2E")

    TalkEnd(0xFE)
    Return()

    # Function_4_A54 end

    def Function_5_C32(): pass

    label("Function_5_C32")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C4B")
    Jump("loc_D4F")

    label("loc_C4B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C61")
    Jump("loc_D4F")

    label("loc_C61")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C77")
    Jump("loc_D4F")

    label("loc_C77")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D3E")

    ChrTalk(
        0xA,
        (
            "#10103FRumors of a "Wish-Granting\x01",
            "Mirror"... Will our wishes\x01",
            "really come true?\x02\x03",
            "#10100FI'm really looking forward\x01",
            "to it, since they say "where\x01",
            "there's smoke there's fire".\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D4F")

    label("loc_D3E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D4F")

    label("loc_D4F")

    TalkEnd(0xFE)
    Return()

    # Function_5_C32 end

    def Function_6_D53(): pass

    label("Function_6_D53")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D6C")
    Jump("loc_E60")

    label("loc_D6C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D82")
    Jump("loc_E60")

    label("loc_D82")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DA5")
    Call(0, 7)
    Jump("loc_E34")

    label("loc_DA5")


    ChrTalk(
        0xB,
        (
            "#10302FIf you don't believe it's\x01",
            "not fun... huh? Hehe,\x01",
            "that's really how it is.\x02\x03",
            "#10304FWell, I think I'll have a\x01",
            "fair bit of fun myself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E34")

    Jump("loc_E60")

    label("loc_E39")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E4F")
    Jump("loc_E60")

    label("loc_E4F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E60")

    label("loc_E60")

    TalkEnd(0xFE)
    Return()

    # Function_6_D53 end

    def Function_7_E64(): pass

    label("Function_7_E64")

    OP_4B(0xB, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xB,
        (
            "#10300FA "Wish-Granting\x01",
            "Mirror"...\x02\x03",
            "#10302FDo you think our wishes\x01",
            "will really come true?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#06409FOf course!\x02\x03",
            "#06400FAfter all, if you don't\x01",
            "believe it, this\x01",
            "attraction's no fun, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#10300FHehe, I see. That's\x01",
            "really how it is.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_7_E64 end

    def Function_8_F77(): pass

    label("Function_8_F77")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F9D")
    Call(0, 9)
    Jump("loc_FC2")

    label("loc_F9D")


    ChrTalk(
        0xC,
        "#01109FMirror Castle is huuuge!\x02",
    )

    CloseMessageWindow()

    label("loc_FC2")

    Jump("loc_101A")

    label("loc_FC7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FDD")
    Jump("loc_101A")

    label("loc_FDD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FF3")
    Jump("loc_101A")

    label("loc_FF3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1009")
    Jump("loc_101A")

    label("loc_1009")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_101A")

    label("loc_101A")

    TalkEnd(0xFE)
    Return()

    # Function_8_F77 end

    def Function_9_101E(): pass

    label("Function_9_101E")

    OP_4B(0xC, 0xFF)
    OP_4B(0x11, 0xFF)

    ChrTalk(
        0xC,
        (
            "#01109FWoooow... Mirror Castle\x01",
            "is huuuge!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#14005FYeah... It's totally\x01",
            "different, seeing it\x01",
            "from up close...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0x11, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0x11, 0xFF)
    Return()

    # Function_9_101E end

    def Function_10_10B2(): pass

    label("Function_10_10B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10CB")
    Jump("loc_1167")

    label("loc_10CB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10E1")
    Jump("loc_1167")

    label("loc_10E1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1140")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1104")
    Call(0, 7)
    Jump("loc_113B")

    label("loc_1104")


    ChrTalk(
        0xD,
        (
            "#06409FThe theme park\x01",
            "attractions are really\x01",
            "fun!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_113B")

    Jump("loc_1167")

    label("loc_1140")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1156")
    Jump("loc_1167")

    label("loc_1156")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1167")

    label("loc_1167")

    TalkEnd(0xFE)
    Return()

    # Function_10_10B2 end

    def Function_11_116B(): pass

    label("Function_11_116B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1184")
    Jump("loc_12E7")

    label("loc_1184")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_124D")

    ChrTalk(
        0xE,
        (
            "#05900FHehe. Ilya the big star together\x01",
            "with the popular Mishy... It's\x01",
            "quite the unusual sight.\x02\x03",
            "#05909FI think it might be an amazing\x01",
            "two-shot for some reason.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_12A5")

    label("loc_124D")


    ChrTalk(
        0xE,
        (
            "#05909FMishy and Ilya together\x01",
            "might make for an amazing\x01",
            "two shot for some reason.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12A5")

    Jump("loc_12E7")

    label("loc_12AA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12C0")
    Jump("loc_12E7")

    label("loc_12C0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12D6")
    Jump("loc_12E7")

    label("loc_12D6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12E7")

    label("loc_12E7")

    TalkEnd(0xFE)
    Return()

    # Function_11_116B end

    def Function_12_12EB(): pass

    label("Function_12_12EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1304")
    Jump("loc_1404")

    label("loc_1304")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1327")
    Call(0, 13)
    Jump("loc_13C2")

    label("loc_1327")


    ChrTalk(
        0xF,
        (
            "#01705FOh, if we stay together for\x01",
            "too long, it seems people\x01",
            "will come gathering.\x02\x03",
            "#01702FI'll excuse myself here,\x01",
            "because I came with friends\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13C2")

    Jump("loc_1404")

    label("loc_13C7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13DD")
    Jump("loc_1404")

    label("loc_13DD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13F3")
    Jump("loc_1404")

    label("loc_13F3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1404")

    label("loc_1404")

    TalkEnd(0xFE)
    Return()

    # Function_12_12EB end

    def Function_13_1408(): pass

    label("Function_13_1408")

    OP_4B(0xF, 0xFF)
    OP_4B(0x12, 0xFF)

    ChrTalk(
        0x12,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Ah, could you be... Ilya\x01",
            "from Arc-en-Ciel?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi, I've always\x01",
            "cheered for you!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01700FHehe. I see you in the\x01",
            "city quite a bit myself.\x02\x03",
            "#01709FLet's both do our best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    OP_4C(0xF, 0xFF)
    OP_4C(0x12, 0xFF)
    Return()

    # Function_13_1408 end

    def Function_14_14DC(): pass

    label("Function_14_14DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14F5")
    Jump("loc_173F")

    label("loc_14F5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_150B")
    Jump("loc_173F")

    label("loc_150B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1521")
    Jump("loc_173F")

    label("loc_1521")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1537")
    Jump("loc_173F")

    label("loc_1537")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_173F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_166D")

    ChrTalk(
        0x10,
        (
            "#01802FThe area around here fills up with couples\x01",
            "when night comes.\x02\x03",
            "#01804FI heard there'll be a full moon tonight...\x01",
            "It'll be a very pretty scene with the\x01",
            "moonlight reflecting on the lake.\x02\x03",
            "#01809FHaha. Just imagining it puts you into a\x01",
            "romantic mood for some reason.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_173F")

    label("loc_166D")


    ChrTalk(
        0x10,
        (
            "#01802FI heard there'll be a full moon tonight...\x01",
            "It should be a very pretty scene with the\x01",
            "moonlight reflecting on the lake.\x02\x03",
            "#01809FHaha. Just imagining it puts you into a\x01",
            "romantic mood for some reason.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_173F")

    TalkEnd(0xFE)
    Return()

    # Function_14_14DC end

    def Function_15_1743(): pass

    label("Function_15_1743")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1769")
    Call(0, 9)
    Jump("loc_17B7")

    label("loc_1769")


    ChrTalk(
        0x11,
        (
            "#14005FIt's this big from up\x01",
            "close, huh... I feel\x01",
            "dizzy for some reason.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17B7")

    Jump("loc_180F")

    label("loc_17BC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17D2")
    Jump("loc_180F")

    label("loc_17D2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17E8")
    Jump("loc_180F")

    label("loc_17E8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17FE")
    Jump("loc_180F")

    label("loc_17FE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_180F")

    label("loc_180F")

    TalkEnd(0xFE)
    Return()

    # Function_15_1743 end

    def Function_16_1813(): pass

    label("Function_16_1813")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_182C")
    Jump("loc_1900")

    label("loc_182C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_184F")
    Call(0, 13)
    Jump("loc_18BE")

    label("loc_184F")


    ChrTalk(
        0x12,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "I'm moved that I was\x01",
            "able to meet Miss Ilya.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi, then, enjoy\x01",
            "your stay to the\x01",
            "fullest.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18BE")

    Jump("loc_1900")

    label("loc_18C3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18D9")
    Jump("loc_1900")

    label("loc_18D9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18EF")
    Jump("loc_1900")

    label("loc_18EF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1900")

    label("loc_1900")

    TalkEnd(0xFE)
    Return()

    # Function_16_1813 end

    def Function_17_1904(): pass

    label("Function_17_1904")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_191D")
    Jump("loc_19E0")

    label("loc_191D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1933")
    Jump("loc_19E0")

    label("loc_1933")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1949")
    Jump("loc_19E0")

    label("loc_1949")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19CF")

    ChrTalk(
        0x13,
        (
            "It was really fantastic\x01",
            "inside Mirror Castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "It made me feel once\x01",
            "again that I've come to\x01",
            "this park.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19E0")

    label("loc_19CF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19E0")

    label("loc_19E0")

    TalkEnd(0xFE)
    Return()

    # Function_17_1904 end

    def Function_18_19E4(): pass

    label("Function_18_19E4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19FD")
    Jump("loc_1ACD")

    label("loc_19FD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A13")
    Jump("loc_1ACD")

    label("loc_1A13")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A29")
    Jump("loc_1ACD")

    label("loc_1A29")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ABC")

    ChrTalk(
        0x14,
        (
            "Going up and down those\x01",
            "long stairs was a little\x01",
            "tiresome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "However, Rimah was happy\x01",
            "so it was worth climbing\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ACD")

    label("loc_1ABC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ACD")

    label("loc_1ACD")

    TalkEnd(0xFE)
    Return()

    # Function_18_19E4 end

    def Function_19_1AD1(): pass

    label("Function_19_1AD1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AEA")
    Jump("loc_1BB5")

    label("loc_1AEA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B00")
    Jump("loc_1BB5")

    label("loc_1B00")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B16")
    Jump("loc_1BB5")

    label("loc_1B16")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BA4")

    ChrTalk(
        0x15,
        (
            "I rang the bell at the\x01",
            "castle with daddy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Ehehe, I wished that we\x01",
            "could come back together\x01",
            "again to have fun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BB5")

    label("loc_1BA4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BB5")

    label("loc_1BB5")

    TalkEnd(0xFE)
    Return()

    # Function_19_1AD1 end

    def Function_20_1BB9(): pass

    label("Function_20_1BB9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CEA")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Welcome to Mirror\x01",
            "Castle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this attraction, you explore the inside\x01",
            "of this castle with the "Wish-Granting\x01",
            "Mirror" on the top floor as your goal!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(I'm playing hide-and-seek with\x01",
            "Mishette... I'll refrain from\x01",
            "visiting the attractions for now.)\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_1CED")

    label("loc_1CEA")

    Call(0, 33)

    label("loc_1CED")

    Return()

    # Function_20_1BB9 end

    def Function_21_1CEE(): pass

    label("Function_21_1CEE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D58")

    ChrTalk(
        0xFE,
        (
            "Climbing to the top of\x01",
            "that big castle...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...It looks quite\x01",
            "tiresome.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D58")

    label("loc_1D58")

    TalkEnd(0xFE)
    Return()

    # Function_21_1CEE end

    def Function_22_1D5C(): pass

    label("Function_22_1D5C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DBE")

    ChrTalk(
        0xFE,
        (
            "For this child's sake, I\x01",
            "must do my best like my\x01",
            "husband and climb.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DBE")

    label("loc_1DBE")

    TalkEnd(0xFE)
    Return()

    # Function_22_1D5C end

    def Function_23_1DC2(): pass

    label("Function_23_1DC2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E17")

    ChrTalk(
        0xFE,
        (
            "*thump thump*... What\x01",
            "should I wish on the\x01",
            "mirror for?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E17")

    label("loc_1E17")

    TalkEnd(0xFE)
    Return()

    # Function_23_1DC2 end

    def Function_24_1E1B(): pass

    label("Function_24_1E1B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E8C")

    ChrTalk(
        0xFE,
        (
            "C'mon, let's hurry and\x01",
            "enter the castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then, we'll spend time\x01",
            "romantically.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EDF")

    label("loc_1E8C")


    ChrTalk(
        0xFE,
        (
            "The night operations\x01",
            "start now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come on, let's enjoy an\x01",
            "eccentric night.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EDF")

    TalkEnd(0xFE)
    Return()

    # Function_24_1E1B end

    def Function_25_1EE3(): pass

    label("Function_25_1EE3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F52")

    ChrTalk(
        0xFE,
        (
            "Haha, what a lovely\x01",
            "castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's like I've come to\x01",
            "the world of fairytales.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FC3")

    label("loc_1F52")


    ChrTalk(
        0xFE,
        (
            "I spent a romantic time\x01",
            "with him at Mirror\x01",
            "Castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, I can't wait for\x01",
            "the night operations\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FC3")

    TalkEnd(0xFE)
    Return()

    # Function_25_1EE3 end

    def Function_26_1FC7(): pass

    label("Function_26_1FC7")

    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x10)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x10)
    SetChrFlags(0x1D, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_201E")
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    Jump("loc_2132")

    label("loc_201E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_204D")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x10)
    Jump("loc_2132")

    label("loc_204D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2077")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)
    Jump("loc_2132")

    label("loc_2077")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20FE")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_20D0")
    SetChrFlags(0x8, 0x80)
    Jump("loc_20DE")

    label("loc_20D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_20DE")
    SetChrFlags(0xA, 0x80)

    label("loc_20DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20F9")
    ClearChrFlags(0x1D, 0x80)

    label("loc_20F9")

    Jump("loc_2132")

    label("loc_20FE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2132")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x10)
    ClearChrFlags(0x1B, 0x10)

    label("loc_2132")

    Return()

    # Function_26_1FC7 end

    def Function_27_2133(): pass

    label("Function_27_2133")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadEffect(0x0, "battle\\cr036301.eff")
    LoadEffect(0x1, "event\\ev15010.eff")
    OP_90(0x101, 100, 5000, -73000, 0)
    OP_90(0x102, -800, 5000, -74100, 0)
    OP_90(0x103, 750, 5000, -73900, 0)
    OP_90(0x104, -100, 5000, -75000, 0)
    SetMapObjFlags(0x0, 0x1000)
    ClearChrFlags(0x1C, 0x80)
    OP_78(0x1, 0x1C)
    OP_49()
    SetChrPos(0x1C, 0, 1600, -56000, 180)
    OP_D5(0x1C, 0x0, 0x2BF20, 0x0, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0xA, 0x2F, 0x0, 0x20)
    SetChrFlags(0x1C, 0x8000)
    SetChrFlags(0x1C, 0x1)
    OP_52(0x1C, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1D4C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_75(0x1, 0x1, 0x0)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 3400, -68000, 0)
    MoveCamera(180, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17000, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(14000, 3000)

    def lambda_22BE():
        OP_9B(0x0, 0x101, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_22BE)
    Sleep(50)

    def lambda_22D6():
        OP_9B(0x0, 0x102, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_22D6)
    Sleep(50)

    def lambda_22EE():
        OP_9B(0x0, 0x103, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_22EE)
    Sleep(50)

    def lambda_2306():
        OP_9B(0x0, 0x104, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2306)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    Fade(1000)
    OP_68(0, 42000, -7500, 0)
    MoveCamera(0, -25, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(35000, 0)
    OP_11(0x47, 0x99, 0xF3, 0x4B, 0x12C, 0x2710)
    OP_68(0, 24000, -7500, 10000)
    MoveCamera(335, 20, 0, 10000)
    SetCameraDistance(100000, 10000)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(0, 3500, -68000, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13500, 0)
    SetCameraDistance(12500, 2500)
    OP_90(0x102, -800, 5000, -67650, 0)
    OP_90(0x103, 750, 5000, -68350, 0)
    OP_90(0x104, 0, 5000, -69100, 0)
    OP_11(0x47, 0x99, 0xF3, 0x14, 0x12C, 0x0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#00303F#6PMirror Castle...\x02\x03",
            "#00301FI thought it was a\x01",
            "simple theme park\x01",
            "monument, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#6P...Spirit pressure is\x01",
            "clearly rising from\x01",
            "there.\x02\x03",
            "#00201FMost likely from the top\x01",
            "floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#5P...I heard this castle\x01",
            "was built because "she"\x01",
            "proposed it...\x02\x03",
            "#00108FBut, don't tell me\x01",
            "that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5P...In any case, let's go\x01",
            "inside.\x02\x03",
            "#00001FIf we're lucky, at the\x01",
            "top floor we─\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    Sound(842, 0, 100, 0)
    BeginChrThread(0x1C, 0, 0, 28)
    Sleep(1000)
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
    Sleep(1000)
    Fade(250)
    OP_68(0, 9500, -56000, 0)
    MoveCamera(35, 27, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(23500, 0)
    MoveCamera(315, 0, 0, 4000)
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7454", 0)
    Sleep(490)
    Sound(919, 0, 100, 0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    PlayEffect(0x0, 0xFF, 0x1C, 0x0, 0, 8500, 0, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x1C, 3, 0, 29)

    def lambda_26DD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_26DD)
    OP_75(0x1, 0x2, 0x3E8)
    WaitChrThread(0x1C, 2)
    CancelBlur(1000)
    EndChrThread(0x1C, 0x0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x79)
    OP_68(0, 5100, -56000, 1000)
    MoveCamera(330, 5, 0, 1000)
    OP_6E(650, 1000)
    SetCameraDistance(20000, 1000)
    OP_6F(0x79)
    Sleep(700)
    OP_68(-1350, 4700, -62800, 2000)
    MoveCamera(317, 5, 0, 2000)
    OP_6E(650, 2000)
    SetCameraDistance(20000, 2000)
    OP_90(0x102, -700, 5000, -67450, 0)
    OP_90(0x103, 1000, 5000, -68850, 0)
    OP_90(0x104, -100, 5000, -69300, 0)
    Sleep(1000)

    def lambda_27A5():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_27A5)
    Sleep(50)

    def lambda_27BD():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_27BD)
    Sleep(50)

    def lambda_27D5():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_27D5)
    Sleep(50)

    def lambda_27ED():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_27ED)
    WaitChrThread(0x104, 1)
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x102,
        "#00110F#1PFrom the Old Mine...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00307F#1PTch! It's guardin' the\x01",
            "castle!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00007F#1P─Prepare to fight! We'll\x01",
            "crush it with everything\x01",
            "we've got!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(60, 80, -1, -1)
    SetChrName("Everyone")

    AnonymousTalk(
        0xFF,
        "#4S#5PYeah!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(-2220, 5100, -59370, 1500)
    SetCameraDistance(11500, 1500)

    def lambda_293A():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_293A)

    def lambda_294F():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_294F)

    def lambda_2964():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2964)

    def lambda_2979():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2979)
    EndChrThread(0x1C, 0x3)
    BeginChrThread(0x1C, 3, 0, 30)
    Sleep(400)
    Sound(842, 0, 100, 0)
    BlurSwitch(0x64, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(400)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    Battle("BattleInfo_570", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 31)
    Return()

    # Function_27_2133 end

    def Function_28_29D9(): pass

    label("Function_28_29D9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_29FD")
    OP_82(0x64, 0x64, 0x1F40, 0x1F4)
    Sleep(500)
    Jump("Function_28_29D9")

    label("loc_29FD")

    Return()

    # Function_28_29D9 end

    def Function_29_29FE(): pass

    label("Function_29_29FE")

    OP_74(0x1, 0x5)

    label("loc_2A02")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A34")
    OP_71(0x1, 0x137, 0x13C, 0x0, 0x8)
    OP_79(0x1)
    OP_71(0x1, 0x13C, 0x137, 0x0, 0x8)
    OP_79(0x1)
    Jump("loc_2A02")

    label("loc_2A34")

    OP_74(0x1, 0xF)
    OP_71(0x1, 0x137, 0x14E, 0x0, 0x8)
    Sleep(550)
    PlayEffect(0x1, 0xFF, 0x1C, 0x0, 0, 1600, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(833, 0, 100, 0)
    OP_82(0x1C2, 0x96, 0x1388, 0x226)
    OP_79(0x1)
    OP_74(0x1, 0x19)
    OP_71(0x1, 0xA, 0x2F, 0x15E, 0x20)
    Return()

    # Function_29_29FE end

    def Function_30_2AA9(): pass

    label("Function_30_2AA9")

    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x78, 0x8C, 0x12C, 0x8)
    OP_79(0x1)
    OP_71(0x1, 0x8D, 0x95, 0x0, 0x20)
    Return()

    # Function_30_2AA9 end

    def Function_31_2AC9(): pass

    label("Function_31_2AC9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadEffect(0x0, "battle\\bs000000.eff")
    LoadEffect(0x1, "battle\\bs000001.eff")
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    OP_90(0x101, 0, 5000, -63000, 0)
    OP_90(0x102, -600, 5000, -64000, 0)
    OP_90(0x103, 600, 5000, -64000, 0)
    OP_90(0x104, 0, 5000, -65000, 0)
    SetMapObjFlags(0x0, 0x1000)
    ClearChrFlags(0x1C, 0x80)
    OP_78(0x1, 0x1C)
    OP_49()
    SetChrPos(0x1C, 0, 1600, -56000, 180)
    OP_D5(0x1C, 0x0, 0x2BF20, 0x0, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0xA, 0x2F, 0x0, 0x20)
    SetChrFlags(0x1C, 0x8000)
    SetChrFlags(0x1C, 0x1)
    OP_52(0x1C, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1D4C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_75(0x1, 0x2, 0x0)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(0, 12000, -56000, 0)
    MoveCamera(315, -10, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(20500, 0)
    FadeToBright(1000, 0)
    OP_68(0, 8500, -56000, 3000)
    MoveCamera(0, 15, 0, 3000)
    SetCameraDistance(35000, 3000)
    BeginChrThread(0x1C, 0, 0, 28)
    BeginChrThread(0x1C, 3, 0, 32)
    Sound(919, 0, 80, 0)
    Sound(842, 0, 100, 0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    PlayEffect(0x0, 0x0, 0x1C, 0x0, 0, 0, 0, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    PlayEffect(0x1, 0x1, 0x1C, 0x0, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)

    def lambda_2CFB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_2CFB)
    OP_75(0x1, 0x1, 0x3E8)
    WaitChrThread(0x1C, 2)
    CancelBlur(1000)
    EndChrThread(0x1C, 0x3)
    EndChrThread(0x1C, 0x0)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    OP_6F(0x79)
    OP_0D()
    SetMapObjFlags(0x1, 0x4)
    SetChrFlags(0x1C, 0x80)
    Sleep(700)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x0, 0x1000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_90(0x0, 0, 5000, -63000, 0)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x183, 0)
    ModifyEventFlags(0, 0, 0x80)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_31_2AC9 end

    def Function_32_2D93(): pass

    label("Function_32_2D93")

    OP_74(0x1, 0x19)
    OP_71(0x1, 0x50, 0x5A, 0x0, 0x8)
    OP_79(0x1)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x5A, 0x6D, 0x0, 0x20)
    Return()

    # Function_32_2D93 end

    def Function_33_2DB7(): pass

    label("Function_33_2DB7")

    EventBegin(0x0)
    Fade(500)
    OP_68(0, 2500, -23700, 0)
    MoveCamera(0, 12, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    OP_4B(0x16, 0xFF)
    SetChrPos(0x101, 0, 1210, -24340, 0)
    OP_0D()

    ChrTalk(
        0x16,
        (
            "Welcome to Mirror\x01",
            "Castle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "In this attraction, you explore the inside\x01",
            "of this castle with the "Wish-Granting\x01",
            "Mirror" on the top floor as your goal!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I recommend entering\x01",
            "with someone if you\x01",
            "like, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P(Who should I\x01",
            "invite...?)\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 5, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWho will you invite?\x07\x00\x02",
        )
    )

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Elie")
    MenuCmd(1, 0, "Tio")
    MenuCmd(1, 0, "Randy")
    MenuCmd(1, 0, "Noｱl")
    MenuCmd(1, 0, "Wazy")
    MenuCmd(1, 0, "KeA")
    MenuCmd(1, 0, "Fran")
    MenuCmd(1, 0, "Cecil")
    MenuCmd(1, 0, "Ilya")
    MenuCmd(1, 0, "Rixia")
    MenuCmd(1, 0, "Sully")
    MenuCmd(1, 0, "Cancel")
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2FBE")
    MenuCmd(3, 0, 0x0)

    label("loc_2FBE")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x20000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2FD0")
    MenuCmd(3, 0, 0x1)

    label("loc_2FD0")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x40000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2FE2")
    MenuCmd(3, 0, 0x2)

    label("loc_2FE2")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x80000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2FF4")
    MenuCmd(3, 0, 0x3)

    label("loc_2FF4")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x100000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3006")
    MenuCmd(3, 0, 0x4)

    label("loc_3006")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x200000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3018")
    MenuCmd(3, 0, 0x5)

    label("loc_3018")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x400000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_302A")
    MenuCmd(3, 0, 0x6)

    label("loc_302A")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x800000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_303C")
    MenuCmd(3, 0, 0x7)

    label("loc_303C")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1000000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_304E")
    MenuCmd(3, 0, 0x8)

    label("loc_304E")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2000000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3060")
    MenuCmd(3, 0, 0x9)

    label("loc_3060")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4000000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3072")
    MenuCmd(3, 0, 0xA)

    label("loc_3072")

    MenuCmd(2, 0, -1, 55, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3633")
    OP_D2(0x5, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x40000000), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))
    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x80000000), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_310C"),
        (1, "loc_3148"),
        (2, "loc_3183"),
        (3, "loc_31C0"),
        (4, "loc_31FC"),
        (5, "loc_3238"),
        (6, "loc_3273"),
        (7, "loc_32AF"),
        (8, "loc_32EC"),
        (9, "loc_3328"),
        (10, "loc_3365"),
        (SWITCH_DEFAULT, "loc_33A2"),
    )


    label("loc_310C")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#6P(Alright... I'll invite\x01",
            "Elie.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33A2")

    label("loc_3148")

    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#6P(Alright... I'll invite\x01",
            "Tio.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33A2")

    label("loc_3183")

    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#6P(Alright... I'll invite\x01",
            "Randy.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33A2")

    label("loc_31C0")

    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#6P(Alright... I'll invite\x01",
            "Noｱl.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33A2")

    label("loc_31FC")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#6P(Alright... I'll invite\x01",
            "Wazy.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33A2")

    label("loc_3238")

    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#6P(Alright... I'll invite\x01",
            "KeA.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33A2")

    label("loc_3273")

    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#6P(Alright... I'll invite\x01",
            "Fran.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33A2")

    label("loc_32AF")

    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#6P(Alright... I'll invite\x01",
            "Cecil.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33A2")

    label("loc_32EC")

    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#6P(Alright... I'll invite\x01",
            "Ilya.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33A2")

    label("loc_3328")

    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#6P(Alright... I'll invite\x01",
            "Rixia.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33A2")

    label("loc_3365")

    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#6P(Alright... I'll invite\x01",
            "Sully.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33A2")

    label("loc_33A2")

    FadeToDark(500, 0, -1)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_33F9"),
        (1, "loc_3402"),
        (2, "loc_340B"),
        (3, "loc_3414"),
        (4, "loc_341D"),
        (5, "loc_3426"),
        (6, "loc_342F"),
        (7, "loc_3438"),
        (8, "loc_3441"),
        (9, "loc_344A"),
        (10, "loc_3453"),
        (SWITCH_DEFAULT, "loc_345C"),
    )


    label("loc_33F9")

    AddParty(0x1, 0xEF, 0xFF)
    Jump("loc_345C")

    label("loc_3402")

    AddParty(0x2, 0xEF, 0xFF)
    Jump("loc_345C")

    label("loc_340B")

    AddParty(0x3, 0xEF, 0xFF)
    Jump("loc_345C")

    label("loc_3414")

    AddParty(0x8, 0xEF, 0xFF)
    Jump("loc_345C")

    label("loc_341D")

    AddParty(0x4, 0xEF, 0xFF)
    Jump("loc_345C")

    label("loc_3426")

    AddParty(0x52, 0xEF, 0xFF)
    Jump("loc_345C")

    label("loc_342F")

    AddParty(0x55, 0xEF, 0xFF)
    Jump("loc_345C")

    label("loc_3438")

    AddParty(0x4B, 0xEF, 0xFF)
    Jump("loc_345C")

    label("loc_3441")

    AddParty(0x33, 0xEF, 0xFF)
    Jump("loc_345C")

    label("loc_344A")

    AddParty(0x34, 0xEF, 0xFF)
    Jump("loc_345C")

    label("loc_3453")

    AddParty(0x65, 0xEF, 0xFF)
    Jump("loc_345C")

    label("loc_345C")

    SetChrPos(0x101, -500, 1030, -24600, 0)
    SetChrPos(0xEF, 500, 1030, -24600, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x16,
        (
            "Then, I'll hold on to\x01",
            "your tickets.\x02",
        )
    )

    CloseMessageWindow()
    SubItemNumber(0x35D, 1)
    FadeToDark(300, 0, 100)
    Sound(18, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Gave the staffer a\x01",
            "ticket.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x16,
        (
            "Alright, I got your\x01",
            "ticket.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Please enjoy your\x01",
            "exploration of the\x01",
            "wondrous Mirror Castle...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x16, 0x0, 0x1F4)
    OP_9B(0x0, 0x16, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(200)
    Sound(116, 0, 100, 0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x1, 0xA, 0x1, 0x0)
    OP_79(0x0)

    def lambda_35AA():
        OP_98(0xFE, 0xFFFFFA24, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_35AA)
    OP_93(0x16, 0x5A, 0x1F4)
    WaitChrThread(0x16, 1)
    Sleep(300)
    StopSound(126, 1000, 70)
    StopSound(821, 1000, 50)
    FadeToDark(1000, 0, -1)

    def lambda_35E8():
        OP_9B(0x0, 0x101, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_35E8)
    Sleep(50)

    def lambda_3600():
        OP_9B(0x0, 0xEF, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_3600)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xEF, 0)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("t1401", 0, 0, 0)
    IdleLoop()
    Jump("loc_367C")

    label("loc_3633")


    ChrTalk(
        0x16,
        "Oh, you're giving up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "We'll be waiting for\x01",
            "your next visit.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_367C")

    OP_4C(0x16, 0xFF)
    SetChrPos(0x0, 0, 0, -28000, 180)
    EventEnd(0x5)
    Return()

    # Function_33_2DB7 end

    def Function_34_3694(): pass

    label("Function_34_3694")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -600, 1030, -24600, 90)
    SetChrPos(0xEF, 600, 1030, -24600, 270)
    OP_4B(0x16, 0xFF)
    FadeToBright(1000, 0)
    OP_68(0, 3000, -23700, 0)
    OP_68(0, 2500, -23700, 2500)
    MoveCamera(0, 12, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    OP_6F(0x79)
    OP_0D()
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_375C"),
        (1, "loc_3804"),
        (2, "loc_38A5"),
        (3, "loc_3945"),
        (4, "loc_39CC"),
        (5, "loc_3A73"),
        (6, "loc_3B0C"),
        (7, "loc_3BA9"),
        (8, "loc_3C4F"),
        (9, "loc_3CFB"),
        (10, "loc_3DA2"),
        (SWITCH_DEFAULT, "loc_3E28"),
    )


    label("loc_375C")


    ChrTalk(
        0x102,
        (
            "#00102F*giggle*. That was a fun\x01",
            "walk through the castle\x01",
            "together.\x02\x03",
            "#00100FThen, it's time for me\x01",
            "to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F*giggle*, later.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E28")

    label("loc_3804")


    ChrTalk(
        0x103,
        (
            "#00202FThe Mirror Castle... It\x01",
            "was fun touring it\x01",
            "together.\x02\x03",
            "#00202FThen, I'll excuse myself\x01",
            "for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FYes, later.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E28")

    label("loc_38A5")


    ChrTalk(
        0x104,
        (
            "#00302FHaha. That was a lot of\x01",
            "fun, even with just us\x01",
            "guys.\x02\x03",
            "#00300FThen, I'm goin'\x01",
            "somewhere else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FYeah, later.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E28")

    label("loc_3945")


    ChrTalk(
        0x109,
        (
            "#10109FMirror Castle was pretty\x01",
            "fun.\x02\x03",
            "#10100FI'll excuse myself here,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FYes, later!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E28")

    label("loc_39CC")


    ChrTalk(
        0x105,
        (
            "#10304FThe Mirror Castle... It\x01",
            "was quite interesting.\x02\x03",
            "#10300FWell then, I believe\x01",
            "I'll go somewhere else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHehe, later.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E28")

    label("loc_3A73")


    ChrTalk(
        0x153,
        (
            "#01109FAhh, such a big castle.\x01",
            "That was fun!\x02\x03",
            "#01100FOk, KeA will go\x01",
            "somewhere else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01100FEhehe, later, Lloyd!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E28")

    label("loc_3B0C")


    ChrTalk(
        0x156,
        (
            "#06409FHaha, the Mirror\x01",
            "Castle... It was really\x01",
            "fun!\x02\x03",
            "#06400FWell then, I'll excuse\x01",
            "myself, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x156,
        "#06400FYes, see you!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E28")

    label("loc_3BA9")


    ChrTalk(
        0x14C,
        (
            "#05902FHaha. It was a lot of\x01",
            "fun seeing that huge\x01",
            "mirror and bell.\x02\x03",
            "#05900FThen, I'll go somewhere\x01",
            "else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14C,
        "#05900FYes, see you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E28")

    label("loc_3C4F")


    ChrTalk(
        0x134,
        (
            "#01709FHaha. That was a pretty\x01",
            "impressive castle, eh?\x02\x03",
            "#01700FNow then, I'll be going\x01",
            "somewhere else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, see you later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        "#01700FYeah, see you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E28")

    label("loc_3CFB")


    ChrTalk(
        0x135,
        (
            "#01809FHaha, it was really fun\x01",
            "walking around the\x01",
            "beautiful castle.\x02\x03",
            "#01802FThen, I'll excuse myself\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        "#01802FYes, then...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E28")

    label("loc_3DA2")


    ChrTalk(
        0x166,
        (
            "#14002F...Walking around the\x01",
            "castle wasn't bad.\x02\x03",
            "#14000FThen, I'm going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x166,
        "#14000FYeah, see ya.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E28")

    label("loc_3E28")

    BeginChrThread(0xEF, 3, 0, 35)
    WaitChrThread(0xEF, 3)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_3E7D"),
        (1, "loc_3E8B"),
        (2, "loc_3E99"),
        (3, "loc_3EA7"),
        (4, "loc_3EB5"),
        (5, "loc_3EC3"),
        (6, "loc_3ED1"),
        (7, "loc_3EDF"),
        (8, "loc_3EED"),
        (9, "loc_3EFB"),
        (10, "loc_3F09"),
        (SWITCH_DEFAULT, "loc_3F17"),
    )


    label("loc_3E7D")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x10000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3F17")

    label("loc_3E8B")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x20000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3F17")

    label("loc_3E99")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x40000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3F17")

    label("loc_3EA7")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x80000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3F17")

    label("loc_3EB5")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x100000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3F17")

    label("loc_3EC3")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x200000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3F17")

    label("loc_3ED1")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x400000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3F17")

    label("loc_3EDF")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x800000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3F17")

    label("loc_3EED")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3F17")

    label("loc_3EFB")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3F17")

    label("loc_3F09")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3F17")

    label("loc_3F17")

    OP_D2(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F54")
    StopSound(126, 1000, 70)
    StopSound(821, 1000, 40)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("t1300", 0, 0, 0)
    IdleLoop()

    label("loc_3F54")

    OP_4C(0x16, 0xFF)
    SetChrPos(0x0, 0, 0, -29000, 180)
    EventEnd(0x5)
    Return()

    # Function_34_3694 end

    def Function_35_3F6C(): pass

    label("Function_35_3F6C")


    def lambda_3F71():
        OP_93(0xFE, 0xB4, 0xC8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3F71)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_3F85():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F85)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0xFE, 1)
    EndChrThread(0x101, 0x2)
    Return()

    # Function_35_3F6C end

    def Function_36_3FAC(): pass

    label("Function_36_3FAC")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x1D, 0x0)
    OP_68(6540, 5060, -25400, 0)
    MoveCamera(320, 41, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(8910, 0)
    SetChrPos(0x101, 2560, 1600, -22190, 90)
    SetChrPos(0xEF, 2590, 1290, -23560, 90)
    OP_4B(0x1D, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#00000FFound her!\x02",
    )

    CloseMessageWindow()
    OP_9C(0x1D, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    Sleep(500)
    TurnDirection(0x1D, 0x101, 500)
    OP_63(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1D,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Eek! You found me☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Mishishi, you're\x01",
            "amazing, mister~!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-2110, 3600, -34340, 0)
    MoveCamera(30, 32, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(10310, 0)
    SetChrPos(0x1D, 80, 0, -29860, 180)
    SetChrPos(0x101, -500, 0, -31500, 0)
    SetChrPos(0xEF, 500, 0, -31500, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x1D,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "I can't believe you\x01",
            "found me five times this\x01",
            "quickly...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Mishishi, this is my\x01",
            "total defeat~.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Mister, you truly are\x01",
            "the King of Hide-and-\x01",
            "Seek~☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_4210")
    OP_63(0x153, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_4288")

    label("loc_4210")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_4230")
    OP_63(0xEF, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_4288")

    label("loc_4230")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_4250")
    OP_63(0xEF, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_4288")

    label("loc_4250")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_4270")
    OP_63(0xEF, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_4288")

    label("loc_4270")

    OP_63(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4288")

    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FK-King of Hide-and-\x01",
            "Seek...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_42F4")

    ChrTalk(
        0x102,
        (
            "#00102F*giggle*, you got a\x01",
            "strange title, eh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4544")

    label("loc_42F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_433E")

    ChrTalk(
        0x103,
        (
            "#00202FAs expected from\x01",
            "Mishette... Loose and\x01",
            "relaxed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4544")

    label("loc_433E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_4374")

    ChrTalk(
        0x104,
        (
            "#00302FYou got a weird title,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4544")

    label("loc_4374")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_43B5")

    ChrTalk(
        0x109,
        (
            "#10102FAhaha... she gave you a\x01",
            "strange title.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4544")

    label("loc_43B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_43F9")

    ChrTalk(
        0x105,
        (
            "#10309FHehe, you earned quite\x01",
            "the cool nickname.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4544")

    label("loc_43F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_442A")

    ChrTalk(
        0x153,
        "#01109FLloyd, you're so cool!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4544")

    label("loc_442A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_4461")

    ChrTalk(
        0x156,
        (
            "#06409FHaha, you got a funny\x01",
            "title!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4544")

    label("loc_4461")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_4497")

    ChrTalk(
        0x14C,
        (
            "#05902FHaha. What a cute\x01",
            "nickname.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4544")

    label("loc_4497")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_44CE")

    ChrTalk(
        0x134,
        (
            "#01702FHuhu. Pretty good, isn't\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4544")

    label("loc_44CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_450E")

    ChrTalk(
        0x135,
        (
            "#01802FA-Ahaha... That's quite\x01",
            "an odd title.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4544")

    label("loc_450E")


    ChrTalk(
        0x166,
        (
            "#14002FAhaha, you got yourself\x01",
            "a weird nickname.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4544")


    ChrTalk(
        0x1D,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "And, I'll give you all\x01",
            "this prize as a reward\x01",
            "for finding me~☆\x07\x00\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x54),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x54, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00000FAh, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Mishishi, you're\x01",
            "welcome☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Then, it's time for me\x01",
            "to leave, you know~.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Make a lot of great\x01",
            "memories at Wonderland for\x01",
            "the rest of the day, ok~?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_46A1():

        label("loc_46A1")

        TurnDirection(0xFE, 0x1D, 500)
        Yield()
        Jump("loc_46A1")

    QueueWorkItem2(0x101, 1, lambda_46A1)

    def lambda_46B3():

        label("loc_46B3")

        TurnDirection(0xFE, 0x1D, 500)
        Yield()
        Jump("loc_46B3")

    QueueWorkItem2(0xEF, 1, lambda_46B3)
    OP_95(0x1D, -1420, 0, -29670, 2000, 0x0)
    OP_95(0x1D, -1630, 230, -38320, 2000, 0x0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)

    def lambda_46F5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_46F5)
    Sleep(50)

    def lambda_4705():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_4705)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_477C")

    ChrTalk(
        0x101,
        (
            "#00012FHaha... Mishy's younger\x01",
            "sister is quite the intense\x01",
            "character herself, isn't she.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47DA")

    label("loc_477C")


    ChrTalk(
        0x101,
        (
            "#00012FHaha... Mishy's younger\x01",
            "sister is quite the intense\x01",
            "character herself, isn't she.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47DA")

    TurnDirection(0xEF, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_483D")

    ChrTalk(
        0x102,
        (
            "#00104F*giggle*, that's right.\x02\x03",
            "#00100FThen, it's time for me\x01",
            "to go too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C21")

    label("loc_483D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_48D6")

    ChrTalk(
        0x103,
        (
            "#00204FHaha. That's right. She\x01",
            "was a better character\x01",
            "than the rumors said.\x02\x03",
            "#00200FThen, it is time for me\x01",
            "to excuse myself as\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C21")

    label("loc_48D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_4935")

    ChrTalk(
        0x104,
        (
            "#00309FHaha, you said it.\x02\x03",
            "#00300FThen, I guess it's time\x01",
            "for me to go too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C21")

    label("loc_4935")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_4993")

    ChrTalk(
        0x109,
        (
            "#10109FHaha, you're right.\x02\x03",
            "#10100FThen, it's time for me\x01",
            "to be going too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C21")

    label("loc_4993")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_49E1")

    ChrTalk(
        0x105,
        (
            "#10309FHehe, right.\x02\x03",
            "#10300FThen, I'll excuse myself\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C21")

    label("loc_49E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_4A4D")

    ChrTalk(
        0x153,
        (
            "#01109FEhehe, I wanna see her\x01",
            "again.\x02\x03",
            "#01104FAlright, then KeA too\x01",
            "will go have fun too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C21")

    label("loc_4A4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_4A9F")

    ChrTalk(
        0x156,
        (
            "#06409FHaha, really.\x02\x03",
            "#06400FThen, it's time for me\x01",
            "to go too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C21")

    label("loc_4A9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_4AFF")

    ChrTalk(
        0x14C,
        (
            "#05904FHaha, really.\x02\x03",
            "#05900FThen, I believe it's\x01",
            "time for me to go as\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C21")

    label("loc_4AFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_4B68")

    ChrTalk(
        0x134,
        (
            "#01709FHuhu. She was good.\x02\x03",
            "#01700FThen, I guess I'll go\x01",
            "have fun somewhere else\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C21")

    label("loc_4B68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_4BC9")

    ChrTalk(
        0x135,
        (
            "#01809FHaha, indeed.\x02\x03",
            "#01802FThen, it's time for me\x01",
            "to excuse myself as\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C21")

    label("loc_4BC9")


    ChrTalk(
        0x166,
        (
            "#14006FYeah, she was a weirdo,\x01",
            "huh.\x02\x03",
            "#14000FThen, I'll go have fun\x01",
            "somewhere else.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C21")

    TurnDirection(0x101, 0xEF, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_4C57")

    ChrTalk(
        0x101,
        "#00000FYeah, see you later.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C70")

    label("loc_4C57")


    ChrTalk(
        0x101,
        "#00000FYeah, later.\x02",
    )

    CloseMessageWindow()

    label("loc_4C70")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_4C91")
    RemoveParty(0x1, 0xFF)
    ClearChrFlags(0x8, 0x80)
    Jump("loc_4D32")

    label("loc_4C91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_4CA2")
    RemoveParty(0x2, 0xFF)
    Jump("loc_4D32")

    label("loc_4CA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_4CB3")
    RemoveParty(0x3, 0xFF)
    Jump("loc_4D32")

    label("loc_4CB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_4CC9")
    RemoveParty(0x8, 0xFF)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_4D32")

    label("loc_4CC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_4CDA")
    RemoveParty(0x4, 0xFF)
    Jump("loc_4D32")

    label("loc_4CDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_4CEB")
    RemoveParty(0x52, 0xFF)
    Jump("loc_4D32")

    label("loc_4CEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_4CFC")
    RemoveParty(0x55, 0xFF)
    Jump("loc_4D32")

    label("loc_4CFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_4D0D")
    RemoveParty(0x4B, 0xFF)
    Jump("loc_4D32")

    label("loc_4D0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_4D1E")
    RemoveParty(0x33, 0xFF)
    Jump("loc_4D32")

    label("loc_4D1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_4D2F")
    RemoveParty(0x34, 0xFF)
    Jump("loc_4D32")

    label("loc_4D2F")

    RemoveParty(0x65, 0xFF)

    label("loc_4D32")

    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Mishette's\x01",
            "Challenge]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x7F, 0x1, 0xF)
    OP_29(0x7F, 0x4, 0x10)
    SetScenarioFlags(0x1C9, 7)
    OP_65(0x0, 0x1)
    SetChrFlags(0x1D, 0x80)
    SetChrPos(0x0, 10, 150, -36180, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_36_3FAC end

    def Function_37_4DAE(): pass

    label("Function_37_4DAE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10200.itc", 0x1E)
    LoadChrToIndex("chr/ch45400.itc", 0x1F)
    LoadChrToIndex("chr/ch22200.itc", 0x20)
    LoadChrToIndex("chr/ch23000.itc", 0x21)
    LoadEffect(0x0, "battle/ms00109.eff")
    SoundLoad(862)
    SoundLoad(645)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x1E, 0x20)
    SetChrFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x21)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x103, 0x1000)
    SetChrFlags(0x1E, 0x1000)
    SetChrFlags(0x1F, 0x1000)
    OP_68(1270, 2520, -36760, 0)
    MoveCamera(51, 26, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(11430, 0)
    SetChrPos(0x101, -300, 300, -43880, 0)
    SetChrPos(0x103, 770, 340, -44750, 0)
    SetChrPos(0x109, 3940, 150, -36320, 0)
    SetChrPos(0x105, 3870, 50, -34830, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x104, 0x80)
    OP_68(1110, 2520, -36960, 3000)
    SetCameraDistance(13230, 3000)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_4ED7():
        OP_97(0xFE, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4ED7)
    Sleep(50)

    def lambda_4EF4():
        OP_97(0xFE, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4EF4)
    Sleep(500)
    OP_63(0x109, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    WaitChrThread(0x103, 1)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_4F71():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4F71)
    Sleep(50)

    def lambda_4F81():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4F81)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05200FHey, Noｱl, Wazy.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4FB2():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4FB2)
    Sleep(50)

    def lambda_4FC2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4FC2)
    Sleep(300)

    def lambda_4FD2():
        OP_97(0xFE, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4FD2)
    Sleep(50)

    def lambda_4FEF():
        OP_97(0xFE, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4FEF)
    WaitChrThread(0x101, 1)

    def lambda_500D():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_500D)
    Sleep(50)

    def lambda_501D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_501D)
    Sleep(300)

    ChrTalk(
        0x105,
        "#10300FHehe, long time no see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FAh, please listen, Mr.\x01",
            "Lloyd!\x02\x03",
            "#10103FThat Wazy wanders off as\x01",
            "soon as I take my eyes\x01",
            "off him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FHehe, I'm not causing any\x01",
            "serious incidents, am I?\x02\x03",
            "#10304FI mean, don't you think\x01",
            "it's better to have some\x01",
            "fun while walking around?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206FI don't? Seriously, it's\x01",
            "not...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x1, 0x8)
    OP_79(0x0)
    Fade(250)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1E, -760, 1600, -21700, 180)
    SetChrPos(0x1F, 650, 1600, -21700, 180)
    OP_0D()
    TurnDirection(0x103, 0x1F, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520FAh... Lloyd, children.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(100, 20, -1, -1)
    SetChrName("Child's Voice")

    AnonymousTalk(
        0xFF,
        "#4SIt's Mishyyy!!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(100, 20, -1, -1)
    SetChrName("Child's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#4SAh, and there's Mishette\x01",
            "too?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    def lambda_527D():
        TurnDirection(0xFE, 0x1F, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_527D)
    Sleep(50)

    def lambda_528D():
        TurnDirection(0xFE, 0x1F, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_528D)
    Sleep(50)

    def lambda_529D():
        TurnDirection(0xFE, 0x1F, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_529D)
    OP_63(0x101, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_70(0x0, 0x0)
    OP_68(-800, 2520, -37470, 3000)
    MoveCamera(43, 32, 0, 3000)
    OP_6E(650, 3000)
    SetCameraDistance(11660, 3000)

    def lambda_5330():
        OP_95(0xFE, -440, 60, -35850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_5330)
    Sleep(100)

    def lambda_534D():
        OP_95(0xFE, 710, 10, -34740, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_534D)

    def lambda_5367():

        label("loc_5367")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_5367")

    QueueWorkItem2(0x109, 1, lambda_5367)

    def lambda_5379():

        label("loc_5379")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_5379")

    QueueWorkItem2(0x105, 1, lambda_5379)
    WaitChrThread(0x1E, 1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)

    def lambda_5397():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_5397)
    Sleep(50)

    def lambda_53A7():
        TurnDirection(0xFE, 0x1E, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_53A7)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05528F(...I failed to hide.)\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "Hiya, kick!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    BeginChrThread(0x1E, 3, 0, 38)
    Sleep(300)
    BeginChrThread(0x1F, 3, 0, 38)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05211F(Wait a...!?)\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10309FPfft...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FW-Wait, you can't do\x01",
            "that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Miss, you don't know? If\x01",
            "you kick Mishy, you'll\x01",
            "get lucky!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "They say luck is packed\x01",
            "in his butt!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Kyah ha ha ha!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05211F(L-Luck... I never heard\x01",
            "anything about that!)\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 6)
    WaitChrThread(0x1E, 3)
    OP_64(0x101)

    def lambda_5536():
        TurnDirection(0x1E, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_5536)
    Sleep(50)
    TurnDirection(0x1F, 0x103, 500)

    ChrTalk(
        0x1F,
        (
            "I wonder if I can kick\x01",
            "her too?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520F(...!)\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05203F(W-What do I do? I've\x01",
            "got to deal with this\x01",
            "somehow...)\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Scold them harshly\x01",      # 0
            "Tickle them\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5656"),
        (1, "loc_5729"),
        (SWITCH_DEFAULT, "loc_583B"),
    )


    label("loc_5656")

    TurnDirection(0x101, 0x1E, 500)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "H-Heey! That's enough!\x02\x03",
            "Even if I am Mishy, I\x01",
            "won't forgive you, you\x01",
            "know!?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1F, 0x101, 500)
    Sleep(100)
    OP_63(0x1E, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1E,
        "Uwaaah, Mishy's mad!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Run awaaay!\x02",
    )

    CloseMessageWindow()
    OP_29(0x86, 0x1, 0x3)
    Jump("loc_583B")

    label("loc_5729")

    OP_2C(0x86, 0x1)
    SetScenarioFlags(0x176, 6)
    TurnDirection(0x101, 0x1E, 500)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "To the kids who do\x01",
            "that... I do thiiis!\x02\x03",
            "*tickle tickle\x01",
            "tickle*...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1F, 0x101, 500)
    Sleep(100)
    OP_9C(0x1E, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    OP_63(0x1E, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x1F, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x1E,
        (
            "Eeek... Kyah ha ha ha ha\x01",
            "ha ha ha!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Yaay, it's Mishy's\x01",
            "counterattack!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Run awaaay!\x02",
    )

    CloseMessageWindow()
    OP_29(0x86, 0x1, 0x4)
    Jump("loc_583B")

    label("loc_583B")


    def lambda_5840():
        OP_97(0xFE, 0xFFFFF95C, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_5840)
    Sleep(100)

    def lambda_585D():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_585D)
    WaitChrThread(0x1F, 1)

    def lambda_587B():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_587B)

    def lambda_5895():

        label("loc_5895")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_5895")

    QueueWorkItem2(0x101, 1, lambda_5895)

    def lambda_58A7():

        label("loc_58A7")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_58A7")

    QueueWorkItem2(0x103, 1, lambda_58A7)

    def lambda_58B9():

        label("loc_58B9")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_58B9")

    QueueWorkItem2(0x109, 1, lambda_58B9)

    def lambda_58CB():

        label("loc_58CB")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_58CB")

    QueueWorkItem2(0x105, 1, lambda_58CB)
    WaitChrThread(0x1E, 1)
    WaitChrThread(0x1F, 1)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    OP_93(0x105, 0xB4, 0x1F4)
    Sleep(50)
    OP_93(0x109, 0xB4, 0x1F4)
    OP_0D()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05200F*sigh*, there they go.\x02\x03",
            "#05206FTo think I was kicked\x01",
            "all of a sudden...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5969():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5969)
    Sleep(50)

    def lambda_5979():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5979)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10300FThat kind of thing seems\x01",
            "popular these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10112FAhaha... How unlucky.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05203FBut... I guess it turned\x01",
            "out all right. I didn't\x01",
            "really think it through...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B66")
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05524F...I think it was better than\x01",
            "yelling at them.\x02\x03",
            "#05520FMishy is a healing character, so\x01",
            "even when driving kids away, you\x01",
            "can't just do whatever you like.\x02\x03",
            "#05522FFrom your good judgment, I would\x01",
            "expect no less.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05202FHaha... Thanks.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CE6")

    label("loc_5B66")

    OP_99(0x103, 0x101, 0xFA, 0x1388, 0x0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 700, 450, -35880, 315, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(645, 0, 30, 0)
    Sound(862, 0, 50, 0)
    Sound(811, 0, 100, 0)
    OP_9B(0x1, 0x103, 0xB4, 0x3E8, 0x1388, 0x0)
    Sleep(500)
    Sound(2031, 255, 100, 0)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05211FAck!?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)
    Sound(2681, 255, 100, 0)

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05531F...No good at all.\x02\x03",
            "#05526FMishy is a healing character, so\x01",
            "even when driving kids away, you\x01",
            "can't just do whatever you like.\x02\x03",
            "#05520FYou should've chosen a more\x01",
            "peaceful method.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206FT-This sure is tough...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CE6")


    ChrTalk(
        0x109,
        (
            "#10100FWell, I'm just glad they\x01",
            "didn't kick Tio.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FHehe, just like a knight\x01",
            "protecting his little\x01",
            "sister, eh?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206FThat doesn't exactly\x01",
            "match our outfits, now\x01",
            "does it...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05524FIncidentally, I heard that Mishy's\x01",
            "butt is sturdy, so even if kicked\x01",
            "you should be all right.\x02\x03",
            "#05520FIt hurt less than expected, right?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05205FT-That is true...\x02\x03",
            "#05203F(They've even got\x01",
            "cushioning in there. It's\x01",
            "no wonder it's stiff...)\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520F...Ah, Lloyd. It's time\x01",
            "to go to the next area.\x02\x03",
            "#05524FWe have a tight schedule\x01",
            "this morning.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05204FG-Got it. ...Then, see\x01",
            "you later, Noｱl, Wazy.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FPlease, do your best!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHehe, later.\x02",
    )

    CloseMessageWindow()

    def lambda_5FA9():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5FA9)
    Sleep(1000)

    def lambda_5FC6():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5FC6)
    Sleep(50)

    def lambda_5FE3():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5FE3)
    Sleep(50)

    def lambda_5FF3():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5FF3)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("t1330", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_37_4DAE end

    def Function_38_6016(): pass

    label("Function_38_6016")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_6050")
    OP_99(0xFE, 0x101, 0xFA, 0x1388, 0x0)
    Sound(811, 0, 60, 0)
    Sound(862, 0, 20, 0)
    OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x1388, 0x0)
    Sleep(500)
    Jump("Function_38_6016")

    label("loc_6050")

    Return()

    # Function_38_6016 end

    def Function_39_6051(): pass

    label("Function_39_6051")

    Sleep(1000)

    label("loc_6054")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6076")
    Sound(918, 0, 70, 0)
    Sleep(2200)
    Sound(918, 0, 60, 0)
    Sleep(5000)
    Jump("loc_6054")

    label("loc_6076")

    Return()

    # Function_39_6051 end

    SaveToFile()

Try(main)
