from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t105b.bin",                # FileName
        "t105b",                    # MapName
        "t105b",                    # Location
        0x0042,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 66, 0, 3, 0, 4],
    )

    BuildStringList((
        "t105b",                  # 0
        "Hagger manager",           # 1
        "Citrus",               # 2
        "tourist",                 # 3
        "tourist",                 # 4
        "tourist",                 # 5
        "tourist",                 # 6
        "tourist",                 # 7
        "Mrs. Margaret",       # 8
        "Franc",                 # 9
        "Cecil",                 # 10
        "Ilia",                 # 11
        "Lisha",               # 12
        "Shuri",                 # 13
        "Zeit",               # 14
    ))

    AddCharChip((
        "chr/ch25800.itc",                   # 00
        "chr/ch25600.itc",                   # 01
        "chr/ch20802.itc",                   # 02
        "chr/ch20902.itc",                   # 03
        "chr/ch23600.itc",                   # 04
        "chr/ch22000.itc",                   # 05
        "chr/ch22100.itc",                   # 06
        "chr/ch44002.itc",                   # 07
    ))

    DeclNpc(4294966817, 0,       10050,   180,  389,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(106129,  0,       11579,   0,    385,  0x0, 0,   1,   0,   0,   1,   0,   7,   255,  0)
    DeclNpc(4294865116, 150,     124540,  90,   453,  0x0, 0,   2,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(4294867886, 150,     124540,  270,  453,  0x0, 0,   3,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(4294867517, 0,       4294886546, 268,  385,  0x0, 0,   4,   0,   0,   2,   0,   10,  255,  0)
    DeclNpc(98669,   0,       120930,  90,   389,  0x0, 0,   5,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(99650,   0,       120900,  270,  389,  0x0, 0,   6,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(97559,   0,       4294883027, 90,   453,  0x0, 0,   7,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(4294967276, 0,       8270,    1500,    4294966816, 1500,    10050,   0x007E, 0,  5,  0x0000)

    ChipFrameInfo(680, 0)                                        # 0

    ScpFunction((
        "Function_0_2A8",          # 00, 0
        "Function_1_360",          # 01, 1
        "Function_2_3C1",          # 02, 2
        "Function_3_3EC",          # 03, 3
        "Function_4_487",          # 04, 4
        "Function_5_513",          # 05, 5
        "Function_6_517",          # 06, 6
        "Function_7_64F",          # 07, 7
        "Function_8_755",          # 08, 8
        "Function_9_7E3",          # 09, 9
        "Function_10_867",         # 0A, 10
        "Function_11_A0A",         # 0B, 11
        "Function_12_AA0",         # 0C, 12
        "Function_13_B11",         # 0D, 13
        "Function_14_B7C",         # 0E, 14
        "Function_15_1242",        # 0F, 15
        "Function_16_1264",        # 10, 16
        "Function_17_12B1",        # 11, 17
    ))


    def Function_0_2A8(): pass

    label("Function_0_2A8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2E8"),
        (1, "loc_2F4"),
        (2, "loc_300"),
        (3, "loc_30C"),
        (4, "loc_318"),
        (5, "loc_324"),
        (6, "loc_330"),
        (SWITCH_DEFAULT, "loc_33C"),
    )


    label("loc_2E8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_348")

    label("loc_2F4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_348")

    label("loc_300")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_348")

    label("loc_30C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_348")

    label("loc_318")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_348")

    label("loc_324")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_348")

    label("loc_330")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_348")

    label("loc_33C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_348")

    label("loc_348")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_35F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_348")

    label("loc_35F")

    Return()

    # Function_0_2A8 end

    def Function_1_360(): pass

    label("Function_1_360")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C0")
    OP_95(0xFE, 106130, 0, 11580, 2000, 0x0)
    OP_95(0xFE, 106130, 0, 8150, 2000, 0x0)
    OP_95(0xFE, 94190, 0, 8150, 2000, 0x0)
    OP_95(0xFE, 94190, 0, 11580, 2000, 0x0)
    Jump("Function_1_360")

    label("loc_3C0")

    Return()

    # Function_1_360 end

    def Function_2_3C1(): pass

    label("Function_2_3C1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3EB")
    OP_94(0xFE, 0xFFFE7366, 0xFFFEBF88, 0xFFFE7F8C, 0xFFFECB72, 0x3E8)
    Sleep(450)
    Jump("Function_2_3C1")

    label("loc_3EB")

    Return()

    # Function_2_3C1 end

    def Function_3_3EC(): pass

    label("Function_3_3EC")

    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_42D")
    Jump("loc_477")

    label("loc_42D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_477")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)

    label("loc_477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_486")
    ClearScenarioFlags(0x22, 0)
    Event(0, 14)

    label("loc_486")

    Return()

    # Function_3_3EC end

    def Function_4_487(): pass

    label("Function_4_487")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4CB")
    OP_7D(0xAA, 0xAA, 0xFF, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x1, 0x1)
    Jump("loc_4F3")

    label("loc_4CB")

    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)

    label("loc_4F3")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_505")
    Jump("loc_512")

    label("loc_505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_512")
    OP_66(0x0, 0x1)

    label("loc_512")

    Return()

    # Function_4_487 end

    def Function_5_513(): pass

    label("Function_5_513")

    Call(0, 6)
    Return()

    # Function_5_513 end

    def Function_6_517(): pass

    label("Function_6_517")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_626")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B1")

    ChrTalk(
        0x8,
        (
            "A way of taking guests already\x01",
            "It seems that I headed to the guest house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Mayor Dieter and Mr. Maria Bell\x01",
            "I am waiting, please hurry.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_621")

    label("loc_5B1")


    ChrTalk(
        0x8,
        (
            "Beyond the villa ground\x01",
            "There is a guest house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Mayor Dieter and Mr. Maria Bell\x01",
            "I am waiting, please hurry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_621")

    Jump("loc_64B")

    label("loc_626")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_634")
    Jump("loc_64B")

    label("loc_634")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_642")
    Jump("loc_64B")

    label("loc_642")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_64B")

    label("loc_64B")

    TalkEnd(0x8)
    Return()

    # Function_6_517 end

    def Function_7_64F(): pass

    label("Function_7_64F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_73A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D3")

    ChrTalk(
        0xFE,
        (
            "Whew, Roche\x01",
            "I wonder if you are doing well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, whatever.\x01",
            "I cleaned up for the time being.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_735")

    label("loc_6D3")


    ChrTalk(
        0xFE,
        (
            "I'm at work,\x01",
            "Only worry about Roche\x01",
            "I do not know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I cleaned up for the time being.\x02",
    )

    CloseMessageWindow()

    label("loc_735")

    Jump("loc_751")

    label("loc_73A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_748")
    Jump("loc_751")

    label("loc_748")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_751")

    label("loc_751")

    TalkEnd(0xFE)
    Return()

    # Function_7_64F end

    def Function_8_755(): pass

    label("Function_8_755")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_7C8")

    ChrTalk(
        0xFE,
        (
            "No, even so\x01",
            "It was a good room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks to you, to tomorrow\x01",
            "You can do it slowly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7DF")

    label("loc_7C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_7D6")
    Jump("loc_7DF")

    label("loc_7D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_7DF")

    label("loc_7DF")

    TalkEnd(0xFE)
    Return()

    # Function_8_755 end

    def Function_9_7E3(): pass

    label("Function_9_7E3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_84C")

    ChrTalk(
        0xFE,
        (
            "Hotel service is also\x01",
            "That's pretty nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, even wine\x01",
            "I wonder if she will ask.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_863")

    label("loc_84C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_85A")
    Jump("loc_863")

    label("loc_85A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_863")

    label("loc_863")

    TalkEnd(0xFE)
    Return()

    # Function_9_7E3 end

    def Function_10_867(): pass

    label("Function_10_867")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_9EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_981")

    ChrTalk(
        0xFE,
        (
            "Today, the alkane shell\x01",
            "Artists\x01",
            "You stay at the upper floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe in a room just above\x01",
            "There may be … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think so, something\x01",
            "I'm getting tangled up.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006F(I'm sorry, the overhead is we … …)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_9EA")

    label("loc_981")


    ChrTalk(
        0xFE,
        (
            "The artists of alkane shell\x01",
            "You may be in a room directly above … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I will be excited when you think so.\x02",
    )

    CloseMessageWindow()

    label("loc_9EA")

    Jump("loc_A06")

    label("loc_9EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_9FD")
    Jump("loc_A06")

    label("loc_9FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_A06")

    label("loc_A06")

    TalkEnd(0xFE)
    Return()

    # Function_10_867 end

    def Function_11_A0A(): pass

    label("Function_11_A0A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_A85")

    ChrTalk(
        0xFE,
        (
            "Well then, take the dinner\x01",
            "Let's go to a restaurant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everything, very nightscape\x01",
            "It is said that it is a beautiful place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A9C")

    label("loc_A85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_A93")
    Jump("loc_A9C")

    label("loc_A93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_A9C")

    label("loc_A9C")

    TalkEnd(0xFE)
    Return()

    # Function_11_A0A end

    def Function_12_AA0(): pass

    label("Function_12_AA0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_AF6")

    ChrTalk(
        0xFE,
        (
            "Also from the restaurant\x01",
            "Can you see fireworks?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uhufu, I'm looking forward to it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B0D")

    label("loc_AF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_B04")
    Jump("loc_B0D")

    label("loc_B04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_B0D")

    label("loc_B0D")

    TalkEnd(0xFE)
    Return()

    # Function_12_AA0 end

    def Function_13_B11(): pass

    label("Function_13_B11")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Okho … … that villa\x01",
            "I liked it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Return to Mr. Clyde\x01",
            "I have to contact you immediately.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_B11 end

    def Function_14_B7C(): pass

    label("Function_14_B7C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08500.itc", 0x1E)
    LoadChrToIndex("chr/ch05200.itc", 0x1F)
    LoadChrToIndex("chr/ch05100.itc", 0x20)
    LoadChrToIndex("chr/ch07500.itc", 0x21)
    LoadChrToIndex("chr/ch10000.itc", 0x22)
    LoadChrToIndex("chr/ch02702.itc", 0x23)
    LoadChrToIndex("chr/ch25800.itc", 0x24)
    LoadChrToIndex("chr/ch02751.itc", 0x25)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x13, 0x1F)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x12, 0x20)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x11, 0x21)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x14, 0x22)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x25)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, -10260, -2040, -2830, 0)
    SetChrFlags(0x15, 0x20)
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x15, 0x8)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -2500, 0, 7000, 135)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x101, -1000, 0, 6000, 315)
    SetChrPos(0x102, -1500, 0, 5000, 315)
    SetChrPos(0x103, -500, 0, 4500, 315)
    SetChrPos(0x104, -1000, 0, 7200, 225)
    SetChrPos(0x109, 0, 0, 6000, 270)
    SetChrPos(0x105, 0, 0, 7200, 225)
    SetChrPos(0x10, 1000, 0, 6350, 270)
    SetChrPos(0x13, 350, 0, 4750, 315)
    SetChrPos(0x12, 1350, 0, 5050, 270)
    SetChrPos(0x11, -100, 0, 3250, 315)
    SetChrPos(0x14, -1350, 0, 3900, 315)
    OP_68(-1300, 2700, 5700, 0)
    MoveCamera(320, 23, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21500, 0)
    FadeToBright(2000, 0)
    OP_68(-1300, 1200, 5700, 3000)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        "#00006F#6PI see.. So she's no on 2F either\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PS-so sorry\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI studied all the rooms all over\x01",
            "I do not mean ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#6PNo, it's enough.\x01",
            "It's such a midnight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#04208F#6PThat Tibicko,\x01",
            "What are you sleeping at … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#05906F#6PI'm pretty worried…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#06411F#12PWhere\x01",
            "You went, did not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#01808F#12P….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6P…… even in my search\x01",
            "I did not find it ……\x02\x03",
            "#00208FWhere is KeA…\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(3054, 255, 100, 0)
    Sleep(800)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-2150, 1200, 5200, 2000)
    ClearChrFlags(0x15, 0x8)
    BeginChrThread(0x15, 3, 0, 16)

    def lambda_105A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_105A)

    def lambda_1067():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1067)
    Sleep(50)

    def lambda_1077():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1077)

    def lambda_1084():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1084)
    Sleep(50)

    def lambda_1094():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1094)

    def lambda_10A1():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_10A1)
    Sleep(50)

    def lambda_10B1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_10B1)

    def lambda_10BE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_10BE)
    Sleep(50)

    def lambda_10CE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_10CE)

    def lambda_10DB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_10DB)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    WaitChrThread(0x12, 2)
    WaitChrThread(0x11, 2)
    WaitChrThread(0x13, 2)
    WaitChrThread(0x14, 2)
    WaitChrThread(0x15, 3)
    OP_6F(0x79)

    ChrTalk(
        0x12,
        "#01705F#12POh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300F#11POh you're here\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(3060, 255, 70, 0)

    ChrTalk(
        0x15,
        "#01201F#5P#30WGrrrr, Woof!\x02",
    )

    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    CloseMessageWindow()
    Sleep(150)
    BeginChrThread(0x15, 3, 0, 17)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#11PW-wait\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#12P\"Come along, this is over\"\x01",
            "I am telling you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#12PLet's get moving!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x15, 0x3)
    EndChrThread(0x15, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("t102B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_B7C end

    def Function_15_1242(): pass

    label("Function_15_1242")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1263")
    Sound(845, 0, 30, 0)
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_15_1242")

    label("loc_1263")

    Return()

    # Function_15_1242 end

    def Function_16_1264(): pass

    label("Function_16_1264")

    BeginChrThread(0xFE, 0, 0, 15)
    OP_95(0xFE, -8730, 10, 1400, 5000, 0x1)
    OP_95(0xFE, -4500, 0, 5200, 5000, 0x0)
    OP_93(0xFE, 0x5A, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_16_1264 end

    def Function_17_12B1(): pass

    label("Function_17_12B1")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 15)
    OP_93(0xFE, 0xE1, 0x320)
    OP_95(0xFE, -8730, 10, 1400, 5000, 0x1)
    OP_95(0xFE, -10260, -2040, -2830, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    Return()

    # Function_17_12B1 end

    SaveToFile()

Try(main)
