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
        "Function_5_1E5C",         # 05, 5
        "Function_6_1FEC",         # 06, 6
        "Function_7_21FF",         # 07, 7
        "Function_8_23DA",         # 08, 8
        "Function_9_30A2",         # 09, 9
        "Function_10_3362",        # 0A, 10
        "Function_11_372F",        # 0B, 11
        "Function_12_422B",        # 0C, 12
        "Function_13_53AA",        # 0D, 13
        "Function_14_5558",        # 0E, 14
        "Function_15_5714",        # 0F, 15
        "Function_16_5899",        # 10, 16
        "Function_17_5B28",        # 11, 17
        "Function_18_5DD4",        # 12, 18
        "Function_19_676E",        # 13, 19
        "Function_20_6EBF",        # 14, 20
        "Function_21_730B",        # 15, 21
        "Function_22_876F",        # 16, 22
        "Function_23_8A0F",        # 17, 23
        "Function_24_A348",        # 18, 24
        "Function_25_A799",        # 19, 25
        "Function_26_A8B9",        # 1A, 26
        "Function_27_AAE3",        # 1B, 27
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

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AD3")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_994")

    ChrTalk(
        0x8,
        (
            "The Special Support Section...\x01",
            "Could you be here for\x01",
            "our company's request?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Actually, the person in charge of it\x01",
            "left to cover the derailment accident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm terribly sorry, but I have to\x01",
            "ask you to come again another day.\x02",
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
            "derailment accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you have business with any of the\x01",
            "reporters, I'll deliver your message.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ACF")

    label("loc_A50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_ACF")

    ChrTalk(
        0x8,
        (
            "To think a derailment occurred\x01",
            "along West Crossbell Highway...\x02",
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_END)), "loc_CFC")
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
            "Quit\x01",                 # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B4B")
    TalkEnd(0x8)
    Return()

    label("loc_B4B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_B77")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_B8A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_B9D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_BB0")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_BC3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_BD6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_BE9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_BFC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_C0F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_C0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_C22")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_C22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_C35")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_C35")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C62")
    TalkEnd(0x8)
    Call(0, 22)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C5C")
    Call(0, 23)

    label("loc_C5C")

    Return()

    label("loc_C62")


    ChrTalk(
        0x101,
        (
            "#00005F(Whoops, we haven't been to at\x01",
            "least 6 restaurants, have we.)\x02\x03",
            "#00003F(We can't report our coverage\x01",
            "now. Let's try a little harder.)\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Return()

    label("loc_CF7")

    Jump("loc_D0A")

    label("loc_CFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D0A")
    Call(0, 20)
    Return()

    label("loc_D0A")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_E10")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DBF")

    ChrTalk(
        0x8,
        (
            "Everyone, please do your best\x01",
            "with the gourmet guide coverage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You get to eat a lot of\x01",
            "delicious food, so I think\x01",
            "you are going to enjoy it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E0B")

    label("loc_DBF")


    ChrTalk(
        0x8,
        "Good work everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We will be counting on\x01",
            "you in the future too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E0B")

    Jump("loc_1E58")

    label("loc_E10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_E9E")

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
            "Uh uh. Anyway, I am\x01",
            "just glad he is safe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E58")

    label("loc_E9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_EAC")
    Jump("loc_1E58")

    label("loc_EAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_109A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FBE")

    ChrTalk(
        0x8,
        (
            "It was frightening when a State Guard\x01",
            "soldier came in this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's only been a week since the declaration\x01",
            "and thing are already this bad...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When people talk about tense situations,\x01",
            "they must be talking about times like these.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1095")

    label("loc_FBE")


    ChrTalk(
        0x8,
        (
            "When I looked at the situation around town,\x01",
            "it seemed like there are, as usual, a lot of\x01",
            "people who support the President, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Honestly, I am very unsure.\x01",
            "...I really wonder what's going to happen now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1095")

    Jump("loc_1E58")

    label("loc_109A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_12EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1222")

    ChrTalk(
        0x8,
        (
            "The reconstruction after the incident, and the\x01",
            "referendum will be held in three days' time.\x02",
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
    Jump("loc_12E5")

    label("loc_1222")


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

    label("loc_12E5")

    Jump("loc_1E58")

    label("loc_12EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_12F8")
    Jump("loc_1E58")

    label("loc_12F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_13CC")

    ChrTalk(
        0x8,
        (
            "It seems that Miss Grace entered\x01",
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
    Jump("loc_1E58")

    label("loc_13CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_15CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1533")

    ChrTalk(
        0x8,
        (
            "I was very busy yesterday running our\x01",
            "contacts for the derailment bulletin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thinking back on things, we've had more opportunities\x01",
            "for extra issues than average this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But the amount of extras with good\x01",
            "news hasn't changed at all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's nothing but incidents and accidents.\x01",
            "That makes me a little depressed.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15CA")

    label("loc_1533")


    ChrTalk(
        0x8,
        (
            "But the amount of extras with good\x01",
            "news hasn't changed at all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's nothing but incidents and accidents.\x01",
            "That makes me a little depressed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15CA")

    Jump("loc_1E58")

    label("loc_15CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_168B")

    ChrTalk(
        0x8,
        (
            "The editorial staff is now working\x01",
            "on a news bulletin regarding the\x01",
            "derailment accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you have business with any of the\x01",
            "reporters, I'll deliver your message.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E58")

    label("loc_168B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_170F")

    ChrTalk(
        0x8,
        (
            "To think a derailment occurred\x01",
            "along West Crossbell Highway...\x02",
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
    Jump("loc_1E58")

    label("loc_170F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1720")
    Call(0, 6)
    Jump("loc_1E58")

    label("loc_1720")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1996")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18CC")

    ChrTalk(
        0x8,
        (
            "A civic forum with the independence\x01",
            "question as the theme will be held at\x01",
            "the City Meeting Hall in two days, but...\x02",
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
            "Wondering if we can do anything besides\x01",
            "articles― We made a suggestion.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1991")

    label("loc_18CC")


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
            "holding a civic forum.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1991")

    Jump("loc_1E58")

    label("loc_1996")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1A64")

    ChrTalk(
        0x8,
        (
            "Miss Grace and Reins said they needed to\x01",
            "hurry and buy something and headed\x01",
            "for the department store, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They might be late for the main session\x01",
            "due to that... What could it be?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E58")

    label("loc_1A64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1A75")
    Call(0, 7)
    Jump("loc_1E58")

    label("loc_1A75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1B0E")

    ChrTalk(
        0x8,
        (
            "The Trade Conference\x01",
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
    Jump("loc_1E58")

    label("loc_1B0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1D12")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C5E")

    ChrTalk(
        0x8,
        (
            "I understand that Reins is going\x01",
            "to visit some ruins today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Miss Grace complained about her\x01",
            "obedient assistant being gone, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now that I think about it, Reins\x01",
            "joined our company just this year.\x02",
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
    Jump("loc_1D0D")

    label("loc_1C5E")


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

    label("loc_1D0D")

    Jump("loc_1E58")

    label("loc_1D12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1E58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DC8")

    ChrTalk(
        0x8,
        (
            "My, it's been awhile. The Special\x01",
            "Support Section, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Welcome to Crossbell News.\x01",
            "If you ever need anything, \x01",
            "please don't hesitate to ask.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E58")

    label("loc_1DC8")


    ChrTalk(
        0x8,
        (
            "Uh uh, Miss Grace will be\x01",
            "overjoyed now that you've\x01",
            "resumed your activities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you ever need anything,\x01",
            "please don't hesitate to ask.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E58")

    TalkEnd(0x8)
    Return()

    # Function_4_867 end

    def Function_5_1E5C(): pass

    label("Function_5_1E5C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1EED")

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
            "Uh uh. Anyway, I am\x01",
            "just glad he is safe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FE8")

    label("loc_1EED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1F73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F0C")
    TalkEnd(0xFE)
    Call(0, 18)
    Return()

    label("loc_1F0C")


    ChrTalk(
        0xFE,
        (
            "I really hope Reins doesn't\x01",
            "do anything reckless, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I pray\x01",
            "that he's safe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FE8")

    label("loc_1F73")


    ChrTalk(
        0xFE,
        (
            "Ah, everyone.\x01",
            "You can't enter\x01",
            "from this side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have business, speak with\x01",
            "me from across the counter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FE8")

    TalkEnd(0xFE)
    Return()

    # Function_5_1E5C end

    def Function_6_1FEC(): pass

    label("Function_6_1FEC")

    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2153")

    ChrTalk(
        0xD,
        (
            "Hmm, I see. I thought that\x01",
            "might be the case today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Incidentally, today he's\x01",
            "at Mining Town Mainz and\x01",
            "I think he will be back late too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I think you should have\x01",
            "left a message that you\x01",
            "wanted to meet him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Well, you're certainly right about that.\x02",
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
    Jump("loc_21FA")

    label("loc_2153")


    ChrTalk(
        0x8,
        (
            "Then once again, can I\x01",
            "ask where are you staying?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Yes, it's the Old Dragon Inn on East Street.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Please tell him I'll\x01",
            "be right there when\x01",
            "he contacts me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21FA")

    OP_4C(0xD, 0xFF)
    Return()

    # Function_6_1FEC end

    def Function_7_21FF(): pass

    label("Function_7_21FF")

    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_233F")

    ChrTalk(
        0xD,
        (
            "Hmm, too bad.\x01",
            "Mr. Nielsen's out\x01",
            "of the office, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Sorry, he's\x01",
            "almost never\x01",
            "at the agency.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He said he was going to\x01",
            "see a friend today. I can\x01",
            "take a message for you...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "No, that's all right. \x01",
            "I just wanted to spend some\x01",
            "time chatting with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "There will be other chances.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_23D5")

    label("loc_233F")


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

    label("loc_23D5")

    OP_4C(0xD, 0xFF)
    Return()

    # Function_7_21FF end

    def Function_8_23DA(): pass

    label("Function_8_23DA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_23EB")
    Jump("loc_309E")

    label("loc_23EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_23F9")
    Jump("loc_309E")

    label("loc_23F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_249C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2414")
    Call(0, 9)
    Jump("loc_2497")

    label("loc_2414")

    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xB,
        (
            "#02100FAlright Reins, please continue\x01",
            "negotiating with the State Guard.\x02\x03",
            "If anything happens, contact me immediately.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)

    label("loc_2497")

    Jump("loc_309E")

    label("loc_249C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_24AA")
    Jump("loc_309E")

    label("loc_24AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2552")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24C9")
    TalkEnd(0xFE)
    Call(0, 19)
    Return()

    label("loc_24C9")


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
    Jump("loc_309E")

    label("loc_2552")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_278D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26E6")

    ChrTalk(
        0xB,
        (
            "#02100FAh, Lloyd and friends.\x01",
            "Nice work last night.\x02\x03",
            "#02101FAbout that... Do you know\x01",
            "something about Wald?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FAh, no...\x02\x03",
            "#00001FWe went to Ignis this morning\x01",
            "but we didn't get any info.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02103FI see...\x02\x03",
            "#02102FWell, I'll try some of\x01",
            "my own ideas, then.\x02\x03",
            "#02100FAnd you too Wazy... \x01",
            "Don't think too hard, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304FHu hu, thank you for your concern.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x171, 1)
    Jump("loc_2788")

    label("loc_26E6")


    ChrTalk(
        0xB,
        (
            "#02101FEven so... I'm worried\x01",
            "about those Azure Flowers.\x02\x03",
            "#02103FIf there was someone other than\x01",
            "Joachim who could make that drug...\x01",
            "That would be very bad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2788")

    Jump("loc_309E")

    label("loc_278D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_279B")
    Jump("loc_309E")

    label("loc_279B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2BA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A28")

    ChrTalk(
        0xB,
        (
            "#02104F*sigh*, a morning dose really calms you down, eh?\x02\x03",
            "#02102FWould any of you guys like one?\x01",
            "It's just canned coffee, though.\x02",
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
            "#02102FOh really?\x01",
            "Uh uh, oh well.\x02\x03",
            "#02104FFor now, it looks like you did\x01",
            "a good job with yesterday's\x01",
            ""Cryptids" extermination.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FThat's certainly true, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F...You sure get word fast.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02109FI guess. That's the business\x01",
            "we're in, after all.\x02\x03",
            "#02100FIf nothing else, take care\x01",
            "not to get yourselves hurt.\x02\x03",
            "#02102FAfter all is said and done,\x01",
            "our bodies are our capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, thank you very much.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x171, 2)
    Jump("loc_2BA1")

    label("loc_2A28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ADE")

    ChrTalk(
        0xB,
        (
            "#02103FEven so, "Cryptids", eh?\x01",
            "I don't really get it, but they're\x01",
            "strange and indescribable.\x02\x03",
            "#02100FLloyd and friends, take care\x01",
            "not to get yourselves hurt.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2B84")

    label("loc_2ADE")


    ChrTalk(
        0xB,
        (
            "#02100FAh, right, right. Once you've got your\x01",
            "gourmet recommendations in order,\x01",
            "report to the reception desk, ok?\x02\x03",
            "#02109FAlright then, I'm counting on you♪\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 2)

    label("loc_2B84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2BA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2BA1")
    ClearScenarioFlags(0x0, 2)

    label("loc_2BA1")

    Jump("loc_309E")

    label("loc_2BA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2BB4")
    Jump("loc_309E")

    label("loc_2BB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2BC2")
    Jump("loc_309E")

    label("loc_2BC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2BD0")
    Jump("loc_309E")

    label("loc_2BD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2C7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BEB")
    Call(0, 10)
    Jump("loc_2C78")

    label("loc_2BEB")


    ChrTalk(
        0xB,
        (
            "#02102FAh, this is the "Snowflake Temple"\x01",
            "everyone's talking about, huh.\x02\x03",
            "#02109FThank you very much.\x01",
            "I wanted to try eating it once...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C78")

    Jump("loc_309E")

    label("loc_2C7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3095")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FFD")

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
        "#00000FHa ha, you could say that.\x02",
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
            "#02106FWell, slowly, I guess you could say.\x02\x03",
            "#02100FI investigated other\x01",
            "bidders, but...\x02\x03",
            "If nothing else happens, that\x01",
            "whole place is going to belong\x01",
            "to Heiyue at this rate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10103FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02106FWell, nobody can\x01",
            "say anymore without\x01",
            "lifting the cover.\x02\x03",
            "#02100FAnd so, I plan to finish\x01",
            "up all this work that's\x01",
            "been piling up today.\x02\x03",
            "#02102FOh yeah! I'll be sure to write\x01",
            "an article about how the\x01",
            "Support Section's restarted.\x02\x03",
            "#02109FIf you have a comment\x01",
            "or photo you want me\x01",
            "to use, lay it on me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FHu hu, then I think\x01",
            "I'll give you one of\x01",
            "my host club photos.\x02",
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
        "#00006F...Please don't, I'm begging you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13E, 3)
    Jump("loc_3090")

    label("loc_2FFD")


    ChrTalk(
        0xB,
        (
            "#02106F*sigh*, but to think Reins is out of\x01",
            "the office on a day like today.\x02\x03",
            "I was thinking of forcing\x01",
            "a lot of odd jobs onto\x01",
            "him... Too bad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3090")

    Jump("loc_309E")

    label("loc_3095")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_309E")

    label("loc_309E")

    TalkEnd(0xFE)
    Return()

    # Function_8_23DA end

    def Function_9_30A2(): pass

    label("Function_9_30A2")

    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0xB, 0x0, 0)
    TurnDirection(0xA, 0x0, 0)

    ChrTalk(
        0xB,
        (
            "#02101FAh, Lloyd and friends. You saw the\x01",
            "President's address, didn't you.\x02",
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
            "#00101FWhat will all\x01",
            "of you do now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02103FAt the very least,\x01",
            "we'll cover this.\x02\x03",
            "#02101FWe'll of course question the\x01",
            "State Guard again and try to\x01",
            "get something specific...\x02\x03",
            "And gather the voices of the citizens in town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "All that's left is to investigate the\x01",
            "reaction of the international media.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The international communicator\x01",
            "on 2F is in full operation.\x02",
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
            "#02104FI guess. I think you guys\x01",
            "have stuff too, so let's\x01",
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

    # Function_9_30A2 end

    def Function_10_3362(): pass

    label("Function_10_3362")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xB,
        (
            "#02109FUh uh, Mr. Nielsen.\x01",
            "We finally meet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Yes, I've been looking forward to this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Come to think of it, I've\x01",
            "heard from the editor-in-chief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "You've become bold in these\x01",
            "past three years, he said.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xB)

    ChrTalk(
        0xB,
        (
            "#02109FDon't say that. I still have\x01",
            "a long way to go, after all.\x02\x03",
            "#02104FI always do what I want,\x01",
            "I guess... So I've only\x01",
            "done what I want to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Ha ha. You say that, but\x01",
            "the most important thing\x01",
            "is to enjoy the work.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_35E9")

    ChrTalk(
        0x101,
        (
            "#00000F(Miss Grace... She's different\x01",
            "than she usually is in\x01",
            "front of Mr. Nielsen.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F(*giggle*, that's right.\x01",
            "You don't see this often.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3723")

    label("loc_35E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 3)), scpexpr(EXPR_END)), "loc_3690")

    ChrTalk(
        0x101,
        (
            "#00000F(I feel like Miss Grace is somehow\x01",
            "different from how she usually is.)\x02\x03",
            "#00003F(Mr. Nielsen...was it?\x01",
            "It seems like they know each other...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3723")

    label("loc_3690")


    ChrTalk(
        0x101,
        (
            "#00000F(I feel like Miss Grace is somehow\x01",
            "different from how she usually is.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(Yes, I agree. I wonder\x01",
            "who's next to her, though.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3723")

    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x148, 1)
    Return()

    # Function_10_3362 end

    def Function_11_372F(): pass

    label("Function_11_372F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3849")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_374D")
    Call(0, 13)
    Jump("loc_3844")

    label("loc_374D")


    ChrTalk(
        0xFE,
        (
            "We're leaving coverage of the huge\x01",
            "tree to senior Grace. We plan to chase\x01",
            "after the actions of the government.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know what kind of organization we\x01",
            "can form before the two major powers act,\x01",
            "but... This is a story I just can't miss.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3844")

    Jump("loc_4227")

    label("loc_3849")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3857")
    Jump("loc_4227")

    label("loc_3857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_38DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3872")
    Call(0, 9)
    Jump("loc_38D5")

    label("loc_3872")

    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xFE,
        "Yes, understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Miss Grace too, please don't dig\x01",
            "into the State Guard too much.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)

    label("loc_38D5")

    Jump("loc_4227")

    label("loc_38DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_38E8")
    Jump("loc_4227")

    label("loc_38E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3983")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3907")
    TalkEnd(0xFE)
    Call(0, 19)
    Return()

    label("loc_3907")


    ChrTalk(
        0xFE,
        (
            "...I heard "Red Constellation"\x01",
            "aren't your usual opponents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone, be careful if you're\x01",
            "heading to Mainz.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4227")

    label("loc_3983")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3A1E")

    ChrTalk(
        0xFE,
        (
            "I'm glad there's not too much confusion\x01",
            "regarding the derailment for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish we could've found the\x01",
            "source of that drug, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4227")

    label("loc_3A1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3A2C")
    Jump("loc_4227")

    label("loc_3A2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3AC2")

    ChrTalk(
        0xFE,
        "We've got an editing meeting this morning.\x02",
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
    Jump("loc_4227")

    label("loc_3AC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3AD0")
    Jump("loc_4227")

    label("loc_3AD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3ADE")
    Jump("loc_4227")

    label("loc_3ADE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3AEC")
    Jump("loc_4227")

    label("loc_3AEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3AFA")
    Jump("loc_4227")

    label("loc_3AFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3B08")
    Jump("loc_4227")

    label("loc_3B08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4227")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41AE")

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
            "...No, what am I saying? I've got to get these\x01",
            "materials in order and get back to my desk.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 500)
    Sleep(200)

    ChrTalk(
        0xFE,
        "Ah, you're the Special Support Section.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FYou're...someone who often\x01",
            "works together with Miss Grace...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yes, I'm Reins, a reporter.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I say that, but lately I've \x01",
            "been getting pigeonholed \x01",
            "as a cameraman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*. I tell around that I'm\x01",
            "a reporter, but... *grumble*...\x02",
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
        "#00106FT-There must be many reasons...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHu hu, there's a gap between \x01",
            "ideals and reality, you know.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F46")

    ChrTalk(
        0x101,
        (
            "#00000FUmm, by the way,\x01",
            "is Miss Grace in?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, no, senior Grace just left\x01",
            "for her coverage today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Something about the coverage\x01",
            "being easier with her alone...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And instead of that,\x01",
            "she forced a quantity\x01",
            "of her work onto me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, whether it's helping or not,\x01",
            "writing is fun for a reporter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4078")

    label("loc_3F46")


    ChrTalk(
        0x101,
        (
            "#00000FUmm, by the way, we already\x01",
            "met Miss Grace, but you're\x01",
            "not with her today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, it was something about the\x01",
            "coverage being easier with her alone...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And instead of that,\x01",
            "she forced a quantity\x01",
            "of her work onto me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, whether it's helping or not,\x01",
            "writing is fun for a reporter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4078")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        (
            "Ah, while we were talking here\x01",
            "like this, the deadline is...!\x02",
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
        "#10100FL-Looks like we're interrupting.\x02",
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

    label("loc_41AE")


    ChrTalk(
        0xFE,
        (
            "Umm, now where were the materials\x01",
            "for that other article?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ooh, while I was talking\x01",
            "like that, the deadline...!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4227")

    TalkEnd(0xFE)
    Return()

    # Function_11_372F end

    def Function_12_422B(): pass

    label("Function_12_422B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_42FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4249")
    Call(0, 13)
    Jump("loc_42F5")

    label("loc_4249")


    ChrTalk(
        0xFE,
        (
            "Anyway, right now, I've got to use my legs\x01",
            "and scrape together as much info as I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just because I finished a bit of work\x01",
            "doesn't mean I have time for a break.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42F5")

    Jump("loc_53A6")

    label("loc_42FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_441E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4319")
    TalkEnd(0xFE)
    Call(0, 18)
    Return()

    label("loc_4319")


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
            "How pathetic. Under the current structure,\x01",
            "we can't even write an article\x01",
            "about the President's injustices.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And so, that's why\x01",
            "I believe in your\x01",
            "breaking into operation!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53A6")

    label("loc_441E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_460E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_454C")

    ChrTalk(
        0xFE,
        (
            "Hey, hey, hey! No matter\x01",
            "how you look at it, this\x01",
            "development is just too quick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honestly, it would be weird\x01",
            "if nothing happened...\x01",
            "An uproar can't be helped.\x02",
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
    Jump("loc_4609")

    label("loc_454C")


    ChrTalk(
        0xFE,
        (
            "Honestly, it would be weird\x01",
            "if nothing happened...\x01",
            "An uproar can't be helped.\x02",
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

    label("loc_4609")

    Jump("loc_53A6")

    label("loc_460E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_470D")
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
    Jump("loc_53A6")

    label("loc_470D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_471B")
    Jump("loc_53A6")

    label("loc_471B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4882")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47F2")

    ChrTalk(
        0xFE,
        (
            "It seems the CGF are\x01",
            "in a tough spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of that, I wonder if the Imperial army\x01",
            "will intervene if this continues for too long...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Man oh man. That's no laughing matter.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_487D")

    label("loc_47F2")


    ChrTalk(
        0xFE,
        (
            "If the occupation continues for too long, I\x01",
            "wonder if the Imperial army will intervene...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Man oh man. That's no laughing matter.\x02",
    )

    CloseMessageWindow()

    label("loc_487D")

    Jump("loc_53A6")

    label("loc_4882")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_49D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4959")

    ChrTalk(
        0xFE,
        (
            "*sigh*. Editing these bulletins really\x01",
            "drains my stamina every single time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It wouldn't be a problem if I was 20,\x01",
            "but lately I really feel it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Man, I don't want to get old.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_49D4")

    label("loc_4959")


    ChrTalk(
        0xFE,
        (
            "Though I say that, I'm\x01",
            "still in my 30s. I'm in\x01",
            "the prime of my life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I don't want to say nothing but complaints.\x02",
    )

    CloseMessageWindow()

    label("loc_49D4")

    Jump("loc_53A6")

    label("loc_49D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_49E7")
    Jump("loc_53A6")

    label("loc_49E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4B2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AFE")

    ChrTalk(
        0xFE,
        "*puff*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now then, I think I'll look over the\x01",
            "materials for this meeting once again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, state independence is\x01",
            "at the center of discussions today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I don't get this material\x01",
            "in my head beforehand, \x01",
            "I'll run out of arguments.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4B25")

    label("loc_4AFE")


    ChrTalk(
        0xFE,
        "Now then, materials, materials...\x02",
    )

    CloseMessageWindow()

    label("loc_4B25")

    Jump("loc_53A6")

    label("loc_4B2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4D9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CDA")

    ChrTalk(
        0xFE,
        (
            "From social problems starting with politics \x01",
            "and economics to amusement information \x01",
            "about culture and public entertainment...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The cases our reporters carry have an\x01",
            "amount of variety you would not believe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we were a bigger\x01",
            "news agency we could\x01",
            "specialize, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're a selected few who take mobility\x01",
            "into serious consideration. It means that\x01",
            "one man can basically cover anything.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4D9A")

    label("loc_4CDA")


    ChrTalk(
        0xFE,
        (
            "Today, materials for three cases are\x01",
            "going to come in from the afternoon...\x01",
            "I also hot a bit of work left to do for my column.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, while I'm free, might\x01",
            "as well take care of that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D9A")

    Jump("loc_53A6")

    label("loc_4D9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4F3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EB0")

    ChrTalk(
        0xFE,
        (
            "The number of reports from\x01",
            "each company covering the\x01",
            "main session is limited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We decided to\x01",
            "send in Grace\x01",
            "and Reins.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The rest of the members here are waiting\x01",
            "for info from Grace and Reins and getting\x01",
            "ready to publish the bulletin.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4F35")

    label("loc_4EB0")


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

    label("loc_4F35")

    Jump("loc_53A6")

    label("loc_4F3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5096")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FFB")

    ChrTalk(
        0xFE,
        (
            "I just had the photos Grace\x01",
            "and Reins took developed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Look at them.\x01",
            "Aren't they well taken?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now then, which photo should\x01",
            "I use in the extra edition...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5091")

    label("loc_4FFB")


    ChrTalk(
        0xFE,
        (
            "This one and that one, and maybe\x01",
            "that one on the right would be good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After resizing them there'll be\x01",
            "the editor-in-chief check...and done.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5091")

    Jump("loc_53A6")

    label("loc_5096")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5252")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5180")

    ChrTalk(
        0xFE,
        (
            "Heh, for as much as Heiyue\x01",
            "acted, it ended up going to\x01",
            "Crimson & Co., huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From the start, we never did\x01",
            "get to the bottom of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well for now, all we can do is\x01",
            "remain silent and wait and see.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_524D")

    label("loc_5180")


    ChrTalk(
        0xFE,
        (
            "Even though the Trade\x01",
            "Conference finally starts\x01",
            "tomorrow... Something's up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, just thinking about it won't solve\x01",
            "anything. Anyway, I've got to get the\x01",
            "Trade Conference-related news in order.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_524D")

    Jump("loc_53A6")

    label("loc_5252")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5328")

    ChrTalk(
        0xFE,
        (
            "*puff*... Heiyue is after\x01",
            "Revache's property, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, the situation being what it is,\x01",
            "the Empire won't stay silent for long...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man oh man... It just gets\x01",
            "more and more suspicious.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53A6")

    label("loc_5328")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_53A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5343")
    Call(0, 15)
    Jump("loc_53A6")

    label("loc_5343")


    ChrTalk(
        0xFE,
        "Oh, thank you for the trouble.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "These are baumkuchen, right?\x01",
            "Ha ha, you always like them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53A6")

    TalkEnd(0xFE)
    Return()

    # Function_12_422B end

    def Function_13_53AA(): pass

    label("Function_13_53AA")

    OP_4B(0xA, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x9,
        (
            "Hey Reins.\x01",
            "Is your camera ready?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Yes, it's in perfect condition.\x02",
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
        "Yeah, got it!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 3)), scpexpr(EXPR_END)), "loc_5542")

    ChrTalk(
        0x101,
        (
            "#00000F(Mr. Reins has resumed \x01",
            "working as a reporter too, huh.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F(I don't know if I should call it two birds with\x01",
            "one stone... Or a man with amazing vitality.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5542")

    OP_4C(0xA, 0xFF)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 3)
    Return()

    # Function_13_53AA end

    def Function_14_5558(): pass

    label("Function_14_5558")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5569")
    Jump("loc_5710")

    label("loc_5569")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5577")
    Jump("loc_5710")

    label("loc_5577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5585")
    Jump("loc_5710")

    label("loc_5585")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5593")
    Jump("loc_5710")

    label("loc_5593")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_55A1")
    Jump("loc_5710")

    label("loc_55A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_55AF")
    Jump("loc_5710")

    label("loc_55AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_55BD")
    Jump("loc_5710")

    label("loc_55BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_55CB")
    Jump("loc_5710")

    label("loc_55CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_55D9")
    Jump("loc_5710")

    label("loc_55D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_566D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55F4")
    Call(0, 10)
    Jump("loc_5668")

    label("loc_55F4")


    ChrTalk(
        0xFE,
        (
            "Ha ha, that's Grace for you. \x01",
            "You already checked it, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I swear...\x01",
            "One bite, and your cheeks will melt.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5668")

    Jump("loc_5710")

    label("loc_566D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_567B")
    Jump("loc_5710")

    label("loc_567B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5710")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5696")
    Call(0, 15)
    Jump("loc_5710")

    label("loc_5696")


    ChrTalk(
        0xFE,
        (
            "Oh right, I'm giving\x01",
            "you all a souvenir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I found a good shop in the Republic.\x01",
            "Uh uh, I'm sure you'll like them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5710")

    TalkEnd(0xFE)
    Return()

    # Function_14_5558 end

    def Function_15_5714(): pass

    label("Function_15_5714")

    OP_4B(0xC, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x9,
        (
            "Ah, it's certainly\x01",
            "been awhile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's been what, three years\x01",
            "since you were last here?\x02",
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
            "I may cause you trouble, but I look\x01",
            "forward to working with you.\x02",
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
            "If you ever need anything,\x01",
            "please don't hesitate to ask.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x0, 3)
    Return()

    # Function_15_5714 end

    def Function_16_5899(): pass

    label("Function_16_5899")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_58AA")
    Jump("loc_5B24")

    label("loc_58AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_597E")
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Well, whatever the truth may be,\x01",
            "the Empire won't recognize\x01",
            "it's an attack from them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What will the Empire do next\x01",
            "regarding this situation...?\x01",
            "We can only watch that attentively.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    Jump("loc_5B24")

    label("loc_597E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_598C")
    Jump("loc_5B24")

    label("loc_598C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_599A")
    Jump("loc_5B24")

    label("loc_599A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_5A26")

    ChrTalk(
        0xFE,
        (
            "Now then, it looks like the editorial\x01",
            "department's going to get busy very soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I've got to get some free time now.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5B24")

    label("loc_5A26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5AC1")

    ChrTalk(
        0xFE,
        (
            "Looks like they're working\x01",
            "on the bulletin on 2F.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How to say this... This noise is the same\x01",
            "no matter which news agency you go to.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B24")

    label("loc_5AC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5AD2")
    Call(0, 6)
    Jump("loc_5B24")

    label("loc_5AD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5AE0")
    Jump("loc_5B24")

    label("loc_5AE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5AEE")
    Jump("loc_5B24")

    label("loc_5AEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5AFF")
    Call(0, 7)
    Jump("loc_5B24")

    label("loc_5AFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5B0D")
    Jump("loc_5B24")

    label("loc_5B0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5B1B")
    Jump("loc_5B24")

    label("loc_5B1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5B24")

    label("loc_5B24")

    TalkEnd(0xFE)
    Return()

    # Function_16_5899 end

    def Function_17_5B28(): pass

    label("Function_17_5B28")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5D1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C40")

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
            "By the way, the other reporters\x01",
            "resumed their coverage immediately.\x02",
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
    Jump("loc_5D16")

    label("loc_5C40")


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

    label("loc_5D16")

    Jump("loc_5DD0")

    label("loc_5D1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5DD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D3A")
    TalkEnd(0xFE)
    Call(0, 18)
    Return()

    label("loc_5D3A")


    ChrTalk(
        0xFE,
        (
            "I'd like to thank\x01",
            "all of you for\x01",
            "helping Grace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Be careful as you proceed... \x01",
            "And please, let us write an article\x01",
            "about your great efforts.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DD0")

    TalkEnd(0xFE)
    Return()

    # Function_17_5B28 end

    def Function_18_5DD4(): pass

    label("Function_18_5DD4")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5E7E")
    Jump("loc_5EC8")

    label("loc_5E7E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5E9E")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5EC8")

    label("loc_5E9E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5EBE")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5EC8")

    label("loc_5EBE")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5EC8")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    ChrTalk(
        0x9,
        "Oh, the Special Support Section.\x02",
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
        "#00000FNo, we'd love to.\x02",
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
            "I see... So you're planning on breaking\x01",
            "into Orchis Tower, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "And if you succeed, the current\x01",
            "authoritarian system will end, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Man, just when I thought we'd be able\x01",
            "to move around a little easier this\x01",
            "high alert order was handed down.\x02",
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
            "#6P#00105FI see, so even normal orbal\x01",
            "communications are affected...\x02",
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
            "#6P#00301FHmm. If we don't do something about it,\x01",
            "the chaos in the city will only grow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FYeah... You're right.\x02\x03",
            "#00000FBy the way, is\x01",
            "everyone here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Well, the other staff got tied\x01",
            "up at their destinations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Even so, we've been lucky to be able\x01",
            "to contact almost all of them, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Reins is the only one we\x01",
            "haven't been able to contact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "We have no idea at all where\x01",
            "or how he is at present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FMr. Reins...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Well, I'm sure he must be\x01",
            "somewhere in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I hope he didn't take\x01",
            "after Miss Grace and did\x01",
            "something reckless...\x02",
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
            "Your plan must succeed.\x01",
            "This rigid order must be crushed,\x01",
            "rightly or wrongly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYeah, got it!\x02\x03",
            "#00003F(So Mr. Reins is out\x01",
            "of contact, huh...)\x02\x03",
            "#00001F(Miss Grace is probably worried\x01",
            "about his safety too.\x01",
            "Let's keep this in mind too.)\x02",
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

    # Function_18_5DD4 end

    def Function_19_676E(): pass

    label("Function_19_676E")

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
        "Everyone from the Support Section...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02101FYou guys must\x01",
            "have it tough.\x02\x03",
            "#02105FThat's right, Randy―\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#02101F...Where's Randy? \x01",
            "Could he be―\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00003F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108F...Well...\x02",
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
            "#02104FI've no intention of following you. \x01",
            "How about an "advice"?\x02",
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
        "#6P#10105FUmm, what do you mean by...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02101FFirst a condition... \x01",
            "I know a certain amount\x01",
            "about Randy's background.\x02\x03",
            "#02103FI'll just say this. It's not\x01",
            "like I have any doubt\x01",
            "about what I'm saying.\x02\x03",
            "#02100FBut at the same time, I've seen many of\x01",
            "his actions as a member of the Support\x01",
            "Section. You can be sure I believe in him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FMiss Grace...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02103FAnd by your reactions,\x01",
            "I can guess the situation.\x02\x03",
            "#02101FRandy headed to\x01",
            "Mainz alone, right?\x02\x03",
            "To resolve this incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00001F...You know that much?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203F...That is a\x01",
            "Crossbell Times\x01",
            "reporter for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02102FUh uh, I knew it. Bullseye, huh.\x02\x03",
            "#02103FAnd you guys are\x01",
            "going to bring\x01",
            "him back...\x02\x03",
            "#02101FI feel like I shouldn't even ask, but\x01",
            "your minds are made up, aren't they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FOf course! \x01",
            "Randy's our comrade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00101FYes, precisely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02104FI see. Then you really\x01",
            "needn't any advice, huh.\x02\x03",
            "#02101FThen I will say\x01",
            "this to you in\x01",
            "my own style.\x02\x03",
            "#02104F―Be careful out there!\x02\x03",
            "#02109FAnd once again, allow me\x01",
            "to write an article about\x01",
            "your great activities!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYes, thank you very much.\x02",
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

    # Function_19_676E end

    def Function_20_6EBF(): pass

    label("Function_20_6EBF")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70C5")

    ChrTalk(
        0x8,
        (
            "Welcome to Crossbell\x01",
            "News Service.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "Oh, you guys are the Special Support Section...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FGood morning, we're here about\x01",
            "your support request.\x02\x03",
            "You needed help with coverage\x01",
            "for your gourmet guide...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uh uh, thank you very\x01",
            "much for coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Can you accept\x01",
            "the request\x01",
            "right away?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x17D, 0)
    Jump("loc_7116")

    label("loc_70C5")


    ChrTalk(
        0x8,
        (
            "Thank you very\x01",
            "much for coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Can you accept\x01",
            "the request\x01",
            "right away?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7116")

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
            "Quit\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7217")

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
    Jump("loc_730A")

    label("loc_7217")


    ChrTalk(
        0x101,
        (
            "#00006FWe're sorry, we have other business\x01",
            "to attend to right now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "My, is that so...?\x01",
            "We will be waiting, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you would like to accept the request,\x01",
            "please return as soon as you can.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 2700, 20, -2000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)

    label("loc_730A")

    Return()

    # Function_20_6EBF end

    def Function_21_730B(): pass

    label("Function_21_730B")

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
            "#02100FHello, hello!♪ My Special\x01",
            "Support Section friends.\x02\x03",
            "#02109FSorry to keep\x01",
            "you waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FI knew it... You're in charge\x01",
            "of this request, Miss Grace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FThere was a certain probability this would happen.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_75C1")

    ChrTalk(
        0xB,
        (
            "#02103FOh, such a weak reaction!\x02\x03",
            "#02100FWe get to work together again!\x01",
            "Can't you be a little happier?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FAhaha... Last time you had us going back\x01",
            "and forth across all of Crossbell, though.\x02\x03",
            "#00105FAnd, what kind of\x01",
            "request is this time?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76B7")

    label("loc_75C1")


    ChrTalk(
        0xB,
        (
            "#02103FOh, such a weak reaction!\x02\x03",
            "#02100FWe get to work together!\x01",
            "Be a little happier!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FA-Ahaha... It feels like\x01",
            "things are always tougher when we\x01",
            "get involved with you, Miss Grace.\x02\x03",
            "#00105FAnd, what kind of\x01",
            "request is this time?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76B7")


    ChrTalk(
        0x105,
        (
            "#10300FSomething about helping with\x01",
            "coverage for a gourmet guide...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)

    ChrTalk(
        0xB,
        (
            "#02100FYes, exactly.\x02\x03",
            "#02104FAwhile back, saying "We want to do something \x01",
            "following the example of Mayor Dieter", I got a\x01",
            "proposal from the Crossbell Merchants Association.\x02\x03",
            "#02102FThey wanted to cooperate\x01",
            "with Crossbell News and\x01",
            "make a gourmet guide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FCooperate with the Merchants Association?\x01",
            "What specifically do they want you to do?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x2)

    ChrTalk(
        0xB,
        (
            "#02104FBasically, they want to introduce the restaurants \x01",
            "of the autonomous state of Crossbell\x02\x03",
            "#02100FIn addition to coverage,\x01",
            "they're going to offer\x01",
            "a discount service.\x02\x03",
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
            "#02109F──So! Now let's get\x01",
            "to the point...\x02\x03",
            "#02100FOne of them is about \x01",
            ""gourmet recommendations \x01",
            "by those famous persons".\x02\x03",
            "#02104FIBC's Miss Mariabell,\x01",
            "Arc-en-ciel's Ilya,\x01",
            "Theodore and Eugene...\x02\x03",
            "#02102FWe want to introduce people\x01",
            "to these Crossbell\x01",
            "celebrities' favorite dishes.\x02\x03",
            "#02109FAnd that's where\x01",
            "you guys come in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FHmm... So that is the request this time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FThat does seem interesting, but...\x02\x03",
            "#00105FIs it really ok to put us\x01",
            "in a lineup like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FI know, right? I'm happy to\x01",
            "stand shoulder-to-shoulder with\x01",
            "Miss Ilya and Miss Mariabell, but...\x02\x03",
            "#00301FIf we're in your article,\x01",
            "I don't think it'd catch\x01",
            "much attention.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHu hu, is that a\x01",
            "nice way of saying\x01",
            "we're spoilers?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#02105FNon, non. \x01",
            "Nothing of the sort!\x02\x03",
            "#02102FLately, you guy have gotten more\x01",
            "honest-to-goodness fans, you know?\x02\x03",
            "#02109FSo much that we even get requests\x01",
            "of people who want intense photos\x01",
            "of the SSS members' private life㈱\x02",
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
        (
            "#00106FA-As you'd expect,\x01",
            "we wouldn't want that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02100FUh uh. Anyway, you guys\x01",
            "are attracting attention\x01",
            "in your own way.\x02\x03",
            "#02104FIf it wasn't the case, then I'd never have asked\x01",
            "for your help with this request in the first place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FAlright, I think I get it.\x02\x03",
            "#00000FSo, how should we proceed with this, specifically?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02102FUhuhu. Let me explain\x01",
            "how to do your coverage.\x02\x03",
            "#02104FFirst, you need to go to\x01",
            "each restaurant or cart and\x01",
            "actually eat their food.\x02\x03",
            "#02109FAnd among each of them, I want\x01",
            "you to find a dish that makes\x01",
            "you think "This is it!".\x02\x03",
            "#02102FAfter that, I'll have you\x01",
            "write your own article\x01",
            "here at Crossbell News.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FSo we've got to go to restaurants\x01",
            "throughout the autonomous state and\x01",
            "find dishes that each of us like.\x02\x03",
            "#10105FBut, what if we can't find anything?\x02",
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
            "#2100FBut ideally, I'd like each\x01",
            "of you to introduce readers\x01",
            "to your favorite dish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FHmm, so we've got to\x01",
            "go to at least six\x01",
            "different places, huh.\x02\x03",
            "#00300FAnything we should\x01",
            "watch out for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02103FHmm, let me think...\x02\x03",
            "#02105FOh, the establishments\x01",
            "and Michelam and all\x01",
            ""bars" are off limits...\x02\x03",
            "#02102FI'd like you to cover\x01",
            "areas other than those.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FHmm, then "Trinity"\x01",
            "in Downtown is off\x01",
            "limits too.\x02\x03",
            "#10300FHu hu. And it was such a good\x01",
            "chance to get more business.\x01",
            "Abbas will be sad.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)

    ChrTalk(
        0xB,
        (
            "#02109FWell, sorry, Wazy! \x01",
            "I'll handle covering\x01",
            "that area.\x02\x03",
            "#02104F...Oh, and I've already spoken with all\x01",
            "the restaurants, so there's no need to\x01",
            "worry about paying for your food.\x02\x03",
            "#02102FIf you explain the situation,\x01",
            "they'll show you their sampler menu.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FAnyway, we'll be fine if we just\x01",
            "visit six stores, bars excepted.\x02\x03",
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
            "#02104FUh uh. This isn't a rush job,\x01",
            "but please do your best on it.\x02\x03",
            "#02100FOnce you're finished, come report\x01",
            "to me here at Crossbell News.\x02\x03",
            "#02109FIf I'm not here for some reason,\x01",
            "just ask Tria, our receptionist.\x01",
            "I'll come running at once!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FAlright, understood.\x01",
            "Let's begin now.\x02",
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
            "Quest [Gourmet Guide Coverage]\x07\x00",
            " started!\x02",
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

    # Function_21_730B end

    def Function_22_876F(): pass

    label("Function_22_876F")

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
        "Nice work, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It looks like you have gone\x01",
            "to six different places for\x01",
            "the gourmet guide coverage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Are you ready to\x01",
            "report to Miss Grace?\x02",
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
            "Do Not Report Yet\x01",      # 0
            "Report to Grace\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8993")

    ChrTalk(
        0x8,
        "Understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'll call Miss Grace for\x01",
            "you. Please wait for her\x01",
            "on the 2nd floor.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jump("loc_8A0E")

    label("loc_8993")


    ChrTalk(
        0x8,
        "My, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In that case, please come again\x01",
            "when you're ready to report.\x02",
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

    label("loc_8A0E")

    Return()

    # Function_22_876F end

    def Function_23_8A0F(): pass

    label("Function_23_8A0F")

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
            "#02102FHow did collecting materials for\x01",
            "the "gourmet recommendations" go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, well...\x01",
            "We enjoyed it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FI'm tired though. All those\x01",
            "places are so far apart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02100FUh uh, well, aren't you glad you\x01",
            "had your fill of delicious food?\x02\x03",
            "#02109FAlright then, show\x01",
            "me what you've got.\x02",
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
            "Lloyd and the others reported about\x01",
            "the establishments they visited.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_8CAC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8CAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_8CBF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8CBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_8CD2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8CD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_8CE5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8CE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_8CF8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8CF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_8D0B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8D0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_8D1E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8D1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_8D31")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8D31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_8D44")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8D44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_8D57")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8D57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_8D6A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8D6A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E55")

    ChrTalk(
        0xB,
        (
            "#02104FHmm, so you went to eleven\x01",
            "places in all, did you.\x02\x03",
            "#02109FThis looks like very\x01",
            "thorough coverage!\x01",
            "Uh uh, bis sis here is so happy!\x02\x03",
            "#02102FThen next... Among them,\x01",
            "tell me your gourmet\x01",
            "recommendations!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9271")

    label("loc_8E55")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F1B")

    ChrTalk(
        0xB,
        (
            "#02104FHmm, so you went to ten\x01",
            "places in all, did you.\x02\x03",
            "#02102FUh uh, this looks\x01",
            "like solid coverage.\x02\x03",
            "#02100FThen next... Among them,\x01",
            "tell me your gourmet\x01",
            "recommendations!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9271")

    label("loc_8F1B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FF3")

    ChrTalk(
        0xB,
        (
            "#02104FHmm, so you went to nine\x01",
            "places in all, did you.\x02\x03",
            "#02102FUh uh, looks like this'll be\x01",
            "some nice coverage for me.\x02\x03",
            "#02100FThen next... Among them,\x01",
            "tell me your gourmet\x01",
            "recommendations!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9271")

    label("loc_8FF3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90CC")

    ChrTalk(
        0xB,
        (
            "#02104FHmm, so you went to eight\x01",
            "places in all, did you.\x02\x03",
            "#02102FUh uh, looks like this'll be\x01",
            "some nice coverage for me.\x02\x03",
            "#02100FThen next... Among them,\x01",
            "tell me your gourmet\x01",
            "recommendations!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9271")

    label("loc_90CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_91A5")

    ChrTalk(
        0xB,
        (
            "#02104FHmm, so you went to seven\x01",
            "places in all, did you.\x02\x03",
            "#02102FUh uh, looks like this'll be\x01",
            "some nice coverage for me.\x02\x03",
            "#02100FThen next... Among them,\x01",
            "tell me your gourmet\x01",
            "recommendations!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9271")

    label("loc_91A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9271")

    ChrTalk(
        0xB,
        (
            "#02104FHmm, you went six\x01",
            "places in all, did you.\x02\x03",
            "#02102FUh uh, looks like this'll be\x01",
            "some nice coverage for me.\x02\x03",
            "#02100FThen next... Among them,\x01",
            "tell me your gourmet\x01",
            "recommendations!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9271")

    Fade(500)
    OP_68(58050, 1900, 10380, 0)
    MoveCamera(12, 26, -1, 0)
    OP_6E(400, 0)
    SetCameraDistance(17470, 0)
    OP_0D()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_93C4")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000FMine was "Chef's Omelet Rice"\x01",
            "from the "Ash Tree" Inn\x01",
            "in Armorica Village.\x02\x03",
            "#00002FThe simple flavor characteristic of\x01",
            "Armorica Village touched on my heartstrings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02102FI see. That omelet rice is indeed\x01",
            "something you can only taste there!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_93C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_94DB")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x102,
        (
            "#00104FMine was "Three-Day Stew" from\x01",
            "the auberge "Le Rekuche"\x01",
            "at St. Ursula Hospital.\x02\x03",
            "#00109FIt's melty due to being cooked for a long\x01",
            "time, and good for you on top of that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02109FYes, yes! Eating that stew will\x01",
            "recover your energy in an instant!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_94DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_9636")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x103,
        (
            "#00204FI recommend "Sherbert "Seven Colors"" from \x01",
            "the ice cream stand in Entertainment District.\x02\x03",
            "#00202FIt has an interesting mouthfeel, and the\x01",
            "taste of its seven colors... It is a\x01",
            "masterpiece that defies simple explanation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02105FOh, that's high praise coming from you,\x01",
            "Tio! I'm sure it will be very popular now!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9636")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_9771")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x104,
        (
            "#00300FFor me it's the "Heavenly Noodles "Sun""\x01",
            "at the Waterfront Area noodle stand.\x02\x03",
            "#00309FThe combination of firm, curly noodles\x01",
            "and salty soup... Just rememberin' its\x01",
            "flavor makes me drool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02104FYes, I see. I often go there\x01",
            "for lunch. The cart's owner\x01",
            "dedication is out of scale!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9771")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_9879")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x109,
        (
            "#10107FMine is the "Peerless Fried Rice" from\x01",
            ""The Old Dragon Inn" on East Street.\x02\x03",
            "#10104FOnce I tasted its simple yet deep\x01",
            "flavor, I couldn't get enough!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02109FThat's Zanghui's specialty!\x01",
            "Hmm, now I think I want to\x01",
            "eat there again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9879")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_99B4")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x105,
        (
            "#10304FMy recommendation is the "Rich Sea Hot\x01",
            "Pot" from the Tangram Gate mess hall.\x02\x03",
            "#10302FIt tastes good and everyone can enjoy it\x01",
            "together. I can't think of anything better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02102FThe border gates mess halls are\x01",
            "hidden gourmet spots indeed!\x01",
            "Uh uh, you really know your stuff, Wazy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_99B4")


    ChrTalk(
        0x101,
        "#00004F...So, that's about it.\x01\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9B9E")
    OP_2C(0x80, 0x2)
    OP_63(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#02102FYeah. It looks like each of\x01",
            "your members found a\x01",
            ""gourmet recommendation" for me.\x02\x03",
            "#02104FThis will improve the gourmet\x01",
            "guide feature page a lot.\x02\x03",
            "#02109FThanks you guys!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FHa ha, we should be thanking you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202FIt was worth it going to all those places.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02105FWhoops, your work's not yet done.\x02\x03",
            "#02102FI've got to have each of you\x01",
            "write up an introduction comment!\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x80, 0x1, 0xF)
    Jump("loc_9F28")

    label("loc_9B9E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9D82")
    OP_2C(0x80, 0x1)

    ChrTalk(
        0xB,
        (
            "#02106FHmm. As expected, not all\x01",
            "of you found a "gourmet\x01",
            "recommendation", huh.\x02\x03",
            "#02102FBut well, I guess you pass.\x01",
            "I'll thank you for now.\x02",
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
            "#00206F(Maybe it would have been better\x01",
            "if we tried a little harder...)\x02",
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
    Jump("loc_9F28")

    label("loc_9D82")

    OP_63(0xB, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#02105FH-Huh? These are all the "gourmet\x01",
            "recommendations" you've found?\x02\x03",
            "#02106FHmm, I guess it can't be helped...\x01",
            "Maybe you should've tried a little harder.\x02",
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
        "#00206F(Maybe we could have done a bit more...)\x02",
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

    label("loc_9F28")

    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "After that, Lloyd and the others had\x01",
            "difficulty with the writing because\x01",
            "they weren't accustomed to it...\x07\x00\x02",
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
            "Somehow, the "gourmet recommendations"\x01",
            "article for the gourmet guide was completed.\x07\x00\x01\x02",
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
            "#02100FHmm, I think that should do it.\x02\x03",
            "#02104FWe'll proof this ourselves\x01",
            "later. It's ok for now!\x02\x03",
            "#02102FUh uh, I think we'll be able to\x01",
            "make an interesting gourmet\x01",
            "guide thanks to all of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FAhaha. That was really tough...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FThen, the request\x01",
            "is complete?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02104FYes. Thanks for your help, guys.\x02\x03",
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
        "#00000FYes. Excuse us, then.\x02",
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
            "Quest [Gourmet Guide Coverage]\x07\x00",
            " complete!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 6)
    OP_29(0x80, 0x1, 0x12)
    OP_29(0x80, 0x4, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_A2CF")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A2CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_A2E1")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A2E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_A2F3")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A2F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_A305")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A305")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_A317")
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A317")

    SetChrFlags(0xB, 0x80)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -6370, 250, 2630, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_23_8A0F end

    def Function_24_A348(): pass

    label("Function_24_A348")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A352")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A798")
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_A384")
    MenuCmd(1, 1, "★Fairy Gelato")
    Jump("loc_A394")

    label("loc_A384")

    MenuCmd(1, 1, "Fairy Gelato")

    label("loc_A394")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_A3B7")
    MenuCmd(1, 1, "★Phoenix Noodles")
    Jump("loc_A3CA")

    label("loc_A3B7")

    MenuCmd(1, 1, "Phoenix Noodles")

    label("loc_A3CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_A3F4")
    MenuCmd(1, 1, "★Satisfying Basil Pasta")
    Jump("loc_A40E")

    label("loc_A3F4")

    MenuCmd(1, 1, "Satisfying Basil Pasta")

    label("loc_A40E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_A434")
    MenuCmd(1, 1, "★Bitter Tomato Soda")
    Jump("loc_A44A")

    label("loc_A434")

    MenuCmd(1, 1, "Bitter Tomato Soda")

    label("loc_A44A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_A46D")
    MenuCmd(1, 1, "★Spicy Mapo Tofu")
    Jump("loc_A480")

    label("loc_A46D")

    MenuCmd(1, 1, "Spicy Mapo Tofu")

    label("loc_A480")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_A4A4")
    MenuCmd(1, 1, "★Sunset Croissant")
    Jump("loc_A4B8")

    label("loc_A4A4")

    MenuCmd(1, 1, "Sunset Croissant")

    label("loc_A4B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_A4DE")
    MenuCmd(1, 1, "★Chef's Omelet Rice")
    Jump("loc_A4F4")

    label("loc_A4DE")

    MenuCmd(1, 1, "Chef's Omelet Rice")

    label("loc_A4F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_A51B")
    MenuCmd(1, 1, "★Thick Stamina Steak")
    Jump("loc_A532")

    label("loc_A51B")

    MenuCmd(1, 1, "Thick Stamina Steak")

    label("loc_A532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_A55B")
    MenuCmd(1, 1, "★Slow-Cooked Beef Stew")
    Jump("loc_A574")

    label("loc_A55B")

    MenuCmd(1, 1, "Slow-Cooked Beef Stew")

    label("loc_A574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_A59F")
    MenuCmd(1, 1, "★Addictive Curry Hot Pot")
    Jump("loc_A5BA")

    label("loc_A59F")

    MenuCmd(1, 1, "Addictive Curry Hot Pot")

    label("loc_A5BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_A5E3")
    MenuCmd(1, 1, "★Rich Soy Milk Hot Pot")
    Jump("loc_A5FC")

    label("loc_A5E3")

    MenuCmd(1, 1, "Rich Soy Milk Hot Pot")

    label("loc_A5FC")

    MenuCmd(1, 1, "Quit")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 0)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A671"),
        (1, "loc_A68A"),
        (2, "loc_A6A3"),
        (3, "loc_A6BC"),
        (4, "loc_A6D5"),
        (5, "loc_A6EE"),
        (6, "loc_A707"),
        (7, "loc_A720"),
        (8, "loc_A739"),
        (9, "loc_A752"),
        (10, "loc_A76B"),
        (11, "loc_A784"),
        (SWITCH_DEFAULT, "loc_A793"),
    )


    label("loc_A671")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_A682")
    ClearScenarioFlags(0x172, 1)
    Jump("loc_A685")

    label("loc_A682")

    SetScenarioFlags(0x172, 1)

    label("loc_A685")

    Jump("loc_A793")

    label("loc_A68A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_A69B")
    ClearScenarioFlags(0x172, 2)
    Jump("loc_A69E")

    label("loc_A69B")

    SetScenarioFlags(0x172, 2)

    label("loc_A69E")

    Jump("loc_A793")

    label("loc_A6A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_A6B4")
    ClearScenarioFlags(0x172, 3)
    Jump("loc_A6B7")

    label("loc_A6B4")

    SetScenarioFlags(0x172, 3)

    label("loc_A6B7")

    Jump("loc_A793")

    label("loc_A6BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_A6CD")
    ClearScenarioFlags(0x172, 4)
    Jump("loc_A6D0")

    label("loc_A6CD")

    SetScenarioFlags(0x172, 4)

    label("loc_A6D0")

    Jump("loc_A793")

    label("loc_A6D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_A6E6")
    ClearScenarioFlags(0x172, 5)
    Jump("loc_A6E9")

    label("loc_A6E6")

    SetScenarioFlags(0x172, 5)

    label("loc_A6E9")

    Jump("loc_A793")

    label("loc_A6EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_A6FF")
    ClearScenarioFlags(0x172, 6)
    Jump("loc_A702")

    label("loc_A6FF")

    SetScenarioFlags(0x172, 6)

    label("loc_A702")

    Jump("loc_A793")

    label("loc_A707")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_A718")
    ClearScenarioFlags(0x172, 7)
    Jump("loc_A71B")

    label("loc_A718")

    SetScenarioFlags(0x172, 7)

    label("loc_A71B")

    Jump("loc_A793")

    label("loc_A720")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_A731")
    ClearScenarioFlags(0x173, 0)
    Jump("loc_A734")

    label("loc_A731")

    SetScenarioFlags(0x173, 0)

    label("loc_A734")

    Jump("loc_A793")

    label("loc_A739")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_A74A")
    ClearScenarioFlags(0x173, 1)
    Jump("loc_A74D")

    label("loc_A74A")

    SetScenarioFlags(0x173, 1)

    label("loc_A74D")

    Jump("loc_A793")

    label("loc_A752")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_A763")
    ClearScenarioFlags(0x173, 2)
    Jump("loc_A766")

    label("loc_A763")

    SetScenarioFlags(0x173, 2)

    label("loc_A766")

    Jump("loc_A793")

    label("loc_A76B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_A77C")
    ClearScenarioFlags(0x173, 3)
    Jump("loc_A77F")

    label("loc_A77C")

    SetScenarioFlags(0x173, 3)

    label("loc_A77F")

    Jump("loc_A793")

    label("loc_A784")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A793")

    label("loc_A793")

    Jump("loc_A352")

    label("loc_A798")

    Return()

    # Function_24_A348 end

    def Function_25_A799(): pass

    label("Function_25_A799")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Regarding battlefield coverage of the "Hundred Days\x01",
            "War", over a three-month period, the series of reports\x01",
            "overflowed with honesty and a sense of justice.\x02\x03",
            "To recognize this achievement,\x01",
            "we award the Fulitzer Prize.\x01",
            "S1192, November\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_25_A799 end

    def Function_26_A8B9(): pass

    label("Function_26_A8B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_A8C3")
    Return()

    label("loc_A8C3")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA71")

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

    def lambda_A932():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_A932)
    Sleep(50)

    def lambda_A942():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_A942)
    Sleep(50)

    def lambda_A952():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_A952)
    Sleep(50)

    def lambda_A962():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_A962)
    Sleep(50)

    def lambda_A972():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x4, 2, lambda_A972)
    Sleep(50)

    def lambda_A982():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x5, 2, lambda_A982)
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
        "If you have business there, please speak with me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FS-Sorry.\x01",
            "Pardon us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_AACC")

    label("loc_AA71")


    ChrTalk(
        0x101,
        (
            "#00000FLooks like 2F entry is prohibited. It's\x01",
            "not like we can go up there uninvited.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AACC")

    Sleep(50)
    SetChrPos(0x0, -6370, 20, 2470, 180)
    EventEnd(0x4)
    Return()

    # Function_26_A8B9 end

    def Function_27_AAE3(): pass

    label("Function_27_AAE3")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Back issues of Crossbell Times\x01",
            "are lined up on the shelves.\x02",
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
            "[Quit]\x01",                        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC94")
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
            "[Quit]\x01",                       # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC3F")
    UseItem(0x2BC, 0xFF)

    label("loc_AC3F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC53")
    UseItem(0x2BD, 0xFF)

    label("loc_AC53")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC67")
    UseItem(0x2BE, 0xFF)

    label("loc_AC67")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC7B")
    UseItem(0x2BF, 0xFF)

    label("loc_AC7B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC8F")
    UseItem(0x2C0, 0xFF)

    label("loc_AC8F")

    Jump("loc_AD7E")

    label("loc_AC94")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD75")
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
            "[Quit]\x01",                    # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD34")
    UseItem(0x2C1, 0xFF)

    label("loc_AD34")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD48")
    UseItem(0x2C2, 0xFF)

    label("loc_AD48")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD5C")
    UseItem(0x2C3, 0xFF)

    label("loc_AD5C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD70")
    UseItem(0x2C4, 0xFF)

    label("loc_AD70")

    Jump("loc_AD7E")

    label("loc_AD75")

    FadeToBright(300, 0)

    label("loc_AD7E")

    TalkEnd(0xFF)
    Return()

    # Function_27_AAE3 end

    SaveToFile()

Try(main)
