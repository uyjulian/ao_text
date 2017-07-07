from ScenarioHelper import *

def main():
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
        "Receptionist Tria",           # 1
        "Makkenen",             # 2
        "Raines",               # 3
        "Grace",               # 4
        "Nielsen",             # 5
        "Reporter Noticia",         # 6
        "Editor-in-chief",                 # 7
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
        "Function_5_1BE2",         # 05, 5
        "Function_6_1D8F",         # 06, 6
        "Function_7_1F71",         # 07, 7
        "Function_8_2139",         # 08, 8
        "Function_9_2D70",         # 09, 9
        "Function_10_3000",        # 0A, 10
        "Function_11_3396",        # 0B, 11
        "Function_12_3D95",        # 0C, 12
        "Function_13_4CBB",        # 0D, 13
        "Function_14_4E4C",        # 0E, 14
        "Function_15_5008",        # 0F, 15
        "Function_16_5199",        # 10, 16
        "Function_17_53CC",        # 11, 17
        "Function_18_566B",        # 12, 18
        "Function_19_5FB2",        # 13, 19
        "Function_20_672A",        # 14, 20
        "Function_21_6B8E",        # 15, 21
        "Function_22_7F46",        # 16, 22
        "Function_23_81E2",        # 17, 23
        "Function_24_99FA",        # 18, 24
        "Function_25_9E15",        # 19, 25
        "Function_26_9EE6",        # 1A, 26
        "Function_27_A0FD",        # 1B, 27
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

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A92")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_986")

    ChrTalk(
        0x8,
        (
            "Everyone at the Special Affairs Division ……\x01",
            "Perhaps, on the request of our company\x01",
            "Have you come over?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Actually, the person in charge is in the interview of a derailment accident\x01",
            "I went out … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I am sorry, but I will rerun the day\x01",
            "Thank you for your visiting.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A8E")

    label("loc_986")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_A13")

    ChrTalk(
        0x8,
        (
            "Now, in the editorial department on the second floor\x01",
            "Quick response to train derailment accident\x01",
            "I am performing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To reporters when you need\x01",
            "Please give me a message here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A8E")

    label("loc_A13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_A8E")

    ChrTalk(
        0x8,
        (
            "On the West Crossbell Highway\x01",
            "Derail accident happened … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No wonder, terrorist\x01",
            "It's not like work or not … ….?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A8E")

    TalkEnd(0x8)
    Return()

    label("loc_A92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_END)), "loc_CBB")
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
            "talk\x01",                # 0
            "Report coverage\x01",      # 1
            "quit\x01",                  # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B13")
    TalkEnd(0x8)
    Return()

    label("loc_B13")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_B3F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_B52")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_B65")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_B78")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_B8B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_B9E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_BB1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_BC4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_BD7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_BEA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_BFD")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BFD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C2A")
    TalkEnd(0x8)
    Call(0, 22)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C24")
    Call(0, 23)

    label("loc_C24")

    Return()

    label("loc_C2A")


    ChrTalk(
        0x101,
        (
            "#00005F(Oops, we still have places to eat and drink\x01",
            "It is not more than 6 places. )\x02\x03",
            "#00003F(You can not report it as it is now.\x01",
            "I have to work hard for a while. )\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Return()

    label("loc_CB6")

    Jump("loc_CC9")

    label("loc_CBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC9")
    Call(0, 20)
    Return()

    label("loc_CC9")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_DDE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D7A")

    ChrTalk(
        0x8,
        (
            "Everyone, coverage of gourmet guide\x01",
            "Please do your best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I can eat delicious things,\x01",
            "If you proceed with fun\x01",
            "I think whether it is OK.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD9")

    label("loc_D7A")


    ChrTalk(
        0x8,
        "Everyone, I really appreciate your work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If there is something again,\x01",
            "Thank you for your consideration.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD9")

    Jump("loc_1BDE")

    label("loc_DDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_E85")

    ChrTalk(
        0x8,
        (
            "Raines君、どうやら\x01",
            "I could get into Geo Front\x01",
            "You seem to have escaped difficulties there, do not you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hehu, anyhow safe\x01",
            "It was really nice to be there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BDE")

    label("loc_E85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_E93")
    Jump("loc_1BDE")

    label("loc_E93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_FFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F5D")

    ChrTalk(
        0x8,
        (
            "A military soldier here in the morning\x01",
            "When I came in, I was really surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In just one week from the declaration\x01",
            "It seems that things have moved so far …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To tell the fallen clouds,\x01",
            "That's exactly this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FF8")

    label("loc_F5D")


    ChrTalk(
        0x8,
        (
            "Looking at the state of the city,\x01",
            "Even those who do not change and who support the president\x01",
            "It seems that there are many … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To be honest, I am more embarrassed.\x01",
            "…… What will happen in the future?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FF8")

    Jump("loc_1BDE")

    label("loc_FFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_11BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1125")

    ChrTalk(
        0x8,
        (
            "Reconstruction activities after the incident,\x01",
            "Refugee vote after three days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "These two things,\x01",
            "A sense of unity that is unprecedented in the city\x01",
            "You seem to be born.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Personally, affirm independence\x01",
            "Discussions are strangely glowing\x01",
            "I am worried about the state … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Considering citizen emotion,\x01",
            "It can not be helped or it is natural\x01",
            "think.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11B9")

    label("loc_1125")


    ChrTalk(
        0x8,
        (
            "Personally, affirm independence\x01",
            "Discussions are strangely glowing\x01",
            "I am worried about the state … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Considering citizen emotion,\x01",
            "It can not be helped or it is natural\x01",
            "think.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11B9")

    Jump("loc_1BDE")

    label("loc_11BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_11CC")
    Jump("loc_1BDE")

    label("loc_11CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1294")

    ChrTalk(
        0x8,
        (
            "Graceさんたち、昨日はかなり\x01",
            "From the security guard stepping into the person in the field\x01",
            "You seem to have received scolding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I understand the reporter's soul … …\x01",
            "I am worried, I will keep my safety a bit more\x01",
            "I want you to think.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BDE")

    label("loc_1294")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_144A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13BF")

    ChrTalk(
        0x8,
        (
            "Yesterday, in response to a preliminary report on derailment accidents,\x01",
            "I was also busy working to communicate in various fields.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In retrospect, this year more than usual\x01",
            "There are many opportunities to put out the issue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To the extent that outsiders increase with good news\x01",
            "I do not mind doing it, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If it is only news of incidents and accidents,\x01",
            "I feel a little depressed.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1445")

    label("loc_13BF")


    ChrTalk(
        0x8,
        (
            "To the extent that outsiders increase with good news\x01",
            "I do not mind doing it, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If it is only news of incidents and accidents,\x01",
            "I feel a little depressed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1445")

    Jump("loc_1BDE")

    label("loc_144A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_14D7")

    ChrTalk(
        0x8,
        (
            "Now, in the editorial department on the second floor\x01",
            "Quick response to train derailment accident\x01",
            "I am performing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To reporters when you need\x01",
            "Please give me a message here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BDE")

    label("loc_14D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1557")

    ChrTalk(
        0x8,
        (
            "On the West Crossbell Highway\x01",
            "Derail accident happened … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No wonder, terrorist\x01",
            "It's not like work or not … ….?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BDE")

    label("loc_1557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1568")
    Call(0, 6)
    Jump("loc_1BDE")

    label("loc_1568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1797")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16DC")

    ChrTalk(
        0x8,
        (
            "Two days later \"the independence of national independence\"\x01",
            "The theme citizen forum\x01",
            "It is held at the city hall, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This is our proposal,\x01",
            "In a form calling for cooperation to the city\x01",
            "It is a realized project.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since independence advocacy, we have\x01",
            "Ask for judgment standard of referendum\x01",
            "Many readers' voices received ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Is there anything besides articles?\x01",
            "I was able to make a suggestion.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1792")

    label("loc_16DC")


    ChrTalk(
        0x8,
        (
            "Since independence advocacy, we have\x01",
            "Ask for judgment standard of referendum\x01",
            "Many readers' voices received ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Is there anything besides articles?\x01",
            "So that the citizens' forum\x01",
            "I made a suggestion.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1792")

    Jump("loc_1BDE")

    label("loc_1797")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1852")

    ChrTalk(
        0x8,
        (
            "GraceさんとRaines君、\x01",
            "Say suddenly I need shopping\x01",
            "It looks like I headed to a department store … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Nevertheless, it is late for plenary sessions due to it,\x01",
            "…… There is nothing like that, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BDE")

    label("loc_1852")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1863")
    Call(0, 7)
    Jump("loc_1BDE")

    label("loc_1863")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_18E8")

    ChrTalk(
        0x8,
        (
            "At last from tomorrow\x01",
            "The commerce meeting begins.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Reporters also\x01",
            "With the feeling of being busy preparing,\x01",
            "Tension is transmitted.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BDE")

    label("loc_18E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1AC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A1C")

    ChrTalk(
        0x8,
        (
            "Raines君、何でも今日は\x01",
            "It seems that he will accompany the investigation of the ruins.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I am sorry that no obedient assistant\x01",
            "Graceさんがぼやいてましたけど……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "よく考えると、Raines君って\x01",
            "I just entered this year, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Nevertheless\x01",
            "I was counted on various things\x01",
            "I think that it is really wonderful thing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1ABC")

    label("loc_1A1C")


    ChrTalk(
        0x8,
        (
            "Everyone tends to forget\x01",
            "Raines君って、まだ今年\x01",
            "I just entered the company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Nevertheless\x01",
            "I was counted on various things\x01",
            "I think that it is really wonderful thing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ABC")

    Jump("loc_1BDE")

    label("loc_1AC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1BDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B63")

    ChrTalk(
        0x8,
        (
            "Oh, it's been a long time.\x01",
            "Are you a member of the Special Affairs Division?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Welcome to Crossbell Communication Company.\x01",
            "If you have something,\x01",
            "Please do not hesitate to ask me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BDE")

    label("loc_1B63")


    ChrTalk(
        0x8,
        (
            "Huhu, everyone's activities\x01",
            "When it comes to restart\x01",
            "Graceさんも喜びますね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you have something,\x01",
            "Please do not hesitate to ask me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BDE")

    TalkEnd(0x8)
    Return()

    # Function_4_867 end

    def Function_5_1BE2(): pass

    label("Function_5_1BE2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1C8C")

    ChrTalk(
        0xFE,
        (
            "Raines君、どうやら\x01",
            "I could get into Geo Front\x01",
            "You seem to have escaped difficulties there, do not you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehu, anyhow safe\x01",
            "It was really nice to be there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D8B")

    label("loc_1C8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1D26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CAB")
    TalkEnd(0xFE)
    Call(0, 18)
    Return()

    label("loc_1CAB")


    ChrTalk(
        0xFE,
        (
            "Raines君、本当に無茶を\x01",
            "I hope I do not have it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, it's safe\x01",
            "I pray for being there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D8B")

    label("loc_1D26")


    ChrTalk(
        0xFE,
        (
            "Oh, everyone.\x01",
            "Come in this side\x01",
            "It's useless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it is good, over the counter\x01",
            "Tell me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D8B")

    TalkEnd(0xFE)
    Return()

    # Function_5_1BE2 end

    def Function_6_1D8F(): pass

    label("Function_6_1D8F")

    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ECD")

    ChrTalk(
        0xD,
        (
            "Well, that's right.\x01",
            "I was thinking today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "By the way, today\x01",
            "Because it is the direction of Mainz mining town\x01",
            "Whether it will be late for returning ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As I expected to see you again\x01",
            "The one who left the message\x01",
            "I think whether it is OK.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Well, that's true.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Well then,\x01",
            "I wonder if I can make a message.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Yes, I got it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F6C")

    label("loc_1ECD")


    ChrTalk(
        0x8,
        (
            "In the meantime,\x01",
            "May I ask you a question?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Yeah, Ryu Old Hotel in east street.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If you get in touch,\x01",
            "You are going to get up soon.\x01",
            "I wonder if you can tell.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F6C")

    OP_4C(0xD, 0xFF)
    Return()

    # Function_6_1D8F end

    def Function_7_1F71(): pass

    label("Function_7_1F71")

    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20BB")

    ChrTalk(
        0xD,
        (
            "Well, sorry.\x01",
            "じゃあNielsenさんは\x01",
            "You are out of the house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Sorry, basically\x01",
            "Those who are in the telecommunications company\x01",
            "It is few people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Today when I go to see my friend\x01",
            "As I mentioned,\x01",
            "Shall I take your message?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "No, that's fine.\x01",
            "Just talking about time\x01",
            "It is bad to have you go for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I will have another opportunity.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2134")

    label("loc_20BB")


    ChrTalk(
        0xD,
        (
            "As it is,\x01",
            "Editor-in-chiefに挨拶をしたいんだけど\x01",
            "I wonder if it is okay now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, I will contact you now.\x01",
            "Please wait a moment.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2134")

    OP_4C(0xD, 0xFF)
    Return()

    # Function_7_1F71 end

    def Function_8_2139(): pass

    label("Function_8_2139")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_214A")
    Jump("loc_2D6C")

    label("loc_214A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2158")
    Jump("loc_2D6C")

    label("loc_2158")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_21EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2173")
    Call(0, 9)
    Jump("loc_21E5")

    label("loc_2173")

    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xB,
        (
            "#02100Fそれじゃ、Raines君は\x01",
            "Please continue to negotiate with the Defense Forces.\x02\x03",
            "If something happens, contact me soon.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)

    label("loc_21E5")

    Jump("loc_2D6C")

    label("loc_21EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_21F8")
    Jump("loc_2D6C")

    label("loc_21F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2295")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2217")
    TalkEnd(0xFE)
    Call(0, 19)
    Return()

    label("loc_2217")


    ChrTalk(
        0xB,
        (
            "#02100FLloyd guys,\x01",
            "Be careful again.\x02\x03",
            "#02109Fand again,\x01",
            "The mission support department works\x01",
            "Let me write an article!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D6C")

    label("loc_2295")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_24CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2435")

    ChrTalk(
        0xB,
        (
            "#02100FOh, Lloyd guys.\x01",
            "Good work till late yesterday.\x02\x03",
            "#02101FSince then……\x01",
            "Did you know something about Wald?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FOh my …\x02\x03",
            "#00001FI went to Ignis this morning,\x01",
            "I could not get any information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02103Fso……\x02\x03",
            "#02102FWell, even here is this\x01",
            "I will get it hit variously.\x02\x03",
            "#02100FAnd then, you also …\x01",
            "Do not think too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304FHuhu, thank you for your concern.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x171, 1)
    Jump("loc_24C8")

    label("loc_2435")


    ChrTalk(
        0xB,
        (
            "#02101FEven so ……\x01",
            "I am also worried about the blue flowers.\x02\x03",
            "#02103FIn addition to that Joachim\x01",
            "If there were people who could make medicine ……\x01",
            "It is going to be quite a nasty story.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24C8")

    Jump("loc_2D6C")

    label("loc_24CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_24DB")
    Jump("loc_2D6C")

    label("loc_24DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2885")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_273D")

    ChrTalk(
        0xB,
        (
            "#02104FWell, the dress in the morning is calm.\x02\x03",
            "#02102FIf you do not mind, how about Lloyd guys as well?\x01",
            "Although it is just can coffee.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh,\x01",
            "I will just let you feel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02102FOh yeah?\x01",
            "Hehe, it's okay though.\x02\x03",
            "#02104FTentatively,\x01",
            "Yesterday, \"Iranian Beast\" exterminating people,\x01",
            "It seems to be good work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FSure it is ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F… … As usual, my ear is early.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02109FWell, well, thank you for that\x01",
            "It is making seeds of rice.\x02\x03",
            "#02100FAnyway, again\x01",
            "Good luck not to get injured.\x02\x03",
            "#02102FAnyway,\x01",
            "Because each other's body is capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, thank you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x171, 2)
    Jump("loc_2880")

    label("loc_273D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27E6")

    ChrTalk(
        0xB,
        (
            "#02103FAnyway, \"Phantom beast\" Hey.\x01",
            "I do not really understand it,\x01",
            "There is nothing to say but it's strange.\x02\x03",
            "#02100FLloyd's guys, too\x01",
            "Good luck not to get injured.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2863")

    label("loc_27E6")


    ChrTalk(
        0xB,
        (
            "#02100FOh, that's right.\x01",
            "Once a sticky gourmet is gathered\x01",
            "I will ask the receptionist to report.\x02\x03",
            "#02109FWell then, I asked for your best regards ~ ♪\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 2)

    label("loc_2863")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2880")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2880")
    ClearScenarioFlags(0x0, 2)

    label("loc_2880")

    Jump("loc_2D6C")

    label("loc_2885")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2893")
    Jump("loc_2D6C")

    label("loc_2893")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_28A1")
    Jump("loc_2D6C")

    label("loc_28A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_28AF")
    Jump("loc_2D6C")

    label("loc_28AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2953")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28CA")
    Call(0, 10)
    Jump("loc_294E")

    label("loc_28CA")


    ChrTalk(
        0xB,
        (
            "#02102FOh, this is a hot topic now\x01",
            "It is a guy of \"Snow Hall\".\x02\x03",
            "#02109FThank you very much.\x01",
            "I once wanted to try it ~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_294E")

    Jump("loc_2D6C")

    label("loc_2953")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2D63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CD2")

    ChrTalk(
        0xB,
        (
            "#02102FOh, Lloyd guys.\x01",
            "Yesterday was the first time ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FHaha, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FSince then\x01",
            "How was the black month 's survey?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02106FWell, it's partly funny.\x02\x03",
            "#02100FFor other bidders as well\x01",
            "I've looked it up all the way … ….\x02\x03",
            "As long as there is nothing extraordinary,\x01",
            "That area is like this\x01",
            "I think it will be the one of the black moon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10103FIs that so……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02106FWell, any further\x01",
            "When the lid is actually opened\x01",
            "I can not tell you anything.\x02\x03",
            "#02100FThat's why I am\x01",
            "Today I was going to work\x01",
            "I am planning to clean them all together.\x02\x03",
            "#02102FOh yes, the Special Affairs Division's\x01",
            "Regarding the restart\x01",
            "Because I will make it an article.\x02\x03",
            "#02109FPictures you want to use\x01",
            "If there are comments,\x01",
            "Please tell me inside now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FHuh, if you are from me\x01",
            "I use it in a host club\x01",
            "I might as well offer it in the photograph.\x02",
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
        "#00006F… … Please stop me please.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13E, 3)
    Jump("loc_2D5E")

    label("loc_2CD2")


    ChrTalk(
        0xB,
        (
            "#02106FFuu, but only on such a day\x01",
            "Raines君が外出中だなんてね。\x02\x03",
            "Yeah\x01",
            "I was going to press it … ….\x01",
            "Sorry it can not be helped.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D5E")

    Jump("loc_2D6C")

    label("loc_2D63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2D6C")

    label("loc_2D6C")

    TalkEnd(0xFE)
    Return()

    # Function_8_2139 end

    def Function_9_2D70(): pass

    label("Function_9_2D70")

    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0xB, 0x0, 0)
    TurnDirection(0xA, 0x0, 0)

    ChrTalk(
        0xB,
        (
            "#02101FOh, Lloyd guys.\x01",
            "You naturally saw the presidential speech.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FYes, please contact me\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FGraceさんたちは\x01",
            "What are you going to do now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02103FYeah, anyway\x01",
            "Anyway, I will be struggling with coverage activities.\x02\x03",
            "#02101FAgain for the Defense Forces\x01",
            "Contact us to tell us a specific story\x01",
            "Of course to withdraw … …\x02\x03",
            "You go out into the city and collect the voices of citizens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Afterwards to foreign media\x01",
            "It's response and response research.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Now also the international communication equipment on the second floor\x01",
            "It is in full operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203FI see, I heard you are busy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02104FWell ~.\x01",
            "I think there are various kinds there, too\x01",
            "Let's do everything we can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, that's OK.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18F, 2)
    OP_93(0xB, 0x10E, 0x0)
    OP_93(0xA, 0x5A, 0x0)
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_9_2D70 end

    def Function_10_3000(): pass

    label("Function_10_3000")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xB,
        (
            "#02109Fふふ、Nielsenさん。\x01",
            "Finally I could see you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Well, I was looking forward to it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "by the way,\x01",
            "Editor-in-chiefから伺っていますよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "この３年で、Grace君がとても\x01",
            "You made it strong.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xB)

    ChrTalk(
        0xB,
        (
            "#02109FSuch a thing, I am still too much.\x02\x03",
            "#02104FAs you always want\x01",
            "I just do it ……\x01",
            "I mean they only do what they like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Haha, do it.\x01",
            "Being able to enjoy work\x01",
            "Is not there anything wrong?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3264")

    ChrTalk(
        0x101,
        (
            "#00000F（Graceさん……\x01",
            "  Nielsenさんの前だと\x01",
            "I feel different from usual. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F(Hehe, that's right.\x01",
            "It might be a little unusual scenery. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_338A")

    label("loc_3264")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 3)), scpexpr(EXPR_END)), "loc_3308")

    ChrTalk(
        0x101,
        (
            "#00000F（Graceさん、なんだか\x01",
            "I feel different from usual. )\x02\x03",
            "#00003F（確かNielsenさんって言ったっけ。\x01",
            "Apparently I'm getting acquainted … …)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_338A")

    label("loc_3308")


    ChrTalk(
        0x101,
        (
            "#00000F（Graceさん、なんだか\x01",
            "I feel different from usual. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(Yes, certainly.\x01",
            "Who is next to me? )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_338A")

    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x148, 1)
    Return()

    # Function_10_3000 end

    def Function_11_3396(): pass

    label("Function_11_3396")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3465")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33B4")
    Call(0, 13)
    Jump("loc_3460")

    label("loc_33B4")


    ChrTalk(
        0xFE,
        (
            "大樹の取材はGrace先輩に任せて\x01",
            "We trend of the government\x01",
            "I will pursue thoroughly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Before two major powers move\x01",
            "How far can you build a system ……\x01",
            "It can not be overlooked.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3460")

    Jump("loc_3D91")

    label("loc_3465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3473")
    Jump("loc_3D91")

    label("loc_3473")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_34F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_348E")
    Call(0, 9)
    Jump("loc_34EF")

    label("loc_348E")

    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xFE,
        "Yes, that's OK.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Graceさんこそ国防軍には\x01",
            "Please do not put too much.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)

    label("loc_34EF")

    Jump("loc_3D91")

    label("loc_34F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3502")
    Jump("loc_3D91")

    label("loc_3502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3590")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3521")
    TalkEnd(0xFE)
    Call(0, 19)
    Return()

    label("loc_3521")


    ChrTalk(
        0xFE,
        (
            "…… \"Red constellation\" is\x01",
            "I listen to someone who is not ordinary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone, in Mainz\x01",
            "Take care when you are headed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D91")

    label("loc_3590")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3618")

    ChrTalk(
        0xFE,
        (
            "For the train accident tentatively\x01",
            "I was fortunate not to become a big mess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Another route of medicine is\x01",
            "I hope I can clarify it … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D91")

    label("loc_3618")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3626")
    Jump("loc_3D91")

    label("loc_3626")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_36AC")

    ChrTalk(
        0xFE,
        "Today is an editorial meeting from morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Recently big news continued\x01",
            "Discussions are often hot,\x01",
            "I'm ready for it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D91")

    label("loc_36AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_36BA")
    Jump("loc_3D91")

    label("loc_36BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_36C8")
    Jump("loc_3D91")

    label("loc_36C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_36D6")
    Jump("loc_3D91")

    label("loc_36D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_36E4")
    Jump("loc_3D91")

    label("loc_36E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_36F2")
    Jump("loc_3D91")

    label("loc_36F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3D91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D27")

    ChrTalk(
        0xFE,
        (
            "That person is a legend of our company ……\x01",
            "After all the great people\x01",
            "It is different from the appearance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Well, I dont wanna.\x01",
            "I have to get the materials and return to the desk quickly.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 500)
    Sleep(200)

    ChrTalk(
        0xFE,
        "Oh, you guys at the Special Affairs Support Division.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005Fあなたは確か、Graceさんと\x01",
            "I often act together ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "ええ、記者のRainesと言います。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……But,\x01",
            "Recently as a photographer\x01",
            "Though it is getting established.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haa, I am a reporter as well as I\x01",
            "I am talking, but grumbling … …\x02",
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
        "#00106FWell, there are various things ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHuff, ideal and reality\x01",
            "It's a gap.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AD8")

    ChrTalk(
        0x101,
        (
            "#00000FUm, by the way,\x01",
            "Graceさんはこちらに？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ああいえ、Grace先輩なら\x01",
            "Today I am going out for interviews.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anything today's interview\x01",
            "One person is more likely to move ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And instead,\x01",
            "Some of my seniors' work\x01",
            "It is a situation that is being pressed on me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, anything with help\x01",
            "I am glad that I can write articles ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C01")

    label("loc_3AD8")


    ChrTalk(
        0x101,
        (
            "#00000FUm, that's right.\x01",
            "Graceさんと会ったんですが\x01",
            "Today is not the same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ええ、Anything today's interview\x01",
            "One person is more likely to move ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And instead,\x01",
            "Some of my seniors' work\x01",
            "It is a situation that is being pressed on me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, anything with help\x01",
            "I am glad that I can write articles ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C01")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        (
            "Oh, while I am doing this\x01",
            "The deadline time …!\x02",
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
        "#10100FWell, it was somewhat disturbing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FPlease, do your best.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    OP_93(0xFE, 0x0, 0x1F4)
    SetScenarioFlags(0x13E, 2)
    Return()

    label("loc_3D27")


    ChrTalk(
        0xFE,
        (
            "Well, one more\x01",
            "Where are the materials necessary for the article?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uu, even while doing this\x01",
            "The deadline time …!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D91")

    TalkEnd(0xFE)
    Return()

    # Function_11_3396 end

    def Function_12_3D95(): pass

    label("Function_12_3D95")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3E34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DB3")
    Call(0, 13)
    Jump("loc_3E2F")

    label("loc_3DB3")


    ChrTalk(
        0xFE,
        (
            "Anyway now, using the foot to inform the information\x01",
            "I will not gather as much as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because I finished my work,\x01",
            "I do not have time to smoke.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E2F")

    Jump("loc_4CB7")

    label("loc_3E34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3F42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E53")
    TalkEnd(0xFE)
    Call(0, 18)
    Return()

    label("loc_3E53")


    ChrTalk(
        0xFE,
        (
            "We are going from now\x01",
            "Graceから得た情報を元に\x01",
            "I am preparing for the breaking news … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Merciless story, now under the regime\x01",
            "It is a thing to write an article on the president's corruption\x01",
            "I can not do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So,\x01",
            "If you are planning to enter\x01",
            "I believe it will go well!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB7")

    label("loc_3F42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_40E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_403D")

    ChrTalk(
        0xFE,
        (
            "Come on, okay …\x01",
            "No matter how much this development\x01",
            "You know it's too quick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honest No matter what happens from now on\x01",
            "No wonder …\x01",
            "It can not be helped just making a noise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, over this\x01",
            "While assuming the worst situation,\x01",
            "I only have to do things.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_40E3")

    label("loc_403D")


    ChrTalk(
        0xFE,
        (
            "To be honest, whatever happens from now on\x01",
            "No wonder …\x01",
            "It can not be helped just making a noise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, over this\x01",
            "While assuming the worst situation,\x01",
            "I only have to do things.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40E3")

    Jump("loc_4CB7")

    label("loc_40E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_41AE")
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xFE,
        (
            "In the meantime the raids of the empire\x01",
            "Rumor that even conspiracy, already among citizens\x01",
            "It seems they are penetrating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it is natural logic,\x01",
            "Is it dangerous to distinguish … ….\x01",
            "I wonder if somehow I can not grasp the truth.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    Jump("loc_4CB7")

    label("loc_41AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_41BC")
    Jump("loc_4CB7")

    label("loc_41BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_42CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_426B")

    ChrTalk(
        0xFE,
        (
            "Apparently the guard\x01",
            "It seems to be quite severe situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then, if occupation continues like this\x01",
            "Eventually the Imperial Army intervened … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, it's a funny smile talk.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_42C6")

    label("loc_426B")


    ChrTalk(
        0xFE,
        (
            "If the occupation continues like this\x01",
            "Eventually the Imperial Army intervened … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, it's a funny smile talk.\x02",
    )

    CloseMessageWindow()

    label("loc_42C6")

    Jump("loc_4CB7")

    label("loc_42CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4415")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_439E")

    ChrTalk(
        0xFE,
        (
            "How about editing breaking news articles?\x01",
            "Every time, I will use my strength physically.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I did not do that when I was in my twenties … …\x01",
            "Recently I feel a lot too tight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Totally, I do not want to get older.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4410")

    label("loc_439E")


    ChrTalk(
        0xFE,
        (
            "Well, I am still in his thirties.\x01",
            "Rather, the prime of work\x01",
            "From now on, keep on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I can not say whining but why.\x02",
    )

    CloseMessageWindow()

    label("loc_4410")

    Jump("loc_4CB7")

    label("loc_4415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4423")
    Jump("loc_4CB7")

    label("loc_4423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4527")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4506")

    ChrTalk(
        0xFE,
        "Super.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, before the meeting\x01",
            "Will you look over the materials again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter what, today\x01",
            "The center of the agenda is about national independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Various elements\x01",
            "Beforehand 込 Mimashita in your head e\x01",
            "We can do a lot of discussions.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4522")

    label("loc_4506")


    ChrTalk(
        0xFE,
        "Well, materials, materials and … …\x02",
    )

    CloseMessageWindow()

    label("loc_4522")

    Jump("loc_4CB7")

    label("loc_4527")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4728")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_468E")

    ChrTalk(
        0xFE,
        (
            "From social problems such as politics and economy\x01",
            "Amusement information on culture and entertainment … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As for the case which reporters of Uchi have,\x01",
            "Variety rich enough to be amazed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If this is a larger correspondent\x01",
            "Each specialized in specialized fields\x01",
            "I have to divide my work in charge … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am emphasizing a small number of elite mobility.\x01",
            "All sorts in one person\x01",
            "Covering is basic.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4723")

    label("loc_468E")


    ChrTalk(
        0xFE,
        (
            "Today is the afternoon coverage\x01",
            "I have about 3 of them … …\x01",
            "The work of the column still remains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, this is a time to have time\x01",
            "Well, I will clean up with Pappa.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4723")

    Jump("loc_4CB7")

    label("loc_4728")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_489D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4825")

    ChrTalk(
        0xFE,
        (
            "On the field of plenary session\x01",
            "To the number of journalists to put directly\x01",
            "There is a limit for each company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From our house,\x01",
            "GraceとRainesの奴を\x01",
            "I am supposed to send it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, the remaining members here\x01",
            "Graceたちの連絡を待って\x01",
            "It is a place to prepare for breaking news.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4898")

    label("loc_4825")


    ChrTalk(
        0xFE,
        (
            "GraceとRainesを\x01",
            "As for the coverage when I made it up\x01",
            "I have a reputation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, if they are\x01",
            "You will do it well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4898")

    Jump("loc_4CB7")

    label("loc_489D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_49D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4961")

    ChrTalk(
        0xFE,
        (
            "今さっきGraceとRainesが\x01",
            "It is where you developed the photos you took.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huh, none of them\x01",
            "Will it be able to take a good picture?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, use it outside the country\x01",
            "To which ones are the pictures unsuccessfully.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_49D3")

    label("loc_4961")


    ChrTalk(
        0xFE,
        (
            "This guy and that guy, later\x01",
            "The right guy looks good as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After narrowing down last\x01",
            "Editor-in-chiefチェックをもらって、っと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49D3")

    Jump("loc_4CB7")

    label("loc_49D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4B82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ACF")

    ChrTalk(
        0xFE,
        (
            "Heck, that much black moon\x01",
            "Even though it moves, eventually\x01",
            "Crimson Shokai?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the first place, there is no real situation\x01",
            "Because the connection can not be known from the bottom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, for some time\x01",
            "It looks like I have to look silent and see a situation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4B7D")

    label("loc_4ACF")


    ChrTalk(
        0xFE,
        (
            "Finally tomorrow\x01",
            "Even though the commerce meeting is starting … …\x01",
            "There is no Kiza smell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, even if I think about it, it does not start.\x01",
            "Anyway, it is related to trade conference\x01",
            "Do not summarize the articles.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B7D")

    Jump("loc_4CB7")

    label("loc_4B82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4C33")

    ChrTalk(
        0xFE,
        (
            "Sue …\x01",
            "Black moon has Rubache?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it turned out to be that way\x01",
            "The empire will not keep silent … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whew … … gradually\x01",
            "I got caught smelling.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB7")

    label("loc_4C33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4CB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C4E")
    Call(0, 15)
    Jump("loc_4CB7")

    label("loc_4C4E")


    ChrTalk(
        0xFE,
        "Well, sorry about that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is this Baumkuchen?\x01",
            "As usual you still like it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CB7")

    TalkEnd(0xFE)
    Return()

    # Function_12_3D95 end

    def Function_13_4CBB(): pass

    label("Function_13_4CBB")

    OP_4B(0xA, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x9,
        (
            "おい、Raines。\x01",
            "Are you ready for the camera?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Yes, it's patched.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "All right, well then\x01",
            "To the Orkis Tower direction\x01",
            "Are you going to cover?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Graceに負けねえように\x01",
            "We also feel guilty!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Okay, okay!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 3)), scpexpr(EXPR_END)), "loc_4E36")

    ChrTalk(
        0x101,
        (
            "#00000F（Rainesさん、記者の仕事も\x01",
            "You are resuming normally. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F(It will be two birds with one stone, but … ….\x01",
            "What a vitality, is not it? )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E36")

    OP_4C(0xA, 0xFF)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 3)
    Return()

    # Function_13_4CBB end

    def Function_14_4E4C(): pass

    label("Function_14_4E4C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4E5D")
    Jump("loc_5004")

    label("loc_4E5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4E6B")
    Jump("loc_5004")

    label("loc_4E6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4E79")
    Jump("loc_5004")

    label("loc_4E79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4E87")
    Jump("loc_5004")

    label("loc_4E87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4E95")
    Jump("loc_5004")

    label("loc_4E95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4EA3")
    Jump("loc_5004")

    label("loc_4EA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4EB1")
    Jump("loc_5004")

    label("loc_4EB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4EBF")
    Jump("loc_5004")

    label("loc_4EBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4ECD")
    Jump("loc_5004")

    label("loc_4ECD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4F5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EE8")
    Call(0, 10)
    Jump("loc_4F5A")

    label("loc_4EE8")


    ChrTalk(
        0xFE,
        (
            "はは、流石はGrace君ですね。\x01",
            "Have you already checked it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I promise--\x01",
            "The cheeks will fall off bitefully.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F5A")

    Jump("loc_5004")

    label("loc_4F5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4F6D")
    Jump("loc_5004")

    label("loc_4F6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5004")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F88")
    Call(0, 15)
    Jump("loc_5004")

    label("loc_4F88")


    ChrTalk(
        0xFE,
        (
            "Oh yeah, to you all\x01",
            "I have given you a souvenir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You found a nice shop in the Republic.\x01",
            "Hehe, you surely like it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5004")

    TalkEnd(0xFE)
    Return()

    # Function_14_4E4C end

    def Function_15_5008(): pass

    label("Function_15_5008")

    OP_4B(0xC, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x9,
        (
            "No, but\x01",
            "It is really a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Since you last came here,\x01",
            "Have you been three years already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Yes, exactly that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Tentatively, for the time being\x01",
            "Here in the form of a special counselor\x01",
            "Because I will come and go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Although I am troubled,\x01",
            "Nice to meet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Oh no, it is not rude.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If there is something, anything\x01",
            "Please do not hesitate to tell me.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x0, 3)
    Return()

    # Function_15_5008 end

    def Function_16_5199(): pass

    label("Function_16_5199")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_51AA")
    Jump("loc_53C8")

    label("loc_51AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_525E")
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Well, regardless of facts,\x01",
            "In any case the empire raids\x01",
            "I will not admit it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For this situation\x01",
            "Next, how the empire goes … …\x01",
            "I guess I have no choice but to watch it.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    Jump("loc_53C8")

    label("loc_525E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_526C")
    Jump("loc_53C8")

    label("loc_526C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_527A")
    Jump("loc_53C8")

    label("loc_527A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_52DF")

    ChrTalk(
        0xFE,
        (
            "Well, the editorial department is even more\x01",
            "It seems to be getting hurried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We should be free now.\x02",
    )

    CloseMessageWindow()
    Jump("loc_53C8")

    label("loc_52DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5365")

    ChrTalk(
        0xFE,
        (
            "On the second floor, we will report\x01",
            "It seems to be in correspondence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To what extent, this noisiness is\x01",
            "I feel the same about any telecommunications company.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53C8")

    label("loc_5365")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5376")
    Call(0, 6)
    Jump("loc_53C8")

    label("loc_5376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5384")
    Jump("loc_53C8")

    label("loc_5384")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5392")
    Jump("loc_53C8")

    label("loc_5392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_53A3")
    Call(0, 7)
    Jump("loc_53C8")

    label("loc_53A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_53B1")
    Jump("loc_53C8")

    label("loc_53B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_53BF")
    Jump("loc_53C8")

    label("loc_53BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_53C8")

    label("loc_53C8")

    TalkEnd(0xFE)
    Return()

    # Function_16_5199 end

    def Function_17_53CC(): pass

    label("Function_17_53CC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_55AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54E1")

    ChrTalk(
        0xFE,
        (
            "Brief report on presidential detention\x01",
            "私とMakkenen君で何とか仕上げて\x01",
            "I was issued in a hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Incidentally, other reporters immediately\x01",
            "I'm in a state of resuming interviews.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今後はGrace君とも\x01",
            "You can get in touch in a dignified manner,\x01",
            "I have to gather new information more and more.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_55A7")

    label("loc_54E1")


    ChrTalk(
        0xFE,
        (
            "今後はGrace君とも\x01",
            "You can get in touch in a dignified manner,\x01",
            "I have to gather new information more and more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To suppress caught upset and confusion\x01",
            "Even one minute or so quickly, accurate information\x01",
            "I will make efforts to be told.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55A7")

    Jump("loc_5667")

    label("loc_55AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5667")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55CB")
    TalkEnd(0xFE)
    Call(0, 18)
    Return()

    label("loc_55CB")


    ChrTalk(
        0xFE,
        (
            "Grace君が\x01",
            "It seems that you are indebted to\x01",
            "I really appreciate to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please be careful further in the future …\x01",
            "And by all means, your success\x01",
            "Let me write an article.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5667")

    TalkEnd(0xFE)
    Return()

    # Function_17_53CC end

    def Function_18_566B(): pass

    label("Function_18_566B")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5715")
    Jump("loc_575F")

    label("loc_5715")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5735")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_575F")

    label("loc_5735")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5755")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_575F")

    label("loc_5755")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_575F")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    ChrTalk(
        0x9,
        "Oh, it is a mission support department?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Everyone, it was well safe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Hmm, I can not say it with a loud voice\x01",
            "You and your circumstances are roughly\x01",
            "Grace君から聞いているよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "About current situation if you do not mind\x01",
            "Have a little information exchange\x01",
            "Does not it matter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FWell, here you are.\x02",
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
            "Indeed … … Then, from now on\x01",
            "Will it rush into the Orkis Tower?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "So, that strategy was successful.\x01",
            "This dictatorship system is over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Want to say a little in the independent ineffective declaration\x01",
            "As soon as I thought it became easier to move\x01",
            "It was this strict guideline.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Since that odd moya began to appear\x01",
            "For some reason communication equipment too\x01",
            "It will be difficult to communicate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FReally,\x01",
            "Normal power communication until ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FPerhaps, to that moja\x01",
            "If some disturbance wave\x01",
            "I guess they are included.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FHmm, I did not manage to do it quickly\x01",
            "The confusion is increasing only.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FOh … That's right.\x02\x03",
            "#00000FBy the way, what I am here\x01",
            "Are you all members?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Oh, everyone else's stuff\x01",
            "I got caught in the destination.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Still, for the most part,\x01",
            "The contact itself is attached … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "ただ１人、Raines君だけ\x01",
            "It is in a state where there is no contact at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "On this occasion\x01",
            "Where and how are you doing …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FRainesさんが……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Well, somewhere in the city\x01",
            "I guess there is no mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Raines君、\x01",
            "Graceさんに感化されて\x01",
            "I hope it does not have to be unreasonable ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "However, he is accustomed to danger so much\x01",
            "I do it, so much\x01",
            "I am not worried, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Well, regardless of this story\x01",
            "No more of your time\x01",
            "I do not seem to be able to take away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Tentatively, we are here\x01",
            "While preparing for breaking news\x01",
            "I pray for martial arts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Always make the strategy successful,\x01",
            "This cramped regime\x01",
            "Even if it is not, break it down!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FOkay, okay!\x02\x03",
            "#00003F（Rainesさんと\x01",
            "I can not get in touch, … …)\x02\x03",
            "#00001F（彼の安否はGraceさんも\x01",
            "I will mind it,\x01",
            "Do you even care about it? )\x02",
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

    # Function_18_566B end

    def Function_19_5FB2(): pass

    label("Function_19_5FB2")

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
        "Everyone in the support section ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02101FLloyd guys,\x01",
            "It became a serious thing.\x02\x03",
            "#02105FThat's right, Randy -\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#02101FWhat happened to Randy?\x01",
            "Did you mean -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00003F…… Well ………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108F……that is………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FExcuse me.\x01",
            "That story on another occasion -\x02\x03",
            "#00003F- Let's go, everyone.\x02",
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
            "#02101FWait a moment, Lloyd!\x02\x03",
            "#02104FI will not pursue it.\x01",
            "Would you like to \"consult\" if you do not mind?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00005FHuh……\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    OP_93(0x102, 0x2D, 0x1F4)

    ChrTalk(
        0x109,
        "#6P#10105FUm, what is that … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02101FFirst of all as a premise ……\x01",
            "Regarding Randy's identity\x01",
            "I know it to a certain extent.\x02\x03",
            "#02103FWhat is it to say,\x01",
            "Eye of doubt as a talk of possibility\x01",
            "I do not mean I do not have it.\x02\x03",
            "#02100FBut at the same time his success in his support department\x01",
            "I have been looking enough at this time,\x01",
            "You certainly trust personally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FGraceさん……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02103FAnd in your reaction\x01",
            "I understand the circumstances.\x02\x03",
            "#02101FRandy is alone\x01",
            "Did you head for Mainz?\x02\x03",
            "To solve this incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00001F… … Do you understand so far?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203F…… As expected,\x01",
            "Crossbell Times'\x01",
            "It is a reporter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02102FHehe, after all, is a star?\x02\x03",
            "#02103FAnd you\x01",
            "To bring him back\x01",
            "Being acting …\x02\x03",
            "#02101FI do not feel like listening,\x01",
            "Of course, there is a corresponding preparedness, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001Fof course!\x01",
            "Because Randy is our friend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00101FYeah, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02104FIndeed, for consultation\x01",
            "I never had to ride.\x02\x03",
            "#02101FIf it is me,\x01",
            "To the end I feel like\x01",
            "I'll make you call out.\x02\x03",
            "#02104F- Beware carefully!\x02\x03",
            "#02109Fand again,\x01",
            "The mission support department works\x01",
            "Let me write an article!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYes, thank you.\x02",
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

    # Function_19_5FB2 end

    def Function_20_672A(): pass

    label("Function_20_672A")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_693E")

    ChrTalk(
        0x8,
        (
            "Welcome.\x01",
            "Welcome to Crossbell Communication Company.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "Oh, everyone is at the Special Affairs Support Division ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHello,\x01",
            "I asked for support request.\x02\x03",
            "About gourmet guide coverage\x01",
            "It is necessary for cooperation … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hehe, come over and come over\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "So, is it soon?\x01",
            "Take the request\x01",
            "Could you please?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x17D, 0)
    Jump("loc_69AB")

    label("loc_693E")


    ChrTalk(
        0x8,
        (
            "Thank you for coming all the way\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Is it soon?\x01",
            "Take the request\x01",
            "Could you please?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69AB")

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
            "undertake\x01",      # 0
            "quit\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6AB2")

    ChrTalk(
        0x101,
        "#00000FYeah, I will underwrite it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Certainly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "On the request from the person in charge\x01",
            "As I will explain,\x01",
            "Please wait at the 2nd floor.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 21)
    Jump("loc_6B8D")

    label("loc_6AB2")


    ChrTalk(
        0x101,
        (
            "#00006FSorry, now I have other\x01",
            "There was errands ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, is that so ……\x01",
            "Well then, we are waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you receive a request\x01",
            "Please come as soon as possible.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 2700, 20, -2000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)

    label("loc_6B8D")

    Return()

    # Function_20_672A end

    def Function_21_6B8E(): pass

    label("Function_21_6B8E")

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
            "#02100FHalo Hello ♪\x01",
            "Everyone in the Special Affairs Division.\x02\x03",
            "#02109FThank you for waiting\x01",
            "Sorry about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FAs expected after all …\x01",
            "Graceさんでしたか。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FI had some expectation.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6E09")

    ChrTalk(
        0xB,
        (
            "#02103FIt is already thin reaction.\x02\x03",
            "#02100FI can work together again,\x01",
            "You may be more pleased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FHaha … when … before\x01",
            "It was hard work around the crossbell.\x02\x03",
            "#00105FSo this time\x01",
            "What kind of request is it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F03")

    label("loc_6E09")


    ChrTalk(
        0xB,
        (
            "#02103FIt is already thin reaction.\x02\x03",
            "#02100FI can work with them all the time,\x01",
            "You may be more pleased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FOh, haha ….\x01",
            "Graceさんが関わっているとなると\x01",
            "It seems to be quite difficult.\x02\x03",
            "#00105FSo this time\x01",
            "What kind of request is it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F03")


    ChrTalk(
        0x105,
        (
            "#10300FTo be sure, gourmet guide coverage\x01",
            "I was talking about cooperation.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)

    ChrTalk(
        0xB,
        (
            "#02100FYes, you are right.\x02\x03",
            "#02104FA while ago, \"Mayor of Dieter\x01",
            "I want to do something because I am momentuming \"\x01",
            "There is a proposal from Cross Bell Chamber of Commerce.\x02\x03",
            "#02102FThe communications company also caught up with it,\x01",
            "Gourmet guide jointly\x01",
            "I decided to make it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FJointly with the Chamber of Commerce ……\x01",
            "What exactly do you do?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x2)

    ChrTalk(
        0xB,
        (
            "#02104FBasically, within the cross-bell autonomous state\x01",
            "I will introduce restaurants.\x02\x03",
            "#02100FIn addition to the coverage at each store,\x01",
            "In cooperation with discount service etc.\x01",
            "You got it.\x02\x03",
            "#02109FWell, that kind of feeling\x01",
            "An interesting project\x01",
            "Wake is ongoing in various ways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI see……\x01",
            "That sounds pretty ephemeral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02109FWith -!\x01",
            "From here it is the main theme … …\x02\x03",
            "#02100FAs one of the projects,\x01",
            "\"One of the rumored people's favorite gourmet\"\x01",
            "It is said that.\x02\x03",
            "#02104FMs. Maria Bell of IBC,\x01",
            "Iria of alkane shell,\x01",
            "Theodore & Eugene ……\x02\x03",
            "#02102FThat's the Cross Bell Times\x01",
            "To famous people who always crowd\x01",
            "I'm introducing a recommended item.\x02\x03",
            "#02109FSo, you also have\x01",
            "I want to have cooperation by all means.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FHmm … … is this request for this time?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FIt certainly sounds like an interesting project ….\x02\x03",
            "#00105FIn that person\x01",
            "Are we okay to enter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FYou know.\x01",
            "Iria and Mary Bell\x01",
            "I am glad that I can line up my shoulders ……\x02\x03",
            "#00301FWhere we participated,\x01",
            "I feel sorry for something.\x01",
            "Is not it going to happen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FTo be convinced,\x01",
            "We are good\x01",
            "Is there a horserace?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#02105FNonon,\x01",
            "It is ridiculous to be a horse!\x02\x03",
            "#02102FLately, I will support you\x01",
            "Are pure fans increasing?\x02\x03",
            "#02109FPrivate of support team members\x01",
            "Needless to say I want to take a picture\x01",
            "It's about as long as I'm coming\x02",
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
            "#00106FWell, as it is\x01",
            "I would like you to have a clue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02100FHuhu, anyhow\x01",
            "You are becoming you\x01",
            "It is said that attention has been paid.\x02\x03",
            "#02104FIf it was not so,\x01",
            "I did not ask you anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FAnyway, I understood the story largely.\x02\x03",
            "#00000FSpecifically, how can we proceed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02102FUhufu, then it continues\x01",
            "I will explain how to interview.\x02\x03",
            "#02104FFirst of all, cooks from various places\x01",
            "Rotating around the stall, in fact that store's\x01",
            "Please have some food.\x02\x03",
            "#02109FYou guys from that\x01",
            "\"this is! I thought the dish\x01",
            "I want you to find each one.\x02\x03",
            "#02102FAnd finally at this correspondent company,\x01",
            "To yourself\x01",
            "That's why I write articles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FTurning around the shop of autonomous state,\x01",
            "Six people, each favorite\x01",
            "That's why you are searching.\x02\x03",
            "#10105FBut, if not found …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02102FThe crossbell is wide,\x01",
            "Absolutely one is\x01",
            "I hope to find the food you like.\x02\x03",
            "#02104FEven if you do not find it,\x01",
            "If you can get around 6\x01",
            "Because I can make articles for now.\x02\x03",
            "#2100FWell, ideal after all\x01",
            "Favorite of all of you six people\x01",
            "It is something I can introduce.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FHmm, anyway at least\x01",
            "I have to pass more than 6 places\x01",
            "It is not good.\x02\x03",
            "#00300FThe other things to pay attention to\x01",
            "Is not there a miss?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02103FHmm, well …\x02\x03",
            "#02105FOh, with the shops in Michelin\x01",
            "The so-called \"bar\"\x01",
            "I wonder if you can exclude it.\x02\x03",
            "#02102FIn other places\x01",
            "You will be interviewed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FHmm, as it becomes\x01",
            "\"Trinity\" in old town is also\x01",
            "Does it matter?\x02\x03",
            "#10300FHuhu, the shops are prosperous\x01",
            "It was a chance,\x01",
            "Is it bad for Abbas?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)

    ChrTalk(
        0xB,
        (
            "#02109FNo. Well, sorry, you!\x01",
            "To the interview team in that direction\x01",
            "I will tell from my direction.\x02\x03",
            "#02104F… … Ah, and for the interview\x01",
            "Since I already have talked to each store,\x01",
            "Do not worry about food and drink.\x02\x03",
            "#02102FIf you go to a shop and tell the situation,\x01",
            "You should get a taste menu.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FAnyhow, store other than the bar\x01",
            "I hope it will be more than six places.\x02\x03",
            "#00103FAll of us favorite\x01",
            "To find out\x01",
            "It seems necessary to turn patiently ….\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x2)

    ChrTalk(
        0xB,
        (
            "#02104FHuhu, it is not a job to hurry up.\x01",
            "Anyway do your best.\x02\x03",
            "#02100FWhen I thought that we had gone through and interviewed,\x01",
            "Please return to the correspondent and report it.\x02\x03",
            "#02109FEven when I am not at a telecommunications company,\x01",
            "If you tell Tria about the reception\x01",
            "Because I can get up soon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, sorry.\x01",
            "I will get down to it.\x02",
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
            "Quest 【Interview coverage of the gourmet guide】\x07\x00",
            "I started!\x02",
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

    # Function_21_6B8E end

    def Function_22_7F46(): pass

    label("Function_22_7F46")

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
            "Gourmet guide coverage\x01",
            "More than 6 restaurants\x01",
            "You seem to have been turned around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "早速、Graceさんに\x01",
            "Would you like to report it?\x02",
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
            "I have not reported it yet\x01",          # 0
            "Graceに報告する\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8168")

    ChrTalk(
        0x8,
        "Certainly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "では、Graceさんを\x01",
            "Because I will call you, everyone\x01",
            "Please wait at the 2nd floor.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jump("loc_81E1")

    label("loc_8168")


    ChrTalk(
        0x8,
        "Oh, is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then, when reporting\x01",
            "Please give your voice again.\x02",
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

    label("loc_81E1")

    Return()

    # Function_22_7F46 end

    def Function_23_81E2(): pass

    label("Function_23_81E2")

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
            "#02109FHey, cheers for good work\x02\x03",
            "#02102FInterview with \"Ichizume Gourmet\"\x01",
            "How was it~?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, well …\x01",
            "I enjoyed it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FBecause it turned quite a wide range\x01",
            "I was tired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02100FHuh, tasty things\x01",
            "I'm glad I could have eaten a lot.\x02\x03",
            "#02109FWell then, I got the results of the interview\x01",
            "Shall I tell you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FUh, well …\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd went for an interview\x01",
            "I reported about the store.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_8458")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_846B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_846B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_847E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_847E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_8491")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_84A4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_84A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_84B7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_84B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_84CA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_84CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_84DD")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_84DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_84F0")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_84F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_8503")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8503")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_8516")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8516")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_861C")

    ChrTalk(
        0xB,
        (
            "#02104FFifpen, 11 shops in all\x01",
            "You came around me.\x02\x03",
            "#02109FThat's quite carefully again\x01",
            "You seem to have interviewed me ~!\x01",
            "Huh, your sister is happy!\x02\x03",
            "#02102FWell then …\x01",
            "You met in it\x01",
            "Please teach me how to eat!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A98")

    label("loc_861C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8701")

    ChrTalk(
        0xB,
        (
            "#02104FFifpen, 10 shops in all\x01",
            "You came around me.\x02\x03",
            "#02102FHuhu, cooperate firmly\x01",
            "You do not seem to have given it.\x02\x03",
            "#02100FWell then …\x01",
            "You met in it\x01",
            "Please teach me how to eat!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A98")

    label("loc_8701")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87E8")

    ChrTalk(
        0xB,
        (
            "#02104FFifpen, 9 shops in all\x01",
            "You came around me.\x02\x03",
            "#02102FHuhu, please cooperate firmly\x01",
            "You do not seem to have given it.\x02\x03",
            "#02100FWell then …\x01",
            "You met in it\x01",
            "Please teach me how to eat!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A98")

    label("loc_87E8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_88CF")

    ChrTalk(
        0xB,
        (
            "#02104FFifpen, 8 shops in all\x01",
            "You came around me.\x02\x03",
            "#02102FHuhu, please cooperate firmly\x01",
            "You do not seem to have given it.\x02\x03",
            "#02100FWell then …\x01",
            "You met in it\x01",
            "Please teach me how to eat!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A98")

    label("loc_88CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89B6")

    ChrTalk(
        0xB,
        (
            "#02104FHmm, seven places in all\x01",
            "You came around me.\x02\x03",
            "#02102FHuhu, please cooperate firmly\x01",
            "You do not seem to have given it.\x02\x03",
            "#02100FWell then …\x01",
            "You met in it\x01",
            "Please teach me how to eat!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A98")

    label("loc_89B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A98")

    ChrTalk(
        0xB,
        (
            "#02104FFifpen, six stores in all\x01",
            "You came around me.\x02\x03",
            "#02102FHuhu, please cooperate firmly\x01",
            "You do not seem to have given it.\x02\x03",
            "#02100FWell then …\x01",
            "You met in it\x01",
            "Please teach me how to eat!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A98")

    Fade(500)
    OP_68(58050, 1900, 10380, 0)
    MoveCamera(12, 26, -1, 0)
    OP_6E(400, 0)
    SetCameraDistance(17470, 0)
    OP_0D()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_8BD2")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000FI am in Almorika village\x01",
            "Accommodation for \"Tonerico Tei\"\x01",
            "It is \"Takumi style omelette\".\x02\x03",
            "#00002FThe rustic taste unique to Almorika village\x01",
            "I touched my string.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02102FIndeed, that omurise is\x01",
            "I can only taste it over there ~!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_8CD4")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x102,
        (
            "#00104FI am in Ursula Hospital\x01",
            "The buffet \"Lecce\"\x01",
            "It is \"Three-day simmered stew\".\x02\x03",
            "#00109FIt was cooked for a long time,\x01",
            "Moreover, it seems to be very good also for your body.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02109FYeah yeah, I just eat that stew\x01",
            "It is going to be fine soon!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8CD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_8DD5")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x103,
        (
            "#00204FI was on the ice stall in the red light district\x01",
            "I'd like to presume \"Frozen Food\" 七 彩 ≫\".\x02\x03",
            "#00202FThat mysterious texture and taste of the seven colors ……\x01",
            "Whether it overrides the common sense of ice until now it is a good item.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02105FHuh, Tio-chan's acclaimed!\x01",
            "Surely it will be popular in the future!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_8EEE")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x104,
        (
            "#00300FI was issued at a noodle stand in the port area\x01",
            "\"Tenkami noodle≪ sunny day \"that's right.\x02\x03",
            "#00309FTiny noodles with elasticity\x01",
            "Attended with crimson dry soup ……\x01",
            "Even just remembering can be touched.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02104FHmm, on that stall\x01",
            "I often go to lunch.\x01",
            "There is no hesitation of the master, is not he ~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8EEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_8FE8")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x109,
        (
            "#10107FI am a member of the East Rd \"Ryuushu\"\x01",
            "\"Tenkanaki fried rice\" is!\x02\x03",
            "#10104FSimple yet deep flavor,\x01",
            "Once you start eating it will not stop!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02109FGood food of Mr. Chan Hui!\x01",
            "Well, I also\x01",
            "I got to want to eat it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_90E8")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x105,
        (
            "#10304FMy push is the tangram gate\x01",
            "Was this review helpful? Yes Problem with this review?\x02\x03",
            "#10302FThe flavor is nice, and to do it all together\x01",
            "I think that there is nothing more than this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02102FBorder gate cafeteria\x01",
            "It's a hidden gourmet spot!\x01",
            "Huh, because Waji you too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_90E8")


    ChrTalk(
        0x101,
        (
            "#00004FTentatively\x01",
            "Is it such a place?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_92E1")
    OP_2C(0x80, 0x2)
    OP_63(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#02102FYeah well, perfectly\x01",
            "\"Memory of gourmet\" of all members\x01",
            "You seem to have found it.\x02\x03",
            "#02104FThis also features gourmet guide special page\x01",
            "It should be fairly fulfilling.\x02\x03",
            "#02109FThank you so much, you guys!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000Fはは、Thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202FIt was worthwhile to work hard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02105FOops, the work has not ended yet.\x02\x03",
            "#02102FGet to you at once\x01",
            "I have to finish introduction comments!\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x80, 0x1, 0xF)
    Jump("loc_964C")

    label("loc_92E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_94AC")
    OP_2C(0x80, 0x1)

    ChrTalk(
        0xB,
        (
            "#02106FWell, as expected\x01",
            "\"One push gourmet\" is\x01",
            "Did not you find it?\x02\x03",
            "#02102FWell, I wonder if it is a running point.\x01",
            "I will say thanks for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012Fあ、Thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F(Even if you try harder a little\x01",
            "It might be good …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02104FBut even those who do not have favorites\x01",
            "Number 2 and Number 3 are\x01",
            "You should have had several?\x02\x03",
            "#02102FWhile compensating for missing parts well,\x01",
            "Get introduction comments immediately\x01",
            "Let's finish it!\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x80, 0x1, 0x10)
    Jump("loc_964C")

    label("loc_94AC")

    OP_63(0xB, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#02105FOh, that? Your\x01",
            "Is this \"just like this gourmet\" alone?\x02\x03",
            "#02106FWell, I guess it can not be helped ….\x01",
            "I wonder if I manage to do something a bit more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FThere is no face.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F(I wish I had worked harder more … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02103F… Well, it can not be helped.\x01",
            "It seems that the minimum has turned around.\x02\x03",
            "#02100FWhile compensating for missing parts well,\x01",
            "Get introduction comments immediately\x01",
            "Let's finish it!\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x80, 0x1, 0x11)

    label("loc_964C")

    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "After that, Lloyd's\x01",
            "To an unfamiliar article\x01",
            "Struggling hard … ….\x07\x00\x02",
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
            "Somehow the gourmet guide\x01",
            "\"One push gourmet\" introduction article\x01",
            "It was finishing.\x07\x00\x02",
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
            "#02100FYeah, I wonder why this is the place.\x02\x03",
            "#02104FI will proofread later this time,\x01",
            "Anyways OK with this!\x02\x03",
            "#02102FHehu, thanks.\x01",
            "An interesting gourmet guide\x01",
            "I wonder if I can make it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FHaha, it was serious but …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FWell, for now\x01",
            "Is it mission completed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02104FYes, I really appreciate it.\x02\x03",
            "#02109FTo issue gourmet guide\x01",
            "It will take a little while, though,\x01",
            "Please look forward to it!\x02\x03",
            "#02102FPlease feel free to contact me again if there is something again ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, then, I will excuse you.\x02",
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
            "Quest 【Interview coverage of the gourmet guide】\x07\x00",
            "Achieved!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 6)
    OP_29(0x80, 0x1, 0x12)
    OP_29(0x80, 0x4, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_9981")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9981")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_9993")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9993")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_99A5")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_99A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_99B7")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_99B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_99C9")
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_99C9")

    SetChrFlags(0xB, 0x80)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -6370, 250, 2630, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_23_81E2 end

    def Function_24_99FA(): pass

    label("Function_24_99FA")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9A04")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9E14")
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_9A3E")
    MenuCmd(1, 1, "★ Fairy Gelato")
    Jump("loc_9A56")

    label("loc_9A3E")

    MenuCmd(1, 1, "Fairy Gelato")

    label("loc_9A56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_9A70")
    MenuCmd(1, 1, "凰 enghong noodles")
    Jump("loc_9A7A")

    label("loc_9A70")

    MenuCmd(1, 1, "Phoenix noodle")

    label("loc_9A7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_9A9E")
    MenuCmd(1, 1, "★ Conference center basil pasta")
    Jump("loc_9AB2")

    label("loc_9A9E")

    MenuCmd(1, 1, "Conference center basil pasta")

    label("loc_9AB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_9AD6")
    MenuCmd(1, 1, "★ Tomato Soda")
    Jump("loc_9AEA")

    label("loc_9AD6")

    MenuCmd(1, 1, "Fresh tomato soda")

    label("loc_9AEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_9B0C")
    MenuCmd(1, 1, "★ Pyrant hot spring tofu")
    Jump("loc_9B1E")

    label("loc_9B0C")

    MenuCmd(1, 1, "Pyranka tofu")

    label("loc_9B1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_9B44")
    MenuCmd(1, 1, "★ Sunset croissant")
    Jump("loc_9B5A")

    label("loc_9B44")

    MenuCmd(1, 1, "Sunset croissant")

    label("loc_9B5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_9B7C")
    MenuCmd(1, 1, "★ masterful omelet rice")
    Jump("loc_9B8E")

    label("loc_9B7C")

    MenuCmd(1, 1, "Takumi style omelet rice")

    label("loc_9B8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_9BB6")
    MenuCmd(1, 1, "★ thick walled stamina steak")
    Jump("loc_9BCE")

    label("loc_9BB6")

    MenuCmd(1, 1, "Thick thick stamina steak")

    label("loc_9BCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_9BF4")
    MenuCmd(1, 1, "★ Ripe Beef Stew")
    Jump("loc_9C0A")

    label("loc_9BF4")

    MenuCmd(1, 1, "Ripe beef stew")

    label("loc_9C0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_9C2E")
    MenuCmd(1, 1, "★ Addictive Curry Pot")
    Jump("loc_9C42")

    label("loc_9C2E")

    MenuCmd(1, 1, "Addictive curry pot")

    label("loc_9C42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_9C64")
    MenuCmd(1, 1, "★ Urumoi soymilk hot pot")
    Jump("loc_9C76")

    label("loc_9C64")

    MenuCmd(1, 1, "Urumoi soymilk hot pot")

    label("loc_9C76")

    MenuCmd(1, 1, "quit")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 0)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9CED"),
        (1, "loc_9D06"),
        (2, "loc_9D1F"),
        (3, "loc_9D38"),
        (4, "loc_9D51"),
        (5, "loc_9D6A"),
        (6, "loc_9D83"),
        (7, "loc_9D9C"),
        (8, "loc_9DB5"),
        (9, "loc_9DCE"),
        (10, "loc_9DE7"),
        (11, "loc_9E00"),
        (SWITCH_DEFAULT, "loc_9E0F"),
    )


    label("loc_9CED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_9CFE")
    ClearScenarioFlags(0x172, 1)
    Jump("loc_9D01")

    label("loc_9CFE")

    SetScenarioFlags(0x172, 1)

    label("loc_9D01")

    Jump("loc_9E0F")

    label("loc_9D06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_9D17")
    ClearScenarioFlags(0x172, 2)
    Jump("loc_9D1A")

    label("loc_9D17")

    SetScenarioFlags(0x172, 2)

    label("loc_9D1A")

    Jump("loc_9E0F")

    label("loc_9D1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_9D30")
    ClearScenarioFlags(0x172, 3)
    Jump("loc_9D33")

    label("loc_9D30")

    SetScenarioFlags(0x172, 3)

    label("loc_9D33")

    Jump("loc_9E0F")

    label("loc_9D38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_9D49")
    ClearScenarioFlags(0x172, 4)
    Jump("loc_9D4C")

    label("loc_9D49")

    SetScenarioFlags(0x172, 4)

    label("loc_9D4C")

    Jump("loc_9E0F")

    label("loc_9D51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_9D62")
    ClearScenarioFlags(0x172, 5)
    Jump("loc_9D65")

    label("loc_9D62")

    SetScenarioFlags(0x172, 5)

    label("loc_9D65")

    Jump("loc_9E0F")

    label("loc_9D6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_9D7B")
    ClearScenarioFlags(0x172, 6)
    Jump("loc_9D7E")

    label("loc_9D7B")

    SetScenarioFlags(0x172, 6)

    label("loc_9D7E")

    Jump("loc_9E0F")

    label("loc_9D83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_9D94")
    ClearScenarioFlags(0x172, 7)
    Jump("loc_9D97")

    label("loc_9D94")

    SetScenarioFlags(0x172, 7)

    label("loc_9D97")

    Jump("loc_9E0F")

    label("loc_9D9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_9DAD")
    ClearScenarioFlags(0x173, 0)
    Jump("loc_9DB0")

    label("loc_9DAD")

    SetScenarioFlags(0x173, 0)

    label("loc_9DB0")

    Jump("loc_9E0F")

    label("loc_9DB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_9DC6")
    ClearScenarioFlags(0x173, 1)
    Jump("loc_9DC9")

    label("loc_9DC6")

    SetScenarioFlags(0x173, 1)

    label("loc_9DC9")

    Jump("loc_9E0F")

    label("loc_9DCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_9DDF")
    ClearScenarioFlags(0x173, 2)
    Jump("loc_9DE2")

    label("loc_9DDF")

    SetScenarioFlags(0x173, 2)

    label("loc_9DE2")

    Jump("loc_9E0F")

    label("loc_9DE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_9DF8")
    ClearScenarioFlags(0x173, 3)
    Jump("loc_9DFB")

    label("loc_9DF8")

    SetScenarioFlags(0x173, 3)

    label("loc_9DFB")

    Jump("loc_9E0F")

    label("loc_9E00")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9E0F")

    label("loc_9E0F")

    Jump("loc_9A04")

    label("loc_9E14")

    Return()

    # Function_24_99FA end

    def Function_25_9E15(): pass

    label("Function_25_9E15")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Battlefield coverage over \"One hundred day campaign\"\x01",
            "Three months of press coverage\x01",
            "It was sincere and full of justice.\x02\x03",
            "To praise that achievement\x01",
            "I give the Fürlitza prize here.\x01",
            "S 1192 November\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_25_9E15 end

    def Function_26_9EE6(): pass

    label("Function_26_9EE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_9EF0")
    Return()

    label("loc_9EF0")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A09C")

    ChrTalk(
        0x8,
        "Oh, everyone …!\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_9F62():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_9F62)
    Sleep(50)

    def lambda_9F72():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_9F72)
    Sleep(50)

    def lambda_9F82():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_9F82)
    Sleep(50)

    def lambda_9F92():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_9F92)
    Sleep(50)

    def lambda_9FA2():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x4, 2, lambda_9FA2)
    Sleep(50)

    def lambda_9FB2():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x5, 2, lambda_9FB2)
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
            "Sorry, basically\x01",
            "The editing department on the second floor is not related\x01",
            "Being off limits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "御用なら私の方にTell me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FWell, sorry.\x01",
            "That was rude of me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_A0E6")

    label("loc_A09C")


    ChrTalk(
        0x101,
        (
            "#00000FThe second floor seems to be off limits.\x01",
            "I can not let you go up without permission.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A0E6")

    Sleep(50)
    SetChrPos(0x0, -6370, 20, 2470, 180)
    EventEnd(0x4)
    Return()

    # Function_26_9EE6 end

    def Function_27_A0FD(): pass

    label("Function_27_A0FD")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "資料棚にCrossbell Times'\x01",
            "Back numbers are listed.\x02",
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
            "【Reading the first insight of 2004】\x01",      # 0
            "【Read the previous term of 2004】\x01",      # 1
            "【quit】\x01",                    # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2CB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Cross Bell Times exclamation]\x01",        # 0
            "【Cross Bell Times 嘇】\x01",        # 1
            "【Cross Bell Times 嘊】\x01",        # 2
            "【Crossbell Times exception】\x01",      # 3
            "【Cross Bell Times 嘋】\x01",        # 4
            "【quit】\x01",                      # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A276")
    UseItem(0x2BC, 0xFF)

    label("loc_A276")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A28A")
    UseItem(0x2BD, 0xFF)

    label("loc_A28A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A29E")
    UseItem(0x2BE, 0xFF)

    label("loc_A29E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2B2")
    UseItem(0x2BF, 0xFF)

    label("loc_A2B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2C6")
    UseItem(0x2C0, 0xFF)

    label("loc_A2C6")

    Jump("loc_A3C9")

    label("loc_A2CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3C0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【Cross Bell Times 嘍】\x01",      # 0
            "【Cross Bell Times 嘐】\x01",      # 1
            "【Cross Bell Times 嘑】\x01",      # 2
            "【Cross Bell Times 嘒】\x01",      # 3
            "【quit】\x01",                    # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A37F")
    UseItem(0x2C1, 0xFF)

    label("loc_A37F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A393")
    UseItem(0x2C2, 0xFF)

    label("loc_A393")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3A7")
    UseItem(0x2C3, 0xFF)

    label("loc_A3A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3BB")
    UseItem(0x2C4, 0xFF)

    label("loc_A3BB")

    Jump("loc_A3C9")

    label("loc_A3C0")

    FadeToBright(300, 0)

    label("loc_A3C9")

    TalkEnd(0xFF)
    Return()

    # Function_27_A0FD end

    SaveToFile()

Try(main)
