from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Manager Haggar",         # 1
        "Citrus",                 # 2
        "Tourist",                # 3
        "Tourist",                # 4
        "Tourist",                # 5
        "Tourist",                # 6
        "Tourist",                # 7
        "Mrs. Margaret",          # 8
        "Fran",                   # 9
        "Cecil",                  # 10
        "Ilya",                   # 11
        "Rixia",                  # 12
        "Sully",                  # 13
        "Zeit",                   # 14
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
        "Function_7_670",          # 07, 7
        "Function_8_781",          # 08, 8
        "Function_9_824",          # 09, 9
        "Function_10_8AF",         # 0A, 10
        "Function_11_A6F",         # 0B, 11
        "Function_12_B0E",         # 0C, 12
        "Function_13_B98",         # 0D, 13
        "Function_14_C09",         # 0E, 14
        "Function_15_12DC",        # 0F, 15
        "Function_16_12FE",        # 10, 16
        "Function_17_134B",        # 11, 17
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_647")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BB")

    ChrTalk(
        0x8,
        (
            "Your friends already\x01",
            "headed to the guest\x01",
            "house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I urge you to hurry, as Mayor\x01",
            "Crois and Lady Mariabell are\x01",
            "waiting for you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_642")

    label("loc_5BB")


    ChrTalk(
        0x8,
        (
            "The guest house is up\x01",
            "past the residential\x01",
            "area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I urge you to hurry, as Mayor\x01",
            "Crois and Lady Mariabell are\x01",
            "waiting for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_642")

    Jump("loc_66C")

    label("loc_647")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_655")
    Jump("loc_66C")

    label("loc_655")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_663")
    Jump("loc_66C")

    label("loc_663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_66C")

    label("loc_66C")

    TalkEnd(0x8)
    Return()

    # Function_6_517 end

    def Function_7_670(): pass

    label("Function_7_670")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_766")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F3")

    ChrTalk(
        0xFE,
        (
            "Oh my, I wonder if Lotti\x01",
            "is doing her job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Oh, well. At any\x01",
            "rate, I'll clean and\x01",
            "clean!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_761")

    label("loc_6F3")


    ChrTalk(
        0xFE,
        (
            "I'm currently working so\x01",
            "I can't worry about\x01",
            "Lotti all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At any rate, I'll clean\x01",
            "and clean!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_761")

    Jump("loc_77D")

    label("loc_766")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_774")
    Jump("loc_77D")

    label("loc_774")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_77D")

    label("loc_77D")

    TalkEnd(0xFE)
    Return()

    # Function_7_670 end

    def Function_8_781(): pass

    label("Function_8_781")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_809")

    ChrTalk(
        0xFE,
        (
            "Well, nevertheless, I\x01",
            "got a nice room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks to this, it seems\x01",
            "I'll be able to take it\x01",
            "easy until tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_820")

    label("loc_809")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_817")
    Jump("loc_820")

    label("loc_817")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_820")

    label("loc_820")

    TalkEnd(0xFE)
    Return()

    # Function_8_781 end

    def Function_9_824(): pass

    label("Function_9_824")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_894")

    ChrTalk(
        0xFE,
        (
            "This hotel's service is\x01",
            "pretty good too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, maybe I'll ask for\x01",
            "wine or something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8AB")

    label("loc_894")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_8A2")
    Jump("loc_8AB")

    label("loc_8A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_8AB")

    label("loc_8AB")

    TalkEnd(0xFE)
    Return()

    # Function_9_824 end

    def Function_10_8AF(): pass

    label("Function_10_8AF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_A54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9DE")

    ChrTalk(
        0xFE,
        (
            "They say that the Arc-en-\x01",
            "Ciel artists are staying\x01",
            "on the floor above today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What if they're in the\x01",
            "room just above this\x01",
            "one...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I think that, I\x01",
            "somehow get all\x01",
            "restless...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F(Sorry, our room is\x01",
            "right above yours...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_A4F")

    label("loc_9DE")


    ChrTalk(
        0xFE,
        (
            "The Arc-en-Ciel artists\x01",
            "might be in the room\x01",
            "just above this one...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I think that, my\x01",
            "heart races.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A4F")

    Jump("loc_A6B")

    label("loc_A54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_A62")
    Jump("loc_A6B")

    label("loc_A62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_A6B")

    label("loc_A6B")

    TalkEnd(0xFE)
    Return()

    # Function_10_8AF end

    def Function_11_A6F(): pass

    label("Function_11_A6F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_AF3")

    ChrTalk(
        0xFE,
        (
            "Well then, should we go\x01",
            "to the restaurant for\x01",
            "dinner?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems it's a place\x01",
            "with a beautiful night\x01",
            "view.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B0A")

    label("loc_AF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_B01")
    Jump("loc_B0A")

    label("loc_B01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_B0A")

    label("loc_B0A")

    TalkEnd(0xFE)
    Return()

    # Function_11_A6F end

    def Function_12_B0E(): pass

    label("Function_12_B0E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_B7D")

    ChrTalk(
        0xFE,
        (
            "I wonder if we can see\x01",
            "the fireworks even from\x01",
            "the restaurant?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uhuhu, I can't wait.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B94")

    label("loc_B7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_B8B")
    Jump("loc_B94")

    label("loc_B8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_B94")

    label("loc_B94")

    TalkEnd(0xFE)
    Return()

    # Function_12_B0E end

    def Function_13_B98(): pass

    label("Function_13_B98")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Oh ho ho... I really\x01",
            "liked that villa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I get back, I'll\x01",
            "have to contact Clyde\x01",
            "immediately.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_B98 end

    def Function_14_C09(): pass

    label("Function_14_C09")

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
        (
            "#00006F#6PI see, so she's not on\x01",
            "2F either...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PI-I am terribly sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWe haven't searched\x01",
            "every nook and cranny of\x01",
            "every guest room, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#6PNo, you did plenty. It's\x01",
            "the middle of the night\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#04208F#6PJeez, that shorty,\x01",
            "what's she doing half\x01",
            "asleep...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#05906F#6PIt's really a little\x01",
            "worrisome...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#06411F#12PW-Where did she go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#01808F#12P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6P...I couldn't find her\x01",
            "with my "search"\x01",
            "either...\x02\x03",
            "#00208FWhere could she have\x01",
            "gone...?\x02",
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

    def lambda_1103():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1103)

    def lambda_1110():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1110)
    Sleep(50)

    def lambda_1120():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1120)

    def lambda_112D():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_112D)
    Sleep(50)

    def lambda_113D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_113D)

    def lambda_114A():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_114A)
    Sleep(50)

    def lambda_115A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_115A)

    def lambda_1167():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1167)
    Sleep(50)

    def lambda_1177():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_1177)

    def lambda_1184():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_1184)
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
        "#01705F#12PMy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F#11POh, this is where you\x01",
            "were!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(3060, 255, 70, 0)

    ChrTalk(
        0x15,
        "#01201F#5P#30WGrrowl... Woof.\x02",
    )

    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    CloseMessageWindow()
    Sleep(150)
    BeginChrThread(0x15, 3, 0, 17)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#11PH-Hey...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#12P"Follow me, this way",\x01",
            "he says.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#12PAnyway, let's follow\x01",
            "him!\x02",
        )
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

    # Function_14_C09 end

    def Function_15_12DC(): pass

    label("Function_15_12DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12FD")
    Sound(845, 0, 30, 0)
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_15_12DC")

    label("loc_12FD")

    Return()

    # Function_15_12DC end

    def Function_16_12FE(): pass

    label("Function_16_12FE")

    BeginChrThread(0xFE, 0, 0, 15)
    OP_95(0xFE, -8730, 10, 1400, 5000, 0x1)
    OP_95(0xFE, -4500, 0, 5200, 5000, 0x0)
    OP_93(0xFE, 0x5A, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_16_12FE end

    def Function_17_134B(): pass

    label("Function_17_134B")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 15)
    OP_93(0xFE, 0xE1, 0x320)
    OP_95(0xFE, -8730, 10, 1400, 5000, 0x1)
    OP_95(0xFE, -10260, -2040, -2830, 5000, 0x0)
    EndChrThread(0xFE, 0x0)
    Return()

    # Function_17_134B end

    SaveToFile()

Try(main)
