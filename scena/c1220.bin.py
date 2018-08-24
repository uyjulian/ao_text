from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1220.bin",                # FileName
        "c1220",                    # MapName
        "c1220",                    # Location
        0x0020,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 32, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1220",                  # 0
        "Receptionist Tria",      # 1
        "McCunnen",               # 2
        "Reins",                  # 3
        "Grace",                  # 4
        "Nielsen",                # 5
        "Reporter Noticia",       # 6
        "Editor-in-Chief",        # 7
    ))

    AddCharChip((
        "chr/ch26602.itc",                   # 00
        "chr/ch45100.itc",                   # 01
        "chr/ch28100.itc",                   # 02
        "chr/ch06000.itc",                   # 03
        "chr/ch06002.itc",                   # 04
        "chr/ch26700.itc",                   # 05
        "chr/ch47900.itc",                   # 06
        "chr/ch20202.itc",                   # 07
        "chr/ch26600.itc",                   # 08
        "chr/ch20200.itc",                   # 09
        "chr/ch26702.itc",                   # 0A
    ))

    DeclNpc(5789,    0,       4294966866, 270,  261,  0x0, 0,   8,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(5099,    0,       60020,   0,    261,  0x0, 0,   5,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(4294966777, 0,       360,     0,    389,  0x0, 0,   2,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(6420,    0,       55520,   135,  389,  0x0, 0,   1,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   6,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(66250,   150,     8420,    270,  389,  0x0, 0,   9,   0,   255, 255, 0,   17,  255,  0)

    DeclEvent(0x0000, 0, 26,  -6.510000228881836,    5.110000133514404,     -0.5,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   3.255000114440918,     -2.555000066757202,    0.10000000149011612,   1.0])

    DeclActor(4100,    0,       4294966776, 1500,    5500,    1800,    4294966826, 0x007E, 0,  3,  0x0000)
    DeclActor(7270,    0,       54230,   1000,    7270,    1400,    54230,   0x007C, 0,  25, 0x0000)
    DeclActor(4294965546, 0,       60890,   1000,    4294965546, 1800,    60890,   0x007C, 0,  27, 0x0000)

    ChipFrameInfo(704, 0)                                        # 0

    ScpFunction((
        "Function_0_2C0",          # 00, 0
        "Function_1_370",          # 01, 1
        "Function_2_7B3",          # 02, 2
        "Function_3_863",          # 03, 3
        "Function_4_867",          # 04, 4
        "Function_5_1E55",         # 05, 5
        "Function_6_1FE2",         # 06, 6
        "Function_7_21EA",         # 07, 7
        "Function_8_23BD",         # 08, 8
        "Function_9_3079",         # 09, 9
        "Function_10_334B",        # 0A, 10
        "Function_11_370A",        # 0B, 11
        "Function_12_41D7",        # 0C, 12
        "Function_13_52DA",        # 0D, 13
        "Function_14_546A",        # 0E, 14
        "Function_15_5622",        # 0F, 15
        "Function_16_5798",        # 10, 16
        "Function_17_59FD",        # 11, 17
        "Function_18_5CA8",        # 12, 18
        "Function_19_665A",        # 13, 19
        "Function_20_6DBC",        # 14, 20
        "Function_21_71D4",        # 15, 21
        "Function_22_856B",        # 16, 22
        "Function_23_87F5",        # 17, 23
        "Function_24_A0D7",        # 18, 24
        "Function_25_A52A",        # 19, 25
        "Function_26_A649",        # 1A, 26
        "Function_27_A873",        # 1B, 27
    ))


    def Function_0_2C0(): pass

    label("Function_0_2C0")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_2F8"),
        (1, "loc_304"),
        (2, "loc_310"),
        (3, "loc_31C"),
        (4, "loc_328"),
        (5, "loc_334"),
        (6, "loc_340"),
        (SWITCH_DEFAULT, "loc_34C"),
    )


    label("loc_2F8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_304")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_310")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_31C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_328")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_334")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_340")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_34C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_358")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_36F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_36F")

    Return()

    # Function_0_2C0 end

    def Function_1_370(): pass

    label("Function_1_370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38B")
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)

    label("loc_38B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3FB")
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x7)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x9, 2160, 0, 60470, 270)
    SetChrPos(0xA, 760, 0, 60470, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F6")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x9, 0x10)

    label("loc_3F6")

    Jump("loc_7B2")

    label("loc_3FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_487")
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x7)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44F")
    SetChrPos(0x9, 66800, 0, 6990, 315)
    SetChrPos(0x8, 66780, 0, 5780, 315)
    SetChrSubChip(0xE, 0x1)
    Jump("loc_482")

    label("loc_44F")

    SetChrPos(0x9, 61280, 150, 340, 0)
    SetChrChipByIndex(0x9, 0xA)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrPos(0x8, 51300, 20, -970, 270)

    label("loc_482")

    Jump("loc_7B2")

    label("loc_487")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4CB")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xB, 480, 0, 760, 270)
    SetChrPos(0xA, -760, 0, 760, 90)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    Jump("loc_7B2")

    label("loc_4CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_50A")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x9, 6300, 0, 57090, 180)
    SetChrPos(0xD, 6420, 0, 55520, 0)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xD, 0x10)
    Jump("loc_7B2")

    label("loc_50A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_555")
    SetChrPos(0x9, -1000, 0, 60290, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xB, 6300, 0, 57090, 180)
    SetChrPos(0xA, 6420, 0, 55520, 0)
    Jump("loc_7B2")

    label("loc_555")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5B0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_57F")
    Jump("loc_5AB")

    label("loc_57F")

    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xB, 480, 0, 760, 270)
    SetChrPos(0xA, -760, 0, 760, 90)

    label("loc_5AB")

    Jump("loc_7B2")

    label("loc_5B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_5D9")
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 2690, 0, 60030, 0)
    Jump("loc_7B2")

    label("loc_5D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_602")
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 2690, 0, 60030, 0)
    Jump("loc_7B2")

    label("loc_602")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_67E")
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)
    SetChrPos(0xD, 3490, 20, 490, 135)
    SetChrFlags(0xD, 0x10)
    SetChrPos(0x9, -3840, 0, -1380, 270)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 530, 150, 56890, 180)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -420, 0, 710, 0)
    Jump("loc_7B2")

    label("loc_67E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_68C")
    Jump("loc_7B2")

    label("loc_68C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_69A")
    Jump("loc_7B2")

    label("loc_69A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6D4")
    SetChrPos(0x9, 3350, 0, 56470, 225)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 3490, 20, 490, 135)
    SetChrFlags(0xD, 0x10)
    Jump("loc_7B2")

    label("loc_6D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_718")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xB, 2690, 0, 60030, 270)
    SetChrPos(0xC, 1190, 0, 60030, 90)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)
    Jump("loc_7B2")

    label("loc_718")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_74D")
    SetChrPos(0x9, -3840, 0, -1380, 270)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 2690, 0, 60030, 0)
    Jump("loc_7B2")

    label("loc_74D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7B2")
    SetChrPos(0x9, 6420, 0, 55520, 0)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 6300, 0, 57090, 180)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 3380, 0, 60280, 135)
    SetChrFlags(0xA, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 2)), scpexpr(EXPR_END)), "loc_7B2")
    OP_93(0xA, 0x0, 0x0)

    label("loc_7B2")

    Return()

    # Function_1_370 end

    def Function_2_7B3(): pass

    label("Function_2_7B3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7CC")
    OP_10(0x0, 0x0)
    OP_10(0x5, 0x1)
    Jump("loc_7D2")

    label("loc_7CC")

    OP_10(0x0, 0x1)
    OP_10(0x5, 0x0)

    label("loc_7D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_7E0")
    ModifyEventFlags(0, 0, 0x80)

    label("loc_7E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_81D")
    SetMapObjFrame(0xFF, "light1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "light0", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_81D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_850")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "light1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "light0", 0x0, 0x1)

    label("loc_850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_862")
    OP_65(0x0, 0x1)

    label("loc_862")

    Return()

    # Function_2_7B3 end

    def Function_3_863(): pass

    label("Function_3_863")

    Call(0, 4)
    Return()

    # Function_3_863 end

    def Function_4_867(): pass

    label("Function_4_867")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AD3")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_994")

    ChrTalk(
        0x8,
        (
            "The Special Support\x01",
            "Section... Could you be here\x01",
            "for our company's request?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Actually, the person in\x01",
            "charge of it left to cover\x01",
            "the derailment incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm terribly sorry, but\x01",
            "I have to ask you to\x01",
            "come again another day.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_ACF")

    label("loc_994")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_A50")

    ChrTalk(
        0x8,
        (
            "The editorial staff is now working\x01",
            "on a news bulletin regarding the\x01",
            "derailment incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you have business with\x01",
            "any of the reporters, I'll\x01",
            "deliver your message.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ACF")

    label("loc_A50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_ACF")

    ChrTalk(
        0x8,
        (
            "To think a derailment\x01",
            "occurred along West\x01",
            "Crossbell Highway...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's not another act of\x01",
            "terror again, is it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ACF")

    TalkEnd(0x8)
    Return()

    label("loc_AD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_END)), "loc_CFE")
    TalkBegin(0x8)
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
            "Talk\x01",                 # 0
            "Report Coverage\x01",      # 1
            "Cancel\x01",               # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B4D")
    TalkEnd(0x8)
    Return()

    label("loc_B4D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_B79")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_B8C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_B9F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_BB2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_BC5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_BD8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_BEB")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_BFE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_C11")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_C11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_C24")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_C24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_C37")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_C37")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C64")
    TalkEnd(0x8)
    Call(0, 22)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C5E")
    Call(0, 23)

    label("loc_C5E")

    Return()

    label("loc_C64")


    ChrTalk(
        0x101,
        (
            "#00005F(Whoops, we haven't been\x01",
            "to at least 6\x01",
            "restaurants, have we.)\x02\x03",
            "#00003F(We can't report our\x01",
            "coverage now. Let's try\x01",
            "a little harder.)\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Return()

    label("loc_CF9")

    Jump("loc_D0C")

    label("loc_CFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D0C")
    Call(0, 20)
    Return()

    label("loc_D0C")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_E0B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC0")

    ChrTalk(
        0x8,
        (
            "Everyone, please do your\x01",
            "best with the gourmet\x01",
            "guide coverage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You get to eat a lot of\x01",
            "delicious food, so I think\x01",
            "you're going to enjoy it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E06")

    label("loc_DC0")


    ChrTalk(
        0x8,
        "Good work everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We'll be counting on you\x01",
            "in the future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E06")

    Jump("loc_1E51")

    label("loc_E0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_E96")

    ChrTalk(
        0x8,
        (
            "It seems Reins snuck into\x01",
            "the Geofront somehow and\x01",
            "had difficulty escaping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha. Anyway, I'm just\x01",
            "glad he's safe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E51")

    label("loc_E96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_EA4")
    Jump("loc_1E51")

    label("loc_EA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_109C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FB6")

    ChrTalk(
        0x8,
        (
            "It was frightening when\x01",
            "State Guard soldiers\x01",
            "came in this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's only been a week since\x01",
            "the declaration and things\x01",
            "are already this bad...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When people talk about tense\x01",
            "situations, they must be\x01",
            "talking about times like these.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1097")

    label("loc_FB6")


    ChrTalk(
        0x8,
        (
            "When I looked at the situation around\x01",
            "town, it seemed like there are still a\x01",
            "lot of people who support the President.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But if you ask me, there are more\x01",
            "who are unsure. ...I really wonder\x01",
            "what's going to happen now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1097")

    Jump("loc_1E51")

    label("loc_109C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_12EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1224")

    ChrTalk(
        0x8,
        (
            "The reconstruction after the\x01",
            "incident, and the referendum will\x01",
            "be held in three days' time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "These two matters give\x01",
            "the city a never before\x01",
            "seen sense of unity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Personally, I feel the arguments\x01",
            "in favor of independence are\x01",
            "strange and heated, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I think "It can't be helped" is a\x01",
            "natural thing to feel when\x01",
            "thinking about citizens' feelings.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12E7")

    label("loc_1224")


    ChrTalk(
        0x8,
        (
            "Personally, I feel the arguments\x01",
            "in favor of independence are\x01",
            "strange and heated, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I think "It can't be helped" is a\x01",
            "natural thing to feel when\x01",
            "thinking about citizens' feelings.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12E7")

    Jump("loc_1E51")

    label("loc_12EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_12FA")
    Jump("loc_1E51")

    label("loc_12FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_13C9")

    ChrTalk(
        0x8,
        (
            "It seems that Grace entered\x01",
            "the scene yesterday and got\x01",
            "scolded by the CGF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I understand her reporter's spirit,\x01",
            "but... I'm worried. I wish she'd\x01",
            "think about her safety a little more.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E51")

    label("loc_13C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_15CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1530")

    ChrTalk(
        0x8,
        (
            "I was very busy yesterday\x01",
            "running our contacts for\x01",
            "the derailment bulletin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thinking back on things, we've\x01",
            "had more opportunities for extra\x01",
            "issues than average this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But the amount of extras\x01",
            "with good news hasn't\x01",
            "changed at all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's nothing but incidents\x01",
            "and accidents. That makes\x01",
            "me a little depressed.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15C7")

    label("loc_1530")


    ChrTalk(
        0x8,
        (
            "But the amount of extras\x01",
            "with good news hasn't\x01",
            "changed at all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's nothing but incidents\x01",
            "and accidents. That makes\x01",
            "me a little depressed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15C7")

    Jump("loc_1E51")

    label("loc_15CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_1688")

    ChrTalk(
        0x8,
        (
            "The editorial staff is now working\x01",
            "on a news bulletin regarding the\x01",
            "derailment incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you have business with\x01",
            "any of the reporters, I'll\x01",
            "deliver your message.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E51")

    label("loc_1688")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_170C")

    ChrTalk(
        0x8,
        (
            "To think a derailment\x01",
            "occurred along West\x01",
            "Crossbell Highway...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's not another act of\x01",
            "terror again, is it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E51")

    label("loc_170C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_171D")
    Call(0, 6)
    Jump("loc_1E51")

    label("loc_171D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_19A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18D4")

    ChrTalk(
        0x8,
        (
            "A citizen's forum with "The Question of State\x01",
            "Independence" as the theme will be held at\x01",
            "City Meeting Hall in two days, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This was our suggestion, but the\x01",
            "city people asked us to hold it\x01",
            "in cooperation with them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ever since the independence proposal,\x01",
            "many readers have called for\x01",
            "referendum evaluation criteria...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Wondering if we can do\x01",
            "anything besides articles―\x01",
            "We made a suggestion.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_199D")

    label("loc_18D4")


    ChrTalk(
        0x8,
        (
            "Ever since the independence proposal,\x01",
            "many readers have called for\x01",
            "referendum evaluation criteria...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Wondering if we can do anything\x01",
            "besides articles― We proposed\x01",
            "holding a citizen's forum.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_199D")

    Jump("loc_1E51")

    label("loc_19A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1A6B")

    ChrTalk(
        0x8,
        (
            "Grace and Reins said they needed to\x01",
            "hurry and buy something and headed\x01",
            "for the department store, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They might be late for\x01",
            "the main session due to\x01",
            "that... What could it be?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E51")

    label("loc_1A6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1A7C")
    Call(0, 7)
    Jump("loc_1E51")

    label("loc_1A7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1B15")

    ChrTalk(
        0x8,
        (
            "The trade conference\x01",
            "finally begins tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The reporters are very busy\x01",
            "getting ready for it, giving\x01",
            "off a feeling of tension.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E51")

    label("loc_1B15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1D11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C5D")

    ChrTalk(
        0x8,
        (
            "I understand that Reins\x01",
            "is going to visit some\x01",
            "ruins today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Grace complained about\x01",
            "her obedient helper\x01",
            "being gone, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now that I think about\x01",
            "it, Reins joined our\x01",
            "company just this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even so, I think it's quite\x01",
            "something that we already rely\x01",
            "on him for a great many things.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D0C")

    label("loc_1C5D")


    ChrTalk(
        0x8,
        (
            "Everyone forgets so quickly,\x01",
            "but Reins just joined the\x01",
            "company this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even so, I think it's quite\x01",
            "something that we already rely\x01",
            "on him for a great many things.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D0C")

    Jump("loc_1E51")

    label("loc_1D11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1E51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DC7")

    ChrTalk(
        0x8,
        (
            "My, it's been a while.\x01",
            "The Special Support\x01",
            "Section, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Welcome to Crossbell News. If\x01",
            "you ever need anything,\x01",
            "please don't hesitate to ask.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E51")

    label("loc_1DC7")


    ChrTalk(
        0x8,
        (
            "Haha, Grace will be\x01",
            "overjoyed now that you've\x01",
            "resumed your activities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you ever need\x01",
            "anything, please don't\x01",
            "hesitate to ask.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E51")

    TalkEnd(0x8)
    Return()

    # Function_4_867 end

    def Function_5_1E55(): pass

    label("Function_5_1E55")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1EE3")

    ChrTalk(
        0xFE,
        (
            "It seems Reins snuck into\x01",
            "the Geofront somehow and\x01",
            "had difficulty escaping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. Anyway, I'm just\x01",
            "glad he's safe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FDE")

    label("loc_1EE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1F69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F02")
    TalkEnd(0xFE)
    Call(0, 18)
    Return()

    label("loc_1F02")


    ChrTalk(
        0xFE,
        (
            "I really hope Reins\x01",
            "doesn't do anything\x01",
            "reckless, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I pray that he's\x01",
            "safe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FDE")

    label("loc_1F69")


    ChrTalk(
        0xFE,
        (
            "Ah, everyone. You can't\x01",
            "enter from this side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have business,\x01",
            "speak with me from\x01",
            "across the counter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FDE")

    TalkEnd(0xFE)
    Return()

    # Function_5_1E55 end

    def Function_6_1FE2(): pass

    label("Function_6_1FE2")

    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2143")

    ChrTalk(
        0xD,
        (
            "Hmm, I see. I thought\x01",
            "that might be the case\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Incidentally, he's at Mining\x01",
            "Town Mainz and I think he'll\x01",
            "be back late as well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I think you should have\x01",
            "left a message that you\x01",
            "want to meet him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Well, you're certainly\x01",
            "right about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Then, if you'd deliver\x01",
            "the message for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Yes, understood.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_21E5")

    label("loc_2143")


    ChrTalk(
        0x8,
        (
            "Then once again, can I\x01",
            "ask where you're\x01",
            "staying?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yes, it's Old Dragon Inn\x01",
            "on East Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Please tell him I'll be\x01",
            "right there when he\x01",
            "contacts me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21E5")

    OP_4C(0xD, 0xFF)
    Return()

    # Function_6_1FE2 end

    def Function_7_21EA(): pass

    label("Function_7_21EA")

    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2322")

    ChrTalk(
        0xD,
        (
            "Hmm, too bad. Nielsen's\x01",
            "out of the office, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Sorry, he's almost never\x01",
            "at our office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He said he was going to\x01",
            "see a friend today. I can\x01",
            "take a message for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "No, that's all right. I\x01",
            "just wanted to spend some\x01",
            "time chatting with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "There will be other\x01",
            "chances.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_23B8")

    label("loc_2322")


    ChrTalk(
        0xD,
        (
            "Things being what they are, I'd\x01",
            "like to say hello to the editor-\x01",
            "in-chief. Is now a good time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, he just got back.\x01",
            "Please wait a moment.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23B8")

    OP_4C(0xD, 0xFF)
    Return()

    # Function_7_21EA end

    def Function_8_23BD(): pass

    label("Function_8_23BD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_23CE")
    Jump("loc_3075")

    label("loc_23CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_23DC")
    Jump("loc_3075")

    label("loc_23DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2485")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23F7")
    Call(0, 9)
    Jump("loc_2480")

    label("loc_23F7")

    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xB,
        (
            "#02100FAlright Reins, please\x01",
            "continue negotiating\x01",
            "with the State Guard.\x02\x03",
            "If anything happens,\x01",
            "I'll contact you\x01",
            "immediately.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)

    label("loc_2480")

    Jump("loc_3075")

    label("loc_2485")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2493")
    Jump("loc_3075")

    label("loc_2493")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_253B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24B2")
    TalkEnd(0xFE)
    Call(0, 19)
    Return()

    label("loc_24B2")


    ChrTalk(
        0xB,
        (
            "#02100FLloyd and friends, be\x01",
            "extremely careful.\x02\x03",
            "#02109FAnd once again, allow me\x01",
            "to write an article about\x01",
            "your great efforts!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3075")

    label("loc_253B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2774")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26CA")

    ChrTalk(
        0xB,
        (
            "#02100FAh, Lloyd and friends.\x01",
            "Nice work last night.\x02\x03",
            "#02101FAbout that... Do you\x01",
            "know something about\x01",
            "Wald?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FAh, no...\x02\x03",
            "#00001FWe went to Ignis this\x01",
            "morning but didn't get\x01",
            "any info.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02103FI see...\x02\x03",
            "#02102FWell, I'll try some of\x01",
            "my own ideas, then.\x02\x03",
            "#02100FAnd you too Wazy...\x01",
            "Don't think too hard,\x01",
            "okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHaha, thank you for your\x01",
            "concern.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x171, 1)
    Jump("loc_276F")

    label("loc_26CA")


    ChrTalk(
        0xB,
        (
            "#02101FEven so... I'm worried about those\x01",
            "blue flowers.\x02\x03",
            "#02103FIf there was someone other than\x01",
            "Joachim who could make that\x01",
            "medicine... That would be very bad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_276F")

    Jump("loc_3075")

    label("loc_2774")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2782")
    Jump("loc_3075")

    label("loc_2782")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2B82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A09")

    ChrTalk(
        0xB,
        (
            "#02104F*sigh*, a morning dose\x01",
            "really calms you down,\x01",
            "eh?\x02\x03",
            "#02102FWould any of you guys\x01",
            "like one? It's just\x01",
            "canned coffee, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FAh, no, but we\x01",
            "appreciate the thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02102FOh really? Haha, well\x01",
            "whatever.\x02\x03",
            "#02104FFor now, it looks like you did\x01",
            "a good job with yesterday's\x01",
            "Cryptid extermination.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FThat's certainly true,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F...You sure get word\x01",
            "fast.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02109FI guess. That's the\x01",
            "business we're in, after\x01",
            "all.\x02\x03",
            "#02100FIf nothing else, take\x01",
            "care not to get\x01",
            "yourselves hurt.\x02\x03",
            "#02102FAfter all is said and\x01",
            "done, our bodies are our\x01",
            "capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FSure, and thanks.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x171, 2)
    Jump("loc_2B7D")

    label("loc_2A09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ABE")

    ChrTalk(
        0xB,
        (
            "#02103FEven so, Cryptids, huh. I don't\x01",
            "really get it, but they're\x01",
            "strange and indescribable.\x02\x03",
            "#02100FLloyd and friends, take care\x01",
            "not to get yourselves hurt.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2B60")

    label("loc_2ABE")


    ChrTalk(
        0xB,
        (
            "#02100FAh, right, right. Once you've got\x01",
            "your recommended gourmet in order,\x01",
            "report to the reception desk, ok?\x02\x03",
            "#02109FAlright then, I'm counting on you♪\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 2)

    label("loc_2B60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2B7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2B7D")
    ClearScenarioFlags(0x0, 2)

    label("loc_2B7D")

    Jump("loc_3075")

    label("loc_2B82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2B90")
    Jump("loc_3075")

    label("loc_2B90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2B9E")
    Jump("loc_3075")

    label("loc_2B9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2BAC")
    Jump("loc_3075")

    label("loc_2BAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2C54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BC7")
    Call(0, 10)
    Jump("loc_2C4F")

    label("loc_2BC7")


    ChrTalk(
        0xB,
        (
            "#02102FAh, this is the Snowflake\x01",
            "Temple everyone's talking\x01",
            "about, huh.\x02\x03",
            "#02109FThank you very much. You\x01",
            "tried it once, didn't\x01",
            "you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C4F")

    Jump("loc_3075")

    label("loc_2C54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_306C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FD7")

    ChrTalk(
        0xB,
        (
            "#02102FAh, Lloyd and friends.\x01",
            "Same as yesterday, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha, you could say\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHow is your Heiyue\x01",
            "investigation going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02106FWell, slowly, I guess you\x01",
            "could say.\x02\x03",
            "#02100FI investigated other bidders,\x01",
            "but...\x02\x03",
            "If nothing else happens, that\x01",
            "whole place is going to belong\x01",
            "to Heiyue at this rate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10103FIs that so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02106FWell, nobody can say anymore\x01",
            "without lifting the cover.\x02\x03",
            "#02100FAnd so, I plan to finish up\x01",
            "all this work that's been\x01",
            "piling up today.\x02\x03",
            "#02102FOh yeah! I'll be sure to write\x01",
            "an article about how the\x01",
            "Support Section's restarted.\x02\x03",
            "#02109FIf you have a comment or photo\x01",
            "you want me to use, lay it on\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FHehe, then I think I'll\x01",
            "give you one of my host\x01",
            "club photos.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x101, 0x105, 500)
    Sleep(200)

    ChrTalk(
        0x101,
        (
            "#00006F...Please don't, I'm\x01",
            "begging you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13E, 3)
    Jump("loc_3067")

    label("loc_2FD7")


    ChrTalk(
        0xB,
        (
            "#02106FHah, but to think Reins\x01",
            "is out of the office on a\x01",
            "day like today.\x02\x03",
            "I was thinking of forcing\x01",
            "a lot of odd jobs onto\x01",
            "him... Too bad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3067")

    Jump("loc_3075")

    label("loc_306C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3075")

    label("loc_3075")

    TalkEnd(0xFE)
    Return()

    # Function_8_23BD end

    def Function_9_3079(): pass

    label("Function_9_3079")

    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0xB, 0x0, 0)
    TurnDirection(0xA, 0x0, 0)

    ChrTalk(
        0xB,
        (
            "#02101FAh, Lloyd and friends.\x01",
            "You saw the President's\x01",
            "address, didn't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FYes, thank you for\x01",
            "contacting us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FWhat will all of you do\x01",
            "now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02103FAt the very least, we'll\x01",
            "cover this.\x02\x03",
            "#02101FWe'll of course question the\x01",
            "State Guard again and try to\x01",
            "get something specific...\x02\x03",
            "And gather the voices of the\x01",
            "citizens who have left town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "All that's left is to\x01",
            "investigate the reaction of\x01",
            "the international media.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The international\x01",
            "communicator on 2F is in\x01",
            "full operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203FI see. You must be busy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02104FI guess. I think you guys have\x01",
            "things to do too, so let's\x01",
            "each do everything we can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, understood.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18F, 2)
    OP_93(0xB, 0x10E, 0x0)
    OP_93(0xA, 0x5A, 0x0)
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_9_3079 end

    def Function_10_334B(): pass

    label("Function_10_334B")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xB,
        (
            "#02109FHaha, Nielsen. We\x01",
            "finally meet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yes, I've been looking\x01",
            "forward to this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Come to think of it, I\x01",
            "asked the editor-in-\x01",
            "chief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "You've become bold in\x01",
            "these past three years,\x01",
            "Grace.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xB)

    ChrTalk(
        0xB,
        (
            "#02109FDon't say that. I still\x01",
            "have a long way to go,\x01",
            "after all.\x02\x03",
            "#02104FI always do what I want,\x01",
            "I guess... So I've only\x01",
            "done what I want to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Haha. You say that, but\x01",
            "the most important thing\x01",
            "is to enjoy the work.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_35B6")

    ChrTalk(
        0x101,
        (
            "#00000F(Grace... She's different\x01",
            "than she usually is in\x01",
            "front of Nielsen.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F(Haha, that's right. You\x01",
            "don't see this often.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36FE")

    label("loc_35B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 3)), scpexpr(EXPR_END)), "loc_3670")

    ChrTalk(
        0x101,
        (
            "#00000F(I feel like Grace is somehow\x01",
            "different from how she\x01",
            "usually is.)\x02\x03",
            "#00003F(It must be because of what\x01",
            "Nielsen said. It seems like\x01",
            "they know each other, but...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36FE")

    label("loc_3670")


    ChrTalk(
        0x101,
        (
            "#00000F(I feel like Grace is\x01",
            "somehow different from\x01",
            "how she usually is.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(Yes, I agree. I wonder\x01",
            "who's next to her,\x01",
            "though.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36FE")

    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x148, 1)
    Return()

    # Function_10_334B end

    def Function_11_370A(): pass

    label("Function_11_370A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3819")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3728")
    Call(0, 13)
    Jump("loc_3814")

    label("loc_3728")


    ChrTalk(
        0xFE,
        (
            "We're leaving coverage of the huge\x01",
            "tree to Grace. We plan to chase\x01",
            "after the actions of the government.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know what kind of organization we\x01",
            "can form before the major powers act,\x01",
            "but... This is a story I just can't miss.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3814")

    Jump("loc_41D3")

    label("loc_3819")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3827")
    Jump("loc_41D3")

    label("loc_3827")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_38A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3842")
    Call(0, 9)
    Jump("loc_389E")

    label("loc_3842")

    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xFE,
        "Yes, understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Grace asked us not to\x01",
            "dig into the State Guard\x01",
            "too much.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)

    label("loc_389E")

    Jump("loc_41D3")

    label("loc_38A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_38B1")
    Jump("loc_41D3")

    label("loc_38B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3947")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38D0")
    TalkEnd(0xFE)
    Call(0, 19)
    Return()

    label("loc_38D0")


    ChrTalk(
        0xFE,
        (
            "...I heard Red\x01",
            "Constellation aren't\x01",
            "your usual opponents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I told everyone going to\x01",
            "Mainz to be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41D3")

    label("loc_3947")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_39E7")

    ChrTalk(
        0xFE,
        (
            "I'm glad there's not too\x01",
            "much confusion regarding\x01",
            "the derailment for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish I could have\x01",
            "found the source of that\x01",
            "medicine, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41D3")

    label("loc_39E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_39F5")
    Jump("loc_41D3")

    label("loc_39F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3A8B")

    ChrTalk(
        0xFE,
        (
            "We've got an editing\x01",
            "meeting this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're fired up because\x01",
            "arguments have gotten heated\x01",
            "lately over all this big news.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41D3")

    label("loc_3A8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3A99")
    Jump("loc_41D3")

    label("loc_3A99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3AA7")
    Jump("loc_41D3")

    label("loc_3AA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3AB5")
    Jump("loc_41D3")

    label("loc_3AB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3AC3")
    Jump("loc_41D3")

    label("loc_3AC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3AD1")
    Jump("loc_41D3")

    label("loc_3AD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_41D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_415A")

    ChrTalk(
        0xFE,
        (
            "That man is a legend at our\x01",
            "company... Great men just look\x01",
            "different than the rest of us, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...No, what am I saying? I've\x01",
            "got to get these materials in\x01",
            "order and get back to my desk.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 500)
    Sleep(200)

    ChrTalk(
        0xFE,
        (
            "Ah, you're the Special\x01",
            "Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FYou're Reins if I\x01",
            "recall. We've worked\x01",
            "together in the past...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yes, I'm reporter Reins.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I say that, but lately\x01",
            "I've been getting\x01",
            "pigeonholed as a cameraman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*. They call\x01",
            "everyone around me\x01",
            "reporters! *grumble*...\x02",
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
            "#00106FT-There's various\x01",
            "things...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FThere's a gap between\x01",
            "ideals and reality, you\x01",
            "know.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EF5")

    ChrTalk(
        0x101,
        (
            "#00000FUmm, by the way, where's\x01",
            "Grace?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, well Grace just left\x01",
            "for her coverage today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Something about the\x01",
            "coverage being easier\x01",
            "with her alone...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And instead of that, she\x01",
            "forced a quantity of her\x01",
            "work onto me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, whether it's\x01",
            "helping or not, writing\x01",
            "is fun for a reporter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4027")

    label("loc_3EF5")


    ChrTalk(
        0x101,
        (
            "#00000FUmm, by the way, we already\x01",
            "met Grace today, but she's\x01",
            "not with you, is she?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, it was something\x01",
            "about the coverage being\x01",
            "easier with her alone...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And instead of that, she\x01",
            "forced a quantity of her\x01",
            "work onto me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, whether it's\x01",
            "helping or not, writing\x01",
            "is fun for a reporter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4027")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        (
            "Ah, while we were\x01",
            "talking here like this,\x01",
            "the deadline...!\x02",
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
        0x109,
        (
            "#10100FL-Looks like we're\x01",
            "interrupting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FUmm, do your best, ok?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    OP_93(0xFE, 0x0, 0x1F4)
    SetScenarioFlags(0x13E, 2)
    Return()

    label("loc_415A")


    ChrTalk(
        0xFE,
        (
            "Umm, now where were the\x01",
            "materials for that other\x01",
            "article?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ooh, while I was talking\x01",
            "like that, the\x01",
            "deadline...!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41D3")

    TalkEnd(0xFE)
    Return()

    # Function_11_370A end

    def Function_12_41D7(): pass

    label("Function_12_41D7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_42A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41F5")
    Call(0, 13)
    Jump("loc_42A1")

    label("loc_41F5")


    ChrTalk(
        0xFE,
        (
            "Anyway, right now, I've got to\x01",
            "use my legs and scrape together\x01",
            "as much info as I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just because I finished a\x01",
            "bit of work doesn't mean\x01",
            "I have time for a break.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42A1")

    Jump("loc_52D6")

    label("loc_42A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_43C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42C5")
    TalkEnd(0xFE)
    Call(0, 18)
    Return()

    label("loc_42C5")


    ChrTalk(
        0xFE,
        (
            "We're getting the bulletin\x01",
            "ready based on the info\x01",
            "Grace got for us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How pathetic. Under the current\x01",
            "structure, we can't even write an article\x01",
            "about the President's injustices.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And so, that's why I\x01",
            "believe in your\x01",
            "infiltration operation!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52D6")

    label("loc_43C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_45B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44F7")

    ChrTalk(
        0xFE,
        (
            "Hey, hey, hey! No matter how\x01",
            "you look at it, this\x01",
            "development is just too quick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honestly, it would be weird\x01",
            "if nothing happened... An\x01",
            "uproar can't be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, now that the situation's\x01",
            "like this, we have to do what we\x01",
            "can and be prepared for the worst.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_45B4")

    label("loc_44F7")


    ChrTalk(
        0xFE,
        (
            "Honestly, it would be weird\x01",
            "if nothing happened... An\x01",
            "uproar can't be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, now that the situation's\x01",
            "like this, we have to do what we\x01",
            "can and be prepared for the worst.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45B4")

    Jump("loc_52D6")

    label("loc_45B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_46B8")
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Rumor has it the attack the other day\x01",
            "was an Imperial plot. It's already\x01",
            "circulating amongst the citizens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although that is logical, jumping to\x01",
            "conclusions is dangerous... I wonder if\x01",
            "we can grab hold of the truth somehow.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    Jump("loc_52D6")

    label("loc_46B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_46C6")
    Jump("loc_52D6")

    label("loc_46C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_482D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_479D")

    ChrTalk(
        0xFE,
        (
            "It seems the CGF are in\x01",
            "a tough spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of that, I wonder if the\x01",
            "Imperial army will intervene if\x01",
            "this continues for too long...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man oh man. That's no\x01",
            "laughing matter.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4828")

    label("loc_479D")


    ChrTalk(
        0xFE,
        (
            "If the occupation continues for\x01",
            "too long, I wonder if the\x01",
            "Imperial army will intervene...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man oh man. That's no\x01",
            "laughing matter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4828")

    Jump("loc_52D6")

    label("loc_482D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4980")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4904")

    ChrTalk(
        0xFE,
        (
            "*sigh*. Editing these\x01",
            "bulletins really drains my\x01",
            "stamina every single time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It wouldn't be a problem\x01",
            "if I was 20, but lately\x01",
            "I really feel it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, I don't want to get\x01",
            "old.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_497B")

    label("loc_4904")


    ChrTalk(
        0xFE,
        (
            "Though I say that, I'm\x01",
            "actually 30. I'm in the\x01",
            "prime of my life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't want to say\x01",
            "nothing but complaints.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_497B")

    Jump("loc_52D6")

    label("loc_4980")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_498E")
    Jump("loc_52D6")

    label("loc_498E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4AD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AA9")

    ChrTalk(
        0xFE,
        "Super.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now then, I think I'll look\x01",
            "over the materials for this\x01",
            "meeting once again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that state\x01",
            "independence is at the center\x01",
            "of today's discussions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I don't get this material\x01",
            "in my head beforehand, I'll\x01",
            "run out of arguments.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4AD0")

    label("loc_4AA9")


    ChrTalk(
        0xFE,
        (
            "Now then, materials,\x01",
            "materials...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AD0")

    Jump("loc_52D6")

    label("loc_4AD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4CE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C56")

    ChrTalk(
        0xFE,
        (
            "From social problems including politics\x01",
            "and economics to amusement information\x01",
            "about culture and the performing arts...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The cases our reporters carry\x01",
            "have an amount of variety you\x01",
            "would not believe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we were a bigger news\x01",
            "agency we could\x01",
            "specialize, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm one of a select few who\x01",
            "are mobile. I can cover\x01",
            "basically anything myself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4CE2")

    label("loc_4C56")


    ChrTalk(
        0xFE,
        (
            "Three incidents have come\x01",
            "in just this afternoon...\x01",
            "My column is left too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, while I'm free,\x01",
            "might as well take care\x01",
            "of them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CE2")

    Jump("loc_52D6")

    label("loc_4CE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4E70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DE6")

    ChrTalk(
        0xFE,
        (
            "The number of reporters from\x01",
            "each company covering the\x01",
            "main session is limited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We sent in Grace and\x01",
            "Reins.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The rest of us here are waiting for\x01",
            "info from Grace and Reins and getting\x01",
            "ready to publish the bulletin.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4E6B")

    label("loc_4DE6")


    ChrTalk(
        0xFE,
        (
            "The Grace and Reins team\x01",
            "have a reputation for\x01",
            "excellent coverage, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, since it's them,\x01",
            "I'm sure it'll go well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E6B")

    Jump("loc_52D6")

    label("loc_4E70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4FC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F2E")

    ChrTalk(
        0xFE,
        (
            "I just had the photos\x01",
            "Grace and Reins took\x01",
            "developed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Look at this. Isn't it\x01",
            "well taken?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now then, which photo\x01",
            "should I use in the\x01",
            "extra edition...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4FBD")

    label("loc_4F2E")


    ChrTalk(
        0xFE,
        (
            "This one and that one,\x01",
            "and maybe that one on\x01",
            "the right would be good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I push him, maybe the\x01",
            "editor-in-chief will\x01",
            "check it for me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FBD")

    Jump("loc_52D6")

    label("loc_4FC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5181")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50AF")

    ChrTalk(
        0xFE,
        (
            "Heh, for as much as it\x01",
            "Heiyue acted, it ended up\x01",
            "going to Crimson & Co., huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From the start, we never\x01",
            "did get to the bottom of\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well for now, all we can\x01",
            "do is remain silent and\x01",
            "wait and see.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_517C")

    label("loc_50AF")


    ChrTalk(
        0xFE,
        (
            "Even though the trade\x01",
            "conference finally starts\x01",
            "tomorrow... Something's up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, just thinking about it won't solve\x01",
            "anything. Anyway, I've got to get the\x01",
            "trade conference-related news in order.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_517C")

    Jump("loc_52D6")

    label("loc_5181")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_525B")

    ChrTalk(
        0xFE,
        (
            "Amazing... So Heiyue is\x01",
            "after Revache's\x01",
            "property, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, the situation being\x01",
            "what it is, the Empire won't\x01",
            "stay silent for long...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man oh man... It just\x01",
            "gets more and more\x01",
            "suspicious.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52D6")

    label("loc_525B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_52D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5276")
    Call(0, 15)
    Jump("loc_52D6")

    label("loc_5276")


    ChrTalk(
        0xFE,
        (
            "Oh, thanks for the\x01",
            "trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is baumkuchen, huh.\x01",
            "Haha, you always like\x01",
            "them, huh.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52D6")

    TalkEnd(0xFE)
    Return()

    # Function_12_41D7 end

    def Function_13_52DA(): pass

    label("Function_13_52DA")

    OP_4B(0xA, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x9,
        (
            "Hey Reins. Your camera\x01",
            "ready?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Yes, you bet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Alright then. Let's head\x01",
            "to the Orchis Tower area\x01",
            "for coverage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Let's do our best, so as\x01",
            "to not lose to Grace!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Yes, roger that!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 3)), scpexpr(EXPR_END)), "loc_5454")

    ChrTalk(
        0x101,
        (
            "#00000F(Reins has resumed work\x01",
            "as a reporter, huh.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F(I don't know if I should call\x01",
            "it two birds with one stone...\x01",
            "or a man with amazing vitality.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5454")

    OP_4C(0xA, 0xFF)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 3)
    Return()

    # Function_13_52DA end

    def Function_14_546A(): pass

    label("Function_14_546A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_547B")
    Jump("loc_561E")

    label("loc_547B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5489")
    Jump("loc_561E")

    label("loc_5489")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5497")
    Jump("loc_561E")

    label("loc_5497")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_54A5")
    Jump("loc_561E")

    label("loc_54A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_54B3")
    Jump("loc_561E")

    label("loc_54B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_54C1")
    Jump("loc_561E")

    label("loc_54C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_54CF")
    Jump("loc_561E")

    label("loc_54CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_54DD")
    Jump("loc_561E")

    label("loc_54DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_54EB")
    Jump("loc_561E")

    label("loc_54EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5584")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5506")
    Call(0, 10)
    Jump("loc_557F")

    label("loc_5506")


    ChrTalk(
        0xFE,
        (
            "Haha, that's Grace for\x01",
            "you. She's already\x01",
            "looked into it, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I swear... One bite, and\x01",
            "your cheeks will melt.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_557F")

    Jump("loc_561E")

    label("loc_5584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5592")
    Jump("loc_561E")

    label("loc_5592")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_561E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55AD")
    Call(0, 15)
    Jump("loc_561E")

    label("loc_55AD")


    ChrTalk(
        0xFE,
        (
            "Oh right, I'm giving you\x01",
            "all a souvenir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I found a good shop in\x01",
            "the Republic. Haha,\x01",
            "don't you like it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_561E")

    TalkEnd(0xFE)
    Return()

    # Function_14_546A end

    def Function_15_5622(): pass

    label("Function_15_5622")

    OP_4B(0xC, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x9,
        (
            "Ah, it's certainly been\x01",
            "a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Is been what, three\x01",
            "years since you were\x01",
            "last here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Yes, just about.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "For the time being, I'll be\x01",
            "dropping in every now and\x01",
            "then as a special consultant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I may be trouble, but I\x01",
            "look forward to working\x01",
            "with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Oh, don't mention it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you ever need\x01",
            "anything, don't hesitate\x01",
            "to ask.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x0, 3)
    Return()

    # Function_15_5622 end

    def Function_16_5798(): pass

    label("Function_16_5798")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_57A9")
    Jump("loc_59F9")

    label("loc_57A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_585C")
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Well, for now, we can't\x01",
            "write this up as an\x01",
            "Imperial attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What will the Empire do next\x01",
            "in this situation...? We can\x01",
            "only keep our eyes on them.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    Jump("loc_59F9")

    label("loc_585C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_586A")
    Jump("loc_59F9")

    label("loc_586A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5878")
    Jump("loc_59F9")

    label("loc_5878")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_58FB")

    ChrTalk(
        0xFE,
        (
            "Now then, it looks like the\x01",
            "editorial department's going\x01",
            "to get busy very soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to get home\x01",
            "soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59F9")

    label("loc_58FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5996")

    ChrTalk(
        0xFE,
        (
            "Looks like they're\x01",
            "working on the bulletin\x01",
            "on 2F.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How to say this... This\x01",
            "noise is the same no matter\x01",
            "which news agency you go to.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59F9")

    label("loc_5996")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_59A7")
    Call(0, 6)
    Jump("loc_59F9")

    label("loc_59A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_59B5")
    Jump("loc_59F9")

    label("loc_59B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_59C3")
    Jump("loc_59F9")

    label("loc_59C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_59D4")
    Call(0, 7)
    Jump("loc_59F9")

    label("loc_59D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_59E2")
    Jump("loc_59F9")

    label("loc_59E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_59F0")
    Jump("loc_59F9")

    label("loc_59F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_59F9")

    label("loc_59F9")

    TalkEnd(0xFE)
    Return()

    # Function_16_5798 end

    def Function_17_59FD(): pass

    label("Function_17_59FD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5BF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B15")

    ChrTalk(
        0xFE,
        (
            "McCunnen and I hurried to finish\x01",
            "and publish this bulletin about\x01",
            "the President's arrest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, the other\x01",
            "reporters resumed their\x01",
            "coverage immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We were able to get in touch\x01",
            "with Grace, and new info is\x01",
            "flowing in steadily.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5BEB")

    label("loc_5B15")


    ChrTalk(
        0xFE,
        (
            "We were able to get in touch\x01",
            "with Grace, and new info is\x01",
            "flowing in steadily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To hold back the agitation and confusion\x01",
            "of the citizens, we're working as fast as\x01",
            "we can to bring them accurate information.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BEB")

    Jump("loc_5CA4")

    label("loc_5BF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5CA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C0F")
    TalkEnd(0xFE)
    Call(0, 18)
    Return()

    label("loc_5C0F")


    ChrTalk(
        0xFE,
        (
            "I'd like to thank all of\x01",
            "you for helping Grace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Be careful as you proceed... And\x01",
            "please, let us write an article\x01",
            "about your great efforts.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CA4")

    TalkEnd(0xFE)
    Return()

    # Function_17_59FD end

    def Function_18_5CA8(): pass

    label("Function_18_5CA8")

    TalkBegin(0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0x8, 0xFF)
    TurnDirection(0x9, 0x0, 0)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5D52")
    Jump("loc_5D9C")

    label("loc_5D52")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5D72")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5D9C")

    label("loc_5D72")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5D92")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5D9C")

    label("loc_5D92")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5D9C")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    ChrTalk(
        0x9,
        (
            "Oh, the Special Support\x01",
            "Section, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Everyone, you're safe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Hmm. I won't say it too loudly,\x01",
            "but we heard about your situation\x01",
            "and efforts from Grace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Do you mind if we have a\x01",
            "little information exchange\x01",
            "regarding the situation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, we'd love to.\x02",
    )

    CloseMessageWindow()
    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(61910, 1500, -2140, 0)
    MoveCamera(59, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21850, 0)
    SetChrPos(0x101, 62030, 0, -2100, 90)
    SetChrPos(0x102, 61830, 0, -1090, 90)
    SetChrPos(0x103, 61480, 0, -3030, 90)
    SetChrPos(0x104, 60040, 0, -1980, 90)
    SetChrPos(0xF4, 59440, 0, -990, 90)
    SetChrPos(0xF5, 59440, 0, -2990, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0xE, 0x9)
    ClearChrBattleFlags(0xE, 0x4)
    SetChrSubChip(0xE, 0x0)
    SetChrPos(0xE, 64370, 0, -1800, 270)
    SetChrPos(0x9, 63780, 0, -800, 270)
    SetChrPos(0x8, 64349, 0, -2890, 270)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xE,
        (
            "I see... So you're\x01",
            "planning on taking\x01",
            "Orchis Tower, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "And if you succeed, the\x01",
            "current authoritarian\x01",
            "system will end, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Man, just when I thought we'd be able to move around\x01",
            "a little easier because of that invalidity\x01",
            "declaration, this martial law order was handed down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "And ever since that weird\x01",
            "mist appeared, it's been very\x01",
            "hard to open comm channels.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FI see, so even normal\x01",
            "orbal communications are\x01",
            "affected...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FMost likely, that mist\x01",
            "is generating some kind\x01",
            "of jamming waves...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FHmm. If we don't do something\x01",
            "about it, the chaos in the\x01",
            "city will only grow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FYeah... That's right.\x02\x03",
            "#00000FBy the way, is everyone\x01",
            "here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Right. The other staff\x01",
            "got tied up at their\x01",
            "destinations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Even so, we were lucky to\x01",
            "be able to contact almost\x01",
            "all of them, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Reins is the only one we\x01",
            "haven't been able to\x01",
            "contact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "We have no idea at all\x01",
            "where or how he is at\x01",
            "present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FReins, huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Well, I'm sure he must\x01",
            "be somewhere in the\x01",
            "city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I hope he didn't take\x01",
            "after Grace and do\x01",
            "something reckless, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "It's just, he's pretty\x01",
            "used to danger. I'm not\x01",
            "that worried about him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "That's about all for us.\x01",
            "I won't waste any more\x01",
            "of your valuable time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "For now, we'll be here preparing\x01",
            "to report on all this, while\x01",
            "praying for your success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Your plan must succeed. This\x01",
            "rigid order must be crushed,\x01",
            "rightly or wrongly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYeah, got it!\x02\x03",
            "#00003F(So Reins is out of\x01",
            "contact, huh...)\x02\x03",
            "#00001F(Grace is probably worried\x01",
            "about his safety too.\x01",
            "Let's keep this in mind.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrPos(0x0, -6570, 20, 2860, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1BF, 0)
    EventEnd(0x5)
    Return()

    # Function_18_5CA8 end

    def Function_19_665A(): pass

    label("Function_19_665A")

    EventBegin(0x0)
    Fade(500)
    OP_68(4720, 1500, 56190, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19720, 0)
    SetChrPos(0x101, 4520, 0, 56690, 90)
    SetChrPos(0x102, 4500, 0, 55000, 45)
    SetChrPos(0x103, 3360, 0, 56510, 90)
    SetChrPos(0x109, 4950, 0, 58190, 135)
    SetChrPos(0x105, 3550, 0, 57990, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_93(0xB, 0x10E, 0x0)
    OP_93(0xA, 0x10E, 0x0)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "Everyone from the\x01",
            "Support Section...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02101FYou guys must have it\x01",
            "tough.\x02\x03",
            "#02105FThat's right, Randy is―\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#02101FWhat's up with Randy?\x01",
            "Could it be―\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00003F......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108F...That's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FSorry. That's a story\x01",
            "for another time―\x02\x03",
            "#00003F―Let's go, everyone.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)
    OP_93(0x102, 0x0, 0x1F4)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#02101FHey, wait! Lloyd!\x02\x03",
            "#02104FI've no intention of\x01",
            "following you. How about\x01",
            "a "discussion"?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00005FHuh...\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    OP_93(0x102, 0x2D, 0x1F4)

    ChrTalk(
        0x109,
        (
            "#6P#10105FUmm, what do you mean\x01",
            "by...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02101FFirst a condition... I know a certain\x01",
            "amount about Randy's background.\x02\x03",
            "#02103FI'll just say this. It's not like I have\x01",
            "any doubt about what I'm saying.\x02\x03",
            "#02100FBut at the same time, I've seen many of\x01",
            "his actions as a member of the Support\x01",
            "Section. You can be sure I believe in him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FGrace...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02103FAnd by your reactions, I\x01",
            "can guess the situation.\x02\x03",
            "#02101FRandy headed to Mainz\x01",
            "alone, right?\x02\x03",
            "To resolve this\x01",
            "incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001F...You know that much,\x01",
            "huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203F...That's a Crossbell\x01",
            "Times reporter for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02102FHaha, I knew it. Bullseye,\x01",
            "huh.\x02\x03",
            "#02103FAnd you guys are going to\x01",
            "bring him back...\x02\x03",
            "#02101FI feel like you're not going\x01",
            "to listen but, your minds\x01",
            "are made up, aren't they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FOf course! Randy's our\x01",
            "friend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00101FYes, exactly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02104FI see. Then this really\x01",
            "wasn't a discussion, huh.\x02\x03",
            "#02101FThen I too will call out\x01",
            "to you with my very own\x01",
            "voice.\x02\x03",
            "#02104F―Be careful out there!\x02\x03",
            "#02109FAnd once again, allow me\x01",
            "to write an article about\x01",
            "your great efforts!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FWe will. Thank you very\x01",
            "much.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_93(0xB, 0xB4, 0x0)
    OP_93(0xA, 0x0, 0x0)
    SetChrPos(0x0, 4720, 0, 56190, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x171, 3)
    EventEnd(0x5)
    Return()

    # Function_19_665A end

    def Function_20_6DBC(): pass

    label("Function_20_6DBC")

    EventBegin(0x0)
    Fade(500)
    OP_68(3050, 1520, -1840, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20950, 0)
    SetChrPos(0x101, 2700, 20, -1900, 90)
    SetChrPos(0x102, 2700, 20, -800, 90)
    SetChrPos(0x103, 1500, 20, -1900, 90)
    SetChrPos(0x109, 1500, 20, -800, 90)
    SetChrPos(0x105, 300, 20, -1900, 90)
    SetChrPos(0x104, 300, 20, -800, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F9E")

    ChrTalk(
        0x8,
        (
            "Welcome to Crossbell\x01",
            "News Agency.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Oh, you all are the\x01",
            "Special Support\x01",
            "Section...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHello, we're here about\x01",
            "your support request.\x02\x03",
            "You needed help with\x01",
            "coverage for your\x01",
            "gourmet guide...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Haha, thanks for coming.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Can you start right\x01",
            "away?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x17D, 0)
    Jump("loc_6FEB")

    label("loc_6F9E")


    ChrTalk(
        0x8,
        "Thank you for coming.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's sudden, but can you\x01",
            "accept the request?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FEB")

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
            "Accept\x01",      # 0
            "Cancel\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70EE")

    ChrTalk(
        0x101,
        "#00000FYes. Allow us to accept.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then, to hear the request details\x01",
            "from the person in charge, please\x01",
            "wait on the second floor.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 21)
    Jump("loc_71D3")

    label("loc_70EE")


    ChrTalk(
        0x101,
        (
            "#00006FSorry, we have other\x01",
            "business to attend to\x01",
            "right now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ah, is that so... I'll\x01",
            "be waiting, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you'd like to accept\x01",
            "the request, please return\x01",
            "as soon as you can.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 2700, 20, -2000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)

    label("loc_71D3")

    Return()

    # Function_20_6DBC end

    def Function_21_71D4(): pass

    label("Function_21_71D4")

    OP_4B(0xB, 0xFF)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x2)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 60010, 150, 10690, 270)
    OP_68(57490, 1500, 11620, 0)
    MoveCamera(76, 28, -1, 0)
    OP_6E(400, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 58200, 0, 11760, 135)
    SetChrPos(0x102, 58650, 0, 12660, 135)
    SetChrPos(0x103, 57000, 0, 11920, 135)
    SetChrPos(0x109, 57480, 0, 13060, 135)
    SetChrPos(0x104, 55980, 0, 12490, 135)
    SetChrPos(0x105, 55580, 0, 11290, 90)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xB,
        (
            "#02100FHello, hello!♪ My\x01",
            "Special Support Section\x01",
            "friends.\x02\x03",
            "#02109FSorry to keep you\x01",
            "waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FI knew it... You're in\x01",
            "charge of this request,\x01",
            "Grace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FThere was a certain\x01",
            "probability this would\x01",
            "happen.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_747E")

    ChrTalk(
        0xB,
        (
            "#02103FOh, such a weak\x01",
            "reaction!\x02\x03",
            "#02100FWe get to work together\x01",
            "again! Can't you be a\x01",
            "little happier?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FAhaha... Last time you had us\x01",
            "going back and forth across\x01",
            "all of Crossbell, though.\x02\x03",
            "#00105FAnd, what do you need this\x01",
            "time?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_755D")

    label("loc_747E")


    ChrTalk(
        0xB,
        (
            "#02103FOh, such a weak\x01",
            "reaction!\x02\x03",
            "#02100FWe get to work together!\x01",
            "Be a little happier!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FA-Ahaha... It feels like\x01",
            "things are always tougher\x01",
            "when you're around, Grace.\x02\x03",
            "#00105FAnd, what do you need this\x01",
            "time?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_755D")


    ChrTalk(
        0x105,
        (
            "#10300FSomething about helping\x01",
            "with coverage for a gourmet\x01",
            "guide, I think it was.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)

    ChrTalk(
        0xB,
        (
            "#02100FYes, exactly.\x02\x03",
            "#02104FA while back, saying "We want to follow the\x01",
            "example of Mayor Dieter's energy", I got a\x01",
            "suggestion from the Crossbell Trade Association.\x02\x03",
            "#02102FThey wanted to cooperate with Crossbell News and\x01",
            "make a gourmet guide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FCooperate with the Trade\x01",
            "Association? What specifically\x01",
            "do they want you to do?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x2)

    ChrTalk(
        0xB,
        (
            "#02104FBasically, they want to\x01",
            "introduce the restaurants\x01",
            "of Crossbell State...\x02\x03",
            "#02100FIn addition to coverage,\x01",
            "they're going to offer\x01",
            "discount service.\x02\x03",
            "#02109FThey've got various\x01",
            "interesting plans like\x01",
            "that in progress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI see... That's\x01",
            "unprecedented.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02109F─Ok! Now let's get to the\x01",
            "point...\x02\x03",
            "#02100FPart of the plan is for\x01",
            ""Individual Gourmet\x01",
            "Recommendations".\x02\x03",
            "#02104FIBC's Mariabell, or Arc-en-\x01",
            "Ciel's Ilya, Theodore and\x01",
            "Eugene...\x02\x03",
            "#02102FWe want to introduce people\x01",
            "to these Crossbell\x01",
            "celebrities' favorite dishes.\x02\x03",
            "#02109FAnd that's where you guys\x01",
            "come in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FHmm... So that's the\x01",
            "request this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FThat does seem\x01",
            "interesting, but...\x02\x03",
            "#00105FIs it really ok to put\x01",
            "us in a lineup like\x01",
            "that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FI know, right? I'm happy to\x01",
            "stand shoulder-to-shoulder\x01",
            "with Ilya or Mariabell, but...\x02\x03",
            "#00301FIf we're in your article, I\x01",
            "don't think it'd catch much\x01",
            "attention.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHaha, is that a nice way\x01",
            "of saying we're\x01",
            "spoilers?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#02105FNo, no. Nothing of the\x01",
            "sort!\x02\x03",
            "#02102FLately, you guys have\x01",
            "gotten more honest-to-\x01",
            "goodness fans, you know?\x02\x03",
            "#02109FSo much that I want to\x01",
            "request your private\x01",
            "photos.㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00106FG-Give us a break.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02100FHaha. Anyway, you guys are\x01",
            "attracting attention in your own\x01",
            "way.\x02\x03",
            "#02104FIf it wasn't the case, then I'd\x01",
            "never have asked for your help with\x01",
            "this request in the first place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FAlright, I think I get\x01",
            "it.\x02\x03",
            "#00000FSo, how should we\x01",
            "proceed with this,\x01",
            "specifically?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02102FUhuhu. Let me explain how to\x01",
            "do your coverage.\x02\x03",
            "#02104FFirst, you need to go to each\x01",
            "restaurant or cart and\x01",
            "actually eat their food.\x02\x03",
            "#02109FAnd among each of them, I want\x01",
            "you to find a dish that makes\x01",
            "you think "This is it!".\x02\x03",
            "#02102FAfter that, I'll have you\x01",
            "write your own article here at\x01",
            "Crossbell News.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FSo we've got to go to restaurants\x01",
            "throughout the state and find\x01",
            "dishes that each of us like.\x02\x03",
            "#10105FBut, what if we can't find\x01",
            "anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02102FCrossbell is a big place. I'm\x01",
            "sure each of you will find at\x01",
            "least one dish you like.\x02\x03",
            "#02104FIf you really can't, then I'll\x01",
            "just have you write about the\x01",
            "restaurants you visited.\x02\x03",
            "#2100FBut ideally, I'd like each of\x01",
            "you to introduce readers to\x01",
            "your favorite dish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FHmm, so we've got to go\x01",
            "to at least six\x01",
            "different places, huh.\x02\x03",
            "#00300FAnything we should watch\x01",
            "out for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02103FHmm, let me think...\x02\x03",
            "#02105FOh, the bar at Michelam\x01",
            "is off limits.\x02\x03",
            "#02102FI'd like you to cover\x01",
            "areas other than that\x01",
            "one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FHmm, then Trinity in\x01",
            "Downtown is off limits too.\x02\x03",
            "#10300FHaha. And it was such a good\x01",
            "chance to get more business.\x01",
            "Abbas will be sad.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)

    ChrTalk(
        0xB,
        (
            "#02109FSorry, Wazy! I'll handle covering that\x01",
            "area.\x02\x03",
            "#02104F...Oh, and I've already spoken with all\x01",
            "the restaurants, so there's no need to\x01",
            "worry about paying for your food.\x02\x03",
            "#02102FIf you explain the situation, they'll\x01",
            "show you their sampler menu.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FAnyway, we'll be fine if\x01",
            "we just visit six\x01",
            "stores, bars excepted.\x02\x03",
            "#00103FWe'll need to persevere\x01",
            "if we're going to find\x01",
            "dishes each of us like.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x2)

    ChrTalk(
        0xB,
        (
            "#02104FHaha. This isn't a rush job, but\x01",
            "please do your best on it.\x02\x03",
            "#02100FOnce you're finished, come\x01",
            "report to me here at Crossbell\x01",
            "News.\x02\x03",
            "#02109FIf I'm not here for some reason,\x01",
            "just ask Tria, our receptionist.\x01",
            "She'll contact me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FUnderstood. Let's get\x01",
            "started then.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Gourmet Guide\x01",
            "Coverage Support]\x07\x00\x01",
            "started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x0, 6)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0x0, -6370, 250, 2630, 180)
    OP_69(0xFF, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x172, 0)
    OP_29(0x80, 0x1, 0x0)
    EventEnd(0x5)
    Return()

    # Function_21_71D4 end

    def Function_22_856B(): pass

    label("Function_22_856B")

    EventBegin(0x0)
    Fade(500)
    OP_68(3050, 1520, -1840, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20950, 0)
    SetChrPos(0x101, 2700, 20, -1900, 90)
    SetChrPos(0x102, 2700, 20, -800, 90)
    SetChrPos(0x103, 1500, 20, -1900, 90)
    SetChrPos(0x109, 1500, 20, -800, 90)
    SetChrPos(0x105, 300, 20, -1900, 90)
    SetChrPos(0x104, 300, 20, -800, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    ChrTalk(
        0x8,
        "Good work, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It looks like you've gone\x01",
            "to six different places for\x01",
            "the gourmet guide coverage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Are you ready to report\x01",
            "to Grace?\x02",
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
            "Not yet\x01",              # 0
            "Report to Grace\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8779")

    ChrTalk(
        0x8,
        "Understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'll call Grace for you.\x01",
            "Please wait for her on\x01",
            "the 2nd floor.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jump("loc_87F4")

    label("loc_8779")


    ChrTalk(
        0x8,
        "Oh, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In that case, please\x01",
            "come again when you're\x01",
            "ready to report.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 2700, 20, -2000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    label("loc_87F4")

    Return()

    # Function_22_856B end

    def Function_23_87F5(): pass

    label("Function_23_87F5")

    OP_4B(0xB, 0xFF)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x2)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 60010, 150, 10690, 270)
    OP_68(57490, 1500, 11620, 0)
    MoveCamera(76, 28, -1, 0)
    OP_6E(400, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 58200, 0, 11760, 135)
    SetChrPos(0x102, 58650, 0, 12660, 135)
    SetChrPos(0x103, 57000, 0, 11920, 135)
    SetChrPos(0x109, 57480, 0, 13060, 135)
    SetChrPos(0x104, 55980, 0, 12490, 135)
    SetChrPos(0x105, 55580, 0, 11290, 90)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xB,
        (
            "#02109FHiya. Nice work㈱\x02\x03",
            "#02102FHow did collecting your\x01",
            ""gourmet\x01",
            "recommendations" go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, well... We had a\x01",
            "lot of fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FI'm tired though. All\x01",
            "those places are so far\x01",
            "apart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02100FHaha, well I'm glad you\x01",
            "had your fill of\x01",
            "delicious food.\x02\x03",
            "#02109FAlright then, show me\x01",
            "what you've got.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, well...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and the others told\x01",
            "Grace about the\x01",
            "establishments they visited.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_8A83")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8A83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_8A96")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8A96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_8AA9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8AA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_8ABC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8ABC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_8ACF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8ACF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_8AE2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8AE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_8AF5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8AF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_8B08")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_8B1B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_8B2E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_8B41")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B41")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C21")

    ChrTalk(
        0xB,
        (
            "#02104FHmm, so you went to\x01",
            "eleven places in all,\x01",
            "did you.\x02\x03",
            "#02109FThis looks like very\x01",
            "thorough coverage! Haha,\x01",
            "I'm so happy!\x02\x03",
            "#02102FThen next... Among them,\x01",
            "tell me your "gourmet\x01",
            "recommendations"!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9041")

    label("loc_8C21")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CE8")

    ChrTalk(
        0xB,
        (
            "#02104FHmm, so you went to ten\x01",
            "places in all, did you.\x02\x03",
            "#02102FHaha, this looks like\x01",
            "solid coverage.\x02\x03",
            "#02100FThen next... Among them,\x01",
            "tell me your "gourmet\x01",
            "recommendations"!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9041")

    label("loc_8CE8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DC1")

    ChrTalk(
        0xB,
        (
            "#02104FHmm, so you went to nine\x01",
            "places in all, did you.\x02\x03",
            "#02102FHaha, looks like this'll\x01",
            "be some nice coverage\x01",
            "for me.\x02\x03",
            "#02100FThen next... Among them,\x01",
            "tell me your "gourmet\x01",
            "recommendations"!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9041")

    label("loc_8DC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E9B")

    ChrTalk(
        0xB,
        (
            "#02104FHmm, so you went to\x01",
            "eight places in all, did\x01",
            "you.\x02\x03",
            "#02102FHaha, looks like this'll\x01",
            "be some nice coverage\x01",
            "for me.\x02\x03",
            "#02100FThen next... Among them,\x01",
            "tell me your "gourmet\x01",
            "recommendations"!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9041")

    label("loc_8E9B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F75")

    ChrTalk(
        0xB,
        (
            "#02104FHmm, so you went to\x01",
            "seven places in all, did\x01",
            "you.\x02\x03",
            "#02102FHaha, looks like this'll\x01",
            "be some nice coverage\x01",
            "for me.\x02\x03",
            "#02100FThen next... Among them,\x01",
            "tell me your "gourmet\x01",
            "recommendations"!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9041")

    label("loc_8F75")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9041")

    ChrTalk(
        0xB,
        (
            "#02104FHehe, you went to all\x01",
            "six places for me.\x02\x03",
            "#02102FHaha, looks like this'll\x01",
            "be some nice coverage\x01",
            "for me.\x02\x03",
            "#02100FThen next... Among them,\x01",
            "tell me your "gourmet\x01",
            "recommendations"!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9041")

    Fade(500)
    OP_68(58050, 1900, 10380, 0)
    MoveCamera(12, 26, -1, 0)
    OP_6E(400, 0)
    SetCameraDistance(17470, 0)
    OP_0D()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_9188")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000FMine was the "Chef Omelet\x01",
            "Rice" from Ash Tree Inn in\x01",
            "Armorica Village.\x02\x03",
            "#00002FThe simple flavor\x01",
            "characteristic of Armorica\x01",
            "touched on my heartstrings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02102FI see. That omelet rice\x01",
            "is indeed something you\x01",
            "can only taste there!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9188")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_929B")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x102,
        (
            "#00104FMine was "Three-Day Stew"\x01",
            "from the Le Rekuche buffet\x01",
            "at St. Ursula Hospital.\x02\x03",
            "#00109FIt's oily due to being\x01",
            "cooked for a long time, and\x01",
            "good for you on top of that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02109FYes, yes! Eating that\x01",
            "stew will recover your\x01",
            "energy in an instant!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_929B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_93F6")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x103,
        (
            "#00204FI recommend "Shaved Ice <Seven Colors>"\x01",
            "from the ice cream stand in Entertainment\x01",
            "District.\x02\x03",
            "#00202FIt has an interesting mouthfeel, and the\x01",
            "taste of its seven colors... It's a\x01",
            "masterpiece that defies simple explanation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02105FOh, that's high praise coming\x01",
            "from you, Tio! I'm sure it\x01",
            "will be very popular now!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_93F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_9520")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x104,
        (
            "#00300FFor me it's the "Heavenly Noodles\x01",
            "<Sun>" at the Waterfront Area noodle\x01",
            "stand.\x02\x03",
            "#00309FThe combination of firm, curly noodles\x01",
            "and salty soup... Just remembering its\x01",
            "flavor makes me drool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02104FYes, I see. I often go\x01",
            "there for lunch. That's\x01",
            "a total masterpiece!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9520")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_961E")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x109,
        (
            "#10107FMine is the "Peerless\x01",
            "Fried Rice" from The Old\x01",
            "Dragon on East Street.\x02\x03",
            "#10104FOnce I tasted its simple\x01",
            "yet deep flavor, I\x01",
            "couldn't get enough!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02109FThat's Zanghui's\x01",
            "specialty! Hmm, I think I\x01",
            "want to eat there again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_961E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_9757")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x105,
        (
            "#10304FMy recommendation is the "Rich\x01",
            "Sea Hot Pot" from the Tangram\x01",
            "Gate cafeteria.\x02\x03",
            "#10302FIt tastes good and everyone\x01",
            "can enjoy it together. I can't\x01",
            "think of anything better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02102FThe border gate cafeterias are\x01",
            "hidden gourmet spots indeed! Haha,\x01",
            "you really know your stuff, Wazy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9757")


    ChrTalk(
        0x101,
        "#00004F...So, that's about it.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9944")
    OP_2C(0x80, 0x2)
    OP_63(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#02102FYeah. It looks like each of\x01",
            "your members found a "gourmet\x01",
            "recommendation" for me.\x02\x03",
            "#02104FThis will improve the gourmet\x01",
            "guide feature page a lot.\x02\x03",
            "#02109FThanks you guys!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha, we should be\x01",
            "thanking you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FIt was worth it going to\x01",
            "all those places, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02105FWhoops, your work's not\x01",
            "yet done.\x02\x03",
            "#02102FI've got to have each of\x01",
            "you write up an\x01",
            "introduction comment!\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x80, 0x1, 0xF)
    Jump("loc_9CAF")

    label("loc_9944")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9B17")
    OP_2C(0x80, 0x1)

    ChrTalk(
        0xB,
        (
            "#02106FHmm. As expected, not all\x01",
            "of you found a "gourmet\x01",
            "recommendation", huh.\x02\x03",
            "#02102FBut well, I guess you\x01",
            "pass. I'll thank you for\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FT-Thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F(Maybe we should have\x01",
            "tried a little\x01",
            "harder...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02104FBut, those of you who didn't find\x01",
            "a favorite must've found at least\x01",
            "a number two or three, right?\x02\x03",
            "#02102FTo make up for the lack of\x01",
            "content, I'll have you write\x01",
            "introduction comments!\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x80, 0x1, 0x10)
    Jump("loc_9CAF")

    label("loc_9B17")

    OP_63(0xB, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#02105FH-Huh? These are all the\x01",
            ""gourmet recommendations"\x01",
            "you found?\x02\x03",
            "#02106FHmm, I guess it can't be\x01",
            "helped... I wonder if\x01",
            "this was a mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FW-We're sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F(Maybe we could have\x01",
            "done a bit more...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02103FWell, it can't be helped.\x01",
            "You did the minimum.\x02\x03",
            "#02100FTo make up for the lack of\x01",
            "content, I'll have you write\x01",
            "introduction comments!\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x80, 0x1, 0x11)

    label("loc_9CAF")

    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "After that, Lloyd and the others had\x01",
            "difficulty with the writing because\x01",
            "they weren't accustomed to it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Somehow, the "Gourmet\x01",
            "Recommendations" article for the\x01",
            "gourmet guide was completed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(57490, 1500, 11620, 0)
    MoveCamera(76, 28, -1, 0)
    OP_6E(400, 0)
    SetCameraDistance(19000, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0xB,
        (
            "#02100FHmm, I think that should do\x01",
            "it.\x02\x03",
            "#02104FWe'll proof this ourselves\x01",
            "later. It's ok for now!\x02\x03",
            "#02102FHaha, I think we'll be able to\x01",
            "make an interesting gourmet\x01",
            "guide thanks to all of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FAhaha. That was really\x01",
            "tough...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FThen, the request is\x01",
            "complete?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02104FYes. Thanks for your help,\x01",
            "guys.\x02\x03",
            "#02109FIt'll take a little more time\x01",
            "to publish the gourmet guide.\x01",
            "Please look forward to it!\x02\x03",
            "#02102FI'll be sure to let you guys\x01",
            "know if I need anything else♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FThanks. Excuse us, then.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Gourmet Guide\x01",
            "Coverage Support]\x07\x00\x01",
            "completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 6)
    OP_29(0x80, 0x1, 0x12)
    OP_29(0x80, 0x4, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_A05E")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A05E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_A070")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A070")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_A082")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A082")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_A094")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A094")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_A0A6")
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A0A6")

    SetChrFlags(0xB, 0x80)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -6370, 250, 2630, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_23_87F5 end

    def Function_24_A0D7(): pass

    label("Function_24_A0D7")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A0E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A529")
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_A113")
    MenuCmd(1, 1, "★Fairy Gelato")
    Jump("loc_A123")

    label("loc_A113")

    MenuCmd(1, 1, "Fairy Gelato")

    label("loc_A123")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_A146")
    MenuCmd(1, 1, "★Phoenix Noodles")
    Jump("loc_A159")

    label("loc_A146")

    MenuCmd(1, 1, "Phoenix Noodles")

    label("loc_A159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_A183")
    MenuCmd(1, 1, "★Satisfying Basil Pasta")
    Jump("loc_A19D")

    label("loc_A183")

    MenuCmd(1, 1, "Satisfying Basil Pasta")

    label("loc_A19D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_A1C3")
    MenuCmd(1, 1, "★Bitter Tomato Soda")
    Jump("loc_A1D9")

    label("loc_A1C3")

    MenuCmd(1, 1, "Bitter Tomato Soda")

    label("loc_A1D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_A1FC")
    MenuCmd(1, 1, "★Spicy Mapo Tofu")
    Jump("loc_A20F")

    label("loc_A1FC")

    MenuCmd(1, 1, "Spicy Mapo Tofu")

    label("loc_A20F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_A233")
    MenuCmd(1, 1, "★Sunset Croissant")
    Jump("loc_A247")

    label("loc_A233")

    MenuCmd(1, 1, "Sunset Croissant")

    label("loc_A247")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_A26D")
    MenuCmd(1, 1, "★Chef's Omelet Rice")
    Jump("loc_A283")

    label("loc_A26D")

    MenuCmd(1, 1, "Chef's Omelet Rice")

    label("loc_A283")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_A2AA")
    MenuCmd(1, 1, "★Thick Stamina Steak")
    Jump("loc_A2C1")

    label("loc_A2AA")

    MenuCmd(1, 1, "Thick Stamina Steak")

    label("loc_A2C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_A2EA")
    MenuCmd(1, 1, "★Slow-Cooked Beef Stew")
    Jump("loc_A303")

    label("loc_A2EA")

    MenuCmd(1, 1, "Slow-Cooked Beef Stew")

    label("loc_A303")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_A32E")
    MenuCmd(1, 1, "★Addictive Curry Hot Pot")
    Jump("loc_A349")

    label("loc_A32E")

    MenuCmd(1, 1, "Addictive Curry Hot Pot")

    label("loc_A349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_A372")
    MenuCmd(1, 1, "★Rich Soy Milk Hot Pot")
    Jump("loc_A38B")

    label("loc_A372")

    MenuCmd(1, 1, "Rich Soy Milk Hot Pot")

    label("loc_A38B")

    MenuCmd(1, 1, "Cancel")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 0)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A402"),
        (1, "loc_A41B"),
        (2, "loc_A434"),
        (3, "loc_A44D"),
        (4, "loc_A466"),
        (5, "loc_A47F"),
        (6, "loc_A498"),
        (7, "loc_A4B1"),
        (8, "loc_A4CA"),
        (9, "loc_A4E3"),
        (10, "loc_A4FC"),
        (11, "loc_A515"),
        (SWITCH_DEFAULT, "loc_A524"),
    )


    label("loc_A402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_A413")
    ClearScenarioFlags(0x172, 1)
    Jump("loc_A416")

    label("loc_A413")

    SetScenarioFlags(0x172, 1)

    label("loc_A416")

    Jump("loc_A524")

    label("loc_A41B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_A42C")
    ClearScenarioFlags(0x172, 2)
    Jump("loc_A42F")

    label("loc_A42C")

    SetScenarioFlags(0x172, 2)

    label("loc_A42F")

    Jump("loc_A524")

    label("loc_A434")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_A445")
    ClearScenarioFlags(0x172, 3)
    Jump("loc_A448")

    label("loc_A445")

    SetScenarioFlags(0x172, 3)

    label("loc_A448")

    Jump("loc_A524")

    label("loc_A44D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_A45E")
    ClearScenarioFlags(0x172, 4)
    Jump("loc_A461")

    label("loc_A45E")

    SetScenarioFlags(0x172, 4)

    label("loc_A461")

    Jump("loc_A524")

    label("loc_A466")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_A477")
    ClearScenarioFlags(0x172, 5)
    Jump("loc_A47A")

    label("loc_A477")

    SetScenarioFlags(0x172, 5)

    label("loc_A47A")

    Jump("loc_A524")

    label("loc_A47F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_A490")
    ClearScenarioFlags(0x172, 6)
    Jump("loc_A493")

    label("loc_A490")

    SetScenarioFlags(0x172, 6)

    label("loc_A493")

    Jump("loc_A524")

    label("loc_A498")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_A4A9")
    ClearScenarioFlags(0x172, 7)
    Jump("loc_A4AC")

    label("loc_A4A9")

    SetScenarioFlags(0x172, 7)

    label("loc_A4AC")

    Jump("loc_A524")

    label("loc_A4B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_A4C2")
    ClearScenarioFlags(0x173, 0)
    Jump("loc_A4C5")

    label("loc_A4C2")

    SetScenarioFlags(0x173, 0)

    label("loc_A4C5")

    Jump("loc_A524")

    label("loc_A4CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_A4DB")
    ClearScenarioFlags(0x173, 1)
    Jump("loc_A4DE")

    label("loc_A4DB")

    SetScenarioFlags(0x173, 1)

    label("loc_A4DE")

    Jump("loc_A524")

    label("loc_A4E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_A4F4")
    ClearScenarioFlags(0x173, 2)
    Jump("loc_A4F7")

    label("loc_A4F4")

    SetScenarioFlags(0x173, 2)

    label("loc_A4F7")

    Jump("loc_A524")

    label("loc_A4FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_A50D")
    ClearScenarioFlags(0x173, 3)
    Jump("loc_A510")

    label("loc_A50D")

    SetScenarioFlags(0x173, 3)

    label("loc_A510")

    Jump("loc_A524")

    label("loc_A515")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A524")

    label("loc_A524")

    Jump("loc_A0E1")

    label("loc_A529")

    Return()

    # Function_24_A0D7 end

    def Function_25_A52A(): pass

    label("Function_25_A52A")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Regarding battlefield coverage of the Hundred Days'\x01",
            "War, over a three-month period, the series of reports\x01",
            "overflowed with honesty and a sense of justice.\x02\x03",
            "To recognize that achievement, I award the Fuelitzer\x01",
            "Prize. S1192, November\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_25_A52A end

    def Function_26_A649(): pass

    label("Function_26_A649")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_A653")
    Return()

    label("loc_A653")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A801")

    ChrTalk(
        0x8,
        "Ah, everyone!\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A6C2():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_A6C2)
    Sleep(50)

    def lambda_A6D2():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_A6D2)
    Sleep(50)

    def lambda_A6E2():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_A6E2)
    Sleep(50)

    def lambda_A6F2():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_A6F2)
    Sleep(50)

    def lambda_A702():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x4, 2, lambda_A702)
    Sleep(50)

    def lambda_A712():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x5, 2, lambda_A712)
    WaitChrThread(0x0, 2)
    Fade(1000)
    OP_68(-2860, 1510, 720, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(25500, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "I'm terribly sorry, but\x01",
            "entry to 2F is restricted\x01",
            "to editorial staff only.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you have business\x01",
            "there, please speak with\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FS-Sorry. Excuse us.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_A85C")

    label("loc_A801")


    ChrTalk(
        0x101,
        (
            "#00000FLooks like 2F entry is\x01",
            "prohibited. It's not like we\x01",
            "can go up there uninvited.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A85C")

    Sleep(50)
    SetChrPos(0x0, -6370, 20, 2470, 180)
    EventEnd(0x4)
    Return()

    # Function_26_A649 end

    def Function_27_A873(): pass

    label("Function_27_A873")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Back issues of Crossbell\x01",
            "Times are lined up on\x01",
            "the shelves.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Read '04 First Half ①]\x01",      # 0
            "[Read '04 First Half ②]\x01",      # 1
            "[Cancel]\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA28")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Crossbell Times ①]\x01",         # 0
            "[Crossbell Times ②]\x01",         # 1
            "[Crossbell Times ③]\x01",         # 2
            "[Crossbell Times Extra]\x01",      # 3
            "[Crossbell Times ④]\x01",         # 4
            "[Cancel]\x01",                     # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A9D3")
    UseItem(0x2BC, 0xFF)

    label("loc_A9D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A9E7")
    UseItem(0x2BD, 0xFF)

    label("loc_A9E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A9FB")
    UseItem(0x2BE, 0xFF)

    label("loc_A9FB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA0F")
    UseItem(0x2BF, 0xFF)

    label("loc_AA0F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA23")
    UseItem(0x2C0, 0xFF)

    label("loc_AA23")

    Jump("loc_AB14")

    label("loc_AA28")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB0B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Crossbell Times ⑤]\x01",      # 0
            "[Crossbell Times ⑥]\x01",      # 1
            "[Crossbell Times ⑦]\x01",      # 2
            "[Crossbell Times ⑧]\x01",      # 3
            "[Cancel]\x01",                  # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AACA")
    UseItem(0x2C1, 0xFF)

    label("loc_AACA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AADE")
    UseItem(0x2C2, 0xFF)

    label("loc_AADE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AAF2")
    UseItem(0x2C3, 0xFF)

    label("loc_AAF2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB06")
    UseItem(0x2C4, 0xFF)

    label("loc_AB06")

    Jump("loc_AB14")

    label("loc_AB0B")

    FadeToBright(300, 0)

    label("loc_AB14")

    TalkEnd(0xFF)
    Return()

    # Function_27_A873 end

    SaveToFile()

Try(main)
