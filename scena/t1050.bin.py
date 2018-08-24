from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Manager Haggar",         # 1
        "Lotti",                  # 2
        "Citrus",                 # 3
        "Engineer",               # 4
        "Fortune Teller",         # 5
        "KeA",                    # 6
        "Fran",                   # 7
        "Cecil",                  # 8
        "Ilya",                   # 9
        "Rixia",                  # 10
        "Sully",                  # 11
        "Mariabell",              # 12
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
        "Function_6_6A5",          # 06, 6
        "Function_7_6A9",          # 07, 7
        "Function_8_107A",         # 08, 8
        "Function_9_166C",         # 09, 9
        "Function_10_17DD",        # 0A, 10
        "Function_11_1B64",        # 0B, 11
        "Function_12_1B68",        # 0C, 12
        "Function_13_1D89",        # 0D, 13
        "Function_14_2C44",        # 0E, 14
        "Function_15_2CA4",        # 0F, 15
        "Function_16_327E",        # 10, 16
        "Function_17_353B",        # 11, 17
        "Function_18_35B7",        # 12, 18
        "Function_19_3638",        # 13, 19
        "Function_20_36B9",        # 14, 20
        "Function_21_373A",        # 15, 21
        "Function_22_37BB",        # 16, 22
        "Function_23_383C",        # 17, 23
        "Function_24_38BD",        # 18, 24
        "Function_25_393E",        # 19, 25
        "Function_26_39BF",        # 1A, 26
        "Function_27_3A40",        # 1B, 27
        "Function_28_3AC1",        # 1C, 28
        "Function_29_3B42",        # 1D, 29
        "Function_30_3BC3",        # 1E, 30
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
            ""The Holidays We Love -\x01",
            "A Careful Recipes\x01",
            "Selection" is here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_6A1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x15)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A1")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Learned the \x07\x02",
            ""Picky\x01",
            "Matcha Latte"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_6A1")

    TalkEnd(0xFF)
    Return()

    # Function_5_5D3 end

    def Function_6_6A5(): pass

    label("Function_6_6A5")

    Call(0, 7)
    Return()

    # Function_6_6A5 end

    def Function_7_6A9(): pass

    label("Function_7_6A9")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1076")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",        # 0
            "Rest\x01",        # 1
            "Cancel\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_708")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_708")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_728")
    OP_AF(0x64)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1071")

    label("loc_728")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1071")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_91A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88E")

    ChrTalk(
        0x8,
        (
            "Since the disturbance in the city has\x01",
            "quieted down, I've come with everyone to\x01",
            "have a look at the hotel's condition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Still, that inexplicable\x01",
            "bluish-white tree... It's even\x01",
            "eerier seen from up close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I knew it even before coming,\x01",
            "but reopening Michelam will be\x01",
            "difficult for the time being.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_915")

    label("loc_88E")


    ChrTalk(
        0x8,
        (
            "Michelam's reopening is\x01",
            "still far off, but... I\x01",
            "just wanted to come here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please, feel free to ask\x01",
            "me if you'd like to\x01",
            "rest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_915")

    Jump("loc_1071")

    label("loc_91A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_A67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9EF")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Oh, Mr. Lloyd... Thank\x01",
            "you for visiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The hotel is closed, but\x01",
            "we are always ready to\x01",
            "accept a customer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please let me know if\x01",
            "you'd like to rest.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A62")

    label("loc_9EF")


    ChrTalk(
        0x8,
        (
            "Hm, even so, what is\x01",
            "with those bell-like\x01",
            "sounds...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "M. W. L. should be\x01",
            "closed too... It's very\x01",
            "strange.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A62")

    Jump("loc_1071")

    label("loc_A67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_A75")
    Jump("loc_1071")

    label("loc_A75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_DB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C83")

    ChrTalk(
        0x8,
        (
            "Oh, Mr. Lloyd and Miss\x01",
            "KeA. Welcome back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I am glad you found each\x01",
            "other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01110FEheheh, I'm back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHaha, sorry to have made\x01",
            "you worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No, no, don't mention\x01",
            "it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ah, your friends have\x01",
            "just gone out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They said they would meet you at the\x01",
            "appointed place after finishing their\x01",
            "business... Should you hurry, I wonder?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYou're right, thank you\x01",
            "very much.\x02\x03",
            "#00000FThen, let's go to the\x01",
            "theme park when we're\x01",
            "finished, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01109FYeah, let's go!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15A, 7)
    Jump("loc_DAB")

    label("loc_C83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D4D")

    ChrTalk(
        0x8,
        (
            "Your friends left not\x01",
            "long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They said they would meet you\x01",
            "at the appointed place after\x01",
            "finishing their business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Perhaps it's time for\x01",
            "you both to be heading\x01",
            "there?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DAB")

    label("loc_D4D")


    ChrTalk(
        0x8,
        (
            "Your friends left not\x01",
            "long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Perhaps it's time for\x01",
            "you both to be heading\x01",
            "there?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DAB")

    Jump("loc_1071")

    label("loc_DB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_EE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E87")

    ChrTalk(
        0x8,
        (
            "It appears Miss KeA left\x01",
            "not long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I spoke to her just in\x01",
            "case, but I was told not\x01",
            "to worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(KeA... As I feared,\x01",
            "maybe I should look for\x01",
            "her outside the hotel.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EE1")

    label("loc_E87")


    ChrTalk(
        0x8,
        (
            "It appears Miss KeA left\x01",
            "not long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, I wonder where she\x01",
            "could have gone?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EE1")

    Jump("loc_1071")

    label("loc_EE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1071")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE0")

    ChrTalk(
        0x8,
        (
            "My my, everyone... Are\x01",
            "you finding our 3F VIP\x01",
            "floor to your liking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, it's very pleasant.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Glad to hear it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please inform me immediately\x01",
            "if anything is not perfect.\x01",
            "It shall be handled at once.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1071")

    label("loc_FE0")


    ChrTalk(
        0x8,
        (
            "Are you finding our 3F\x01",
            "VIP floor to your\x01",
            "liking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please inform me immediately\x01",
            "if anything is not perfect.\x01",
            "It shall be handled at once.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1071")

    Jump("loc_6B6")

    label("loc_1076")

    TalkEnd(0x8)
    Return()

    # Function_7_6A9 end

    def Function_8_107A(): pass

    label("Function_8_107A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_11CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1139")

    ChrTalk(
        0x9,
        (
            "Because it was neglected\x01",
            "for a while, quite a lot\x01",
            "of dust has gathered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "*sigh*... That pale blue\x01",
            "tree makes me feel uneasy,\x01",
            "but I must clean properly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_11C8")

    label("loc_1139")


    ChrTalk(
        0x9,
        (
            "We periodically come to\x01",
            "clean so we can reopen\x01",
            "at any time, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That pale blue tree\x01",
            "really makes me uneasy\x01",
            "because it's so close.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11C8")

    Jump("loc_1668")

    label("loc_11CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_13B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12E5")

    ChrTalk(
        0x9,
        (
            "That Arios, the State Guard\x01",
            "Commander in Chief, passed\x01",
            "through the arcade not long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "He seemed to have a cute\x01",
            "little girl with him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F(Arios and KeA... It\x01",
            "seems they're really\x01",
            "here.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F(Quick, let's chase\x01",
            "after them.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_13AE")

    label("loc_12E5")


    ChrTalk(
        0x9,
        (
            "State Guard Commander in\x01",
            "Chief Arios passed through\x01",
            "the arcade not long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "He had a little girl with him and it\x01",
            "seemed like they were heading to the\x01",
            "theme park... I wonder what's going on?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13AE")

    Jump("loc_1668")

    label("loc_13B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_13C1")
    Jump("loc_1668")

    label("loc_13C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1449")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13DC")
    Call(0, 9)
    Jump("loc_1444")

    label("loc_13DC")


    ChrTalk(
        0xFE,
        (
            "Pleeease, let me be in\x01",
            "charge of taking care of\x01",
            "Wazyyy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll treat you to gelato\x01",
            "next tiiime!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1444")

    Jump("loc_1668")

    label("loc_1449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1668")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15D5")
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(
        0xFE,
        (
            "Oh, the customer is...\x01",
            "Wazy!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "C-Could it be that the\x01",
            "customers staying at the\x01",
            "VIP floor today are...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FYeah, I think that would\x01",
            "be us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "!!!!!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(D-Dear me... Of all days, why\x01",
            "do I have to be in charge of\x01",
            "the commoners' floor today!?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FI-I don't really get\x01",
            "why, but she looks\x01",
            "shocked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHehe, what a strange\x01",
            "kid.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1668")

    label("loc_15D5")


    ChrTalk(
        0xFE,
        (
            "D-Dear me... Of all days, why'd\x01",
            "I have to be in charge of the\x01",
            "commoners' floor today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was a chance to take\x01",
            "care of Wazy, and yet...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1668")

    TalkEnd(0xFE)
    Return()

    # Function_8_107A end

    def Function_9_166C(): pass

    label("Function_9_166C")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x9,
        (
            "Come on, Citrus, I beg\x01",
            "of you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Let me handle the VIP\x01",
            "floor where Wazy is\x01",
            "staying today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "And here I was, wondering\x01",
            "what you're bothering me\x01",
            "with when I'm working...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Also, didn't you force this on\x01",
            "me saying, "It's a bother to\x01",
            "take care of the VIP floor"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "C-Can't you help me out\x01",
            "there? I'll treat you to\x01",
            "a gelato next tiiime!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_9_166C end

    def Function_10_17DD(): pass

    label("Function_10_17DD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1999")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18F5")

    ChrTalk(
        0xA,
        (
            "It seems that Chairman\x01",
            "MacDowell and others were\x01",
            "confined at the guest house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "And, it seems they they're\x01",
            "being watched by the jaegers\x01",
            "who attacked the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It may have been for\x01",
            "independence, but the President\x01",
            "did some cruel things...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1994")

    label("loc_18F5")


    ChrTalk(
        0xA,
        (
            "It seems that Chairman\x01",
            "MacDowell and others were\x01",
            "confined at the guest house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The President did some\x01",
            "cruel things... I'm glad\x01",
            "he was caught, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1994")

    Jump("loc_1B60")

    label("loc_1999")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1AB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A58")

    ChrTalk(
        0xA,
        (
            "The person sitting over\x01",
            "there is the fortune teller\x01",
            "who works at the theme park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It seems she just showed\x01",
            "up one day... I wonder\x01",
            "where she usually lives.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1AAD")

    label("loc_1A58")


    ChrTalk(
        0xA,
        (
            "...Whoops, I've got to\x01",
            "finish the cleaning quickly.\x01",
            "I can't waste time talking.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AAD")

    Jump("loc_1B60")

    label("loc_1AB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1AC0")
    Jump("loc_1B60")

    label("loc_1AC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1B57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ADB")
    Call(0, 9)
    Jump("loc_1B52")

    label("loc_1ADB")


    ChrTalk(
        0xFE,
        (
            "Geez, if you're that set\x01",
            "on it I guess I could\x01",
            "switch with you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honestly, you always do\x01",
            "whatever you want.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B52")

    Jump("loc_1B60")

    label("loc_1B57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1B60")

    label("loc_1B60")

    TalkEnd(0xFE)
    Return()

    # Function_10_17DD end

    def Function_11_1B64(): pass

    label("Function_11_1B64")

    Call(0, 12)
    Return()

    # Function_11_1B64 end

    def Function_12_1B68(): pass

    label("Function_12_1B68")

    TalkBegin(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1B75")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D85")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                   # 0
            "Modify/Synthesize\x01",      # 1
            "Cancel\x01",                 # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BD4")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1BD4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BF4")
    OP_AF(0x65)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D80")

    label("loc_1BF4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D80")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1CC3")

    ChrTalk(
        0xB,
        (
            "Though such a mysterious thing\x01",
            "has appeared, this place's\x01",
            "personnel has got guts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...I want to finish the\x01",
            "maintenance quickly and get\x01",
            "away from here at once.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D80")

    label("loc_1CC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1D80")

    ChrTalk(
        0xB,
        (
            "I just came with the hotel\x01",
            "people to do maintenance on the\x01",
            "facilities while they're closed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you need something,\x01",
            "don't hesitate to ask. I'll\x01",
            "help you in my spare time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D80")

    Jump("loc_1B75")

    label("loc_1D85")

    TalkEnd(0xB)
    Return()

    # Function_12_1B68 end

    def Function_13_1D89(): pass

    label("Function_13_1D89")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_250B")
    Call(0, 14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2124")
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
        "#11POh, those books...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PCould they be "Agnes in the Sunny\x01",
            "Place" that you can see in\x01",
            "Crossbell City from time to time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FUhhm, are you talking\x01",
            "about this novel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FWell, we have gathered\x01",
            "all the volumes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PHehe, that is amazing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PI too had the chance to\x01",
            "obtain that novel before. I\x01",
            "really enjoyed reading it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PIt seems it is a made-up story,\x01",
            "but... Maybe the female protagonist\x01",
            "was based on someone somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PI intended to remain here as\x01",
            "a spectator until the end of\x01",
            "the Crossbell incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PIt could be nice doing\x01",
            "that while reading such\x01",
            "books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004F(Since we have them,\x01",
            "should we give them to\x01",
            "this person...?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18A, 5)
    Call(0, 15)
    Jump("loc_2506")

    label("loc_2124")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22F2")
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
            "#11PThose are "Agnes in the Sunny Place"\x01",
            "that you can see in Crossbell City\x01",
            "from time to time, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PI intended to remain here as\x01",
            "a spectator until the end of\x01",
            "the Crossbell incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PIt could be nice doing\x01",
            "that while reading such\x01",
            "books.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 15)
    Jump("loc_2506")

    label("loc_22F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2451")

    ChrTalk(
        0xC,
        (
            "That azure tree... To\x01",
            "think such a thing\x01",
            "appeared...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Tarots, crystal-gazing, star-gazing...\x01",
            "Even using all the methods I am capable\x01",
            "of, I can not read the future events.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hehe, interesting... It\x01",
            "is the first time such a\x01",
            "thing happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "What will the future of\x01",
            "Crossbell be...? I shall see\x01",
            "it with my own eyes here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2506")

    label("loc_2451")


    ChrTalk(
        0xC,
        (
            "Hehe...probably even "they" did\x01",
            "not foresee that the situation\x01",
            "would have become like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "What will the future of\x01",
            "Crossbell be...? I shall see\x01",
            "it with my own eyes here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2506")

    Jump("loc_2C40")

    label("loc_250B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2C40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A6C")

    ChrTalk(
        0xC,
        "Hm............\x02",
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
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_25DC")

    ChrTalk(
        0x101,
        (
            "#00005F(This person... Is she\x01",
            "the theme park fortune\x01",
            "teller?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2601")

    label("loc_25DC")


    ChrTalk(
        0x101,
        "#00005F(Who is this person...?)\x02",
    )

    CloseMessageWindow()

    label("loc_2601")


    ChrTalk(
        0x102,
        (
            "#00105F(It looks like she has\x01",
            "tarot cards spread in\x01",
            "front of her...)\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_26DC")
    Jump("loc_2726")

    label("loc_26DC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_26FC")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2726")

    label("loc_26FC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_271C")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2726")

    label("loc_271C")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2726")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)

    ChrTalk(
        0xC,
        "...Be careful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If you intend to advance further...\x01",
            "You all will most likely walk a\x01",
            "terribily difficult path.\x02",
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
        "#00201F............!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FW-What do you mean!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well then, how shall I\x01",
            "read this difficult\x01",
            "spread...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It is just that, if you\x01",
            "would proceed, you should\x01",
            "be prepared for the worst.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Even if you face the difficulties that lie\x01",
            "ahead, will you be able to protect that which\x01",
            "is important to you until the very end...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "That is what will depend\x01",
            "on you.\x02",
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
            "#00003F...I don't really get\x01",
            "it, but... I'll keep it\x01",
            "in mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hehe. I wish you good\x01",
            "luck.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x191, 7)
    SetChrSubChip(0xC, 0x0)
    Jump("loc_2C40")

    label("loc_2A6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B96")

    ChrTalk(
        0xC,
        (
            "If you wish to proceed,\x01",
            "you should be prepared\x01",
            "for the worst.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Even if you face the difficulties that lie\x01",
            "ahead, will you be able to protect that which\x01",
            "is important to you until the very end...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "That is what will depend\x01",
            "on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hehe. I wish you good\x01",
            "luck.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    ClearChrFlags(0xC, 0x10)
    Jump("loc_2C40")

    label("loc_2B96")


    ChrTalk(
        0xC,
        (
            "Even if you face the difficulties that lie\x01",
            "ahead, will you be able to protect that which\x01",
            "is important to you until the very end...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hehe. I wish you good\x01",
            "luck.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C40")

    TalkEnd(0xFE)
    Return()

    # Function_13_1D89 end

    def Function_14_2C44(): pass

    label("Function_14_2C44")

    ClearScenarioFlags(0x0, 5)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2EE, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2EF, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2F0, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2F1, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2F2, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2F3, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2F4, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2F5, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2F6, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2F7, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2F8, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2F9, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2FA, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2FB, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CA3")
    SetScenarioFlags(0x0, 5)

    label("loc_2CA3")

    Return()

    # Function_14_2C44 end

    def Function_15_2CA4(): pass

    label("Function_15_2CA4")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Hand Over the Novel\x01",      # 0
            "Don't\x01",                    # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3220")

    ChrTalk(
        0x101,
        (
            "#6P#00000FIf you like... Would you\x01",
            "like to have these\x01",
            "books?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PMy... Is it alright?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FIf Lloyd says so...\x01",
            "They're mostly gifts in\x01",
            "the first place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FPlease feel free to take\x01",
            "'em.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PHehe, in that case, I\x01",
            "shall accept them with\x01",
            "gratitude.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Handed over the entire\x01",
            "Agnes in the Sunny Place\x01",
            "set.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SubItemNumber(0x2EE, 1)
    SubItemNumber(0x2EF, 1)
    SubItemNumber(0x2F0, 1)
    SubItemNumber(0x2F1, 1)
    SubItemNumber(0x2F2, 1)
    SubItemNumber(0x2F3, 1)
    SubItemNumber(0x2F4, 1)
    SubItemNumber(0x2F5, 1)
    SubItemNumber(0x2F6, 1)
    SubItemNumber(0x2F7, 1)
    SubItemNumber(0x2F8, 1)
    SubItemNumber(0x2F9, 1)
    SubItemNumber(0x2FA, 1)
    SubItemNumber(0x2FB, 1)

    ChrTalk(
        0xC,
        "#11P...I agree.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PPerhaps it is presumptuous\x01",
            "of me, but... I shall give\x01",
            "this to you.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x396),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x396, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#6P#00005FThis is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PIt is something I obtained\x01",
            "from one of my connections\x01",
            "some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PI do not know what purpose\x01",
            "it serves, but... Take it\x01",
            "with you, if you like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FUmm, is it alright? It\x01",
            "looks rather valuable...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PHehe, I do not mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PIn the whirl of this\x01",
            "Crossbell incident I am just\x01",
            "a bystander, this time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PIf it is just this level of\x01",
            "involvement, I do not think\x01",
            "anyone will complain.\x02",
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
        (
            "#11PHehe... I'm just talking\x01",
            "to myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PIf you like, take good\x01",
            "care of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FUmm, thank you very\x01",
            "much.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x18A, 6)
    Jump("loc_324E")

    label("loc_3220")


    ChrTalk(
        0x101,
        (
            "#6P#00000F(Hmm, maybe I should\x01",
            "refuse.)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_324E")

    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -12560, 0, 13000, 0)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_15_2CA4 end

    def Function_16_327E(): pass

    label("Function_16_327E")

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

    # Function_16_327E end

    def Function_17_353B(): pass

    label("Function_17_353B")

    SetChrPos(0xFE, 3500, 0, 5500, 90)
    OP_9B(0x0, 0xFE, 0xFFD3, 0xFA0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x10CC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x3E8, 0x7D0, 0x1)
    Sound(121, 0, 100, 0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x0)

    def lambda_3597():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3597)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_17_353B end

    def Function_18_35B7(): pass

    label("Function_18_35B7")

    SetChrPos(0xFE, 1300, 0, 6200, 90)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_3618():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3618)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_18_35B7 end

    def Function_19_3638(): pass

    label("Function_19_3638")

    SetChrPos(0xFE, 1300, 0, 4800, 90)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_3699():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3699)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_19_3638 end

    def Function_20_36B9(): pass

    label("Function_20_36B9")

    SetChrPos(0xFE, -600, 0, 6200, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x1518, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_371A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_371A)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_20_36B9 end

    def Function_21_373A(): pass

    label("Function_21_373A")

    SetChrPos(0xFE, -600, 0, 4800, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x1518, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_379B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_379B)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_21_373A end

    def Function_22_37BB(): pass

    label("Function_22_37BB")

    SetChrPos(0xFE, -2500, 0, 6200, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x1E78, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_381C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_381C)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_22_37BB end

    def Function_23_383C(): pass

    label("Function_23_383C")

    SetChrPos(0xFE, -2500, 0, 4800, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x1E78, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_389D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_389D)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_23_383C end

    def Function_24_38BD(): pass

    label("Function_24_38BD")

    SetChrPos(0xFE, -4400, 0, 5500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x251C, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_391E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_391E)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_24_38BD end

    def Function_25_393E(): pass

    label("Function_25_393E")

    SetChrPos(0xFE, -6300, 0, 6200, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2C88, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_399F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_399F)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_25_393E end

    def Function_26_39BF(): pass

    label("Function_26_39BF")

    SetChrPos(0xFE, -6300, 0, 4800, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2C88, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_3A20():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3A20)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_26_39BF end

    def Function_27_3A40(): pass

    label("Function_27_3A40")

    SetChrPos(0xFE, -8200, 0, 5500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x33F4, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_3AA1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3AA1)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_27_3A40 end

    def Function_28_3AC1(): pass

    label("Function_28_3AC1")

    SetChrPos(0xFE, -10100, 0, 6200, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x3B60, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_3B22():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3B22)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_28_3AC1 end

    def Function_29_3B42(): pass

    label("Function_29_3B42")

    SetChrPos(0xFE, -10100, 0, 4800, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x3B60, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_3BA3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3BA3)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_29_3B42 end

    def Function_30_3BC3(): pass

    label("Function_30_3BC3")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "　　　 ～Staircase～\x01",
            "The 3F VIP floor is reserved.\x01",
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

    # Function_30_3BC3 end

    SaveToFile()

Try(main)
