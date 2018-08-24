from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c033b.bin",                # FileName
        "c033b",                    # MapName
        "c033b",                    # Location
        0x002C,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "c033b",                  # 0
        "Harold",                 # 1
        "Sophia",                 # 2
        "Colin",                  # 3
    ))

    AddCharChip((
        "chr/ch09300.itc",                   # 00
        "chr/ch09302.itc",                   # 01
        "chr/ch09400.itc",                   # 02
        "chr/ch09402.itc",                   # 03
        "chr/ch07200.itc",                   # 04
        "chr/ch07202.itc",                   # 05
    ))

    DeclNpc(4294966956, 0,       4409,    315,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(550,     0,       2039,    180,  261,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(37479,   0,       3799,    180,  261,  0x0, 0,   4,   0,   0,   0,   0,   6,   255,  0)

    DeclActor(34620,   0,       7280,    1200,    34620,   1750,    7280,    0x007C, 0,  3,  0x0000)

    ChipFrameInfo(320, 0)                                        # 0

    ScpFunction((
        "Function_0_140",          # 00, 0
        "Function_1_1F0",          # 01, 1
        "Function_2_23A",          # 02, 2
        "Function_3_23B",          # 03, 3
        "Function_4_2EB",          # 04, 4
        "Function_5_49D",          # 05, 5
        "Function_6_520",          # 06, 6
    ))


    def Function_0_140(): pass

    label("Function_0_140")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_178"),
        (1, "loc_184"),
        (2, "loc_190"),
        (3, "loc_19C"),
        (4, "loc_1A8"),
        (5, "loc_1B4"),
        (6, "loc_1C0"),
        (SWITCH_DEFAULT, "loc_1CC"),
    )


    label("loc_178")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_184")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_190")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_19C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1A8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1B4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1C0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1CC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1EF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1EF")

    Return()

    # Function_0_140 end

    def Function_1_1F0(): pass

    label("Function_1_1F0")

    SetChrPos(0x8, 1940, 200, 6910, 270)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x9, 40940, 0, -550, 180)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0xA, 40930, 0, -1640, 90)
    Return()

    # Function_1_1F0 end

    def Function_2_23A(): pass

    label("Function_2_23A")

    Return()

    # Function_2_23A end

    def Function_3_23B(): pass

    label("Function_3_23B")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a car magazine,\x01",
            ""Monthly Car Mania\x01",
            "Vol.1".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x36C, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E7")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "Learned the \x07\x02",
            ""Sky\x01",
            "Coloring"\x07\x00",
            " paint pattern.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x36C, 1)

    label("loc_2E7")

    TalkEnd(0xFF)
    Return()

    # Function_3_23B end

    def Function_4_2EB(): pass

    label("Function_4_2EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_425")

    ChrTalk(
        0x8,
        "#03605FOh, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FGood evening, Harold.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FA nice smell is coming from\x01",
            "the second floor... It seems\x01",
            "your wife is preparing dinner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03600FYes, you're right. And\x01",
            "it seems Colin is\x01",
            "helping her today, too.\x02\x03",
            "#03609FMan, I've just gotten\x01",
            "home and I'm very\x01",
            "hungry.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 6)
    Jump("loc_499")

    label("loc_425")


    ChrTalk(
        0x8,
        (
            "#03600FIt seems Colin is\x01",
            "helping too today.\x02\x03",
            "#03609FHaha, I can't wait to\x01",
            "see what dishes we're\x01",
            "going to have.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_499")

    TalkEnd(0xFE)
    Return()

    # Function_4_2EB end

    def Function_5_49D(): pass

    label("Function_5_49D")

    TalkBegin(0xFE)

    ChrTalk(
        0x9,
        (
            "#03700FAlright, we only need to\x01",
            "let it simmer.\x02\x03",
            "#03709FHaha. You did well,\x01",
            "Colin. Your dad will be\x01",
            "delighted for sure.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_49D end

    def Function_6_520(): pass

    label("Function_6_520")

    TalkBegin(0xFE)

    ChrTalk(
        0xA,
        (
            "#03802FTonight's dinner is\x01",
            "curry...\x02\x03",
            "#03809FEhehe, I cut the\x01",
            "vegetables. Cool, huh?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_520 end

    SaveToFile()

Try(main)
