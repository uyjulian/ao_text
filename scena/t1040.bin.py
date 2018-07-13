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
        "Function_5_8E3",          # 05, 5
        "Function_6_A7B",          # 06, 6
        "Function_7_A7F",          # 07, 7
        "Function_8_E84",          # 08, 8
        "Function_9_1109",         # 09, 9
        "Function_10_12FE",        # 0A, 10
        "Function_11_138E",        # 0B, 11
        "Function_12_142B",        # 0C, 12
        "Function_13_14A3",        # 0D, 13
        "Function_14_152F",        # 0E, 14
        "Function_15_15CF",        # 0F, 15
        "Function_16_16D3",        # 10, 16
        "Function_17_1756",        # 11, 17
        "Function_18_17CC",        # 12, 18
        "Function_19_19DE",        # 13, 19
        "Function_20_1AC8",        # 14, 20
        "Function_21_1CD8",        # 15, 21
        "Function_22_2330",        # 16, 22
        "Function_23_2550",        # 17, 23
        "Function_24_2D69",        # 18, 24
        "Function_25_2D6D",        # 19, 25
        "Function_26_30AF",        # 1A, 26
        "Function_27_329E",        # 1B, 27
        "Function_28_3359",        # 1C, 28
        "Function_29_33EE",        # 1D, 29
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
    Jump("loc_8DF")

    label("loc_7BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_7CB")
    Jump("loc_8DF")

    label("loc_7CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_7D9")
    Jump("loc_8DF")

    label("loc_7D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_7E7")
    Jump("loc_8DF")

    label("loc_7E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_8BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_802")
    Call(0, 5)
    Jump("loc_8B5")

    label("loc_802")


    ChrTalk(
        0x12,
        (
            "#10304FHu hu, as you can see, I was\x01",
            "caught by one of the club's regulars.\x02\x03",
            "#10300FWell, I intend to cut short quickly\x01",
            "to not be late at the meeting,\x01",
            "so don't worry about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B5")

    Jump("loc_8DF")

    label("loc_8BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_8C8")
    Jump("loc_8DF")

    label("loc_8C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_8D6")
    Jump("loc_8DF")

    label("loc_8D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_8DF")

    label("loc_8DF")

    TalkEnd(0xFE)
    Return()

    # Function_4_7AC end

    def Function_5_8E3(): pass

    label("Function_5_8E3")


    ChrTalk(
        0xA,
        (
            "Uh uh, even so, what a coincidence\x01",
            "to see Wazy coming here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Although I could've made you company as\x01",
            "much as you want if you had called at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#10304FHu hu, you see, today I'm here with friends.\x02\x03",
            "#10302FI am sorry, but because I have plans\x01",
            "for later, can we finish this quickly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Ahn, such cold side of you is dreamy too㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(I-Is she really\x01",
            "fine with that...?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    ClearChrFlags(0x12, 0x10)
    ClearChrFlags(0xA, 0x10)
    Return()

    # Function_5_8E3 end

    def Function_6_A7B(): pass

    label("Function_6_A7B")

    Call(0, 7)
    Return()

    # Function_6_A7B end

    def Function_7_A7F(): pass

    label("Function_7_A7F")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A8C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E80")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ADC")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_ADC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AFC")
    OP_AF(0x66)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E7B")

    label("loc_AFC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B10")
    Jump("loc_E7B")

    label("loc_B10")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E7B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_B37")
    Jump("loc_E7B")

    label("loc_B37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_CF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C3E")

    ChrTalk(
        0x8,
        (
            "This name's restaurant,\x01",
            ""Fortuna" means "Fortune".\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We are giving the highest of service\x01",
            "to the customers to have them\x01",
            "enjoy a truly fortunate meal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you have any particular comments,\x01",
            "please tell us without hesitation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CEB")

    label("loc_C3E")


    ChrTalk(
        0x8,
        (
            "We are giving the highest of service\x01",
            "to the customers to have them\x01",
            "enjoy a fortunate meal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you have any particular comments,\x01",
            "please tell us without hesitation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CEB")

    Jump("loc_E7B")

    label("loc_CF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_E7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD6")

    ChrTalk(
        0x8,
        "Welcome to restaurant "Fortuna".\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In this establishment you can have\x01",
            "supreme dishes prepared with the\x01",
            "best ingredients on a top class location.\x02",
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
    Jump("loc_E7B")

    label("loc_DD6")


    ChrTalk(
        0x8,
        (
            "In this establishment you can have\x01",
            "supreme dishes prepared with the\x01",
            "best ingredients on a top class location.\x02",
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

    label("loc_E7B")

    Jump("loc_A8C")

    label("loc_E80")

    TalkEnd(0x8)
    Return()

    # Function_7_A7F end

    def Function_8_E84(): pass

    label("Function_8_E84")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_E95")
    Jump("loc_1105")

    label("loc_E95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_F3E")

    ChrTalk(
        0xFE,
        (
            "Lately, a new attraction\x01",
            "was installed at the\x01",
            "theme park, they say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rumors go that it's a scaaary one...\x01",
            "I wonder what kind of attraction is it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1105")

    label("loc_F3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1105")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1075")

    ChrTalk(
        0xFE,
        (
            "The recently opened Lake Beach \x01",
            "seems to be very popular among\x01",
            "people regardless of age and sex.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The hot days will go on and on and it seems\x01",
            "that even the customers visiting Michelam will\x01",
            "be increasing compared to the average year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uuhm, I'd like to go there once too.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1105")

    label("loc_1075")


    ChrTalk(
        0xFE,
        (
            "The recently opened Lake Beach \x01",
            "seems to be very popular among\x01",
            "people regardless of age and sex.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uuhm, I'd like to go there once too.\x02",
    )

    CloseMessageWindow()

    label("loc_1105")

    TalkEnd(0xFE)
    Return()

    # Function_8_E84 end

    def Function_9_1109(): pass

    label("Function_9_1109")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_111A")
    Jump("loc_12FA")

    label("loc_111A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_125A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11D9")

    ChrTalk(
        0xFE,
        "Aah, Wazy went away.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On the other hand, even if I\x01",
            "went back home, I'd have to\x01",
            "look after my boring husband...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I believe I'll drink alone fo a while.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1255")

    label("loc_11D9")


    ChrTalk(
        0xFE,
        "Aah, Wazy went away.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm not good at taking care of my husband at\x01",
            "home so I believe I'll drink alone for a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1255")

    Jump("loc_12FA")

    label("loc_125A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_12F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_127D")
    Call(0, 5)
    TalkEnd(0xFE)
    SetChrSubChip(0xA, 0x2)
    Return()

    label("loc_127D")


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
        "...Well, that side of hime is dreamy, though㈱\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    SetChrSubChip(0xA, 0x2)
    Return()

    label("loc_12F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_12FA")

    label("loc_12FA")

    TalkEnd(0xFE)
    Return()

    # Function_9_1109 end

    def Function_10_12FE(): pass

    label("Function_10_12FE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_130F")
    Jump("loc_138A")

    label("loc_130F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_131D")
    Jump("loc_138A")

    label("loc_131D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_138A")

    ChrTalk(
        0xFE,
        "I'm having breakfast a little late.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hoh hoh ho, maybe it's too\x01",
            "luxurious for the morning.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_138A")

    TalkEnd(0xFE)
    Return()

    # Function_10_12FE end

    def Function_11_138E(): pass

    label("Function_11_138E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_139F")
    Jump("loc_1427")

    label("loc_139F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_13AD")
    Jump("loc_1427")

    label("loc_13AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1427")

    ChrTalk(
        0xFE,
        "Uuhm, what could I have...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's still hot, so having something that\x01",
            "refreshes me could be nice anyway.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1427")

    TalkEnd(0xFE)
    Return()

    # Function_11_138E end

    def Function_12_142B(): pass

    label("Function_12_142B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_143C")
    Jump("loc_149F")

    label("loc_143C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_144A")
    Jump("loc_149F")

    label("loc_144A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_149F")

    ChrTalk(
        0xFE,
        "(*clatter clatter*)...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Delicious, *munch munch*...\x01",
            "*chew chew*...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_149F")

    TalkEnd(0xFE)
    Return()

    # Function_12_142B end

    def Function_13_14A3(): pass

    label("Function_13_14A3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_14B4")
    Jump("loc_152B")

    label("loc_14B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1522")

    ChrTalk(
        0xFE,
        (
            "Oh, it seems the reservation\x01",
            "is only valid in the morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Should we go after eating?\x02",
    )

    CloseMessageWindow()
    Jump("loc_152B")

    label("loc_1522")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_152B")

    label("loc_152B")

    TalkEnd(0xFE)
    Return()

    # Function_13_14A3 end

    def Function_14_152F(): pass

    label("Function_14_152F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1540")
    Jump("loc_15CB")

    label("loc_1540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_15C2")

    ChrTalk(
        0xFE,
        (
            "Ha ha, how is it?\x01",
            "The store I've chosen is quite something, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Savor this taste to your heart's content.\x02",
    )

    CloseMessageWindow()
    Jump("loc_15CB")

    label("loc_15C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_15CB")

    label("loc_15CB")

    TalkEnd(0xFE)
    Return()

    # Function_14_152F end

    def Function_15_15CF(): pass

    label("Function_15_15CF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_15E0")
    Jump("loc_16CF")

    label("loc_15E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_165B")

    ChrTalk(
        0xFE,
        (
            "(The dishes' taste is\x01",
            "pretty good, but...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(Uhhm, I chose the wrong\x01",
            "person to come with, I guess.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16CF")

    label("loc_165B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_16CF")

    ChrTalk(
        0xFE,
        "Wait, wait a moment father.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mind your table manners in this\x01",
            "establishment, because you're noisy!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16CF")

    TalkEnd(0xFE)
    Return()

    # Function_15_15CF end

    def Function_16_16D3(): pass

    label("Function_16_16D3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_16E4")
    Jump("loc_1752")

    label("loc_16E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1749")

    ChrTalk(
        0xFE,
        "I've started to feel hot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Say mother, let's go to the\x01",
            "lake beach after noon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1752")

    label("loc_1749")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1752")

    label("loc_1752")

    TalkEnd(0xFE)
    Return()

    # Function_16_16D3 end

    def Function_17_1756(): pass

    label("Function_17_1756")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_1767")
    Jump("loc_17C8")

    label("loc_1767")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1775")
    Jump("loc_17C8")

    label("loc_1775")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1783")
    Jump("loc_17C8")

    label("loc_1783")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_17A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_179B")
    Jump("loc_179E")

    label("loc_179B")

    Call(0, 20)

    label("loc_179E")

    Jump("loc_17C8")

    label("loc_17A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_17B1")
    Jump("loc_17C8")

    label("loc_17B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_17BF")
    Jump("loc_17C8")

    label("loc_17BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_17C8")

    label("loc_17C8")

    TalkEnd(0xFE)
    Return()

    # Function_17_1756 end

    def Function_18_17CC(): pass

    label("Function_18_17CC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_17DD")
    Jump("loc_19DA")

    label("loc_17DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_17EB")
    Jump("loc_19DA")

    label("loc_17EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_17F9")
    Jump("loc_19DA")

    label("loc_17F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1923")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_191B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1894")

    ChrTalk(
        0x1A,
        (
            "#01703FUuhm, the clothes of this\x01",
            "store do not suit me well.\x02\x03",
            "#01702FI'd like they were\x01",
            "more luscious\x01",
            "and exotic.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_1916")

    label("loc_1894")


    ChrTalk(
        0x1A,
        (
            "#01705FEven so, Rixia\x01",
            "sure is late.\x02\x03",
            "#01706FIf she doesn't come quickly,\x01",
            "our time for choosing clothes\x01",
            "for her will be over.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1916")

    Jump("loc_191E")

    label("loc_191B")

    Call(0, 20)

    label("loc_191E")

    Jump("loc_19DA")

    label("loc_1923")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_19C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_193E")
    Call(0, 19)
    Jump("loc_19BE")

    label("loc_193E")


    ChrTalk(
        0x1A,
        (
            "#01705FOh, by the way, I wonder\x01",
            "if Rixia isn't here yet?\x02\x03",
            "#01706FI'd like to make her\x01",
            "wear a little sexier\x01",
            "clothes to her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19BE")

    Jump("loc_19DA")

    label("loc_19C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_19D1")
    Jump("loc_19DA")

    label("loc_19D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_19DA")

    label("loc_19DA")

    TalkEnd(0xFE)
    Return()

    # Function_18_17CC end

    def Function_19_19DE(): pass

    label("Function_19_19DE")

    OP_4B(0x1A, 0xFF)
    OP_4B(0x15, 0xFF)

    ChrTalk(
        0x15,
        (
            "I see, in that case, what about\x01",
            "these dresses over here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#01703FHmm, let's see...\x01",
            "Personally, I'd like\x01",
            "something a little showier.\x02\x03",
            "#01702FAh, could you show me some hats too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Yes, this way please.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    ClearChrFlags(0x1A, 0x10)
    OP_4C(0x1A, 0xFF)
    Return()

    # Function_19_19DE end

    def Function_20_1AC8(): pass

    label("Function_20_1AC8")

    OP_4B(0x1A, 0xFF)
    OP_4B(0x1B, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C55")

    ChrTalk(
        0x1A,
        (
            "#01700FIt's a dress I found just before, it's got an\x01",
            "empty part on the breast...sexy, isn't it?\x02\x03",
            "#01709FWhat do you say, Rixia?\x01",
            "I'll buy it for you, so won't you try it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#01805FE-Eeh!?\x01",
            "I have to wear this!?\x02\x03",
            "#01809FA-As you expect it'll\x01",
            "be embarrassing and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#01709FIt's fine, fine, someone like you will be able\x01",
            "to charmingly wear it for sure, trust me!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_1CCF")

    label("loc_1C55")


    ChrTalk(
        0x1A,
        (
            "#01709FEnough now, \x01",
            "believe me and\x01",
            "just try it on.\x02\x03",
            "#01701FRather, I want to see you in that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#01806FE-Eeek...!\x02",
    )

    CloseMessageWindow()

    label("loc_1CCF")

    OP_4C(0x1A, 0xFF)
    OP_4C(0x1B, 0xFF)
    Return()

    # Function_20_1AC8 end

    def Function_21_1CD8(): pass

    label("Function_21_1CD8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_1CE9")
    Jump("loc_232C")

    label("loc_1CE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1CF7")
    Jump("loc_232C")

    label("loc_1CF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1D05")
    Jump("loc_232C")

    label("loc_1D05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_207F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F7F")

    ChrTalk(
        0x19,
        (
            "#05900FI heard about it from Miss Elie before,\x01",
            "she said you bought a suit in this\x01",
            "boutique, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FYeah, it was some time ago, though...\x01",
            "Is there something wrong with that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#05906FUuh, your big sister wanted\x01",
            "to choose the suit for your\x01",
            "wedding ceremony, and yet...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01105FHuh, Lloyd, are\x01",
            "you going to marry?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FN-No no, I won't!\x02\x03",
            "#00006FAnd in the first place, that was\x01",
            "something chosen for an investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#05905FMy, is that so?\x01",
            "That's a pity, in its own respect.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F(Sister Cecil...\x01",
            "Aren't you somehow enjoying my reaction?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_207A")

    label("loc_1F7F")


    ChrTalk(
        0x19,
        (
            "#05902FUh uh, by all means call me when it\x01",
            "will be time for your wedding ceremony.\x02\x03",
            "#05901FBig sister will chose for you\x01",
            "from the marriage place setting\x01",
            "to the honeymoon location!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FIt's too much of a leapt\x01",
            "from talking about a suit...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_207A")

    Jump("loc_232C")

    label("loc_207F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_2315")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2281")

    ChrTalk(
        0x19,
        "#05903F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FSister Cecil, is something wrong?\x02",
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x19,
        (
            "#05902F...Ah, Lloyd.\x02\x03",
            "#05909FNo, it's that it's my first time going\x01",
            "to a theme park and I was wondering \x01",
            "what kind of place is it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah, it's the first time for me too.\x02\x03",
            "#00000FMaybe you're looking forward to it\x01",
            "according to what we heard from \x01",
            "Randy and Noｱl who went to it before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#05909FUh uh, right.\x01",
            "Since it's a rare chance, we must\x01",
            "have them show us a lot of things.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_2310")

    label("loc_2281")


    ChrTalk(
        0x19,
        (
            "#05904FYes, I'll have to enjoy\x01",
            "today at my fullest.\x02\x03",
            "#05902FIt's my first time here too,\x01",
            "I guess I'll have Randy\x01",
            "and Noｱl show me around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2310")

    Jump("loc_232C")

    label("loc_2315")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_2323")
    Jump("loc_232C")

    label("loc_2323")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_232C")

    label("loc_232C")

    TalkEnd(0xFE)
    Return()

    # Function_21_1CD8 end

    def Function_22_2330(): pass

    label("Function_22_2330")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_2341")
    Jump("loc_254C")

    label("loc_2341")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_234F")
    Jump("loc_254C")

    label("loc_234F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_235D")
    Jump("loc_254C")

    label("loc_235D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_236D")
    Jump("loc_254C")

    label("loc_236D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_237B")
    Jump("loc_254C")

    label("loc_237B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_2535")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24D4")

    ChrTalk(
        0x18,
        (
            "#06405FAh, Mr. Lloyd!\x01",
            "Please, look here for a moment.\x02\x03",
            "#06409FWhat do you say about this dress?\x01",
            "Does it suit me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, I think it's quite good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#06402FOoh, it's Mr. Lloyd's seal of approval!\x01",
            "Then, I'll buy this and...\x02\x03",
            "#06409FUh uh, I guess I'll choose a dress\x01",
            "for big sis too on my own accord...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_2530")

    label("loc_24D4")


    ChrTalk(
        0x18,
        (
            "#06409FThere're plenty of nice-looking clothes!\x02\x03",
            "#06406FI wish big sis had come too...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2530")

    Jump("loc_254C")

    label("loc_2535")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_2543")
    Jump("loc_254C")

    label("loc_2543")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_254C")

    label("loc_254C")

    TalkEnd(0xFE)
    Return()

    # Function_22_2330 end

    def Function_23_2550(): pass

    label("Function_23_2550")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_2561")
    Jump("loc_2D65")

    label("loc_2561")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_256F")
    Jump("loc_2D65")

    label("loc_256F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_257D")
    Jump("loc_2D65")

    label("loc_257D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_2809")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_275C")

    ChrTalk(
        0x17,
        (
            "#00113F*haah*, I was a little prepared, but who\x01",
            "could've thought I'd went through that...\x02\x03",
            "#00111F...Say, Lloyd.\x01",
            "You really didn't see, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FY-Yeah.\x01",
            "Don't worry, I didn't.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#00106F*sigh*, fine then.\x02\x03",
            "#00112F...If you had seen then I would\x01",
            "have made you taken responsibility.\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x101,
        "#00011F#4SEH!?#3S\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#00104F...Just kidding.\x02\x03",
            "#00109F*giggle*, teasing you\x01",
            "is really worth it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FC-Cut me some slack...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2804")

    label("loc_275C")


    ChrTalk(
        0x17,
        (
            "#00113FW-Well, I was prepared to go through\x01",
            "such a thing to a certain extent...\x02\x03",
            "#00102FFor now I'm glad we could repel the\x01",
            "monsters...and let's leave it at that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2804")

    Jump("loc_2D65")

    label("loc_2809")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_2A08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2987")

    ChrTalk(
        0x17,
        (
            "#00105FAh, KeA.\x02\x03",
            "#00102FSay, what do you think about this dress?\x01",
            "I think it's a perfect fit for you.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01110FWow, how pretty...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FA d-dress...?\x01",
            "Is there an occasion to put one on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#00109F*giggle*, even if not, what's wrong with it?\x02\x03",
            "#00104FWe have to make KeA\x01",
            "try many different clothes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F(Uuhm, it looks like fun...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2A03")

    label("loc_2987")


    ChrTalk(
        0x17,
        (
            "#00102F*giggle*, I'll stay here a little\x01",
            "longer to have a look.\x02\x03",
            "#00109FI have to find many different\x01",
            "clothes for KeA.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A03")

    Jump("loc_2D65")

    label("loc_2A08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_2D40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C83")

    ChrTalk(
        0x17,
        (
            "#00103FAs I thought, this boutique seems to have \x01",
            "an assortment of good quality clothes.\x02\x03",
            "#00100FThe silk of this dress too, and\x01",
            "the Bareahard's fur over\x01",
            "there is very nice to the touch...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FBareahard...\x01",
            "Isn't it the name of a city in the\x01",
            "north-east part of the Empire?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#00100FYes, the place is famous as a\x01",
            "superior quality fur producing area.\x02\x03",
            "#00104FWhen attending at social parties,\x01",
            "you often notice women\x01",
            "wearing them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FEeh, you really know a lot.\x02\x03",
            "#00003FAlthough I think that for this season\x01",
            "fur would be sweltering...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#00111F...You can say pretty\x01",
            "blunt things, eh?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2D3B")

    label("loc_2C83")


    ChrTalk(
        0x17,
        (
            "#00104FFor social occasions,\x01",
            "what you wear is a\x01",
            "kind of status.\x02\x03",
            "#00100FI personally think that, if someone likes\x01",
            "how they're made, there's no need\x01",
            "to concern with branded goods.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D3B")

    Jump("loc_2D65")

    label("loc_2D40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_2D4E")
    Jump("loc_2D65")

    label("loc_2D4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_2D5C")
    Jump("loc_2D65")

    label("loc_2D5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_2D65")

    label("loc_2D65")

    TalkEnd(0xFE)
    Return()

    # Function_23_2550 end

    def Function_24_2D69(): pass

    label("Function_24_2D69")

    Call(0, 25)
    Return()

    # Function_24_2D69 end

    def Function_25_2D6D(): pass

    label("Function_25_2D6D")

    TalkBegin(0x14)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D7A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30AB")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DCA")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2DCA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DEA")
    OP_AF(0x69)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_30A6")

    label("loc_2DEA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DFE")
    Jump("loc_30A6")

    label("loc_2DFE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30A6")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_2E25")
    Jump("loc_30A6")

    label("loc_2E25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_2F1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EBC")

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
            "I know how she feels,\x01",
            "but I wish she held back\x01",
            "in front of the customers.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2F16")

    label("loc_2EBC")


    ChrTalk(
        0x14,
        (
            "*sigh*, that Drona.\x01",
            "I wish she held back from being\x01",
            "merry in front of the customers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F16")

    Jump("loc_30A6")

    label("loc_2F1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_2FAC")

    ChrTalk(
        0x14,
        (
            "A great number of female\x01",
            "customers has arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Uh uh, you end up letting out a sigh\x01",
            "with just so many beautiful ladies.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30A6")

    label("loc_2FAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_30A6")

    ChrTalk(
        0x14,
        (
            "With the occasion of the lake beach\x01",
            "opening, we, at boutique "Colserica"\x01",
            "have started handling in swimsuits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Since we deal in fashionable swimsuits\x01",
            "imported from the continent coastal areas,\x01",
            "by all means please have a look around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30A6")

    Jump("loc_2D7A")

    label("loc_30AB")

    TalkEnd(0x14)
    Return()

    # Function_25_2D6D end

    def Function_26_30AF(): pass

    label("Function_26_30AF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_30C0")
    Jump("loc_329A")

    label("loc_30C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_31B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_313D")

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
        "Aah, it'll be the treasure of my life!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_31AF")

    label("loc_313D")


    ChrTalk(
        0xFE,
        (
            "I can't believe I met that\x01",
            "Ilya in a place like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "This autograph will be the treasure of my life!\x02",
    )

    CloseMessageWindow()

    label("loc_31AF")

    Jump("loc_329A")

    label("loc_31B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_3217")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31CF")
    Call(0, 19)
    Jump("loc_3212")

    label("loc_31CF")


    ChrTalk(
        0xFE,
        (
            "(...Oh? By the way,\x01",
            "I think I saw this\x01",
            "customer somewhere...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3212")

    Jump("loc_329A")

    label("loc_3217")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_329A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3232")
    Call(0, 27)
    Jump("loc_329A")

    label("loc_3232")


    ChrTalk(
        0xFE,
        "Uhuhu, it looks very well on you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think it brings out your\x01",
            "elegance greatly,\x01",
            "miss customer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_329A")

    TalkEnd(0xFE)
    Return()

    # Function_26_30AF end

    def Function_27_329E(): pass

    label("Function_27_329E")

    OP_4B(0x15, 0xFF)
    OP_4B(0x16, 0xFF)

    ChrTalk(
        0x15,
        (
            "Let's see, I think you will be even\x01",
            "more elegant if we coordinate it\x01",
            "with this ribbon, miss customer...\x02",
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
        "Uhuhu, it looks very well on you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    OP_4C(0x15, 0xFF)
    OP_4C(0x16, 0xFF)
    Return()

    # Function_27_329E end

    def Function_28_3359(): pass

    label("Function_28_3359")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_336A")
    Jump("loc_33EA")

    label("loc_336A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_3378")
    Jump("loc_33EA")

    label("loc_3378")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_33EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3393")
    Call(0, 27)
    Jump("loc_33EA")

    label("loc_3393")


    ChrTalk(
        0xFE,
        (
            "Uh uh, you really\x01",
            "know your stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then, can I have this\x01",
            "coordinated outfit?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33EA")

    TalkEnd(0xFE)
    Return()

    # Function_28_3359 end

    def Function_29_33EE(): pass

    label("Function_29_33EE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34FE")

    ChrTalk(
        0xFE,
        (
            "Michelam Health Resort...\x01",
            "It's the first time I came here and it's great.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I lived here, it seems\x01",
            "I could say goodbye to the\x01",
            "life with that boring husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After I have eaten, I must go immediately \x01",
            "to have a look at the villas area.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_35AA")

    label("loc_34FE")


    ChrTalk(
        0xFE,
        (
            "If I lived here, it seems\x01",
            "I could say goodbye to the\x01",
            "life with that boring husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After I have eaten, I must go immediately \x01",
            "to have a look at the villas area.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35AA")

    TalkEnd(0xFE)
    Return()

    # Function_29_33EE end

    SaveToFile()

Try(main)
