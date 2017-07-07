from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1050.bin",                # FileName
        "t1050",                    # MapName
        "t1050",                    # Location
        0x0042,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 66, 0, 3, 0, 4],
    )

    BuildStringList((
        "t1050",                  # 0
        "Hagger manager",           # 1
        "Roche",               # 2
        "Citrus",               # 3
        "Engineer",                   # 4
        "fortune teller",                 # 5
        "Keya",                 # 6
        "Franc",                 # 7
        "Cecil",                 # 8
        "Ilia",                 # 9
        "Lisha",               # 10
        "Shuri",                 # 11
        "Marybele",             # 12
    ))

    AddCharChip((
        "chr/ch25800.itc",                   # 00
        "chr/ch25700.itc",                   # 01
        "chr/ch25600.itc",                   # 02
        "chr/ch26000.itc",                   # 03
        "chr/ch14202.itc",                   # 04
    ))

    DeclNpc(4294966817, 0,       10050,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4294873337, 0,       8260,    0,    385,  0x0, 0,   1,   0,   0,   1,   0,   8,   255,  0)
    DeclNpc(4294865477, 0,       8859,    90,   389,  0x0, 0,   2,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(1059,    0,       10489,   177,  389,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(4294953937, 150,     15430,   90,   453,  0x0, 0,   4,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(5500,    0,       13500,   1200,    5500,    1500,    13500,   0x007C, 0,  30, 0x0000)
    DeclActor(4294967276, 0,       8270,    1500,    4294966816, 1500,    10050,   0x007E, 0,  6,  0x0000)
    DeclActor(12010,   0,       15830,   1200,    12010,   450,     15830,   0x007C, 0,  5,  0x0000)
    DeclActor(1260,    0,       9210,    1500,    1060,    1500,    10490,   0x007E, 0,  11, 0x0000)

    ChipFrameInfo(772, 0)                                        # 0

    ScpFunction((
        "Function_0_304",          # 00, 0
        "Function_1_3BC",          # 01, 1
        "Function_2_41D",          # 02, 2
        "Function_3_47E",          # 03, 3
        "Function_4_586",          # 04, 4
        "Function_5_5D3",          # 05, 5
        "Function_6_688",          # 06, 6
        "Function_7_68C",          # 07, 7
        "Function_8_1035",         # 08, 8
        "Function_9_159F",         # 09, 9
        "Function_10_16EE",        # 0A, 10
        "Function_11_19D3",        # 0B, 11
        "Function_12_19D7",        # 0C, 12
        "Function_13_1BCC",        # 0D, 13
        "Function_14_28F3",        # 0E, 14
        "Function_15_2953",        # 0F, 15
        "Function_16_2EC1",        # 10, 16
        "Function_17_317E",        # 11, 17
        "Function_18_31FA",        # 12, 18
        "Function_19_327B",        # 13, 19
        "Function_20_32FC",        # 14, 20
        "Function_21_337D",        # 15, 21
        "Function_22_33FE",        # 16, 22
        "Function_23_347F",        # 17, 23
        "Function_24_3500",        # 18, 24
        "Function_25_3581",        # 19, 25
        "Function_26_3602",        # 1A, 26
        "Function_27_3683",        # 1B, 27
        "Function_28_3704",        # 1C, 28
        "Function_29_3785",        # 1D, 29
        "Function_30_3806",        # 1E, 30
    ))


    def Function_0_304(): pass

    label("Function_0_304")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_344"),
        (1, "loc_350"),
        (2, "loc_35C"),
        (3, "loc_368"),
        (4, "loc_374"),
        (5, "loc_380"),
        (6, "loc_38C"),
        (SWITCH_DEFAULT, "loc_398"),
    )


    label("loc_344")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_350")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_35C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_368")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_374")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_380")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_38C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_398")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_3A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3BB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_3BB")

    Return()

    # Function_0_304 end

    def Function_1_3BC(): pass

    label("Function_1_3BC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_41C")
    OP_95(0xFE, -106030, 0, 8260, 2000, 0x0)
    OP_95(0xFE, -106030, 0, 11300, 2000, 0x0)
    OP_95(0xFE, -93960, 0, 11300, 2000, 0x0)
    OP_95(0xFE, -93960, 0, 8260, 2000, 0x0)
    Jump("Function_1_3BC")

    label("loc_41C")

    Return()

    # Function_1_3BC end

    def Function_2_41D(): pass

    label("Function_2_41D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_47D")
    OP_95(0xFE, 106130, 0, 11580, 2000, 0x0)
    OP_95(0xFE, 106130, 0, 8150, 2000, 0x0)
    OP_95(0xFE, 94190, 0, 8150, 2000, 0x0)
    OP_95(0xFE, 94190, 0, 11580, 2000, 0x0)
    Jump("Function_2_41D")

    label("loc_47D")

    Return()

    # Function_2_41D end

    def Function_3_47E(): pass

    label("Function_3_47E")

    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4C8")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 106130, 0, 11580, 0)
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_576")

    label("loc_4C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_521")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 4270, 0, 7670, 90)
    BeginChrThread(0x9, 0, 0, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 5450, 0, 7670, 270)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51C")
    SetChrFlags(0xC, 0x10)

    label("loc_51C")

    Jump("loc_576")

    label("loc_521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_52F")
    Jump("loc_576")

    label("loc_52F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_568")
    BeginChrThread(0x9, 0, 0, 0)
    SetChrPos(0x9, -100710, 0, 8860, 270)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_576")

    label("loc_568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_576")
    ClearChrFlags(0x9, 0x80)

    label("loc_576")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_585")
    ClearScenarioFlags(0x22, 0)
    Event(0, 16)

    label("loc_585")

    Return()

    # Function_3_47E end

    def Function_4_586(): pass

    label("Function_4_586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_598")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_598")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_5AF")
    ClearMapObjFlags(0x0, 0x10)
    OP_66(0x0, 0x1)

    label("loc_5AF")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5C5")
    OP_66(0x3, 0x1)
    Jump("loc_5D2")

    label("loc_5C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5D2")
    OP_66(0x3, 0x1)

    label("loc_5D2")

    Return()

    # Function_4_586 end

    def Function_5_5D3(): pass

    label("Function_5_5D3")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "\"Recipe collection that I love the holiday carefully selected\".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('料理手册', 0x0)"), scpexpr(EXPR_END)), "loc_684")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x15)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_684")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "\"Commitment Matcha Latte\"\x07\x00",
            "I learned the recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_684")

    TalkEnd(0xFF)
    Return()

    # Function_5_5D3 end

    def Function_6_688(): pass

    label("Function_6_688")

    Call(0, 7)
    Return()

    # Function_6_688 end

    def Function_7_68C(): pass

    label("Function_7_68C")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_699")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1031")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",        # 0
            "To take a break\x01",      # 1
            "quit\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F5")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_6F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_715")
    OP_AF(0x64)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_102C")

    label("loc_715")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_102C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_89F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81E")

    ChrTalk(
        0x8,
        (
            "Since the fuss in the town fell,\x01",
            "Everyone has come to see the state of the hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, that mysterious pale big tree …\x01",
            "It is more eerie to see it closer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As I knew, for the time being,\x01",
            "Restarting Michelam will be difficult.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_89A")

    label("loc_81E")


    ChrTalk(
        0x8,
        (
            "Although Michelam's resumption will still be ahead … …\x01",
            "It is that it is coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At the time of break,\x01",
            "Please do not hesitate to tell us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89A")

    Jump("loc_102C")

    label("loc_89F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_9EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_978")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Ooo, Mr. Lloyd ……\x01",
            "I often came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although our hotel is closed,\x01",
            "Ready to accept customers\x01",
            "We are in place at any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Please tell us when you have a break.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9EA")

    label("loc_978")


    ChrTalk(
        0x8,
        (
            "Hmm, even then,\x01",
            "Why the sound of such a bell …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "MWL is supposed to be closed, but …\x01",
            "It is strange.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9EA")

    Jump("loc_102C")

    label("loc_9EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_9FD")
    Jump("loc_102C")

    label("loc_9FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_D3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C0A")

    ChrTalk(
        0x8,
        (
            "おお、ロイド様にKeya様。\x01",
            "Please do not leave this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "It seems I have met you, than anything else.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01110FEh, I'm back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FI am sorry for making you worry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "No, there is no disappearance …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, the way you took me\x01",
            "It seems that it went out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "After each, I completed errands\x01",
            "Things that go to the meeting place …\x01",
            "Why should I hurry?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FI agree,\x01",
            "Thank you very much.\x02\x03",
            "#00000FWell then,\x01",
            "When we got errands as well\x01",
            "Shall we go to the theme park?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01109FYes, Let's go!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15A, 7)
    Jump("loc_D37")

    label("loc_C0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC7")

    ChrTalk(
        0x8,
        (
            "The way you took me a while ago\x01",
            "It seems that it went out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "After each, I completed errands\x01",
            "I'm going to the meeting place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Mr. Lloyd, soon.\x01",
            "Is it better to be headed?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D37")

    label("loc_CC7")


    ChrTalk(
        0x8,
        (
            "The way you took me a while ago\x01",
            "It seems that it went out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Mr. Lloyd, soon.\x01",
            "Is it better to be headed?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D37")

    Jump("loc_102C")

    label("loc_D3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_EA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E30")

    ChrTalk(
        0x8,
        (
            "先ほどKeya様がお一人で\x01",
            "It seems that it went out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I just wanted to hear your voice, just in case,\x01",
            "I was told not to worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F（Keya……\x01",
            "After all, outside the hotel\x01",
            "You might as well look for it. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EA0")

    label("loc_E30")


    ChrTalk(
        0x8,
        (
            "先ほどKeya様がお一人で\x01",
            "It seems that it went out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, where is this\x01",
            "I guess it went off.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EA0")

    Jump("loc_102C")

    label("loc_EA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_102C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F9F")

    ChrTalk(
        0x8,
        (
            "This is for everyone ……\x01",
            "The comfort of the 3rd floor VIP floor\x01",
            "How is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, it's very comfortable.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "That's more than anything.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If there are no points\x01",
            "Please let me know soon.\x01",
            "Because I will correspond as soon as possible.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_102C")

    label("loc_F9F")


    ChrTalk(
        0x8,
        (
            "The comfort of the 3rd floor VIP floor\x01",
            "How is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If there are no points\x01",
            "Please let me know soon.\x01",
            "Because I will correspond as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_102C")

    Jump("loc_699")

    label("loc_1031")

    TalkEnd(0x8)
    Return()

    # Function_7_68C end

    def Function_8_1035(): pass

    label("Function_8_1035")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_115F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10D3")

    ChrTalk(
        0x9,
        (
            "Because it was left for a while,\x01",
            "It seems like dust is accumulating fairly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ha … … pear tree is uneasy,\x01",
            "I have to clean it properly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_115A")

    label("loc_10D3")


    ChrTalk(
        0x9,
        (
            "To be able to resume at any time,\x01",
            "I'm coming to clean up on a regular basis ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Such a pale tree\x01",
            "Things that are near that,\x01",
            "It sounds anxious.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_115A")

    Jump("loc_159B")

    label("loc_115F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1302")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1268")

    ChrTalk(
        0x9,
        (
            "Later on, I became Secretary of Defense\x01",
            "That Arios,\x01",
            "I went through the arcade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "A cute little girl\x01",
            "It seems I was taking a … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F（アリオスさんとKeya……\x01",
            "I guess it was coming. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F(Let's chase soon.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_12FD")

    label("loc_1268")


    ChrTalk(
        0x9,
        (
            "A little earlier, Secretary of Defense Arios\x01",
            "I went through the arcade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Take a little girl\x01",
            "It seems I went to a theme park ….\x01",
            "What on earth is it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12FD")

    Jump("loc_159B")

    label("loc_1302")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1310")
    Jump("loc_159B")

    label("loc_1310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1389")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_132B")
    Call(0, 9)
    Jump("loc_1384")

    label("loc_132B")


    ChrTalk(
        0xFE,
        (
            "Please,\x01",
            "I'd like to take care of Mr. Wado ~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I will treat you like gelato next time!\x02",
    )

    CloseMessageWindow()

    label("loc_1384")

    Jump("loc_159B")

    label("loc_1389")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_159B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1516")
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(
        0xFE,
        "Well, the guest … … like a wad! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, maybe,\x01",
            "I will stay on the VIP floor today.\x01",
            "Customer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FOh, in that case\x01",
            "I think we are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It is! It is! It is! It is! It is! It is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(Oh, when I see ……\x01",
            "Why on such a day only on the general floor\x01",
            "I was in charge! It is! )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FNo, I do not know anything.\x01",
            "You seem to be shocked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302FHuh, you are a funny child.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_159B")

    label("loc_1516")


    ChrTalk(
        0xFE,
        (
            "Oh, when I do … …\x01",
            "For general days only on such days\x01",
            "I will be in charge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can take care of Wadayama\x01",
            "It was a chance … ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_159B")

    TalkEnd(0xFE)
    Return()

    # Function_8_1035 end

    def Function_9_159F(): pass

    label("Function_9_159F")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x9,
        "ねっ、Citrusお願いっ！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I have a wanderer today.\x01",
            "Let me dive on the VIP floor ~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Call me while I was working.\x01",
            "If I think something ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Generally speaking, you mean\x01",
            "\"I take care of VIP floor care.\"\x01",
            "Saying that, it was not against me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, there somehow ~.\x01",
            "I will treat you like gelato next time!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_9_159F end

    def Function_10_16EE(): pass

    label("Function_10_16EE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1852")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17CA")

    ChrTalk(
        0xA,
        (
            "In the guest house,\x01",
            "McDaill's chairman\x01",
            "I wish you were confined.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Moreover, to the hunters who struck the streets\x01",
            "I guess I was watching you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Although for independence,\x01",
            "The President also does a terrible thing …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_184D")

    label("loc_17CA")


    ChrTalk(
        0xA,
        (
            "In the guest house,\x01",
            "McDaill's chairman\x01",
            "I wish you were confined.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The President also does a terrible thing …\x01",
            "I was glad I was caught.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_184D")

    Jump("loc_19CF")

    label("loc_1852")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_193F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18FD")

    ChrTalk(
        0xA,
        (
            "Sitting in the direction of her,\x01",
            "テーマパークで働いてるfortune tellerさんよね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It seems that it appeared unexpectedly ….\x01",
            "Where do you usually live?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_193A")

    label("loc_18FD")


    ChrTalk(
        0xA,
        (
            "…… Oops, do not talk\x01",
            "I have to clean up thoroughly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_193A")

    Jump("loc_19CF")

    label("loc_193F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_194D")
    Jump("loc_19CF")

    label("loc_194D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_19C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1968")
    Call(0, 9)
    Jump("loc_19C1")

    label("loc_1968")


    ChrTalk(
        0xFE,
        (
            "Already, if it says so far\x01",
            "I can give it to you, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It is totally selfish.\x02",
    )

    CloseMessageWindow()

    label("loc_19C1")

    Jump("loc_19CF")

    label("loc_19C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_19CF")

    label("loc_19CF")

    TalkEnd(0xFE)
    Return()

    # Function_10_16EE end

    def Function_11_19D3(): pass

    label("Function_11_19D3")

    Call(0, 12)
    Return()

    # Function_11_19D3 end

    def Function_12_19D7(): pass

    label("Function_12_19D7")

    TalkBegin(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_19E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BC8")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",            # 0
            "To remodel and synthesize\x01",      # 1
            "quit\x01",              # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A44")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1A44")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A64")
    OP_AF(0x65)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BC3")

    label("loc_1A64")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BC3")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1B1E")

    ChrTalk(
        0xB,
        (
            "Such an incomprehensible man\x01",
            "Even though it appears, the staff here\x01",
            "It is quite sitting there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "… … Finish maintenance sooner\x01",
            "I want to get away from here quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC3")

    label("loc_1B1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1BC3")

    ChrTalk(
        0xB,
        (
            "Just with the people of the hotel,\x01",
            "Maintenance of facilities that are closed\x01",
            "That's where I came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you have something else\x01",
            "Please do not hesitate to say.\x01",
            "I will help you in one hand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BC3")

    Jump("loc_19E4")

    label("loc_1BC8")

    TalkEnd(0xB)
    Return()

    # Function_12_19D7 end

    def Function_13_1BCC(): pass

    label("Function_13_1BCC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_228E")
    Call(0, 14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F11")
    EventBegin(0x0)
    Fade(500)
    OP_68(-13160, 1200, 13150, 0)
    MoveCamera(320, 21, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(17640, 0)
    SetChrPos(0x101, -12560, 0, 13000, 0)
    SetChrPos(0x102, -13820, 0, 12710, 45)
    SetChrPos(0x103, -12700, 0, 11800, 0)
    SetChrPos(0x104, -13690, 0, 13610, 45)
    SetChrPos(0xF4, -14000, 0, 11480, 45)
    SetChrPos(0xF5, -14760, 0, 12870, 50)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0xC, 0x2)
    OP_0D()

    ChrTalk(
        0xC,
        "#11POh, that book ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PSometimes I see it in Crossbell City\x01",
            "I wonder if it is \"Agnes of sunshine\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FEr, is it about this novel?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FOnce in a while, the whole volume is gathered.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PHuh, that's great.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PPreviously, I also made that novel\x01",
            "I have the opportunity to pick it up.\x01",
            "I really enjoyed reading it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PIt seems to be a fictional story, but …\x01",
            "There is something in common with the hero's girl\x01",
            "It may have been there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PThe end of the Crossbell incident,\x01",
            "Have a sidelobe from here\x01",
            "I intended to do it ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PWhile reading such a book,\x01",
            "It might be good for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004F(Because it is a point, this person\x01",
            "I wonder if I will give it … ….? )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18A, 5)
    Call(0, 15)
    Jump("loc_2289")

    label("loc_1F11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20B9")
    EventBegin(0x0)
    Fade(500)
    OP_68(-13160, 1200, 13150, 0)
    MoveCamera(320, 21, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(17640, 0)
    SetChrPos(0x101, -12560, 0, 13000, 0)
    SetChrPos(0x102, -13820, 0, 12710, 45)
    SetChrPos(0x103, -12700, 0, 11800, 0)
    SetChrPos(0x104, -13690, 0, 13610, 45)
    SetChrPos(0xF4, -14000, 0, 11480, 45)
    SetChrPos(0xF5, -11330, 0, 11290, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0xC, 0x2)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "#11PI sometimes see it in Crossbell City\x01",
            "\"Book of Agnes of the Yang\" book.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PThe end of the Crossbell incident,\x01",
            "Have a sidelobe from here\x01",
            "I intended to do it ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PWhile reading such a book,\x01",
            "It might be good for you.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 15)
    Jump("loc_2289")

    label("loc_20B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21E5")

    ChrTalk(
        0xC,
        (
            "That blue sky big tree ……\x01",
            "I do not think that such things will emerge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Tarot, crystal, star look … …\x01",
            "Even with all the methods I have,\x01",
            "I can not divine the fate of the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Fuh, funny ……\x01",
            "This is my first time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The cross bell is\x01",
            "What kind of future do you grab ……\x01",
            "Let 's see it here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2289")

    label("loc_21E5")


    ChrTalk(
        0xC,
        (
            "Huh … … \"them\" too\x01",
            "What is the situation so far\x01",
            "You probably did not expect it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The cross bell is\x01",
            "What kind of future do you grab ……\x01",
            "Let 's see it here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2289")

    Jump("loc_28EF")

    label("loc_228E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_28EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_279E")

    ChrTalk(
        0xC,
        "HM…………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_235C")

    ChrTalk(
        0x101,
        (
            "#00005F(this person is……\x01",
            "  テーマパークのfortune tellerさんか？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_237B")

    label("loc_235C")


    ChrTalk(
        0x101,
        "#00005F(this person is……?)\x02",
    )

    CloseMessageWindow()

    label("loc_237B")


    ChrTalk(
        0x102,
        (
            "#00105F(Tarot cards\x01",
            "It seems to be spreading … …)\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x0, 0)
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_244A")
    Jump("loc_2494")

    label("loc_244A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_246A")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2494")

    label("loc_246A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_248A")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2494")

    label("loc_248A")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2494")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)

    ChrTalk(
        0xC,
        "Be careful … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If I'm planning on going ahead … …\x01",
            "Perhaps you will be fierce\x01",
            "It will be a path of difficulty.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#00201F………………! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FWhat, what does that mean …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well …… This esoteric arrangement\x01",
            "How did you read that … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "However, if you go forward\x01",
            "You'd better make up your mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Even with all difficulties\x01",
            "Can I withdraw my precious things ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It is for you\x01",
            "Because it will be.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)

    ChrTalk(
        0x101,
        (
            "#00003F…… I'm not sure but …\x01",
            "I want to keep it in mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Huh, I will pray for a good fight.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x191, 7)
    SetChrSubChip(0xC, 0x0)
    Jump("loc_28EF")

    label("loc_279E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_288A")

    ChrTalk(
        0xC,
        (
            "If you go on ahead\x01",
            "You'd better make up your mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Even with all difficulties\x01",
            "Can I withdraw my precious things ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It is for you\x01",
            "Because it will be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Huh, I will pray for a good fight.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    ClearChrFlags(0xC, 0x10)
    Jump("loc_28EF")

    label("loc_288A")


    ChrTalk(
        0xC,
        (
            "Even with all difficulties\x01",
            "Can I withdraw my precious things ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Huh, I will pray for a good fight.\x02",
    )

    CloseMessageWindow()

    label("loc_28EF")

    TalkEnd(0xFE)
    Return()

    # Function_13_1BCC end

    def Function_14_28F3(): pass

    label("Function_14_28F3")

    ClearScenarioFlags(0x0, 5)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('沐浴阳光的阿尼艾丝１卷', 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber('沐浴阳光的阿尼艾丝２卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('沐浴阳光的阿尼艾丝３卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('沐浴阳光的阿尼艾丝４卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('沐浴阳光的阿尼艾丝５卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('沐浴阳光的阿尼艾丝６卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('沐浴阳光的阿尼艾丝７卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('沐浴阳光的阿尼艾丝８卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('沐浴阳光的阿尼艾丝９卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('沐浴阳光的阿尼艾丝10卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('沐浴阳光的阿尼艾丝11卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('沐浴阳光的阿尼艾丝12卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('沐浴阳光的阿尼艾丝13卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('沐浴阳光的阿尼艾丝14卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2952")
    SetScenarioFlags(0x0, 5)

    label("loc_2952")

    Return()

    # Function_14_28F3 end

    def Function_15_2953(): pass

    label("Function_15_2953")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Pass a novel\x01",      # 0
            "Do not hand it over.\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E5E")

    ChrTalk(
        0x101,
        (
            "#6P#00000FIf you do not mind ……\x01",
            "Shall I hand it over to this book?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11POh … I wonder if it is okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FIf Lloyd said so … …\x01",
            "Originally it is mostly gifts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00300FPlease do not hesitate to receive it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PHuh, I'd appreciate it\x01",
            "I will accept it.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I handed over all of Agnes of the sunshine.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SubItemNumber('沐浴阳光的阿尼艾丝１卷', 1)
    SubItemNumber('沐浴阳光的阿尼艾丝２卷', 1)
    SubItemNumber('沐浴阳光的阿尼艾丝３卷', 1)
    SubItemNumber('沐浴阳光的阿尼艾丝４卷', 1)
    SubItemNumber('沐浴阳光的阿尼艾丝５卷', 1)
    SubItemNumber('沐浴阳光的阿尼艾丝６卷', 1)
    SubItemNumber('沐浴阳光的阿尼艾丝７卷', 1)
    SubItemNumber('沐浴阳光的阿尼艾丝８卷', 1)
    SubItemNumber('沐浴阳光的阿尼艾丝９卷', 1)
    SubItemNumber('沐浴阳光的阿尼艾丝10卷', 1)
    SubItemNumber('沐浴阳光的阿尼艾丝11卷', 1)
    SubItemNumber('沐浴阳光的阿尼艾丝12卷', 1)
    SubItemNumber('沐浴阳光的阿尼艾丝13卷', 1)
    SubItemNumber('沐浴阳光的阿尼艾丝14卷', 1)

    ChrTalk(
        0xC,
        "#11P… That's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PWhat is to say instead, but,\x01",
            "Let's give this to you.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '塞姆里亚石'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('塞姆里亚石', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#6P#00005Fthis is……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PPreviously, from a certain tip\x01",
            "I got it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PWhether you can handle it\x01",
            "I do not know but ….\x01",
            "You should have it if you do not mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FWell, is that okay?\x01",
            "Things that seems to be such valuable ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PHuh, I do not mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PAs the incident swirled in Crossbell,\x01",
            "I am a bystander to the last time …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PIf this degree of intervention\x01",
            "Nobody will complain.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x4, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x5, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xC,
        "#11PHuh … … this story.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PPlease take good care of it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FUm, thank you.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x18A, 6)
    Jump("loc_2E91")

    label("loc_2E5E")


    ChrTalk(
        0x101,
        "#6P#00000F(Well, I still have to stop it.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2E91")

    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -12560, 0, 13000, 0)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_15_2953 end

    def Function_16_2EC1(): pass

    label("Function_16_2EC1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08200.itc", 0x1E)
    LoadChrToIndex("chr/ch08500.itc", 0x1F)
    LoadChrToIndex("chr/ch05200.itc", 0x20)
    LoadChrToIndex("chr/ch05100.itc", 0x21)
    LoadChrToIndex("chr/ch07500.itc", 0x22)
    LoadChrToIndex("chr/ch10000.itc", 0x23)
    LoadChrToIndex("chr/ch05500.itc", 0x24)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x22)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0x23)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x101, 0, 0, 0, 0)
    SetChrPos(0x102, 0, 0, 0, 0)
    SetChrPos(0x103, 0, 0, 0, 0)
    SetChrPos(0x104, 0, 0, 0, 0)
    SetChrPos(0x109, 0, 0, 0, 0)
    SetChrPos(0x105, 0, 0, 0, 0)
    SetChrPos(0xD, 0, 0, 0, 0)
    SetChrPos(0xE, 0, 0, 0, 0)
    SetChrPos(0x10, 0, 0, 0, 0)
    SetChrPos(0xF, 0, 0, 0, 0)
    SetChrPos(0x11, 0, 0, 0, 0)
    SetChrPos(0x12, 0, 0, 0, 0)
    SetChrPos(0x13, 0, 0, 0, 0)
    ClearChrFlags(0xD, 0x4)
    ClearChrFlags(0xE, 0x4)
    ClearChrFlags(0x10, 0x4)
    ClearChrFlags(0xF, 0x4)
    ClearChrFlags(0x11, 0x4)
    ClearChrFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x4)
    ClearMapObjFlags(0x0, 0x10)
    OP_68(4140, 1000, 8840, 0)
    MoveCamera(315, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23500, 0)
    FadeToBright(1000, 0)
    OP_68(5450, 1000, 10150, 6000)
    BeginChrThread(0x13, 3, 0, 17)
    BeginChrThread(0x10, 3, 0, 18)
    BeginChrThread(0xF, 3, 0, 19)
    BeginChrThread(0xE, 3, 0, 20)
    BeginChrThread(0x11, 3, 0, 22)
    BeginChrThread(0x12, 3, 0, 23)
    BeginChrThread(0xD, 3, 0, 24)
    BeginChrThread(0x102, 3, 0, 25)
    BeginChrThread(0x103, 3, 0, 26)
    BeginChrThread(0x109, 3, 0, 21)
    BeginChrThread(0x105, 3, 0, 29)
    BeginChrThread(0x101, 3, 0, 27)
    BeginChrThread(0x104, 3, 0, 28)
    OP_6F(0x79)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x3)
    EndChrThread(0x102, 0x3)
    EndChrThread(0x103, 0x3)
    EndChrThread(0x104, 0x3)
    EndChrThread(0x109, 0x3)
    EndChrThread(0x105, 0x3)
    EndChrThread(0xD, 0x3)
    EndChrThread(0xE, 0x3)
    EndChrThread(0x10, 0x3)
    EndChrThread(0xF, 0x3)
    EndChrThread(0x11, 0x3)
    EndChrThread(0x12, 0x3)
    EndChrThread(0x13, 0x3)
    SetMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("t1080", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_2EC1 end

    def Function_17_317E(): pass

    label("Function_17_317E")

    SetChrPos(0xFE, 3500, 0, 5500, 90)
    OP_9B(0x0, 0xFE, 0xFFD3, 0xFA0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x10CC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x3E8, 0x7D0, 0x1)
    Sound(121, 0, 100, 0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x0)

    def lambda_31DA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_31DA)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_17_317E end

    def Function_18_31FA(): pass

    label("Function_18_31FA")

    SetChrPos(0xFE, 1300, 0, 6200, 90)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_325B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_325B)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_18_31FA end

    def Function_19_327B(): pass

    label("Function_19_327B")

    SetChrPos(0xFE, 1300, 0, 4800, 90)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_32DC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_32DC)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_19_327B end

    def Function_20_32FC(): pass

    label("Function_20_32FC")

    SetChrPos(0xFE, -600, 0, 6200, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x1518, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_335D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_335D)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_20_32FC end

    def Function_21_337D(): pass

    label("Function_21_337D")

    SetChrPos(0xFE, -600, 0, 4800, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x1518, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_33DE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_33DE)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_21_337D end

    def Function_22_33FE(): pass

    label("Function_22_33FE")

    SetChrPos(0xFE, -2500, 0, 6200, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x1E78, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_345F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_345F)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_22_33FE end

    def Function_23_347F(): pass

    label("Function_23_347F")

    SetChrPos(0xFE, -2500, 0, 4800, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x1E78, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_34E0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_34E0)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_23_347F end

    def Function_24_3500(): pass

    label("Function_24_3500")

    SetChrPos(0xFE, -4400, 0, 5500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x251C, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_3561():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3561)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_24_3500 end

    def Function_25_3581(): pass

    label("Function_25_3581")

    SetChrPos(0xFE, -6300, 0, 6200, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2C88, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_35E2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_35E2)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_25_3581 end

    def Function_26_3602(): pass

    label("Function_26_3602")

    SetChrPos(0xFE, -6300, 0, 4800, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2C88, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_3663():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3663)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_26_3602 end

    def Function_27_3683(): pass

    label("Function_27_3683")

    SetChrPos(0xFE, -8200, 0, 5500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x33F4, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_36E4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_36E4)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_27_3683 end

    def Function_28_3704(): pass

    label("Function_28_3704")

    SetChrPos(0xFE, -10100, 0, 6200, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x3B60, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_3765():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3765)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_28_3704 end

    def Function_29_3785(): pass

    label("Function_29_3785")

    SetChrPos(0xFE, -10100, 0, 4800, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x3B60, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_37E6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_37E6)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_29_3785 end

    def Function_30_3806(): pass

    label("Function_30_3806")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "~ Stairs Room ~\x01",
            "On the third floor VIP floor\x01",
            "It is a reservation.\x01",
            "Please refrain from entering.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_30_3806 end

    SaveToFile()

Try(main)
