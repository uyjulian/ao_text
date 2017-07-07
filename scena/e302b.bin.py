from ScenarioHelper import *

def main():
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
        "Positive knight Abbas",         # 1
        "Yona",                   # 2
        "Waji",                   # 3
        "Tio",                 # 4
        "Franc",                 # 5
        "Lisha",               # 6
        "Randy",               # 7
        "Noel",                 # 8
        "Erie",                 # 9
        "McDowell",         # 10
        "Grace",               # 11
        "God wolf Zeit",           # 12
        "Adjunct Ventos",       # 13
        "Adjunctive Juno",         # 14
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
        "Function_4_71C",          # 04, 4
        "Function_5_857",          # 05, 5
        "Function_6_DF9",          # 06, 6
        "Function_7_1193",         # 07, 7
        "Function_8_1738",         # 08, 8
        "Function_9_1AED",         # 09, 9
        "Function_10_1C55",        # 0A, 10
        "Function_11_2190",        # 0B, 11
        "Function_12_230D",        # 0C, 12
        "Function_13_2942",        # 0D, 13
        "Function_14_2BA6",        # 0E, 14
        "Function_15_2D2E",        # 0F, 15
        "Function_16_311A",        # 10, 16
        "Function_17_3549",        # 11, 17
        "Function_18_38D5",        # 12, 18
        "Function_19_38D9",        # 13, 19
        "Function_20_3BEB",        # 14, 20
        "Function_21_3BEF",        # 15, 21
        "Function_22_3E28",        # 16, 22
        "Function_23_45CD",        # 17, 23
        "Function_24_4D08",        # 18, 24
        "Function_25_5484",        # 19, 25
        "Function_26_5EF4",        # 1A, 26
        "Function_27_688F",        # 1B, 27
        "Function_28_6D6A",        # 1C, 28
        "Function_29_76DB",        # 1D, 29
        "Function_30_76FB",        # 1E, 30
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

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6CF")
    RunExpression(0x5, (scpexpr(EXPR_EXEC_OP, "OP_E5(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_END)),
        (0, "loc_5AC"),
        (1, "loc_5DB"),
        (2, "loc_6B3"),
        (3, "loc_6BB"),
        (SWITCH_DEFAULT, "loc_6CA"),
    )


    label("loc_5AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5CB")
    OP_2B(0x9A, 0x9B, 0x9C, 0x96, 0x97, 0x98, 0x99, 0xFFFF)
    Jump("loc_5D6")

    label("loc_5CB")

    OP_2B(0x96, 0x97, 0x98, 0x99, 0xFFFF)

    label("loc_5D6")

    Jump("loc_6CA")

    label("loc_5DB")

    SetMapFlags(0x40000000)
    OP_E5(0x7)
    Sleep(500)
    SetChrName("Automatic announcement")

    AnonymousTalk(
        0xFF,
        "This is Crosbell Police.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E5(0x4)"), scpexpr(EXPR_END)), "loc_683")

    AnonymousTalk(
        0xFF,
        "We will receive reports.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x8, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xC)
    SetChrName("Automatic announcement")

    AnonymousTalk(
        0xFF,
        (
            "Finish report processing.\x01",
            "Thank you for your hard work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A5")

    label("loc_683")


    AnonymousTalk(
        0xFF,
        "There are no reportable requests.\x02",
    )

    CloseMessageWindow()

    label("loc_6A5")

    OP_57(0x0)
    OP_E5(0x8)
    ClearMapFlags(0x40000000)
    Jump("loc_6CA")

    label("loc_6B3")

    Call(0, 4)
    Jump("loc_6CA")

    label("loc_6BB")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6CA")

    label("loc_6CA")

    Jump("loc_573")

    label("loc_6CF")

    OP_E5(0x6)
    OP_C9(0x1, 0x4)
    OP_C9(0x1, 0x100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_70C")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 5)
    Return()

    label("loc_70C")

    FadeToBright(1000, 0)
    OP_0D()
    OP_E5(0xB)
    TalkEnd(0xFF)
    Return()

    # Function_3_54E end

    def Function_4_71C(): pass

    label("Function_4_71C")

    OP_E5(0x6)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 3)), scpexpr(EXPR_END)), "loc_73E")
    SetScenarioFlags(0x2A, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_73E")
    ClearScenarioFlags(0x2A, 0)

    label("loc_73E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 4)), scpexpr(EXPR_END)), "loc_75B")
    SetScenarioFlags(0x2A, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_75B")
    ClearScenarioFlags(0x2A, 1)

    label("loc_75B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 5)), scpexpr(EXPR_END)), "loc_778")
    SetScenarioFlags(0x2A, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_778")
    ClearScenarioFlags(0x2A, 2)

    label("loc_778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 6)), scpexpr(EXPR_END)), "loc_795")
    SetScenarioFlags(0x2A, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_795")
    ClearScenarioFlags(0x2A, 3)

    label("loc_795")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 7)), scpexpr(EXPR_END)), "loc_7B2")
    SetScenarioFlags(0x2A, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B2")
    ClearScenarioFlags(0x2A, 4)

    label("loc_7B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 0)), scpexpr(EXPR_END)), "loc_7CF")
    SetScenarioFlags(0x2A, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7CF")
    ClearScenarioFlags(0x2A, 5)

    label("loc_7CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 1)), scpexpr(EXPR_END)), "loc_7DB")
    SetScenarioFlags(0x2A, 6)

    label("loc_7DB")

    OP_24(0x1F2)
    RunExpression(0x9, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1F()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_820")
    Sound(498, 1, 50, 0)
    Jump("loc_826")

    label("loc_820")

    Sound(498, 1, 100, 0)

    label("loc_826")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_856")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_856")

    Return()

    # Function_4_71C end

    def Function_5_857(): pass

    label("Function_5_857")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_END)), "loc_8C0")
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, 102700, 0, -102930, 180)

    label("loc_8C0")

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
            "#00205FGee\x02\x03",
            "#00204FApparently Lloyd said,\x01",
            "\"Pomutto! 'From everyone\x01",
            "You seem to have won.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01905FWell, really? ~! Is it?\x02\x03",
            "#01909FMr. Lloyd is …\x01",
            "It's too amazing ~! It is!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_END)), "loc_A3E")

    ChrTalk(
        0x9,
        (
            "#02302FOh, yes.\x01",
            "You do pretty well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3E")

    SetChrSubChip(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#00009FThank you.\x01",
            "It may be just luck but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FNo, in this puzzle game\x01",
            "Only luck is a factor of victory.\x02\x03",
            "#12102FBannings, you are the one\x01",
            "True \"Pomutto! Master \".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FWell, thanks.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('贤者', 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CE3")

    ChrTalk(
        0x8,
        (
            "#12100FHm … … That's right.\x02\x03",
            "You should accept this if you do not mind.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '贤者'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('贤者', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x8,
        (
            "#12100FThe church and the Epstein Foundation\x01",
            "We jointly developed based on ancient techniques,\x01",
            "It's a forbidden master quartz.\x02\x03",
            "It is too strong to handle,\x01",
            "Although it was not able to be operated … …\x02\x03",
            "#12102FYou can handle it correctly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, I understand.\x01",
            "I will be of use to you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DC7")

    label("loc_CE3")


    ChrTalk(
        0x8,
        (
            "#12100FHm … … That's right.\x02\x03",
            "#12102FLet's do this to you as a reward.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '水耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('水耀珠', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00000FThank you.\x01",
            "I will be of use to you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_DC7")

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

    # Function_5_857 end

    def Function_6_DF9(): pass

    label("Function_6_DF9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E1C")
    Call(0, 22)
    Jump("loc_E89")

    label("loc_E1C")


    ChrTalk(
        0x10,
        (
            "#00102F(……see you later.)\x02\x03",
            "#00104F(I do not mind being late\x01",
            "Please prepare slowly. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E89")

    Jump("loc_118F")

    label("loc_E8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1100")

    ChrTalk(
        0x10,
        (
            "#00103FCrossbell city liberation strategy ……\x01",
            "I approached tomorrow at last.\x02\x03",
            "#00108FWhen I see a bell or uncle,\x01",
            "Asking the real intention of a series of incidents … …\x01",
            "I want to persuade you if I can.\x02\x03",
            "#00101FBut, if that does not come true ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008FErie……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#00106F……I'm sorry.\x01",
            "I got a bad voice.\x02\x03",
            "#00100FIt will help me without looking at danger\x01",
            "To reward a lot of people ……\x02\x03",
            "To regain Ka'a-chan more than anything,\x01",
            "We can not be defeated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F……明日は一緒に頑張ろう、Erie。\x01",
            "Because I and everyone is attached.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#00104F… … Hehe, well.\x02\x03",
            "#00102FThank you, Lloyd.\x01",
            "Thanks and feelings\x01",
            "I feel I got a little easier.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 5)
    Jump("loc_118F")

    label("loc_1100")


    ChrTalk(
        0x10,
        (
            "#00104FThank you, Lloyd.\x01",
            "Thanks to you I feel a little\x01",
            "I feel like I got easier.\x02\x03",
            "#00102FTake a rest nights.\x01",
            "Let's get ready for tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_118F")

    TalkEnd(0xFE)
    Return()

    # Function_6_DF9 end

    def Function_7_1193(): pass

    label("Function_7_1193")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_122B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11B6")
    Call(0, 23)
    Jump("loc_1226")

    label("loc_11B6")


    ChrTalk(
        0xB,
        (
            "#00204FWhen this is done,\x01",
            "I am going to the deck as well.\x02\x03",
            "#00202FConsultation … ….\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1226")

    Jump("loc_1734")

    label("loc_122B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1686")

    ChrTalk(
        0xB,
        (
            "#00203F(Rattling rattling … …)\x02\x03",
            "#00200FHmm, we are ready for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FTio……\x01",
            "What are you doing?\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1357")
    Jump("loc_13A1")

    label("loc_1357")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1377")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13A1")

    label("loc_1377")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1397")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13A1")

    label("loc_1397")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13A1")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)

    ChrTalk(
        0xB,
        (
            "#00202FTowards tomorrow's rush\x01",
            "Mercapa system's\x01",
            "I am doing the final check.\x02\x03",
            "#00203FI am with Lloyd's\x01",
            "I plan to get down Mercava, but …\x02\x03",
            "#00200FAfter holding down the communication terminal\x01",
            "ハッキングなどは、YonaとFrancさんに\x01",
            "I need to leave it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FReally……\x01",
            "Something seems to be tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00204FWell, it will close soon\x01",
            "Do not worry.\x02\x03",
            "#00202FLloyd seems to be a leader,\x01",
            "If you keep up with Don\x01",
            "Well enough.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FNo,\x01",
            "There are various preparations tomorrow.\x02\x03",
            "#00000FWell, if that's how it is\x01",
            "I'm afraid I can leave it here.\x02\x03",
            "Tioたちもしっかり\x01",
            "Please take a rest?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00204FYes, that's OK.\x01",
            "Please take your time off.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)
    SetScenarioFlags(0x1DA, 6)
    ClearChrFlags(0xB, 0x10)
    Jump("loc_1734")

    label("loc_1686")


    ChrTalk(
        0xB,
        (
            "#00204FTowards tomorrow's rush\x01",
            "Mercapa system's\x01",
            "I am doing the final check.\x02\x03",
            "#00202FAfter a while,\x01",
            "I am going to take a rest.\x01",
            "Please take your time off.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1734")

    TalkEnd(0xFE)
    Return()

    # Function_7_1193 end

    def Function_8_1738(): pass

    label("Function_8_1738")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_17BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_175B")
    Call(0, 24)
    Jump("loc_17B8")

    label("loc_175B")


    ChrTalk(
        0xE,
        (
            "#00304FWell then, see you later.\x02\x03",
            "#00302FOnce I finish developing the guy\x01",
            "Because I will go soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17B8")

    Jump("loc_1AE9")

    label("loc_17BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A6F")

    ChrTalk(
        0xE,
        "#00300FWell, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FRandyたちは、\x01",
            "It looks like we are improving weapons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00302FOh, no matter what the strategy of tomorrow\x01",
            "It will be the biggest mountain so far.\x02\x03",
            "#00304FThere will be a turn of \"Bergerger\"\x01",
            "In occasion for the occasion,\x01",
            "Do not worry too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FWell, until now I'm stupid\x01",
            "I did not have much opportunity, but …\x02\x03",
            "#00003FI will be with you tonight\x01",
            "Shall I take care of a tofa?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00309FOh, I gotta do it.\x02\x03",
            "#00303FUnlike your rifle\x01",
            "The precision part maintenance\x01",
            "It probably is not necessary …\x02\x03",
            "#00300FEven just by polishing\x01",
            "Oita is different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FI see, I see … ….\x01",
            "Surely it may be.\x02\x03",
            "#00002Fthank you for the advice.\x01",
            "I'll do it later as well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 7)
    Jump("loc_1AE9")

    label("loc_1A6F")


    ChrTalk(
        0xE,
        (
            "#00304FYou must also bring weapons by tomorrow\x01",
            "You should keep it firmly in place.\x02\x03",
            "#00309FIt is like treating an absurdly beautiful woman\x01",
            "Be gentle and polite.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AE9")

    TalkEnd(0xFE)
    Return()

    # Function_8_1738 end

    def Function_9_1AED(): pass

    label("Function_9_1AED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x68), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1BB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B10")
    Call(0, 25)
    Jump("loc_1BB0")

    label("loc_1B10")


    ChrTalk(
        0xF,
        (
            "#10106FLet me see……\x01",
            "By all means to Mr. Lloyd\x01",
            "There is something I'd like to ask.\x02\x03",
            "#10101FPlease come to the deck later.\x01",
            "When I've done various errands as well\x01",
            "I will be headed … ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BB0")

    Jump("loc_1C51")

    label("loc_1BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BC7")
    Call(0, 10)
    Jump("loc_1C51")

    label("loc_1BC7")


    ChrTalk(
        0xF,
        (
            "#10100FMy person again within tonight\x01",
            "I will keep in touch with the commander.\x02\x03",
            "#10103FFinal confirmation of the operation of tomorrow\x01",
            "It seems better to do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C51")

    TalkEnd(0xFE)
    Return()

    # Function_9_1AED end

    def Function_10_1C55(): pass

    label("Function_10_1C55")

    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x101, 0)
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1CE6")
    Jump("loc_1D30")

    label("loc_1CE6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1D06")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D30")

    label("loc_1D06")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D26")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D30")

    label("loc_1D26")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D30")

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
            "#00000Fお疲れ様、Noel、Franc。\x02\x03",
            "#00002FTomorrow's strategy is approaching\x01",
            "I'm somewhat relaxing here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#10102FI'm sorry.\x02\x03",
            "#10106F武器の手入れ中にFrancが\x01",
            "I came in … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01909FHaha, my sister's\x01",
            "I came to cheer you ~.\x02\x03",
            "#01904FI will prepare for tomorrow\x01",
            "I made it perfectly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FWell, that is reliable.\x02\x03",
            "#00000FFrancもオペレーターとして\x01",
            "You have to be active,\x01",
            "Feed me well for yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01902FYes, of course.\x01",
            "… or so, for that\x01",
            "I came here ~!\x02\x03",
            "#01909FAnyway, I\x01",
            "By being on your sister's side\x01",
            "I can fill energy!\x02",
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
            "#00000FHaha\x01",
            "I guess it is not a joke either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#10106FHa, already …\x01",
            "Please do not disturb at least.\x02\x03",
            "#10100FEr, Mr. Lloyd.\x01",
            "My person again within tonight\x01",
            "I will keep in touch with the commander.\x02\x03",
            "#10103FFinal confirmation of the operation of tomorrow\x01",
            "It seems better to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FOh, I beg you to do my best.\x02\x03",
            "#00000FNoelも、手入れが終わったら\x01",
            "Please take a good rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#10109FYes!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xF, 0x0)
    OP_93(0xC, 0x10E, 0x0)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x1DB, 0)
    Return()

    # Function_10_1C55 end

    def Function_11_2190(): pass

    label("Function_11_2190")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x69), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2250")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21B3")
    Call(0, 26)
    Jump("loc_224B")

    label("loc_21B3")


    ChrTalk(
        0xA,
        (
            "#10404FAnother one, to you\x01",
            "Should I tell the Kossori\x01",
            "There is a thing.\x02\x03",
            "#10402FPlease come to the deck later.\x01",
            "If I also finished drinking with Abbas\x01",
            "I will go there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_224B")

    Jump("loc_2309")

    label("loc_2250")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2262")
    Call(0, 12)
    Jump("loc_2309")

    label("loc_2262")


    ChrTalk(
        0xA,
        (
            "#10404FWell, the above permission is down.\x01",
            "We do not care\x01",
            "I will have my mission done.\x02\x03",
            "#10402FHuh, I'm getting busy tomorrow.\x01",
            "I am well amazed now#2RRelax#I guess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2309")

    TalkEnd(0xFE)
    Return()

    # Function_11_2190 end

    def Function_12_230D(): pass

    label("Function_12_230D")

    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x101, 0)
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_239E")
    Jump("loc_23E8")

    label("loc_239E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_23BE")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_23E8")

    label("loc_23BE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_23DE")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_23E8")

    label("loc_23DE")

    OP_52(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_23E8")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_249E")
    Jump("loc_24E8")

    label("loc_249E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_24BE")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24E8")

    label("loc_24BE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24DE")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24E8")

    label("loc_24DE")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_24E8")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0x8, 0x10)

    ChrTalk(
        0x101,
        (
            "#00005FWaji、アッバス……\x01",
            "Maybe, are you drinking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10404FFor the time being,\x01",
            "The preparation is over.\x02\x03",
            "#10402FHuh, how about you, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FCome on … …\x01",
            "I wonder if it's a strategy tomorrow?\x02\x03",
            "#00001FAlready have some glasses\x01",
            "It seems I got out of sight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FDo not worry.\x01",
            "I made Ventos make it\x01",
            "It is non alcoholic cocktail.\x02\x03",
            "To the progress of tomorrow's strategy\x01",
            "There are no obstacles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FOh, I see.\x02\x03",
            "#00000FWell, if Abbas says so\x01",
            "I think you should believe me this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10409FEven when I'm drinking alone\x01",
            "I do not mind believing.\x02\x03",
            "#10403F… Oh yeah, to you guys as well.\x01",
            "It seems better to tell him.\x02\x03",
            "#10400FTomorrow's strategy, also from the pope\x01",
            "I was officially permitted to participate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FAh … is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FMercapa mainly for secret activities\x01",
            "Operating with a large scale strategy\x01",
            "Originally should avoid it … …\x02\x03",
            "Given the state of confusion across the continent,\x01",
            "It is not possible to stop some exposures any longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FReally……\x01",
            "I am grateful for the judgment of the church.\x02\x03",
            "#00013F…… Anyway, the decisive battle is tomorrow.\x01",
            "Well, I beg you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#10402FHuh, I agree with the leader.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#12102FOf course, let me help you.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetScenarioFlags(0x1DB, 1)
    Return()

    # Function_12_230D end

    def Function_13_2942(): pass

    label("Function_13_2942")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x69), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2A6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_296A")
    Call(0, 26)
    Jump("loc_2A69")

    label("loc_296A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2974")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A69")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",          # 0
            "Party organization\x01",      # 1
            "quit\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_29C5"),
        (1, "loc_2A3E"),
        (SWITCH_DEFAULT, "loc_2A5A"),
    )


    label("loc_29C5")


    ChrTalk(
        0x8,
        (
            "#12100FWhew ……\x01",
            "That is still a secret matter.\x02\x03",
            "#12102F… Well, there is no help.\x01",
            "You do not have any problem.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A64")

    label("loc_2A3E")

    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(0)
    Fade(500)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A64")

    label("loc_2A5A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2A64")

    Jump("loc_2974")

    label("loc_2A69")

    Jump("loc_2BA2")

    label("loc_2A6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A80")
    Call(0, 12)
    Jump("loc_2BA2")

    label("loc_2A80")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2A8A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BA2")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",          # 0
            "Party organization\x01",      # 1
            "quit\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2ADB"),
        (1, "loc_2B77"),
        (SWITCH_DEFAULT, "loc_2B93"),
    )


    label("loc_2ADB")


    ChrTalk(
        0x8,
        (
            "#12100FTomorrow's strategy ……\x01",
            "This is from Mercava\x01",
            "Let's focus on backup.\x02\x03",
            "Those who infiltrate the city,\x01",
            "Firmly now\x01",
            "Prepare yourself well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B9D")

    label("loc_2B77")

    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(0)
    Fade(500)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2B9D")

    label("loc_2B93")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2B9D")

    Jump("loc_2A8A")

    label("loc_2BA2")

    TalkEnd(0xFE)
    Return()

    # Function_13_2942 end

    def Function_14_2BA6(): pass

    label("Function_14_2BA6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x68), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2C89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BC9")
    Call(0, 25)
    Jump("loc_2C84")

    label("loc_2BC9")


    ChrTalk(
        0xC,
        (
            "#01900FMr. Lloyd, please make my sister's request\x01",
            "Please listen carefully.\x02\x03",
            "#01909FHehe, I'm looking forward to seeing ~ ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F（う〜ん、なんでFrancが\x01",
            "I guess it sounds like fun … …)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C84")

    Jump("loc_2D2A")

    label("loc_2C89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C9B")
    Call(0, 10)
    Jump("loc_2D2A")

    label("loc_2C9B")


    ChrTalk(
        0xC,
        (
            "#01902FMr. Lloyd, tomorrow really\x01",
            "Please do your best~.\x02\x03",
            "#01909FMe too, my sister\x01",
            "Filling with energy,\x01",
            "I will keep it secure!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D2A")

    TalkEnd(0xFE)
    Return()

    # Function_14_2BA6 end

    def Function_15_2D2E(): pass

    label("Function_15_2D2E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_308E")

    ChrTalk(
        0x9,
        (
            "#02300FTomorrow, you go to Cros Bell City\x01",
            "As you infiltrate, from Mercava\x01",
            "I will start hacking.\x02\x03",
            "#02303FWell, at best, try hard.\x01",
            "Please scratch the city?\x02\x03",
            "#02302FIf real is confused,\x01",
            "There is also a ski to get in from the power net\x01",
            "I will be born.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FOh, the roles of each other\x01",
            "It seems to be exactly like it.\x02\x03",
            "#00001F……ところで、Yona……\x01",
            "I am planning to stay up all night today.\x01",
            "Is not it? (Girolli)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#02305F… … Gikutsu.\x02\x03",
            "#02309FNo, no … … Hey.\x01",
            "Preparation is about to end,\x01",
            "I am a night type person.\x02\x03",
            "#02304FRather than going to bed poorly,\x01",
            "The tension of the all-day closing is\x01",
            "You may be feeling fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FAnonymous ……\x01",
            "It will be a long time tomorrow,\x01",
            "Do not stay up all night?\x02\x03",
            "#00001FIf preparation is about to end soon\x01",
            "Please rest as soon as possible.\x01",
            "That 's definitely better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#02306FOh yeah, I understood that I knew.\x02\x03",
            "#02300FBecause I cut it up and rest from the proper place\x01",
            "It 's the best of everyone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 3)
    Jump("loc_3116")

    label("loc_308E")


    ChrTalk(
        0x9,
        (
            "#02300FPrepare for tomorrow 's hacking\x01",
            "It will be over soon.\x02\x03",
            "#02306FBecause I cut it up and rest from the proper place\x01",
            "Do not come to check each time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3116")

    TalkEnd(0xFE)
    Return()

    # Function_15_2D2E end

    def Function_16_311A(): pass

    label("Function_16_311A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34A0")

    ChrTalk(
        0x12,
        (
            "#02103FThose who disagreed on the current system\x01",
            "Concentrate and challenge at the pretense of death\x01",
            "\"Crossbell City Liberation Operation\" … …\x02\x03",
            "#02101FIf this fails,\x01",
            "\"The President was right\"\x01",
            "It will be a conclusion.\x02\x03",
            "#02103FDemocratization of the past Calvert,\x01",
            "Conspiracy play done behind that\x01",
            "Just as now justified.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F……I agree.\x02\x03",
            "#00001FIt all depends tomorrow … …\x01",
            "It is not exaggeration to say so\x01",
            "I am going to know enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#02109FHaha, press the pressure\x01",
            "I did not mean to give it.\x02\x03",
            "#02103F…… as a journalist\x01",
            "I saw the destiny of this crossbell,\x01",
            "There is a mission to tell people.\x02\x03",
            "#02100FBut before being a journalist\x01",
            "As a human being, I\x01",
            "I want to cheer you.\x02\x03",
            "#02104FBorn born inheriting the intention of Guy,\x01",
            "You guys special support department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FGraceさん……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#02109FFor Huh, Kaea-chan ….\x01",
            "Good luck tomorrow!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FWell, please leave it!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 4)
    Jump("loc_3545")

    label("loc_34A0")


    ChrTalk(
        0x12,
        (
            "#02100FBefore being a journalist\x01",
            "As a human being, I\x01",
            "I want to cheer you.\x02\x03",
            "#02109FEven for Koa-chan ….\x01",
            "Good luck tomorrow!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3545")

    TalkEnd(0xFE)
    Return()

    # Function_16_311A end

    def Function_17_3549(): pass

    label("Function_17_3549")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3841")

    ChrTalk(
        0x11,
        (
            "#02503F…… Perhaps tomorrow,\x01",
            "It will be a tough day.\x02\x03",
            "#02500FMore than anything, for you guys\x01",
            "\"Fate of autonomous state\"\x01",
            "I carried heavy baggage on my back.\x02\x03",
            "#02503FAs a representative of autonomous state … …\x01",
            "Please, let me head down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F…… I do not care\x01",
            "Please do not say.\x02\x03",
            "#00000FMcDowellには、\x01",
            "It is called ineffective declaration of an independent country\x01",
            "I played a big role.\x02\x03",
            "#00004FAfter that, we can fight\x01",
            "I have to do it with my own hands\x01",
            "I think that it is a problem that is not a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#02503FI'm sorry.\x01",
            "Truly do not put your hardship on you.\x02\x03",
            "#02500FSo then I guess you guys\x01",
            "Believe in accomplishing \"release strategy\"\x01",
            "Let's consider future measures.\x02\x03",
            "#02503FCrossbell residents, confused,\x01",
            "So that you can return to your original life as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah … well, thank you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 5)
    Jump("loc_38D1")

    label("loc_3841")


    ChrTalk(
        0x11,
        (
            "#02503FI guess you guys\x01",
            "Believe in accomplishing \"release strategy\"\x01",
            "Let's consider future measures.\x02\x03",
            "#02500F…… Please, do not protect the goddess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38D1")

    TalkEnd(0xFE)
    Return()

    # Function_17_3549 end

    def Function_18_38D5(): pass

    label("Function_18_38D5")

    Call(0, 19)
    Return()

    # Function_18_38D5 end

    def Function_19_38D9(): pass

    label("Function_19_38D9")

    TalkBegin(0x14)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_38E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BE7")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",          # 0
            "Buy accessories\x01",      # 1
            "Buy expendable items\x01",      # 2
            "quit\x01",            # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3951")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3951")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3970")
    OP_AF(0xD8)
    Jump("loc_39C2")

    label("loc_3970")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_3980")
    OP_AF(0xD7)
    Jump("loc_39C2")

    label("loc_3980")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_3990")
    OP_AF(0xD6)
    Jump("loc_39C2")

    label("loc_3990")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_39A0")
    OP_AF(0xD5)
    Jump("loc_39C2")

    label("loc_39A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_39B0")
    OP_AF(0xD4)
    Jump("loc_39C2")

    label("loc_39B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_39C0")
    OP_AF(0xD3)
    Jump("loc_39C2")

    label("loc_39C0")

    OP_AF(0xD2)

    label("loc_39C2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3BE2")

    label("loc_39D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39F1")
    OP_AF(0xDC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3BE2")

    label("loc_39F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A05")
    Jump("loc_3BE2")

    label("loc_3A05")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BE2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B2A")

    ChrTalk(
        0x14,
        (
            "You can never be optimistic.\x01",
            "The situation is not\x01",
            "I know it, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "A police church, a guard, a black moon,\x01",
            "Hello \"God of war\" and \"Silver\" until\x01",
            "I'm on this side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "If all these items are complete,\x01",
            "You can get anything done\x01",
            "It will come to me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3BE2")

    label("loc_3B2A")


    ChrTalk(
        0x14,
        (
            "A police church, a guard, a black moon,\x01",
            "Hello \"God of war\" and \"Silver\" until\x01",
            "I'm on this side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "If all these items are complete,\x01",
            "You can get anything done\x01",
            "It will come to me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BE2")

    Jump("loc_38E6")

    label("loc_3BE7")

    TalkEnd(0x14)
    Return()

    # Function_19_38D9 end

    def Function_20_3BEB(): pass

    label("Function_20_3BEB")

    Call(0, 21)
    Return()

    # Function_20_3BEB end

    def Function_21_3BEF(): pass

    label("Function_21_3BEF")

    TalkBegin(0x15)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3BFC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E24")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",            # 0
            "To remodel and synthesize\x01",      # 1
            "quit\x01",              # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C5C")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3C5C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C7C")
    OP_AF(0xDD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3E1F")

    label("loc_3C7C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C90")
    Jump("loc_3E1F")

    label("loc_3C90")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E1F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D93")

    ChrTalk(
        0x15,
        (
            "In the strategy of tomorrow,\x01",
            "It is still a problem\x01",
            "It will be three \"Shinkansen\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "How to reject the \"god machine\" … that,\x01",
            "I think it will be the key to infiltration into the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Taking cooperation with each side,\x01",
            "I want to make the strategy a success anyhow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3E1F")

    label("loc_3D93")


    ChrTalk(
        0x15,
        (
            "How to reject three \"shinkin\" machines,\x01",
            "I think it will be the key to infiltration into the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Taking cooperation with each side,\x01",
            "I want to make the strategy a success anyhow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E1F")

    Jump("loc_3BFC")

    label("loc_3E24")

    TalkEnd(0x15)
    Return()

    # Function_21_3BEF end

    def Function_22_3E28(): pass

    label("Function_22_3E28")

    EventBegin(0x0)
    Fade(500)
    OP_68(100420, 1000, -101760, 0)
    MoveCamera(47, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15480, 0)
    SetChrPos(0x101, 100110, 0, -101660, 180)
    SetChrSubChip(0x10, 0x2)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4383")

    ChrTalk(
        0x10,
        (
            "#12P#00106FCrossbell city liberation strategy ……\x01",
            "I approached tomorrow at last.\x02\x03",
            "#00108FWhen I see a bell or uncle,\x01",
            "Asking the real intention of a series of incidents … …\x01",
            "I want to persuade you if I can.\x02\x03",
            "#00101FBut, if that does not come true ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#5P…… Conflict can not be avoided.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#12P#00103FYeah … I do not care anymore\x01",
            "I am prepared for that at long last.\x02\x03",
            "#00108FIt will help me without looking at danger\x01",
            "To reward a lot of people ……\x02\x03",
            "#00101FMore than anything, Ka'aa\x01",
            "To regain it, we absolutely\x01",
            "It can not be defeated.\x02",
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
            "#00004F#5P……なあ、Erie。\x02\x03",
            "#00000FI do not need to be alone with so much alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#12P#00105FHuh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PMr. Dieter and Mr. Mary Bell,\x01",
            "It was also close friends for us.\x02\x03",
            "#00001Fだから、その重みはErieだけじゃなく、\x01",
            "I think that it should be carried on by all members.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#12P#00108FLloyd …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F……明日は一緒に頑張ろう、Erie。\x01",
            "Because I and everyone is attached.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#12P#00104F… … Hehe, well.\x02\x03",
            "#00102FThank you, Lloyd.\x01",
            "Thanks to my feelings I got easier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009F#5PHaha … … You are welcome.\x02",
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x10)
    Sleep(500)

    ChrTalk(
        0x10,
        (
            "#12P#00106F(… …. Ah, that, Lloyd.\x02\x03",
            "#00112F(After preparing for tomorrow,\x01",
            "Will you come to the deck later? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#5P(eh……?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#12P#00113F(If possible, that … …\x01",
            "I want to talk with the two of you,\x01",
            "Why\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 5)
    Jump("loc_4416")

    label("loc_4383")


    ChrTalk(
        0x10,
        (
            "#12P#00112F(After preparing for tomorrow,\x01",
            "Will you come to the deck later? )\x02\x03",
            "#00113F(If possible, that … …\x01",
            "I want to talk with the two of you,\x01",
            "Why\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4416")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Erieの誘いを受ける\x01",      # 0
            "To give up\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44F0")

    ChrTalk(
        0x101,
        (
            "#00002F#5P(…, I understand.\x01",
            "I'll let you go if you do not mind. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#12P#00109F(… …. Hehe, thank you.\x01",
            "Well then, see you later. )\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 27)
    SetScenarioFlags(0x1AA, 3)
    Jump("loc_45C6")

    label("loc_44F0")


    ChrTalk(
        0x10,
        (
            "#12P#00106F(……I see.)\x02\x03",
            "#00102F(Hehe, do not mind.\x01",
            "It's not a big deal. )\x02\x03",
            "#00104F(If you feel like it's okay,\x01",
            "Please give me a voice again. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5P(Oh, I will do so.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_45C6")

    SetChrSubChip(0x10, 0x0)
    EventEnd(0x5)
    Return()

    # Function_22_3E28 end

    def Function_23_45CD(): pass

    label("Function_23_45CD")

    EventBegin(0x0)
    Fade(500)
    OP_68(-3160, -500, 6480, 0)
    MoveCamera(52, 29, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16170, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 6)), scpexpr(EXPR_END)), "loc_460F")
    SetChrSubChip(0xB, 0x1)

    label("loc_460F")

    SetChrPos(0x101, -3610, -1500, 5780, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B10")

    ChrTalk(
        0xB,
        (
            "#11P#00203F(Rattling rattling … …)\x02\x03",
            "#00200FHmm, we are ready for now.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xB)

    ChrTalk(
        0xB,
        (
            "#11P#00208F(Casually)\x02\x03",
            "#00203F……………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005F……えっと、Tio？\x01",
            "What are you doing?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0xB, 0x1)

    ChrTalk(
        0xB,
        (
            "#5P#00202F…… Yeah, toward tomorrow's rush\x01",
            "Mercapa system's\x01",
            "I was doing the final check.\x02\x03",
            "#00203FI am with Lloyd's\x01",
            "I plan to get down Mercava, but …\x02\x03",
            "#00200FAfter holding down the communication terminal\x01",
            "ハッキングなどは、YonaとFrancさんに\x01",
            "I need to leave it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FReally……\x01",
            "Something seems to be tough.\x02\x03",
            "#00000FIs there anything I can do for you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#00203F…… No, in particular.\x02\x03",
            "#00202FIt is clearly my field,\x01",
            "Yonaもいるので十分です。\x02\x03",
            "#00204FLloyd seems to be a leader,\x01",
            "If you keep up with Don\x01",
            "Well enough.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00006FNo,\x01",
            "There are various preparations tomorrow.\x02\x03",
            "#00000FWell, if that's how it is\x01",
            "I'm afraid I can leave it here.\x02",
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
            "#5P#00203F……by the way,\x01",
            "There was only one.\x02\x03",
            "#00208FActually … to Mr. Lloyd\x01",
            "I have something I would like to consult with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FConsultation ……?\x01",
            "Is there something wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#00206F…… No, here is a bit.\x02\x03",
            "#00201FWhen you've done that,\x01",
            "Later on the deck of Mercapa\x01",
            "Could you please come?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 6)
    ClearChrFlags(0xB, 0x10)
    Jump("loc_4B9A")

    label("loc_4B10")


    ChrTalk(
        0xB,
        (
            "#5P#00206FActually … to Mr. Lloyd\x01",
            "I have something I would like to consult with.\x02\x03",
            "#00201FWhen you've done that,\x01",
            "Later on the deck of Mercapa\x01",
            "Could you please come?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B9A")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Tioの誘いを受ける\x01",      # 0
            "To give up\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C5E")

    ChrTalk(
        0x101,
        (
            "#12P#00002FI got it, if it's OK with me\x01",
            "I will be pleased to have a consultation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#00209FHehu ……\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 27)
    SetScenarioFlags(0x1AA, 4)
    Jump("loc_4D01")

    label("loc_4C5E")


    ChrTalk(
        0xB,
        (
            "#5P#00204F……Is that so.\x01",
            "Well, it can not be helped.\x02\x03",
            "#00202FIf you can get a consultation\x01",
            "I'm happy to hear your voice again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FOh, I understand.\x02",
    )

    OP_5A()
    CloseMessageWindow()

    label("loc_4D01")

    SetChrSubChip(0xB, 0x0)
    EventEnd(0x5)
    Return()

    # Function_23_45CD end

    def Function_24_4D08(): pass

    label("Function_24_4D08")

    EventBegin(0x0)
    Fade(500)
    OP_68(98200, 1000, 600, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16090, 0)
    SetChrPos(0x101, 97510, 0, -530, 0)
    SetChrSubChip(0xE, 0x2)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5280")

    ChrTalk(
        0xE,
        "#5P#00300FWell, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FRandyたちは、\x01",
            "It looks like we are improving weapons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5P#00302FOh, no matter what the strategy of tomorrow\x01",
            "It will be the biggest mountain so far.\x02\x03",
            "#00304FThere will be a turn of \"Bergerger\"\x01",
            "In occasion for the occasion,\x01",
            "Do not worry too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FWell, until now I'm stupid\x01",
            "I did not have much opportunity, but …\x02\x03",
            "#00003FI will be with you tonight\x01",
            "Shall I take care of a tofa?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5P#00309FOh, I gotta do it.\x02\x03",
            "#00303FUnlike your rifle\x01",
            "The precision part maintenance\x01",
            "It probably is not necessary …\x02\x03",
            "#00300FEven just by polishing\x01",
            "Oita is different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00009FHaha, that's right.\x02\x03",
            "#00005FEven so ……\x01",
            "Randyって意外とマメだよな。\x02\x03",
            "#00000FNot just that rifle,\x01",
            "Caring for Stanhalvard as well\x01",
            "It seems not to be missing everyday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5P#00302FWell, care of weapons\x01",
            "It is a first step in the beginning.\x02\x03",
            "#00304FIt is like treating an absurdly beautiful woman\x01",
            "Be kind and gently treated.\x02\x03",
            "#00300FWell then, on the battlefield\x01",
            "Unnecessary troubles\x01",
            "It's that they will soak in ──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xE)

    ChrTalk(
        0x101,
        (
            "#12P#00011F… … bad, maybe,\x01",
            "Did you remind me of extra things?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5P#00309F…… Ha ha, what are you apologizing for?\x02\x03",
            "#00306F… But, that's right.\x02\x03",
            "#00308FIt is almost time …\x01",
            "It might be a good time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005Feh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5P#00300FHey, if I wish later\x01",
            "Is it on the deck of Mercapa?\x02\x03",
            "I want you to go out with me for a while\x01",
            "I have it, right?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 7)
    Jump("loc_52F4")

    label("loc_5280")


    ChrTalk(
        0xE,
        (
            "#5P#00300FWow, if it's time to go later\x01",
            "Is it on the deck of Mercapa?\x02\x03",
            "I want you to go out with me for a while\x01",
            "I have it, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52F4")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Randyの誘いを受ける\x01",      # 0
            "To give up\x01",                  # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53DD")

    ChrTalk(
        0x101,
        (
            "#12P#00002F……I understood,\x01",
            "I will let you go later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5P#00309FWell then, see you later.\x02\x03",
            "#00302FOnce I finish developing the guy\x01",
            "Because I will go soon.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 27)
    SetScenarioFlags(0x1AA, 5)
    Jump("loc_547D")

    label("loc_53DD")


    ChrTalk(
        0xE,
        (
            "#5P#00306F……Really.\x01",
            "Well, another fun story\x01",
            "Even wake up ….\x02\x03",
            "#00300FIf that comes to mind\x01",
            "Please give me a voice again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FOh, I will let you.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_547D")

    SetChrSubChip(0xE, 0x0)
    EventEnd(0x5)
    Return()

    # Function_24_4D08 end

    def Function_25_5484(): pass

    label("Function_25_5484")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C38")

    ChrTalk(
        0xF,
        "#5P#10100FMr. Lloyd, cheers for good work!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5P#01902FIs cheers for good work~!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000Fお疲れ様、Noel、Franc。\x02\x03",
            "#00009FTomorrow's strategy is approaching\x01",
            "I'm somewhat relaxing here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5P#10102FI'm sorry.\x02\x03",
            "#10106F武器の手入れ中にFrancが\x01",
            "I came in … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5P#01909FHaha, my sister's\x01",
            "I came to cheer you ~.\x02\x03",
            "#01904FI will prepare for tomorrow\x01",
            "I made it perfectly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00004FWell, that is reliable.\x02\x03",
            "#00000FFrancもオペレーターとして\x01",
            "You have to be active,\x01",
            "Feed me well for yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5P#01902FYes, of course.\x01",
            "… or so, for that\x01",
            "I came here ~!\x02\x03",
            "#01909FAnyway, I\x01",
            "By being on your sister's side\x01",
            "I can fill energy!\x02",
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
            "#12P#00012FHaha\x01",
            "I guess it is not a joke either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5P#10106FHa, already …\x01",
            "Please do not disturb at least.\x02\x03",
            "#10102FEr, Mr. Lloyd.\x01",
            "My person again within tonight\x01",
            "I will keep in touch with the commander.\x02\x03",
            "#10103FFinal confirmation of the operation of tomorrow\x01",
            "It seems better to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FOh, I beg you to do my best.\x02\x03",
            "#00003FNoelは明日、俺たちと一緒に\x01",
            "I will infiltrate the city …\x02\x03",
            "#00000FBe prepared for thorough preparation,\x01",
            "Please take a good rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#5P#10109FYes!\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xC)

    ChrTalk(
        0xC,
        (
            "#11P#01905F(Hey Hey, old sister.\x01",
            "As it is, today's chat is\x01",
            "It seems like it will end? )\x02\x03",
            "#01909F(Although it is a great opportunity,\x01",
            "Is it okay to leave this as it is? )\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xF,
        (
            "#5P#10111F(Cha, Chance!\x01",
            "  Franc、いい加減に……！）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00005FWell, what's wrong?\x01",
            "Was there also a problem?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xF)

    ChrTalk(
        0xF,
        "#5P#10114FWell, er, um … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11P#01909F(Gunbare, older sister!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5P#10103F… … that … … I can do it later,\x01",
            "Would you please come to the deck?\x02\x03",
            "#10101FIt's not a big deal,\x01",
            "By all means to Mr. Lloyd\x01",
            "There is something I'd like to ask.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 0)
    Jump("loc_5CC3")

    label("loc_5C38")


    ChrTalk(
        0xF,
        (
            "#5P#10103F……後で、Would you please come to the deck?\x02\x03",
            "#10101FIt's not a big deal,\x01",
            "By all means to Mr. Lloyd\x01",
            "There is something I'd like to ask.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CC3")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Noelの誘いを受ける\x01",      # 0
            "To give up\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DDE")

    ChrTalk(
        0x101,
        (
            "#12P#00002FOh, I understand.\x01",
            "Noelが頼み事なんて\x01",
            "I feel unusual … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11P#01909F(You did it, Onee!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5P#10114FWell then, then …\x01",
            "When I've done various errands as well\x01",
            "I'm heading there.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 27)
    SetScenarioFlags(0x1AA, 6)
    Jump("loc_5EE2")

    label("loc_5DDE")


    ChrTalk(
        0xF,
        (
            "#5P#10106FIs that so …?\x02\x03",
            "#10112FNo, do not mind!\x01",
            "It's really a lot of business\x01",
            "There is not it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5P#01906FIt can not be helped ~.\x02\x03",
            "#01901FMr. Lloyd, if you feel like it\x01",
            "To your older sister again\x01",
            "Please speak to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FOh, I understand.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_5EE2")

    SetChrSubChip(0xF, 0x0)
    OP_93(0xC, 0x10E, 0x0)
    OP_4C(0xC, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_25_5484 end

    def Function_26_5EF4(): pass

    label("Function_26_5EF4")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6625")

    ChrTalk(
        0x101,
        (
            "#6P#00005FWaji、アッバス……\x01",
            "Maybe, are you drinking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#10404FFor the time being,\x01",
            "The preparation is over.\x02\x03",
            "#10402FHuh, how about you, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FCome on … …\x01",
            "I wonder if it's a strategy tomorrow?\x02\x03",
            "#00001FAlready have some glasses\x01",
            "It seems I got out of sight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#12100FDo not worry.\x01",
            "I made Ventos make it\x01",
            "It is non alcoholic cocktail.\x02\x03",
            "To the progress of tomorrow's strategy\x01",
            "There are no obstacles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FOh, I see.\x02\x03",
            "#00000FWell, if Abbas says so\x01",
            "I think you should believe me this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#10409FEven when I'm drinking alone\x01",
            "I do not mind believing.\x02\x03",
            "#10403F… Oh yeah, to you guys as well.\x01",
            "It seems better to tell him.\x02\x03",
            "#10400FTomorrow's strategy, also from the pope\x01",
            "I was officially permitted to participate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FAh … is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#12100FMercapa mainly for secret activities\x01",
            "Operating with a large scale strategy\x01",
            "Originally should avoid it … …\x02\x03",
            "Given the state of confusion across the continent,\x01",
            "It is not possible to stop some exposures any longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FReally……\x01",
            "I am grateful for the judgment of the church.\x02\x03",
            "#00013F…… Anyway, the decisive battle is tomorrow.\x01",
            "Well, I beg you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11P#10402FHuh, I agree with the leader.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#12102FOf course, let me help you.\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "#11P#10403FOh … by the way.\x01",
            "Tell me only one more thing\x01",
            "There was something I had to do.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00005FHuh……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#12100F……Waji。\x01",
            "That matter, at the moment\x01",
            "It is supposed to be a confidential matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#10405FWas that so?\x02\x03",
            "#10409FHuh, then then as much we can\x01",
            "I have to tell Kossori.\x02",
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
            "#5P#12100F……まあいい、Wajiが\x01",
            "There is no way to say so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00012FWell, somewhat well\x01",
            "I do not know ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#10404FHuh, you guys\x01",
            "It is greatly related.\x02\x03",
            "#10402F─ ─ If you are concerned,\x01",
            "Later on a deck meeting\x01",
            "Can I also talk?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 1)
    Jump("loc_66B8")

    label("loc_6625")


    ChrTalk(
        0xA,
        (
            "#11P#10404FTell me only one more thing\x01",
            "There was something I had to do.\x02\x03",
            "#10402FHuff, if you care\x01",
            "Later on a deck meeting\x01",
            "Can I also talk?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66B8")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Wajiの誘いを受ける\x01",      # 0
            "To give up\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6813")

    ChrTalk(
        0x101,
        (
            "#6P#00006F……I understood.\x01",
            "You only have to go to the deck?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11P#10409FHuh, it's a rule.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#12100FWaji、念の為言っておくが\x01",
            "Even more than that … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#10404FHuh, I know that I know.\x02\x03",
            "#10400FI will go after drinking\x01",
            "You do not have to hurry so fast.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 27)
    SetScenarioFlags(0x1AA, 7)
    Jump("loc_6884")

    label("loc_6813")


    ChrTalk(
        0xA,
        (
            "#11P#10405FIs that it?\x01",
            "That's fine, but …\x02\x03",
            "#10404FHuh, if I change my mind\x01",
            "Try calling out again.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_6884")

    SetChrSubChip(0xA, 0x0)
    SetChrSubChip(0x8, 0x0)
    EventEnd(0x5)
    Return()

    # Function_26_5EF4 end

    def Function_27_688F(): pass

    label("Function_27_688F")

    FadeToDark(500, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 3)), scpexpr(EXPR_END)), "loc_6954")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F（……Erieに、行けなくなることを\x01",
            "I have to apologize properly. )\x02",
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
            "ロイドはErieに、\x01",
            "I apologized for losing my promise.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 3)
    Jump("loc_6D69")

    label("loc_6954")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 4)), scpexpr(EXPR_END)), "loc_6A0E")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F（……Tioに、行けなくなることを\x01",
            "I have to apologize properly. )\x02",
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
            "ロイドはTioに、\x01",
            "I apologized for losing my promise.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 4)
    Jump("loc_6D69")

    label("loc_6A0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 5)), scpexpr(EXPR_END)), "loc_6ACC")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F（……Randyに、行けなくなることを\x01",
            "I have to apologize properly. )\x02",
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
            "ロイドはRandyに、\x01",
            "I apologized for losing my promise.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 5)
    Jump("loc_6D69")

    label("loc_6ACC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 6)), scpexpr(EXPR_END)), "loc_6B86")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F（……Noelに、行けなくなることを\x01",
            "I have to apologize properly. )\x02",
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
            "ロイドはNoelに、\x01",
            "I apologized for losing my promise.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 6)
    Jump("loc_6D69")

    label("loc_6B86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 7)), scpexpr(EXPR_END)), "loc_6C3C")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F（……Wajiに、行けなくなることを\x01",
            "I have to apologize properly. )\x02",
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
            "ロイドはWajiに、\x01",
            "I apologized for losing my promise.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 7)
    Jump("loc_6D69")

    label("loc_6C3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 0)), scpexpr(EXPR_END)), "loc_6CFA")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F（……Lishaに、行けなくなることを\x01",
            "I have to apologize properly. )\x02",
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
            "ロイドはLishaに、\x01",
            "I apologized for losing my promise.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AB, 0)
    Jump("loc_6D69")

    label("loc_6CFA")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00003F(…… one thing in a sleeping room\x01",
            "After preparing for tomorrow,\x01",
            "Let's face the deck. )\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_6D69")

    Return()

    # Function_27_688F end

    def Function_28_6D6A(): pass

    label("Function_28_6D6A")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_739D")
    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x101, 1420, 0, -92300, 90)
    OP_68(2300, 1000, -92050, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 3)), scpexpr(EXPR_END)), "loc_6E8A")

    ChrTalk(
        0x101,
        (
            "#00005F#6P(by the way……\x01",
            "  Erieと話す約束をしていたな。）\x02\x03",
            "#00003F(…………………………………)\x02\x03",
            "#00000F(…, what do you do?\x01",
            "Are you preparing for tomorrow? )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_721D")

    label("loc_6E8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 4)), scpexpr(EXPR_END)), "loc_6F46")

    ChrTalk(
        0x101,
        (
            "#00005F#6P（そういえば、Tioが\x01",
            "I was saying that I wanted consultation. )\x02\x03",
            "#00003F(…………………………………)\x02\x03",
            "#00000F(……what will you do?\x01",
            "Are you preparing for tomorrow? )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_721D")

    label("loc_6F46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 5)), scpexpr(EXPR_END)), "loc_7002")

    ChrTalk(
        0x101,
        (
            "#00005F#6P（そういえば、Randyが\x01",
            "I told you I have something I want to talk about. )\x02\x03",
            "#00003F(…………………………………)\x02\x03",
            "#00000F(……what will you do?\x01",
            "Are you preparing for tomorrow? )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_721D")

    label("loc_7002")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 6)), scpexpr(EXPR_END)), "loc_70B8")

    ChrTalk(
        0x101,
        (
            "#00005F#6P（そういえば、Noelが\x01",
            "I was saying that there is a need. )\x02\x03",
            "#00003F(…………………………………)\x02\x03",
            "#00000F(……what will you do?\x01",
            "Are you preparing for tomorrow? )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_721D")

    label("loc_70B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 7)), scpexpr(EXPR_END)), "loc_716C")

    ChrTalk(
        0x101,
        (
            "#00005F#6P（そういえば、Wajiが\x01",
            "I was saying something to worry about. )\x02\x03",
            "#00003F(…………………………………)\x02\x03",
            "#00000F(……what will you do?\x01",
            "Are you preparing for tomorrow? )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_721D")

    label("loc_716C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 0)), scpexpr(EXPR_END)), "loc_721D")

    ChrTalk(
        0x101,
        (
            "#00005F#6P（そういえば、Lishaと\x01",
            "I promised to talk. )\x02\x03",
            "#00003F(…………………………………)\x02\x03",
            "#00000F(……what will you do?\x01",
            "Are you preparing for tomorrow? )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_721D")

    Sound(814, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When the free action ends, that day ends,\x01",
            "Be careful as the event goes forward.\x07\x00\x02",
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
            "【There are still other things to do】\x01",                        # 0
            "【Talk with the partner who promised to finish free action】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_72FD"),
        (1, "loc_7302"),
        (SWITCH_DEFAULT, "loc_7384"),
    )


    label("loc_72FD")

    Jump("loc_7384")

    label("loc_7302")

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
            "Then Lloyd prepares for the release strategy of tomorrow\x01",
            "I went to the deck of the night after I finished it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x22, 0)
    NewScene("e440B", 0, 0, 0)
    IdleLoop()
    Jump("loc_7384")

    label("loc_7384")

    OP_5A()
    SetChrPos(0x0, 550, 0, -92390, 270)
    EventEnd(0x5)
    Jump("loc_76D7")

    label("loc_739D")


    ChrTalk(
        0x101,
        (
            "#00005F(…… early today\x01",
            "Should I take a rest? )\x02\x03",
            "#00003F(For one, before the operation of tomorrow\x01",
            "Those who confirm the state of everyone\x01",
            "It might be nice … …)\x02",
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
            "When choosing to take a rest in the sleeping room\x01",
            "That day finished as it is,\x01",
            "Be careful as the event goes forward.\x07\x00\x02",
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
            "【There are still other things to do】\x01",          # 0
            "【End freed behavior and take a rest】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_751D")
    Jump("loc_76D7")

    label("loc_751D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76D7")
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
            "#00003F#6P(… preparing everything in a sleeping room,\x01",
            "Let's have a break for tonight. )\x02\x03",
            "#00001F(Cross Bell City Liberation Operations tomorrow ……\x01",
            "I will definitely succeed! )\x02",
        )
    )

    CloseMessageWindow()
    Sound(100, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0xA, 0x1, 0x8)
    Sleep(500)

    def lambda_7655():
        OP_95(0xFE, 4300, 0, -92030, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7655)
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

    label("loc_76D7")

    TalkEnd(0xFF)
    Return()

    # Function_28_6D6A end

    def Function_29_76DB(): pass

    label("Function_29_76DB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x0, -150, 0, -88230, 180)
    EventEnd(0x5)
    Return()

    # Function_29_76DB end

    def Function_30_76FB(): pass

    label("Function_30_76FB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50203.itc", 0x1E)
    LoadChrToIndex("chr/ch06902.itc", 0x1F)
    LoadChrToIndex("chr/ch06000.itc", 0x20)
    LoadChrToIndex("chr/ch05800.itc", 0x21)
    SoundLoad(943)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7735")
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_7735")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7748")
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_7748")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_775B")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_775B")

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
            "Thus - ─ covering Crossbell City\x01",
            "The inviolable \"barrier\" has disappeared.\x02\x03",
            "Lloyd's are \"Kuro Mun\"'s Tsao and\x01",
            "I contacted Mireilleu of resistance and others …\x02\x03",
            "Further from Sonja command\x01",
            "The Belgard gate, the Tangram gate unit\x01",
            "I attached a promise to keep neutrality.\x02\x03",
            "And ──\x02\x03",
            "In the night, at the bridge of Mercapa\x01",
            "There was a message from Father Kevin.\x07\x00\x02",
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
            "─ ─ So,\x01",
            "I entered the airspace\x01",
            "Do not worry about being attacked?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x105,
        (
            "#10403F#6POh, apparently God machine#4RIron#They are\x01",
            "It seems that I concentrate on urban defense.\x02\x03",
            "#10400FUnless you approach Cross Bell City\x01",
            "I think it's okay.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(90, -1, -1, -1)
    SetChrName("Father Kevin")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Alright, somehow with this\x01",
            "I suspect a sight will come …\x02\x03",
            "I will return there tomorrow morning.\x02\x03",
            "About timing\x01",
            "Let 's try to speak at that time.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x105,
        "#10402F#6PHuh, I understand.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(190, -1, -1, -1)
    SetChrName("Voice of Lease")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2S…… Kevin, on behalf.\x07\x00\x02",
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
        "#00102F#12PMr. Lease ……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(160, -1, -1, -1)
    SetChrName("Sister · Lease")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……Erieさん。\x01",
            "It is safe and above all.\x02\x03",
            "To Mr. Lloyd,\x01",
            "Everyone else.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00002F#12PHaha, thanks to you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#12PWell ~, leasing properly in this form\x01",
            "I did not expect to speak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#12P#NWith our rush\x01",
            "You are helping me, are not you?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(140, 70, -1, -1)
    SetChrName("Sister · Lease")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yeah, here in Mercapa\x01",
            "God machine to defend the city#4RIron#We\x01",
            "I will attract them.\x02\x03",
            "To the hunters and the defense forces\x01",
            "I can not cope … …\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00004F#12P……enough.\x01",
            "It really helps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#12Pリースさん、Father Kevin。\x01",
            "What to thank you … …\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(90, -1, -1, -1)
    SetChrName("Father Kevin")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Well, thank you.\x01",
            "Have been successful since it succeeded.\x02\x03",
            "Once, this time also helpers\x01",
            "I'm going to bring a burn … ….\x02\x03",
            "Still, that doll is a partner\x01",
            "Minutes may be too bad.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x103,
        "#00208F#12P#Nsurely……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00301F#12PWell, not much\x01",
            "Do not push yourself too hard?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(105, -1, -1, -1)
    SetChrName("Father Kevin")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hahaha, and then.\x02\x03",
            "──Waji。\x01",
            "Then, in tomorrow morning.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x105,
        "#10400F#6POh, I'll be waiting.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(180, -1, -1, -1)
    SetChrName("Sister · Lease")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Then, I will excuse you.\x07\x00\x02",
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

    def lambda_816A():
        TurnDirection(0x11, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_816A)
    Sleep(50)

    def lambda_817A():
        TurnDirection(0x12, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_817A)
    Sleep(50)

    def lambda_818A():
        TurnDirection(0x13, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_818A)
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
            "#02501F#5P─ ─ um.\x01",
            "It is going to be a tough day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#02106F#6P#NI agree……\x01",
            "About the difference in the strength of the ground\x01",
            "The President is outnumbered.\x02\x03",
            "#02101FAnyway, that dolls\x01",
            "Is not it ridiculous strength?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x106,
        (
            "#10708F#12PAccording to Meister,\x01",
            "The power of the \"space disappearance\" of the white fuselage\x01",
            "It seems that it can not be used … …\x02\x03",
            "#10701FStill basic performance is\x01",
            "It is not changed, is it?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#12100F#5PWell, those who thought so\x01",
            "Probably safe.\x02\x03",
            "This white aircraft is this#2RMale#Unit,\x01",
            "I need to see the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#5PIn any case, around the city\x01",
            "It is expected to be in a stalemate state.\x02\x03",
            "#10401FIf you were to hold the key\x01",
            "I guess we are in charge of infiltration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#12POh, I know.\x02\x03",
            "#00013F… … somehow entered\x01",
            "With the section chief and Mr. Dudley\x01",
            "We have to join together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#11PBut is it okay?\x02\x03",
            "#00301FContact from Dudley\x01",
            "It seems that it has run out in the middle.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x1)
    Sleep(200)

    ChrTalk(
        0x9,
        (
            "#02305F#5PProbably, at the communication terminal\x01",
            "You forced shut down, right?\x02\x03",
            "#02303FSpecific Enigma registration number only\x01",
            "You should have disabled send and receive.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0x2)
    Sleep(100)

    ChrTalk(
        0xC,
        (
            "#01901F#5PWell then in the city,\x01",
            "The president side can use communication\x01",
            "We can not use … ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#12PYes, communication terminal is also\x01",
            "It seems necessary to hold down.\x02\x03",
            "#00208FBecause it is in the Orkis Tower\x01",
            "It seems not easy, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#12PEither way …\x01",
            "Everything is tomorrow morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#12PYeah ….\x01",
            "\"Cross Bell City Liberation Operation\".\x02\x03",
            "#00101FTo regain Ka'a-chan\x01",
            "You have to make it successful at all costs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11POh … Absent tonight\x01",
            "It is necessary to cultivate spirit.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00004F#5PEveryone has a sleeping room\x01",
            "If you are tired, please take a rest.\x02\x03",
            "#00000FWith perfect attitude ……\x01",
            "Let's face it tomorrow morning.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    SetMessageWindowPos(290, 50, -1, -1)
    SetChrName("All of us")

    AnonymousTalk(
        0xFF,
        "#4SHuh!\x02",
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x79), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_885D")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_885D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7A), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8874")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8874")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7B), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_888B")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_888B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7D), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_88A2")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_88A2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7C), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_88B9")
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_88B9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7E), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_88D0")
    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_88D0")

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

    # Function_30_76FB end

    SaveToFile()

Try(main)
