from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e302b.bin",                # FileName
        "e302b",                    # MapName
        "e302b",                    # Location
        0x0000,                     # MapIndex
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
        "e302b",                  # 0
        "Knight Abbas",           # 1
        "Jona",                   # 2
        "Wazy",                   # 3
        "Tio",                    # 4
        "Fran",                   # 5
        "Rixia",                  # 6
        "Randy",                  # 7
        "Noｱl",                  # 8
        "Elie",                   # 9
        "Chairman MacDowell",     # 10
        "Grace",                  # 11
        "Divine Wolf Zeit",       # 12
        "Squire Ventos",          # 13
        "Squire Juno",            # 14
    ))

    AddCharChip((
        "chr/ch06712.itc",                   # 00
        "chr/ch06102.itc",                   # 01
        "chr/ch03100.itc",                   # 02
        "chr/ch03102.itc",                   # 03
        "chr/ch00202.itc",                   # 04
        "chr/ch06900.itc",                   # 05
        "chr/ch03200.itc",                   # 06
        "chr/ch00302.itc",                   # 07
        "chr/ch06002.itc",                   # 08
        "chr/ch02902.itc",                   # 09
        "chr/ch00102.itc",                   # 0A
        "chr/ch05802.itc",                   # 0B
        "chr/ch02710.itc",                   # 0C
        "chr/ch48400.itc",                   # 0D
    ))

    DeclNpc(101790,  150,     4294873286, 90,   261,  0x0, 0,   0,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(3000,    4294965946, 6960,    45,   261,  0x0, 0,   1,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(101790,  150,     4294871316, 90,   261,  0x0, 0,   3,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(4294964177, 4294965946, 7039,    315,  261,  0x0, 0,   4,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(100849,  0,       270,     270,  261,  0x0, 0,   5,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(4294965796, 0,       4294965796, 0,    389,  0x0, 0,   6,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(97639,   170,     959,     90,   261,  0x0, 0,   7,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(100309,  170,     959,     270,  261,  0x0, 0,   9,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(100169,  100,     4294864576, 270,  261,  0x0, 0,   10,  0,   255, 255, 0,   6,   255,  0)
    DeclNpc(98440,   100,     4294866186, 180,  261,  0x0, 0,   11,  0,   255, 255, 0,   17,  255,  0)
    DeclNpc(100220,  100,     4294862517, 270,  261,  0x0, 0,   8,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(4294964296, 0,       4294964796, 0,    389,  0x0, 0,   12,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(103569,  0,       4294870207, 270,  257,  0x0, 0,   13,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(103949,  0,       4294967087, 270,  257,  0x0, 0,   13,  0,   0,   0,   0,   21,  255,  0)

    DeclActor(102510,  0,       4294870276, 1000,    103570,  1500,    4294870206, 0x007E, 0,  18, 0x0000)
    DeclActor(102710,  0,       4294967096, 400,     103950,  1500,    4294967086, 0x007E, 0,  20, 0x0000)
    DeclActor(2350,    0,       4294875066, 800,     2350,    1500,    4294875066, 0x007C, 0,  28, 0x0000)
    DeclActor(103750,  0,       4294861656, 2000,    103750,  1500,    4294861656, 0x007C, 0,  3,  0x0000)

    ChipFrameInfo(864, 0)                                        # 0

    ScpFunction((
        "Function_0_360",          # 00, 0
        "Function_1_410",          # 01, 1
        "Function_2_509",          # 02, 2
        "Function_3_54E",          # 03, 3
        "Function_4_734",          # 04, 4
        "Function_5_86F",          # 05, 5
        "Function_6_E3C",          # 06, 6
        "Function_7_11FA",         # 07, 7
        "Function_8_17B8",         # 08, 8
        "Function_9_1BC3",         # 09, 9
        "Function_10_1D42",        # 0A, 10
        "Function_11_2275",        # 0B, 11
        "Function_12_2417",        # 0C, 12
        "Function_13_2AF7",        # 0D, 13
        "Function_14_2D7D",        # 0E, 14
        "Function_15_2F05",        # 0F, 15
        "Function_16_3383",        # 10, 16
        "Function_17_37DF",        # 11, 17
        "Function_18_3BEA",        # 12, 18
        "Function_19_3BEE",        # 13, 19
        "Function_20_3EE9",        # 14, 20
        "Function_21_3EED",        # 15, 21
        "Function_22_416C",        # 16, 22
        "Function_23_4928",        # 17, 23
        "Function_24_50DA",        # 18, 24
        "Function_25_5911",        # 19, 25
        "Function_26_6347",        # 1A, 26
        "Function_27_6DAB",        # 1B, 27
        "Function_28_72A4",        # 1C, 28
        "Function_29_7C63",        # 1D, 29
        "Function_30_7C83",        # 1E, 30
    ))


    def Function_0_360(): pass

    label("Function_0_360")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_398"),
        (1, "loc_3A4"),
        (2, "loc_3B0"),
        (3, "loc_3BC"),
        (4, "loc_3C8"),
        (5, "loc_3D4"),
        (6, "loc_3E0"),
        (SWITCH_DEFAULT, "loc_3EC"),
    )


    label("loc_398")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3F8")

    label("loc_3A4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3F8")

    label("loc_3B0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3F8")

    label("loc_3BC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3F8")

    label("loc_3C8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3F8")

    label("loc_3D4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3F8")

    label("loc_3E0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3F8")

    label("loc_3EC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3F8")

    label("loc_3F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_40F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3F8")

    label("loc_40F")

    Return()

    # Function_0_360 end

    def Function_1_410(): pass

    label("Function_1_410")

    SetMapFlags(0x10000)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrChipByIndex(0xE, 0x7)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrChipByIndex(0x12, 0x8)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    SetChrChipByIndex(0xF, 0x9)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    SetChrChipByIndex(0x10, 0xA)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    SetChrChipByIndex(0x11, 0xB)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BD")
    SetChrFlags(0xB, 0x10)

    label("loc_4BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_4D7")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 30)
    Jump("loc_508")

    label("loc_4D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_4EB")
    ClearScenarioFlags(0x22, 2)
    Event(0, 29)
    Jump("loc_508")

    label("loc_4EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 3)), scpexpr(EXPR_END)), "loc_508")
    ClearScenarioFlags(0x24, 3)
    SetChrPos(0x0, 102230, 0, -105070, 90)

    label("loc_508")

    Return()

    # Function_1_410 end

    def Function_2_509(): pass

    label("Function_2_509")

    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0xD0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_527")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_527")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_53B")
    OP_24(0x1F2)
    ClearScenarioFlags(0x0, 1)
    Jump("loc_541")

    label("loc_53B")

    Sound(498, 1, 80, 0)

    label("loc_541")

    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x3, 0x10)
    Return()

    # Function_2_509 end

    def Function_3_54E(): pass

    label("Function_3_54E")

    OP_C9(0x0, 0x4)
    OP_C9(0x0, 0x100)
    OP_E5(0xA)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E5(0x5)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_573")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6E7")
    RunExpression(0x5, (scpexpr(EXPR_EXEC_OP, "OP_E5(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_END)),
        (0, "loc_5AC"),
        (1, "loc_5DB"),
        (2, "loc_6CB"),
        (3, "loc_6D3"),
        (SWITCH_DEFAULT, "loc_6E2"),
    )


    label("loc_5AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5CB")
    OP_2B(0x9A, 0x9B, 0x9C, 0x96, 0x97, 0x98, 0x99, 0xFFFF)
    Jump("loc_5D6")

    label("loc_5CB")

    OP_2B(0x96, 0x97, 0x98, 0x99, 0xFFFF)

    label("loc_5D6")

    Jump("loc_6E2")

    label("loc_5DB")

    SetMapFlags(0x40000000)
    OP_E5(0x7)
    Sleep(500)
    SetChrName("Announcement")

    AnonymousTalk(
        0xFF,
        "This is Crossbell Police.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E5(0x4)"), scpexpr(EXPR_END)), "loc_69A")

    AnonymousTalk(
        0xFF,
        "I will receive your report.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x8, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xC)
    SetChrName("Announcement")

    AnonymousTalk(
        0xFF,
        (
            "Report processing, complete.\x01",
            "Thank you for your hard work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BD")

    label("loc_69A")


    AnonymousTalk(
        0xFF,
        "There no reportable requests.\x02",
    )

    CloseMessageWindow()

    label("loc_6BD")

    OP_57(0x0)
    OP_E5(0x8)
    ClearMapFlags(0x40000000)
    Jump("loc_6E2")

    label("loc_6CB")

    Call(0, 4)
    Jump("loc_6E2")

    label("loc_6D3")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6E2")

    label("loc_6E2")

    Jump("loc_573")

    label("loc_6E7")

    OP_E5(0x6)
    OP_C9(0x1, 0x4)
    OP_C9(0x1, 0x100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_724")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 5)
    Return()

    label("loc_724")

    FadeToBright(1000, 0)
    OP_0D()
    OP_E5(0xB)
    TalkEnd(0xFF)
    Return()

    # Function_3_54E end

    def Function_4_734(): pass

    label("Function_4_734")

    OP_E5(0x6)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 3)), scpexpr(EXPR_END)), "loc_756")
    SetScenarioFlags(0x2A, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_756")
    ClearScenarioFlags(0x2A, 0)

    label("loc_756")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 4)), scpexpr(EXPR_END)), "loc_773")
    SetScenarioFlags(0x2A, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_773")
    ClearScenarioFlags(0x2A, 1)

    label("loc_773")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 5)), scpexpr(EXPR_END)), "loc_790")
    SetScenarioFlags(0x2A, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_790")
    ClearScenarioFlags(0x2A, 2)

    label("loc_790")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 6)), scpexpr(EXPR_END)), "loc_7AD")
    SetScenarioFlags(0x2A, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7AD")
    ClearScenarioFlags(0x2A, 3)

    label("loc_7AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 7)), scpexpr(EXPR_END)), "loc_7CA")
    SetScenarioFlags(0x2A, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7CA")
    ClearScenarioFlags(0x2A, 4)

    label("loc_7CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 0)), scpexpr(EXPR_END)), "loc_7E7")
    SetScenarioFlags(0x2A, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7E7")
    ClearScenarioFlags(0x2A, 5)

    label("loc_7E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 1)), scpexpr(EXPR_END)), "loc_7F3")
    SetScenarioFlags(0x2A, 6)

    label("loc_7F3")

    OP_24(0x1F2)
    RunExpression(0x9, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1F()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_838")
    Sound(498, 1, 50, 0)
    Jump("loc_83E")

    label("loc_838")

    Sound(498, 1, 100, 0)

    label("loc_83E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_86E")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_86E")

    Return()

    # Function_4_734 end

    def Function_5_86F(): pass

    label("Function_5_86F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0xB, 0x12)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0x8, 0x1A)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0xC, 0x1B)
    SetChrSubChip(0xC, 0x0)
    OP_4B(0xB, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_END)), "loc_8D8")
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, 102700, 0, -102930, 180)

    label("loc_8D8")

    OP_68(102970, 1000, -104740, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(14560, 0)
    SetChrPos(0x101, 103020, 100, -105800, 90)
    SetChrPos(0xB, 101590, 0, -105440, 90)
    SetChrPos(0xC, 101470, 0, -104110, 135)
    SetChrPos(0x8, 103000, 0, -104100, 180)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xB,
        (
            "#00205FOh...\x02\x03",
            "#00204FIt looks like you've\x01",
            "won against all "Pom!"\x01",
            "opponents, Mr. Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01905FWow, reallyyy!?\x02\x03",
            "#01909FThat's Mr. Lloyd for you...\x01",
            "He's too amaziiing!!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_END)), "loc_A45")

    ChrTalk(
        0x9,
        (
            "#02302FHeh, that's right.\x01",
            "You're pretty good too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A45")

    SetChrSubChip(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, thanks. \x01",
            "I just got lucky, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FNo. In puzzle games like that, luck isn't the\x01",
            "primary factor that determines the winner.\x02\x03",
            "#12102FBannings, you are a\x01",
            "true "Pom! Master".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F...T-Thank you for that.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xF0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D30")

    ChrTalk(
        0x8,
        (
            "#12100FHmm... That's right.\x02\x03",
            "If you like, please take this.\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x8, 0x0, 0x1F4, 0x5DC, 0x0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xF0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0xF0, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x8,
        (
            "#12100FIt's a prohibited Master Quartz, jointly\x01",
            "developed by the Church and Epstein\x01",
            "Foundation using ancient techniques.\x02\x03",
            "Being it too powerful and difficult to handle\x01",
            "it's something we hesitated to use, but...\x02\x03",
            "#12102FYou should be able to use it in the right way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FSure, understood. \x01",
            "I'll put it to use, then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E0A")

    label("loc_D30")


    ChrTalk(
        0x8,
        (
            "#12100FHmm... That's right.\x02\x03",
            "#12102FI'll give you this as a prize.\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x8, 0x0, 0x1F4, 0x5DC, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x67),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x67, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00000FHa ha, thanks.\x01",
            "I'll put it to good use.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_E0A")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x2A, 7)
    OP_E0(0x35, 0x0)
    OP_E0(0x80, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x4)
    OP_D7(0x1E)
    EventEnd(0x5)
    SetScenarioFlags(0x24, 3)
    NewScene("e302B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_86F end

    def Function_6_E3C(): pass

    label("Function_6_E3C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E5F")
    Call(0, 22)
    Jump("loc_ED6")

    label("loc_E5F")


    ChrTalk(
        0x10,
        (
            "#00102F(...See you later.)\x02\x03",
            "#00104F(I don't mind if you're late, so please\x01",
            "take your time and finish to prepare.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ED6")

    Jump("loc_11F6")

    label("loc_EDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1169")

    ChrTalk(
        0x10,
        (
            "#00103FThe Crossbell City liberation operation... \x01",
            "It finally starts tomorrow.\x02\x03",
            "#00108FIf we see Bell or "uncle", I'll ask them the\x01",
            "reasoning behind this chain of events...\x01",
            "And if possible, I want to persuade them.\x02\x03",
            "#00101FBut, if I can't, then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008FElie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#00106F...I'm sorry. I'm\x01",
            "just complaining.\x02\x03",
            "#00100FTo repay the many who helped\x01",
            "us heedless of danger...\x02\x03",
            "And above all, to take back\x01",
            "KeA, we mustn't lose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F...Let's do our best together tomorrow, Elie.\x01",
            "Everyone, myself included, is with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#00104F...*giggle*, that's right.\x02\x03",
            "#00102FThank you, Lloyd.\x01",
            "Thanks to you, I feel\x01",
            "a little better.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 5)
    Jump("loc_11F6")

    label("loc_1169")


    ChrTalk(
        0x10,
        (
            "#00104FThank you, Lloyd.\x01",
            "Thanks to you, I feel\x01",
            "just a little better.\x02\x03",
            "#00102FLet's sleep well tonight...\x01",
            "And prepare well for tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11F6")

    TalkEnd(0xFE)
    Return()

    # Function_6_E3C end

    def Function_7_11FA(): pass

    label("Function_7_11FA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1299")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_121D")
    Call(0, 23)
    Jump("loc_1294")

    label("loc_121D")


    ChrTalk(
        0xB,
        (
            "#00204FOnce I finish here, I will\x01",
            "head to the deck as well.\x02\x03",
            "#00202FAbout that discussion...\x01",
            "I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1294")

    Jump("loc_17B4")

    label("loc_1299")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1707")

    ChrTalk(
        0xB,
        (
            "#00203F(*klak klak klak klak*...)\x02\x03",
            "#00200FHmm. Preparations are complete for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FTio... \x01",
            "What're you doing?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x101, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_13C7")
    Jump("loc_1411")

    label("loc_13C7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13E7")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1411")

    label("loc_13E7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1407")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1411")

    label("loc_1407")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1411")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)

    ChrTalk(
        0xB,
        (
            "#00202FI'm performing a final check\x01",
            "of the Merkabah's systems\x01",
            "for tomorrow's sortie.\x02\x03",
            "#00203FAlthough I am planning to disembark\x01",
            "tomorrow with all of you...\x02\x03",
            "#00200FAfter gaining control of the communication\x01",
            "mainframe, I will have to leave the hacking\x01",
            "and the rest to Jona and Miss Fran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FI see... \x01",
            "That seems tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00204FWell, I'll be done soon, so\x01",
            "there's no need to worry.\x02\x03",
            "#00202FIt is enough if Mr. Lloyd\x01",
            "remains unperturbed\x01",
            "like a leader would.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FNo, no. I've got lots to do\x01",
            "to prepare for tomorrow.\x02\x03",
            "#00000FWell, I'll leave\x01",
            "it to you, then.\x02\x03",
            "Make sure you all\x01",
            "get proper rest, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00204FYes, understood. You\x01",
            "too. Please rest well.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)
    SetScenarioFlags(0x1DA, 6)
    ClearChrFlags(0xB, 0x10)
    Jump("loc_17B4")

    label("loc_1707")


    ChrTalk(
        0xB,
        (
            "#00204FI'm performing a final check\x01",
            "of the Merkabah's systems\x01",
            "for tomorrow's sortie.\x02\x03",
            "#00202FI'm almost done, and I\x01",
            "plan to rest myself too.\x01",
            "Please sleep well as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17B4")

    TalkEnd(0xFE)
    Return()

    # Function_7_11FA end

    def Function_8_17B8(): pass

    label("Function_8_17B8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1848")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17DB")
    Call(0, 24)
    Jump("loc_1843")

    label("loc_17DB")


    ChrTalk(
        0xE,
        (
            "#00304FSee you later, then.\x02\x03",
            "#00302FI'll be right there once I finish\x01",
            "maintaining this little guy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1843")

    Jump("loc_1BBF")

    label("loc_1848")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B1E")

    ChrTalk(
        0xE,
        "#00300FYo, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIt looks like you guys are\x01",
            "maintaining your weapons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00302FYeah. They say tomorrow's operation\x01",
            "will be the biggest turning point yet.\x02\x03",
            "#00304FIt'll probably be "Berserker"'s\x01",
            "turn too, so I want to make sure\x01",
            "he's ready when the time comes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FHmm. I suppose there really hasn't been\x01",
            "many chances to make noise up until now...\x02\x03",
            "#00003FMaybe I should repair\x01",
            "my tonfas tonight, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00309FYeah, that's the way.\x02\x03",
            "#00303FUnlike a rifle, yours\x01",
            "don't have any small parts\x01",
            "that need maintenance...\x02\x03",
            "#00300FJust throwing some polish\x01",
            "on there might be enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FI-I see... \x01",
            "I suppose you're right.\x02\x03",
            "#00002FThanks for the advice.\x01",
            "I'll do mine later too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 7)
    Jump("loc_1BBF")

    label("loc_1B1E")


    ChrTalk(
        0xE,
        (
            "#00304FOn my end, I've got to do proper\x01",
            "maintenance for tomorrow.\x02\x03",
            "#00309FAnd just like dealin' with peerless beauties, \x01",
            "you have to be gentle and careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BBF")

    TalkEnd(0xFE)
    Return()

    # Function_8_17B8 end

    def Function_9_1BC3(): pass

    label("Function_9_1BC3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x68), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1C91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BE6")
    Call(0, 25)
    Jump("loc_1C8C")

    label("loc_1BE6")


    ChrTalk(
        0xF,
        (
            "#10106FU-Umm... \x01",
            "There's something I absolutely\x01",
            "want to ask you, Mr. Lloyd.\x02\x03",
            "#10101FPlease come to the deck\x01",
            "later. I'll head there too\x01",
            "once I'm finished here...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C8C")

    Jump("loc_1D3E")

    label("loc_1C91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CA3")
    Call(0, 10)
    Jump("loc_1D3E")

    label("loc_1CA3")


    ChrTalk(
        0xF,
        (
            "#10100FI'd like to get in contact with the\x01",
            "Commander once more tonight.\x02\x03",
            "#10103FI think we should get final confirmation\x01",
            "before tomorrow's operation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D3E")

    TalkEnd(0xFE)
    Return()

    # Function_9_1BC3 end

    def Function_10_1D42(): pass

    label("Function_10_1D42")

    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x101, 0)
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1DD3")
    Jump("loc_1E1D")

    label("loc_1DD3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1DF3")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E1D")

    label("loc_1DF3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E13")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E1D")

    label("loc_1E13")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E1D")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xC, 0x101, 0)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0x101,
        (
            "#00000FGood work, Noｱl and Fran.\x02\x03",
            "#00002FYou are somehow calm heading\x01",
            "into tomorrow's operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#10102FUmm, sorry.\x02\x03",
            "#10106FI was maintaining my weapons\x01",
            "when Fran came in...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01909FUh uh, I came to\x01",
            "support big siiis.\x02\x03",
            "#01904FI've already finished\x01",
            "preparing for tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, how dependable.\x02\x03",
            "#00000FFran, you'll have to work\x01",
            "as an operator for us, so\x01",
            "restore your batteries, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01902FYes, of cooourse.\x01",
            "...And that's why\x01",
            "I've come here!\x02\x03",
            "#01909FAfter all, my energies\x01",
            "are refilled just by being\x01",
            "by my big sis' side!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xF, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00000FHa ha. That doesn't seem\x01",
            "like a joke, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#10106F*sigh*, c'mon... At least\x01",
            "stay out of my way, ok?\x02\x03",
            "#10100FU-Umm, Mr. Lloyd. \x01",
            "I'd like to get in contact with\x01",
            "the Commander once more tonight.\x02\x03",
            "#10103FI think we should get final confirmation\x01",
            "before tomorrow's operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah. I'll be counting on you.\x02\x03",
            "#00000FYou should get some sleep once you've\x01",
            "finished your maintenance too, Noｱl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#10109FYes sir!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xF, 0x0)
    OP_93(0xC, 0x10E, 0x0)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x1DB, 0)
    Return()

    # Function_10_1D42 end

    def Function_11_2275(): pass

    label("Function_11_2275")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x69), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2336")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2298")
    Call(0, 26)
    Jump("loc_2331")

    label("loc_2298")


    ChrTalk(
        0xA,
        (
            "#10404FThere's just one more\x01",
            "thing I'd like to tell\x01",
            "you in secret.\x02\x03",
            "#10402FCome to the deck later.\x01",
            "I'll be there once I finish\x01",
            "drinking with Abbas.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2331")

    Jump("loc_2413")

    label("loc_2336")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2348")
    Call(0, 12)
    Jump("loc_2413")

    label("loc_2348")


    ChrTalk(
        0xA,
        (
            "#10404FWell, we got permission from the\x01",
            "higher-ups, so we too can carry out\x01",
            "the mission without hesitation.\x02\x03",
            "#10402FHu hu. Looks like it's going to be busy\x01",
            "tomorrow. Better relax while I still can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2413")

    TalkEnd(0xFE)
    Return()

    # Function_11_2275 end

    def Function_12_2417(): pass

    label("Function_12_2417")

    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x101, 0)
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_24A8")
    Jump("loc_24F2")

    label("loc_24A8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_24C8")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24F2")

    label("loc_24C8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24E8")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24F2")

    label("loc_24E8")

    OP_52(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_24F2")

    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x101, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_25A8")
    Jump("loc_25F2")

    label("loc_25A8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_25C8")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_25F2")

    label("loc_25C8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_25E8")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_25F2")

    label("loc_25E8")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_25F2")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0x8, 0x10)

    ChrTalk(
        0x101,
        (
            "#00005FWazy, Abbas... Are\x01",
            "you guys drinking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10404FBoth of us have finished\x01",
            "preparing for now, you see.\x02\x03",
            "#10402FHu hu, care to join us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FHey now... Will you be all right,\x01",
            "even though the operation's tomorrow?\x02\x03",
            "#00001FIt looks like there're already\x01",
            "a lot of empty glasses there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FNo need to worry.\x01",
            "They're Ventos' non-\x01",
            "alcoholic cocktails.\x02\x03",
            "They'll be no obstacle\x01",
            "to tomorrow's operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FO-Oh, I see...\x02\x03",
            "#00000FWell if you say so Abbas,\x01",
            "I think I'll trust you this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10409FHu hu. I wouldn't mind it if you\x01",
            "believed me when I drink alone too.\x02\x03",
            "#10403F...That's right, I should\x01",
            "have told you guys earlier.\x02\x03",
            "#10400FOfficial permission has been given\x01",
            "from His Eminence, the Pope, for \x01",
            "participation in tomorrow's operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FAh... I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FThe Merkabah operates in secret.\x01",
            "We normally avoid its use during\x01",
            "large scale operations, but...\x02\x03",
            "When we thought about the confusion \x01",
            "across the continent, perhaps a little \x01",
            "exposure can't be avoided.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FI see.. I'm grateful for\x01",
            "the Church's decision.\x02\x03",
            "#00013F...Anyway, the operation's\x01",
            "tomorrow. Let's do this, Wazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#10402FHu hu, roger that, leader.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#12102FAllow us to assist you, of course.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetScenarioFlags(0x1DB, 1)
    Return()

    # Function_12_2417 end

    def Function_13_2AF7(): pass

    label("Function_13_2AF7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x69), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2C32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B1F")
    Call(0, 26)
    Jump("loc_2C2D")

    label("loc_2B1F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2B29")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C2D")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",              # 0
            "Change Party\x01",      # 1
            "Quit\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2B74"),
        (1, "loc_2C02"),
        (SWITCH_DEFAULT, "loc_2C1E"),
    )


    label("loc_2B74")


    ChrTalk(
        0x8,
        (
            "#12100FOh boy...\x01",
            "That's still a confidential matter.\x02\x03",
            "#12102F...Well, it can't be helped. \x01",
            "If it's you, there should be no problem.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C28")

    label("loc_2C02")

    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(0)
    Fade(500)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C28")

    label("loc_2C1E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C28")

    Jump("loc_2B29")

    label("loc_2C2D")

    Jump("loc_2D79")

    label("loc_2C32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C44")
    Call(0, 12)
    Jump("loc_2D79")

    label("loc_2C44")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C4E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D79")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",              # 0
            "Change Party\x01",      # 1
            "Quit\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2C99"),
        (1, "loc_2D4E"),
        (SWITCH_DEFAULT, "loc_2D6A"),
    )


    label("loc_2C99")


    ChrTalk(
        0x8,
        (
            "#12100FTomorrow's operation...\x01",
            "We will focus on backing\x01",
            "you up from the Merkabah.\x02\x03",
            "You all, who will be infiltrating\x01",
            "in the city, should prepare\x01",
            "well while you still can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D74")

    label("loc_2D4E")

    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(0)
    Fade(500)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D74")

    label("loc_2D6A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D74")

    Jump("loc_2C4E")

    label("loc_2D79")

    TalkEnd(0xFE)
    Return()

    # Function_13_2AF7 end

    def Function_14_2D7D(): pass

    label("Function_14_2D7D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x68), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2E6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DA0")
    Call(0, 25)
    Jump("loc_2E67")

    label("loc_2DA0")


    ChrTalk(
        0xC,
        (
            "#01900FMr. Lloyd, please listen to\x01",
            "big sis' request properly.\x02\x03",
            "#01909FUh uh, I'm looking forward to what will happeeen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Hmm. I wonder why Fran's looking\x01",
            "forward to it that much...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E67")

    Jump("loc_2F01")

    label("loc_2E6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E7E")
    Call(0, 10)
    Jump("loc_2F01")

    label("loc_2E7E")


    ChrTalk(
        0xC,
        (
            "#01902FMr. Lloyd, please do your\x01",
            "very best tomorrow, oook?\x02\x03",
            "#01909FAs for me, big sis\x01",
            "refilled my energy,\x01",
            "so I'm ready to go!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F01")

    TalkEnd(0xFE)
    Return()

    # Function_14_2D7D end

    def Function_15_2F05(): pass

    label("Function_15_2F05")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32E7")

    ChrTalk(
        0x9,
        (
            "#02300FWhen you guys infiltrate the\x01",
            "city tomorrow, I'll start\x01",
            "hacking from the Merkabah.\x02\x03",
            "#02303FWell, do your best to throw\x01",
            "the city into chaos, ok?\x02\x03",
            "#02302FIf they're confused in the real world, \x01",
            "it'll probably create an exploitable \x01",
            "opening in the orbal net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah. Let's both execute\x01",
            "our assigned duties.\x02\x03",
            "#00001F...By the way, Jona... \x01",
            "You're not pulling an all-nighter\x01",
            "tonight, are you? (*stare*)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#02305F...*gulp*\x02\x03",
            "#02309FN-Nah... See? I'm almost\x01",
            "done preparing, but I'm\x01",
            "a night owl, see?\x02\x03",
            "#02304FThe tension of staying up all\x01",
            "night until dawn is a better\x01",
            "feeling than poor sleep, see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FNow look here... Tomorrow's going\x01",
            "to be a long day. You won't hold\x01",
            "out if you'll stay up the entire night.\x02\x03",
            "#00001FIt looks like you're almost finished,\x01",
            "so you should get to bed earlier than\x01",
            "usual. That'll definitely be better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#02306FHehe, I know, I know.\x02\x03",
            "#02300FI'll get to bed right after I'm finished,\x01",
            "so you don't have to glare so much.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 3)
    Jump("loc_337F")

    label("loc_32E7")


    ChrTalk(
        0x9,
        (
            "#02300FI'll be done preparing for\x01",
            "tomorrow's hacking shorty.\x02\x03",
            "#02306FI'll get to bed right after I'm finished,\x01",
            "so you don't have to glare so much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_337F")

    TalkEnd(0xFE)
    Return()

    # Function_15_2F05 end

    def Function_16_3383(): pass

    label("Function_16_3383")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_374B")

    ChrTalk(
        0x12,
        (
            "#02103FThe "Crossbell City Liberation Operation"...\x01",
            "You, who protested the current system,\x01",
            "gathered, and will face it ready to die...\x02\x03",
            "#02101FIf this fails, "The\x01",
            "President was right"\x01",
            "will be the conclusion.\x02\x03",
            "#02103FJust like during the democratization\x01",
            "of Calvard, there was a plot behind the\x01",
            "scenes that's now seen as justified.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI see...\x02\x03",
            "#00001FEverything rests on tomorrow...\x01",
            "We understand well that\x01",
            "it's no exaggeration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#02109FAhaha. I didn't mean to\x01",
            "pressure you, though.\x02\x03",
            "#02103F...As a journalist, my role is to\x01",
            "watch over the fate of Crossbell,\x01",
            "and communicate it to the people.\x02\x03",
            "#02100FBut before a journalist,\x01",
            "I'm a person, and I want\x01",
            "to root for you guys.\x02\x03",
            "#02104FThe ones who were borned from Mr. Guy's\x01",
            "suggestion and inherited his will \x01",
            "is you, the Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FMiss Grace...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#02109FUh uh, for KeA too... You've\x01",
            "got to do your best tomorrow!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, please leave it to us!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 4)
    Jump("loc_37DB")

    label("loc_374B")


    ChrTalk(
        0x12,
        (
            "#02100FBut before a journalist,\x01",
            "I'm a person, and I want\x01",
            "to root for you guys.\x02\x03",
            "#02109FFor KeA too... You've got\x01",
            "to do your best tomorrow!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37DB")

    TalkEnd(0xFE)
    Return()

    # Function_16_3383 end

    def Function_17_37DF(): pass

    label("Function_17_37DF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B4B")

    ChrTalk(
        0x11,
        (
            "#02503F...Tomorrow will most\x01",
            "likely be a rough day.\x02\x03",
            "#02500FAfter all, I made you carry a very\x01",
            "heavy burden to you young ones,\x01",
            ""the fate of the autonomous state".\x02\x03",
            "#02503FAs the autonomous state representative...\x01",
            "Please, allow me to bow my head to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Please, don't say\x01",
            "things like that.\x02\x03",
            "#00000FYou played an important role in\x01",
            "delivering the independence declaration\x01",
            "of invalidity, Chairman MacDowell.\x02\x03",
            "#00004FAs for the rest, I consider it as\x01",
            "a problem that we, who can fight,\x01",
            "must deal with our own hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#02503F...Thank you. I didn't\x01",
            "mean to trouble you.\x02\x03",
            "#02500FIn that case, I believe the "Liberation\x01",
            "Operation" will be a success, and think\x01",
            "about countermeasures going forward.\x02\x03",
            "#02503FTo return the confused citizens of Crossbell\x01",
            "to their former lives as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, please, we're counting on you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 5)
    Jump("loc_3BE6")

    label("loc_3B4B")


    ChrTalk(
        0x11,
        (
            "#02503FI believe the "Liberation Operation"\x01",
            "will be a success, and think about\x01",
            "countermeasures going forward.\x02\x03",
            "#02500F...May the Goddess protect you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BE6")

    TalkEnd(0xFE)
    Return()

    # Function_17_37DF end

    def Function_18_3BEA(): pass

    label("Function_18_3BEA")

    Call(0, 19)
    Return()

    # Function_18_3BEA end

    def Function_19_3BEE(): pass

    label("Function_19_3BEE")

    TalkBegin(0x14)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3BFB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EE5")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",               # 0
            "Buy Equipment\x01",      # 1
            "Buy Items\x01",          # 2
            "Quit\x01",               # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C5E")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3C5E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3C7D")
    OP_AF(0xD8)
    Jump("loc_3CCF")

    label("loc_3C7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_3C8D")
    OP_AF(0xD7)
    Jump("loc_3CCF")

    label("loc_3C8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_3C9D")
    OP_AF(0xD6)
    Jump("loc_3CCF")

    label("loc_3C9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_3CAD")
    OP_AF(0xD5)
    Jump("loc_3CCF")

    label("loc_3CAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_3CBD")
    OP_AF(0xD4)
    Jump("loc_3CCF")

    label("loc_3CBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_3CCD")
    OP_AF(0xD3)
    Jump("loc_3CCF")

    label("loc_3CCD")

    OP_AF(0xD2)

    label("loc_3CCF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3EE0")

    label("loc_3CDE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CFE")
    OP_AF(0xDC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3EE0")

    label("loc_3CFE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D12")
    Jump("loc_3EE0")

    label("loc_3D12")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EE0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E35")

    ChrTalk(
        0x14,
        (
            "I don't know if I can take\x01",
            "an optimistic view of\x01",
            "this situation, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "The police and the Church, the CGF,\x01",
            "Heiyue, a "Divine Wolf" and even\x01",
            ""Yin" have become our allies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "If we have these\x01",
            "members, I think we can\x01",
            "accomplish anything.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3EE0")

    label("loc_3E35")


    ChrTalk(
        0x14,
        (
            "The police and the Church, the CGF,\x01",
            "Heiyue, a "Divine Wolf" and even\x01",
            ""Yin" have become our allies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "If we have these\x01",
            "members, I think we can\x01",
            "accomplish anything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EE0")

    Jump("loc_3BFB")

    label("loc_3EE5")

    TalkEnd(0x14)
    Return()

    # Function_19_3BEE end

    def Function_20_3EE9(): pass

    label("Function_20_3EE9")

    Call(0, 21)
    Return()

    # Function_20_3EE9 end

    def Function_21_3EED(): pass

    label("Function_21_3EED")

    TalkBegin(0x15)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3EFA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4168")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                   # 0
            "Modify/Synthesize\x01",      # 1
            "Quit\x01",                   # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F57")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3F57")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F77")
    OP_AF(0xDD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4163")

    label("loc_3F77")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F8B")
    Jump("loc_4163")

    label("loc_3F8B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4163")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40B9")

    ChrTalk(
        0x15,
        (
            "The biggest problem with\x01",
            "tomorrow's operation will\x01",
            "likely be those three "Aions".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "How to drive away the "Aions"... I think that\x01",
            "will be key to your infiltration in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "We have to cooperate with everyone\x01",
            "and make this operation a success.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4163")

    label("loc_40B9")


    ChrTalk(
        0x15,
        (
            "I think that driving away the three "Aions"\x01",
            "will be key to your infiltration in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "We have to cooperate with everyone\x01",
            "and make this operation a success.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4163")

    Jump("loc_3EFA")

    label("loc_4168")

    TalkEnd(0x15)
    Return()

    # Function_21_3EED end

    def Function_22_416C(): pass

    label("Function_22_416C")

    EventBegin(0x0)
    Fade(500)
    OP_68(100420, 1000, -101760, 0)
    MoveCamera(47, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15480, 0)
    SetChrPos(0x101, 100110, 0, -101660, 180)
    SetChrSubChip(0x10, 0x2)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46DA")

    ChrTalk(
        0x10,
        (
            "#12P#00106FThe Crossbell City liberation operation... \x01",
            "It finally starts tomorrow.\x02\x03",
            "#00108FIf we see Bell or "uncle", I'll ask them the\x01",
            "reasoning behind this chain of events...\x01",
            "And if possible, I want to persuade them.\x02\x03",
            "#00101FBut, if I can't, then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#5P...We won't be able to avoid confronting them.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#12P#00103FYes... And I'm already\x01",
            "prepared to accept that.\x02\x03",
            "#00108FTo repay the many who helped\x01",
            "us heedless of danger...\x02\x03",
            "#00101FAnd above all,\x01",
            "to take back KeA,\x01",
            "we can't lose.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFFFF)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00004F#5P...Say, Elie. There's no need to...\x02\x03",
            "#00000FGet so worked up all by yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#12P#00105FEh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PMr. Dieter and Miss Mariabell\x01",
            "were close persons to us too.\x02\x03",
            "#00001FThat weight is not just on\x01",
            "you, Elie, it's on all of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#12P#00108FLloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F...Let's do our best together tomorrow, Elie.\x01",
            "Everyone, myself included, is with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#12P#00104F...*giggle*, that's right.\x02\x03",
            "#00102FThank you, Lloyd. I feel\x01",
            "a little better now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009F#5PHa ha... You're welcome.\x02",
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x10)
    Sleep(500)

    ChrTalk(
        0x10,
        (
            "#12P#00106F(...U-Umm, Lloyd.)\x02\x03",
            "#00112F(When you're finished preparing for\x01",
            "tomorrow, would you come to the deck?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#5P(Huh...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#12P#00113F(If possible, umm...\x01",
            "I'd like to talk alone,\x01",
            "just the two of us...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 5)
    Jump("loc_4781")

    label("loc_46DA")


    ChrTalk(
        0x10,
        (
            "#12P#00112F(When you're finished preparing for\x01",
            "tomorrow, would you come to the deck?)\x02\x03",
            "#00113F(If possible, umm...\x01",
            "I'd like to talk alone,\x01",
            "just the two of us...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4781")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Accept Elie's Invitation\x01",      # 0
            "Decline\x01",                       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_485E")

    ChrTalk(
        0x101,
        (
            "#00002F#5P(...I-I understand. If you're okay\x01",
            "with me, I would love to go.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#12P#00109F(...*giggle*, thank you.\x01",
            "See you later, then.)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 27)
    SetScenarioFlags(0x1AA, 3)
    Jump("loc_4921")

    label("loc_485E")


    ChrTalk(
        0x10,
        (
            "#12P#00106F(...I see.)\x02\x03",
            "#00102F(*giggle*, don't worry about it.\x01",
            "It's not a big deal.)\x02\x03",
            "#00104F(If you change your mind,\x01",
            "please speak with me again.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5P(Sure, I'll be sure to.)\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_4921")

    SetChrSubChip(0x10, 0x0)
    EventEnd(0x5)
    Return()

    # Function_22_416C end

    def Function_23_4928(): pass

    label("Function_23_4928")

    EventBegin(0x0)
    Fade(500)
    OP_68(-3160, -500, 6480, 0)
    MoveCamera(52, 29, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16170, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 6)), scpexpr(EXPR_END)), "loc_496A")
    SetChrSubChip(0xB, 0x1)

    label("loc_496A")

    SetChrPos(0x101, -3610, -1500, 5780, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EAE")

    ChrTalk(
        0xB,
        (
            "#11P#00203F(*klak klak klak klak*...)\x02\x03",
            "#00200FHmm. Preparations are complete for now.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xB)

    ChrTalk(
        0xB,
        (
            "#11P#00208F(*keystroke*)\x02\x03",
            "#00203F............\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005F...Umm, Tio? \x01",
            "What're you doing?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0xB, 0x1)

    ChrTalk(
        0xB,
        (
            "#5P#00202F...I was performing a final\x01",
            "check of the Merkabah's\x01",
            "systems for tomorrow's sortie.\x02\x03",
            "#00203FAlthough I am planning to disembark\x01",
            "tomorrow with all of you...\x02\x03",
            "#00200FAfter gaining control of the communication\x01",
            "mainframe, I'll have to leave the hacking\x01",
            "and the rest to Jona and Miss Fran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FI see... \x01",
            "That seems tough.\x02\x03",
            "#00000FIs there anything I could help with?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#00203F...No, not especially.\x02\x03",
            "#00202FGiven my field, Jona\x01",
            "here should be enough.\x02\x03",
            "#00204FIt's enough if Mr. Lloyd\x01",
            "remains unperturbed\x01",
            "like a leader would.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00006FNo, no. I've got lots to do\x01",
            "to prepare for tomorrow.\x02\x03",
            "#00000FWell, I'll leave\x01",
            "it to you, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xB)
    Sleep(500)

    ChrTalk(
        0xB,
        (
            "#5P#00203F...Come to think of it,\x01",
            "there is one thing.\x02\x03",
            "#00208FActually... There is something I would\x01",
            "like to discuss with you, Mr. Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FSomething to discuss...? Is there\x01",
            "something you're worried about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#00206F...No, not here.\x02\x03",
            "#00201FOnce you have finished what you\x01",
            "need to, will you come to the\x01",
            "Merkabah's deck later?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 6)
    ClearChrFlags(0xB, 0x10)
    Jump("loc_4F66")

    label("loc_4EAE")


    ChrTalk(
        0xB,
        (
            "#5P#00206FActually... There is something I would\x01",
            "like to discuss with you, Mr. Lloyd.\x02\x03",
            "#00201FOnce you have finished what you\x01",
            "need to, will you come to the\x01",
            "Merkabah's deck later?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F66")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Accept Tio's Invitation\x01",      # 0
            "Decline\x01",                      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_504B")

    ChrTalk(
        0x101,
        (
            "#12P#00002FUnderstood. If you're okay with me, I\x01",
            "would be happy to discuss this with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#00209FUh uh... \x01",
            "I will be counting on you then.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 27)
    SetScenarioFlags(0x1AA, 4)
    Jump("loc_50D3")

    label("loc_504B")


    ChrTalk(
        0xB,
        (
            "#5P#00204F...I see. Well, it\x01",
            "can't be helped.\x02\x03",
            "#00202FIf you change your mind,\x01",
            "speak with me again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYeah, got it.\x02",
    )

    OP_5A()
    CloseMessageWindow()

    label("loc_50D3")

    SetChrSubChip(0xB, 0x0)
    EventEnd(0x5)
    Return()

    # Function_23_4928 end

    def Function_24_50DA(): pass

    label("Function_24_50DA")

    EventBegin(0x0)
    Fade(500)
    OP_68(98200, 1000, 600, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16090, 0)
    SetChrPos(0x101, 97510, 0, -530, 0)
    SetChrSubChip(0xE, 0x2)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56F6")

    ChrTalk(
        0xE,
        "#5P#00300FYo, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FIt looks like you guys are\x01",
            "maintaining your weapons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5P#00302FYeah. They say tomorrow's operation\x01",
            "will be the biggest turning point yet.\x02\x03",
            "#00304FIt'll probably be "Berserker"'s\x01",
            "turn too, so I want to make sure\x01",
            "he's ready when the time comes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FHmm. I suppose there really hasn't been\x01",
            "many chances to make noise up until now...\x02\x03",
            "#00003FMaybe I should repair\x01",
            "my tonfas tonight, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5P#00309FYeah, that's the way.\x02\x03",
            "#00303FUnlike a rifle, yours\x01",
            "don't have any small parts\x01",
            "that need maintenance...\x02\x03",
            "#00300FJust throwing some polish\x01",
            "on there might be enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00009FHa ha, that's right.\x02\x03",
            "#00005FEven so... You're more\x01",
            "diligent than I thought.\x02\x03",
            "#00000FIt looks like you haven't missed a\x01",
            "single day maintaining not just that\x01",
            "rifle but your Stunhalberd as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5P#00302FWell, weapon maintenance is\x01",
            "just the basics of the basics.\x02\x03",
            "#00304FYou've got to treat them just as if they were\x01",
            "peerless beauties: gently and carefully.\x02\x03",
            "#00300FIf you don't, you'll find\x01",
            "yourself in unnecessary\x01",
            "trouble in battle──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xE)

    ChrTalk(
        0x101,
        (
            "#12P#00011F...Sorry. Could I have made you\x01",
            "remember something unpleasant?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5P#00309F...Ha ha, what're you aplogizin' for?\x02\x03",
            "#00306F...But you're right.\x02\x03",
            "#00308FMaybe...it's about time\x01",
            "I told you about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5P#00300FSay, if you're free later, want\x01",
            "to come to the Merkabah's deck?\x02\x03",
            "I'd just like you to join\x01",
            "me for a little while.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 7)
    Jump("loc_5777")

    label("loc_56F6")


    ChrTalk(
        0xE,
        (
            "#5P#00300FHey. If you're free later, want\x01",
            "to come to the Merkabah's deck?\x02\x03",
            "I'd just like you to join\x01",
            "me for a little while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5777")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Accept Randy's Invitation\x01",      # 0
            "Decline\x01",                        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5865")

    ChrTalk(
        0x101,
        (
            "#12P#00002F...Understood. \x01",
            "I'll go there later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5P#00309FHa ha. Later, then.\x02\x03",
            "#00302FI'll be right there once I finish\x01",
            "maintaining this little guy.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 27)
    SetScenarioFlags(0x1AA, 5)
    Jump("loc_590A")

    label("loc_5865")


    ChrTalk(
        0xE,
        (
            "#5P#00306F...I see. It's not\x01",
            "like it was something\x01",
            "especially fun, but...\x02\x03",
            "#00300FIf you change your mind,\x01",
            "speak with me again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYeah, I'll do.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_590A")

    SetChrSubChip(0xE, 0x0)
    EventEnd(0x5)
    Return()

    # Function_24_50DA end

    def Function_25_5911(): pass

    label("Function_25_5911")

    EventBegin(0x0)
    Fade(500)
    OP_68(100500, 1000, -240, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16970, 0)
    SetChrPos(0x101, 100340, 0, -1010, 0)
    SetChrSubChip(0xF, 0x1)
    OP_93(0xC, 0xB4, 0x0)
    OP_4B(0xC, 0xFF)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6099")

    ChrTalk(
        0xF,
        "#5P#10100FMr. Lloyd, good work today!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5P#01902FGood work today!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FGood work, Noｱl and Fran.\x02\x03",
            "#00009FYou are somehow calm heading\x01",
            "into tomorrow's operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5P#10102FUmm, sorry.\x02\x03",
            "#10106FI was maintaining my weapons\x01",
            "when Fran came in...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5P#01909FUh uh, I came to\x01",
            "support big siiis.\x02\x03",
            "#01904FI've already finished\x01",
            "preparing for tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00004FHa ha, how dependable.\x02\x03",
            "#00000FFran, you'll have to work\x01",
            "as an operator for us, so\x01",
            "restore your batteries, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5P#01902FYes, of cooourse.\x01",
            "...And that's why\x01",
            "I've come here!\x02\x03",
            "#01909FAfter all, my energies\x01",
            "are refilled just by being\x01",
            "by my big sis' side!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xF, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00012FHa ha. That doesn't seem\x01",
            "like a joke, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5P#10106F*sigh*, c'mon... At least\x01",
            "stay out of my way, ok?\x02\x03",
            "#10102FU-Umm, Mr. Lloyd. \x01",
            "I'd like to get in contact with the\x01",
            "Commander once more tonight.\x02\x03",
            "#10103FI think we should get final confirmation\x01",
            "before tomorrow's operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FYeah. I'll be counting on you.\x02\x03",
            "#00003FYou'll be infiltrating the\x01",
            "city with us tomorrow, Noｱl...\x02\x03",
            "#00000FOnce everything's ready, make\x01",
            "sure you get proper rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#5P#10109FYes sir!\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xC)

    ChrTalk(
        0xC,
        (
            "#11P#01905F(Hey, hey big sis. Don't you feel\x01",
            "that today's conversation\x01",
            "will end at this rate?)\x02\x03",
            "#01909F(This is your chance! Are you\x01",
            "sure you're okay with thiiis?)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xF,
        (
            "#5P#10111F(C-Chance, you say?\x01",
            "...Fran, cut that out...!)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00005F...Umm, what's wrong?\x01",
            "Is there some kind of problem?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xF)

    ChrTalk(
        0xF,
        "#5P#10114FN-No, umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11P#01909F(Go for it, big sis!!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5P#10103F...Umm... Later is fine, but can\x01",
            "I ask you to come to the deck?\x02\x03",
            "#10101FIt's not a big deal, but\x01",
            "there's something I'd\x01",
            "like to ask you, Mr. Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 0)
    Jump("loc_611E")

    label("loc_6099")


    ChrTalk(
        0xF,
        (
            "#5P#10103F...Can you come to the deck later?\x02\x03",
            "#10101FIt's not a big deal, but\x01",
            "there's something I'd\x01",
            "like to ask you, Mr. Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_611E")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Accept Noｱl's Invitation\x01",      # 0
            "Decline\x01",                        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_622F")

    ChrTalk(
        0x101,
        (
            "#12P#00002FYeah, understood. I feel\x01",
            "it's unusual for you to ask\x01",
            "me something though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11P#01909F(Way to go, big sis!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5P#10114FT-Then... I'll\x01",
            "head there once\x01",
            "I'm finished here.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 27)
    SetScenarioFlags(0x1AA, 6)
    Jump("loc_6335")

    label("loc_622F")


    ChrTalk(
        0xF,
        (
            "#5P#10106FI-Is that so...\x02\x03",
            "#10112FNo, please don't worry\x01",
            "about it! It's really\x01",
            "not a big deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5P#01906FMrr. I guess it can't be heeelped.\x02\x03",
            "#01901FMr. Lloyd, if you change\x01",
            "your mind, please speak\x01",
            "with big sis again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYeah, understood.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_6335")

    SetChrSubChip(0xF, 0x0)
    OP_93(0xC, 0x10E, 0x0)
    OP_4C(0xC, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_25_5911 end

    def Function_26_6347(): pass

    label("Function_26_6347")

    EventBegin(0x0)
    Fade(500)
    OP_68(102260, 800, -94610, 0)
    MoveCamera(48, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16290, 0)
    SetChrPos(0x101, 100450, 0, -95200, 90)
    SetChrSubChip(0x8, 0x2)
    SetChrSubChip(0xA, 0x1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B24")

    ChrTalk(
        0x101,
        (
            "#6P#00005FWazy, Abbas... Are\x01",
            "you guys drinking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#10404FBoth of us have finished\x01",
            "preparing for now, you see.\x02\x03",
            "#10402FHu hu, care to join us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FHey now... Will you be all right,\x01",
            "even though the operation's tomorrow?\x02\x03",
            "#00001FIt looks like there're already\x01",
            "a lot of empty glasses there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#12100FNo need to worry.\x01",
            "They're Ventos' non-\x01",
            "alcoholic cocktails.\x02\x03",
            "They'll be no obstacle\x01",
            "to tomorrow's operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FO-Oh, I see...\x02\x03",
            "#00000FWell if you say so Abbas,\x01",
            "I think I'll trust you this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#10409FHu hu. I wouldn't mind it if you\x01",
            "believed me when I drink alone too.\x02\x03",
            "#10403F...That's right, I should\x01",
            "have told you guys earlier.\x02\x03",
            "#10400FOfficial permission has been given\x01",
            "from His Eminence, the Pope, for \x01",
            "participation in tomorrow's operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FAh... I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#12100FThe Merkabah operates in secret.\x01",
            "We normally avoid its use during\x01",
            "large scale operations, but...\x02\x03",
            "When we thought about the confusion \x01",
            "across the continent, perhaps a little \x01",
            "exposure can't be avoided.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FI see.. I'm grateful for\x01",
            "the Church's decision.\x02\x03",
            "#00013F...Anyway, the operation's\x01",
            "tomorrow. Let's do this, Wazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11P#10402FHu hu, roger that, leader.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#12102FAllow us to assist you, of course.\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "#11P#10403FOh... that's right.\x01",
            "There's just one more\x01",
            "thing I should tell you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00005FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#12100F...Wazy. That matter\x01",
            "is confidential at the\x01",
            "present time, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#10405FOh, really?\x02\x03",
            "#10409FHu hu, then I'll tell you\x01",
            "as secretly as possible.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#5P#12100F...Whatever. If Wazy says\x01",
            "so, then it can't be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00012FI-I don't really\x01",
            "get it, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#10404FHu hu. I'm telling you, this has\x01",
            "great relevance to you guys.\x02\x03",
            "#10402F──If you're interested\x01",
            "in it, can we talk on\x01",
            "the deck later?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 1)
    Jump("loc_6BAD")

    label("loc_6B24")


    ChrTalk(
        0xA,
        (
            "#11P#10404FThere's just one more\x01",
            "thing I should tell you.\x02\x03",
            "#10402FHu hu. If you're\x01",
            "interested in it, can we\x01",
            "talk on the deck later?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BAD")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Accept Wazy's Invitation\x01",      # 0
            "Decline\x01",                       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D32")

    ChrTalk(
        0x101,
        (
            "#6P#00006F...Understood. \x01",
            "I just need to go to the deck, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11P#10409FHu hu, it's decided then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#12100FWazy, let me just say this. \x01",
            "Take care not say any more than...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#10404FHu hu, I know, I know.\x02\x03",
            "#10400FI'll head there once I've finished my\x01",
            "drink, so there's no need to hurry.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 27)
    SetScenarioFlags(0x1AA, 7)
    Jump("loc_6DA0")

    label("loc_6D32")


    ChrTalk(
        0xA,
        (
            "#11P#10405F...Really? \x01",
            "That's fine, but...\x02\x03",
            "#10404FHu hu, if you change your\x01",
            "mind, speak with me again.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_6DA0")

    SetChrSubChip(0xA, 0x0)
    SetChrSubChip(0x8, 0x0)
    EventEnd(0x5)
    Return()

    # Function_26_6347 end

    def Function_27_6DAB(): pass

    label("Function_27_6DAB")

    FadeToDark(500, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 3)), scpexpr(EXPR_END)), "loc_6E73")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F(...I'll have to apologize to\x01",
            "Elie for not being able to go.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd apologized to Elie for not\x01",
            "being able to go as promised.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 3)
    Jump("loc_72A3")

    label("loc_6E73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 4)), scpexpr(EXPR_END)), "loc_6F2E")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F(...I'll have to apologize to\x01",
            "Tio for not being able to go.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd apologized to Tio for not\x01",
            "being able to go as promised.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 4)
    Jump("loc_72A3")

    label("loc_6F2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 5)), scpexpr(EXPR_END)), "loc_6FED")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F(...I'll have to apologize to\x01",
            "Randy for not being able to go.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd apologized to Randy for not\x01",
            "being able to go as promised.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 5)
    Jump("loc_72A3")

    label("loc_6FED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 6)), scpexpr(EXPR_END)), "loc_70AA")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F(...I'll have to apologize to\x01",
            "Noｱl for not being able to go.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd apologized to Noｱl for not\x01",
            "being able to go as promised.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 6)
    Jump("loc_72A3")

    label("loc_70AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 7)), scpexpr(EXPR_END)), "loc_7167")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F(...I'll have to apologize to\x01",
            "Wazy for not being able to go.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd apologized to Wazy for not\x01",
            "being able to go as promised.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 7)
    Jump("loc_72A3")

    label("loc_7167")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 0)), scpexpr(EXPR_END)), "loc_7226")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F(...I'll have to apologize to\x01",
            "Rixia for not being able to go.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd apologized to Rixia for not\x01",
            "being able to go as promised.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AB, 0)
    Jump("loc_72A3")

    label("loc_7226")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00003F(...I'll head to the deck once\x01",
            "my preparations for tomorrow\x01",
            "are complete at the nap room.)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_72A3")

    Return()

    # Function_27_6DAB end

    def Function_28_72A4(): pass

    label("Function_28_72A4")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_78CA")
    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x101, 1420, 0, -92300, 90)
    OP_68(2300, 1000, -92050, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 3)), scpexpr(EXPR_END)), "loc_73BC")

    ChrTalk(
        0x101,
        (
            "#00005F#6P(Come to think of it... \x01",
            "I promised to speak with Elie.)\x02\x03",
            "#00003F(......)\x02\x03",
            "#00000F(...W-What should I do? Am I\x01",
            "finished preparing for tomorrow?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_771E")

    label("loc_73BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 4)), scpexpr(EXPR_END)), "loc_7469")

    ChrTalk(
        0x101,
        (
            "#00005F#6P(Come to think of it... \x01",
            "I promised to speak with Tio.)\x02\x03",
            "#00003F(......)\x02\x03",
            "#00000F(...W-What should I do? Am I\x01",
            "finished preparing for tomorrow?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_771E")

    label("loc_7469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 5)), scpexpr(EXPR_END)), "loc_7518")

    ChrTalk(
        0x101,
        (
            "#00005F#6P(Come to think of it... \x01",
            "I promised to speak with Randy.)\x02\x03",
            "#00003F(......)\x02\x03",
            "#00000F(...W-What should I do? Am I\x01",
            "finished preparing for tomorrow?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_771E")

    label("loc_7518")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 6)), scpexpr(EXPR_END)), "loc_75C6")

    ChrTalk(
        0x101,
        (
            "#00005F#6P(Come to think of it... \x01",
            "I promised to speak with Noｱl.)\x02\x03",
            "#00003F(......)\x02\x03",
            "#00000F(...W-What should I do? Am I\x01",
            "finished preparing for tomorrow?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_771E")

    label("loc_75C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 7)), scpexpr(EXPR_END)), "loc_7674")

    ChrTalk(
        0x101,
        (
            "#00005F#6P(Come to think of it... \x01",
            "I promised to speak with Wazy.)\x02\x03",
            "#00003F(......)\x02\x03",
            "#00000F(...W-What should I do? Am I\x01",
            "finished preparing for tomorrow?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_771E")

    label("loc_7674")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 0)), scpexpr(EXPR_END)), "loc_771E")

    ChrTalk(
        0x101,
        (
            "#00005F#6P(Come to think of it... \x01",
            "I promised to speak with Rixia.)\x02\x03",
            "#00003F(......)\x02\x03",
            "#00000F(...W-What should I do? Am I\x01",
            "finished preparing for tomorrow?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_771E")

    Sound(814, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Free time and the day will end, and events\x01",
            "will proceed, so please be aware of that.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[I Still Have Other Things To Do]\x01",            # 0
            "[Speak with the Person You Promised To]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7815"),
        (1, "loc_781A"),
        (SWITCH_DEFAULT, "loc_78B1"),
    )


    label("loc_7815")

    Jump("loc_78B1")

    label("loc_781A")

    StopSound(498, 1500, 70)
    FadeToDark(1500, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "After that── Lloyd finished his preparations\x01",
            "for tomorrow and went out onto the deck at night.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x22, 0)
    NewScene("e440B", 0, 0, 0)
    IdleLoop()
    Jump("loc_78B1")

    label("loc_78B1")

    OP_5A()
    SetChrPos(0x0, 550, 0, -92390, 270)
    EventEnd(0x5)
    Jump("loc_7C5F")

    label("loc_78CA")


    ChrTalk(
        0x101,
        (
            "#00005F(...I wonder if I should\x01",
            "turn in early tonight?)\x02\x03",
            "#00003F(Although, it might be better\x01",
            "to see how everyone's doing\x01",
            "before tomorrow's operation...)\x02",
        )
    )

    CloseMessageWindow()
    Sound(814, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If you choose to rest in the nap room,\x01",
            "the day will end and events will proceed,\x01",
            "so please be aware of that.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Sleep(300)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[I Still Have Other Things to Do]\x01",      # 0
            "[End Free Time and Rest]\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A73")
    Jump("loc_7C5F")

    label("loc_7A73")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C5F")
    EventBegin(0x0)
    Fade(500)
    OP_68(2040, 1000, -91940, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 1300, 0, -92030, 90)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003F#6P(...At the nap room, I'll get everything\x01",
            "ready, and then get some sleep tonight.)\x02\x03",
            "#00001F(Tomorrow's the Crossbell City liberation\x01",
            "operation... We will definitely make it a success!)\x02",
        )
    )

    CloseMessageWindow()
    Sound(100, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0xA, 0x1, 0x8)
    Sleep(500)

    def lambda_7BDD():
        OP_95(0xFE, 4300, 0, -92030, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7BDD)
    Sleep(1000)
    StopSound(498, 2000, 70)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(1000)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x23, 1)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    EventEnd(0x3)

    label("loc_7C5F")

    TalkEnd(0xFF)
    Return()

    # Function_28_72A4 end

    def Function_29_7C63(): pass

    label("Function_29_7C63")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x0, -150, 0, -88230, 180)
    EventEnd(0x5)
    Return()

    # Function_29_7C63 end

    def Function_30_7C83(): pass

    label("Function_30_7C83")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50203.itc", 0x1E)
    LoadChrToIndex("chr/ch06902.itc", 0x1F)
    LoadChrToIndex("chr/ch06000.itc", 0x20)
    LoadChrToIndex("chr/ch05800.itc", 0x21)
    SoundLoad(943)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7CBD")
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_7CBD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7CD0")
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_7CD0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7CE3")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_7CE3")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x2)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xC, 0x4)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0x20)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x11, 0x21)
    SetChrSubChip(0x11, 0x0)
    SetChrSubChip(0x13, 0x5)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    OP_74(0x1, 0x14)
    OP_70(0x1, 0x24)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "And thusly── the impenetrable "barrier"\x01",
            "surrounding Crossbell City disappeared.\x02\x03",
            "Lloyd contacted Cao of "Heiyue"\x01",
            "and Mireille of the Resistance...\x02\x03",
            "Furthermore, Commander Sonya and\x01",
            "her Bellguard and Tangram units\x01",
            "promised to remain neutral.\x02\x03",
            "And then──\x02\x03",
            "That night, there was a call from\x01",
            "Father Kevin to the Merkabah's bridge.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x9, -3150, -1350, 7150, 315)
    SetChrPos(0x13, 2900, 0, -850, 0)
    SetChrPos(0x11, -3300, 0, 250, 45)
    SetChrPos(0x12, -3800, 0, -1000, 45)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    SetChrPos(0xC, 3000, -1350, 6960, 45)
    SetChrPos(0x101, -750, 250, 200, 0)
    SetChrPos(0x102, 0, 0, -450, 0)
    SetChrPos(0x104, 650, 0, -1250, 0)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x103, -1460, 0, -1190, 0)
    SetChrPos(0x109, -700, 0, -1770, 0)
    SetChrPos(0x106, 200, 0, -2200, 0)
    PlayBGM("ed7583", 0)
    Sound(498, 1, 80, 0)
    FadeToBright(1000, 0)
    OP_68(660, 800, 3830, 0)
    MoveCamera(44, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetCameraDistance(22500, 2000)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)
    SetMessageWindowPos(95, 70, -1, -1)
    SetChrName("Father Kevin")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──All righty then. You've\x01",
            "entered their firing range but\x01",
            "there's no sign of attack?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x105,
        (
            "#10403F#6PYeah, it seems the Aions are\x01",
            "focused on city defense.\x02\x03",
            "#10400FWe should be fine as long as we don't\x01",
            "get any closer to Crossbell City.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(90, -1, -1, -1)
    SetChrName("Father Kevin")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Alright, I think I've got a\x01",
            "rough idea of the situation.\x02\x03",
            "I'll return there tomorrow at dawn.\x02\x03",
            "We'll talk about the\x01",
            "timing then.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x105,
        "#10402F#6PHu hu, roger.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(190, -1, -1, -1)
    SetChrName("Ries' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2S...Kevin, switch with me.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(250)
    OP_70(0x1, 0x1F)
    Sound(73, 0, 100, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x102,
        "#00102F#12PMiss Ries...\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(160, -1, -1, -1)
    SetChrName("Sister Ries")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "...Miss Elie. Thank\x01",
            "goodness you're safe.\x02\x03",
            "And Mr. Lloyd and \x01",
            "everyone else, too.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00002F#12PHa ha, fortunately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#12PMan, I didn't think I'd get to\x01",
            "talk to you like this, dear Ries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#12P#NYou are helping us with our\x01",
            "infiltration, aren't you?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(140, 70, -1, -1)
    SetChrName("Sister Ries")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yes. We plan to distract the\x01",
            "Aion units protecting the\x01",
            "city with our Merkabah.\x02\x03",
            "We can't deal with the jaegers\x01",
            "or the State Guard, though...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00004F#12P...That's plenty.\x01",
            "It's really a great help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#12PMiss Ries, Father Kevin... \x01",
            "I don't know how we can ever thank you...\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(90, -1, -1, -1)
    SetChrName("Father Kevin")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Well if you want to thank us, you can conduct\x01",
            "this operation safely and successfully.\x02\x03",
            "We do intend to back you\x01",
            "up a little bit, but...\x02\x03",
            "It'll be plenty tough going\x01",
            "up against those dolls.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x103,
        "#00208F#12P#NIndeed...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00301F#12PWell, don't do anything\x01",
            "too reckless, alright?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(105, -1, -1, -1)
    SetChrName("Father Kevin")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ha ha, thanks.\x02\x03",
            "──Wazy. See you \x01",
            "tomorrow morning.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x105,
        "#10400F#6PYeah, I'll be waiting.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(180, -1, -1, -1)
    SetChrName("Sister Ries")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Excuse me then.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(250)
    OP_70(0x1, 0x1E)
    Sound(73, 0, 100, 0)
    OP_0D()
    Sleep(500)
    Sound(943, 2, 60, 0)
    OP_71(0x1, 0x2F, 0x4C, 0x0, 0x8)
    OP_68(-340, 800, 2640, 2000)
    MoveCamera(40, 22, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(22440, 2000)
    Sleep(1000)
    SetChrFlags(0x13, 0x20)

    def lambda_8785():
        TurnDirection(0x11, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_8785)
    Sleep(50)

    def lambda_8795():
        TurnDirection(0x12, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_8795)
    Sleep(50)

    def lambda_87A5():
        TurnDirection(0x13, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_87A5)
    Sleep(50)
    WaitChrThread(0x11, 0)
    WaitChrThread(0x12, 0)
    WaitChrThread(0x13, 0)
    OP_6F(0x79)
    ClearChrFlags(0x13, 0x20)
    OP_24(0x3AF)
    Sound(143, 0, 50, 0)
    Sleep(500)

    ChrTalk(
        0x11,
        (
            "#02501F#5P──Mmm. Looks like this is\x01",
            "going to be one tough day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#02106F#6P#NRight... On the surface, the\x01",
            "President's combat strength\x01",
            "far exceeds our own.\x02\x03",
            "#02101FAnd that's not even including those\x01",
            "dolls. How strong can you get?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x106,
        (
            "#10708F#12PAccording to Meister Jｶrg, the\x01",
            "white frame's "Space Annihilation"\x01",
            "power can no longer be used, but...\x02\x03",
            "#10701FEven so, its basic functions\x01",
            "haven't changed at all, right?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#12100F#5PYes, I think it's\x01",
            "safe to assume that.\x02\x03",
            "This No. 9 unit will need to\x01",
            "keep an eye on that white frame.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#5PIn any case, the battles at the city\x01",
            "perimeter are expected to be stalemates.\x02\x03",
            "#10401FTherefore, we infiltrators\x01",
            "will be holding the key.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#12PYeah, I know.\x02\x03",
            "#00013F...We need to sneak inside\x01",
            "somehow and rendezvous with the\x01",
            "Chief, Mr. Dudley and the others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#11PBut, are they all right?\x02\x03",
            "#00301FWhen Dudley contacted us, the signal\x01",
            "was cut right in the middle of it.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x1)
    Sleep(200)

    ChrTalk(
        0x9,
        (
            "#02305F#5PProbably, the communication\x01",
            "mainframe was forcibly isolated.\x02\x03",
            "#02303FThey probably made it so that specific\x01",
            "ENIGMA serial numbers can't send or receive.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0x2)
    Sleep(100)

    ChrTalk(
        0xC,
        (
            "#01901F#5PThen the President\x01",
            "can transmit in the\x01",
            "city and we can't?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#12PYes. It seems we need to gain control\x01",
            "of the communications mainframe.\x02\x03",
            "#00208FIt is inside Orchis Tower,\x01",
            "so it won't be that easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#12PIn any case... Everything\x01",
            "starts tomorrow morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#12PYes... The "Crossbell City\x01",
            "Liberation Operation".\x02\x03",
            "#00101FTo have any chance of freeing KeA\x01",
            "too, we have to make it a success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PYeah... Tonight we need to rest\x01",
            "and get ready for tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00004F#5PEveryone, there's a nap room,\x01",
            "so if you're tired, please rest.\x02\x03",
            "#00000FLet's face tomorrow head on...\x01",
            "Fully prepared.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    SetMessageWindowPos(290, 50, -1, -1)
    SetChrName("All")

    AnonymousTalk(
        0xFF,
        "#4SRight!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetCameraDistance(22940, 2000)
    StopSound(498, 2000, 80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(1)
    ClearChrFlags(0x105, 0x4)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    SetScenarioFlags(0x1A5, 2)
    OP_29(0xB0, 0x4, 0x10)
    OP_29(0xB1, 0x4, 0x2)
    OP_29(0xB1, 0x1, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x79), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8F5F")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8F5F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7A), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8F76")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8F76")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7B), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8F8D")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8F8D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7D), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8FA4")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8FA4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7C), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8FBB")
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8FBB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7E), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8FD2")
    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8FD2")

    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7513", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x201), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(498, 1, 80, 0)
    OP_24(0x3AF)
    Sleep(500)
    SetScenarioFlags(0x22, 2)
    NewScene("e302B", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_30_7C83 end

    SaveToFile()

Try(main)
