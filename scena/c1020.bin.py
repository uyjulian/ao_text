from ScenarioHelper import *

def main():
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
        "儗僀 僋儘 乕僪 嘨悽",       # 1
        "庴晅 忟僙 僀儔 乕儉",       # 2
        "嬧橥 僩儕 僩儞",           # 3
        "棾媨 僇僌 儎",             # 4
        "悈嫸 僫儖 僙僗",           # 5
        "奀恘 僔儍 乕僋 儅儞",       # 6
        "Falsehood",               # 7
        "僐僷 儞",                 # 8
        "Penetrating",         # 9
        "僢僔 儍乕 insertion",       # 10
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
        "Function_4_1021",         # 04, 4
        "Function_5_1025",         # 05, 5
        "Function_6_30C6",         # 06, 6
        "Function_7_31C7",         # 07, 7
        "Function_8_32D3",         # 08, 8
        "Function_9_3409",         # 09, 9
        "Function_10_34F4",        # 0A, 10
        "Function_11_37B4",        # 0B, 11
        "Function_12_3AE6",        # 0C, 12
        "Function_13_3D80",        # 0D, 13
        "Function_14_3E24",        # 0E, 14
        "Function_15_4BC4",        # 0F, 15
        "Function_16_4BFF",        # 10, 16
        "Function_17_60D2",        # 11, 17
        "Function_18_650E",        # 12, 18
        "Function_19_69CB",        # 13, 19
        "Function_20_69E7",        # 14, 20
        "Function_21_6A03",        # 15, 21
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
    Jump("loc_101D")

    label("loc_576")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_675")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62D")

    ChrTalk(
        0x8,
        (
            "They are not\x01",
            "What is calling Harvard ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "…… Huh, but I hope and fulfilled.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway, for me\x01",
            "It's like being in the crossbell.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_670")

    label("loc_62D")


    ChrTalk(
        0x8,
        (
            "Come on now, Harvard ……\x01",
            "I will give you guidance directly!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_670")

    Jump("loc_6D8")

    label("loc_675")


    ChrTalk(
        0x8,
        "If you use a boat cabinet …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Certainly, that atmosphere\x01",
            "It may be a challenge to train … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D8")

    Jump("loc_101D")

    label("loc_6DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A4")

    ChrTalk(
        0x8,
        (
            "To our Emperor's Club and Fishing public division\x01",
            "There are not a few famous fellows.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I do not think you know anything … …\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "…… Hun, you said things just.\x01",
            "Forget about the story now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_7D9")

    label("loc_7A4")


    ChrTalk(
        0x8,
        (
            "…… Hun, you said things just.\x01",
            "Forget about the story now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D9")

    Jump("loc_101D")

    label("loc_7DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_94F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C1")

    ChrTalk(
        0x8,
        (
            "Apparently, Serdans are\x01",
            "It seems to be accepting defeat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Huff, but still at this point\x01",
            "I do not even arrive at this one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The passion for your fishing is\x01",
            "Apparently it seemed like a pretense.\x01",
            "Hu ha ha ha ha.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_94A")

    label("loc_8C1")


    ChrTalk(
        0x8,
        (
            "Huff, at this point yet\x01",
            "I do not even arrive at this one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The passion for your fishing is\x01",
            "Apparently it seemed like a pretense.\x01",
            "Hu ha ha ha ha.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_94A")

    Jump("loc_101D")

    label("loc_94F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_AB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A2C")

    ChrTalk(
        0x8,
        (
            "My father Lakewood Yeonsee\x01",
            "He is the greatest and greatest fisherman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At our Lakeload company,\x01",
            "Fishing gear with its name\x01",
            "I have developed a couple of them … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "All of them, my father\x01",
            "It is designed by my own hand.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_AB3")

    label("loc_A2C")


    ChrTalk(
        0x8,
        (
            "My father Lakewood Yeonsee\x01",
            "He is the greatest and greatest fisherman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That intolerable inquiry mind is\x01",
            "Always beyond our imagination … …\x01",
            "It is exactly the ultimate hobbyist.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB3")

    Jump("loc_101D")

    label("loc_AB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB6")

    ChrTalk(
        0x8,
        (
            "Members of our crown club,\x01",
            "Everyone is a professional elite fisher.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And all of the fishing fruits\x01",
            "For the development of Lake Road's new product\x01",
            "Feedback has been done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A fishing public division etc.\x01",
            "Half the tea girls who played\x01",
            "It is different from the fundamental.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C41")

    label("loc_BB6")


    ChrTalk(
        0x8,
        (
            "Members of our crown crown party,\x01",
            "Everyone is a professional elite fisher.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A fishing public division etc.\x01",
            "Half the tea girls who played\x01",
            "It is different from the fundamental.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C41")

    Jump("loc_101D")

    label("loc_C46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_CF2")

    ChrTalk(
        0x8,
        (
            "Hmm, with advocacy of independence etc\x01",
            "Something Crossbell people doing selfishness\x01",
            "It seems to be overwhelmed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anxiety of this land, my mother country\x01",
            "Eleventh is the only thing that exists\x01",
            "Why do not you understand.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_101D")

    label("loc_CF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_D81")

    ChrTalk(
        0x8,
        (
            "Hmm, on the crossbell\x01",
            "Many surprising fishing spots are there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It is a pity that there is no sea,\x01",
            "It is quite rich in fish species\x01",
            "You are entertained.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_101D")

    label("loc_D81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_ECB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E41")

    ChrTalk(
        0x8,
        "Are you doing well with the bombing match?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Huff, do not push yourself if it gets hard\x01",
            "You can surrender to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "What, at that time you crossbell\x01",
            "I just can not fish freely.\x01",
            "Huhahahahaha!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EC6")

    label("loc_E41")


    ChrTalk(
        0x8,
        (
            "Huff, do not push yourself if it gets hard\x01",
            "You can surrender to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "What, at that time you crossbell\x01",
            "I just can not fish freely.\x01",
            "Huhahahahaha!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EC6")

    Jump("loc_101D")

    label("loc_ECB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_F60")

    ChrTalk(
        0x8,
        (
            "Huh, how far can you do\x01",
            "I will be looking forward to it at most.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, the result is\x01",
            "It is more evident than looking at fire.\x01",
            "Huhahahahaha!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_101D")

    label("loc_F60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1014")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FD2")

    ChrTalk(
        0x8,
        "I thought … was still there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There is nothing to talk with you any more.\x01",
            "Get off quickly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_100F")

    label("loc_FD2")


    ChrTalk(
        0x8,
        (
            "There is nothing to talk with you any more.\x01",
            "Get off quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_100F")

    Jump("loc_101D")

    label("loc_1014")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_101D")

    label("loc_101D")

    TalkEnd(0xFE)
    Return()

    # Function_3_53E end

    def Function_4_1021(): pass

    label("Function_4_1021")

    Call(0, 5)
    Return()

    # Function_4_1021 end

    def Function_5_1025(): pass

    label("Function_5_1025")

    TalkBegin(0x9)
    ClearScenarioFlags(0x0, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1053")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1047")
    SetScenarioFlags(0x0, 2)

    label("loc_1047")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_1053")
    SetScenarioFlags(0x0, 2)

    label("loc_1053")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_105D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_111C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B9")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",                  # 0
            "Listen to the explanation of the bomb victory\x01",      # 1
            "quit\x01",                    # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jump("loc_1117")

    label("loc_10B9")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_110D")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_1117")

    label("loc_110D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1117")

    Jump("loc_1126")

    label("loc_111C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1126")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1157")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1146")
    OP_AF(0x36)
    Jump("loc_1148")

    label("loc_1146")

    OP_AF(0x37)

    label("loc_1148")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_30BD")

    label("loc_1157")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CE8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1170")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CE3")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "About agreement of game\x01",          # 0
            "About the qualification necessary for the challenge\x01",        # 1
            "About the whereabouts of Fisher Four\x01",      # 2
            "quit\x01",                          # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1392")

    ChrTalk(
        0x9,
        (
            "If you win all the bomb victories … …\x01",
            "I can get back this office,\x01",
            "It's a promise that you can order just one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There are five opponents in all.\x01",
            "Fishing Jie four heavenly king and Lake Road sama\x01",
            "That is your opponent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "By the way, when you win the Fisting Four Shitenno,\x01",
            "Currently managed by each\x01",
            "The fishing spot will be opened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Then, to challenge each person\x01",
            "I need qualifications ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Once you have your qualifications,\x01",
            "After that, you can challenge as many times as you like.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CDE")

    label("loc_1392")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BD4")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13AB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BC5")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Lake Road Yongsei\x01",      # 0
            "Ginza Triton\x01",          # 1
            "Ryugu Kaguya\x01",            # 2
            "Water mad Naruses\x01",          # 3
            "Sharp Edge Shark Man\x01",      # 4
            "quit\x01",                # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15A2")

    ChrTalk(
        0x9,
        (
            "Both names and clubs at the top of the club\x01",
            "To the reigning Lake Road\x01",
            "Qualification to challenge -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's fine,\x01",
            "\"Kill Five Shitennatsu all four people\"\x01",
            "You can get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Endlessly tough\x01",
            "I think it is difficult, but …\x01",
            "Overcome with spirit and guts.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1593")

    ChrTalk(
        0x9,
        (
            "- Well, you've already killed all four people.\x01",
            "Hehe, it's amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Mr. Lake Road as well\x01",
            "Leave only … … I wish for martial arts.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1593")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BC0")

    label("loc_15A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16F8")

    ChrTalk(
        0x9,
        (
            "It is touted as the strongest four king of heaven,\x01",
            "\"Silver Ring\" to Triton\x01",
            "Qualification to challenge -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's fine,\x01",
            "\"Fishing 29 kinds of prey\"\x01",
            "You can get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I think the road is pretty steep, but …\x01",
            "Do not give up until the very end and do your best.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 3)), scpexpr(EXPR_END)), "loc_16E9")

    ChrTalk(
        0x9,
        (
            "- Well,\x01",
            "You won Triton.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Huhu, if it is already\x01",
            "I did not need such information.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16E9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BC0")

    label("loc_16F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1855")

    ChrTalk(
        0x9,
        (
            "Loved by fishing gods,\x01",
            "\"Ryugu\" to Mr. Kaguya\x01",
            "Qualification to challenge -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's fine,\x01",
            "\"Fishing 130 big rice or more\"\x01",
            "You can get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Beyond technology,\x01",
            "I think luck will be important, though ….\x01",
            "Do your best and try hard.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 4)), scpexpr(EXPR_END)), "loc_1846")

    ChrTalk(
        0x9,
        (
            "- Well,\x01",
            "You won Kaguya-san.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Huhu, if it is already\x01",
            "I did not need such information.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1846")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BC0")

    label("loc_1855")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19CE")

    ChrTalk(
        0x9,
        (
            "I love myself beautiful fish\x01",
            "\"Water madman\" to Naruses\x01",
            "Qualification to challenge -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's fine,\x01",
            "\"Fishing the most beautiful fish in Crossbell\"\x01",
            "You can get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The standards are ambiguous, but …\x01",
            "Fishing up what you call this\x01",
            "Let Naruses shoot.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 5)), scpexpr(EXPR_END)), "loc_19BF")

    ChrTalk(
        0x9,
        (
            "- Well,\x01",
            "You won Mr. Naruses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Huhu, if it is already\x01",
            "I did not need such information.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19BF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BC0")

    label("loc_19CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BBB")

    ChrTalk(
        0x9,
        (
            "Contrary to the appearance known to the artisan\x01",
            "\"Sea blade\" to Sharkman\x01",
            "Qualification to challenge -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's fine,\x01",
            "\"Fishing six kinds of game fish\"\x01",
            "You can get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Detailed fish species, in the Graton Bus\x01",
            "Rock, Almorica beech -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In addition to Aranona in Piragna,\x01",
            "And Parulque.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Fishing up everything\x01",
            "I think it is pretty difficult, but …\x01",
            "Do your best.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 6)), scpexpr(EXPR_END)), "loc_1BAC")

    ChrTalk(
        0x9,
        (
            "- Well,\x01",
            "You won Sharkman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Huhu, if it is already\x01",
            "I did not need such information.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BAC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BC0")

    label("loc_1BBB")

    Jump("loc_1BC5")

    label("loc_1BC0")

    Jump("loc_13AB")

    label("loc_1BC5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CDE")

    label("loc_1BD4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CCF")

    ChrTalk(
        0x9,
        (
            "Sharkman is\x01",
            "\"Ursula intermittent pond\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Mr. Naruses\x01",
            "\"Mountain stream of Mainz mountain road\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Mr. Kaguya\x01",
            "\"Almorica ancient road resting place\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "And Triton\x01",
            "In \"Pond of West Crossbell Highway\"\x01",
            "You are coming, respectively.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CDE")

    label("loc_1CCF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CE3")

    label("loc_1CE3")

    Jump("loc_30BD")

    label("loc_1CDE")

    Jump("loc_1170")

    label("loc_1CE8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D0B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1E36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DAE")

    ChrTalk(
        0x9,
        (
            "A while ago, in Almorika village\x01",
            "With family and friends\x01",
            "I managed to get in touch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Future things\x01",
            "I am worried about various things … ….\x01",
            "Anyway I was relieved.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E31")

    label("loc_1DAE")


    ChrTalk(
        0x9,
        (
            "Even so ……\x01",
            "Everyone is a hardcore fishing idiot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The branch manager and Peter also\x01",
            "Copan is going to fish at once\x01",
            "I went out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E31")

    Jump("loc_30BD")

    label("loc_1E36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1EA6")

    ChrTalk(
        0x9,
        (
            "……Yup,\x01",
            "Even so, it is a disturbing situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Everyone in Almorika village\x01",
            "I hope it is safe ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30BD")

    label("loc_1EA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_207D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_1F31")

    ChrTalk(
        0x9,
        (
            "The activity of the fishing public division is also\x01",
            "When it is time to resume,\x01",
            "You did not have anything to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Would you like to return to Almorika village once?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2078")

    label("loc_1F31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FF8")

    ChrTalk(
        0x9,
        (
            "I, thanks to Lakeway sama\x01",
            "I was able to enter the fishing public division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Lake Road Mr.\x01",
            "He is very nice and a good one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Why, with the fishing public division\x01",
            "I wonder they can not make friends ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2078")

    label("loc_1FF8")


    ChrTalk(
        0x9,
        (
            "それにしてもThe activity of the fishing public division is also\x01",
            "When it is time to resume,\x01",
            "You did not have anything to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Would you like to return to Almorika village once?\x02",
    )

    CloseMessageWindow()

    label("loc_2078")

    Jump("loc_30BD")

    label("loc_207D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_24AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2122")

    ChrTalk(
        0x9,
        (
            "The final weapon of the fishing public division is,\x01",
            "She seems to be a person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "What kind of person,\x01",
            "I wonder if he is a fisherman ……\x01",
            "It makes me somewhat oddly excited.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24A9")

    label("loc_2122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_224B")

    ChrTalk(
        0x9,
        (
            "I heard it, it is over\x01",
            "You challenge Lake Road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The decisive battlefield is shallow in Ursula's …\x01",
            "Lake Road-sama is among the many fishing spots\x01",
            "It's the place I like the most.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I think it will be a difficult battle,\x01",
            "Please do your best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "And, if possible, with the Emperor 's Club\x01",
            "Take the relationship between the fishing public division.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_22E8")

    label("loc_224B")


    ChrTalk(
        0x9,
        (
            "The decisive battlefield is shallow in Ursula's …\x01",
            "Lake Road-sama is among the many fishing spots\x01",
            "It's the place I like the most.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I think it will be a difficult battle,\x01",
            "Please do your best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22E8")

    Jump("loc_24A9")

    label("loc_22ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2418")

    ChrTalk(
        0x9,
        (
            "Congratulations, Mr. Lloyd.\x01",
            "You pretty much won the game.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "And thanks to Lakeload-sama\x01",
            "I also heard that I entered the fishing public division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I mean,\x01",
            "Lake Road Mr.\x01",
            "I am very nice and kind one ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "How can I do with the fishing public division?\x01",
            "I wonder if I can resolve it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_24A9")

    label("loc_2418")


    ChrTalk(
        0x9,
        (
            "I mean,\x01",
            "Lake Road Mr.\x01",
            "I am very nice and kind one ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "How can I do with the fishing public division?\x01",
            "I wonder if I can resolve it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24A9")

    Jump("loc_30BD")

    label("loc_24AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_25F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_257B")

    ChrTalk(
        0x9,
        (
            "Mr. Lakeload,\x01",
            "An amateur fisher before\x01",
            "I told you I dislike … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Apparently, before that\x01",
            "Something personal to the fishing public division\x01",
            "You seem to have a feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I wonder, what happened?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_25F3")

    label("loc_257B")


    ChrTalk(
        0x9,
        (
            "Mr. Lakeload, apparently\x01",
            "Something personal to the fishing public division\x01",
            "It seems like a thought ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I wonder, what happened?\x02",
    )

    CloseMessageWindow()

    label("loc_25F3")

    Jump("loc_30BD")

    label("loc_25F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_26EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26A6")

    ChrTalk(
        0x9,
        (
            "Something recently, Serdan\x01",
            "Throwing in the final weapon or somehow\x01",
            "She seems to have muttered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "What on earth is it?\x01",
            "Well, I'm curious.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_26E9")

    label("loc_26A6")


    ChrTalk(
        0x9,
        (
            "What on earth is the final weapon?\x01",
            "Well, I'm curious.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26E9")

    Jump("loc_30BD")

    label("loc_26EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2772")

    ChrTalk(
        0x9,
        (
            "Lake Road Mr.\x01",
            "When you are talking about your father,\x01",
            "I always see my eyes shining.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Huhuu, that's great.\x02",
    )

    CloseMessageWindow()
    Jump("loc_30BD")

    label("loc_2772")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2842")

    ChrTalk(
        0x9,
        (
            "Mr. Lake Road like this\x01",
            "You have an imagination\x01",
            "I was praised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "What kind of fish are there in this fishing spot\x01",
            "How I live life ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That's the power to imagine that way\x01",
            "It's important for fishing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30BD")

    label("loc_2842")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_28D7")

    ChrTalk(
        0x9,
        (
            "Me too,\x01",
            "It came out to the city and it became considerable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Regular face is on sale ….\x01",
            "I relaxed at Almorika village\x01",
            "I'm nostalgic.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30BD")

    label("loc_28D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_298F")

    ChrTalk(
        0x9,
        (
            "Everyone of the four heavenly kings,\x01",
            "I just seemed to be playing\x01",
            "Actually, I have been doing a lot of work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As well as testing fishing tackle,\x01",
            "Distribution of water quality and ecology until investigation …\x01",
            "It really hurts me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30BD")

    label("loc_298F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2B81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AE5")

    ChrTalk(
        0x9,
        (
            "Laked Road-like family lines\x01",
            "I heard that he is succeeding the rank of the empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In the empire is a national character, an entrepreneur\x01",
            "There seems to be many aristocrats ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In the case of Lakeload, in addition,\x01",
            "It is amazing that a professional fisherman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Anything, fishing from childhood\x01",
            "It seems that you have received a gifted education.\x01",
            "…… I do not know what kind of education.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B7C")

    label("loc_2AE5")


    ChrTalk(
        0x9,
        (
            "I'm telling myself … but …\x01",
            "When thinking carefully, I think that gifted education for fishing\x01",
            "I can not imagine what it is like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… Next time on Mr. Lakeload\x01",
            "Should I ask?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B7C")

    Jump("loc_30BD")

    label("loc_2B81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2C0B")

    ChrTalk(
        0x9,
        (
            "Well, from Lake Road.\x01",
            "I've heard a detailed story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "What you do not know about the game\x01",
            "If you do, please ask me anything.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30BD")

    label("loc_2C0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_30B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3024")
    TurnDirection(0x9, 0x101, 0)

    ChrTalk(
        0x9,
        (
            "Er …\x01",
            "You are a person of the fishing public division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I, really to the fishing public division\x01",
            "I was planning to enter … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FTo the fishing public division …. Was that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Yeah, I was lost forever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "One day, joining the group\x01",
            "If you decide to come here\x01",
            "There is Lake Road-sama ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "While saying that it is okay\x01",
            "When I noticed it was accepted ……\x02",
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
        "#00106FYes, it was hard work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But I can not say that either way.\x01",
            "Sorry for making something ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Because of Mr. Lakeload\x01",
            "It makes me really good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The latest type made by Lake Road\x01",
            "You give me a fishing rod … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Personally when there is time\x01",
            "He will tell me about fishing,\x01",
            "Fishing food is unlimited unlimited use … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FThat's tremendous treatment ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "What is it, so I am complicated ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "First of all, Mr. Lakeload\x01",
            "I really dislike the fishing public division\x01",
            "It looks like … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As for me, I managed to do both\x01",
            "You want to make friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Something I can do\x01",
            "I wish I had it … ….\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13F, 6)
    Jump("loc_30AF")

    label("loc_3024")


    ChrTalk(
        0x9,
        (
            "Fishing public division and the Aime clubs ……\x01",
            "As for me, I managed to do both\x01",
            "You want to make friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Something I can do\x01",
            "I wish I had it … ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30AF")

    Jump("loc_30BD")

    label("loc_30B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_30BD")

    label("loc_30BD")

    Jump("loc_105D")

    label("loc_30C2")

    TalkEnd(0x9)
    Return()

    # Function_5_1025 end

    def Function_6_30C6(): pass

    label("Function_6_30C6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_30D7")
    Jump("loc_31C3")

    label("loc_30D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_313C")

    ChrTalk(
        0xA,
        (
            "No, no way\x01",
            "I guess they lose everyone ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "It was a lot of fun though it was fun.\x02",
    )

    CloseMessageWindow()
    Jump("loc_31C3")

    label("loc_313C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_314A")
    Jump("loc_31C3")

    label("loc_314A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3158")
    Jump("loc_31C3")

    label("loc_3158")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3166")
    Jump("loc_31C3")

    label("loc_3166")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3174")
    Jump("loc_31C3")

    label("loc_3174")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3182")
    Jump("loc_31C3")

    label("loc_3182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3190")
    Jump("loc_31C3")

    label("loc_3190")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_319E")
    Jump("loc_31C3")

    label("loc_319E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_31AC")
    Jump("loc_31C3")

    label("loc_31AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_31BA")
    Jump("loc_31C3")

    label("loc_31BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_31C3")

    label("loc_31C3")

    TalkEnd(0xFE)
    Return()

    # Function_6_30C6 end

    def Function_7_31C7(): pass

    label("Function_7_31C7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_31D8")
    Jump("loc_32CF")

    label("loc_31D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3248")

    ChrTalk(
        0xB,
        (
            "No way, that Gigaroook\x01",
            "I fished it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Funutsu\x01",
            "It has been decided as a fluke!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32CF")

    label("loc_3248")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3256")
    Jump("loc_32CF")

    label("loc_3256")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3264")
    Jump("loc_32CF")

    label("loc_3264")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3272")
    Jump("loc_32CF")

    label("loc_3272")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3280")
    Jump("loc_32CF")

    label("loc_3280")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_328E")
    Jump("loc_32CF")

    label("loc_328E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_329C")
    Jump("loc_32CF")

    label("loc_329C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_32AA")
    Jump("loc_32CF")

    label("loc_32AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_32B8")
    Jump("loc_32CF")

    label("loc_32B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_32C6")
    Jump("loc_32CF")

    label("loc_32C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_32CF")

    label("loc_32CF")

    TalkEnd(0xFE)
    Return()

    # Function_7_31C7 end

    def Function_8_32D3(): pass

    label("Function_8_32D3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_32E4")
    Jump("loc_3405")

    label("loc_32E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_333D")

    ChrTalk(
        0xC,
        (
            "The fishing public division won to us ……\x01",
            "~ ~, Buli Ho ー ー ー ー ー ー ー ー ー ー ッ!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3405")

    label("loc_333D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_338C")

    ChrTalk(
        0xC,
        (
            "Mysterious Armed Group ……\x01",
            "~ ~, Nut · Buriho!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3405")

    label("loc_338C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_339A")
    Jump("loc_3405")

    label("loc_339A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_33A8")
    Jump("loc_3405")

    label("loc_33A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_33B6")
    Jump("loc_3405")

    label("loc_33B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_33C4")
    Jump("loc_3405")

    label("loc_33C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_33D2")
    Jump("loc_3405")

    label("loc_33D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_33E0")
    Jump("loc_3405")

    label("loc_33E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_33EE")
    Jump("loc_3405")

    label("loc_33EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_33FC")
    Jump("loc_3405")

    label("loc_33FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3405")

    label("loc_3405")

    TalkEnd(0xFE)
    Return()

    # Function_8_32D3 end

    def Function_9_3409(): pass

    label("Function_9_3409")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_341A")
    Jump("loc_34F0")

    label("loc_341A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3469")

    ChrTalk(
        0xD,
        (
            "This big catch flag …… Ikasu.\x01",
            "Let's take it back to the empire!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34F0")

    label("loc_3469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3477")
    Jump("loc_34F0")

    label("loc_3477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3485")
    Jump("loc_34F0")

    label("loc_3485")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3493")
    Jump("loc_34F0")

    label("loc_3493")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_34A1")
    Jump("loc_34F0")

    label("loc_34A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_34AF")
    Jump("loc_34F0")

    label("loc_34AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_34BD")
    Jump("loc_34F0")

    label("loc_34BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_34CB")
    Jump("loc_34F0")

    label("loc_34CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_34D9")
    Jump("loc_34F0")

    label("loc_34D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_34E7")
    Jump("loc_34F0")

    label("loc_34E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_34F0")

    label("loc_34F0")

    TalkEnd(0xFE)
    Return()

    # Function_9_3409 end

    def Function_10_34F4(): pass

    label("Function_10_34F4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3505")
    Jump("loc_37B0")

    label("loc_3505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_356B")

    ChrTalk(
        0xE,
        (
            "Umm … for the time being\x01",
            "Take care of the fishing tackle and also time\x01",
            "It seems to be just crushing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37B0")

    label("loc_356B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_371B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_3611")

    ChrTalk(
        0xE,
        (
            "No, no,\x01",
            "President Dieter is also bold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I understand the assertion … …\x01",
            "Can we go ahead with the crossbell\x01",
            "I will feel uneasy about it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3716")

    label("loc_3611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3689")

    ChrTalk(
        0xE,
        (
            "No, no,\x01",
            "Our head is Fisher\x01",
            "It is truly a tremendous person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Head of Fisher, Banza ~ a!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3716")

    label("loc_3689")


    ChrTalk(
        0xE,
        (
            "But President Dieter, too\x01",
            "It is bold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I understand the assertion … …\x01",
            "Can we go ahead with the crossbell\x01",
            "I feel insecure that it will not stop.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3716")

    Jump("loc_37B0")

    label("loc_371B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3729")
    Jump("loc_37B0")

    label("loc_3729")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3737")
    Jump("loc_37B0")

    label("loc_3737")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3745")
    Jump("loc_37B0")

    label("loc_3745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3753")
    Jump("loc_37B0")

    label("loc_3753")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3761")
    Jump("loc_37B0")

    label("loc_3761")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_376F")
    Jump("loc_37B0")

    label("loc_376F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_377D")
    Jump("loc_37B0")

    label("loc_377D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_378B")
    Jump("loc_37B0")

    label("loc_378B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3799")
    Jump("loc_37B0")

    label("loc_3799")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_37A7")
    Jump("loc_37B0")

    label("loc_37A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_37B0")

    label("loc_37B0")

    TalkEnd(0xFE)
    Return()

    # Function_10_34F4 end

    def Function_11_37B4(): pass

    label("Function_11_37B4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_37C5")
    Jump("loc_3AE2")

    label("loc_37C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_383C")

    ChrTalk(
        0xF,
        "There are plenty of preserved food in this branch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "…… So even if you make a mistake\x01",
            "Is it not to touch the fish in the aquarium from hands?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AE2")

    label("loc_383C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3A4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_3960")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38EE")

    ChrTalk(
        0xF,
        (
            "Oh, after all\x01",
            "This building will settle down ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "However, this independent development\x01",
            "Something I could not read at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "…… What will happen in the future?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_395B")

    label("loc_38EE")


    ChrTalk(
        0xF,
        (
            "Although I finally came back,\x01",
            "I could not read this independent development.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "…… What will happen in the future?\x02",
    )

    CloseMessageWindow()

    label("loc_395B")

    Jump("loc_3A48")

    label("loc_3960")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39DD")

    ChrTalk(
        0xF,
        "Fischer head coach, you look awesome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Ku ~, I also like that super-big thing\x01",
            "I want to try to fish once!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3A48")

    label("loc_39DD")


    ChrTalk(
        0xF,
        (
            "Even so, for the time being\x01",
            "I could not read this independent development.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "…… What will happen in the future?\x02",
    )

    CloseMessageWindow()

    label("loc_3A48")

    Jump("loc_3AE2")

    label("loc_3A4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3A5B")
    Jump("loc_3AE2")

    label("loc_3A5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3A69")
    Jump("loc_3AE2")

    label("loc_3A69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3A77")
    Jump("loc_3AE2")

    label("loc_3A77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3A85")
    Jump("loc_3AE2")

    label("loc_3A85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3A93")
    Jump("loc_3AE2")

    label("loc_3A93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3AA1")
    Jump("loc_3AE2")

    label("loc_3AA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3AAF")
    Jump("loc_3AE2")

    label("loc_3AAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3ABD")
    Jump("loc_3AE2")

    label("loc_3ABD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3ACB")
    Jump("loc_3AE2")

    label("loc_3ACB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3AD9")
    Jump("loc_3AE2")

    label("loc_3AD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3AE2")

    label("loc_3AE2")

    TalkEnd(0xFE)
    Return()

    # Function_11_37B4 end

    def Function_12_3AE6(): pass

    label("Function_12_3AE6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3AF7")
    Jump("loc_3D7C")

    label("loc_3AF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3B7A")

    ChrTalk(
        0x10,
        (
            "If you think that the situation where you can not go outside the city has continued\x01",
            "I can not get out of branch this time …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Haa, do not want it to fish.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D7C")

    label("loc_3B7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3CE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_3BE6")

    ChrTalk(
        0x10,
        "Crossbell independent country ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "The Emperor 's Club Well, with Empire\x01",
            "Is it a fate that can not be friends?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CE2")

    label("loc_3BE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C85")

    ChrTalk(
        0x10,
        (
            "However, the people of the Emperor 's Club\x01",
            "It was really tough people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "The love for their fishing\x01",
            "Unquestionably authentic ……\x01",
            "I thank you for studying.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3CE2")

    label("loc_3C85")


    ChrTalk(
        0x10,
        "しかし、Crossbell independent country ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "The Emperor 's Club Well, with Empire\x01",
            "Is it a fate that can not be friends?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CE2")

    Jump("loc_3D7C")

    label("loc_3CE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3CF5")
    Jump("loc_3D7C")

    label("loc_3CF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3D03")
    Jump("loc_3D7C")

    label("loc_3D03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3D11")
    Jump("loc_3D7C")

    label("loc_3D11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3D1F")
    Jump("loc_3D7C")

    label("loc_3D1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3D2D")
    Jump("loc_3D7C")

    label("loc_3D2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3D3B")
    Jump("loc_3D7C")

    label("loc_3D3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3D49")
    Jump("loc_3D7C")

    label("loc_3D49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3D57")
    Jump("loc_3D7C")

    label("loc_3D57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3D65")
    Jump("loc_3D7C")

    label("loc_3D65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3D73")
    Jump("loc_3D7C")

    label("loc_3D73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3D7C")

    label("loc_3D7C")

    TalkEnd(0xFE)
    Return()

    # Function_12_3AE6 end

    def Function_13_3D80(): pass

    label("Function_13_3D80")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3E17")

    ChrTalk(
        0x11,
        (
            "Hmm, anyway\x01",
            "Save the crisis of the crossbell branch\x01",
            "It was good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "With this,\x01",
            "Stretch my heart and turn to Libert\x01",
            "It is possible to return.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E20")

    label("loc_3E17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3E20")

    label("loc_3E20")

    TalkEnd(0xFE)
    Return()

    # Function_13_3D80 end

    def Function_14_3E24(): pass

    label("Function_14_3E24")

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

    def lambda_3F23():
        OP_9B(0x1, 0x101, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F23)
    Sleep(300)

    def lambda_3F3B():
        OP_9B(0x1, 0x102, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3F3B)
    Sleep(300)

    def lambda_3F53():
        OP_9B(0x1, 0x109, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3F53)
    Sleep(300)

    def lambda_3F6B():
        OP_9B(0x1, 0x105, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3F6B)
    OP_68(4590, 1400, 3920, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#12P#00000F--Excuse me.\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#5POh……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "A good man",
        "#11PHmm, what are they?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#6PWhat is it …?\x02",
    )

    CloseMessageWindow()

    def lambda_4040():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4040)
    Sleep(50)

    def lambda_4050():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4050)
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
        "#11PB, Is not it a member of Lloyd? Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5POh, it was just right.\x01",
            "Lloyd also to this person\x01",
            "Can you tell me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PThis is a fishing public division · crossbell branch -\x01",
            "Of the anglers who love peace and coexistence\x01",
            "It is a place of relaxation.\x02",
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
        "#12P#00012FWhat kind of story is it?\x02",
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
        "A good man",
        (
            "#5PHun, are you a person closely related to the fishing public division?\x01",
            "Did you come to a friendly protest?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FUm, indeed\x01",
            "I am a member, but …\x02",
        )
    )

    CloseMessageWindow()
    Sound(802, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd showed the investigative notebook to the man,\x01",
            "I explained the survey that I am doing now.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    NpcTalk(
        0x8,
        "A good man",
        "#5PInvestigation of suspicious houses, … …?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "A good man",
        (
            "#5PHuun, certainly corporate registration was still,\x01",
            "Then, let's introduce ourselves anew -\x01",
            "My name is Lakewood Yeonsee.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBased in Erebonia Empire\x01",
            "Continental leading fishing gear maker,\x01",
            "It is a person who succeeds \"Lake Road company\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAnd \"The Emperor#4RAfternoon tea#The \"club\"\x01",
            "This I will be the representative\x01",
            "It is a professional fishing organization.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FLake Road Company ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FDo you know Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FOh, I am doing fishing\x01",
            "It's as humane as you can say\x01",
            "It's a name to hear.\x02\x03",
            "#00000FBy all means continental fishing gear share\x01",
            "Always keep running top\x01",
            "Immovable No. 1 Manufacturer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FI see, I see … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101FBut why such a person\x01",
            "To this crossbell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHuh, that is obvious\x01",
            "With further development of our crown club\x01",
            "It is to expand the scale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAnd here,\x01",
            "It was a foothold that made it an office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBy the way, the legitimacy of the contract\x01",
            "As this document shows.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00001F…… I will check it.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_9B(0x1, 0x101, 0x0, 0x7D0, 0x7D0, 0x0)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#12P#00005Fthis is……\x01",
            "It is a rental agreement for this property.\x02\x03",
            "#00003FCertainly as you say,\x01",
            "The current contractor is with the Emperor 's Club.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PHuh, did you understand?\x02",
    )

    CloseMessageWindow()
    OP_9B(0x1, 0x101, 0xB4, 0x7D0, 0x7D0, 0x0)
    Sleep(50)

    ChrTalk(
        0xF,
        (
            "#11PMembers of Lloyd ……\x01",
            "Such domineering, do not admit it.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)

    ChrTalk(
        0x101,
        "#6P#00005FDomineering, is not it …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PYeah, in fact this man\x01",
            "No obligation to Seldan branch chief,\x01",
            "I brutally deprived the contract.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PWith the power of Mira tired,\x01",
            "By including a real estate company.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#5PWhether Hun, or somewhat of a way,\x01",
            "It must be a formal procedure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBesides, here in the first place\x01",
            "It is an unacceptable property for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PFishing is just a hobby music\x01",
            "I think that it is a tool of familiarity,\x01",
            "You are the \"fishing public division\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00001FOh, you …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PAnyway, the story ends with this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POnce you understand it, you leave early,\x01",
            "Please also tell them to Serdan.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    ChrTalk(
        0x8,
        "#11P- Sailor, I will leave it to you later.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 300)

    ChrTalk(
        0x9,
        "#5PYes, I got it.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 1, 0, 15)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_4AB7():
        OP_93(0xF, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4AB7)
    Sleep(50)

    def lambda_4AC7():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4AC7)
    Sleep(50)

    def lambda_4AD7():
        TurnDirection(0x102, 0x8, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4AD7)
    Sleep(50)

    def lambda_4AE7():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4AE7)
    Sleep(50)

    def lambda_4AF7():
        TurnDirection(0x105, 0x8, 300)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4AF7)
    Sleep(50)

    def lambda_4B07():
        TurnDirection(0xE, 0x8, 300)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4B07)

    ChrTalk(
        0xF,
        "#12POh, it's cowardly fleeing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12PThat's right, here as well.\x01",
            "There is still something I want to say …\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 1)

    ChrTalk(
        0x105,
        "#6P#10302FHuh, it has gone.\x02",
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

    # Function_14_3E24 end

    def Function_15_4BC4(): pass

    label("Function_15_4BC4")

    OP_95(0x8, 8680, 0, 4760, 2000, 0x0)
    OP_95(0x8, 11520, 0, 4740, 2000, 0x0)
    OP_9B(0x0, 0x8, 0x10E, 0x7D0, 0x7D0, 0x0)
    Sleep(200)
    Return()

    # Function_15_4BC4 end

    def Function_16_4BFF(): pass

    label("Function_16_4BFF")

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
        "Fu, you playfully!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Well, how far we are\x01",
            "Is it fun if I make a fool?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F(What, is it a dispute?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F(Is there something else …??)\x02",
    )

    CloseMessageWindow()

    def lambda_4DB2():
        OP_9B(0x1, 0xFE, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4DB2)
    Sleep(300)

    def lambda_4DCA():
        OP_9B(0x1, 0xFE, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4DCA)
    Sleep(300)

    def lambda_4DE2():
        OP_9B(0x1, 0xFE, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4DE2)
    Sleep(300)

    def lambda_4DFA():
        OP_9B(0x1, 0xFE, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4DFA)
    Sleep(300)

    def lambda_4E12():
        OP_9B(0x1, 0xFE, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4E12)
    OP_68(4190, 1400, 3520, 2500)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#00005Feveryone……\x01",
            "What's wrong?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xE, 0x101, 500)

    ChrTalk(
        0xE,
        (
            "Oh, Lloyd … …\x01",
            "It was just right.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4EAD():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4EAD)
    Sleep(50)
    TurnDirection(0xF, 0x101, 500)

    ChrTalk(
        0x10,
        "Lloyd members, listen.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Actually, some of these colleagues,\x01",
            "It appears in fishing spots outside the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I suddenly monopolize those places\x01",
            "I did something to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FExclusive fishing spot ……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Yes, other than the crown club\x01",
            "Humans must fish at that place\x01",
            "Say something is wrong ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I neglected and took a step forward,\x01",
            "Then cut the thread off\x01",
            "It was obstructed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106FThat is a terrible story.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FUm … why?\x01",
            "Can not you make friends?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hun, that is because the fishing public division\x01",
            "Because it is a playful amateur group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It is the supremely professional group\x01",
            "When we are caught in front of us,\x01",
            "That's just an eyesore.\x02",
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
            "A, in an amateur\x01",
            "How bad is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "To enjoy fishing,\x01",
            "Neither professional nor amate will matter.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5194():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5194)
    Sleep(50)
    TurnDirection(0xF, 0x8, 500)

    ChrTalk(
        0x10,
        (
            "Oh, and you guys\x01",
            "I will show you results at various events\x01",
            "I know but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I also have a reasonable person in Uchi.\x01",
            "I do not want you to lick us.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "How is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "It is as the branch manager says!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I am returning now, but,\x01",
            "I will not lick \"Special Prize Wrestler\"!\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x32, 0x0, 0x3E8, 0xC8)

    ChrTalk(
        0x8,
        "#4SHuh, huh ha ha ha!#3S\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "……interesting.\x01",
            "Such words from you\x01",
            "It was surprising to hear it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If it says so far …\x01",
            "Special \"Bomb#4REmbankment#A game\x01",
            "Is there nothing to accept?\x02",
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
        "If it is a battle for a bomb … ….?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Anta, saneish?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FLet me see,\x01",
            "\"Bombing fight\" …?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_544C():
        TurnDirection(0x10, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_544C)
    Sleep(50)

    def lambda_545C():
        TurnDirection(0xE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_545C)
    Sleep(50)

    def lambda_546C():
        TurnDirection(0xF, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_546C)
    Sleep(50)
    WaitChrThread(0x10, 0)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xF, 0)

    ChrTalk(
        0xE,
        (
            "Yes, due to fishing as its name suggests\x01",
            "I will show you the confrontation … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "The game winning the name of \"bombing\"\x01",
            "It has an absolute meaning for the fisherman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Oh, the pride and honor of the fisherman … ….\x01",
            "And tangible and intangible things\x01",
            "It's a serious game to be done by betting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "What I actually did is\x01",
            "There is not something ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I lost all the wealth by losing the battle for explosion\x01",
            "Suddenly I heard the talk of a fisherman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "In other words, I can not lose anything ……\x01",
            "It's not such a fight.\x02",
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
        "#00006FWell, is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FSomething ridiculous …\x02",
    )

    CloseMessageWindow()

    def lambda_56DA():
        TurnDirection(0x10, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_56DA)
    Sleep(50)

    def lambda_56EA():
        TurnDirection(0xE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_56EA)
    Sleep(50)

    def lambda_56FA():
        TurnDirection(0xF, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_56FA)
    Sleep(50)
    WaitChrThread(0x10, 0)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xF, 0)

    ChrTalk(
        0x10,
        "So … What is the rule of the game?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That's right, now to crossbell\x01",
            "I and 4 people who are coming this -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We challenged all five of us,\x01",
            "If anyone can pull out five people,\x01",
            "How about your victory?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No matter how many times you challenge, but it is free …\x01",
            "Instead, unless you can do it\x01",
            "I will pass our wishes through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, of course,\x01",
            "It's limited to fishing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "………………………………\x01",
            "…… What if we win?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, it is a miracle in no case,\x01",
            "You guys would like to see a dream.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, with each victory\x01",
            "Of course to open fishing spots in order … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If we can win all five people,\x01",
            "We totally withdraw from the crossbell ……\x01",
            "Naturally deliver this office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "further--\x01",
            "Let 's hear only one instruction for anything.\x02",
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
        "#00005FHuh……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Ma, Magisu! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHuh, but really\x01",
            "Can I trust him?\x02\x03",
            "#10300FI will keep promises even if I win\x01",
            "There seems to be no guarantee, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "No, just as Peter said earlier\x01",
            "The result of the battle is absolute for the fisherman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "And how about the attitude towards us?\x01",
            "They are proud as a fisherman\x01",
            "There is no doubt that he has many times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "To break promises\x01",
            "It can be said that it is impossible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FI see, I see … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FIt is such a thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Huff, Serdan …\x01",
            "You are surprising, do not you understand the story?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "How do you do?\x01",
            "Do you want to challenge us a game?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "………………………….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "…… OK, let me challenge you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Huh, let's go.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x10, 500)

    ChrTalk(
        0xE,
        "Are you OK, Seldan?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "If I could not win, forever\x01",
            "It's a story to follow the other side of me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Hello, but instead\x01",
            "No matter how many times you challenge me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "That's what I said,\x01",
            "Honestly, is not it a victory?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "No matter how much skill it is\x01",
            "Humans who can keep winning with fishing\x01",
            "It's not from there ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006Fsurely……\x01",
            "I feel like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Heh, you guys\x01",
            "There is still much fishing\x01",
            "It does not seem to be well understood.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x8, 500)

    ChrTalk(
        0x8,
        (
            "Well, incidentally\x01",
            "It is permissible to challenge me\x01",
            "Only the one who knocked down the group of four people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In addition to challenging them,\x01",
            "Have them show appropriate qualifications.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Those who do not have the ability more than a certain level\x01",
            "I do not have time to make a partner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "You will get that point acknowledged.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Oh … I understand.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x10, 500)

    ChrTalk(
        0xE,
        "Serdan branch chief …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, something else too\x01",
            "If there is something you do not understand\x01",
            "Please listen to the receptionist's sailor later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Our boasted by the Emperor's Club\x01",
            "\"Fishing Jie#4RLantern#Four head orders \"… …\x01",
            "I wonder if you will serve as a partner, do you?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 7)
    NewScene("c1000", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_16_4BFF end

    def Function_17_60D2(): pass

    label("Function_17_60D2")

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
        "Wh … what the heck you?\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "No way, Fishing Jie four heavenly kings\x01",
            "Do not say that you've killed everyone\x01",
            "Is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FWell, that's nothing ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm … then,\x01",
            "Shall I show you the medals?\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Fishing Jie received from four heavenly kings\x01",
            "Four medals\x01",
            "I showed it to Lake Road.\x07\x00\x02",
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
            "Certainly, these are\x01",
            "Unquestionably the medal of the four heavenly kings … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "…… Huh, no doubt\x01",
            "Those who challenge this \"Empress\"\x01",
            "I will not show up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011FCha, \"The Empress\" … …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "- Naturally.\x01",
            "I am the \"Fisherman\" Lake Road 嘨 世.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Taking the name itself of the Emperor 's Club,\x01",
            "Moreover, he reigns at its top.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyways……\x01",
            "I'll be waiting at the battlefield ahead of the other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "The place is a shallow shoulder of Ursula.\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x4)

    def lambda_6422():

        label("loc_6422")

        TurnDirection(0x101, 0x8, 500)
        Yield()
        Jump("loc_6422")

    QueueWorkItem2(0x101, 2, lambda_6422)

    def lambda_6434():

        label("loc_6434")

        TurnDirection(0x102, 0x8, 500)
        Yield()
        Jump("loc_6434")

    QueueWorkItem2(0x102, 2, lambda_6434)

    def lambda_6446():

        label("loc_6446")

        TurnDirection(0x109, 0x8, 500)
        Yield()
        Jump("loc_6446")

    QueueWorkItem2(0x109, 2, lambda_6446)

    def lambda_6458():

        label("loc_6458")

        TurnDirection(0x105, 0x8, 500)
        Yield()
        Jump("loc_6458")

    QueueWorkItem2(0x105, 2, lambda_6458)

    def lambda_646A():

        label("loc_646A")

        TurnDirection(0x104, 0x8, 500)
        Yield()
        Jump("loc_646A")

    QueueWorkItem2(0x104, 2, lambda_646A)

    def lambda_647C():

        label("loc_647C")

        TurnDirection(0x103, 0x8, 500)
        Yield()
        Jump("loc_647C")

    QueueWorkItem2(0x103, 2, lambda_647C)

    def lambda_648E():
        OP_95(0xFE, -210, 0, 50780, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_648E)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0xB4, 0x1F4)

    def lambda_64B3():
        OP_9B(0x1, 0xFE, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_64B3)
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

    # Function_17_60D2 end

    def Function_18_650E(): pass

    label("Function_18_650E")

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

    def lambda_65EC():
        OP_95(0xFE, 3330, 0, 4330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_65EC)

    def lambda_6606():
        OP_95(0xFE, 2310, 0, 3310, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6606)
    BeginChrThread(0x102, 3, 0, 19)
    BeginChrThread(0x104, 3, 0, 20)

    def lambda_662C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_662C)

    def lambda_663D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_663D)

    def lambda_664E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_664E)

    def lambda_665F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_665F)
    Sleep(1000)
    BeginChrThread(0x10, 3, 0, 21)
    Sleep(50)
    BeginChrThread(0x11, 3, 0, 21)
    OP_6F(0x1)

    ChrTalk(
        0x10,
        "#11POh, it is a member of Lloyd.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x11,
        "Fischer",
        (
            "Hmm, you are the rumored special affairs support section\x01",
            "You are Lloyd · Bannings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FWell, yes, but … …\x01",
            "Is the people of the Emperor 's Club all together?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00000FThat's right, for all the bomb victories\x01",
            "You were able to win?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#11POh, that's it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#11PThat and this too -\x01",
            "All that we are here is\x01",
            "Fischer団長のおかげさ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00005FOh, you are the head of the fishing public division ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#11PWell, even so\x01",
            "A splendid look at that big lizard\x01",
            "What is to be caught … …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#11Pafter a long time\x01",
            "I was excited a lot!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "No, it is this too\x01",
            "The rainbow ball EX you developed\x01",
            "Wherever you are, that's it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Anyway,\x01",
            "I was able to regain my office\x01",
            "It was good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004FI see, I see … ….\x01",
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

    # Function_18_650E end

    def Function_19_69CB(): pass

    label("Function_19_69CB")

    OP_95(0xFE, 4310, 0, 3130, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_19_69CB end

    def Function_20_69E7(): pass

    label("Function_20_69E7")

    OP_95(0xFE, 3310, 0, 2130, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_20_69E7 end

    def Function_21_6A03(): pass

    label("Function_21_6A03")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x101, 500)
    OP_4B(0xFE, 0xFF)
    Return()

    # Function_21_6A03 end

    SaveToFile()

Try(main)
