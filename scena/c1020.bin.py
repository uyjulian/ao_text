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
        "Function_4_1274",         # 04, 4
        "Function_5_1278",         # 05, 5
        "Function_6_3A3B",         # 06, 6
        "Function_7_3B39",         # 07, 7
        "Function_8_3C45",         # 08, 8
        "Function_9_3D6F",         # 09, 9
        "Function_10_3E7D",        # 0A, 10
        "Function_11_4177",        # 0B, 11
        "Function_12_452D",        # 0C, 12
        "Function_13_4888",        # 0D, 13
        "Function_14_492A",        # 0E, 14
        "Function_15_58D8",        # 0F, 15
        "Function_16_5913",        # 10, 16
        "Function_17_709C",        # 11, 17
        "Function_18_755D",        # 12, 18
        "Function_19_7A1F",        # 13, 19
        "Function_20_7A3B",        # 14, 20
        "Function_21_7A57",        # 15, 21
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
    Jump("loc_1270")

    label("loc_576")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_720")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_694")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_646")

    ChrTalk(
        0x8,
        (
            "Who would've thought they \x01",
            "would've called Harvard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "...Uh uh, still, everything is going on as I desired.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "After all, I came to Crossbell\x01",
            "for that motive.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_68F")

    label("loc_646")


    ChrTalk(
        0x8,
        (
            "Come quickly, Harvard...\x01",
            "I will personally give you the final word!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68F")

    Jump("loc_71B")

    label("loc_694")


    ChrTalk(
        0x8,
        "I don't mind if they use a boat shed, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's true that, with that atmosphere, it\x01",
            "could be most suitable for training...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71B")

    Jump("loc_1270")

    label("loc_720")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_870")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82D")

    ChrTalk(
        0x8,
        (
            "The connections between my Fishing Emperor\x01",
            "Club and the Fisherman's Guild are considerable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I think that you don't know anything about it, but...\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "...Hmph, I was talking nonsense.\x01",
            "Forget what I said now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_86B")

    label("loc_82D")


    ChrTalk(
        0x8,
        (
            "...Hmph, I was talking nonsense.\x01",
            "Forget what I said now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86B")

    Jump("loc_1270")

    label("loc_870")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_977")

    ChrTalk(
        0x8,
        (
            "It looks like that Celdan and the others\x01",
            "are going to accept defeat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hu hu, but at this point, they haven't \x01",
            "even struggled to reach me yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems that their passion for \x01",
            "fishing was just a pretend.\x01",
            "Bwah ha ha ha hah!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A13")

    label("loc_977")


    ChrTalk(
        0x8,
        (
            "Hu hu, at this point, they haven't \x01",
            "even struggled to reach me yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems that your passion for fishing\x01",
            "was just a pretend.\x01",
            "Bwah ha ha ha hah!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A13")

    Jump("loc_1270")

    label("loc_A18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_B9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF7")

    ChrTalk(
        0x8,
        (
            "My father, Lakelord II,\x01",
            "is a very great angler.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In our Lakelord Corporation,\x01",
            "a few fishing tools have been\x01",
            "named after him, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Those were all designed by\x01",
            "my father's own hands.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B9A")

    label("loc_AF7")


    ChrTalk(
        0x8,
        (
            "My father, Lakelord II,\x01",
            "is a very great angler.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That persistent spirit of enquiry\x01",
            "always surpasses our imagination...\x01",
            "He is truly the ultimate hobbyist.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B9A")

    Jump("loc_1270")

    label("loc_B9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CCC")

    ChrTalk(
        0x8,
        (
            "The members of my Fishing Emperor\x01",
            "Club are all pro elite anglers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Also, every catch is a\x01",
            "feedback for the Lakelord Corp.\x01",
            "development of new products.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We are different from the roots from\x01",
            "those joke of guys who do this half\x01",
            "for fun like the Fisherman's Guild.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D85")

    label("loc_CCC")


    ChrTalk(
        0x8,
        (
            "The members of my Fishing Emperor\x01",
            "Club are all pro elite anglers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We are different from the roots from\x01",
            "those joke of guys who do this half\x01",
            "for fun like the Fisherman's Guild.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D85")

    Jump("loc_1270")

    label("loc_D8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_E69")

    ChrTalk(
        0x8,
        (
            "Hm, it seems that the Crossbellans\x01",
            "are prattling about something like an\x01",
            "independence proposal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "How can't they understand that this\x01",
            "land is publicly peaceful right\x01",
            "because of my fatherland Erebonia.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1270")

    label("loc_E69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_F2E")

    ChrTalk(
        0x8,
        (
            "Hm, contrary to expectations, in Crossbell\x01",
            "there are many good fishing places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's a pity there is no sea, but\x01",
            "I can enjoy myself with quite\x01",
            "the abundance of fish species.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1270")

    label("loc_F2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1119")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1045")

    ChrTalk(
        0x8,
        "Are you doing well in the Angler Duels?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hu hu, if it's tough for you, even giving up\x01",
            "without pushing yourselves is all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, it's just that if you do that, you won't\x01",
            "be able to fish freely in Crossbell anymore.\x01",
            "Bwah ha ha ha hah!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1114")

    label("loc_1045")


    ChrTalk(
        0x8,
        (
            "Hu hu, if it's tough for you, even giving up\x01",
            "without pushing yourselves is all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, it's just that if you do that, you won't\x01",
            "be able to fish freely in Crossbell anymore.\x01",
            "Bwah ha ha ha hah!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1114")

    Jump("loc_1270")

    label("loc_1119")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_11B1")

    ChrTalk(
        0x8,
        (
            "Hu hu, I'll look forward greatly\x01",
            "to how far you'll be able to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although, the result\x01",
            "is plain as daylight.\x01",
            "Bwah ha ha ha hah!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1270")

    label("loc_11B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1267")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1226")

    ChrTalk(
        0x8,
        "Hm...are you still here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I have nothing to say to you anymore.\x01",
            "Retreat at once.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1262")

    label("loc_1226")


    ChrTalk(
        0x8,
        (
            "I have nothing to say to you anymore.\x01",
            "Retreat at once.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1262")

    Jump("loc_1270")

    label("loc_1267")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1270")

    label("loc_1270")

    TalkEnd(0xFE)
    Return()

    # Function_3_53E end

    def Function_4_1274(): pass

    label("Function_4_1274")

    Call(0, 5)
    Return()

    # Function_4_1274 end

    def Function_5_1278(): pass

    label("Function_5_1278")

    TalkBegin(0x9)
    ClearScenarioFlags(0x0, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_129A")
    SetScenarioFlags(0x0, 2)

    label("loc_129A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_12A6")
    SetScenarioFlags(0x0, 2)

    label("loc_12A6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_135F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_130A")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                          # 0
            "Angler Duels Explanation\x01",      # 1
            "Quit\x01",                          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jump("loc_135A")

    label("loc_130A")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",      # 0
            "Shop\x01",      # 1
            "Quit\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1350")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_135A")

    label("loc_1350")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_135A")

    Jump("loc_1369")

    label("loc_135F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1369")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_139A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1389")
    OP_AF(0x36)
    Jump("loc_138B")

    label("loc_1389")

    OP_AF(0x37)

    label("loc_138B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3A32")

    label("loc_139A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21F2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21ED")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "About the Duels Agreement\x01",             # 0
            "About Required Qualifications\x01",         # 1
            "About the Elite Four Whereabouts\x01",      # 2
            "Quit\x01",                                  # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1663")

    ChrTalk(
        0x9,
        (
            "If you win all the Angler Duels...\x01",
            "You will be able to get back this office and \x01",
            "give out one, and only one order, whatever it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Your opponents for the matches are a total of five people.\x01",
            "Those opponents are the Elite Four and Sir Lakelord.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Also, when you beat one of the\x01",
            "Elite Four, you can liberate the fishing\x01",
            "point he or she is managing at present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Also, to challenge them, you need\x01",
            "qualifications for each of them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "When you are qualified, it is possible to\x01",
            "make a challenge how many times you want.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_21E8")

    label("loc_1663")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20C0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_167C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20B1")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Lakelord III\x01",                  # 0
            "Triton, the Silver Orca\x01",       # 1
            "Kaguya, the Dragon Queen\x01",      # 2
            "Narses, the Crazy Wave\x01",        # 3
            "Sharkman, the Sea Edge\x01",        # 4
            "Quit\x01",                          # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1909")

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
            "Well, you will be able to earn it by\x01",
            ""defeating all of the Elite Four".\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I think it's an incredible intense difficulty, but...\x01",
            "Please overcome it with fighting spirit and willpower.\x01\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18FA")

    ChrTalk(
        0x9,
        (
            "Wait, you have already defeated all four of them.\x01",
            "Hu hu, amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Then only Sir Lakelord is left...\x01",
            "I'll pray for your fortune in the duel.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18FA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_20AC")

    label("loc_1909")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AD3")

    ChrTalk(
        0x9,
        (
            "As for the qualification to challenge Mr. \x01",
            "Triton, the "Silver Orca", famed to be \x01",
            "the strongest of the Elite Four...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, you will be able to earn it by\x01",
            ""catching 29 different kind of fish".\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I think the road ahead is quite steep, but...\x01",
            "Please do your best until the end without giving up.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 3)), scpexpr(EXPR_END)), "loc_1AC4")

    ChrTalk(
        0x9,
        (
            "Wait, you have already won\x01",
            "against Mr. Triton.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hu hu, then you didn't need\x01",
            "such information anymore.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AC4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_20AC")

    label("loc_1AD3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C95")

    ChrTalk(
        0x9,
        (
            "As for the qualification to challenge\x01",
            "Miss Kaguya, the "Dragon Queen",\x01",
            "loved by the gods of fishing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, you will be able to earn it by\x01",
            ""catching a big game of 130 rege or more".\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I think that you will need, \x01",
            "above skills, luck too.\x01",
            "Please do your best without being discouraged.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 4)), scpexpr(EXPR_END)), "loc_1C86")

    ChrTalk(
        0x9,
        (
            "Wait, you have already won\x01",
            "against Miss Kaguya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hu hu, then you didn't need\x01",
            "such information anymore.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C86")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_20AC")

    label("loc_1C95")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E47")

    ChrTalk(
        0x9,
        (
            "As for the qualification to challenge Mr.\x01",
            "Narses, the "Crazy Wave", who loves\x01",
            "beautiful fish and himself...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, you will be able to earn it by\x01",
            ""catching Crossbell most beautiful fish".\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The criterion is vague, but...\x01",
            "Pulling in fish like these\x01",
            "makes Mr. Narses howl.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 5)), scpexpr(EXPR_END)), "loc_1E38")

    ChrTalk(
        0x9,
        (
            "Wait, you have already won\x01",
            "against Mr. Narses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hu hu, then you didn't need\x01",
            "such information anymore.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E38")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_20AC")

    label("loc_1E47")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20A7")

    ChrTalk(
        0x9,
        (
            "As for the qualification to challenge Mr.\x01",
            "Sharkman, the "Sea Edge", known as a\x01",
            "technician in contrast with his appearance...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, you will be able to earn it by\x01",
            ""catching 6 different types at the fishing mini game".\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The fish in question are the Gluttonous\x01",
            "Bass, Rockeater, Armorica Carp...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "And also the Piranha, Arowana\x01",
            "and a Pirarucu too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I think it will be pretty hard\x01",
            "to fish all of them, but...\x01",
            "Somehow, please do your best.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 6)), scpexpr(EXPR_END)), "loc_2098")

    ChrTalk(
        0x9,
        (
            "Wait, you have already won\x01",
            "against Mr. Sharkman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hu hu, then you didn't need\x01",
            "such information anymore.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2098")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_20AC")

    label("loc_20A7")

    Jump("loc_20B1")

    label("loc_20AC")

    Jump("loc_167C")

    label("loc_20B1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_21E8")

    label("loc_20C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21D9")

    ChrTalk(
        0x9,
        (
            "Mr. Sharkman is at\x01",
            ""St. Ursula Byroad Pond".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Mr. Narses is at\x01",
            ""Mainz Mountain Path Stream".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Miss Kaguya is at\x01",
            ""Armorica Old Road Refresht Area".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Then, Mr. Triton is at\x01",
            ""West Crossbell Highway Pond".\x01",
            "This is where each of them are.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_21E8")

    label("loc_21D9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_21ED")

    label("loc_21ED")

    Jump("loc_3A32")

    label("loc_21E8")

    Jump("loc_13B3")

    label("loc_21F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2215")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2215")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_237C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22E0")

    ChrTalk(
        0x9,
        (
            "Just before, I was able to\x01",
            "get in touch with my family\x01",
            "and friends at Armorica Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "From now on I'll be anxious\x01",
            "for many things, but...\x01",
            "For now, it was a relief.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2377")

    label("loc_22E0")


    ChrTalk(
        0x9,
        (
            "Nevertheless... Everyone is\x01",
            "a hardcore fishing enthusiast.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The branch manager, Mr.\x01",
            "Peter and Mr. Coppen have\x01",
            "gone out to fish without delay.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2377")

    Jump("loc_3A32")

    label("loc_237C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_23F9")

    ChrTalk(
        0x9,
        (
            "...Uuhm, at any rate, it's\x01",
            "a turbulent situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I hope that everyone at\x01",
            "Amorica Village is safe...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A32")

    label("loc_23F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2621")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_24A4")

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
        "I wonder if I should go back to Armorica Village once?\x02",
    )

    CloseMessageWindow()
    Jump("loc_261C")

    label("loc_24A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_257B")

    ChrTalk(
        0x9,
        (
            "Thanks to Sir Lakelord, I could\x01",
            "enter the Fisherman's Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Sir Lakelord in truth is a\x01",
            "very kind and nice person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder why he can't get along\x01",
            "well with the Fisherman's Guild...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_261C")

    label("loc_257B")


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
        "I wonder if I should go back to Armorica Village once?\x02",
    )

    CloseMessageWindow()

    label("loc_261C")

    Jump("loc_3A32")

    label("loc_2621")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2B71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26E9")

    ChrTalk(
        0x9,
        (
            "It seems the Fisherman's Guild final\x01",
            "weapon is a certain someone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder what kind of man...\x01",
            "No, what kind of angler he is...\x01",
            "Somehow my heart is racing strangely.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B6C")

    label("loc_26E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2962")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2885")

    ChrTalk(
        0x9,
        (
            "I have heard about it. You're\x01",
            "finally challenging Sir Lakelord.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The place of the decisive battle is St. Ursula \x01",
            "Byroad sandbank... Among the numerous fishing \x01",
            "points, that's Sir Lakelord's most favorite one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I think it will be a painful battle,\x01",
            "but please do your best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "And then, pleas act as a mediator between the\x01",
            "Fishing Emperor Club and the Fisherman's Guild.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_295D")

    label("loc_2885")


    ChrTalk(
        0x9,
        (
            "The place of the decisive battle is St. Ursula \x01",
            "Byroad sandbank... Among the numerous fishing \x01",
            "points, that's Sir Lakelord's most favorite one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I think it will be a painful battle,\x01",
            "but please do your best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_295D")

    Jump("loc_2B6C")

    label("loc_2962")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ABD")

    ChrTalk(
        0x9,
        (
            "Congratulations, Mr. Lloyd.\x01",
            "They say you splendidly won the duel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Also, thanks to Sir Lakelord I heard\x01",
            "that I could join the Fisherman's Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "How can I put it, Sir\x01",
            "Lakelord is in truth a\x01",
            "very kind and nice person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "What should I do...I wonder if he could come\x01",
            "to an understanding with the Fisherman's Guild?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B6C")

    label("loc_2ABD")


    ChrTalk(
        0x9,
        (
            "How can I put it, Sir\x01",
            "Lakelord is in truth a\x01",
            "very kind and nice person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "What should I do...I wonder if he could come\x01",
            "to an understanding with the Fisherman's Guild?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B6C")

    Jump("loc_3A32")

    label("loc_2B71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2CD3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C51")

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
            "It appears he somehow has\x01",
            "a personal attachment to the\x01",
            "Fisherman's Guild since way before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I wonder if something happened?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2CCE")

    label("loc_2C51")


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
        "I wonder if something happened?\x02",
    )

    CloseMessageWindow()

    label("loc_2CCE")

    Jump("loc_3A32")

    label("loc_2CD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2DE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D8B")

    ChrTalk(
        0x9,
        (
            "Somehow, recently Mr. Celdan\x01",
            "seemed to muttering to resort to\x01",
            "a final weapon or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder what that is?\x01",
            "Hmmm, I'm sooo curious about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2DDD")

    label("loc_2D8B")


    ChrTalk(
        0x9,
        (
            "I wonder what that "final weapon" could be?\x01",
            "Hmmm, I'm sooo curious about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DDD")

    Jump("loc_3A32")

    label("loc_2DE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2E64")

    ChrTalk(
        0x9,
        (
            "When Sir Lakelord talks\x01",
            "about his father, you can\x01",
            "always see his eyes sparkling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hu hu, that's wonderful.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A32")

    label("loc_2E64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2F60")

    ChrTalk(
        0x9,
        (
            "The other day, I was praised by\x01",
            "Sir Lakelord who said to me\x01",
            "that I have power of imagination.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "What kind of fish are in this fishing\x01",
            "point, how they live...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The power to imagine those things\x01",
            "are needed for fishing, he said.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A32")

    label("loc_2F60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3001")

    ChrTalk(
        0x9,
        (
            "Anyway, it's been a long time\x01",
            "since I came to the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I visit periodically, but...\x01",
            "I miss the carefree atmosphere\x01",
            "of Armorica Village.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A32")

    label("loc_3001")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3117")

    ChrTalk(
        0x9,
        (
            "The Elite Four...\x01",
            "Although it can appear that they're just having fun,\x01",
            "they actually are doing many kind of works.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Of course they test fishing gear, but they even\x01",
            "investigate water quality and fish territory distribution...\x01",
            "I really admire them greatly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A32")

    label("loc_3117")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_33E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3300")

    ChrTalk(
        0x9,
        (
            "Sir Lakelord family lineage appears to\x01",
            "have inherited the position of viscount of\x01",
            "Erebonia generation after generation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In the Empire it appears that many nobles\x01",
            "are national characters or businessmen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In the case of Sir Lakelord, the fact that he\x01",
            "is also a professional angler is amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It appears that he received special education for\x01",
            "gifted children in fishing since he was a child.\x01",
            "...Though I don't know what kind of education it is.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_33E4")

    label("loc_3300")


    ChrTalk(
        0x9,
        (
            "I was the one who started talking about it, but...\x01",
            "I can't imagine, even if I think deeply about it, what\x01",
            "the special education for gifted children in fishing is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Perhaps I'll try asking\x01",
            "Sir Lakelord the next time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33E4")

    Jump("loc_3A32")

    label("loc_33E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3497")

    ChrTalk(
        0x9,
        (
            "Uhhm, I've heard the whole\x01",
            "story from Sir Lakelord.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If there's something you don't understand about\x01",
            "the matches, please feel free to ask me anything.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A32")

    label("loc_3497")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3A29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3970")
    TurnDirection(0x9, 0x101, 0)

    ChrTalk(
        0x9,
        (
            "Uhhm...\x01",
            "You're from the Fisherman's Guild, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Actually, I was planning to join\x01",
            "the Fisherman's Guild, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FThe Fisherman's Guild...is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Yes, but I've been always indecisive about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "One day, when I came\x01",
            "with the resolve to join,\x01",
            "Sir Lakelord was here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I was gazing at him in shock, and when\x01",
            "I noticed, I had become the receptionist...\x02",
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
        "#00106FI see, it must've been difficult for you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, because I didn't say it clearly,\x01",
            "somehow I felt terribly sorry...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Because, Sir Lakelord is\x01",
            "treating me extremely well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "He gave me the latest model of rod\x01",
            "by the Lakelord Corp. as present...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If he has time, he personally coaches\x01",
            "me in fishing... I can use all the\x01",
            "fishing baits I want free of charge...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FThat's a great treatment you're receiving...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I mean, that's why it's complicated for me...\x02",
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
            "But to me, I'd like for both to get\x01",
            "along well in a way or another.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If only there was something\x01",
            "that even I could do...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13F, 6)
    Jump("loc_3A24")

    label("loc_3970")


    ChrTalk(
        0x9,
        (
            "The Fisherman's Guild and the Fishing Emperor Club...\x01",
            "To me, I'd like for both to get\x01",
            "along well in a way or another.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If only there was something\x01",
            "that even I could do...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A24")

    Jump("loc_3A32")

    label("loc_3A29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3A32")

    label("loc_3A32")

    Jump("loc_12B0")

    label("loc_3A37")

    TalkEnd(0x9)
    Return()

    # Function_5_1278 end

    def Function_6_3A3B(): pass

    label("Function_6_3A3B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3A4C")
    Jump("loc_3B35")

    label("loc_3A4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3AAE")

    ChrTalk(
        0xA,
        (
            "Maaan, who could've\x01",
            "though we'd all lose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "It was fun, though regrettable.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B35")

    label("loc_3AAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3ABC")
    Jump("loc_3B35")

    label("loc_3ABC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3ACA")
    Jump("loc_3B35")

    label("loc_3ACA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3AD8")
    Jump("loc_3B35")

    label("loc_3AD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3AE6")
    Jump("loc_3B35")

    label("loc_3AE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3AF4")
    Jump("loc_3B35")

    label("loc_3AF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3B02")
    Jump("loc_3B35")

    label("loc_3B02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3B10")
    Jump("loc_3B35")

    label("loc_3B10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3B1E")
    Jump("loc_3B35")

    label("loc_3B1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3B2C")
    Jump("loc_3B35")

    label("loc_3B2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3B35")

    label("loc_3B35")

    TalkEnd(0xFE)
    Return()

    # Function_6_3A3B end

    def Function_7_3B39(): pass

    label("Function_7_3B39")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3B4A")
    Jump("loc_3C41")

    label("loc_3B4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3BBA")

    ChrTalk(
        0xB,
        (
            "To think you would catch\x01",
            "that Giant Pirarucu...\x02",
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
    Jump("loc_3C41")

    label("loc_3BBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3BC8")
    Jump("loc_3C41")

    label("loc_3BC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3BD6")
    Jump("loc_3C41")

    label("loc_3BD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3BE4")
    Jump("loc_3C41")

    label("loc_3BE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3BF2")
    Jump("loc_3C41")

    label("loc_3BF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3C00")
    Jump("loc_3C41")

    label("loc_3C00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3C0E")
    Jump("loc_3C41")

    label("loc_3C0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3C1C")
    Jump("loc_3C41")

    label("loc_3C1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3C2A")
    Jump("loc_3C41")

    label("loc_3C2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3C38")
    Jump("loc_3C41")

    label("loc_3C38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3C41")

    label("loc_3C41")

    TalkEnd(0xFE)
    Return()

    # Function_7_3B39 end

    def Function_8_3C45(): pass

    label("Function_8_3C45")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3C56")
    Jump("loc_3D6B")

    label("loc_3C56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3CA7")

    ChrTalk(
        0xC,
        (
            "The Fisherman's Guild uon against us...\x01",
            "Nnnn, byurihooooooo!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D6B")

    label("loc_3CA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3CF2")

    ChrTalk(
        0xC,
        (
            "A misuteriasu armed group...\x01",
            "Nnnn, natto byurihoooooo!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D6B")

    label("loc_3CF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3D00")
    Jump("loc_3D6B")

    label("loc_3D00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3D0E")
    Jump("loc_3D6B")

    label("loc_3D0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3D1C")
    Jump("loc_3D6B")

    label("loc_3D1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3D2A")
    Jump("loc_3D6B")

    label("loc_3D2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3D38")
    Jump("loc_3D6B")

    label("loc_3D38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3D46")
    Jump("loc_3D6B")

    label("loc_3D46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3D54")
    Jump("loc_3D6B")

    label("loc_3D54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3D62")
    Jump("loc_3D6B")

    label("loc_3D62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3D6B")

    label("loc_3D6B")

    TalkEnd(0xFE)
    Return()

    # Function_8_3C45 end

    def Function_9_3D6F(): pass

    label("Function_9_3D6F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3D80")
    Jump("loc_3E79")

    label("loc_3D80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3DF2")

    ChrTalk(
        0xD,
        (
            "This fisherman's banner...is cool.\x01",
            "Gwah ha ha, I'd like to take it back with me to the Empire!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E79")

    label("loc_3DF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3E00")
    Jump("loc_3E79")

    label("loc_3E00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3E0E")
    Jump("loc_3E79")

    label("loc_3E0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3E1C")
    Jump("loc_3E79")

    label("loc_3E1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3E2A")
    Jump("loc_3E79")

    label("loc_3E2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3E38")
    Jump("loc_3E79")

    label("loc_3E38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3E46")
    Jump("loc_3E79")

    label("loc_3E46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3E54")
    Jump("loc_3E79")

    label("loc_3E54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3E62")
    Jump("loc_3E79")

    label("loc_3E62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3E70")
    Jump("loc_3E79")

    label("loc_3E70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3E79")

    label("loc_3E79")

    TalkEnd(0xFE)
    Return()

    # Function_9_3D6F end

    def Function_10_3E7D(): pass

    label("Function_10_3E7D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3E8E")
    Jump("loc_4173")

    label("loc_3E8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3F02")

    ChrTalk(
        0xE,
        (
            "Uhhm...at any rate, it seems\x01",
            "the only thing I can do is to kill\x01",
            "time repairing the fishing gear.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4173")

    label("loc_3F02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_40DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_3FC1")

    ChrTalk(
        0xE,
        (
            "Dear me, President Dieter\x01",
            "is daring too, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I understand his opinion, but...\x01",
            "I feel like Crossbell will have to manage\x01",
            "an indescribable anxiety from now on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40D9")

    label("loc_3FC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4034")

    ChrTalk(
        0xE,
        (
            "Dear me, our leader, Mr. Fisher,\x01",
            "is really a terrific person.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Leader Fisher, hooray!!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_40D9")

    label("loc_4034")


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
            "I understand his opinion, but...\x01",
            "I feel like Crossbell will have to manage\x01",
            "an incomparable anxiety from now on.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40D9")

    Jump("loc_4173")

    label("loc_40DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_40EC")
    Jump("loc_4173")

    label("loc_40EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_40FA")
    Jump("loc_4173")

    label("loc_40FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4108")
    Jump("loc_4173")

    label("loc_4108")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4116")
    Jump("loc_4173")

    label("loc_4116")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4124")
    Jump("loc_4173")

    label("loc_4124")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4132")
    Jump("loc_4173")

    label("loc_4132")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4140")
    Jump("loc_4173")

    label("loc_4140")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_414E")
    Jump("loc_4173")

    label("loc_414E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_415C")
    Jump("loc_4173")

    label("loc_415C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_416A")
    Jump("loc_4173")

    label("loc_416A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4173")

    label("loc_4173")

    TalkEnd(0xFE)
    Return()

    # Function_10_3E7D end

    def Function_11_4177(): pass

    label("Function_11_4177")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4188")
    Jump("loc_4529")

    label("loc_4188")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4227")

    ChrTalk(
        0xF,
        "In this branch there's a lot of preserved food.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "...So, don't you lay your hands on the fish\x01",
            "in the water tank not even by mistake, ok?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4529")

    label("loc_4227")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4494")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_437D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42F2")

    ChrTalk(
        0xF,
        (
            "*haah*, as expected this\x01",
            "building is relaxing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Anyway, I hadn't foreseen this\x01",
            "independence development at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "...What's going to happen in the future?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4378")

    label("loc_42F2")


    ChrTalk(
        0xF,
        (
            "We have finally just come back...\x01",
            "Who could foresee this independence development.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "...What's going to happen in the future?\x02",
    )

    CloseMessageWindow()

    label("loc_4378")

    Jump("loc_448F")

    label("loc_437D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_440A")

    ChrTalk(
        0xF,
        "Our captain, Mr. Fisher, has not to be underestimated!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Gnnn, I to want to catch a\x01",
            "super big game like that once!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_448F")

    label("loc_440A")


    ChrTalk(
        0xF,
        (
            "Leaving that aside, at any rate I couldn't\x01",
            "foresee this independence development.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "...What's going to happen in the future?\x02",
    )

    CloseMessageWindow()

    label("loc_448F")

    Jump("loc_4529")

    label("loc_4494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_44A2")
    Jump("loc_4529")

    label("loc_44A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_44B0")
    Jump("loc_4529")

    label("loc_44B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_44BE")
    Jump("loc_4529")

    label("loc_44BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_44CC")
    Jump("loc_4529")

    label("loc_44CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_44DA")
    Jump("loc_4529")

    label("loc_44DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_44E8")
    Jump("loc_4529")

    label("loc_44E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_44F6")
    Jump("loc_4529")

    label("loc_44F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4504")
    Jump("loc_4529")

    label("loc_4504")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4512")
    Jump("loc_4529")

    label("loc_4512")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4520")
    Jump("loc_4529")

    label("loc_4520")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4529")

    label("loc_4529")

    TalkEnd(0xFE)
    Return()

    # Function_11_4177 end

    def Function_12_452D(): pass

    label("Function_12_452D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_453E")
    Jump("loc_4884")

    label("loc_453E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_45E1")

    ChrTalk(
        0x10,
        (
            "First there was a persistent situation where I couldn't\x01",
            "leave the city, and now I can't go out the branch...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "*sigh*, I can't wait to fish.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4884")

    label("loc_45E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_47EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_4693")

    ChrTalk(
        0x10,
        "The Independent State of Crossbell, eh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Not only with the Fishing Emperor Club, is it fate \x01",
            "that we can't get along well with the Empire too?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47EA")

    label("loc_4693")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4747")

    ChrTalk(
        0x10,
        (
            "Still, the guys from the Fishing \x01",
            "Emperor Club were really strong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Their love for fishing was\x01",
            "unmistakably real...\x01",
            "It was a good experience for me too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_47EA")

    label("loc_4747")


    ChrTalk(
        0x10,
        "Anyway, the Independent State of Crossbell, eh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Not only with the Fishing Emperor Club, is it fate \x01",
            "that we can't get along well with the Empire too?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47EA")

    Jump("loc_4884")

    label("loc_47EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_47FD")
    Jump("loc_4884")

    label("loc_47FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_480B")
    Jump("loc_4884")

    label("loc_480B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4819")
    Jump("loc_4884")

    label("loc_4819")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4827")
    Jump("loc_4884")

    label("loc_4827")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4835")
    Jump("loc_4884")

    label("loc_4835")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4843")
    Jump("loc_4884")

    label("loc_4843")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4851")
    Jump("loc_4884")

    label("loc_4851")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_485F")
    Jump("loc_4884")

    label("loc_485F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_486D")
    Jump("loc_4884")

    label("loc_486D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_487B")
    Jump("loc_4884")

    label("loc_487B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4884")

    label("loc_4884")

    TalkEnd(0xFE)
    Return()

    # Function_12_452D end

    def Function_13_4888(): pass

    label("Function_13_4888")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_491D")

    ChrTalk(
        0x11,
        (
            "Hm, anyhow, I am glad\x01",
            "I could save the Crossbell\x01",
            "branch from its crisis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Now I can return to\x01",
            "Liberl puffed up\x01",
            "with pride.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4926")

    label("loc_491D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4926")

    label("loc_4926")

    TalkEnd(0xFE)
    Return()

    # Function_13_4888 end

    def Function_14_492A(): pass

    label("Function_14_492A")

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

    def lambda_4A29():
        OP_9B(0x1, 0x101, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4A29)
    Sleep(300)

    def lambda_4A41():
        OP_9B(0x1, 0x102, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4A41)
    Sleep(300)

    def lambda_4A59():
        OP_9B(0x1, 0x109, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4A59)
    Sleep(300)

    def lambda_4A71():
        OP_9B(0x1, 0x105, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4A71)
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
        "#5POh...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Well-Dressed Man",
        "#11PHm, who're you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#6PW-What is it now...?\x02",
    )

    CloseMessageWindow()

    def lambda_4B45():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4B45)
    Sleep(50)

    def lambda_4B55():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4B55)
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
        "#11PI-If it isn't member Lloyd!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PYes, just at the right time.\x01",
            "Lloyd, could you tell it\x01",
            "to this person too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PThat the Fisherman's Guild, Crossbell Branch, is\x01",
            "a place for relaxation and refreshment for anglers \x01",
            "who love to coexist in peace and harmony, I mean.\x02",
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
        "#12P#00012FW-What could you be talking about?\x02",
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
            "#5PHmph, are you too related to the Fisherman's Guild?\x01",
            "Have you come to protest to get along or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FUhhm, it's true that\x01",
            "I'm a member, but...\x02",
        )
    )

    CloseMessageWindow()
    Sound(802, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd showed the Detective Notebook to the man and \x01",
            "explained they are doing an investigation at present.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    NpcTalk(
        0x8,
        "Well-Dressed Man",
        "#5PYou are...investigating suspicious housing units?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Well-Dressed Man",
        (
            "#5PHmph, it's true that we haven't legally registered yet... \x01",
            "Then, I'll formally introduce myself:\x01",
            "My name is Lakelord III.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe heir to the "Lakelord Corporation", the\x01",
            "leading fishing gear manufacturer of Zemuria,\x01",
            "which is based in the Erebonian Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAs for the "Fishing Emperor Club",\x01",
            "it's none other than the professional\x01",
            "fishing organization I represent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FThe Lakelord Corporation...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FLloyd, do you know it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FYeah, because if you're someone\x01",
            "who does fishing it's a famous\x01",
            "name you almost always hear.\x02\x03",
            "#00000FIn any case, they are the No. 1\x01",
            "manufacturers always at the top in\x01",
            "the continent with their fishing gears.\x02",
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
            "#12P#10101FBut, why is such a\x01",
            "man in Crossbell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHmph, of course it's for further\x01",
            "growing and expanding the scale\x01",
            "of my Fishing Emperor Club.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThen, having a new office\x01",
            "here it's its foothold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIncidentally, this document states\x01",
            "the legality of the contract.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00001F...Please allow me to check.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_9B(0x1, 0x101, 0x0, 0x7D0, 0x7D0, 0x0)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#12P#00005FThis...\x01",
            "This is a rental agreement.\x02\x03",
            "#00003FIt is indeed as you say. The current\x01",
            "contractor is the Fishing Emperor Club.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PHu hu, did you understand?\x02",
    )

    CloseMessageWindow()
    OP_9B(0x1, 0x101, 0xB4, 0x7D0, 0x7D0, 0x0)
    Sleep(50)

    ChrTalk(
        0xF,
        (
            "#11PMember Lloyd...\x01",
            "You can't approve of this violence.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)

    ChrTalk(
        0x101,
        "#6P#00005FViolence, you say...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PYes, the truth is that this man plundered \x01",
            "the contract with force without any \x01",
            "permission from Branch Manager Celdan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PHe spared no mira and gave detailed\x01",
            "instructions to the real estate company.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#5PHmph, maybe it was a little forceful method,\x01",
            "but the document officiality is not in question.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAlso, this place is, to begin with,\x01",
            "wasted for the likes of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYou, of the "Fisherman's Guild",\x01",
            "who think that fishing is just a\x01",
            "pastime and use illicit tools.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00001FH-Hey now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PAnyhow, I'm done with the talkings.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIf you have understood, leave quickly\x01",
            "and inform that Celdan or whoever too.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    ChrTalk(
        0x8,
        "#11P...Sylum, I leave the rest to you.\x02",
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

    def lambda_57C8():
        OP_93(0xF, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_57C8)
    Sleep(50)

    def lambda_57D8():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_57D8)
    Sleep(50)

    def lambda_57E8():
        TurnDirection(0x102, 0x8, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_57E8)
    Sleep(50)

    def lambda_57F8():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_57F8)
    Sleep(50)

    def lambda_5808():
        TurnDirection(0x105, 0x8, 300)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5808)
    Sleep(50)

    def lambda_5818():
        TurnDirection(0xE, 0x8, 300)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5818)

    ChrTalk(
        0xF,
        "#12PAh, running away is cowardice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12PThat's right, we still have\x01",
            "some things to say and...\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 1)

    ChrTalk(
        0x105,
        "#6P#10302FHu hu, he left.\x02",
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

    # Function_14_492A end

    def Function_15_58D8(): pass

    label("Function_15_58D8")

    OP_95(0x8, 8680, 0, 4760, 2000, 0x0)
    OP_95(0x8, 11520, 0, 4740, 2000, 0x0)
    OP_9B(0x0, 0x8, 0x10E, 0x7D0, 0x7D0, 0x0)
    Sleep(200)
    Return()

    # Function_15_58D8 end

    def Function_16_5913(): pass

    label("Function_16_5913")

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
            "How much does you have to make a\x01",
            "fool of us before you're satisfied!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F(What the...a quarrel?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F(Has something happened again...?)\x02",
    )

    CloseMessageWindow()

    def lambda_5AE3():
        OP_9B(0x1, 0xFE, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5AE3)
    Sleep(300)

    def lambda_5AFB():
        OP_9B(0x1, 0xFE, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5AFB)
    Sleep(300)

    def lambda_5B13():
        OP_9B(0x1, 0xFE, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5B13)
    Sleep(300)

    def lambda_5B2B():
        OP_9B(0x1, 0xFE, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5B2B)
    Sleep(300)

    def lambda_5B43():
        OP_9B(0x1, 0xFE, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5B43)
    OP_68(4190, 1400, 3520, 2500)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#00005FEveryone...\x01",
            "Is something wrong?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xE, 0x101, 500)

    ChrTalk(
        0xE,
        (
            "Yes, Lloyd...\x01",
            "You arrive at the right time.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5BE4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5BE4)
    Sleep(50)
    TurnDirection(0xF, 0x101, 500)

    ChrTalk(
        0x10,
        "Member Lloyd, listen to this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "The truth is that all of his comrades have appeared\x01",
            "in various fishing points outside the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "He suddenly blurted out that they\x01",
            "have monopolized those places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FM-Monopolizing the fishing points...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Yes, he said that outsiders of\x01",
            "the Fishing Emperor Club can't\x01",
            "fish in those places...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I ignored him and forced myself in,\x01",
            "but when I did that, I was obstructed\x01",
            "by having my line snapped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106FThat's an awful story.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FExcuse me...why can't\x01",
            "you get all along?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmph, that's because the Fisherman's\x01",
            "Guild is a ludic amateur group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even just seeing them loitering around\x01",
            "in front of us, a supreme professional\x01",
            "group, is an eyesore.\x02",
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
            "Enjoying fishing has got nothing to\x01",
            "do with being pros or amateurs.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5F5C():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5F5C)
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
            "There're some reasonable big wheels among us too.\x01",
            "I wish you don't underestimate us.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "Ooh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "It's like the Branch Manager says!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I had to relinquish my title, but don't\x01",
            "make lightly of a "Master Fisherman"!\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x32, 0x0, 0x3E8, 0xC8)

    ChrTalk(
        0x8,
        "#4SHu hu, bwah ha ha ha hah!!#3S\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Interesting.\x01",
            "I didn't expect I could hear\x01",
            "such words from you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you insist, then...\x01",
            "Why don't you undertake\x01",
            "the "Angler Duels"?\x02",
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
        "A-Angler Duels...?\x02",
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
            "#00005FE-Ehmm...\x01",
            "What're the "Angler Duels"...?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6234():
        TurnDirection(0x10, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_6234)
    Sleep(50)

    def lambda_6244():
        TurnDirection(0xE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_6244)
    Sleep(50)

    def lambda_6254():
        TurnDirection(0xF, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_6254)
    Sleep(50)
    WaitChrThread(0x10, 0)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xF, 0)

    ChrTalk(
        0xE,
        (
            "Well, just as the name indicates, they're\x01",
            "confrontations done through fishing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "A match named as "Angler Duel" has\x01",
            "an absolute meaning to an angler.\x02",
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
        "I've never done one, but...\x01\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I heard of stories of anglers who lost their\x01",
            "entire fortune by losing in those matches.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "In other words, you can't lose by all means...\x01",
            "They're those kind of battles.\x02",
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
        "#00306FSomehow that's crazy stuff...\x02",
    )

    CloseMessageWindow()

    def lambda_651B():
        TurnDirection(0x10, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_651B)
    Sleep(50)

    def lambda_652B():
        TurnDirection(0xE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_652B)
    Sleep(50)

    def lambda_653B():
        TurnDirection(0xF, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_653B)
    Sleep(50)
    WaitChrThread(0x10, 0)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xF, 0)

    ChrTalk(
        0x10,
        "So...what're the duels rules?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Let's see, there're four of my comrades who\x01",
            "have already come to Crossbell and I.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If even one of you challenges us\x01",
            "five and defeats all of us, it'll\x01",
            "be your victory. What about it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You're free to challenge us how many\x01",
            "times you want, but...until you win the\x01",
            "duels, you will overlook our whims.\x02",
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
            "............\x01",
            "...And in case we win?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hm, it's a remote possibility that a miracle happens,\x01",
            "but I guess you too want to dream, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, by defeating each one of us we will\x01",
            "of course set free the fishing points in order...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you manage to defeat all five of us, we\x01",
            "will completely withdraw from Crossbell...\x01",
            "And we'll hand over this office too, naturally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Furthermore...\x01",
            "I'll listen to one of your orders, whatever it is.\x02",
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
            "#10302FHu hu, but can we\x01",
            "really trust you?\x02\x03",
            "#10300FIt seems that even if they won there's\x01",
            "no guarantee you'd keep your promise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "No, like Peter said just before, the result\x01",
            "of an Angler Duel is absolute to an angler.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Then, no matter what our attitude towards\x01",
            "fishing is, no doubt these guys have a\x01",
            "pride as anglers more than others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I can say that breaking a\x01",
            "promise for them is unlikely.\x02",
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
        "#00100FSo that's what it is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hu hu, Celdan...\x01",
            "Contrary to expectations, even you understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "So, what do you want to do?\x01",
            "Do you want to try challenging us?\x02",
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
        "...All right, we will challenge you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hu hu, as you wish.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x10, 500)

    ChrTalk(
        0xE,
        "Are you sure, branch manager?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "If we don't win, we'll have to abide\x01",
            "to their whims forever, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Eh eh, but on the contrary, we can challenge \x01",
            "them as many times as we want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Being things like this, frankly,\x01",
            "don't you think it'll be an easy victory?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "No matter how strong they are,\x01",
            "no one can keep winning\x01",
            "at fishing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FIndeed...\x01",
            "It's just a hunch, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hu hu, it appears that you\x01",
            "don't understand well what\x01",
            "fishing is, yet.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x8, 500)

    ChrTalk(
        0x8,
        (
            "Well, whatever, incidentally\x01",
            "I will only allow to challenge me\x01",
            "who has defeated my four comrades.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In addition, I will indicate reasonable\x01",
            "qualifications for challenging them too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As you can expect, we don't have the time to face\x01",
            "people who don't have a certain level of skills.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Please understand that point.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Yes...I understand.\x02",
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
            "Well, if there're other things\x01",
            "you don't understand, you can ask\x01",
            "Sylum, the receptionist, later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wonder if you will really be suitable \x01",
            "opponents for the "Elite Four", the\x01",
            "pride of my Fishing Emperor Club?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 7)
    NewScene("c1000", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_16_5913 end

    def Function_17_709C(): pass

    label("Function_17_709C")

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
        "Hm...what do you want?\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "You aren't going to tell me\x01",
            "you have beaten all the\x01",
            "Elite Four, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FUhmm, well, it's as you say...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmph...then, will you\x01",
            "show me their medals?\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd showed to Lakelord III\x01",
            "the four medals he received\x01",
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
            "Indeed, these are, without\x01",
            "doubt, the Elite Four medals...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Hu hu, to think that someone\x01",
            "would appear to challenge me,\x01",
            "the "Fishing Emperor"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F"F-Fishing Emperor"...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Yes.\x01",
            "I am Lakelord III, the "Fishing Emperor".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I am who gave the club that name and\x01",
            "also who reigns at the top of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In any case... I'll go on ahead to the \x01",
            "decisive battlefield and wait for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "The place is St. Ursula Byroad sandbank.\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x4)

    def lambda_7471():

        label("loc_7471")

        TurnDirection(0x101, 0x8, 500)
        Yield()
        Jump("loc_7471")

    QueueWorkItem2(0x101, 2, lambda_7471)

    def lambda_7483():

        label("loc_7483")

        TurnDirection(0x102, 0x8, 500)
        Yield()
        Jump("loc_7483")

    QueueWorkItem2(0x102, 2, lambda_7483)

    def lambda_7495():

        label("loc_7495")

        TurnDirection(0x109, 0x8, 500)
        Yield()
        Jump("loc_7495")

    QueueWorkItem2(0x109, 2, lambda_7495)

    def lambda_74A7():

        label("loc_74A7")

        TurnDirection(0x105, 0x8, 500)
        Yield()
        Jump("loc_74A7")

    QueueWorkItem2(0x105, 2, lambda_74A7)

    def lambda_74B9():

        label("loc_74B9")

        TurnDirection(0x104, 0x8, 500)
        Yield()
        Jump("loc_74B9")

    QueueWorkItem2(0x104, 2, lambda_74B9)

    def lambda_74CB():

        label("loc_74CB")

        TurnDirection(0x103, 0x8, 500)
        Yield()
        Jump("loc_74CB")

    QueueWorkItem2(0x103, 2, lambda_74CB)

    def lambda_74DD():
        OP_95(0xFE, -210, 0, 50780, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_74DD)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0xB4, 0x1F4)

    def lambda_7502():
        OP_9B(0x1, 0xFE, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7502)
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

    # Function_17_709C end

    def Function_18_755D(): pass

    label("Function_18_755D")

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

    def lambda_763B():
        OP_95(0xFE, 3330, 0, 4330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_763B)

    def lambda_7655():
        OP_95(0xFE, 2310, 0, 3310, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7655)
    BeginChrThread(0x102, 3, 0, 19)
    BeginChrThread(0x104, 3, 0, 20)

    def lambda_767B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_767B)

    def lambda_768C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_768C)

    def lambda_769D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_769D)

    def lambda_76AE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_76AE)
    Sleep(1000)
    BeginChrThread(0x10, 3, 0, 21)
    Sleep(50)
    BeginChrThread(0x11, 3, 0, 21)
    OP_6F(0x1)

    ChrTalk(
        0x10,
        "#11POoh, if it isn't member Lloyd.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x11,
        "Fisher",
        (
            "Hm, so you're the rumored\x01",
            "Lloyd Bannings of the SSS.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FYes I am...\x01",
            "What happened to the Fishing Emperor Club people?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00000FI see, you were able to win\x01",
            "all the Angler Duels, eh?\x02",
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
            "due to this man here, our\x01",
            "leader, Mr. Fisher!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00005FY-You're the Fisherman's Guild leader...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#11PMy, even so, to think\x01",
            "you could splendidly\x01",
            "catch that big Guardian...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#11PI hadn't been so excited\x01",
            "in a long time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Dear me, everything was possible\x01",
            "because of the Rainbow Gem EX\x01",
            "you all developed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "At all events, I'm \x01",
            "glad I could get \x01",
            "back the office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004FI-I see...\x01",
            "Thank you very much.\x02",
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

    # Function_18_755D end

    def Function_19_7A1F(): pass

    label("Function_19_7A1F")

    OP_95(0xFE, 4310, 0, 3130, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_19_7A1F end

    def Function_20_7A3B(): pass

    label("Function_20_7A3B")

    OP_95(0xFE, 3310, 0, 2130, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_20_7A3B end

    def Function_21_7A57(): pass

    label("Function_21_7A57")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x101, 500)
    OP_4B(0xFE, 0xFF)
    Return()

    # Function_21_7A57 end

    SaveToFile()

Try(main)
