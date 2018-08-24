from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1020.bin",                # FileName
        "c1020",                    # MapName
        "c1020",                    # Location
        0x0014,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 20, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1020",                  # 0
        "Lakelord III",           # 1
        "Receptionist Sylum",     # 2
        "Triton, the Silver Orca",# 3
        "Kaguya, the Dragon Queen",# 4
        "Narses, the Crazy Wave", # 5
        "Sharkman, the Sea Edge", # 6
        "Peter",                  # 7
        "Coppen",                 # 8
        "Branch Manager Celdan",  # 9
        "Leader Fisher",          # 10
    ))

    AddCharChip((
        "chr/ch45600.itc",                   # 00
        "chr/ch22100.itc",                   # 01
        "chr/ch45700.itc",                   # 02
        "chr/ch45800.itc",                   # 03
        "chr/ch45900.itc",                   # 04
        "chr/ch46000.itc",                   # 05
        "chr/ch24200.itc",                   # 06
        "chr/ch23600.itc",                   # 07
        "chr/ch32200.itc",                   # 08
        "chr/ch46100.itc",                   # 09
    ))

    DeclNpc(4294963296, 0,       48369,   0,    261,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(7230,    0,       9069,    180,  261,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(50,      0,       43369,   90,   389,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4294962527, 0,       47610,   0,    389,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4599,    0,       4294966966, 90,   389,  0x0, 0,   4,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(4294967096, 0,       7579,    315,  389,  0x0, 0,   5,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(4260,    0,       6059,    90,   389,  0x0, 0,   6,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(4294963747, 0,       51630,   0,    389,  0x0, 0,   7,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(5639,    0,       6059,    270,  389,  0x0, 0,   8,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(4260,    0,       6059,    90,   389,  0x0, 0,   9,   0,   0,   0,   0,   13,  255,  0)

    DeclActor(6580,    0,       7980,    1500,    7230,    1500,    9070,    0x007E, 0,  4,  0x0000)

    ChipFrameInfo(592, 0)                                        # 0

    ScpFunction((
        "Function_0_250",          # 00, 0
        "Function_1_308",          # 01, 1
        "Function_2_4C5",          # 02, 2
        "Function_3_53E",          # 03, 3
        "Function_4_1209",         # 04, 4
        "Function_5_120D",         # 05, 5
        "Function_6_3927",         # 06, 6
        "Function_7_3A26",         # 07, 7
        "Function_8_3B41",         # 08, 8
        "Function_9_3C6B",         # 09, 9
        "Function_10_3D7A",        # 0A, 10
        "Function_11_406B",        # 0B, 11
        "Function_12_4413",        # 0C, 12
        "Function_13_47A7",        # 0D, 13
        "Function_14_4842",        # 0E, 14
        "Function_15_56CE",        # 0F, 15
        "Function_16_5709",        # 10, 16
        "Function_17_6E7B",        # 11, 17
        "Function_18_732F",        # 12, 18
        "Function_19_77EF",        # 13, 19
        "Function_20_780B",        # 14, 20
        "Function_21_7827",        # 15, 21
    ))


    def Function_0_250(): pass

    label("Function_0_250")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_290"),
        (1, "loc_29C"),
        (2, "loc_2A8"),
        (3, "loc_2B4"),
        (4, "loc_2C0"),
        (5, "loc_2CC"),
        (6, "loc_2D8"),
        (SWITCH_DEFAULT, "loc_2E4"),
    )


    label("loc_290")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_29C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2A8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2B4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2C0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2CC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2D8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2E4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_307")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_307")

    Return()

    # Function_0_250 end

    def Function_1_308(): pass

    label("Function_1_308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_31B")
    SetChrFlags(0x8, 0x80)
    Jump("loc_470")

    label("loc_31B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_35F")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 4850, 0, 6960, 45)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 8390, 0, 6850, 0)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_470")

    label("loc_35F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3A1")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39C")
    SetChrPos(0xE, 50, 0, 43370, 90)
    ClearChrFlags(0x11, 0x80)

    label("loc_39C")

    Jump("loc_470")

    label("loc_3A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BD")
    SetChrFlags(0x8, 0x80)

    label("loc_3BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_3DF")
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)

    label("loc_3DF")

    Jump("loc_470")

    label("loc_3E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3F7")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_470")

    label("loc_3F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_405")
    Jump("loc_470")

    label("loc_405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_413")
    Jump("loc_470")

    label("loc_413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_421")
    Jump("loc_470")

    label("loc_421")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_42F")
    Jump("loc_470")

    label("loc_42F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_43D")
    Jump("loc_470")

    label("loc_43D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_44B")
    Jump("loc_470")

    label("loc_44B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_459")
    Jump("loc_470")

    label("loc_459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_467")
    Jump("loc_470")

    label("loc_467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_470")

    label("loc_470")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_484")
    ClearScenarioFlags(0x22, 0)
    SetMapFlags(0x10000000)
    Event(0, 14)

    label("loc_484")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A9")
    SetMapFlags(0x10000000)
    Event(0, 18)
    Jump("loc_4C4")

    label("loc_4A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C4")
    SetMapFlags(0x10000000)
    Event(0, 16)

    label("loc_4C4")

    Return()

    # Function_1_308 end

    def Function_2_4C5(): pass

    label("Function_2_4C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4F6")
    SetMapObjFrame(0xFF, "sunlight", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_4F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_51D")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sunlight", 0x0, 0x1)

    label("loc_51D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_534")
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_53D")

    label("loc_534")

    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0xD5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_53D")

    Return()

    # Function_2_4C5 end

    def Function_3_53E(): pass

    label("Function_3_53E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_565")
    Call(0, 17)
    Return()

    label("loc_565")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_576")
    Jump("loc_1205")

    label("loc_576")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_715")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_692")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_646")

    ChrTalk(
        0x8,
        (
            "Who would've thought\x01",
            "they would've called\x01",
            "Harvard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Hehe. Still,\x01",
            "everything is going\x01",
            "according to plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "After all, I came to\x01",
            "Crossbell for that\x01",
            "motive.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_68D")

    label("loc_646")


    ChrTalk(
        0x8,
        (
            "Come quickly, Harvard...\x01",
            "I'll personally give you\x01",
            "the final word!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68D")

    Jump("loc_710")

    label("loc_692")


    ChrTalk(
        0x8,
        (
            "I don't mind using the\x01",
            "boat shed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's true that, with that\x01",
            "atmosphere, it could be most\x01",
            "suitable for training...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_710")

    Jump("loc_1205")

    label("loc_715")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_867")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81F")

    ChrTalk(
        0x8,
        (
            "The connections between my Imperial\x01",
            "Fishing Club and the Fisherman's\x01",
            "Guild are considerable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Not that the likes of\x01",
            "you would know, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "...Hmph, I was talking\x01",
            "nonsense. Forget what I\x01",
            "said just now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_862")

    label("loc_81F")


    ChrTalk(
        0x8,
        (
            "...Hmph, I was talking\x01",
            "nonsense. Forget what I\x01",
            "said just now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_862")

    Jump("loc_1205")

    label("loc_867")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_9F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_960")

    ChrTalk(
        0x8,
        (
            "It looks like that Celdan\x01",
            "and the others are going\x01",
            "to accept defeat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hehe. At this point,\x01",
            "they haven't even\x01",
            "reached my level yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems that your passion\x01",
            "for fishing was just for\x01",
            "show. Bwah ha ha ha hah!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9EE")

    label("loc_960")


    ChrTalk(
        0x8,
        (
            "Hehe. At this point,\x01",
            "they haven't even\x01",
            "reached me yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems that your passion\x01",
            "for fishing was just for\x01",
            "show. Bwah ha ha ha hah!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9EE")

    Jump("loc_1205")

    label("loc_9F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_B69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC5")

    ChrTalk(
        0x8,
        (
            "My father, Lakelord II,\x01",
            "is a great angler.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In our Lakelord Corporation,\x01",
            "a few fishing tools have\x01",
            "been named after him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They were all designed\x01",
            "by my father's own\x01",
            "hands.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B64")

    label("loc_AC5")


    ChrTalk(
        0x8,
        (
            "My father, Lakelord II,\x01",
            "is a great angler.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That persistent spirit of inquiry\x01",
            "always surpasses our imaginations...\x01",
            "He is truly the ultimate hobbyist.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B64")

    Jump("loc_1205")

    label("loc_B69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C89")

    ChrTalk(
        0x8,
        (
            "The members of my\x01",
            "Imperial Fishing Club are\x01",
            "all pro elite anglers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Also, every catch is\x01",
            "feedback for Lakelord\x01",
            "Corp.'s product development.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At the core, we are very different\x01",
            "from the likes of those Fisherman's\x01",
            "Guild guys who do this half in fun.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D40")

    label("loc_C89")


    ChrTalk(
        0x8,
        (
            "The members of my\x01",
            "Fishing Emperor Club are\x01",
            "all pro elite anglers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At the core, we are very different\x01",
            "from the likes of those Fisherman's\x01",
            "Guild guys who do this half in fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D40")

    Jump("loc_1205")

    label("loc_D45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_E19")

    ChrTalk(
        0x8,
        (
            "Hmm, it seems the Crossbellians\x01",
            "are prattling about something\x01",
            "like an independence proposal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Why can't they understand the\x01",
            "peace of this land is due entirely\x01",
            "to my fatherland of Erebonia.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1205")

    label("loc_E19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_EDA")

    ChrTalk(
        0x8,
        (
            "Hmm. Unexpectedly, there\x01",
            "are a lot of good fishing\x01",
            "spots here in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's a pity there's no sea, but\x01",
            "I can fully enjoy myself with\x01",
            "its abundance of fish species.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1205")

    label("loc_EDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_10BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE8")

    ChrTalk(
        0x8,
        (
            "Doing well in the Angler\x01",
            "Duels?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hehe. If they're too tough for\x01",
            "you, you can give up without\x01",
            "even pushing yourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, it's just that if you do that,\x01",
            "you won't be able to fish freely in\x01",
            "Crossbell anymore. Bwah ha ha ha hah!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10B6")

    label("loc_FE8")


    ChrTalk(
        0x8,
        (
            "Hehe. If they're too tough for\x01",
            "you, you can give up without\x01",
            "even pushing yourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, it's just that if you do that,\x01",
            "you won't be able to fish freely in\x01",
            "Crossbell anymore. Bwah ha ha ha hah!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10B6")

    Jump("loc_1205")

    label("loc_10BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1148")

    ChrTalk(
        0x8,
        (
            "Hehe. I look forward to\x01",
            "seeing how far you'll be\x01",
            "able to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although the result is\x01",
            "plain as day. Bwah ha ha\x01",
            "ha hah!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1205")

    label("loc_1148")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_11FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11BD")

    ChrTalk(
        0x8,
        (
            "Huh... Are you still\x01",
            "here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I have nothing further\x01",
            "to say to you. Leave at\x01",
            "once.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11F7")

    label("loc_11BD")


    ChrTalk(
        0x8,
        (
            "I have nothing further\x01",
            "to say to you. Leave at\x01",
            "once.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11F7")

    Jump("loc_1205")

    label("loc_11FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1205")

    label("loc_1205")

    TalkEnd(0xFE)
    Return()

    # Function_3_53E end

    def Function_4_1209(): pass

    label("Function_4_1209")

    Call(0, 5)
    Return()

    # Function_4_1209 end

    def Function_5_120D(): pass

    label("Function_5_120D")

    TalkBegin(0x9)
    ClearScenarioFlags(0x0, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_123B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_122F")
    SetScenarioFlags(0x0, 2)

    label("loc_122F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_123B")
    SetScenarioFlags(0x0, 2)

    label("loc_123B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1245")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3923")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12A1")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                          # 0
            "Angler Duels Explanation\x01",      # 1
            "Cancel\x01",                        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jump("loc_12F3")

    label("loc_12A1")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12E9")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_12F3")

    label("loc_12E9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12F3")

    Jump("loc_1302")

    label("loc_12F8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1302")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1333")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1322")
    OP_AF(0x36)
    Jump("loc_1324")

    label("loc_1322")

    OP_AF(0x37)

    label("loc_1324")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_391E")

    label("loc_1333")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_214D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_134C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2148")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "About the Duel Agreement\x01",                     # 0
            "About Required Qualifications\x01",                # 1
            "About the Whereabouts of the Elite Four\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15CF")

    ChrTalk(
        0x9,
        (
            "If you win all the Angler Duels...\x01",
            "you'll get back this office and give out\x01",
            "one, and only one order, whatever it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Your opponents for the matches are a\x01",
            "total of five people. Those opponents\x01",
            "are the Elite Four and Sir Lakelord.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Also, when you beat one of the Elite\x01",
            "Four, you can liberate the fishing point\x01",
            "he or she is occupying at present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Also, to challenge them,\x01",
            "you need to be\x01",
            "qualified...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Once qualified, you can\x01",
            "challenge them however\x01",
            "many times you want.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2143")

    label("loc_15CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2021")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15E8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2012")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Lakelord Ⅲ\x01",                   # 0
            "Triton, the Silver Orca\x01",       # 1
            "Kaguya, the Dragon Queen\x01",      # 2
            "Narses, the Crazy Wave\x01",        # 3
            "Sharkman, the Sea Edge\x01",        # 4
            "Cancel\x01",                        # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_185C")

    ChrTalk(
        0x9,
        (
            "As for the qualification to challenge\x01",
            "Sir Lakelord who reigns at the top of\x01",
            "the club in name and in reality...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, you will be able\x01",
            "to earn it by "defeating\x01",
            "all of the Elite Four".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It will be incredibly difficult,\x01",
            "but... Please overcome it with\x01",
            "fighting spirit and willpower.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_184D")

    ChrTalk(
        0x9,
        (
            "Wait, you've already\x01",
            "defeated all four of\x01",
            "them. Haha, amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Then only Sir Lakelord\x01",
            "is left... I'll pray for\x01",
            "your good fortune.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_184D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_200D")

    label("loc_185C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A27")

    ChrTalk(
        0x9,
        (
            "As for the qualification to challenge\x01",
            "Mr. Triton, the Silver Orca, famed to\x01",
            "be the strongest of the Elite Four...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, you will be able to\x01",
            "earn it by "catching 29\x01",
            "different kinds of fish".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I think the road ahead is quite\x01",
            "steep, but... Please do your best\x01",
            "until the end without giving up.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 3)), scpexpr(EXPR_END)), "loc_1A18")

    ChrTalk(
        0x9,
        (
            "Wait, you've already won\x01",
            "against Mr. Triton.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha. In that case, you\x01",
            "don't need such\x01",
            "information anymore.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A18")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_200D")

    label("loc_1A27")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BF1")

    ChrTalk(
        0x9,
        (
            "As for the qualification to challenge\x01",
            "Miss Kaguya, the Dragon Queen, loved\x01",
            "by the gods of fishing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, you will be able to\x01",
            "earn it by "catching a big\x01",
            "one of 130 rege or more".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In addition to skills, I feel you\x01",
            "will need luck as well. Please do\x01",
            "your best without being discouraged.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 4)), scpexpr(EXPR_END)), "loc_1BE2")

    ChrTalk(
        0x9,
        (
            "Wait, you have already\x01",
            "won against Miss Kaguya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha. In that case, you\x01",
            "don't need such\x01",
            "information anymore.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BE2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_200D")

    label("loc_1BF1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DA7")

    ChrTalk(
        0x9,
        (
            "As for the qualification to challenge\x01",
            "Mr. Narses, the Crazy Wave, who loves\x01",
            "beautiful fish and himself...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, you will be able to earn\x01",
            "it by "catching Crossbell's\x01",
            "most beautiful fish".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The criterion is vague,\x01",
            "but... Pulling in fish like\x01",
            "these makes Mr. Narses howl.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 5)), scpexpr(EXPR_END)), "loc_1D98")

    ChrTalk(
        0x9,
        (
            "Wait, you've already won\x01",
            "against Mr. Narses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha. In that case, you\x01",
            "don't need such\x01",
            "information anymore.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D98")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_200D")

    label("loc_1DA7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2008")

    ChrTalk(
        0x9,
        (
            "As for the qualification to challenge Mr.\x01",
            "Sharkman, the Sea Edge, known as a\x01",
            "technician in contrast to his appearance...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, you will be able to earn\x01",
            "it by "catching 6 different\x01",
            "types in the fishing mini game".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The fish in question are\x01",
            "the Gluttonous Bass,\x01",
            "Rockeater, Armorica Carp...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "And also the Piranha,\x01",
            "Arowana and a Pirarucu\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I think it will be pretty hard\x01",
            "to catch all of them, but...\x01",
            "Somehow, please do your best.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 6)), scpexpr(EXPR_END)), "loc_1FF9")

    ChrTalk(
        0x9,
        (
            "Wait, you've already won\x01",
            "against Mr. Sharkman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha. In that case, you\x01",
            "don't need such\x01",
            "information anymore.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FF9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_200D")

    label("loc_2008")

    Jump("loc_2012")

    label("loc_200D")

    Jump("loc_15E8")

    label("loc_2012")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2143")

    label("loc_2021")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2134")

    ChrTalk(
        0x9,
        (
            "Mr. Sharkman is at St.\x01",
            "Ursula Byroad Pond.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Mr. Narses is at Mainz\x01",
            "Mountain Path Stream.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Miss Kaguya is at\x01",
            "Armorica Old Road Rest\x01",
            "Area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "And finally, Mr. Triton is at\x01",
            "West Crossbell Highway Pond.\x01",
            "That's where each of them are.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2143")

    label("loc_2134")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2148")

    label("loc_2148")

    Jump("loc_391E")

    label("loc_2143")

    Jump("loc_134C")

    label("loc_214D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_391E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2170")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2170")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_22E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_224F")

    ChrTalk(
        0x9,
        (
            "I was able to get in touch\x01",
            "with my family and friends\x01",
            "at Armorica Village earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There will be many things to worry\x01",
            "about going forward, but... For\x01",
            "now, I'll breathe a sigh of relief.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_22DE")

    label("loc_224F")


    ChrTalk(
        0x9,
        (
            "Nevertheless... Everyone\x01",
            "here are hardcore\x01",
            "fishing enthusiasts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The branch manager, Peter\x01",
            "and Coppen went out to\x01",
            "fish without delay.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22DE")

    Jump("loc_391E")

    label("loc_22E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_235A")

    ChrTalk(
        0x9,
        (
            "...Hmm. Anyway, it's a\x01",
            "turbulent situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I hope that everyone at\x01",
            "Amorica Village is\x01",
            "safe...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_391E")

    label("loc_235A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2583")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_2408")

    ChrTalk(
        0x9,
        (
            "When the Fisherman's Guild\x01",
            "activities finally restarted,\x01",
            "something crazy happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder if I should go\x01",
            "back to Armorica Village\x01",
            "for now?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_257E")

    label("loc_2408")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24DA")

    ChrTalk(
        0x9,
        (
            "Thanks to Sir Lakelord,\x01",
            "I joined the Fisherman's\x01",
            "Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Sir Lakelord is in truth\x01",
            "is a very kind and nice\x01",
            "person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder why he doesn't\x01",
            "get along with the\x01",
            "Fisherman's Guild...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_257E")

    label("loc_24DA")


    ChrTalk(
        0x9,
        (
            "At any rate, when the Fisherman's\x01",
            "Guild activities finally restarted,\x01",
            "something crazy happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder if I should go\x01",
            "back to Armorica Village\x01",
            "for now?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_257E")

    Jump("loc_391E")

    label("loc_2583")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2AC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_264B")

    ChrTalk(
        0x9,
        (
            "It seems the Fisherman's\x01",
            "Guild final weapon is a\x01",
            "certain someone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder what kind of man... No,\x01",
            "what kind of angler he is... Somehow\x01",
            "my heart is racing strangely.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ABE")

    label("loc_264B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27DC")

    ChrTalk(
        0x9,
        (
            "I've heard about it.\x01",
            "You're finally\x01",
            "challenging Sir Lakelord.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The place of the decisive battle is St. Ursula\x01",
            "Byroad sandbank... Amongst the numerous fishing\x01",
            "points, that is Sir Lakelord's favorite.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I think it will be a\x01",
            "hard battle, but please\x01",
            "do your best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "And then, please act as a mediator\x01",
            "between the Imperial Fishing Club\x01",
            "and the Fisherman's Guild.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_28A9")

    label("loc_27DC")


    ChrTalk(
        0x9,
        (
            "The place of the decisive battle is St. Ursula\x01",
            "Byroad sandbank... Amongst the numerous fishing\x01",
            "points, that is Sir Lakelord's favorite.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I think it will be a\x01",
            "hard battle, but please\x01",
            "do your best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28A9")

    Jump("loc_2ABE")

    label("loc_28AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A0F")

    ChrTalk(
        0x9,
        (
            "Congratulations, Mr.\x01",
            "Lloyd. They say you\x01",
            "splendidly won the duel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Also, thanks to Sir Lakelord,\x01",
            "I heard that I'll be able\x01",
            "join the Fisherman's Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "How can I put it? In\x01",
            "truth, Sir Lakelord is a\x01",
            "very kind and nice person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "What should I do... I wonder if\x01",
            "he can come to an understanding\x01",
            "with the Fisherman's Guild?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2ABE")

    label("loc_2A0F")


    ChrTalk(
        0x9,
        (
            "How can I put it? In\x01",
            "truth, Sir Lakelord is a\x01",
            "very kind and nice person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "What should I do... I wonder if\x01",
            "he can come to an understanding\x01",
            "with the Fisherman's Guild?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ABE")

    Jump("loc_391E")

    label("loc_2AC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2C20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B9E")

    ChrTalk(
        0x9,
        (
            "Before, Sir Lakelord\x01",
            "said he hated amateur\x01",
            "anglers, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It appears he has had a personal\x01",
            "attachment to the Fisherman's\x01",
            "Guild for a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder if something\x01",
            "happened?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C1B")

    label("loc_2B9E")


    ChrTalk(
        0x9,
        (
            "It appears that Sir Lakelord\x01",
            "has a personal attachment to\x01",
            "the Fisherman's Guild...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder if something\x01",
            "happened?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C1B")

    Jump("loc_391E")

    label("loc_2C20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2D27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CD4")

    ChrTalk(
        0x9,
        (
            "Mr. Celdan's been muttering to\x01",
            "himself the need to resort to\x01",
            "a final weapon or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder what it is?\x01",
            "Hmm, I'm sooo curious\x01",
            "about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2D22")

    label("loc_2CD4")


    ChrTalk(
        0x9,
        (
            "What ever could that\x01",
            ""final weapon" be? Hmmm,\x01",
            "I'm sooo curious about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D22")

    Jump("loc_391E")

    label("loc_2D27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2DA8")

    ChrTalk(
        0x9,
        (
            "When Sir Lakelord talks about\x01",
            "his father, you can always\x01",
            "see his eyes sparkling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Haha, that's wonderful.\x02",
    )

    CloseMessageWindow()
    Jump("loc_391E")

    label("loc_2DA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2E99")

    ChrTalk(
        0x9,
        (
            "The other day, I was praised\x01",
            "by Sir Lakelord who said I\x01",
            "have power of imagination.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "What kind of fish are in\x01",
            "this fishing point, how\x01",
            "they live...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The power to imagine\x01",
            "those things are needed\x01",
            "for fishing, he said.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_391E")

    label("loc_2E99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2F3A")

    ChrTalk(
        0x9,
        (
            "Anyway, it's been a long\x01",
            "time since I came to the\x01",
            "city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I visit periodically, but... I\x01",
            "miss the carefree atmosphere\x01",
            "of Armorica Village.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_391E")

    label("loc_2F3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3047")

    ChrTalk(
        0x9,
        (
            "The Elite Four... Although it may\x01",
            "look like they're just having fun,\x01",
            "they are actually working very hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Of course they test fishing gear, but they even\x01",
            "investigate water quality and fish territory\x01",
            "distribution... I really admire them greatly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_391E")

    label("loc_3047")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_330F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_323F")

    ChrTalk(
        0x9,
        (
            "Sir Lakelord's family lineage appears to\x01",
            "have inherited the position of viscount of\x01",
            "Erebonia for generation after generation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In the Empire, it appears\x01",
            "that many nobles are national\x01",
            "characters or businessmen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In the case of Sir Lakelord,\x01",
            "the fact that he is also a\x01",
            "professional angler is amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It appears that he received special education for gifted\x01",
            "children in fishing since he was a child. ...Though I\x01",
            "don't know what kind of education that would be.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_330A")

    label("loc_323F")


    ChrTalk(
        0x9,
        (
            "I mentioned it, but... Even after thinking hard\x01",
            "on it, I can't imagine what the special education\x01",
            "for gifted children in fishing actually is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Perhaps I'll try\x01",
            "asking Sir Lakelord next\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_330A")

    Jump("loc_391E")

    label("loc_330F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_33BC")

    ChrTalk(
        0x9,
        (
            "Umm, I've heard the\x01",
            "whole story from Sir\x01",
            "Lakelord.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If there's something you don't\x01",
            "understand about the matches, please\x01",
            "feel free to ask me anything.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_391E")

    label("loc_33BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3915")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_386F")
    TurnDirection(0x9, 0x101, 0)

    ChrTalk(
        0x9,
        (
            "Uhhm... You're from the\x01",
            "Fisherman's Guild,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Actually, I was planning\x01",
            "to join the Fisherman's\x01",
            "Guild, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FThe Fisherman's Guild...\x01",
            "is that so?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yes, but I've always\x01",
            "been indecisive about\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "One day, when I came with\x01",
            "the resolve to join, Sir\x01",
            "Lakelord was here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I gazed at him in shock,\x01",
            "and before I knew it, I'd\x01",
            "become the receptionist...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00106FI see. That must've been\x01",
            "difficult for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, because I didn't\x01",
            "say it clearly, somehow I\x01",
            "felt terribly sorry...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Because, Sir Lakelord is\x01",
            "treating me extremely\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "He gave me Lakelord\x01",
            "Corp. latest rod as a\x01",
            "present...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If he has time, he personally coaches\x01",
            "me in fishing... I can use all the\x01",
            "fishing bait I want free of charge...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FThose sure are some\x01",
            "great perks...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I mean, that's why it's\x01",
            "complicated for me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "At any rate, Sir Lakelord\x01",
            "seems to hate the\x01",
            "Fisherman's Guild a lot...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But to me, I'd like them\x01",
            "both to get along\x01",
            "somehow or other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If only there was\x01",
            "something that even I\x01",
            "could do...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13F, 6)
    Jump("loc_3910")

    label("loc_386F")


    ChrTalk(
        0x9,
        (
            "The Fisherman's Guild and the\x01",
            "Fishing Emperor Club... I'd like\x01",
            "both to get along somehow or other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If only there was\x01",
            "something that even I\x01",
            "could do...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3910")

    Jump("loc_391E")

    label("loc_3915")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_391E")

    label("loc_391E")

    Jump("loc_1245")

    label("loc_3923")

    TalkEnd(0x9)
    Return()

    # Function_5_120D end

    def Function_6_3927(): pass

    label("Function_6_3927")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3938")
    Jump("loc_3A22")

    label("loc_3938")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_399B")

    ChrTalk(
        0xA,
        (
            "Maaan, who would've\x01",
            "thought we'd all lose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It was fun, though\x01",
            "regrettable.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A22")

    label("loc_399B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_39A9")
    Jump("loc_3A22")

    label("loc_39A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_39B7")
    Jump("loc_3A22")

    label("loc_39B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_39C5")
    Jump("loc_3A22")

    label("loc_39C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_39D3")
    Jump("loc_3A22")

    label("loc_39D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_39E1")
    Jump("loc_3A22")

    label("loc_39E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_39EF")
    Jump("loc_3A22")

    label("loc_39EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_39FD")
    Jump("loc_3A22")

    label("loc_39FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3A0B")
    Jump("loc_3A22")

    label("loc_3A0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3A19")
    Jump("loc_3A22")

    label("loc_3A19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3A22")

    label("loc_3A22")

    TalkEnd(0xFE)
    Return()

    # Function_6_3927 end

    def Function_7_3A26(): pass

    label("Function_7_3A26")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3A37")
    Jump("loc_3B3D")

    label("loc_3A37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3AB6")

    ChrTalk(
        0xB,
        (
            "I can't believe it! To\x01",
            "think you caught that\x01",
            "Giant Pirarucu...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hmph, it's obvious it\x01",
            "was just a fluke!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B3D")

    label("loc_3AB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3AC4")
    Jump("loc_3B3D")

    label("loc_3AC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3AD2")
    Jump("loc_3B3D")

    label("loc_3AD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3AE0")
    Jump("loc_3B3D")

    label("loc_3AE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3AEE")
    Jump("loc_3B3D")

    label("loc_3AEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3AFC")
    Jump("loc_3B3D")

    label("loc_3AFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3B0A")
    Jump("loc_3B3D")

    label("loc_3B0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3B18")
    Jump("loc_3B3D")

    label("loc_3B18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3B26")
    Jump("loc_3B3D")

    label("loc_3B26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3B34")
    Jump("loc_3B3D")

    label("loc_3B34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3B3D")

    label("loc_3B3D")

    TalkEnd(0xFE)
    Return()

    # Function_7_3A26 end

    def Function_8_3B41(): pass

    label("Function_8_3B41")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3B52")
    Jump("loc_3C67")

    label("loc_3B52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3BA3")

    ChrTalk(
        0xC,
        (
            "The Fisherman's Guild\x01",
            "uon against us... Nnnn,\x01",
            "byurihooooooo!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C67")

    label("loc_3BA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3BEE")

    ChrTalk(
        0xC,
        (
            "A misuteriasu armed\x01",
            "group... Nnnn, natto\x01",
            "byurihoooooo!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C67")

    label("loc_3BEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3BFC")
    Jump("loc_3C67")

    label("loc_3BFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3C0A")
    Jump("loc_3C67")

    label("loc_3C0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3C18")
    Jump("loc_3C67")

    label("loc_3C18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3C26")
    Jump("loc_3C67")

    label("loc_3C26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3C34")
    Jump("loc_3C67")

    label("loc_3C34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3C42")
    Jump("loc_3C67")

    label("loc_3C42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3C50")
    Jump("loc_3C67")

    label("loc_3C50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3C5E")
    Jump("loc_3C67")

    label("loc_3C5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3C67")

    label("loc_3C67")

    TalkEnd(0xFE)
    Return()

    # Function_8_3B41 end

    def Function_9_3C6B(): pass

    label("Function_9_3C6B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3C7C")
    Jump("loc_3D76")

    label("loc_3C7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3CEF")

    ChrTalk(
        0xD,
        (
            "This fisherman's banner... is\x01",
            "cool. Gwah ha ha, I'd like to take\x01",
            "it back with me to the Empire!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D76")

    label("loc_3CEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3CFD")
    Jump("loc_3D76")

    label("loc_3CFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3D0B")
    Jump("loc_3D76")

    label("loc_3D0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3D19")
    Jump("loc_3D76")

    label("loc_3D19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3D27")
    Jump("loc_3D76")

    label("loc_3D27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3D35")
    Jump("loc_3D76")

    label("loc_3D35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3D43")
    Jump("loc_3D76")

    label("loc_3D43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3D51")
    Jump("loc_3D76")

    label("loc_3D51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3D5F")
    Jump("loc_3D76")

    label("loc_3D5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3D6D")
    Jump("loc_3D76")

    label("loc_3D6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3D76")

    label("loc_3D76")

    TalkEnd(0xFE)
    Return()

    # Function_9_3C6B end

    def Function_10_3D7A(): pass

    label("Function_10_3D7A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3D8B")
    Jump("loc_4067")

    label("loc_3D8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3DF7")

    ChrTalk(
        0xE,
        (
            "Uhhm... Anyhow, it seems the\x01",
            "only thing I can do is to kill\x01",
            "time repairing fishing gear.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4067")

    label("loc_3DF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3FD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_3EB6")

    ChrTalk(
        0xE,
        (
            "Dear me, President\x01",
            "Dieter is daring too,\x01",
            "eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I understand his opinion, but... I feel\x01",
            "like Crossbell will have to manage an\x01",
            "indescribable anxiety from now on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FCD")

    label("loc_3EB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F28")

    ChrTalk(
        0xE,
        (
            "Dear me. Our leader, Mr.\x01",
            "Fisher, is really a\x01",
            "terrific person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Leader Fisher, hooray!!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3FCD")

    label("loc_3F28")


    ChrTalk(
        0xE,
        (
            "Still, President Dieter\x01",
            "is daring too, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I understand his opinion, but... I feel\x01",
            "like Crossbell will have to manage an\x01",
            "incomparable anxiety from now on.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FCD")

    Jump("loc_4067")

    label("loc_3FD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3FE0")
    Jump("loc_4067")

    label("loc_3FE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3FEE")
    Jump("loc_4067")

    label("loc_3FEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3FFC")
    Jump("loc_4067")

    label("loc_3FFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_400A")
    Jump("loc_4067")

    label("loc_400A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4018")
    Jump("loc_4067")

    label("loc_4018")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4026")
    Jump("loc_4067")

    label("loc_4026")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4034")
    Jump("loc_4067")

    label("loc_4034")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4042")
    Jump("loc_4067")

    label("loc_4042")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4050")
    Jump("loc_4067")

    label("loc_4050")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_405E")
    Jump("loc_4067")

    label("loc_405E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4067")

    label("loc_4067")

    TalkEnd(0xFE)
    Return()

    # Function_10_3D7A end

    def Function_11_406B(): pass

    label("Function_11_406B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_407C")
    Jump("loc_440F")

    label("loc_407C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4113")

    ChrTalk(
        0xF,
        (
            "In this branch there's a\x01",
            "lot of preserved food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "...So, don't lay your hands\x01",
            "on the fish in the water\x01",
            "tank even by mistake, ok?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_440F")

    label("loc_4113")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_437A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_4262")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41DE")

    ChrTalk(
        0xF,
        (
            "*sigh*, as expected this\x01",
            "building is relaxing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Anyway, I hadn't foreseen\x01",
            "this independence\x01",
            "development at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "...What's going to\x01",
            "happen in the future?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_425D")

    label("loc_41DE")


    ChrTalk(
        0xF,
        (
            "We finally just got back...\x01",
            "I didn't foresee this\x01",
            "independence development.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "...What's going to\x01",
            "happen in the future?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_425D")

    Jump("loc_4375")

    label("loc_4262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42FC")

    ChrTalk(
        0xF,
        (
            "Our captain, Mr. Fisher,\x01",
            "is not to be\x01",
            "underestimated!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Gnnn, I to want to catch\x01",
            "a super big game like\x01",
            "that, even if just once!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4375")

    label("loc_42FC")


    ChrTalk(
        0xF,
        (
            "Anyhow, that aside, I\x01",
            "couldn't foresee this\x01",
            "independence development.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "...What's going to\x01",
            "happen in the future?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4375")

    Jump("loc_440F")

    label("loc_437A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4388")
    Jump("loc_440F")

    label("loc_4388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4396")
    Jump("loc_440F")

    label("loc_4396")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_43A4")
    Jump("loc_440F")

    label("loc_43A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_43B2")
    Jump("loc_440F")

    label("loc_43B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_43C0")
    Jump("loc_440F")

    label("loc_43C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_43CE")
    Jump("loc_440F")

    label("loc_43CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_43DC")
    Jump("loc_440F")

    label("loc_43DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_43EA")
    Jump("loc_440F")

    label("loc_43EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_43F8")
    Jump("loc_440F")

    label("loc_43F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4406")
    Jump("loc_440F")

    label("loc_4406")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_440F")

    label("loc_440F")

    TalkEnd(0xFE)
    Return()

    # Function_11_406B end

    def Function_12_4413(): pass

    label("Function_12_4413")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4424")
    Jump("loc_47A3")

    label("loc_4424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_44CC")

    ChrTalk(
        0x10,
        (
            "First there was a persistent situation\x01",
            "where I couldn't leave the city, and\x01",
            "now I can't leave the branch...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "*sigh*, I can't wait to\x01",
            "go fishing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47A3")

    label("loc_44CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_470E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_4598")

    ChrTalk(
        0x10,
        (
            "The Independent State of\x01",
            "Crossbell, eh...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "It wasn't just the Imperial Fishing Club we\x01",
            "couldn't get along with. Is it fate that we\x01",
            "can't get along with the Empire either?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4709")

    label("loc_4598")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_464C")

    ChrTalk(
        0x10,
        (
            "Still, the guys from the\x01",
            "Imperial Fishing Club\x01",
            "were really strong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Their love for fishing was\x01",
            "unmistakably real... It was a\x01",
            "good experience for me too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4709")

    label("loc_464C")


    ChrTalk(
        0x10,
        (
            "Anyway, the Independent\x01",
            "State of Crossbell,\x01",
            "eh...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "It wasn't just the Imperial Fishing Club we\x01",
            "couldn't get along with. Is it fate that we\x01",
            "can't get along with the Empire either?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4709")

    Jump("loc_47A3")

    label("loc_470E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_471C")
    Jump("loc_47A3")

    label("loc_471C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_472A")
    Jump("loc_47A3")

    label("loc_472A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4738")
    Jump("loc_47A3")

    label("loc_4738")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4746")
    Jump("loc_47A3")

    label("loc_4746")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4754")
    Jump("loc_47A3")

    label("loc_4754")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4762")
    Jump("loc_47A3")

    label("loc_4762")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4770")
    Jump("loc_47A3")

    label("loc_4770")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_477E")
    Jump("loc_47A3")

    label("loc_477E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_478C")
    Jump("loc_47A3")

    label("loc_478C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_479A")
    Jump("loc_47A3")

    label("loc_479A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_47A3")

    label("loc_47A3")

    TalkEnd(0xFE)
    Return()

    # Function_12_4413 end

    def Function_13_47A7(): pass

    label("Function_13_47A7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4835")

    ChrTalk(
        0x11,
        (
            "Hmm. Anyhow, I'm glad I\x01",
            "could save the Crossbell\x01",
            "branch from its crisis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Now I can return to\x01",
            "Liberl with my pride.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_483E")

    label("loc_4835")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_483E")

    label("loc_483E")

    TalkEnd(0xFE)
    Return()

    # Function_13_47A7 end

    def Function_14_4842(): pass

    label("Function_14_4842")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch23600.itc", 0x1E)
    LoadChrToIndex("chr/ch24200.itc", 0x1F)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 7530, 0, 6780, 225)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 7230, 0, 9070, 225)
    OP_4B(0x9, 0xFF)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrPos(0xF, 5820, 0, 4630, 45)
    OP_4B(0xF, 0xFF)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrPos(0xE, 5020, 0, 5530, 45)
    OP_4B(0xE, 0xFF)
    OP_68(2300, 1400, 1800, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, 2300, 0, 1600, 45)
    SetChrPos(0x102, 1300, 0, 2100, 45)
    SetChrPos(0x109, 1600, 0, 300, 45)
    SetChrPos(0x105, 100, 0, 1600, 45)

    def lambda_4941():
        OP_9B(0x1, 0x101, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4941)
    Sleep(300)

    def lambda_4959():
        OP_9B(0x1, 0x102, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4959)
    Sleep(300)

    def lambda_4971():
        OP_9B(0x1, 0x109, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4971)
    Sleep(300)

    def lambda_4989():
        OP_9B(0x1, 0x105, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4989)
    OP_68(4590, 1400, 3920, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#12P#00000F...Excuse us.\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#5POh my...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Well-Dressed Man",
        "#11PHuh, who're you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#6PW-What's this now?\x02",
    )

    CloseMessageWindow()

    def lambda_4A5F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4A5F)
    Sleep(50)

    def lambda_4A6F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4A6F)
    WaitChrThread(0xE, 1)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)

    ChrTalk(
        0xF,
        "#11PM-Member Lloyd!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5POh, perfect timing.\x01",
            "Lloyd, please tell him\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PThat this is the Fisherman's Guild,\x01",
            "Crossbell Branch- a place for anglers\x01",
            "who love peace and harmony to relax.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00012FW-What's going on?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(5070, 1400, 5070, 0)
    MoveCamera(75, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21850, 0)
    SetChrPos(0x101, 4500, 0, 3800, 45)
    SetChrPos(0x102, 3400, 0, 4300, 45)
    SetChrPos(0x109, 4200, 0, 2500, 45)
    SetChrPos(0x105, 3200, 0, 3000, 45)
    SetChrPos(0xF, 5300, 0, 3000, 45)
    SetChrPos(0xE, 6200, 0, 2250, 0)
    OP_0D()

    NpcTalk(
        0x8,
        "Well-Dressed Man",
        (
            "#5PHmph, so you're with the\x01",
            "Fisherman's Guild too, huh.\x01",
            "Are you here to complain too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FUmm, it's true that I'm\x01",
            "a member, but...\x02",
        )
    )

    CloseMessageWindow()
    Sound(802, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd showed the Detective\x01",
            "Notebook and explained their\x01",
            "current investigation.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    NpcTalk(
        0x8,
        "Well-Dressed Man",
        (
            "#5PSuspicious addresses,\x01",
            "you say?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Well-Dressed Man",
        (
            "#5PHmph, well it's true we haven't filed our\x01",
            "corporate registration yet. In that case,\x01",
            "I'll introduce myself: I am Lakelord Ⅲ.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHeir to the Lakelord\x01",
            "Company, the continent's\x01",
            "leading fishing gear maker.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAnd as for the Imperial Fishing Club,\x01",
            "it's none other than the professional\x01",
            "fishing organization I represent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FThe Lakelord Company...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FLloyd, have you heard of\x01",
            "it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FYeah, any fisherman has heard\x01",
            "at least the name.\x02\x03",
            "#00000FYou see, they've remained No.\x01",
            "1 in continental fishing gear\x01",
            "sales for some time now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FI-I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101FBut, why someone like\x01",
            "that in Crossbell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHmph. Naturally, it's to further\x01",
            "expand the influence and reach\x01",
            "of our Imperial Fishing Club.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAnd so, our new office\x01",
            "here is a foothold for\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIncidentally, the contract\x01",
            "is perfectly legal, as\x01",
            "stated in this document.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001F...Please allow me to\x01",
            "check.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_9B(0x1, 0x101, 0x0, 0x7D0, 0x7D0, 0x0)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#12P#00005FThis... This is a lease\x01",
            "agreement for this\x01",
            "property.\x02\x03",
            "#00003FAs you say, the Imperial\x01",
            "Fishing Club is indeed\x01",
            "the current leaseholder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PHaha, understand?\x02",
    )

    CloseMessageWindow()
    OP_9B(0x1, 0x101, 0xB4, 0x7D0, 0x7D0, 0x0)
    Sleep(50)

    ChrTalk(
        0xF,
        (
            "#11PMember Lloyd... You\x01",
            "can't possibly approve\x01",
            "of this tyranny.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)

    ChrTalk(
        0x101,
        "#6P#00005FTyranny?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PYes. You see, this man forcibly\x01",
            "stole the contract without\x01",
            "notifying Branch Manager Celdan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PAnd you greased the skids with\x01",
            "the real estate company with\x01",
            "the power of mira, didn't you?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#5PHmph. Maybe the method was a little\x01",
            "forceful, but the legality of the\x01",
            "contract is not in question.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAnd to begin with, this\x01",
            "place would be wasted on\x01",
            "the likes of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYou of the Fisherman's Guild,\x01",
            "who think fishing is just a\x01",
            "pastime and use illicit tools.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00001FY-You...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAnyway, this discussion\x01",
            "is over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIf you understand, leave\x01",
            "now, and tell Celdan and\x01",
            "the others too.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    ChrTalk(
        0x8,
        (
            "#11P...Sylum, I leave the\x01",
            "rest to you.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 300)

    ChrTalk(
        0x9,
        "#5PY-Yes, understood.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 1, 0, 15)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_55BF():
        OP_93(0xF, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_55BF)
    Sleep(50)

    def lambda_55CF():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_55CF)
    Sleep(50)

    def lambda_55DF():
        TurnDirection(0x102, 0x8, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_55DF)
    Sleep(50)

    def lambda_55EF():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_55EF)
    Sleep(50)

    def lambda_55FF():
        TurnDirection(0x105, 0x8, 300)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_55FF)
    Sleep(50)

    def lambda_560F():
        TurnDirection(0xE, 0x8, 300)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_560F)

    ChrTalk(
        0xF,
        (
            "#12PAh, running away is\x01",
            "cowardly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12PRight, and we still have\x01",
            "things to say to you...\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 1)

    ChrTalk(
        0x105,
        "#6P#10302FHaha, there he goes.\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x80)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    StopSound(128, 2000, 40)
    StopBGM(0xBB8)
    WaitBGM()
    SetScenarioFlags(0x22, 5)
    NewScene("c1000", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_14_4842 end

    def Function_15_56CE(): pass

    label("Function_15_56CE")

    OP_95(0x8, 8680, 0, 4760, 2000, 0x0)
    OP_95(0x8, 11520, 0, 4740, 2000, 0x0)
    OP_9B(0x0, 0x8, 0x10E, 0x7D0, 0x7D0, 0x0)
    Sleep(200)
    Return()

    # Function_15_56CE end

    def Function_16_5709(): pass

    label("Function_16_5709")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x8, 7530, 0, 6780, 225)
    SetChrPos(0x10, 5820, 0, 4630, 45)
    SetChrPos(0xE, 5020, 0, 5530, 45)
    SetChrPos(0xF, 6570, 0, 3900, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xE, 0x80)
    OP_4B(0x9, 0xFF)
    OP_93(0x9, 0xE1, 0x0)
    OP_4B(0x8, 0xFF)
    OP_4B(0x10, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_68(2300, 1400, 1800, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, 2300, 0, 1600, 45)
    SetChrPos(0x102, 1300, 0, 2100, 45)
    SetChrPos(0x109, 1600, 0, 300, 45)
    SetChrPos(0x104, 100, 0, 1600, 45)
    SetChrPos(0x105, 410, 0, 410, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x10,
        "D-Don't screw with us!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "How foolish do you need\x01",
            "to make us look before\x01",
            "you're satisfied!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F(What the... A quarrel?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F(Did something happen\x01",
            "again...?)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_58D4():
        OP_9B(0x1, 0xFE, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_58D4)
    Sleep(300)

    def lambda_58EC():
        OP_9B(0x1, 0xFE, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_58EC)
    Sleep(300)

    def lambda_5904():
        OP_9B(0x1, 0xFE, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5904)
    Sleep(300)

    def lambda_591C():
        OP_9B(0x1, 0xFE, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_591C)
    Sleep(300)

    def lambda_5934():
        OP_9B(0x1, 0xFE, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5934)
    OP_68(4190, 1400, 3520, 2500)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#00005FEveryone... Is something\x01",
            "wrong?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xE, 0x101, 500)

    ChrTalk(
        0xE,
        (
            "Yes, Lloyd... You\x01",
            "arrived at the right\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_59D6():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_59D6)
    Sleep(50)
    TurnDirection(0xF, 0x101, 500)

    ChrTalk(
        0x10,
        (
            "Member Lloyd, listen to\x01",
            "this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "The truth is, his comrades have\x01",
            "appeared at various fishing\x01",
            "points outside the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "He suddenly blurted out\x01",
            "that they have\x01",
            "monopolized those places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FM-Monopolizing the\x01",
            "fishing points...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Yes, he said those outside\x01",
            "the Imperial Fishing Club\x01",
            "can't fish in those places...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I ignored him and forced my way in,\x01",
            "but when I did that, I was obstructed\x01",
            "by having my line snapped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106FThat's awful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FExcuse me... Why can't\x01",
            "you get all along?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmph, that's because the\x01",
            "Fisherman's Guild is a\x01",
            "group of foolish amateurs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even just seeing them loitering\x01",
            "around in front of we, a supreme\x01",
            "professional group, is an eyesore.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x8, 500)
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xE)

    ChrTalk(
        0xE,
        (
            "W-What's wrong with\x01",
            "being amateurs?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Enjoying fishing has\x01",
            "nothing to do with being\x01",
            "pros or amateurs.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5D3A():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5D3A)
    Sleep(50)
    TurnDirection(0xF, 0x8, 500)

    ChrTalk(
        0x10,
        (
            "Yeah. I know that you guys\x01",
            "have obtained results in\x01",
            "many tournaments, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "There are some skilled anglers\x01",
            "among our number as well. I wish\x01",
            "you wouldn't underestimate us.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "Oh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "It's like the Branch\x01",
            "Manager says!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I had to relinquish my\x01",
            "title, but don't take a\x01",
            ""Master Fisherman" lightly!\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x32, 0x0, 0x3E8, 0xC8)

    ChrTalk(
        0x8,
        (
            "#4SHehe, bwah ha ha ha\x01",
            "hah!!#3S\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Interesting. I didn't\x01",
            "expect to hear such\x01",
            "words from you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you insist, then...\x01",
            "Why don't you undertake\x01",
            "the Angler Duels?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x10,
        "A-Angler duels...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Are you crazy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FU-Umm... What are these\x01",
            "Angler Duels...?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_600D():
        TurnDirection(0x10, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_600D)
    Sleep(50)

    def lambda_601D():
        TurnDirection(0xE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_601D)
    Sleep(50)

    def lambda_602D():
        TurnDirection(0xF, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_602D)
    Sleep(50)
    WaitChrThread(0x10, 0)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xF, 0)

    ChrTalk(
        0xE,
        (
            "Well, like the name says,\x01",
            "they're battles conducted\x01",
            "through fishing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "A match called an "Angler\x01",
            "Duel" has an absolute\x01",
            "meaning to an angler.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Yes, the angler's pride and honor...\x01",
            "They're earnest matches performed by\x01",
            "betting all things material and spiritual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I've never done one,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I heard of stories of anglers\x01",
            "who lost their entire fortune\x01",
            "by losing in those matches.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "In other words, you have to\x01",
            "win at all costs... They're\x01",
            "those kind of battles.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006FI-Is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FThat's some crazy\x01",
            "stuff...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_62E8():
        TurnDirection(0x10, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_62E8)
    Sleep(50)

    def lambda_62F8():
        TurnDirection(0xE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_62F8)
    Sleep(50)

    def lambda_6308():
        TurnDirection(0xF, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_6308)
    Sleep(50)
    WaitChrThread(0x10, 0)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xF, 0)

    ChrTalk(
        0x10,
        (
            "So... What are the\x01",
            "rules?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Let's see, it is my four\x01",
            "comrades and I that have\x01",
            "come to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If even one of you challenges and\x01",
            "defeats all five of us, it'll be\x01",
            "your victory. What do you say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You're free to challenge us however many\x01",
            "times you like, but... Until you win the\x01",
            "duels, you'll overlook our whims.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Of course the whims will\x01",
            "be limited to fishing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "............ ...And if\x01",
            "we win?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, it's a remote possibility\x01",
            "that a miracle happens, but a\x01",
            "man can dream, am I right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, by defeating each of us\x01",
            "we will of course set free the\x01",
            "corresponding fishing points...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And if you manage to defeat all five of us, we\x01",
            "will completely withdraw from Crossbell... And\x01",
            "we'll hand over this office too, naturally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Furthermore... I'll listen\x01",
            "to a single one of your\x01",
            "orders, whatever it is.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "F-For real!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHehe, but can we really\x01",
            "trust you?\x02\x03",
            "#10300FIt seems that even if they\x01",
            "won, there's no guarantee\x01",
            "you'd keep your promise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "No, like Peter said earlier,\x01",
            "the result of an Angler Duel\x01",
            "is absolute to an angler.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Then, no matter what our attitude towards\x01",
            "fishing is, it's certain these guys have more\x01",
            "pride as anglers than your average fisherman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I think it's safe to say that\x01",
            "them breaking their promises\x01",
            "is out of the question.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FI-I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FSo that's how it is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hehe, Celdan... Contrary\x01",
            "to expectations, even\x01",
            "you understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "So, what do you want to\x01",
            "do? Do you want to try\x01",
            "challenging us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "...All right, we'll\x01",
            "challenge you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hehe, as you wish.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x10, 500)

    ChrTalk(
        0xE,
        (
            "Are you sure, Branch\x01",
            "Manager?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "If we don't win, we'll\x01",
            "have to abide to their\x01",
            "whims forever, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Hehe, but on the contrary,\x01",
            "we can challenge them as\x01",
            "many times as we want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "This being the case,\x01",
            "frankly, don't you think\x01",
            "it'll be an easy win?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "No matter how strong they\x01",
            "are, no one can keep\x01",
            "winning at fishing forever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FIndeed... I get that\x01",
            "feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hehe. It appears you all\x01",
            "haven't yet unlocked the\x01",
            "meaning of fishing.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x8, 500)

    ChrTalk(
        0x8,
        (
            "Well, whatever. Incidentally, I'll\x01",
            "only allow one who has defeated all\x01",
            "four of comrades to challenge me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In addition, I will indicate\x01",
            "reasonable qualifications for\x01",
            "challenging each of them too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As might can expect, we don't\x01",
            "have time to face people without\x01",
            "a certain level of skills.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please understand that\x01",
            "point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Yes... I understand.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x10, 500)

    ChrTalk(
        0xE,
        "Branch Manager...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, if there's anything else\x01",
            "you don't understand, you can ask\x01",
            "Sylum, the receptionist, later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wonder if you'll really be suitable\x01",
            "opponents for the "Elite Four", the\x01",
            "pride of my Imperial Fishing Club?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 7)
    NewScene("c1000", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_16_5709 end

    def Function_17_6E7B(): pass

    label("Function_17_6E7B")

    EventBegin(0x0)
    Fade(500)
    OP_68(-4540, 1400, 48400, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, -4070, 0, 49840, 180)
    SetChrPos(0x102, -2990, 0, 50250, 180)
    SetChrPos(0x103, -4110, 0, 50870, 180)
    SetChrPos(0x104, -5080, 0, 51200, 180)
    SetChrPos(0x109, -2730, 0, 51480, 180)
    SetChrPos(0x105, -1420, 0, 51120, 225)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_0D()

    ChrTalk(
        0x8,
        "Hmm... What do you want?\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "You're not going to tell\x01",
            "me you've beaten the\x01",
            "entire Elite Four, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FUmm, well, it's as you\x01",
            "say...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmph... Then, will you\x01",
            "show me their medals?\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd showed Lakelord Ⅲ the\x01",
            "four medals he received\x01",
            "from the Elite Four.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "Indeed, these are,\x01",
            "without doubt, the medals\x01",
            "of the Elite Four...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Hehe. To think someone\x01",
            "would appear to challenge\x01",
            "me, the Fishing Emperor...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011FF-Fishing Emperor...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Yes. I am Lakelord Ⅲ,\x01",
            "the Fishing Emperor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I am he who gave the\x01",
            "club its and also he who\x01",
            "reigns as its head.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In any case... I'll go on\x01",
            "ahead to the decisive\x01",
            "battlefield and wait for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The place is St. Ursula\x01",
            "Byroad sandbank.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x4)

    def lambda_7243():

        label("loc_7243")

        TurnDirection(0x101, 0x8, 500)
        Yield()
        Jump("loc_7243")

    QueueWorkItem2(0x101, 2, lambda_7243)

    def lambda_7255():

        label("loc_7255")

        TurnDirection(0x102, 0x8, 500)
        Yield()
        Jump("loc_7255")

    QueueWorkItem2(0x102, 2, lambda_7255)

    def lambda_7267():

        label("loc_7267")

        TurnDirection(0x109, 0x8, 500)
        Yield()
        Jump("loc_7267")

    QueueWorkItem2(0x109, 2, lambda_7267)

    def lambda_7279():

        label("loc_7279")

        TurnDirection(0x105, 0x8, 500)
        Yield()
        Jump("loc_7279")

    QueueWorkItem2(0x105, 2, lambda_7279)

    def lambda_728B():

        label("loc_728B")

        TurnDirection(0x104, 0x8, 500)
        Yield()
        Jump("loc_728B")

    QueueWorkItem2(0x104, 2, lambda_728B)

    def lambda_729D():

        label("loc_729D")

        TurnDirection(0x103, 0x8, 500)
        Yield()
        Jump("loc_729D")

    QueueWorkItem2(0x103, 2, lambda_729D)

    def lambda_72AF():
        OP_95(0xFE, -210, 0, 50780, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_72AF)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0xB4, 0x1F4)

    def lambda_72D4():
        OP_9B(0x1, 0xFE, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_72D4)
    WaitChrThread(0x8, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x103, 0x2)
    SetScenarioFlags(0x190, 7)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -4070, 0, 49840, 135)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_17_6E7B end

    def Function_18_732F(): pass

    label("Function_18_732F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x9, 0xFF)
    OP_93(0x9, 0xE1, 0x0)
    OP_68(410, 1400, 410, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, -1580, 0, -580, 45)
    SetChrPos(0x102, -580, 0, -1580, 45)
    SetChrPos(0x104, -1580, 0, -2580, 45)
    SetChrPos(0x103, -2580, 0, -1580, 45)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(3850, 1400, 4450, 4000)
    SetCameraDistance(22000, 4000)

    def lambda_740D():
        OP_95(0xFE, 3330, 0, 4330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_740D)

    def lambda_7427():
        OP_95(0xFE, 2310, 0, 3310, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7427)
    BeginChrThread(0x102, 3, 0, 19)
    BeginChrThread(0x104, 3, 0, 20)

    def lambda_744D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_744D)

    def lambda_745E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_745E)

    def lambda_746F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_746F)

    def lambda_7480():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7480)
    Sleep(1000)
    BeginChrThread(0x10, 3, 0, 21)
    Sleep(50)
    BeginChrThread(0x11, 3, 0, 21)
    OP_6F(0x1)

    ChrTalk(
        0x10,
        (
            "#11POhh, if it isn't member\x01",
            "Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x11,
        "Fisher",
        (
            "Hmm, so you're the\x01",
            "rumored Lloyd Bannings\x01",
            "of the SSS.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FYes I am... What\x01",
            "happened to the Imperial\x01",
            "Fishing Club people?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00000FI see, you were able to\x01",
            "win all the Angler\x01",
            "Duels, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#11PYes, it's as you say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#11PEverything was possible\x01",
            "due to this man here,\x01",
            "our leader, Mr. Fisher!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00005FY-You're the Fisherman's\x01",
            "Guild leader...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#11PMy, even so, to think you\x01",
            "could splendidly catch\x01",
            "that big Guardian...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#11PI haven't been so\x01",
            "excited in a long time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Dear me, everything was\x01",
            "possible because of the Rainbow\x01",
            "Gem EX you all developed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "In any case, I'm glad I\x01",
            "could recover our\x01",
            "office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004FI-I see... Thank you\x01",
            "very much.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x191, 2)
    TurnDirection(0x11, 0x10, 0)
    TurnDirection(0x10, 0x11, 0)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    OP_93(0x9, 0xB4, 0x0)
    OP_4C(0x9, 0xFF)
    ClearMapFlags(0x10000000)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 3330, 0, 4330, 45)
    EventEnd(0x5)
    Return()

    # Function_18_732F end

    def Function_19_77EF(): pass

    label("Function_19_77EF")

    OP_95(0xFE, 4310, 0, 3130, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_19_77EF end

    def Function_20_780B(): pass

    label("Function_20_780B")

    OP_95(0xFE, 3310, 0, 2130, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_20_780B end

    def Function_21_7827(): pass

    label("Function_21_7827")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x101, 500)
    OP_4B(0xFE, 0xFF)
    Return()

    # Function_21_7827 end

    SaveToFile()

Try(main)
