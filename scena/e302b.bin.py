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
        "Function_6_E33",          # 06, 6
        "Function_7_11F8",         # 07, 7
        "Function_8_179A",         # 08, 8
        "Function_9_1B9D",         # 09, 9
        "Function_10_1CF4",        # 0A, 10
        "Function_11_2207",        # 0B, 11
        "Function_12_23A0",        # 0C, 12
        "Function_13_2A6C",        # 0D, 13
        "Function_14_2CDB",        # 0E, 14
        "Function_15_2E4B",        # 0F, 15
        "Function_16_32AF",        # 10, 16
        "Function_17_3704",        # 11, 17
        "Function_18_3ABF",        # 12, 18
        "Function_19_3AC3",        # 13, 19
        "Function_20_3DBC",        # 14, 20
        "Function_21_3DC0",        # 15, 21
        "Function_22_4037",        # 16, 22
        "Function_23_47F6",        # 17, 23
        "Function_24_4FBD",        # 18, 24
        "Function_25_57E0",        # 19, 25
        "Function_26_61D5",        # 1A, 26
        "Function_27_6C12",        # 1B, 27
        "Function_28_710D",        # 1C, 28
        "Function_29_7AAD",        # 1D, 29
        "Function_30_7ACD",        # 1E, 30
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
        (
            "This is Crossbell\x01",
            "Police.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E5(0x4)"), scpexpr(EXPR_END)), "loc_69A")

    AnonymousTalk(
        0xFF,
        (
            "I will receive your\x01",
            "report.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x8, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xC)
    SetChrName("Announcement")

    AnonymousTalk(
        0xFF,
        (
            "Report processing,\x01",
            "complete. Thank you for\x01",
            "your hard work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BD")

    label("loc_69A")


    AnonymousTalk(
        0xFF,
        (
            "There no reportable\x01",
            "requests.\x02",
        )
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
            "#00204FIt looks like you've won\x01",
            "against all "Pom!"\x01",
            "opponents, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01905FWow, really!?\x02\x03",
            "#01909FThat Lloyd for you...\x01",
            "He's too amazing!!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_END)), "loc_A33")

    ChrTalk(
        0x9,
        (
            "#02302FHeh, that's right.\x01",
            "You're pretty good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A33")

    SetChrSubChip(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#00009FHaha, thanks. I just got\x01",
            "lucky, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FNo. In puzzle games like that,\x01",
            "luck isn't the primary factor\x01",
            "that determines the winner.\x02\x03",
            "#12102FBannings, you are a true "Pom!\x01",
            "Master".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F...T-Thank you for that.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xF0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D28")

    ChrTalk(
        0x8,
        (
            "#12100FHmm... That's right.\x02\x03",
            "If you like, please take\x01",
            "this.\x02",
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
            "#12100FIt's a forbidden master quartz, jointly\x01",
            "developed by the church and Epstein\x01",
            "Foundation using ancient techniques.\x02\x03",
            "Being it too powerful and difficult to\x01",
            "handle it's something we hesitated to\x01",
            "use, but...\x02\x03",
            "#12102FBecause it is you, I'm sure you'll\x01",
            "handle it correctly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FSure, understood. I'll\x01",
            "put it to good use,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E01")

    label("loc_D28")


    ChrTalk(
        0x8,
        (
            "#12100FHmm... That's right.\x02\x03",
            "#12102FI'll give you this as a\x01",
            "prize.\x02",
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
            "#00000FHaha, thanks. I'll put\x01",
            "it to good use.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_E01")

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

    def Function_6_E33(): pass

    label("Function_6_E33")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_ED2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E56")
    Call(0, 22)
    Jump("loc_ECD")

    label("loc_E56")


    ChrTalk(
        0x10,
        (
            "#00102F(...See you later.)\x02\x03",
            "#00104F(I don't mind if you're\x01",
            "late, so please take your\x01",
            "time and finish to prepare.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ECD")

    Jump("loc_11F4")

    label("loc_ED2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1173")

    ChrTalk(
        0x10,
        (
            "#00103FThe Crossbell City liberation operation...\x01",
            "It finally starts tomorrow.\x02\x03",
            "#00108FIf we see Bell or "uncle", I'll ask them the\x01",
            "reasoning behind this chain of events... And\x01",
            "if possible, I want to persuade them.\x02\x03",
            "#00101FBut, if they don't agree...\x02",
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
            "#00106F...I'm sorry. I'm just\x01",
            "complaining.\x02\x03",
            "#00100FTo reward the many who lent\x01",
            "a hand without turning\x01",
            "their backs on danger...\x02\x03",
            "And above all to take back\x01",
            "KeA, we mustn't lose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F...Let's do our best together\x01",
            "tomorrow, Elie. Everyone,\x01",
            "myself included, is with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#00104F...Haha, that's right.\x02\x03",
            "#00102FThank you, Lloyd. Thanks\x01",
            "to you, I feel a little\x01",
            "better.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 5)
    Jump("loc_11F4")

    label("loc_1173")


    ChrTalk(
        0x10,
        (
            "#00104FThank you, Lloyd. Thanks\x01",
            "to you, I feel just a\x01",
            "little better.\x02\x03",
            "#00102FSleep well tonight... To\x01",
            "prepare for tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11F4")

    TalkEnd(0xFE)
    Return()

    # Function_6_E33 end

    def Function_7_11F8(): pass

    label("Function_7_11F8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1299")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_121B")
    Call(0, 23)
    Jump("loc_1294")

    label("loc_121B")


    ChrTalk(
        0xB,
        (
            "#00204FOnce I finished here, I\x01",
            "will head to the deck as\x01",
            "well.\x02\x03",
            "#00202FAbout that discussion...\x01",
            "I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1294")

    Jump("loc_1796")

    label("loc_1299")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16ED")

    ChrTalk(
        0xB,
        (
            "#00203F(*furious typing*)\x02\x03",
            "#00200FHmm. Preparations are\x01",
            "complete for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FTio... What are you\x01",
            "doing?\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_13BF")
    Jump("loc_1409")

    label("loc_13BF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13DF")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1409")

    label("loc_13DF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13FF")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1409")

    label("loc_13FF")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1409")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)

    ChrTalk(
        0xB,
        (
            "#00202FI'm performing a final check of the\x01",
            "Merkabah's systems for tomorrow's sortie.\x02\x03",
            "#00203FAlthough I am planning to disembark\x01",
            "tomorrow with all of you...\x02\x03",
            "#00200FAfter gaining control of the communication\x01",
            "terminal, I'll have to leave the rest of\x01",
            "the hacking to Jona and Fran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FI see... That seems\x01",
            "difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00204FWell, I'll be done soon,\x01",
            "so there's no need to\x01",
            "worry.\x02\x03",
            "#00202FAs leader, it's enough\x01",
            "if you just save your\x01",
            "strength.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FNo, no. I've got lots to\x01",
            "do to prepare for\x01",
            "tomorrow.\x02\x03",
            "#00000FWell, I'll leave it to\x01",
            "you, then.\x02\x03",
            "Make sure you all get\x01",
            "proper rest, ok?\x02",
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
    Jump("loc_1796")

    label("loc_16ED")


    ChrTalk(
        0xB,
        (
            "#00204FI'm performing a final check\x01",
            "of the Merkabah's systems\x01",
            "for tomorrow's sortie.\x02\x03",
            "#00202FI'm almost done, and I plan\x01",
            "to rest myself. Please sleep\x01",
            "well as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1796")

    TalkEnd(0xFE)
    Return()

    # Function_7_11F8 end

    def Function_8_179A(): pass

    label("Function_8_179A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_182A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17BD")
    Call(0, 24)
    Jump("loc_1825")

    label("loc_17BD")


    ChrTalk(
        0xE,
        (
            "#00304FSee you later, then.\x02\x03",
            "#00302FI'll be right there once\x01",
            "I finish maintaining\x01",
            "this little guy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1825")

    Jump("loc_1B99")

    label("loc_182A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AF9")

    ChrTalk(
        0xE,
        "#00300FYo, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIt looks like you guys\x01",
            "are maintaining your\x01",
            "weapons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00302FYeah. They say tomorrow's\x01",
            "operation will be the biggest\x01",
            "turning point yet.\x02\x03",
            "#00304FIt'll probably be Berzerker's\x01",
            "turn too, so I want to make sure\x01",
            "he's ready when the time comes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FHmm. I suppose there really\x01",
            "haven't been many chances\x01",
            "to use him up until now...\x02\x03",
            "#00003FMaybe I should repair my\x01",
            "tonfas tonight, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00309FYeah, that's the way.\x02\x03",
            "#00303FUnlike a rifle, yours\x01",
            "doesn't have any small parts\x01",
            "that need maintenance...\x02\x03",
            "#00300FJust throwing some polish on\x01",
            "there might be enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FI-I see... I suppose\x01",
            "you're right.\x02\x03",
            "#00002FThanks for the advice.\x01",
            "I'll do mine later.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 7)
    Jump("loc_1B99")

    label("loc_1AF9")


    ChrTalk(
        0xE,
        (
            "#00304FOn my end, I've got to do\x01",
            "proper maintenance for\x01",
            "tomorrow.\x02\x03",
            "#00309FAnd just like dealing with\x01",
            "peerless beauties, you have\x01",
            "to be gentle and careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B99")

    TalkEnd(0xFE)
    Return()

    # Function_8_179A end

    def Function_9_1B9D(): pass

    label("Function_9_1B9D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x68), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1C49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BC0")
    Call(0, 25)
    Jump("loc_1C44")

    label("loc_1BC0")


    ChrTalk(
        0xF,
        (
            "#10106FU-Umm... I would love for\x01",
            "you to come.\x02\x03",
            "#10101FPlease come to the deck\x01",
            "later. I'll head there\x01",
            "once I'm finished here...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C44")

    Jump("loc_1CF0")

    label("loc_1C49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C5B")
    Call(0, 10)
    Jump("loc_1CF0")

    label("loc_1C5B")


    ChrTalk(
        0xF,
        (
            "#10100FI'd like to get in\x01",
            "contact with command once\x01",
            "more tonight.\x02\x03",
            "#10103FI think we should get\x01",
            "final confirmation before\x01",
            "tomorrow's operation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CF0")

    TalkEnd(0xFE)
    Return()

    # Function_9_1B9D end

    def Function_10_1CF4(): pass

    label("Function_10_1CF4")

    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x101, 0)
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1D85")
    Jump("loc_1DCF")

    label("loc_1D85")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1DA5")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1DCF")

    label("loc_1DA5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DC5")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1DCF")

    label("loc_1DC5")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1DCF")

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
            "#00000FGood work, Noｱl and\x01",
            "Fran.\x02\x03",
            "#00002FYou guys are rather calm\x01",
            "heading into tomorrow's\x01",
            "operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#10102FUmm, sorry.\x02\x03",
            "#10106FI was maintaining my\x01",
            "weapons when Fran came\x01",
            "in...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01909FHaha, I came to support\x01",
            "my sister~.\x02\x03",
            "#01904FI've already finished\x01",
            "preparing for tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, thank you for that.\x02\x03",
            "#00000FBecause of your efforts\x01",
            "as operator, we were able\x01",
            "to restore our energy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01902FYes, of course~. ...I\x01",
            "should say, that's why I'm\x01",
            "here!\x02\x03",
            "#01909FHow to say it... My energy\x01",
            "is refilled just by being\x01",
            "by my sister's side!\x02",
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
            "#00000FHaha. That doesn't seem\x01",
            "like a joke, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#10106F*sigh*, c'mon... At least\x01",
            "stay out of my way, ok?\x02\x03",
            "#10100FU-Umm, Lloyd. I'd like to\x01",
            "get in contact with\x01",
            "command once more tonight.\x02\x03",
            "#10103FI think we should get\x01",
            "final confirmation before\x01",
            "tomorrow's operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah, thanks.\x02\x03",
            "#00000FYou should get some sleep\x01",
            "once you've finished your\x01",
            "maintenance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#10109FYes, sir!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xF, 0x0)
    OP_93(0xC, 0x10E, 0x0)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x1DB, 0)
    Return()

    # Function_10_1CF4 end

    def Function_11_2207(): pass

    label("Function_11_2207")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x69), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_22C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_222A")
    Call(0, 26)
    Jump("loc_22BF")

    label("loc_222A")


    ChrTalk(
        0xA,
        (
            "#10404FThere's just one more\x01",
            "thing, and I want to\x01",
            "tell you in secret.\x02\x03",
            "#10402FCome to the deck later.\x01",
            "I'll be there once I\x01",
            "finish Abbas' drink.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22BF")

    Jump("loc_239C")

    label("loc_22C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22D6")
    Call(0, 12)
    Jump("loc_239C")

    label("loc_22D6")


    ChrTalk(
        0xA,
        (
            "#10404FWell, we got permission from the\x01",
            "higher-ups, so we can carry out\x01",
            "the mission without hesitation.\x02\x03",
            "#10402FHaha. Looks like it's going to\x01",
            "be busy tomorrow. Better relax\x01",
            "while I still can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_239C")

    TalkEnd(0xFE)
    Return()

    # Function_11_2207 end

    def Function_12_23A0(): pass

    label("Function_12_23A0")

    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x101, 0)
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2431")
    Jump("loc_247B")

    label("loc_2431")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2451")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_247B")

    label("loc_2451")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2471")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_247B")

    label("loc_2471")

    OP_52(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_247B")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2531")
    Jump("loc_257B")

    label("loc_2531")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2551")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_257B")

    label("loc_2551")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2571")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_257B")

    label("loc_2571")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_257B")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0x8, 0x10)

    ChrTalk(
        0x101,
        (
            "#00005FWazy, Abbas... Are you\x01",
            "guys drinking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10404FBoth of us have finished\x01",
            "preparing for now, you\x01",
            "see.\x02\x03",
            "#10402FHaha, care to join us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FHey now... Will it be all\x01",
            "right, even though the\x01",
            "operation's tomorrow?\x02\x03",
            "#00001FIt looks like there\x01",
            "already a lot of empty\x01",
            "glasses there.\x02",
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
            "#00006FOh, I see...\x02\x03",
            "#00000FWell if you say so\x01",
            "Abbas, I think I can\x01",
            "believe you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10409FHehe. I wouldn't mind if you\x01",
            "believed me when I drink alone,\x01",
            "too.\x02\x03",
            "#10403F...That's right, I should have\x01",
            "told you guys earlier.\x02\x03",
            "#10400FOfficial permission has come down\x01",
            "from the pope for participation\x01",
            "in tomorrow's operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FAh... So that's what it\x01",
            "was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FThe Merkabah operates in secret. We\x01",
            "normally avoid its use during large\x01",
            "scale operations, but...\x02\x03",
            "When we thought about the confusion\x01",
            "across the continent, perhaps a\x01",
            "little exposure can't be avoided.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FI see... I'm grateful\x01",
            "for the Church's\x01",
            "decision.\x02\x03",
            "#00013F...Anyway, the\x01",
            "operation's tomorrow.\x01",
            "Let's do this, Wazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10402FHehe. Roger that,\x01",
            "leader.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12102FAllow us to assist you,\x01",
            "of course.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetScenarioFlags(0x1DB, 1)
    Return()

    # Function_12_23A0 end

    def Function_13_2A6C(): pass

    label("Function_13_2A6C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x69), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2BA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A94")
    Call(0, 26)
    Jump("loc_2BA0")

    label("loc_2A94")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2A9E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BA0")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",              # 0
            "Change Party\x01",      # 1
            "Cancel\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2AEB"),
        (1, "loc_2B75"),
        (SWITCH_DEFAULT, "loc_2B91"),
    )


    label("loc_2AEB")


    ChrTalk(
        0x8,
        (
            "#12100FMan... So he was hiding\x01",
            "something else, huh.\x02\x03",
            "#12102F...Well, it can't be\x01",
            "helped. If it is you\x01",
            "guys, there's no problem.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B9B")

    label("loc_2B75")

    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(0)
    Fade(500)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2B9B")

    label("loc_2B91")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2B9B")

    Jump("loc_2A9E")

    label("loc_2BA0")

    Jump("loc_2CD7")

    label("loc_2BA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BB7")
    Call(0, 12)
    Jump("loc_2CD7")

    label("loc_2BB7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2BC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CD7")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",              # 0
            "Change Party\x01",      # 1
            "Cancel\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2C0E"),
        (1, "loc_2CAC"),
        (SWITCH_DEFAULT, "loc_2CC8"),
    )


    label("loc_2C0E")


    ChrTalk(
        0x8,
        (
            "#12100FTomorrow's operation... The\x01",
            "Merkabah will focus on\x01",
            "backing you up.\x02\x03",
            "You all will be infiltrating\x01",
            "the city. You should prepare\x01",
            "without delay.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CD2")

    label("loc_2CAC")

    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(0)
    Fade(500)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2CD2")

    label("loc_2CC8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2CD2")

    Jump("loc_2BC1")

    label("loc_2CD7")

    TalkEnd(0xFE)
    Return()

    # Function_13_2A6C end

    def Function_14_2CDB(): pass

    label("Function_14_2CDB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x68), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2DBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CFE")
    Call(0, 25)
    Jump("loc_2DB6")

    label("loc_2CFE")


    ChrTalk(
        0xC,
        (
            "#01900FLloyd, please listen to\x01",
            "my sister's wish.\x02\x03",
            "#01909FHaha, I'm looking\x01",
            "forward to what will\x01",
            "happen~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Hmm. I wonder why\x01",
            "Fran's looking forward\x01",
            "to it that much...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DB6")

    Jump("loc_2E47")

    label("loc_2DBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DCD")
    Call(0, 10)
    Jump("loc_2E47")

    label("loc_2DCD")


    ChrTalk(
        0xC,
        (
            "#01902FLloyd, please do your\x01",
            "best tomorrow, ok?\x02\x03",
            "#01909FAs for me, my sister\x01",
            "refilled my energy, so\x01",
            "I'm ready to go!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E47")

    TalkEnd(0xFE)
    Return()

    # Function_14_2CDB end

    def Function_15_2E4B(): pass

    label("Function_15_2E4B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3213")

    ChrTalk(
        0x9,
        (
            "#02300FWhen you guys infiltrate the city\x01",
            "tomorrow, I'll start hacking from the\x01",
            "Merkabah.\x02\x03",
            "#02303FWell, do your best to throw the city\x01",
            "into chaos, ok?\x02\x03",
            "#02302FIf they're confused in the real\x01",
            "world, it'll probably create an\x01",
            "exploitable opening in the orbal net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah. Let's both execute our\x01",
            "assigned duties.\x02\x03",
            "#00001F...By the way, Jona... You're\x01",
            "not pulling an all-nighter\x01",
            "tonight, are you? (*stare*)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#02305F...*gulp*\x02\x03",
            "#02309FN-Nah... See? I'm almost done\x01",
            "preparing, but I'm a night\x01",
            "owl, see?\x02\x03",
            "#02304FThe tension of staying up all\x01",
            "night 'til dawn is a better\x01",
            "feeling than poor sleep, see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FNow look here... Tomorrow's going to\x01",
            "be a long day. And you're staying up\x01",
            "all night?\x02\x03",
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
            "#02300FI'll get to bed right after\x01",
            "I'm finished, so you don't\x01",
            "have to glare so much.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 3)
    Jump("loc_32AB")

    label("loc_3213")


    ChrTalk(
        0x9,
        (
            "#02300FI'll be done preparing for\x01",
            "tomorrow's hacking shorty.\x02\x03",
            "#02306FI'll get to bed right after\x01",
            "I'm finished, so you don't\x01",
            "have to glare so much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32AB")

    TalkEnd(0xFE)
    Return()

    # Function_15_2E4B end

    def Function_16_32AF(): pass

    label("Function_16_32AF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3670")

    ChrTalk(
        0x12,
        (
            "#02103FThe Crossbell City liberation operation... You\x01",
            "who protested the current system gathered, and\x01",
            "will put your lives on the line for it...\x02\x03",
            "#02101FIf this fails, "the President's justice" will\x01",
            "be the conclusion.\x02\x03",
            "#02103FJust like, during the democratization of\x01",
            "Calvard, there was a plot behind the scenes\x01",
            "that's now seen as justified.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Right.\x02\x03",
            "#00001FEverything rests on tomorrow...\x01",
            "You understand well that it's\x01",
            "no exaggeration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#02109FAhaha. I didn't mean to pressure you,\x01",
            "though.\x02\x03",
            "#02103F...As a journalist, my role is to\x01",
            "watch over the fate of Crossbell, and\x01",
            "communicate our mission to the people.\x02\x03",
            "#02100FBut before a journalist I am a person,\x01",
            "and I want to root for you guys.\x02\x03",
            "#02104FThe ones who were born out of, and\x01",
            "inherited Guy's will is you all, the\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FGrace...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#02109FHaha, for KeA too...\x01",
            "You've got to do your\x01",
            "best tomorrow!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, leave it to us!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 4)
    Jump("loc_3700")

    label("loc_3670")


    ChrTalk(
        0x12,
        (
            "#02100FBut before a journalist I\x01",
            "am a person, and I want\x01",
            "to root for you guys.\x02\x03",
            "#02109FFor KeA too... You've got\x01",
            "to do your best tomorrow!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3700")

    TalkEnd(0xFE)
    Return()

    # Function_16_32AF end

    def Function_17_3704(): pass

    label("Function_17_3704")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A0E")

    ChrTalk(
        0x11,
        (
            "#02503F...Tomorrow will most likely be\x01",
            "a rough day.\x02\x03",
            "#02500FAfter all, I made you young\x01",
            "ones carry a heavy burden, "the\x01",
            "fate of the autonomous state".\x02\x03",
            "#02503FAs a state representative... I\x01",
            "bow my head to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Please, don't say things\x01",
            "like that.\x02\x03",
            "#00000FYou played an important role\x01",
            "in delivering the independence\x01",
            "invalidity declaration.\x02\x03",
            "#00004FThink of the remaining\x01",
            "problems as jobs for those of\x01",
            "us who can fight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#02503F...Sorry. I didn't mean to trouble you.\x02\x03",
            "#02500FIn that case, I'll believe the "Liberation\x01",
            "Operation" will be a success, and think of\x01",
            "countermeasures going forward.\x02\x03",
            "#02503FTo return the confused citizens of\x01",
            "Crossbell to their former lives as soon as\x01",
            "possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FRight... We'll be\x01",
            "counting on you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 5)
    Jump("loc_3ABB")

    label("loc_3A0E")


    ChrTalk(
        0x11,
        (
            "#02503FI'll believe the "Liberation Operation"\x01",
            "will be a success, and think of\x01",
            "countermeasures going forward.\x02\x03",
            "#02500F...May the protection of the Goddess be\x01",
            "with you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ABB")

    TalkEnd(0xFE)
    Return()

    # Function_17_3704 end

    def Function_18_3ABF(): pass

    label("Function_18_3ABF")

    Call(0, 19)
    Return()

    # Function_18_3ABF end

    def Function_19_3AC3(): pass

    label("Function_19_3AC3")

    TalkBegin(0x14)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3AD0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DB8")
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
            "Cancel\x01",             # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B35")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3B35")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3B54")
    OP_AF(0xD8)
    Jump("loc_3BA6")

    label("loc_3B54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_3B64")
    OP_AF(0xD7)
    Jump("loc_3BA6")

    label("loc_3B64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_3B74")
    OP_AF(0xD6)
    Jump("loc_3BA6")

    label("loc_3B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_3B84")
    OP_AF(0xD5)
    Jump("loc_3BA6")

    label("loc_3B84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_3B94")
    OP_AF(0xD4)
    Jump("loc_3BA6")

    label("loc_3B94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_3BA4")
    OP_AF(0xD3)
    Jump("loc_3BA6")

    label("loc_3BA4")

    OP_AF(0xD2)

    label("loc_3BA6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3DB3")

    label("loc_3BB5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BD5")
    OP_AF(0xDC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3DB3")

    label("loc_3BD5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BE9")
    Jump("loc_3DB3")

    label("loc_3BE9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DB3")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D09")

    ChrTalk(
        0x14,
        (
            "I don't know if can take\x01",
            "an optimistic view of\x01",
            "this situation, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "The police and the church, the\x01",
            "CGF, Heiyue and even a Divine Wolf\x01",
            "and Yin have become our allies.\x02",
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
    Jump("loc_3DB3")

    label("loc_3D09")


    ChrTalk(
        0x14,
        (
            "The police and the church, the\x01",
            "CGF, Heiyue and even a Divine Wolf\x01",
            "and Yin have become our allies.\x02",
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

    label("loc_3DB3")

    Jump("loc_3AD0")

    label("loc_3DB8")

    TalkEnd(0x14)
    Return()

    # Function_19_3AC3 end

    def Function_20_3DBC(): pass

    label("Function_20_3DBC")

    Call(0, 21)
    Return()

    # Function_20_3DBC end

    def Function_21_3DC0(): pass

    label("Function_21_3DC0")

    TalkBegin(0x15)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3DCD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4033")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                   # 0
            "Modify/Synthesize\x01",      # 1
            "Cancel\x01",                 # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E2C")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3E2C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E4C")
    OP_AF(0xDD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_402E")

    label("loc_3E4C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E60")
    Jump("loc_402E")

    label("loc_3E60")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_402E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F8C")

    ChrTalk(
        0x15,
        (
            "The biggest problem with\x01",
            "tomorrow's operation will\x01",
            "likely be those three Aions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "How to drive away the Aions...\x01",
            "I think your infiltration of\x01",
            "the city will be a key to that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "We have to cooperate with\x01",
            "everyone and make this\x01",
            "operation a success.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_402E")

    label("loc_3F8C")


    ChrTalk(
        0x15,
        (
            "I think your infiltration of\x01",
            "the city will be they key to\x01",
            "driving away the Aions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "We have to cooperate with\x01",
            "everyone and make this\x01",
            "operation a success.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_402E")

    Jump("loc_3DCD")

    label("loc_4033")

    TalkEnd(0x15)
    Return()

    # Function_21_3DC0 end

    def Function_22_4037(): pass

    label("Function_22_4037")

    EventBegin(0x0)
    Fade(500)
    OP_68(100420, 1000, -101760, 0)
    MoveCamera(47, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15480, 0)
    SetChrPos(0x101, 100110, 0, -101660, 180)
    SetChrSubChip(0x10, 0x2)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45A9")

    ChrTalk(
        0x10,
        (
            "#12P#00106FThe Crossbell City liberation operation...\x01",
            "It finally starts tomorrow.\x02\x03",
            "#00108FIf we see Bell or "uncle", I'll ask them the\x01",
            "reasoning behind this chain of events... And\x01",
            "if possible, I want to persuade them.\x02\x03",
            "#00101FBut, if they don't agree...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5P...We won't be able to\x01",
            "avoid confronting them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#12P#00103FYes... And I'm already\x01",
            "prepared to accept that.\x02\x03",
            "#00108FTo reward the many who lent\x01",
            "a hand without turning\x01",
            "their backs on danger...\x02\x03",
            "#00101FAnd above all, to take back\x01",
            "KeA, we can't lose.\x02",
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
            "#00004F#5P...Say, Elie.\x02\x03",
            "#00000FThere's no need to get\x01",
            "so worked up all by\x01",
            "yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#12P#00105FHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PAll of us were close to\x01",
            "Dieter and Mariabell\x01",
            "too.\x02\x03",
            "#00001FThat weight is not just\x01",
            "on you, Elie, it's on\x01",
            "all of us.\x02",
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
            "#00002F...Let's do our best together\x01",
            "tomorrow, Elie. Everyone,\x01",
            "myself included, is with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#12P#00104F...Haha, that's right.\x02\x03",
            "#00102FThank you, Lloyd. I feel\x01",
            "a little better now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009F#5PHaha... You're welcome.\x02",
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
            "#00112F(When you're finished\x01",
            "preparing for tomorrow,\x01",
            "would you come to the deck?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#5P(Huh?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#12P#00113F(If possible, umm... I'd\x01",
            "like to talk alone, just\x01",
            "the two of us...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 5)
    Jump("loc_4650")

    label("loc_45A9")


    ChrTalk(
        0x10,
        (
            "#12P#00112F(When you're finished\x01",
            "preparing for tomorrow,\x01",
            "would you come to the deck?)\x02\x03",
            "#00113F(If possible, umm... I'd\x01",
            "like to talk alone, just the\x01",
            "two of us...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4650")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Accept Elie's Invitation\x01",      # 0
            "Refuse\x01",                        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_472C")

    ChrTalk(
        0x101,
        (
            "#00002F#5P(...I-I understand. If\x01",
            "you're okay with me, I\x01",
            "would love to go.)\x02",
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
    Jump("loc_47EF")

    label("loc_472C")


    ChrTalk(
        0x10,
        (
            "#12P#00106F(...I see.)\x02\x03",
            "#00102F(*giggle*, don't worry\x01",
            "about it. It's not a big\x01",
            "deal.)\x02\x03",
            "#00104F(If you change your\x01",
            "mind, please speak with\x01",
            "me again.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5P(Sure, I'll be sure to.)\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_47EF")

    SetChrSubChip(0x10, 0x0)
    EventEnd(0x5)
    Return()

    # Function_22_4037 end

    def Function_23_47F6(): pass

    label("Function_23_47F6")

    EventBegin(0x0)
    Fade(500)
    OP_68(-3160, -500, 6480, 0)
    MoveCamera(52, 29, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16170, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 6)), scpexpr(EXPR_END)), "loc_4838")
    SetChrSubChip(0xB, 0x1)

    label("loc_4838")

    SetChrPos(0x101, -3610, -1500, 5780, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D4E")

    ChrTalk(
        0xB,
        (
            "#11P#00203F(*furious typing*)\x02\x03",
            "#00200FHmm. Preparations are\x01",
            "complete for now.\x02",
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
            "#00203F...............\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005F...Umm, Tio? What are\x01",
            "you doing?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0xB, 0x1)

    ChrTalk(
        0xB,
        (
            "#5P#00202F...I was performing a final check of the\x01",
            "Merkabah's systems for tomorrow's sortie.\x02\x03",
            "#00203FAlthough I am planning to disembark\x01",
            "tomorrow with all of you...\x02\x03",
            "#00200FAfter gaining control of the communication\x01",
            "terminal, I'll have to leave the rest of\x01",
            "the hacking to Jona and Fran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FI see... That seems\x01",
            "difficult.\x02\x03",
            "#00000FIs there anything I can\x01",
            "help with?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#00203F...No, not especially.\x02\x03",
            "#00202FGiven my field, Jona\x01",
            "here should be enough.\x02\x03",
            "#00204FAs leader, it's enough\x01",
            "if you just save your\x01",
            "strength.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00006FNo, no. I've got lots to\x01",
            "do to prepare for\x01",
            "tomorrow.\x02\x03",
            "#00000FWell, I'll leave it to\x01",
            "you, then.\x02",
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
            "#00208FActually... There's\x01",
            "something I want to\x01",
            "discuss with you, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FA discussion? Is there\x01",
            "something you're worried\x01",
            "about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#00206F...No, not here.\x02\x03",
            "#00201FOnce you've finished what you\x01",
            "need to, will you come to the\x01",
            "Merkabah's deck later?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 6)
    ClearChrFlags(0xB, 0x10)
    Jump("loc_4DF9")

    label("loc_4D4E")


    ChrTalk(
        0xB,
        (
            "#5P#00206FActually... There's something\x01",
            "I want to discuss with you,\x01",
            "Lloyd.\x02\x03",
            "#00201FOnce you've finished what you\x01",
            "need to, will you come to the\x01",
            "Merkabah's deck later?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DF9")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Accept Tio's Invitation\x01",      # 0
            "Refuse\x01",                       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4ED9")

    ChrTalk(
        0x101,
        (
            "#12P#00002FUnderstood. If you're okay\x01",
            "with me, I would be happy\x01",
            "to discuss this with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#00209FHaha... I'll be counting\x01",
            "on you then.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 27)
    SetScenarioFlags(0x1AA, 4)
    Jump("loc_4FB6")

    label("loc_4ED9")


    ChrTalk(
        0xB,
        (
            "#5P#00204F...I see. Well, it can't\x01",
            "be helped.\x02\x03",
            "#00202FIf you change your mind,\x01",
            "speak with me again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FThe ones who were born out from,\x01",
            "and inherited Guy's will is you\x01",
            "all, the Special Support Section.\x02",
        )
    )

    OP_5A()
    CloseMessageWindow()

    label("loc_4FB6")

    SetChrSubChip(0xB, 0x0)
    EventEnd(0x5)
    Return()

    # Function_23_47F6 end

    def Function_24_4FBD(): pass

    label("Function_24_4FBD")

    EventBegin(0x0)
    Fade(500)
    OP_68(98200, 1000, 600, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16090, 0)
    SetChrPos(0x101, 97510, 0, -530, 0)
    SetChrSubChip(0xE, 0x2)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55C9")

    ChrTalk(
        0xE,
        "#5P#00300FYo, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FIt looks like you guys\x01",
            "are maintaining your\x01",
            "weapons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5P#00302FYeah. They say tomorrow's\x01",
            "operation will be the biggest\x01",
            "turning point yet.\x02\x03",
            "#00304FIt'll probably be Berzerker's\x01",
            "turn too, so I want to make sure\x01",
            "he's ready when the time comes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FHmm. I suppose there really\x01",
            "haven't been many chances\x01",
            "to use him up until now...\x02\x03",
            "#00003FMaybe I should repair my\x01",
            "tonfas tonight, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5P#00309FYeah, that's the way.\x02\x03",
            "#00303FUnlike a rifle, yours\x01",
            "doesn't have any small parts\x01",
            "that need maintenance...\x02\x03",
            "#00300FJust throwing some polish on\x01",
            "there might be enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00009FHaha, that's true.\x02\x03",
            "#00005FEven so... You're more diligent than\x01",
            "I thought.\x02\x03",
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
            "#00304FYou've got to treat them just\x01",
            "as if they were peerless\x01",
            "beauties─ gently and carefully.\x02\x03",
            "#00300FIf you don't, you'll find\x01",
            "yourself in trouble in battle─\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xE)

    ChrTalk(
        0x101,
        (
            "#12P#00011F...Sorry. Could I have\x01",
            "made you remember\x01",
            "something unpleasant?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5P#00309F...Haha, what are you\x01",
            "apologizing for?\x02\x03",
            "#00306F...But you're right.\x02\x03",
            "#00308FMaybe... it's about time\x01",
            "I told you about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5P#00300FSay, if you're free\x01",
            "later, want to come to\x01",
            "the Merkabah's deck?\x02\x03",
            "I'd just like you to\x01",
            "join me for a little\x01",
            "while.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 7)
    Jump("loc_564A")

    label("loc_55C9")


    ChrTalk(
        0xE,
        (
            "#5P#00300FHey. If you're free\x01",
            "later, want to come to\x01",
            "the Merkabah's deck?\x02\x03",
            "I'd just like you to\x01",
            "join me for a little\x01",
            "while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_564A")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Accept Randy's Invitation\x01",      # 0
            "Refuse\x01",                         # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5735")

    ChrTalk(
        0x101,
        (
            "#12P#00002F...Understood. I'll go\x01",
            "there later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5P#00309FHaha. Later, then.\x02\x03",
            "#00302FI'll be right there once\x01",
            "I finish maintaining\x01",
            "this little guy.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 27)
    SetScenarioFlags(0x1AA, 5)
    Jump("loc_57D9")

    label("loc_5735")


    ChrTalk(
        0xE,
        (
            "#5P#00306F...I see. It's not like\x01",
            "it was something\x01",
            "especially fun, but...\x02\x03",
            "#00300FIf you change your mind,\x01",
            "speak with me again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYeah, I will.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_57D9")

    SetChrSubChip(0xE, 0x0)
    EventEnd(0x5)
    Return()

    # Function_24_4FBD end

    def Function_25_57E0(): pass

    label("Function_25_57E0")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F49")

    ChrTalk(
        0xF,
        "#5P#10100FLloyd, good work today!\x02",
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
            "#12P#00000FGood work, Noｱl and\x01",
            "Fran.\x02\x03",
            "#00009FYou guys are rather calm\x01",
            "heading into tomorrow's\x01",
            "operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5P#10102FUmm, sorry.\x02\x03",
            "#10106FI was maintaining my\x01",
            "weapons when Fran came\x01",
            "in...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5P#01909FHaha, I came to support\x01",
            "my sister~.\x02\x03",
            "#01904FI've already finished\x01",
            "preparing for tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00004FHaha, thank you for that.\x02\x03",
            "#00000FBecause of your efforts\x01",
            "as operator, we were able\x01",
            "to restore our energy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5P#01902FYes, of course~. ...I\x01",
            "should say, that's why I'm\x01",
            "here!\x02\x03",
            "#01909FHow to say it... My energy\x01",
            "is refilled just by being\x01",
            "by my sister's side!\x02",
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
            "#12P#00012FHaha. That doesn't seem\x01",
            "like a joke, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5P#10106F*sigh*, c'mon... At least\x01",
            "stay out of my way, ok?\x02\x03",
            "#10102FU-Umm, Lloyd. I'd like to\x01",
            "get in contact with\x01",
            "command once more tonight.\x02\x03",
            "#10103FI think we should get\x01",
            "final confirmation before\x01",
            "tomorrow's operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FYeah. I'll be counting\x01",
            "on you.\x02\x03",
            "#00003FYou'll be infiltrating\x01",
            "the city with us\x01",
            "tomorrow, Noｱl...\x02\x03",
            "#00000FOnce everything's ready,\x01",
            "make sure you get proper\x01",
            "rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#5P#10109FYes, sir!\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xC)

    ChrTalk(
        0xC,
        (
            "#11P#01905F(Hey. Big sis. Don't you feel\x01",
            "that today's conversation\x01",
            "will end at this rate?)\x02\x03",
            "#01909F(This is your chance! Are you\x01",
            "sure you're okay ending it\x01",
            "here??)\x02",
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
            "...Fran, cut it out!)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00005F...Umm, what's wrong? Is\x01",
            "there some kind of\x01",
            "problem?\x02",
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
        "#11P#01909F(Go for it, Noｱl!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5P#10103F...Umm... Later is fine,\x01",
            "but can I ask you to\x01",
            "come to the deck?\x02\x03",
            "#10101FIt's not a big deal, but\x01",
            "there's something I want\x01",
            "to ask you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 0)
    Jump("loc_5FC1")

    label("loc_5F49")


    ChrTalk(
        0xF,
        (
            "#5P#10103F...Can you come to the\x01",
            "deck later?\x02\x03",
            "#10101FIt's not a big deal, but\x01",
            "there's something I want\x01",
            "to ask you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FC1")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Accept Noｱl's Invitation\x01",      # 0
            "Refuse\x01",                         # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60C5")

    ChrTalk(
        0x101,
        (
            "#12P#00002FYeah, understood. I feel\x01",
            "it's rare for you to ask\x01",
            "a favor though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11P#01909F(Way to go, sis!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5P#10114FT-Then... I'll head\x01",
            "there once I'm finished\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 27)
    SetScenarioFlags(0x1AA, 6)
    Jump("loc_61C3")

    label("loc_60C5")


    ChrTalk(
        0xF,
        (
            "#5P#10106FI-I see...\x02\x03",
            "#10112FNo, please don't worry\x01",
            "about it! It's really\x01",
            "not a big deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5P#01906FMrr. I guess it can't be\x01",
            "helped~.\x02\x03",
            "#01901FLloyd, if you change\x01",
            "your mind, please speak\x01",
            "with my sister again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYeah, understood.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_61C3")

    SetChrSubChip(0xF, 0x0)
    OP_93(0xC, 0x10E, 0x0)
    OP_4C(0xC, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_25_57E0 end

    def Function_26_61D5(): pass

    label("Function_26_61D5")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_699D")

    ChrTalk(
        0x101,
        (
            "#6P#00005FWazy, Abbas... Are you\x01",
            "guys drinking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#10404FBoth of us have finished\x01",
            "preparing for now, you\x01",
            "see.\x02\x03",
            "#10402FHaha, care to join us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FHey now... Will it be all\x01",
            "right, even though the\x01",
            "operation's tomorrow?\x02\x03",
            "#00001FIt looks like there\x01",
            "already a lot of empty\x01",
            "glasses there.\x02",
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
            "#6P#00006FOh, I see...\x02\x03",
            "#00000FWell if you say so\x01",
            "Abbas, I think I can\x01",
            "believe you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#10409FHehe. I wouldn't mind if you\x01",
            "believed me when I drink alone,\x01",
            "too.\x02\x03",
            "#10403F...That's right, I should have\x01",
            "told you guys earlier.\x02\x03",
            "#10400FOfficial permission has come down\x01",
            "from the pope for participation\x01",
            "in tomorrow's operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FAh... So that's what it\x01",
            "was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#12100FThe Merkabah operates in secret. We\x01",
            "normally avoid its use during large\x01",
            "scale operations, but...\x02\x03",
            "When we thought about the confusion\x01",
            "across the continent, perhaps a\x01",
            "little exposure can't be avoided.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FI see... I'm grateful\x01",
            "for the Church's\x01",
            "decision.\x02\x03",
            "#00013F...Anyway, the\x01",
            "operation's tomorrow.\x01",
            "Let's do this, Wazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#10402FHehe. Roger that,\x01",
            "leader.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#12102FAllow us to assist you,\x01",
            "of course.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "#11P#10403FYeah... that's right.\x01",
            "There's just one more\x01",
            "thing I need to tell you.\x02",
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
            "#5P#12100F...Wazy. That matter is\x01",
            "confidential at the\x01",
            "present time, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#10405FOh, really?\x02\x03",
            "#10409FHaha, then I'll tell you\x01",
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
            "#5P#12100F...Whatever. If Wazy\x01",
            "says so, then it can't\x01",
            "be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00012FI-I don't really get it,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#10404FHaha. I'm telling you,\x01",
            "this has great relevance\x01",
            "to you guys.\x02\x03",
            "#10402F─If you're interested in\x01",
            "it, can we talk on the\x01",
            "deck later?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 1)
    Jump("loc_6A26")

    label("loc_699D")


    ChrTalk(
        0xA,
        (
            "#11P#10404FThere's just one more\x01",
            "thing I need to tell\x01",
            "you.\x02\x03",
            "#10402FHaha. If you're\x01",
            "interested in it, can we\x01",
            "talk on the deck later?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A26")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Accept Wazy's Invitation\x01",      # 0
            "Refuse\x01",                        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B9B")

    ChrTalk(
        0x101,
        (
            "#6P#00006F...Understood. Should I\x01",
            "head to the deck?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11P#10409FHehe. It's decided then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#12100FWazy, let me just say\x01",
            "this. Take care not say\x01",
            "any more than...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#10404FHaha, I know, I know.\x02\x03",
            "#10400FI'll head there once I've\x01",
            "finished my drink, so\x01",
            "there's no need to hurry.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 27)
    SetScenarioFlags(0x1AA, 7)
    Jump("loc_6C07")

    label("loc_6B9B")


    ChrTalk(
        0xA,
        (
            "#11P#10405F...Really? That's fine,\x01",
            "but...\x02\x03",
            "#10404FHaha, if you change your\x01",
            "mind, speak with me\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_6C07")

    SetChrSubChip(0xA, 0x0)
    SetChrSubChip(0x8, 0x0)
    EventEnd(0x5)
    Return()

    # Function_26_61D5 end

    def Function_27_6C12(): pass

    label("Function_27_6C12")

    FadeToDark(500, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 3)), scpexpr(EXPR_END)), "loc_6CDA")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F(...I'll have to\x01",
            "apologize to Elie for\x01",
            "not being able to go.)\x02",
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
            "Lloyd apologized to Elie\x01",
            "for not being able to go\x01",
            "as promised.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 3)
    Jump("loc_710C")

    label("loc_6CDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 4)), scpexpr(EXPR_END)), "loc_6D95")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F(...I'll have to\x01",
            "apologize to Tio for not\x01",
            "being able to go.)\x02",
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
            "Lloyd apologized to Tio\x01",
            "for not being able to go\x01",
            "as promised.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 4)
    Jump("loc_710C")

    label("loc_6D95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 5)), scpexpr(EXPR_END)), "loc_6E54")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F(...I'll have to\x01",
            "apologize to Randy for\x01",
            "not being able to go.)\x02",
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
            "Lloyd apologized to\x01",
            "Randy for not being able\x01",
            "to go as promised.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 5)
    Jump("loc_710C")

    label("loc_6E54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 6)), scpexpr(EXPR_END)), "loc_6F11")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F(...I'll have to\x01",
            "apologize to Noｱl for\x01",
            "not being able to go.)\x02",
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
            "Lloyd apologized to Noｱl\x01",
            "for not being able to go\x01",
            "as promised.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 6)
    Jump("loc_710C")

    label("loc_6F11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 7)), scpexpr(EXPR_END)), "loc_6FCE")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F(...I'll have to\x01",
            "apologize to Wazy for\x01",
            "not being able to go.)\x02",
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
            "Lloyd apologized to Wazy\x01",
            "for not being able to go\x01",
            "as promised.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 7)
    Jump("loc_710C")

    label("loc_6FCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 0)), scpexpr(EXPR_END)), "loc_708D")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F(...I'll have to\x01",
            "apologize to Rixia for\x01",
            "not being able to go.)\x02",
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
            "Lloyd apologized to\x01",
            "Rixia for not being able\x01",
            "to go as promised.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AB, 0)
    Jump("loc_710C")

    label("loc_708D")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00003F(...I'll head to the deck from\x01",
            "the nap room once my preparations\x01",
            "for tomorrow are complete.)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_710C")

    Return()

    # Function_27_6C12 end

    def Function_28_710D(): pass

    label("Function_28_710D")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_771C")
    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x101, 1420, 0, -92300, 90)
    OP_68(2300, 1000, -92050, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 3)), scpexpr(EXPR_END)), "loc_7224")

    ChrTalk(
        0x101,
        (
            "#00005F#6P(Come to think of it...\x01",
            "I promised to speak with\x01",
            "Elie.)\x02\x03",
            "#00003F(......)\x02\x03",
            "#00000F(...W-What should I do?\x01",
            "Am I finished preparing\x01",
            "for tomorrow?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7581")

    label("loc_7224")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 4)), scpexpr(EXPR_END)), "loc_72D0")

    ChrTalk(
        0x101,
        (
            "#00005F#6P(Come to think of it...\x01",
            "I promised to speak with\x01",
            "Tio.)\x02\x03",
            "#00003F(......)\x02\x03",
            "#00000F(...W-What should I do?\x01",
            "Am I finished preparing\x01",
            "for tomorrow?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7581")

    label("loc_72D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 5)), scpexpr(EXPR_END)), "loc_737E")

    ChrTalk(
        0x101,
        (
            "#00005F#6P(Come to think of it...\x01",
            "I promised to speak with\x01",
            "Randy.)\x02\x03",
            "#00003F(......)\x02\x03",
            "#00000F(...W-What should I do?\x01",
            "Am I finished preparing\x01",
            "for tomorrow?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7581")

    label("loc_737E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 6)), scpexpr(EXPR_END)), "loc_742B")

    ChrTalk(
        0x101,
        (
            "#00005F#6P(Come to think of it...\x01",
            "I promised to speak with\x01",
            "Noｱl.)\x02\x03",
            "#00003F(......)\x02\x03",
            "#00000F(...W-What should I do?\x01",
            "Am I finished preparing\x01",
            "for tomorrow?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7581")

    label("loc_742B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 7)), scpexpr(EXPR_END)), "loc_74D8")

    ChrTalk(
        0x101,
        (
            "#00005F#6P(Come to think of it...\x01",
            "I promised to speak with\x01",
            "Wazy.)\x02\x03",
            "#00003F(......)\x02\x03",
            "#00000F(...W-What should I do?\x01",
            "Am I finished preparing\x01",
            "for tomorrow?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7581")

    label("loc_74D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 0)), scpexpr(EXPR_END)), "loc_7581")

    ChrTalk(
        0x101,
        (
            "#00005F#6P(Come to think of it...\x01",
            "I promised to speak with\x01",
            "Rixia.)\x02\x03",
            "#00003F(......)\x02\x03",
            "#00000F(...W-What should I do?\x01",
            "Am I finished preparing\x01",
            "for tomorrow?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7581")

    Sound(814, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Free time and the day will\x01",
            "end, and events will proceed,\x01",
            "so please be aware of that.\x07\x00\x02",
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
            "[I Still Have Other Things to Do]\x01",      # 0
            "[Speak with Partner]\x01",                   # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7665"),
        (1, "loc_766A"),
        (SWITCH_DEFAULT, "loc_7703"),
    )


    label("loc_7665")

    Jump("loc_7703")

    label("loc_766A")

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
            "And after that─ Lloyd finished\x01",
            "his preparations for tomorrow and\x01",
            "went out onto the deck at night.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x22, 0)
    NewScene("e440B", 0, 0, 0)
    IdleLoop()
    Jump("loc_7703")

    label("loc_7703")

    OP_5A()
    SetChrPos(0x0, 550, 0, -92390, 270)
    EventEnd(0x5)
    Jump("loc_7AA9")

    label("loc_771C")


    ChrTalk(
        0x101,
        (
            "#00005F(... I wonder if I should turn\x01",
            "in early tonight?)\x02\x03",
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
            "the day will end and events will\x01",
            "proceed, so please be aware of that.\x07\x00\x02",
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
            "[We Have Other Things to Do]\x01",      # 0
            "[End Free Time and Rest]\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78C1")
    Jump("loc_7AA9")

    label("loc_78C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AA9")
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
            "#00003F#6P(...I'll get everything ready\x01",
            "and then get some sleep\x01",
            "tonight in the nap room.)\x02\x03",
            "#00001F(Tomorrow's the Crossbell City\x01",
            "Liberation Operation... We'll\x01",
            "definitely make it a success!)\x02",
        )
    )

    CloseMessageWindow()
    Sound(100, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0xA, 0x1, 0x8)
    Sleep(500)

    def lambda_7A27():
        OP_95(0xFE, 4300, 0, -92030, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7A27)
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

    label("loc_7AA9")

    TalkEnd(0xFF)
    Return()

    # Function_28_710D end

    def Function_29_7AAD(): pass

    label("Function_29_7AAD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x0, -150, 0, -88230, 180)
    EventEnd(0x5)
    Return()

    # Function_29_7AAD end

    def Function_30_7ACD(): pass

    label("Function_30_7ACD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50203.itc", 0x1E)
    LoadChrToIndex("chr/ch06902.itc", 0x1F)
    LoadChrToIndex("chr/ch06000.itc", 0x20)
    LoadChrToIndex("chr/ch05800.itc", 0x21)
    SoundLoad(943)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7B07")
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_7B07")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7B1A")
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_7B1A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7B2D")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_7B2D")

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
            "And thusly, the impenetrable\x01",
            "Barrier surrounding Crossbell\x01",
            "City disappeared.\x02\x03",
            "Lloyd contacted Cao of Heiyue\x01",
            "and Mireille of the\x01",
            "Resistance...\x02\x03",
            "Furthermore, Commander Sonya and\x01",
            "her Bellguard and Tangram units\x01",
            "promised to remain neutral.\x02\x03",
            "And then─\x02\x03",
            "That night, Father Kevin\x01",
            "received a call on the Merkabah\x01",
            "bridge.\x07\x00\x02",
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
            "─All righty then. We've\x01",
            "entered their firing range but\x01",
            "there's no sign of attack.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x105,
        (
            "#10403F#6PYeah, it seems the Aions\x01",
            "are focused on city\x01",
            "defense.\x02\x03",
            "#10400FWe should be fine as long\x01",
            "as we don't get any\x01",
            "closer to Crossbell City.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(90, -1, -1, -1)
    SetChrName("Father Kevin")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Alright, think I have a\x01",
            "rough idea of the\x01",
            "situation.\x02\x03",
            "I'll return here\x01",
            "tomorrow at dawn.\x02\x03",
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
        "#10402F#6PHaha, roger.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(190, -1, -1, -1)
    SetChrName("Ries' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2S...Kevin, it's me, Ries.\x07\x00\x02",
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
        "#00102F#12PRies...\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(160, -1, -1, -1)
    SetChrName("Sister Ries")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "...Elie. Thank goodness\x01",
            "you're safe.\x02\x03",
            "And Lloyd and everyone\x01",
            "else, too.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00002F#12PHaha, fortunately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#12PMan, I didn't think I'd\x01",
            "get to talk to you like\x01",
            "this, Ries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#12P#NYou're helping us with\x01",
            "our raid, aren't you?\x02",
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
            "city with this Merkabah.\x02\x03",
            "We can't deal with the\x01",
            "jaegers or National Guard,\x01",
            "though...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00004F#12P...That's plenty. We\x01",
            "couldn't do it without\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#12PRies, Kevin... I don't\x01",
            "know how we can ever\x01",
            "thank you...\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(90, -1, -1, -1)
    SetChrName("Father Kevin")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Well if you want to thank us,\x01",
            "you can conduct this operation\x01",
            "safely and successfully.\x02\x03",
            "We do intend to back you up a\x01",
            "little bit, but...\x02\x03",
            "It'll be plenty tough going up\x01",
            "against those dolls.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x103,
        "#00208F#12P#NThat's true...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00301F#12PDon't do anything too\x01",
            "reckless, alright?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(105, -1, -1, -1)
    SetChrName("Father Kevin")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Haha, thanks.\x02\x03",
            "─Wazy. See you tomorrow\x01",
            "morning.\x07\x00\x02",
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
            "Ries out.\x07\x00\x02",
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

    def lambda_8581():
        TurnDirection(0x11, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_8581)
    Sleep(50)

    def lambda_8591():
        TurnDirection(0x12, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_8591)
    Sleep(50)

    def lambda_85A1():
        TurnDirection(0x13, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_85A1)
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
            "#02501F#5P─Mmm. Looks like this is\x01",
            "going to be one tough\x01",
            "day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#02106F#6P#NRight... On the surface, the\x01",
            "President's combat strength\x01",
            "far exceeds our own.\x02\x03",
            "#02101FAnd that's not even\x01",
            "including those dolls. How\x01",
            "strong can you get?\x02",
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
            "#12100F#5PYes, I think it's safe\x01",
            "to assume that.\x02\x03",
            "This No. 9 unit will\x01",
            "need to keep an eye on\x01",
            "that white frame.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#5PIn any case, the battles\x01",
            "at the city perimeter are\x01",
            "expected to be stalemates.\x02\x03",
            "#10401FTherefore, we infiltrators\x01",
            "will be the key.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#12PYeah, I know.\x02\x03",
            "#00013F...We need to sneak inside\x01",
            "somehow and rendezvous with\x01",
            "chief and Detective Dudley.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#11PBut, are they all right?\x02\x03",
            "#00301FWhen Dudley contacted us,\x01",
            "the signal was cut right\x01",
            "in the middle of it.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x1)
    Sleep(200)

    ChrTalk(
        0x9,
        (
            "#02305F#5PProbably, the transmitting\x01",
            "terminal was forcibly\x01",
            "isolated.\x02\x03",
            "#02303FThey probably made it so that\x01",
            "specific ENIGMA serial numbers\x01",
            "can't send or receive.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0x2)
    Sleep(100)

    ChrTalk(
        0xC,
        (
            "#01901F#5PThen the President can\x01",
            "transmit in the city and\x01",
            "we can't?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#12PYes. It seems we need to\x01",
            "gain control of the\x01",
            "communications mainframe.\x02\x03",
            "#00208FIt's inside Orchis Tower,\x01",
            "so it won't be that easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#12PIn any case...\x01",
            "Everything starts\x01",
            "tomorrow morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#12PYes... The "Crossbell\x01",
            "City Liberation\x01",
            "Operation".\x02\x03",
            "#00101FTo have any chance of\x01",
            "freeing KeA too, we have\x01",
            "to make it a success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PYeah... Tonight we need\x01",
            "to rest and get ready\x01",
            "for tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00004F#5PEveryone, there's a nap\x01",
            "room, so if you're\x01",
            "tired, please rest.\x02\x03",
            "#00000FWe'll be fully\x01",
            "prepared... And face\x01",
            "tomorrow head on.\x02",
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x79), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8D4B")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8D4B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7A), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8D62")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8D62")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7B), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8D79")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8D79")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7D), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8D90")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8D90")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7C), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8DA7")
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8DA7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7E), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8DBE")
    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8DBE")

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

    # Function_30_7ACD end

    SaveToFile()

Try(main)
