from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1010.bin",                # FileName
        "t1010",                    # MapName
        "t1010",                    # Location
        0x0045,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 69, 0, 3, 0, 4],
    )

    BuildStringList((
        "t1010",                  # 0
        "Amy",                    # 1
        "Zell",                   # 2
        "Cabilan",                # 3
        "Loogman",                # 4
        "Mrs. Margaret",          # 5
        "イベント用モンスター",   # 6
        "イベント用モンスター",   # 7
        "イベント用モンスター",   # 8
        "イベント用モンスター",   # 9
        "イベント用モンスター",   # 10
        "イベント用モンスター",   # 11
        "イベント用モンスター",   # 12
        "イベント用モンスター",   # 13
        "bt1010",                 # 14
        "To Guest House",         # 15
        "To Hotel Delphinia",     # 16
    ))

    ATBonus("ATBonus_2CC", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_38C", 8, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_390", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_394", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_398", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_39C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_36C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_370", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_374", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_378", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_37C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_380", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_384", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_388", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_3AC", 0x004A, 255, 6, 45, 3, 3, 30, 0, "bt1010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms86100.dat", "ms82002.dat", "ms82002.dat", "ms82002.dat", 0, 0, 0, 0, "MonsterBattlePostion_38C", "MonsterBattlePostion_36C", "ed7540", "ed7453", "ATBonus_2CC"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch22302.itc",                   # 00
        "chr/ch22202.itc",                   # 01
        "chr/ch33100.itc",                   # 02
        "chr/ch33000.itc",                   # 03
        "chr/ch44000.itc",                   # 04
    ))

    DeclNpc(2279,    4294963596, 4294954866, 180,  325,  0x0, 0,   0,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(3660,    4294963596, 4294954866, 180,  325,  0x0, 0,   1,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(26860,   4294965296, 2200,    270,  257,  0x0, 0,   2,   0,   0,   1,   0,   8,   255,  0)
    DeclNpc(4294965326, 4294965296, 34720,   180,  257,  0x0, 0,   3,   0,   0,   2,   0,   9,   255,  0)
    DeclNpc(4294961066, 4294965497, 0,       0,    389,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 11,  5.5,                   0.0,                   -3.0,                  400.0,                 [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.09999999403953552,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -1.375,                -0.0,                  0.5999999642372131,    1.0])

    PlaceName(-5.0, 0.0, 81.0, 0x0000, 0x0000, "To Guest House")
    PlaceName(65.0, 0.0, 0.0, 0x0000, 0x0000, "To Hotel Delphinia")

    ChipFrameInfo(1072, 0)                                       # 0

    ScpFunction((
        "Function_0_430",          # 00, 0
        "Function_1_4E8",          # 01, 1
        "Function_2_549",          # 02, 2
        "Function_3_5AA",          # 03, 3
        "Function_4_614",          # 04, 4
        "Function_5_6B2",          # 05, 5
        "Function_6_7E7",          # 06, 6
        "Function_7_A92",          # 07, 7
        "Function_8_BCE",          # 08, 8
        "Function_9_F77",          # 09, 9
        "Function_10_12CD",        # 0A, 10
        "Function_11_13F8",        # 0B, 11
        "Function_12_1AE1",        # 0C, 12
        "Function_13_1B00",        # 0D, 13
        "Function_14_1B1F",        # 0E, 14
        "Function_15_1B3C",        # 0F, 15
    ))


    def Function_0_430(): pass

    label("Function_0_430")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_470"),
        (1, "loc_47C"),
        (2, "loc_488"),
        (3, "loc_494"),
        (4, "loc_4A0"),
        (5, "loc_4AC"),
        (6, "loc_4B8"),
        (SWITCH_DEFAULT, "loc_4C4"),
    )


    label("loc_470")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_4D0")

    label("loc_47C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_4D0")

    label("loc_488")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_4D0")

    label("loc_494")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_4D0")

    label("loc_4A0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_4D0")

    label("loc_4AC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_4D0")

    label("loc_4B8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4D0")

    label("loc_4C4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4D0")

    label("loc_4D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4E7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4D0")

    label("loc_4E7")

    Return()

    # Function_0_430 end

    def Function_1_4E8(): pass

    label("Function_1_4E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_548")
    OP_95(0xFE, 26860, -2000, 2200, 2000, 0x0)
    OP_95(0xFE, -4019, -1800, 2200, 2000, 0x0)
    OP_95(0xFE, -3510, -1800, -1500, 2000, 0x0)
    OP_95(0xFE, 26860, -2000, -2060, 2000, 0x0)
    Jump("Function_1_4E8")

    label("loc_548")

    Return()

    # Function_1_4E8 end

    def Function_2_549(): pass

    label("Function_2_549")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5A9")
    OP_95(0xFE, -1970, -2000, 34720, 2000, 0x0)
    OP_95(0xFE, -1970, -2000, 8940, 2000, 0x0)
    OP_95(0xFE, 2029, -2000, 8940, 2000, 0x0)
    OP_95(0xFE, 2029, -2000, 34720, 2000, 0x0)
    Jump("Function_2_549")

    label("loc_5A9")

    Return()

    # Function_2_549 end

    def Function_3_5AA(): pass

    label("Function_3_5AA")

    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrSubChip(0x8, 0x1)
    SetChrFlags(0x8, 0x10)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrSubChip(0x9, 0x2)
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_5FB")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)

    label("loc_5FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_613")
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)

    label("loc_613")

    Return()

    # Function_3_5AA end

    def Function_4_614(): pass

    label("Function_4_614")

    SetMapObjFrame(0xFF, "t1010_sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "t1010_sky_y", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_64A")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_64A")

    Sound(126, 1, 80, 0)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_668")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_668")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_68F")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Jump("loc_6B1")

    label("loc_68F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_6B1")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)

    label("loc_6B1")

    Return()

    # Function_4_614 end

    def Function_5_6B2(): pass

    label("Function_5_6B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_6C3")
    Jump("loc_7DF")

    label("loc_6C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_74A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DE")
    Call(0, 6)
    Jump("loc_745")

    label("loc_6DE")


    ChrTalk(
        0x8,
        "Oh Zell, that's no good, really no good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's improper for a gentleman \x01",
            "to embarrass a lady.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_745")

    Jump("loc_7DF")

    label("loc_74A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_7DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_765")
    Call(0, 6)
    Jump("loc_7DF")

    label("loc_765")


    ChrTalk(
        0x8,
        "Oh Zell, that's no good, really no good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even in order to become my amazing husband,\x01",
            "you must do at least that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DF")

    TalkEnd(0xFE)
    SetChrSubChip(0x8, 0x1)
    Return()

    # Function_5_6B2 end

    def Function_6_7E7(): pass

    label("Function_6_7E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_91B")

    ChrTalk(
        0x8,
        (
            "Listen, Zell?\x01",
            "Because you're my fiancｳe, I think\x01",
            "you need to look into the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            ""The most ideal thing is to have a girl first and\x01",
            "then a boy", mama said. What do you think...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "A girl's first and then a boy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "W-What're you talking about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "...I-It's nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "???\x02",
    )

    CloseMessageWindow()
    Jump("loc_A84")

    label("loc_91B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_A84")

    ChrTalk(
        0x8,
        (
            "Listen, Zell?\x01",
            "Because you're my fiancｳe,\x01",
            "you must become a cool man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Smart, athletic and\x01",
            "a man kind to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "E-Even if you tell me that...\x01",
            "How should I do that concretely?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "First, begin with doing 100\x01",
            "push-ups and sit-ups a day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then, I will only allow you to score\x01",
            "full in the Sunday School's tests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "D-Don't say nonsense...\x02",
    )

    CloseMessageWindow()

    label("loc_A84")

    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_6_7E7 end

    def Function_7_A92(): pass

    label("Function_7_A92")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_AA3")
    Jump("loc_BC6")

    label("loc_AA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_B33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ABE")
    Call(0, 6)
    Jump("loc_B2E")

    label("loc_ABE")


    ChrTalk(
        0x9,
        (
            "Sometimes I don't understand\x01",
            "well what Amy says.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "A girl first and then a boy...\x01",
            "What could that mean?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B2E")

    Jump("loc_BC6")

    label("loc_B33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_BC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B4E")
    Call(0, 6)
    Jump("loc_BC6")

    label("loc_B4E")


    ChrTalk(
        0x9,
        "Amy has got too grand expectations.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Life is already difficult\x01",
            "the way it is even if\x01",
            "she doesn't rise the bar.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BC6")

    TalkEnd(0xFE)
    SetChrSubChip(0x9, 0x2)
    Return()

    # Function_7_A92 end

    def Function_8_BCE(): pass

    label("Function_8_BCE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_BDF")
    Jump("loc_F73")

    label("loc_BDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_D5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D09")

    ChrTalk(
        0xA,
        (
            "Hmph, you commoners,\x01",
            "what're you doing here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01105FWhat?\x02",
    )

    CloseMessageWindow()
    OP_63(0x153, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sound(822, 0, 100, 0)
    Sleep(1000)
    OP_63(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_64(0x153)

    ChrTalk(
        0xA,
        "...No, it's nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "And because it's nothing,\x01",
            "don't look at me with such\x01",
            "a carefree smile...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F(Ha ha...KeA is invincible.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D5A")

    label("loc_D09")


    ChrTalk(
        0xA,
        "...Go away.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Now I feel ashamed for having\x01",
            "said stupid bitter things...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D5A")

    Jump("loc_F73")

    label("loc_D5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_DFB")

    ChrTalk(
        0xA,
        (
            "It's like I saw that green-haired little\x01",
            "girl who went to the guest house\x01",
            "just now a very long time ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Wait, when was it again?\x02",
    )

    CloseMessageWindow()
    Jump("loc_F73")

    label("loc_DFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_F73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F04")

    ChrTalk(
        0xA,
        "Oh, what business do you have here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "This high class residential area is a place\x01",
            "commoners have nothing to do with...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...Hmph, well, all right.\x01",
            "Burn into your eyes as much as possible\x01",
            "how the mansions of us rich people are.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F73")

    label("loc_F04")


    ChrTalk(
        0xA,
        (
            "...Hmph, well, all right.\x01",
            "Burn into your eyes as much as possible\x01",
            "how the mansions of us rich people are.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F73")

    TalkEnd(0xFE)
    Return()

    # Function_8_BCE end

    def Function_9_F77(): pass

    label("Function_9_F77")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_F88")
    Jump("loc_12C9")

    label("loc_F88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1098")

    ChrTalk(
        0xB,
        (
            "After former Chairman Hartmann lost his\x01",
            "standing, even sightings of suspicious\x01",
            "people around here have almost vanished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "After all, by turning that residence into a\x01",
            "guest house, vigilance has intensified.\x01",
            "Public order too has improved considerably.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12C9")

    label("loc_1098")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_12C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11E9")

    ChrTalk(
        0xB,
        (
            "A little time ago, former Chairman Hartmann's\x01",
            "residence was turned into a guest house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It was used to welcome every\x01",
            "countries' VIPs during the\x01",
            "recent Trade Conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Compared to the period when suspicious\x01",
            "parties were held, it can be said it's really\x01",
            "become a worthwhile and good clean place.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_12C9")

    label("loc_11E9")


    ChrTalk(
        0xB,
        (
            "A little time ago, former Chairman Hartmann's\x01",
            "residence was turned into a guest house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Compared to the period when suspicious\x01",
            "parties were held, it can be said it's really\x01",
            "become a worthwhile and good clean place.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12C9")

    TalkEnd(0xFE)
    Return()

    # Function_9_F77 end

    def Function_10_12CD(): pass

    label("Function_10_12CD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1378")

    ChrTalk(
        0xFE,
        (
            "The mansion featured in the\x01",
            "pamphlet seems to be this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A location where you can have an unbroken\x01",
            "view of the lake... It's quite nice.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_13F4")

    label("loc_1378")


    ChrTalk(
        0xFE,
        (
            "A location where you can have an unbroken\x01",
            "view of the lake... It's quite nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Maybe I should really purchase it.\x02",
    )

    CloseMessageWindow()

    label("loc_13F4")

    TalkEnd(0xFE)
    Return()

    # Function_10_12CD end

    def Function_11_13F8(): pass

    label("Function_11_13F8")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00250.itc", 0x1F)
    LoadChrToIndex("chr/ch00350.itc", 0x20)
    LoadChrToIndex("chr/ch02950.itc", 0x21)
    LoadChrToIndex("chr/ch03150.itc", 0x22)
    LoadChrToIndex("chr/ch03250.itc", 0x23)
    LoadChrToIndex("monster/ch82050.itc", 0x24)
    LoadChrToIndex("monster/ch82051.itc", 0x25)
    LoadChrToIndex("monster/ch86150.itc", 0x26)
    LoadChrToIndex("monster/ch86151.itc", 0x27)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_90(0x101, 5500, 0, 2000, 315)
    OP_90(0x104, 6500, 0, 2000, 315)
    OP_90(0x103, 6500, 0, 500, 315)
    OP_90(0x109, 5500, 0, 500, 315)
    OP_90(0x105, 7500, 0, 1250, 315)
    OP_90(0x106, 4500, 0, 1250, 315)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrChipByIndex(0xD, 0x24)
    SetChrChipByIndex(0xE, 0x24)
    SetChrChipByIndex(0xF, 0x24)
    SetChrChipByIndex(0x10, 0x24)
    SetChrChipByIndex(0x12, 0x26)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0xF, 0x0)
    SetChrSubChip(0x10, 0x0)
    SetChrSubChip(0x11, 0x0)
    SetChrSubChip(0x12, 0x0)
    SetChrSubChip(0x13, 0x0)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xE, 0x20)
    SetChrFlags(0xF, 0x20)
    SetChrFlags(0x10, 0x20)
    SetChrFlags(0x11, 0x20)
    SetChrFlags(0x12, 0x20)
    SetChrFlags(0x13, 0x20)
    SetChrFlags(0x14, 0x20)
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xD, 0, 0, 12)
    BeginChrThread(0xE, 0, 0, 12)
    BeginChrThread(0xF, 0, 0, 12)
    BeginChrThread(0x10, 0, 0, 12)
    BeginChrThread(0x12, 0, 0, 14)
    SetChrPos(0xE, -1800, -2000, 19500, 180)
    SetChrPos(0xF, 0, -2000, 18500, 180)
    SetChrPos(0x10, 1800, -2000, 19500, 180)
    SetChrPos(0x12, 0, -2000, 22500, 180)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0x10, 0x8)
    SetChrFlags(0x11, 0x8)
    SetChrFlags(0x12, 0x8)
    SetChrFlags(0x13, 0x8)
    SetChrFlags(0x14, 0x8)
    FadeToBright(1000, 0)
    OP_68(2700, -500, 1500, 0)
    OP_68(0, -500, 4500, 2500)
    MoveCamera(315, 33, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)

    def lambda_16A9():
        OP_95(0xFE, -1500, 0, 4250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_16A9)
    Sleep(50)

    def lambda_16C6():
        OP_95(0xFE, -500, 0, 5000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16C6)
    Sleep(50)

    def lambda_16E3():
        OP_95(0xFE, 500, 0, 5000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_16E3)
    Sleep(50)

    def lambda_1700():
        OP_95(0xFE, -500, 0, 3500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1700)
    Sleep(50)

    def lambda_171D():
        OP_95(0xFE, 500, 0, 3500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_171D)
    Sleep(50)

    def lambda_173A():
        OP_95(0xFE, 1500, 0, 4250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_173A)
    Sleep(800)
    Sound(948, 0, 30, 0)
    Sound(911, 0, 100, 0)
    WaitChrThread(0x106, 1)

    def lambda_1767():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_1767)
    WaitChrThread(0x101, 1)

    def lambda_1778():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1778)
    WaitChrThread(0x104, 1)

    def lambda_1789():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1789)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    WaitChrThread(0x109, 1)

    def lambda_1830():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1830)
    WaitChrThread(0x103, 1)

    def lambda_1841():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1841)
    WaitChrThread(0x105, 1)

    def lambda_1852():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1852)
    OP_6F(0x79)
    OP_0D()
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0xF, 0x8)
    ClearChrFlags(0x10, 0x8)
    ClearChrFlags(0x12, 0x8)
    OP_68(150, -500, 18040, 2000)
    MoveCamera(321, 21, 0, 2000)
    OP_6E(400, 2000)
    SetCameraDistance(25000, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00010F#2PCrap, other military monsters!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00307F#2PThat's a red lion──watch out!\x02",
    )

    CloseMessageWindow()
    OP_68(0, -500, 8000, 1100)
    SetCameraDistance(18000, 1100)
    Sound(911, 0, 80, 0)
    Sound(948, 0, 100, 0)
    SetChrChipByIndex(0xE, 0x25)
    BeginChrThread(0xE, 0, 0, 13)

    def lambda_1934():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1934)
    Sleep(50)
    SetChrChipByIndex(0xF, 0x25)
    BeginChrThread(0xF, 0, 0, 13)

    def lambda_1956():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1956)
    Sleep(50)
    SetChrChipByIndex(0x10, 0x25)
    BeginChrThread(0x10, 0, 0, 13)

    def lambda_1978():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1978)
    Sleep(50)
    SetChrChipByIndex(0x12, 0x27)
    BeginChrThread(0x12, 0, 0, 15)

    def lambda_199A():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_199A)
    Sleep(50)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0x23)
    SetChrSubChip(0x106, 0x0)
    Sleep(700)
    BlurSwitch(0x64, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(18000, 300)
    Sleep(300)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x10, 0x1)
    EndChrThread(0x11, 0x1)
    EndChrThread(0x12, 0x1)
    EndChrThread(0x13, 0x1)
    EndChrThread(0x14, 0x1)
    EndChrThread(0xD, 0x0)
    EndChrThread(0xE, 0x0)
    EndChrThread(0xF, 0x0)
    EndChrThread(0x10, 0x0)
    EndChrThread(0x11, 0x0)
    EndChrThread(0x12, 0x0)
    EndChrThread(0x13, 0x0)
    EndChrThread(0x14, 0x0)
    Battle("BattleInfo_3AC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrPos(0x0, 0, -1800, 6000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A3, 7)
    ModifyEventFlags(0, 0, 0x80)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_11_13F8 end

    def Function_12_1AE1(): pass

    label("Function_12_1AE1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1AFF")
    OP_A1(0xFE, 0x6A4, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_12_1AE1")

    label("loc_1AFF")

    Return()

    # Function_12_1AE1 end

    def Function_13_1B00(): pass

    label("Function_13_1B00")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1B1E")
    OP_A1(0xFE, 0xBB8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_13_1B00")

    label("loc_1B1E")

    Return()

    # Function_13_1B00 end

    def Function_14_1B1F(): pass

    label("Function_14_1B1F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1B3B")
    OP_A1(0xFE, 0x5DC, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_14_1B1F")

    label("loc_1B3B")

    Return()

    # Function_14_1B1F end

    def Function_15_1B3C(): pass

    label("Function_15_1B3C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1B58")
    OP_A1(0xFE, 0x960, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_15_1B3C")

    label("loc_1B58")

    Return()

    # Function_15_1B3C end

    SaveToFile()

Try(main)
