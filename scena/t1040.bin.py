from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1040.bin",                # FileName
        "t1040",                    # MapName
        "t1040",                    # Location
        0x0043,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 67, 0, 2, 0, 3],
    )

    BuildStringList((
        "t1040",                  # 0
        "Ryｹto",                 # 1
        "Marcy",                  # 2
        "Woman",                  # 3
        "Tourist",                # 4
        "Tourist",                # 5
        "Tourist",                # 6
        "Tourist",                # 7
        "Tourist",                # 8
        "Tourist",                # 9
        "Tourist",                # 10
        "Wazy",                   # 11
        "Mrs. Margaret",          # 12
        "Winona",                 # 13
        "Drona",                  # 14
        "Tourist",                # 15
        "Elie",                   # 16
        "Fran",                   # 17
        "Cecil",                  # 18
        "Ilya",                   # 19
        "Rixia",                  # 20
    ))

    AddCharChip((
        "chr/ch25000.itc",                   # 00
        "chr/ch34500.itc",                   # 01
        "chr/ch33202.itc",                   # 02
        "chr/ch24002.itc",                   # 03
        "chr/ch21702.itc",                   # 04
        "chr/ch21802.itc",                   # 05
        "chr/ch21902.itc",                   # 06
        "chr/ch33102.itc",                   # 07
        "chr/ch44202.itc",                   # 08
        "chr/ch34402.itc",                   # 09
        "chr/ch27900.itc",                   # 0A
        "chr/ch26600.itc",                   # 0B
        "chr/ch33300.itc",                   # 0C
        "chr/ch03002.itc",                   # 0D
        "chr/ch00100.itc",                   # 0E
        "chr/ch08500.itc",                   # 0F
        "chr/ch07500.itc",                   # 10
        "chr/ch05100.itc",                   # 11
        "chr/ch05200.itc",                   # 12
        "chr/ch44002.itc",                   # 13
    ))

    DeclNpc(4294863227, 0,       2980,    90,   261,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4294866197, 0,       5880,    90,   257,  0x0, 0,   1,   0,   0,   1,   0,   8,   255,  0)
    DeclNpc(4294865477, 119,     4294966417, 270,  453,  0x0, 0,   2,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(4294862496, 119,     8930,    45,   453,  0x0, 0,   3,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(4294864296, 119,     10930,   225,  453,  0x0, 0,   4,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(4294869337, 119,     19090,   45,   453,  0x0, 0,   5,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(4294869337, 119,     19090,   45,   453,  0x0, 0,   6,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(4294862496, 119,     8930,    45,   453,  0x0, 0,   7,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   8,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(4294871176, 119,     20889,   225,  453,  0x0, 0,   9,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(4294865506, 119,     1120,    270,  453,  0x0, 0,   13,  0,   255, 255, 0,   4,   255,  0)
    DeclNpc(4294865506, 119,     4294966386, 270,  453,  0x0, 0,   19,  0,   255, 255, 0,   29,  255,  0)
    DeclNpc(4294965436, 0,       10640,   180,  261,  0x0, 0,   10,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(4294961046, 0,       6099,    180,  261,  0x0, 0,   11,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(4294959107, 0,       7510,    0,    389,  0x0, 0,   12,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(4294963246, 0,       4530,    270,  389,  0x0, 0,   14,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(4294959126, 0,       7940,    270,  389,  0x0, 0,   15,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(4300,    0,       5079,    90,   389,  0x0, 0,   16,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   17,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   18,  0,   0,   0,   0,   17,  255,  0)

    DeclActor(4294965526, 0,       8810,    1000,    4294965436, 1500,    10640,   0x007E, 0,  24, 0x0000)
    DeclActor(4294865646, 0,       2470,    1000,    4294863226, 1500,    2980,    0x007E, 0,  6,  0x0000)

    ChipFrameInfo(980, 0)                                        # 0

    ScpFunction((
        "Function_0_3D4",          # 00, 0
        "Function_1_48C",          # 01, 1
        "Function_2_515",          # 02, 2
        "Function_3_74D",          # 03, 3
        "Function_4_7AC",          # 04, 4
        "Function_5_8D4",          # 05, 5
        "Function_6_A67",          # 06, 6
        "Function_7_A6B",          # 07, 7
        "Function_8_E78",          # 08, 8
        "Function_9_10DC",         # 09, 9
        "Function_10_12BA",        # 0A, 10
        "Function_11_134A",        # 0B, 11
        "Function_12_13D3",        # 0C, 12
        "Function_13_144B",        # 0D, 13
        "Function_14_14D5",        # 0E, 14
        "Function_15_1574",        # 0F, 15
        "Function_16_1682",        # 10, 16
        "Function_17_16F9",        # 11, 17
        "Function_18_176F",        # 12, 18
        "Function_19_1987",        # 13, 19
        "Function_20_1A77",        # 14, 20
        "Function_21_1C8E",        # 15, 21
        "Function_22_22BC",        # 16, 22
        "Function_23_24DD",        # 17, 23
        "Function_24_2CF1",        # 18, 24
        "Function_25_2CF5",        # 19, 25
        "Function_26_3024",        # 1A, 26
        "Function_27_3206",        # 1B, 27
        "Function_28_32B4",        # 1C, 28
        "Function_29_333C",        # 1D, 29
    ))


    def Function_0_3D4(): pass

    label("Function_0_3D4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_414"),
        (1, "loc_420"),
        (2, "loc_42C"),
        (3, "loc_438"),
        (4, "loc_444"),
        (5, "loc_450"),
        (6, "loc_45C"),
        (SWITCH_DEFAULT, "loc_468"),
    )


    label("loc_414")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_474")

    label("loc_420")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_474")

    label("loc_42C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_474")

    label("loc_438")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_474")

    label("loc_444")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_474")

    label("loc_450")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_474")

    label("loc_45C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_474")

    label("loc_468")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_474")

    label("loc_474")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_48B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_474")

    label("loc_48B")

    Return()

    # Function_0_3D4 end

    def Function_1_48C(): pass

    label("Function_1_48C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_514")
    OP_95(0xFE, -98090, 0, 5880, 2000, 0x0)
    OP_95(0xFE, -98090, 0, 12710, 2000, 0x0)
    OP_95(0xFE, -92260, 0, 12710, 2000, 0x0)
    OP_95(0xFE, -92260, 0, 15180, 2000, 0x0)
    OP_95(0xFE, -101100, 0, 15180, 2000, 0x0)
    OP_95(0xFE, -101100, 0, 5880, 2000, 0x0)
    Jump("Function_1_48C")

    label("loc_514")

    Return()

    # Function_1_48C end

    def Function_2_515(): pass

    label("Function_2_515")

    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrChipByIndex(0xE, 0x6)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    SetChrChipByIndex(0x10, 0x8)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    SetChrChipByIndex(0x11, 0x9)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    SetChrChipByIndex(0x12, 0xD)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    SetChrChipByIndex(0x13, 0x13)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_5CD")
    Jump("loc_74C")

    label("loc_5CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_5DB")
    Jump("loc_74C")

    label("loc_5DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_664")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x15, 1590, 0, 8900, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61F")
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -1050, 0, 2180, 0)
    Jump("loc_655")

    label("loc_61F")

    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, -1530, 0, 2530, 90)
    SetChrFlags(0x1B, 0x10)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -540, 0, 2530, 270)
    SetChrFlags(0x1A, 0x10)

    label("loc_655")

    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_74C")

    label("loc_664")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_6F4")
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    SetChrSubChip(0xA, 0x2)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -103000, 120, 10930, 225)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x15, -1530, 0, 2530, 90)
    SetChrFlags(0x15, 0x10)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -540, 0, 2530, 270)
    SetChrFlags(0x1A, 0x10)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_74C")

    label("loc_6F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_74C")
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x10)
    SetChrPos(0x10, -96120, 120, 20890, 225)
    SetChrPos(0x15, -8189, 0, 8640, 180)
    SetChrFlags(0x15, 0x10)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x10)

    label("loc_74C")

    Return()

    # Function_2_515 end

    def Function_3_74D(): pass

    label("Function_3_74D")

    SetMapObjFrame(0xFF, "t1040_sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "t1040_sky_y", 0x0, 0x1)
    SetMapObjFrame(0xFF, "t1040_sky01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "t1040_sky01_y", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7AB")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7AB")

    Return()

    # Function_3_74D end

    def Function_4_7AC(): pass

    label("Function_4_7AC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_7BD")
    Jump("loc_8D0")

    label("loc_7BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_7CB")
    Jump("loc_8D0")

    label("loc_7CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_7D9")
    Jump("loc_8D0")

    label("loc_7D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_7E7")
    Jump("loc_8D0")

    label("loc_7E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_8AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_802")
    Call(0, 5)
    Jump("loc_8A6")

    label("loc_802")


    ChrTalk(
        0x12,
        (
            "#10304FHehe. As you can see, I was\x01",
            "caught by one of the club's\x01",
            "regulars.\x02\x03",
            "#10300FWell, I intend to cut things\x01",
            "off early so as not to be\x01",
            "late, so not to worry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A6")

    Jump("loc_8D0")

    label("loc_8AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_8B9")
    Jump("loc_8D0")

    label("loc_8B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_8C7")
    Jump("loc_8D0")

    label("loc_8C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_8D0")

    label("loc_8D0")

    TalkEnd(0xFE)
    Return()

    # Function_4_7AC end

    def Function_5_8D4(): pass

    label("Function_5_8D4")


    ChrTalk(
        0xA,
        (
            "Hehe. But even so, what\x01",
            "a coincidence to see you\x01",
            "here, Wazy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Although I could've kept\x01",
            "you company as much as you\x01",
            "like if you had called me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#10304FHehe. I'm here with\x01",
            "friends today, you see.\x02\x03",
            "#10302FI am sorry, but I have\x01",
            "plans later. Can we\x01",
            "finish this quickly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Ahh, that cold side of\x01",
            "your is dreamy too㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(I-Is this the kind of\x01",
            "thing that hosts do...?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    ClearChrFlags(0x12, 0x10)
    ClearChrFlags(0xA, 0x10)
    Return()

    # Function_5_8D4 end

    def Function_6_A67(): pass

    label("Function_6_A67")

    Call(0, 7)
    Return()

    # Function_6_A67 end

    def Function_7_A6B(): pass

    label("Function_7_A6B")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A78")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E74")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ACA")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_ACA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AEA")
    OP_AF(0x66)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E6F")

    label("loc_AEA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AFE")
    Jump("loc_E6F")

    label("loc_AFE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E6F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_B25")
    Jump("loc_E6F")

    label("loc_B25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_CE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C2C")

    ChrTalk(
        0x8,
        (
            "This restaurant's name\x01",
            ""Fortuna" means\x01",
            ""Fortune".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We give our customers service of\x01",
            "the highest level to let them\x01",
            "enjoy a truly fortunate meal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you have any comments in\x01",
            "particular, please don't\x01",
            "hesitate to let us know.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CDB")

    label("loc_C2C")


    ChrTalk(
        0x8,
        (
            "We give our customers service\x01",
            "of the highest level to let\x01",
            "them enjoy a fortunate meal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you have any comments in\x01",
            "particular, please don't\x01",
            "hesitate to let us know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CDB")

    Jump("loc_E6F")

    label("loc_CE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_E6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC7")

    ChrTalk(
        0x8,
        (
            "Welcome to Fortuna\x01",
            "restaurant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In this establishment you can enjoy\x01",
            "supreme dishes prepared with the finest\x01",
            "ingredients in a top-class location.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please enjoy a refined\x01",
            "and fortunate time...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E6F")

    label("loc_DC7")


    ChrTalk(
        0x8,
        (
            "In this establishment you can enjoy\x01",
            "supreme dishes prepared with the finest\x01",
            "ingredients in a top-class location.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please enjoy a refined\x01",
            "and fortunate time...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E6F")

    Jump("loc_A78")

    label("loc_E74")

    TalkEnd(0x8)
    Return()

    # Function_7_A6B end

    def Function_8_E78(): pass

    label("Function_8_E78")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_E89")
    Jump("loc_10D8")

    label("loc_E89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_F35")

    ChrTalk(
        0xFE,
        (
            "They've installed a new\x01",
            "attraction at the theme\x01",
            "park, haven't they.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rumor has it that it's a\x01",
            "scaaary one... I wonder what\x01",
            "kind of attraction it is.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10D8")

    label("loc_F35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_10D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1049")

    ChrTalk(
        0xFE,
        (
            "The recently opened Lake Beach\x01",
            "seems to be very popular among\x01",
            "people regardless of age and sex.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The hot days will go on and on and\x01",
            "it seems more customers will visit\x01",
            "Michelam than usual this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. I'd like to go\x01",
            "there too, once.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_10D8")

    label("loc_1049")


    ChrTalk(
        0xFE,
        (
            "The recently opened Lake Beach\x01",
            "seems to be very popular among\x01",
            "people regardless of age and sex.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. I'd like to go\x01",
            "there too, once.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10D8")

    TalkEnd(0xFE)
    Return()

    # Function_8_E78 end

    def Function_9_10DC(): pass

    label("Function_9_10DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_10ED")
    Jump("loc_12B6")

    label("loc_10ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_121D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A1")

    ChrTalk(
        0xFE,
        "Aah, Wazy left.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On the other hand, if I went\x01",
            "back home, I'd have to look\x01",
            "after my boring husband...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'll drink alone\x01",
            "for a while.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1218")

    label("loc_11A1")


    ChrTalk(
        0xFE,
        "Aah, Wazy left.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm not good at taking care of\x01",
            "my husband at home so I believe\x01",
            "I'll drink alone for a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1218")

    Jump("loc_12B6")

    label("loc_121D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_12AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1240")
    Call(0, 5)
    TalkEnd(0xFE)
    SetChrSubChip(0xA, 0x2)
    Return()

    label("loc_1240")


    ChrTalk(
        0xFE,
        (
            "Although Wazy is a host,\x01",
            "sometimes he's cold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...That side of him is\x01",
            "dreamy, though㈱\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    SetChrSubChip(0xA, 0x2)
    Return()

    label("loc_12AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_12B6")

    label("loc_12B6")

    TalkEnd(0xFE)
    Return()

    # Function_9_10DC end

    def Function_10_12BA(): pass

    label("Function_10_12BA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_12CB")
    Jump("loc_1346")

    label("loc_12CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_12D9")
    Jump("loc_1346")

    label("loc_12D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1346")

    ChrTalk(
        0xFE,
        (
            "I'm having breakfast a\x01",
            "little late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hoh hoh ho, maybe it's\x01",
            "too luxurious for the\x01",
            "morning.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1346")

    TalkEnd(0xFE)
    Return()

    # Function_10_12BA end

    def Function_11_134A(): pass

    label("Function_11_134A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_135B")
    Jump("loc_13CF")

    label("loc_135B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1369")
    Jump("loc_13CF")

    label("loc_1369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_13CF")

    ChrTalk(
        0xFE,
        (
            "Hmmm, what should I\x01",
            "have...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's still hot, so\x01",
            "something refreshing\x01",
            "might be nice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13CF")

    TalkEnd(0xFE)
    Return()

    # Function_11_134A end

    def Function_12_13D3(): pass

    label("Function_12_13D3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_13E4")
    Jump("loc_1447")

    label("loc_13E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_13F2")
    Jump("loc_1447")

    label("loc_13F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1447")

    ChrTalk(
        0xFE,
        "(*clatter clatter*)...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Delicious, *munch\x01",
            "munch*... *chew chew*...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1447")

    TalkEnd(0xFE)
    Return()

    # Function_12_13D3 end

    def Function_13_144B(): pass

    label("Function_13_144B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_145C")
    Jump("loc_14D1")

    label("loc_145C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_14C8")

    ChrTalk(
        0xFE,
        (
            "Oh, it seems the\x01",
            "reservation is only\x01",
            "valid this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Should we go after\x01",
            "eating?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D1")

    label("loc_14C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_14D1")

    label("loc_14D1")

    TalkEnd(0xFE)
    Return()

    # Function_13_144B end

    def Function_14_14D5(): pass

    label("Function_14_14D5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_14E6")
    Jump("loc_1570")

    label("loc_14E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1567")

    ChrTalk(
        0xFE,
        (
            "Haha, how is it? The\x01",
            "store I've chosen is\x01",
            "quite something, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Savor this taste to your\x01",
            "heart's content.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1570")

    label("loc_1567")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1570")

    label("loc_1570")

    TalkEnd(0xFE)
    Return()

    # Function_14_14D5 end

    def Function_15_1574(): pass

    label("Function_15_1574")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1585")
    Jump("loc_167E")

    label("loc_1585")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_15FA")

    ChrTalk(
        0xFE,
        (
            "(This dish tastes pretty\x01",
            "good, but...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(Hmm. I guess I chose\x01",
            "the wrong person to come\x01",
            "with.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_167E")

    label("loc_15FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_167E")

    ChrTalk(
        0xFE,
        (
            "Wait, wait a moment\x01",
            "father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Your table manners are too awful\x01",
            "for this sort of establishment.\x01",
            "Pay more attention!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_167E")

    TalkEnd(0xFE)
    Return()

    # Function_15_1574 end

    def Function_16_1682(): pass

    label("Function_16_1682")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1693")
    Jump("loc_16F5")

    label("loc_1693")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_16EC")

    ChrTalk(
        0xFE,
        "I'm feeling hot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Say mom. Let's go to\x01",
            "Lake Beach this\x01",
            "afternoon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16F5")

    label("loc_16EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_16F5")

    label("loc_16F5")

    TalkEnd(0xFE)
    Return()

    # Function_16_1682 end

    def Function_17_16F9(): pass

    label("Function_17_16F9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_170A")
    Jump("loc_176B")

    label("loc_170A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1718")
    Jump("loc_176B")

    label("loc_1718")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1726")
    Jump("loc_176B")

    label("loc_1726")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1746")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_173E")
    Jump("loc_1741")

    label("loc_173E")

    Call(0, 20)

    label("loc_1741")

    Jump("loc_176B")

    label("loc_1746")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1754")
    Jump("loc_176B")

    label("loc_1754")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_1762")
    Jump("loc_176B")

    label("loc_1762")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_176B")

    label("loc_176B")

    TalkEnd(0xFE)
    Return()

    # Function_17_16F9 end

    def Function_18_176F(): pass

    label("Function_18_176F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_1780")
    Jump("loc_1983")

    label("loc_1780")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_178E")
    Jump("loc_1983")

    label("loc_178E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_179C")
    Jump("loc_1983")

    label("loc_179C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_18BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_183A")

    ChrTalk(
        0x1A,
        (
            "#01703FHmm. The clothes in this\x01",
            "store aren't my style.\x02\x03",
            "#01702FI'd prefer it if they\x01",
            "were more luscious and\x01",
            "exotic.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_18B0")

    label("loc_183A")


    ChrTalk(
        0x1A,
        (
            "#01705FEven so, Rixia sure is\x01",
            "late.\x02\x03",
            "#01706FIf she doesn't come\x01",
            "quickly, we won't have\x01",
            "time to shop for clothes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18B0")

    Jump("loc_18B8")

    label("loc_18B5")

    Call(0, 20)

    label("loc_18B8")

    Jump("loc_1983")

    label("loc_18BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_196C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18D8")
    Call(0, 19)
    Jump("loc_1967")

    label("loc_18D8")


    ChrTalk(
        0x1A,
        (
            "#01705FHuh? Come to think of\x01",
            "it, I wonder why Rixia\x01",
            "isn't here yet.\x02\x03",
            "#01706FI'd like to make her\x01",
            "wear a clothes that are\x01",
            "a little sexier.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1967")

    Jump("loc_1983")

    label("loc_196C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_197A")
    Jump("loc_1983")

    label("loc_197A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1983")

    label("loc_1983")

    TalkEnd(0xFE)
    Return()

    # Function_18_176F end

    def Function_19_1987(): pass

    label("Function_19_1987")

    OP_4B(0x1A, 0xFF)
    OP_4B(0x15, 0xFF)

    ChrTalk(
        0x15,
        (
            "I see, in that case,\x01",
            "what about these dresses\x01",
            "over here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#01703FHmm, let's see...\x01",
            "Personally, I'd like\x01",
            "something a little showier.\x02\x03",
            "#01702FAh, could you show me some\x01",
            "hats too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Yes, right this way\x01",
            "please.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    ClearChrFlags(0x1A, 0x10)
    OP_4C(0x1A, 0xFF)
    Return()

    # Function_19_1987 end

    def Function_20_1A77(): pass

    label("Function_20_1A77")

    OP_4B(0x1A, 0xFF)
    OP_4B(0x1B, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C00")

    ChrTalk(
        0x1A,
        (
            "#01700FI found this dress earlier.\x01",
            "It's got a cutout on the\x01",
            "breast... Sexy, isn't it?\x02\x03",
            "#01709FWhat do you say, Rixia?\x01",
            "I'll buy it for you, so\x01",
            "won't you try it on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#01805FH-Huuuh!? I have to wear\x01",
            "this!?\x02\x03",
            "#01809FA-As you might expect\x01",
            "it'll be embarrassing\x01",
            "and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#01709FIt's fine, it's fine. Someone\x01",
            "like you will be able pull it\x01",
            "off for sure, trust me!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_1C85")

    label("loc_1C00")


    ChrTalk(
        0x1A,
        (
            "#01709FThat's enough, just\x01",
            "believe me already and\x01",
            "try it on.\x02\x03",
            "#01701FOr rather, I want to see\x01",
            "you in it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#01806FE-Eeek...!\x02",
    )

    CloseMessageWindow()

    label("loc_1C85")

    OP_4C(0x1A, 0xFF)
    OP_4C(0x1B, 0xFF)
    Return()

    # Function_20_1A77 end

    def Function_21_1C8E(): pass

    label("Function_21_1C8E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_1C9F")
    Jump("loc_22B8")

    label("loc_1C9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1CAD")
    Jump("loc_22B8")

    label("loc_1CAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1CBB")
    Jump("loc_22B8")

    label("loc_1CBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_2014")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F24")

    ChrTalk(
        0x19,
        (
            "#05900FI heard about it from Elie\x01",
            "earlier. She said you bought a\x01",
            "suit in this boutique, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FYeah. Although that was a\x01",
            "while ago... Is there\x01",
            "something wrong with that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#05906FOoh, your big sister wanted\x01",
            "to choose the suit for your\x01",
            "wedding ceremony, and yet...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01105FHuh, Lloyd, are you\x01",
            "going to marry?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FN-No no, I won't!\x02\x03",
            "#00006FAnd it was chosen for an\x01",
            "investigation in the\x01",
            "first place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#05905FMy, is that so? That's a\x01",
            "pity, in its own way.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F(Cecil... Aren't you\x01",
            "enjoying my reaction a\x01",
            "little too much?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_200F")

    label("loc_1F24")


    ChrTalk(
        0x19,
        (
            "#05902FHaha. By all means, please\x01",
            "let me know when it's time\x01",
            "for your wedding.\x02\x03",
            "#05901FYour big sister will the\x01",
            "locations of the ceremony\x01",
            "and the honeymoon for you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FIt's too much of a leap\x01",
            "from talking about a\x01",
            "suit...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_200F")

    Jump("loc_22B8")

    label("loc_2014")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_22A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2209")

    ChrTalk(
        0x19,
        "#05903F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FCecil, is something\x01",
            "wrong?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x19,
        (
            "#05902F...Ah, Lloyd.\x02\x03",
            "#05909FNo, it's just that it's my first time\x01",
            "going to the theme park and I was\x01",
            "wondering what kind of place it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah, it's my first time too.\x02\x03",
            "#00000FBased on what I heard from Randy\x01",
            "and Noｱl, who have already been, I\x01",
            "think we can look forward to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#05909FHaha, right. Since it's a\x01",
            "rare chance, we have to have\x01",
            "them show us lots of things.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_229C")

    label("loc_2209")


    ChrTalk(
        0x19,
        (
            "#05904FYes, I'll have to enjoy\x01",
            "today to the fullest.\x02\x03",
            "#05902FIt's my first time here too,\x01",
            "so I guess I'll have Randy\x01",
            "and Noｱl show me around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_229C")

    Jump("loc_22B8")

    label("loc_22A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_22AF")
    Jump("loc_22B8")

    label("loc_22AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_22B8")

    label("loc_22B8")

    TalkEnd(0xFE)
    Return()

    # Function_21_1C8E end

    def Function_22_22BC(): pass

    label("Function_22_22BC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_22CD")
    Jump("loc_24D9")

    label("loc_22CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_22DB")
    Jump("loc_24D9")

    label("loc_22DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_22E9")
    Jump("loc_24D9")

    label("loc_22E9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_22F9")
    Jump("loc_24D9")

    label("loc_22F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_2307")
    Jump("loc_24D9")

    label("loc_2307")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_24C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2461")

    ChrTalk(
        0x18,
        (
            "#06405FAh, Lloyd! Please, look\x01",
            "here for a moment.\x02\x03",
            "#06409FWhat do think about this\x01",
            "dress? How do I look?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, you look pretty\x01",
            "good in that, don't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#06402FOoh, it's Mr. Lloyd's\x01",
            "seal of approval! Then,\x01",
            "I'll buy this and...\x02\x03",
            "#06409FHaha, I guess I'll\x01",
            "choose a dress for Noｱl\x01",
            "of my own accord...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_24BD")

    label("loc_2461")


    ChrTalk(
        0x18,
        (
            "#06409FThere's lots of nice-\x01",
            "looking clothes here!\x02\x03",
            "#06406FI wish Noｱl had come\x01",
            "too...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24BD")

    Jump("loc_24D9")

    label("loc_24C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_24D0")
    Jump("loc_24D9")

    label("loc_24D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_24D9")

    label("loc_24D9")

    TalkEnd(0xFE)
    Return()

    # Function_22_22BC end

    def Function_23_24DD(): pass

    label("Function_23_24DD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_24EE")
    Jump("loc_2CED")

    label("loc_24EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_24FC")
    Jump("loc_2CED")

    label("loc_24FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_250A")
    Jump("loc_2CED")

    label("loc_250A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_2795")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2700")

    ChrTalk(
        0x17,
        (
            "#00113F*sigh*. I had prepared myself for this\x01",
            "to a certain extent, but who would've\x01",
            "thought I'd have gone through that...\x02\x03",
            "#00111F...Say, Lloyd. You didn't see me,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FY-Yeah. Don't worry, I\x01",
            "didn't.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#00106F*sigh*, fine then.\x02\x03",
            "#00112F...If you had, then I\x01",
            "would have made you take\x01",
            "responsibility.\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x101,
        "#00011F#4SWHAT!?#3S\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#00104F...Just kidding.\x02\x03",
            "#00109F*giggle*, teasing you is\x01",
            "really worth it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FG-Give me a break...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2790")

    label("loc_2700")


    ChrTalk(
        0x17,
        (
            "#00113FW-Well, I was prepared\x01",
            "for it to a certain\x01",
            "extent...\x02\x03",
            "#00102FFor now I'm glad we drove\x01",
            "away the monsters...\x01",
            "Let's leave it at that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2790")

    Jump("loc_2CED")

    label("loc_2795")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_299F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_291F")

    ChrTalk(
        0x17,
        (
            "#00105FAh, KeA.\x02\x03",
            "#00102FSay, what do you think\x01",
            "about this dress? I think\x01",
            "it's a perfect for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01110FWah, how pretty!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FA d-dress...? Is there\x01",
            "some special occasion?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#00109F*giggle*, even if there\x01",
            "isn't, what's wrong with\x01",
            "it?\x02\x03",
            "#00104FWe've got to have KeA\x01",
            "try on many different\x01",
            "clothes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(Hmm, looks like they're\x01",
            "having fun...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_299A")

    label("loc_291F")


    ChrTalk(
        0x17,
        (
            "#00102F*giggle*, I'll keep\x01",
            "looking here for a while\x01",
            "longer.\x02\x03",
            "#00109FI have to find lots of\x01",
            "different clothes for\x01",
            "KeA.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_299A")

    Jump("loc_2CED")

    label("loc_299F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_2CC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C0E")

    ChrTalk(
        0x17,
        (
            "#00103FAs I thought, this boutique\x01",
            "seems to have an assortment of\x01",
            "good quality clothes.\x02\x03",
            "#00100FThe silk of this dress too, and\x01",
            "the Bareahard fur over there is\x01",
            "very nice to the touch...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FBareahard... Isn't that the\x01",
            "name of a city in the\x01",
            "northeast part of the Empire?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#00100FYes, it's famous for its\x01",
            "high quality furs.\x02\x03",
            "#00104FWhen attending social\x01",
            "parties, you often notice\x01",
            "the women wearing them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWow, you really know\x01",
            "your stuff.\x02\x03",
            "#00003FAlthough I think fur\x01",
            "would be sweltering in\x01",
            "this season...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#00111F...You say pretty blunt\x01",
            "things sometimes, don't\x01",
            "you?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2CC3")

    label("loc_2C0E")


    ChrTalk(
        0x17,
        (
            "#00104FFor social occasions, what you wear\x01",
            "is a kind of status.\x02\x03",
            "#00100FPersonally, I feel that if you like\x01",
            "the style, there's no need to concern\x01",
            "yourself with the brand name.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CC3")

    Jump("loc_2CED")

    label("loc_2CC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_2CD6")
    Jump("loc_2CED")

    label("loc_2CD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_2CE4")
    Jump("loc_2CED")

    label("loc_2CE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_2CED")

    label("loc_2CED")

    TalkEnd(0xFE)
    Return()

    # Function_23_24DD end

    def Function_24_2CF1(): pass

    label("Function_24_2CF1")

    Call(0, 25)
    Return()

    # Function_24_2CF1 end

    def Function_25_2CF5(): pass

    label("Function_25_2CF5")

    TalkBegin(0x14)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D02")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3020")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D54")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2D54")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D74")
    OP_AF(0x69)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_301B")

    label("loc_2D74")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D88")
    Jump("loc_301B")

    label("loc_2D88")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_301B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_2DAF")
    Jump("loc_301B")

    label("loc_2DAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_2EA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E48")

    ChrTalk(
        0x14,
        (
            "*sigh*, that Drona,\x01",
            "being so festive...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "I know how she feels, but\x01",
            "I wish she'd hold back in\x01",
            "front of the customers.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2E9C")

    label("loc_2E48")


    ChrTalk(
        0x14,
        (
            "*sigh*, that Drona. I wish\x01",
            "she wouldn't be so merry\x01",
            "in front of the customers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E9C")

    Jump("loc_301B")

    label("loc_2EA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_2F2F")

    ChrTalk(
        0x14,
        (
            "A great number of female\x01",
            "customers have arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Haha. You end up letting\x01",
            "out a sigh with this\x01",
            "many beautiful ladies.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_301B")

    label("loc_2F2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_301B")

    ChrTalk(
        0x14,
        (
            "With the opening of Lake Beach,\x01",
            "we at boutique Colserica have\x01",
            "started dealing in swimsuits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Since we deal in fashionable swimsuits\x01",
            "imported from the continent's coastal areas,\x01",
            "by all means, please have a look around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_301B")

    Jump("loc_2D02")

    label("loc_3020")

    TalkEnd(0x14)
    Return()

    # Function_25_2CF5 end

    def Function_26_3024(): pass

    label("Function_26_3024")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_3035")
    Jump("loc_3202")

    label("loc_3035")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_3124")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30B2")

    ChrTalk(
        0xFE,
        (
            "I received an autograph\x01",
            "from that Ilya Platiｲre.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aah, it'll be the\x01",
            "treasure of my life!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_311F")

    label("loc_30B2")


    ChrTalk(
        0xFE,
        (
            "I can't believe I met\x01",
            "Ilya in a place like\x01",
            "this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This autograph will be\x01",
            "the treasure of my life!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_311F")

    Jump("loc_3202")

    label("loc_3124")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_3187")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_313F")
    Call(0, 19)
    Jump("loc_3182")

    label("loc_313F")


    ChrTalk(
        0xFE,
        (
            "(...Oh? By the way, I\x01",
            "think I saw this\x01",
            "customer somewhere...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3182")

    Jump("loc_3202")

    label("loc_3187")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_3202")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31A2")
    Call(0, 27)
    Jump("loc_3202")

    label("loc_31A2")


    ChrTalk(
        0xFE,
        (
            "Uhuhu, it looks very\x01",
            "good on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think it brings out\x01",
            "your elegance greatly,\x01",
            "madam.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3202")

    TalkEnd(0xFE)
    Return()

    # Function_26_3024 end

    def Function_27_3206(): pass

    label("Function_27_3206")

    OP_4B(0x15, 0xFF)
    OP_4B(0x16, 0xFF)

    ChrTalk(
        0x15,
        (
            "Let's see, I think you'll be\x01",
            "even more elegant if we combine\x01",
            "it with this ribbon, madam...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "...Like this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Uhuhu, it looks very\x01",
            "good on you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    OP_4C(0x15, 0xFF)
    OP_4C(0x16, 0xFF)
    Return()

    # Function_27_3206 end

    def Function_28_32B4(): pass

    label("Function_28_32B4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_32C5")
    Jump("loc_3338")

    label("loc_32C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_32D3")
    Jump("loc_3338")

    label("loc_32D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_3338")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32EE")
    Call(0, 27)
    Jump("loc_3338")

    label("loc_32EE")


    ChrTalk(
        0xFE,
        (
            "Haha, you really know\x01",
            "your stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then, can I have this\x01",
            "outfit?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3338")

    TalkEnd(0xFE)
    Return()

    # Function_28_32B4 end

    def Function_29_333C(): pass

    label("Function_29_333C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3446")

    ChrTalk(
        0xFE,
        (
            "Michelam Health Resort...\x01",
            "It's my first time here\x01",
            "and it's great.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I lived here, I think I\x01",
            "could say goodbye to life with\x01",
            "that boring husband of mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After I've eaten, I must\x01",
            "immediately go have a look\x01",
            "at the residential area.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_34F4")

    label("loc_3446")


    ChrTalk(
        0xFE,
        (
            "If I lived here, I think I\x01",
            "could say goodbye to life with\x01",
            "that boring husband of mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After I've eaten, I must\x01",
            "immediately go have a look\x01",
            "at the residential area.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34F4")

    TalkEnd(0xFE)
    Return()

    # Function_29_333C end

    SaveToFile()

Try(main)
