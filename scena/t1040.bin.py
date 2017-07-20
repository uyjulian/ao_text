from ScenarioHelper import *

def main():
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
        "lute",               # 1
        "Mesh",               # 2
        "Woman",                   # 3
        "tourist",                 # 4
        "tourist",                 # 5
        "tourist",                 # 6
        "tourist",                 # 7
        "tourist",                 # 8
        "tourist",                 # 9
        "tourist",                 # 10
        "Waji",                   # 11
        "Mrs. Margaret",       # 12
        "Winona",               # 13
        "Dorona",               # 14
        "tourist",                 # 15
        "Erie",                 # 16
        "Franc",                 # 17
        "Cecil",                 # 18
        "Ilia",                 # 19
        "Lisha",               # 20
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
        "Function_5_8C7",          # 05, 5
        "Function_6_A32",          # 06, 6
        "Function_7_A36",          # 07, 7
        "Function_8_E44",          # 08, 8
        "Function_9_104B",         # 09, 9
        "Function_10_1221",        # 0A, 10
        "Function_11_12AE",        # 0B, 11
        "Function_12_1339",        # 0C, 12
        "Function_13_13B2",        # 0D, 13
        "Function_14_143D",        # 0E, 14
        "Function_15_14C4",        # 0F, 15
        "Function_16_15C5",        # 10, 16
        "Function_17_164C",        # 11, 17
        "Function_18_16C2",        # 12, 18
        "Function_19_18E1",        # 13, 19
        "Function_20_19CF",        # 14, 20
        "Function_21_1BA9",        # 15, 21
        "Function_22_2129",        # 16, 22
        "Function_23_232C",        # 17, 23
        "Function_24_2ABE",        # 18, 24
        "Function_25_2AC2",        # 19, 25
        "Function_26_2DBB",        # 1A, 26
        "Function_27_2F9F",        # 1B, 27
        "Function_28_3043",        # 1C, 28
        "Function_29_30E9",        # 1D, 29
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
    Jump("loc_8C3")

    label("loc_7BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_7CB")
    Jump("loc_8C3")

    label("loc_7CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_7D9")
    Jump("loc_8C3")

    label("loc_7D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_7E7")
    Jump("loc_8C3")

    label("loc_7E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_89E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_802")
    Call(0, 5)
    Jump("loc_899")

    label("loc_802")


    ChrTalk(
        0x12,
        (
            "#10304FHuff, as you can see the club\x01",
            "I got caught by regulars.\x02\x03",
            "#10300FWell, not to be late for the set\x01",
            "As I will cut it early,\x01",
            "You can rest assured.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_899")

    Jump("loc_8C3")

    label("loc_89E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_8AC")
    Jump("loc_8C3")

    label("loc_8AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_8BA")
    Jump("loc_8C3")

    label("loc_8BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_8C3")

    label("loc_8C3")

    TalkEnd(0xFE)
    Return()

    # Function_4_7AC end

    def Function_5_8C7(): pass

    label("Function_5_8C7")


    ChrTalk(
        0xA,
        (
            "Huhu, even so, it is unusual.\x01",
            "Waji you are coming over here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If you contact me immediately,\x01",
            "I will go out with as much as I can ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#10304FHuh, I am coming with my friends today.\x02\x03",
            "#10302FI'm sorry, but I have a promise after this\x01",
            "I will have you round up early?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Ah, the place where such a naughty thing is also a nice scintillator\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(Ho, hosts are\x01",
            "Is it okay with this …? )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    ClearChrFlags(0x12, 0x10)
    ClearChrFlags(0xA, 0x10)
    Return()

    # Function_5_8C7 end

    def Function_6_A32(): pass

    label("Function_6_A32")

    Call(0, 7)
    Return()

    # Function_6_A32 end

    def Function_7_A36(): pass

    label("Function_7_A36")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A43")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E40")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AA1")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_AA1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC1")
    OP_AF(0x66)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E3B")

    label("loc_AC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AD5")
    Jump("loc_E3B")

    label("loc_AD5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E3B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_AFC")
    Jump("loc_E3B")

    label("loc_AFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_CBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C14")

    ChrTalk(
        0x8,
        (
            "This restaurant\x01",
            "In the name \"Fortuna\"\x01",
            "It means \"happiness\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In order to enjoy a very happy meal,\x01",
            "Maximum service to our customers\x01",
            "I am allowed to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If there is something to notice,\x01",
            "Please do not hesitate to tell us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CB5")

    label("loc_C14")


    ChrTalk(
        0x8,
        (
            "To make you enjoy a happy meal,\x01",
            "Maximum service to our customers\x01",
            "I am allowed to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If there is something to notice,\x01",
            "Please do not hesitate to tell us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CB5")

    Jump("loc_E3B")

    label("loc_CBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_E3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D9E")

    ChrTalk(
        0x8,
        "Welcome to the restaurant \"Fortuna\".\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In our shop, we used the best ingredients\x01",
            "The best dishes at the best location\x01",
            "It is served.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please, elegant and happy temporary\x01",
            "I hope you have fun ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E3B")

    label("loc_D9E")


    ChrTalk(
        0x8,
        (
            "In our shop, we used the best ingredients\x01",
            "The best dishes at the best location\x01",
            "It is served.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please, elegant and happy temporary\x01",
            "I hope you have fun ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E3B")

    Jump("loc_A43")

    label("loc_E40")

    TalkEnd(0x8)
    Return()

    # Function_7_A36 end

    def Function_8_E44(): pass

    label("Function_8_E44")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_E55")
    Jump("loc_1047")

    label("loc_E55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_EF2")

    ChrTalk(
        0xFE,
        (
            "Recently in the theme park,\x01",
            "A new attraction\x01",
            "It seems that it was installed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is rumored to be a coffee - bastard,\x01",
            "I wonder what kind of attraction.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1047")

    label("loc_EF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1047")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FD8")

    ChrTalk(
        0xFE,
        (
            "Lake beach which opened this time,\x01",
            "It seems to be very popular regardless of age and sex.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It still has a hot day,\x01",
            "Customers visiting Michelam, too,\x01",
            "It seems that it is increasing compared with the average year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, I also want to go once.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1047")

    label("loc_FD8")


    ChrTalk(
        0xFE,
        (
            "Lake beach which opened this time,\x01",
            "It seems to be very popular regardless of age and sex.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, I also want to go once.\x02",
    )

    CloseMessageWindow()

    label("loc_1047")

    TalkEnd(0xFE)
    Return()

    # Function_8_E44 end

    def Function_9_104B(): pass

    label("Function_9_104B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_105C")
    Jump("loc_121D")

    label("loc_105C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1187")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1111")

    ChrTalk(
        0xFE,
        "Oh, Wazy you have gone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if you go home\x01",
            "Taking care of a boring husband\x01",
            "I have to do it ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I guess I'm drinking alone for a while.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1182")

    label("loc_1111")


    ChrTalk(
        0xFE,
        "Oh, Wazy you have gone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not care for my husband at home,\x01",
            "I guess I'm drinking alone for a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1182")

    Jump("loc_121D")

    label("loc_1187")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1214")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11AA")
    Call(0, 5)
    TalkEnd(0xFE)
    SetChrSubChip(0xA, 0x2)
    Return()

    label("loc_11AA")


    ChrTalk(
        0xFE,
        (
            "Wada is your host,\x01",
            "Sometimes you do not care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… Well, there is nice though\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    SetChrSubChip(0xA, 0x2)
    Return()

    label("loc_1214")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_121D")

    label("loc_121D")

    TalkEnd(0xFE)
    Return()

    # Function_9_104B end

    def Function_10_1221(): pass

    label("Function_10_1221")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1232")
    Jump("loc_12AA")

    label("loc_1232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1240")
    Jump("loc_12AA")

    label("loc_1240")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_12AA")

    ChrTalk(
        0xFE,
        "A little late breakfast.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ho Ho Ho, for Morning\x01",
            "Maybe it is too luxurious.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12AA")

    TalkEnd(0xFE)
    Return()

    # Function_10_1221 end

    def Function_11_12AE(): pass

    label("Function_11_12AE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_12BF")
    Jump("loc_1335")

    label("loc_12BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_12CD")
    Jump("loc_1335")

    label("loc_12CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1335")

    ChrTalk(
        0xFE,
        "No, I wonder what I should eat.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's still hot, and anyway\x01",
            "I hope something cool can be done.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1335")

    TalkEnd(0xFE)
    Return()

    # Function_11_12AE end

    def Function_12_1339(): pass

    label("Function_12_1339")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_134A")
    Jump("loc_13AE")

    label("loc_134A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1358")
    Jump("loc_13AE")

    label("loc_1358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_13AE")

    ChrTalk(
        0xFE,
        "(Kachakaka … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's delicious, mumps ……\x01",
            "It's a crazy little … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13AE")

    TalkEnd(0xFE)
    Return()

    # Function_12_1339 end

    def Function_13_13B2(): pass

    label("Function_13_13B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_13C3")
    Jump("loc_1439")

    label("loc_13C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1430")

    ChrTalk(
        0xFE,
        (
            "Well, it was a charter\x01",
            "I just want to see it in the morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Let's go when we eat rice.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1439")

    label("loc_1430")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1439")

    label("loc_1439")

    TalkEnd(0xFE)
    Return()

    # Function_13_13B2 end

    def Function_14_143D(): pass

    label("Function_14_143D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_144E")
    Jump("loc_14C0")

    label("loc_144E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_14B7")

    ChrTalk(
        0xFE,
        (
            "Haha, how are you?\x01",
            "I guess the shop I chose is quite interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Enjoy this taste until you feel well.\x02",
    )

    CloseMessageWindow()
    Jump("loc_14C0")

    label("loc_14B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_14C0")

    label("loc_14C0")

    TalkEnd(0xFE)
    Return()

    # Function_14_143D end

    def Function_15_14C4(): pass

    label("Function_15_14C4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_14D5")
    Jump("loc_15C1")

    label("loc_14D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_154B")

    ChrTalk(
        0xFE,
        (
            "(The taste of cooking\x01",
            "It's pretty nice though ….)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(Well, come on with the other\x01",
            "I made a mistake. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C1")

    label("loc_154B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_15C1")

    ChrTalk(
        0xFE,
        "Hey, I'm a bit dad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "These stores are in table manners\x01",
            "It is noisy, so be careful!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15C1")

    TalkEnd(0xFE)
    Return()

    # Function_15_14C4 end

    def Function_16_15C5(): pass

    label("Function_16_15C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_15D6")
    Jump("loc_1648")

    label("loc_15D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_163F")

    ChrTalk(
        0xFE,
        "I got hotter.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hey mom, from noon\x01",
            "Let's go to Lake Beach.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1648")

    label("loc_163F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1648")

    label("loc_1648")

    TalkEnd(0xFE)
    Return()

    # Function_16_15C5 end

    def Function_17_164C(): pass

    label("Function_17_164C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_165D")
    Jump("loc_16BE")

    label("loc_165D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_166B")
    Jump("loc_16BE")

    label("loc_166B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1679")
    Jump("loc_16BE")

    label("loc_1679")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1699")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1691")
    Jump("loc_1694")

    label("loc_1691")

    Call(0, 20)

    label("loc_1694")

    Jump("loc_16BE")

    label("loc_1699")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_16A7")
    Jump("loc_16BE")

    label("loc_16A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_16B5")
    Jump("loc_16BE")

    label("loc_16B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_16BE")

    label("loc_16BE")

    TalkEnd(0xFE)
    Return()

    # Function_17_164C end

    def Function_18_16C2(): pass

    label("Function_18_16C2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_16D3")
    Jump("loc_18DD")

    label("loc_16D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_16E1")
    Jump("loc_18DD")

    label("loc_16E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_16EF")
    Jump("loc_18DD")

    label("loc_16EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1821")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1819")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1797")

    ChrTalk(
        0x1A,
        (
            "#01703FWell, this store's clothes\x01",
            "I do not think so.\x02\x03",
            "#01702FMore like this, passionate\x01",
            "If you have exotic\x01",
            "It was good, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_1814")

    label("loc_1797")


    ChrTalk(
        0x1A,
        (
            "#01705FEven so,\x01",
            "Lisha is late.\x02\x03",
            "#01706FIf you do not come quickly,\x01",
            "Time to choose clothes\x01",
            "It's gone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1814")

    Jump("loc_181C")

    label("loc_1819")

    Call(0, 20)

    label("loc_181C")

    Jump("loc_18DD")

    label("loc_1821")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_18C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_183C")
    Call(0, 19)
    Jump("loc_18C1")

    label("loc_183C")


    ChrTalk(
        0x1A,
        (
            "#01705FOh, that's right, Lisha\x01",
            "I wonder if I will come yet?\x02\x03",
            "#01706FTo that girl,\x01",
            "A little more sexy clothes\x01",
            "I'd like to dress up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18C1")

    Jump("loc_18DD")

    label("loc_18C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_18D4")
    Jump("loc_18DD")

    label("loc_18D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_18DD")

    label("loc_18DD")

    TalkEnd(0xFE)
    Return()

    # Function_18_16C2 end

    def Function_19_18E1(): pass

    label("Function_19_18E1")

    OP_4B(0x1A, 0xFF)
    OP_4B(0x15, 0xFF)

    ChrTalk(
        0x15,
        (
            "That's right.\x01",
            "How about this dress?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#01703FHmm, that's right ……\x01",
            "A more gaudy person is\x01",
            "I like it privately.\x02\x03",
            "#01702FOh, can you show me a hat, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Yes, here please.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    ClearChrFlags(0x1A, 0x10)
    OP_4C(0x1A, 0xFF)
    Return()

    # Function_19_18E1 end

    def Function_20_19CF(): pass

    label("Function_20_19CF")

    OP_4B(0x1A, 0xFF)
    OP_4B(0x1B, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B13")

    ChrTalk(
        0x1A,
        (
            "#01700FI found the clothes I found earlier,\x01",
            "It's sexy with breasts free with spoon.\x02\x03",
            "#01709FHow? Lisa.\x01",
            "I will buy it so do not you wear it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#01805FWell, yeah! Is it?\x01",
            "Do you wear this! Is it?\x02\x03",
            "#01809FSurely\x01",
            "It's embarrassing ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#01709FIt's okay, if you\x01",
            "It is absolutely fascinating to dress!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_1BA0")

    label("loc_1B13")


    ChrTalk(
        0x1A,
        (
            "#01709FBecause it's okay,\x01",
            "I thought that I was deceived once\x01",
            "Try on it.\x02\x03",
            "#01701FYuka, I want to see it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#01806FHim, well …!\x02",
    )

    CloseMessageWindow()

    label("loc_1BA0")

    OP_4C(0x1A, 0xFF)
    OP_4C(0x1B, 0xFF)
    Return()

    # Function_20_19CF end

    def Function_21_1BA9(): pass

    label("Function_21_1BA9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_1BBA")
    Jump("loc_2125")

    label("loc_1BBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1BC8")
    Jump("loc_2125")

    label("loc_1BC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1BD6")
    Jump("loc_2125")

    label("loc_1BD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1ED3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E0B")

    ChrTalk(
        0x19,
        (
            "#05900FI heard from Elie a little while ago,\x01",
            "Lloyd in this boutique\x01",
            "You bought a suit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FOh, a while ago ….\x01",
            "What's wrong with that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#05906FUu, a suit for a wedding ceremony\x01",
            "My sister will give it up\x01",
            "I thought I intended!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01105FWell, Lloyd's\x01",
            "After all I am getting married -?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FNo, no, I will not!\x02\x03",
            "#00006FOriginally for investigation\x01",
            "It is a thing that I have taken care of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#05905FWell, was that so?\x01",
            "That's a shame with that.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F(Cecil elder sister ….\x01",
            "Have not you enjoyed my reaction? )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_1ECE")

    label("loc_1E0B")


    ChrTalk(
        0x19,
        (
            "#05902FHuhu, when doing a wedding ceremony,\x01",
            "Absolutely call me.\x02\x03",
            "#05901FFrom the setting of the wedding ceremony\x01",
            "Until the location of the honeymoon is decided,\x01",
            "Because my sister will do it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FFrom the story of a suit\x01",
            "You are leaping too much ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ECE")

    Jump("loc_2125")

    label("loc_1ED3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_210E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_208C")

    ChrTalk(
        0x19,
        "#05903F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FCecil elder sister, what's wrong?\x02",
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x19,
        (
            "#05902F…… Oh, Lloyd.\x02\x03",
            "#05909FYes, on a theme park\x01",
            "Because it is the first time to go,\x01",
            "What kind of place is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FOh, I am the first time.\x02\x03",
            "#00000FI have been to before\x01",
            "As far as I hear from Randy and Noel,\x01",
            "Is not it okay to expect?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#05909FHehe, that's right.\x01",
            "Because it's been awesome\x01",
            "I have to guide you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_2109")

    label("loc_208C")


    ChrTalk(
        0x19,
        (
            "#05904FYes, today.\x01",
            "You must have fun.\x02\x03",
            "#05902FI am the first time,\x01",
            "To Randy and Noel\x01",
            "Let me show you around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2109")

    Jump("loc_2125")

    label("loc_210E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_211C")
    Jump("loc_2125")

    label("loc_211C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_2125")

    label("loc_2125")

    TalkEnd(0xFE)
    Return()

    # Function_21_1BA9 end

    def Function_22_2129(): pass

    label("Function_22_2129")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_213A")
    Jump("loc_2328")

    label("loc_213A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_2148")
    Jump("loc_2328")

    label("loc_2148")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_2156")
    Jump("loc_2328")

    label("loc_2156")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_2166")
    Jump("loc_2328")

    label("loc_2166")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_2174")
    Jump("loc_2328")

    label("loc_2174")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_2311")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22B2")

    ChrTalk(
        0x18,
        (
            "#06405FOh, Mr. Lloyd!\x01",
            "Please take a look.\x02\x03",
            "#06409FHow is this clothes,\x01",
            "Do you look good on me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, is not it quite good?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#06402FOops, it is a seal of Lloyd 's seal!\x01",
            "Well then let's buy this … …\x02\x03",
            "#06409FHuhu, even my sister's clothes\x01",
            "I will choose it without permission.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_230C")

    label("loc_22B2")


    ChrTalk(
        0x18,
        (
            "#06409FThere are lots of clothes that looks good ~!\x02\x03",
            "#06406FI wish I could have had a big sister.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_230C")

    Jump("loc_2328")

    label("loc_2311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_231F")
    Jump("loc_2328")

    label("loc_231F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_2328")

    label("loc_2328")

    TalkEnd(0xFE)
    Return()

    # Function_22_2129 end

    def Function_23_232C(): pass

    label("Function_23_232C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_233D")
    Jump("loc_2ABA")

    label("loc_233D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_234B")
    Jump("loc_2ABA")

    label("loc_234B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_2359")
    Jump("loc_2ABA")

    label("loc_2359")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_25D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_253F")

    ChrTalk(
        0x17,
        (
            "#00113FHa, I was prepared for a while\x01",
            "No way it meets such eye … …\x02\x03",
            "#00111F…… Hey, Lloyd.\x01",
            "I have not really seen it#8R噵 噵 噵 噵#Is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FOh, oh.\x01",
            "It's all right, I have not seen it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#00106FWell, I do not have any idea.\x02\x03",
            "#00112F…… If I had seen it,\x01",
            "I will take responsibility.\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x101,
        "#00011F#4SEh! Is it?#3S\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#00104F…… Oh no, it is a joke.\x02\x03",
            "#00109FHuhu, you really are\x01",
            "There are places to treat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FWell, forgive me …\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_25CB")

    label("loc_253F")


    ChrTalk(
        0x17,
        (
            "#00113FWell, well that suits you\x01",
            "I was prepared to a certain extent … ….\x02\x03",
            "#00102FI'm glad I could repel demon for the time being,\x01",
            "Let's say that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25CB")

    Jump("loc_2ABA")

    label("loc_25D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_27B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_273E")

    ChrTalk(
        0x17,
        (
            "#00105FOh, Ka'aa-chan.\x02\x03",
            "#00102FHey, maybe this dress.\x01",
            "It is perfect for Kia-chan\x01",
            "I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01110FWow, Kire!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FDo, you dress ……\x01",
            "Do you have timing to wear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#00109FHuhuu, you do not need to.\x02\x03",
            "#00104FKa'a-chan has various clothes\x01",
            "I have to try it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F(Well, it looks fun … …)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_27AE")

    label("loc_273E")


    ChrTalk(
        0x17,
        (
            "#00102FHuhuu, I'm a little more\x01",
            "I will look at you here.\x02\x03",
            "#00109FKaea's clothes\x01",
            "I have to look for various things.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27AE")

    Jump("loc_2ABA")

    label("loc_27B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_2A95")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29E8")

    ChrTalk(
        0x17,
        (
            "#00103FAfter all, this boutique is\x01",
            "It seems that there are good quality items.\x02\x03",
            "#00100FIt is also the silk of this dress,\x01",
            "Barrier heart fur there also\x01",
            "With a very gentle touch ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FBarrier Heart ……\x01",
            "Surely in the eastern part of the Empire\x01",
            "Was it the name of the city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#00100FYeah, that is over there\x01",
            "It is famous for producing good quality fur.\x02\x03",
            "#00104FWhen attending a social party,\x01",
            "Ladies wearing\x01",
            "There are many things to see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWell, it's truly familiar.\x02\x03",
            "#00003FThis season, as expected the fur\x01",
            "I think it's hot, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#00111F…… that there is no body and no lid\x01",
            "Wait for me to say.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2A90")

    label("loc_29E8")


    ChrTalk(
        0x17,
        (
            "#00104FIn a social occasion,\x01",
            "What I am wearing is\x01",
            "It is a kind of status.\x02\x03",
            "#00100FPersonally, if you can make it\x01",
            "I need to be concerned about brand-name items\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A90")

    Jump("loc_2ABA")

    label("loc_2A95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_2AA3")
    Jump("loc_2ABA")

    label("loc_2AA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_2AB1")
    Jump("loc_2ABA")

    label("loc_2AB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_2ABA")

    label("loc_2ABA")

    TalkEnd(0xFE)
    Return()

    # Function_23_232C end

    def Function_24_2ABE(): pass

    label("Function_24_2ABE")

    Call(0, 25)
    Return()

    # Function_24_2ABE end

    def Function_25_2AC2(): pass

    label("Function_25_2AC2")

    TalkBegin(0x14)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2ACF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DB7")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B2D")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2B2D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B4D")
    OP_AF(0x69)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2DB2")

    label("loc_2B4D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B61")
    Jump("loc_2DB2")

    label("loc_2B61")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DB2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_2B88")
    Jump("loc_2DB2")

    label("loc_2B88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_2C6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C18")

    ChrTalk(
        0x14,
        (
            "When it comes to Dorona\x01",
            "It got floating ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "I understand your feelings,\x01",
            "In front of the customer\x01",
            "I want you to refrain.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2C66")

    label("loc_2C18")


    ChrTalk(
        0x14,
        (
            "When it comes to Dorona.\x01",
            "What is floating in front of customers\x01",
            "I want you to refrain.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C66")

    Jump("loc_2DB2")

    label("loc_2C6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_2CE3")

    ChrTalk(
        0x14,
        (
            "Female customers\x01",
            "There were many.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Huhu, all the beautiful people\x01",
            "I will be sighing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DB2")

    label("loc_2CE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_2DB2")

    ChrTalk(
        0x14,
        (
            "Along with the opening of Lake Beach,\x01",
            "In the boutique \"Corserica\"\x01",
            "I also started handling swimwear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Imported from the continental coast\x01",
            "We also have fashionable swimwear,\x01",
            "Please do not miss it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DB2")

    Jump("loc_2ACF")

    label("loc_2DB7")

    TalkEnd(0x14)
    Return()

    # Function_25_2AC2 end

    def Function_26_2DBB(): pass

    label("Function_26_2DBB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_2DCC")
    Jump("loc_2F9B")

    label("loc_2DCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_2EB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E4A")

    ChrTalk(
        0xFE,
        (
            "To that Iria-Platier\x01",
            "I got an autographed signature.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, I will make it a lifetime treasure!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2EAF")

    label("loc_2E4A")


    ChrTalk(
        0xFE,
        (
            "No way to that Iria,\x01",
            "I can not see you in such a place ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I will make this signature, a lifetime treasure!\x02",
    )

    CloseMessageWindow()

    label("loc_2EAF")

    Jump("loc_2F9B")

    label("loc_2EB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_2F1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ECF")
    Call(0, 19)
    Jump("loc_2F15")

    label("loc_2ECF")


    ChrTalk(
        0xFE,
        (
            "(……that?\x01",
            "By the way, this customer,\x01",
            "Like you saw somewhere … …)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F15")

    Jump("loc_2F9B")

    label("loc_2F1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_2F9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F35")
    Call(0, 27)
    Jump("loc_2F9B")

    label("loc_2F35")


    ChrTalk(
        0xFE,
        "Uhufu, it fits you very well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Your elegance\x01",
            "I wonder if I draw it to the maximum\x01",
            "I know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F9B")

    TalkEnd(0xFE)
    Return()

    # Function_26_2DBB end

    def Function_27_2F9F(): pass

    label("Function_27_2F9F")

    OP_4B(0x15, 0xFF)
    OP_4B(0x16, 0xFF)

    ChrTalk(
        0x15,
        (
            "Well, in coordination\x01",
            "When I turn on this ribbon\x01",
            "Would it be more elegant …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "Is it … like that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Uhufu, it matches very well.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    OP_4C(0x15, 0xFF)
    OP_4C(0x16, 0xFF)
    Return()

    # Function_27_2F9F end

    def Function_28_3043(): pass

    label("Function_28_3043")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_3054")
    Jump("loc_30E5")

    label("loc_3054")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_3062")
    Jump("loc_30E5")

    label("loc_3062")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_30E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_307D")
    Call(0, 27)
    Jump("loc_30E5")

    label("loc_307D")


    ChrTalk(
        0xFE,
        (
            "Hehe, you\x01",
            "I know quite well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well then this coordination\x01",
            "I wonder if it will give you a line.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30E5")

    TalkEnd(0xFE)
    Return()

    # Function_28_3043 end

    def Function_29_30E9(): pass

    label("Function_29_30E9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31B0")

    ChrTalk(
        0xFE,
        (
            "Recreational area Michelam ……\x01",
            "It was the first time I came, but it is the best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you live here,\x01",
            "Both living with that inept husband\x01",
            "I guess I can do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As soon as you eat rice\x01",
            "I have to go to the villa ground.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_322F")

    label("loc_31B0")


    ChrTalk(
        0xFE,
        (
            "If you live here,\x01",
            "Both living with that inept husband\x01",
            "I guess I can do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As soon as you eat rice\x01",
            "I have to go to the villa ground.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_322F")

    TalkEnd(0xFE)
    Return()

    # Function_29_30E9 end

    SaveToFile()

Try(main)
