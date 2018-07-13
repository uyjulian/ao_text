from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1210.bin",                # FileName
        "c1210",                    # MapName
        "c1210",                    # Location
        0x0021,                     # MapIndex
        "ed7114",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 33, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1210",                  # 0
        "Cao",                    # 1
        "Lau",                    # 2
        "Shing",                  # 3
        "Heiyue Member",          # 4
        "SE制御",                 # 5
    ))

    AddCharChip((
        "chr/ch06302.itc",                   # 00
        "chr/ch31400.itc",                   # 01
        "chr/ch45000.itc",                   # 02
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   2,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(4294894996, 0,       1900,    500,     4294894996, 1500,    1900,    0x007C, 0,  14, 0x0000)
    DeclActor(4294930066, 0,       7940,    500,     4294930066, 1500,    7940,    0x007C, 0,  14, 0x0000)
    DeclActor(5000,    0,       6440,    500,     5000,    1500,    6440,    0x007C, 0,  14, 0x0000)
    DeclActor(3430,    0,       70,      500,     5650,    1500,    40,      0x007E, 0,  3,  0x0000)

    ChipFrameInfo(504, 0)                                        # 0

    ScpFunction((
        "Function_0_1F8",          # 00, 0
        "Function_1_2A8",          # 01, 1
        "Function_2_3C3",          # 02, 2
        "Function_3_45A",          # 03, 3
        "Function_4_507",          # 04, 4
        "Function_5_5B4",          # 05, 5
        "Function_6_6B5",          # 06, 6
        "Function_7_7E3",          # 07, 7
        "Function_8_DA8",          # 08, 8
        "Function_9_29BA",         # 09, 9
        "Function_10_2AE5",        # 0A, 10
        "Function_11_2DDD",        # 0B, 11
        "Function_12_3EDF",        # 0C, 12
        "Function_13_51A5",        # 0D, 13
        "Function_14_51B8",        # 0E, 14
    ))


    def Function_0_1F8(): pass

    label("Function_0_1F8")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_230"),
        (1, "loc_23C"),
        (2, "loc_248"),
        (3, "loc_254"),
        (4, "loc_260"),
        (5, "loc_26C"),
        (6, "loc_278"),
        (SWITCH_DEFAULT, "loc_284"),
    )


    label("loc_230")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_290")

    label("loc_23C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_290")

    label("loc_248")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_290")

    label("loc_254")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_290")

    label("loc_260")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_290")

    label("loc_26C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_290")

    label("loc_278")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_290")

    label("loc_284")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_290")

    label("loc_290")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_290")

    label("loc_2A7")

    Return()

    # Function_0_1F8 end

    def Function_1_2A8(): pass

    label("Function_1_2A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2ED")
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 5600, 50, 0, 270)

    label("loc_2ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_301")
    ClearScenarioFlags(0x22, 0)
    Event(0, 7)
    Jump("loc_310")

    label("loc_301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_310")
    ClearScenarioFlags(0x22, 1)
    Event(0, 12)

    label("loc_310")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_33F")
    Event(0, 8)

    label("loc_33F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_385")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 5800, 0, 1300, 270)
    BeginChrThread(0xA, 0, 0, 0)
    ClearChrFlags(0xA, 0x40)

    label("loc_385")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C2")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 5800, 0, -1460, 270)
    BeginChrThread(0x9, 0, 0, 0)
    ClearChrFlags(0x9, 0x40)

    label("loc_3C2")

    Return()

    # Function_1_2A8 end

    def Function_2_3C3(): pass

    label("Function_2_3C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3D8")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_3D8")

    SetMapObjFrame(0xFF, "c122_tesri02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tama00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tama01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kuro01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ato", 0x0, 0x1)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x4, 0x2)
    ClearMapObjFlags(0x5, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_459")
    OP_66(0x3, 0x1)

    label("loc_459")

    Return()

    # Function_2_3C3 end

    def Function_3_45A(): pass

    label("Function_3_45A")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_48A")
    Call(0, 9)
    Jump("loc_503")

    label("loc_48A")


    ChrTalk(
        0x8,
        (
            "#03200FNevertheless, it was\x01",
            "really fortuitous that\x01",
            "you all came.\x02\x03",
            "#03204FPlease, take very good\x01",
            "care of Lord Shing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_503")

    TalkEnd(0x8)
    Return()

    # Function_3_45A end

    def Function_4_507(): pass

    label("Function_4_507")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_537")
    Call(0, 9)
    Jump("loc_5B0")

    label("loc_537")


    ChrTalk(
        0x8,
        (
            "#03200FNevertheless, it was\x01",
            "really fortuitous that\x01",
            "you all came.\x02\x03",
            "#03204FPlease, take very good\x01",
            "care of Lord Shing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B0")

    TalkEnd(0x8)
    Return()

    # Function_4_507 end

    def Function_5_5B4(): pass

    label("Function_5_5B4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_676")

    ChrTalk(
        0x9,
        (
            "In case you want to do us the favor\x01",
            "to accept, please return quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Lord Shing, but also we, don't have\x01",
            "unlimited time that we can wait.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B1")

    label("loc_676")


    ChrTalk(
        0x9,
        (
            "Lord Shing, please be careful\x01",
            "and have a safe travel.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B1")

    TalkEnd(0xFE)
    Return()

    # Function_5_5B4 end

    def Function_6_6B5(): pass

    label("Function_6_6B5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7DF")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_772")

    ChrTalk(
        0xA,
        (
            "Miss, I will\x01",
            "wait here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Please, you have to come back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FEehm, I can't promise you, but...\x01",
            "I'll see what I can do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7DF")

    label("loc_772")


    ChrTalk(
        0xA,
        (
            "I don't know what you have to do,\x01",
            "just finish it and come back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I won't forgive you\x01",
            "if you refuse!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DF")

    TalkEnd(0xFE)
    Return()

    # Function_6_6B5 end

    def Function_7_7E3(): pass

    label("Function_7_7E3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06300.itc", 0x1E)
    LoadChrToIndex("chr/ch31400.itc", 0x1F)
    LoadChrToIndex("chr/ch31500.itc", 0x20)
    LoadChrToIndex("apl/ch50237.itc", 0x21)
    SoundLoad(128)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 7200, 0, 0, 90)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 6000, 0, 1500, 135)
    SetChrChipByIndex(0xB, 0x20)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -6000, 0, 0, 90)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x0, 0x8)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    OP_68(9200, 1100, 0, 0)
    MoveCamera(47, 15, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20000, 0)
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)
    Sound(128, 2, 50, 0)
    OP_68(7200, 1100, 0, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            "#03204F──Oh my, what a fancy coincidence.\x02\x03",
            "#03210FEven at the time of the "Black Auction"...\x01",
            "It really seems we have a fateful connection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PHowever, Master Cao...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PWhat could there be at the\x01",
            "south bank of Elm Lake?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03204FWell, as for that, we can\x01",
            "only bet on "his" intuition.\x02\x03",
            "#03200FThat delinquents' leader demonize and\x01",
            "the "Snake" and "Church" intervention...\x02\x03",
            "There's nothing like taking care of blind\x01",
            "spots in advance, even just a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P...Indeed.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0xB, 0x80)
    Sound(886, 0, 50, 0)
    Sleep(150)
    Sound(886, 0, 40, 0)
    Sleep(150)
    Sound(886, 0, 40, 0)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    NpcTalk(
        0xB,
        "Man's Voice",
        "──P-Pardon me!\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(250)
    OP_68(-3000, 700, 0, 0)
    MoveCamera(40, 27, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(17500, 0)
    OP_68(4900, 1100, 0, 2000)
    MoveCamera(40, 19, 0, 2000)
    SetCameraDistance(19500, 2000)
    Sound(103, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_BCF():
        OP_96(0xFE, 0x8FC, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_BCF)

    def lambda_BE9():

        label("loc_BE9")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_BE9")

    QueueWorkItem2(0x8, 2, lambda_BE9)
    Sleep(50)

    def lambda_BFE():

        label("loc_BFE")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_BFE")

    QueueWorkItem2(0x9, 2, lambda_BFE)

    def lambda_C10():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_C10)
    WaitChrThread(0xB, 1)
    EndChrThread(0x8, 0x2)
    EndChrThread(0x9, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x9,
        (
            "#11PWhat is it, Fung!\x01",
            "Why are you restless!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#6PI-I'm terribly sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#6PIt's that...moments ago, there was a hard\x01",
            "to believe report from the surveillance unit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PA hard to believe report...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#03205F............\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    Sleep(130)
    SetChrSubChip(0x8, 0x1)
    Sleep(130)
    SetChrSubChip(0x8, 0x2)
    Sleep(130)
    Sound(318, 0, 100, 0)
    SetChrSubChip(0x8, 0x3)
    Sleep(800)

    ChrTalk(
        0x8,
        (
            "#03201F──Fung.\x01",
            "Please, let me hear the details.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19000, 2000)
    StopSound(128, 2000, 40)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(1000)
    SetScenarioFlags(0x22, 0)
    NewScene("e4500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_7E3 end

    def Function_8_DA8(): pass

    label("Function_8_DA8")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    AddParty(0xA1, 0xFF, 0xFF)
    SetChrFlags(0x1A2, 0x80)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 5800, 0, -1460, 270)
    OP_4B(0x9, 0xFF)
    OP_68(3470, 1000, -250, 0)
    MoveCamera(44, 20, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 2300, 0, 470, 90)
    SetChrPos(0x102, 2130, 0, -650, 90)
    SetChrPos(0x104, 1020, 0, 1050, 90)
    SetChrPos(0x109, 810, 0, -120, 90)
    SetChrPos(0x105, 1030, 0, -1210, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrSubChip(0x8, 0x0)
    SetCameraDistance(21120, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x8,
        (
            "#11P#03200FHi.\x02\x03",
            "#03209FWelcome to the "Heiyue Trade Company".\x01",
            "Allow me to receive you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00001F...Pardon the intrusion.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FWe accepted your kind\x01",
            "offer and entered inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#03200FHu hu...\x01",
            "Long time no see too, Mr. Randy.\x02\x03",
            "#03204FI was looking forward to your comeback.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303F...Well, thanks.\x01",
            "You seem to never change too, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#03204FHa ha, I will take that\x01",
            "as a compliment.\x02\x03",
            "#03209FWell, to think that Mr. Randy was \x01",
            "connected to that Crimson & Co....\x02\x03",
            "I too was really surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00301FHmph...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FIt seems that you know about "them"\x01",
            "to a certain extent, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#03204FYes, actually, it's not that we\x01",
            "haven't a little connection.\x02\x03",
            "#03200FCould it be that Mr. Randy\x01",
            "knows about that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303FYeah...about one year ago, it seems that uncle\x01",
            "and the others snuck in the Eastern District \x01",
            "and picked a fight with you "Heiyue", right?\x02\x03",
            "#00301FSeems it was quite a\x01",
            "full-blown war, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_12A4")

    ChrTalk(
        0x101,
        "#6P#00003F...Right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108FMr. Dudley too\x01",
            "said that...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12EC")

    label("loc_12A4")


    ChrTalk(
        0x102,
        "#6P#00105FBy the way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FMr. Dudley too\x01",
            "said that...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12EC")


    ChrTalk(
        0x8,
        (
            "#11P#03204FHu hu, it's true that it made\x01",
            "things lively in many ways.\x02\x03",
            "#03200FLuckily, since we closed a deal, it\x01",
            "didn't left a grudge on both parts, but...\x02\x03",
            "#03209FAmong the Heiyue elders, there're\x01",
            "those who, just by hearing their\x01",
            "names, swoon in anger even now.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#6P#10106FI-It was that much of a...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FHu hu, a lot of things\x01",
            "happened for sure, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#03203FWell, regarding the Revache old site,\x01",
            "it's a real pity but we gave up.\x02\x03",
            "#03200FDifferently from Revache that was a\x01",
            "mafia organization, there are a few\x01",
            "businesses we can cope up with directly...\x02\x03",
            "#03210FYou can rest assured\x01",
            "in that regard, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F...How kind of you.\x01",
            "(I can't completely believe him, though...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FExcuse me, what is the\x01",
            ""favor" you wanted to ask?\x02\x03",
            "#00103FWe thought it was certainly\x01",
            "about the Crimson & Co....\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Yes, actually──\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, 5080, 0, 7720, 180)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    Sound(121, 0, 100, 0)
    OP_71(0x3, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x3)
    Sleep(500)

    NpcTalk(
        0x1A2,
        "Boy's Voice",
        (
            "#5P#NYou're late, Cao!\x01",
            "What the heck are you doing!?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x8, 0x2)

    def lambda_17D9():

        label("loc_17D9")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_17D9")

    QueueWorkItem2(0x101, 1, lambda_17D9)
    Sleep(50)

    def lambda_17EE():

        label("loc_17EE")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_17EE")

    QueueWorkItem2(0x102, 1, lambda_17EE)
    Sleep(50)

    def lambda_1803():

        label("loc_1803")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_1803")

    QueueWorkItem2(0x104, 1, lambda_1803)
    Sleep(50)

    def lambda_1818():

        label("loc_1818")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_1818")

    QueueWorkItem2(0x109, 1, lambda_1818)
    Sleep(50)

    def lambda_182D():

        label("loc_182D")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_182D")

    QueueWorkItem2(0x105, 1, lambda_182D)
    Sleep(50)

    def lambda_1842():

        label("loc_1842")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_1842")

    QueueWorkItem2(0x9, 1, lambda_1842)
    Sleep(300)
    OP_68(4460, 1100, 100, 3000)

    def lambda_1868():
        OP_95(0xFE, 5800, 0, 1300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_1868)
    Sleep(100)

    def lambda_1885():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_1885)
    WaitChrThread(0x1A2, 1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x9, 0x1)
    OP_6F(0x1)

    ChrTalk(
        0x8,
        "#11P#03200FOoh, if it isn't Lord Shing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Did we do something wrong?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1A2,
        "Boy",
        (
            "Everything, how much do\x01",
            "you want to make me wait!?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1A2,
        "Boy",
        (
            "When is the guide\x01",
            "coming to pick me up!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That is why I said that if you are fine\x01",
            "with me, I could guide you anyt──\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1A2,
        "Boy",
        "You're no good, don't make me repeat it again!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1A2,
        "Boy",
        (
            "I finally came to have fun in Crossbell,\x01",
            "being guided by you would ruin it, right!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#03209FHu hu, since you say that we have\x01",
            "made the arrangements you see.\x02\x03",
            "#03204F"They" will be your guide.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1A2,
        "Boy",
        "What...?\x02",
    )

    CloseMessageWindow()
    OP_68(3470, 1000, -250, 1500)
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_1B71():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B71)
    Sleep(50)

    def lambda_1B81():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B81)
    Sleep(50)

    def lambda_1B91():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1B91)
    Sleep(50)

    def lambda_1BA1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1BA1)
    Sleep(50)

    def lambda_1BB1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1BB1)
    Sleep(300)

    ChrTalk(
        0x101,
        "#6P#00005FE-Excuse me, Branch Manager Cao...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105FCould it be that the "favor"\x01",
            "you wanted to ask is...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sleep(50)
    OP_93(0x9, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#11P#03200FHu hu, let me introduce you.\x02\x03",
            "#03204FThis is Lord Shing,\x01",
            "a certain "Heiyue"\x01",
            "elder's grandson.\x02\x03",
            "#03209FWe want you to guide\x01",
            "Lord Shing around\x01",
            "Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00106FA-As I thought...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00306FHey now, for real?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10300FHu hu, what a big request.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#11PThese guys are guides?\x01",
            "Aren't they still youngsters?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#11PHasn't Ilya Platiｲre or\x01",
            "Dieter Crois come for me?\x01\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x8, 0x2)

    ChrTalk(
        0x8,
        (
            "#11P#03209FHa ha, as you can imagine\x01",
            "that would be difficult...\x02\x03",
            "#03200FThey too are quite\x01",
            "famous in Crossbell...\x02\x03",
            "#03204FAfter all, they even were the center\x01",
            "figures who solved that incident...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "#11PEeh, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#11PSo you're the "Special Support Section"\x01",
            "that solved the Cult incident, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x8, 0x0)

    def lambda_202D():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_202D)
    Sleep(50)

    def lambda_203D():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_203D)
    Sleep(50)

    def lambda_204D():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_204D)
    Sleep(50)

    def lambda_205D():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_205D)
    Sleep(50)

    def lambda_206D():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_206D)
    Sleep(300)

    ChrTalk(
        0x101,
        "#6P#00005FHuh...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FW-Why do you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Because he is an elder's grandson,\x01",
            "Lord Shing is a well-informed person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In order to be able to come to Crossbell,\x01",
            "it seems he was made study a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "#11PEh eh, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#11PAs the grandson of an elder,\x01",
            "I'm in the position of bearing\x01",
            "the "Heiyue" future one day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#11PEven my mental attitude is different\x01",
            "from that of ordinary men like you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00306F(Damn brat...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10102F(Now now, senior Randy.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#11PWell, if you insist,\x01",
            "I'll have to accept, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#11PI also want to ask you\x01",
            "about the Cult incident──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "#11PEh...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00005F???\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FW-What's wrong?\x02",
    )

    CloseMessageWindow()

    def lambda_23C5():

        label("loc_23C5")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_23C5")

    QueueWorkItem2(0x101, 1, lambda_23C5)
    Sleep(50)

    def lambda_23DA():

        label("loc_23DA")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_23DA")

    QueueWorkItem2(0x102, 1, lambda_23DA)
    Sleep(50)

    def lambda_23EF():

        label("loc_23EF")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_23EF")

    QueueWorkItem2(0x104, 1, lambda_23EF)
    Sleep(50)

    def lambda_2404():

        label("loc_2404")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_2404")

    QueueWorkItem2(0x109, 1, lambda_2404)
    Sleep(50)

    def lambda_2419():

        label("loc_2419")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_2419")

    QueueWorkItem2(0x105, 1, lambda_2419)
    OP_95(0x1A2, 4900, 0, 2510, 2000, 0x0)
    TurnDirection(0x1A2, 0x102, 500)
    OP_63(0x1A2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "#11P#800WI-It's my #800Wf...\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    ChrTalk(
        0x1A2,
        "#11P#5SIt's my fated person...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x101, 0x1)
    OP_68(3060, 1100, -70, 2000)
    MoveCamera(52, 19, 0, 2000)
    OP_6E(380, 2000)
    SetCameraDistance(22270, 2000)
    OP_95(0x1A2, 2800, 0, 2150, 4000, 0x0)

    def lambda_2502():
        OP_95(0xFE, 2300, 0, 470, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_2502)
    OP_93(0x101, 0x5A, 0x0)
    OP_93(0x104, 0x5A, 0x0)
    OP_93(0x109, 0x5A, 0x0)

    def lambda_2531():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2531)

    def lambda_2546():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2546)

    def lambda_255B():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_255B)

    def lambda_2570():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2570)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    TurnDirection(0x101, 0x1A2, 500)

    ChrTalk(
        0x101,
        "#6P#00011FW-What...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105FEek...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Lovely looks!\x01",
            "Beautiful pearl gray hair!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "And capacious\x01",
            "amazing proportions!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "T-To think that I could meet\x01",
            "my ideal person in such place!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Miss!\x01",
            "What is your name?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FEhm...\x01",
            "It's Elie, Elie MacDowell.\x02\x03",
            "#00109F*giggle*, nice to meet you, Shing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Miss Elie...\x01",
            "...Even the name is lovely...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "I see, I came to Crossbell\x01",
            "to meet this person...!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00005F(W-What can I say...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306F(Jeez, not only he's impudent,\x01",
            "he's a super precocious brat.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10109F(Ahaha...\x01",
            "Miss Elie is so popular.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "#6PCao, I like her!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PI want this Miss to\x01",
            "be my guide at once!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#03204FHu hu, it is nice to hear that.\x02\x03",
            "#03209F──Then, everyone.\x01",
            "Please take care of Lord Shing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00011FPlease, w-wait a moment!\x02\x03",
            "#00003F(Guides for a Heiyue elder's grandson...\x01",
            "Is it all right to accept it?)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_29(0x73, 0x4, 0x2)
    Call(0, 10)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_8_DA8 end

    def Function_9_29BA(): pass

    label("Function_9_29BA")

    EventBegin(0x0)
    Fade(500)
    AddParty(0xA1, 0xFF, 0xFF)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0xA, 0x80)
    OP_68(3470, 1000, -250, 0)
    MoveCamera(44, 20, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x1A2, 5800, 0, 1300, 270)
    SetChrPos(0x101, 2300, 0, 470, 90)
    SetChrPos(0x102, 2130, 0, -650, 90)
    SetChrPos(0x104, 1020, 0, 1050, 90)
    SetChrPos(0x109, 810, 0, -120, 90)
    SetChrPos(0x105, 1030, 0, -1210, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrSubChip(0x8, 0x0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#11P#03200FWhat about it, Mr. Lloyd?\x02\x03",
            "Can I ask you to be a guide\x01",
            "for Lord Shing in Crossbell?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 10)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_9_29BA end

    def Function_10_2AE5(): pass

    label("Function_10_2AE5")

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
            "Accept the Request\x01",          # 0
            "Think About It For Now\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2B5F"),
        (1, "loc_2B67"),
        (SWITCH_DEFAULT, "loc_2D87"),
    )


    label("loc_2B5F")

    Call(0, 11)
    Jump("loc_2D87")

    label("loc_2B67")


    ChrTalk(
        0x101,
        (
            "#6P#00003FI'm sorry,\x01",
            "we're busy now...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#11PW-What did you say...?\x01",
            "Are you refusing to be my guides!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00106FI'm sorry, Shing.\x01",
            "It will be fine when we finish what we have to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FEehm, can we accept it\x01",
            "again after, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#03204FYes, of course we don't mind.\x02\x03",
            "#03200FHowever, Lord Shing\x01",
            "can't endure to wait too much.\x02\x03",
            "For that reason, please come back quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "#11PI'll be waiting for you, so do it fast!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0xA1, 0xFF)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 5800, 0, 1300, 270)
    BeginChrThread(0xA, 0, 0, 0)
    ClearChrFlags(0xA, 0x40)
    SetScenarioFlags(0x154, 6)
    Jump("loc_2D87")

    label("loc_2D87")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 900, 0, 50, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_71(0x3, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x3)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 5800, 0, -1460, 270)
    BeginChrThread(0x9, 0, 0, 0)
    ClearChrFlags(0x9, 0x40)
    EventEnd(0x5)
    Return()

    # Function_10_2AE5 end

    def Function_11_2DDD(): pass

    label("Function_11_2DDD")


    ChrTalk(
        0x101,
        (
            "#6P#00003FUnderstood.\x01",
            "We accept.\x02\x03",
            "#00000FSo, about the flow\x01",
            "of the city tour...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 6)), scpexpr(EXPR_END)), "loc_3050")

    ChrTalk(
        0x8,
        (
            "#11P#03200FAh, please inquire Lord \x01",
            "Shing directly about that.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x2)

    ChrTalk(
        0x8,
        (
            "#11P#03209FWell then, Lord Shing.\x01",
            "Please be careful and have a nice trip.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "#6PYeah, got it!\x02",
    )

    CloseMessageWindow()

    def lambda_2EF7():

        label("loc_2EF7")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_2EF7")

    QueueWorkItem2(0x101, 1, lambda_2EF7)
    Sleep(50)

    def lambda_2F0C():

        label("loc_2F0C")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_2F0C")

    QueueWorkItem2(0x102, 1, lambda_2F0C)
    Sleep(50)

    def lambda_2F21():

        label("loc_2F21")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_2F21")

    QueueWorkItem2(0x104, 1, lambda_2F21)
    Sleep(50)

    def lambda_2F36():

        label("loc_2F36")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_2F36")

    QueueWorkItem2(0x109, 1, lambda_2F36)
    Sleep(50)

    def lambda_2F4B():

        label("loc_2F4B")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_2F4B")

    QueueWorkItem2(0x105, 1, lambda_2F4B)
    OP_95(0x1A2, 4900, 0, 2510, 2000, 0x0)
    OP_68(3060, 1100, -70, 2000)
    MoveCamera(52, 19, 0, 2000)
    OP_6E(380, 2000)
    SetCameraDistance(22270, 2000)
    SetChrSubChip(0x8, 0x0)
    OP_95(0x1A2, 2800, 0, 2150, 2000, 0x0)

    def lambda_2FB7():
        OP_95(0xFE, 2300, 0, 470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_2FB7)
    OP_93(0x101, 0x5A, 0x0)
    OP_93(0x104, 0x5A, 0x0)
    OP_93(0x109, 0x5A, 0x0)

    def lambda_2FE6():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2FE6)

    def lambda_2FFB():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2FFB)

    def lambda_3010():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3010)

    def lambda_3025():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3025)
    WaitChrThread(0x101, 1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    OP_6F(0x79)
    Jump("loc_30F1")

    label("loc_3050")


    ChrTalk(
        0x8,
        (
            "#11P#03200FAh, please inquire Lord \x01",
            "Shing directly about that.\x02\x03",
            "#03209FWell then, Lord Shing.\x01",
            "Please be careful and have a nice trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "#6PYeah, got it!\x02",
    )

    CloseMessageWindow()

    label("loc_30F1")

    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#5P──Come now, miss,\x01",
            "let's go at once!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_312E():
        OP_95(0xFE, 1310, 0, -400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_312E)

    def lambda_3148():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3148)

    def lambda_3155():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3155)

    def lambda_3162():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3162)
    WaitChrThread(0x109, 1)

    def lambda_3173():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3173)

    def lambda_3188():
        OP_9B(0x1, 0xFE, 0xB4, 0x320, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3188)

    def lambda_319D():
        OP_9B(0x1, 0xFE, 0xB4, 0x320, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_319D)
    OP_68(930, 1100, -390, 1500)
    WaitChrThread(0x109, 1)

    def lambda_31C7():

        label("loc_31C7")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_31C7")

    QueueWorkItem2(0x101, 1, lambda_31C7)
    Sleep(50)

    def lambda_31DC():

        label("loc_31DC")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_31DC")

    QueueWorkItem2(0x104, 1, lambda_31DC)
    Sleep(50)

    def lambda_31F1():

        label("loc_31F1")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_31F1")

    QueueWorkItem2(0x109, 1, lambda_31F1)
    Sleep(50)

    def lambda_3206():

        label("loc_3206")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_3206")

    QueueWorkItem2(0x105, 1, lambda_3206)

    def lambda_3218():
        OP_97(0xFE, 0xFFFFFA24, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_3218)

    def lambda_3232():
        OP_97(0xFE, 0xFFFFFA24, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3232)
    WaitChrThread(0x102, 1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    OP_6F(0x1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#11P#00105FW-Wait, Shing...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00005FUhhm, don't tell me you're thinking\x01",
            "to go around the city you two alone?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#12PEeh, but moving around\x01",
            "in a group is annoying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PAlso, I prefer to\x01",
            "be alone with her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00001FUhhm, even so...\x02\x03",
            "#00003F(I think he won't be targeted just\x01",
            "because he's an elder's grandson, but...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00103F...*cough*.\x02\x03",
            "#00100FShing, we're now before the Trade Conference.\x01",
            "We honestly don't know what could happen.\x02\x03",
            "#00104FThinking about your safety, don't you think\x01",
            "it would be better to have bodyguards?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#6PUuh, I think that if you say so,\x01",
            "then it can't be helped.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#12PThen, bring another two.\x01",
            "And see that you protect us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PAs for the remaining two...let's see...\x01",
            "They should watch over us maintaining\x01",
            "a reasonable distance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "#12PWhat about that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00005FEeh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00303F...He unintentionally said something right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10100FYes, that's an effective arrangement for\x01",
            "the bodyguards of an important person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#11P#10300FHu hu, then it's decided.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#11P#10300FOne of the bodyguards is you,\x01",
            "but who will be the other one?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00003FRight...\x02",
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
            "[Have Randy Accompany You]\x01",      # 0
            "[Have Noｱl Accompany You]\x01",      # 1
            "[Have Wazy Accompany You]\x01",       # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3838"),
        (1, "loc_39A5"),
        (2, "loc_3B1F"),
        (SWITCH_DEFAULT, "loc_3C83"),
    )


    label("loc_3838")

    SetScenarioFlags(0x1C4, 6)
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00000FThen, Randy.\x01",
            "Can you come with us?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#6P#00300FYeah, got it.\x02\x03",
            "#00304FThen let's get moderately fired up and\x01",
            "go on our guide & escort mission.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00000FAs for the others, like he said,\x01",
            "follow us from behind while\x01",
            "seeing the situation.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        "#6P#10100FUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10300FHu hu, roger.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C83")

    label("loc_39A5")

    SetScenarioFlags(0x1C4, 7)
    TurnDirection(0x101, 0x109, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00000FThen, Noｱl.\x01",
            "Can you come with us?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#6P#10100FYes, understood.\x02\x03",
            "#10101FLet's escort him properly without letting\x01",
            "our guards down even if it's sightseeing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00000FAs for the others, like he said,\x01",
            "follow us from behind while\x01",
            "seeing the situation.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        "#6P#00300FYeah, leave it to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10300FHu hu, roger.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C83")

    label("loc_3B1F")

    SetScenarioFlags(0x1C5, 0)
    TurnDirection(0x101, 0x105, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#00000FThen, Wazy.\x01",
            "Can you come with us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHu hu, roger.\x02\x03",
            "#10302FIn this case, I'll keep you\x01",
            "company until the end.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00000FAs for the others, like he said,\x01",
            "follow us from behind while\x01",
            "seeing the situation.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3C28():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3C28)
    Sleep(50)

    def lambda_3C38():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3C38)
    Sleep(300)

    ChrTalk(
        0x104,
        "#6P#00300FYeah, leave it to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10100FRoger.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C83")

    label("loc_3C83")

    TurnDirection(0x101, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#00000F...Well then.\x01",
            "Are you fine with this, Shing?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3CCE():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3CCE)
    Sleep(50)

    def lambda_3CDE():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3CDE)
    Sleep(50)

    def lambda_3CEE():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3CEE)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "#12PYeah, I'm good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PAlso, no formalities among us.\x01",
            "You aren't Heiyue members, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00009FHa ha, got it, Shing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PAlright!\x01",
            "Then, let's go out quick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PI'll tell you in detail the places\x01",
            "I want to go to when we'll be outside!\x02",
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
            "Quest [Showing Shing Around The City]\x07\x00",
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
    SetScenarioFlags(0x1C5, 1)
    OP_29(0x73, 0x1, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 900, 0, 50, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_71(0x3, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x3)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 5800, 0, -1460, 270)
    BeginChrThread(0x9, 0, 0, 0)
    ClearChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x80)
    EventEnd(0x5)
    Return()

    # Function_11_2DDD end

    def Function_12_3EDF(): pass

    label("Function_12_3EDF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31400.itc", 0x1E)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 3420, 0, 3170, 180)
    OP_68(3470, 1000, -250, 0)
    MoveCamera(44, 20, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x1A2, 5800, 0, 1300, 180)
    SetChrPos(0x101, 2300, 0, 470, 90)
    SetChrPos(0x102, 2130, 0, -650, 90)
    SetChrPos(0x104, 1020, 0, 1050, 90)
    SetChrPos(0x109, 810, 0, -120, 90)
    SetChrPos(0x105, 1030, 0, -1210, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrSubChip(0x8, 0x2)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#11P#03204F#N──Hu hu, I'm glad\x01",
            "you had fun.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(1000, 0)
    OP_0D()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 2)), scpexpr(EXPR_END)), "loc_402C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_402C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 4)), scpexpr(EXPR_END)), "loc_403F")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_403F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_END)), "loc_4052")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_END)), "loc_4065")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4065")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 1)), scpexpr(EXPR_END)), "loc_4078")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4078")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 0)), scpexpr(EXPR_END)), "loc_408B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_408B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 5)), scpexpr(EXPR_END)), "loc_409E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_409E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 5)), scpexpr(EXPR_END)), "loc_40B1")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_40B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 0)), scpexpr(EXPR_END)), "loc_40C4")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_40C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_41A6")

    ChrTalk(
        0x1A2,
        "#5PYeah, it was really worthwhile!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#5PCrossbell is not only the \x01",
            "Arc-en-ciel and the theme park!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#5PI feel I understand too the reason why a shrewd\x01",
            "businessman like you is peculiar about it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42BB")

    label("loc_41A6")


    ChrTalk(
        0x1A2,
        "#5PYeah, it was really worthwhile!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#5PActually, there were some other\x01",
            "places I wanted to see, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#5PCrossbell is not only the \x01",
            "Arc-en-ciel and the theme park!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#5PI feel I understand too the reason why a shrewd\x01",
            "businessman like you is peculiar about it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42BB")


    ChrTalk(
        0x8,
        "#11P#03200FHa ha, why thank you.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#11P#03200FMr. Lloyd, Miss Elie\x01",
            "and you all.\x02\x03",
            "#03209FI would have never imagined that\x01",
            "Lord Shing could be this happy.\x02\x03",
            "#03204FThank you very much,\x01",
            "you were of great help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FNo, don't mention it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00102F*giggle*, we had \x01",
            "a good time too.\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x9, 2580, 0, 1630, 2000, 0x0)

    def lambda_440F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_440F)
    Sleep(50)

    def lambda_441F():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_441F)
    Sleep(50)

    def lambda_442F():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_442F)
    Sleep(50)

    def lambda_443F():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_443F)
    Sleep(50)

    def lambda_444F():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_444F)
    Sleep(50)

    def lambda_445F():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_445F)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "──It is nothing much,\x01",
            "but please accept this.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00003FAh, since we're policemen\x01",
            "we can't accept such a──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#03204FHu hu, thinking you would've said that,\x01",
            "I refrained to reward you with mira.\x02\x03",
            "#03210FCould you accept it as a\x01",
            "token of friendship with\x01",
            "Lord Shing, not with us?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_460E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_460E)
    Sleep(50)

    def lambda_461E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_461E)
    Sleep(50)

    def lambda_462E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_462E)
    Sleep(50)

    def lambda_463E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_463E)
    Sleep(50)

    def lambda_464E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_464E)
    Sleep(300)

    ChrTalk(
        0x101,
        "#6P#00011FUh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FWell...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "#5PCao, how thoughtful of you!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#11PYes, yes, no need to be reserved!\x01",
            "Take it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00306F(Pushy...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302F(Hu hu, if he says it in that way,\x01",
            "we can only accept it.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10106F(I-Indeed.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001F...All right.\x01",
            "As long as it's not mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FWe accept it with gratitude.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 500)
    Sleep(300)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4840")
    OP_29(0x73, 0x1, 0xD)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x53),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x53, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_488F")

    label("loc_4840")

    OP_29(0x73, 0x1, 0xE)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x47),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x47, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_488F")

    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#6P#00000FThen, we will\x01",
            "excuse us here.\x02\x03",
            "#00009F──Shing, see you, ok?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        "#6P#00109F*giggle*, be well.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "#11PYeah, miss and you all too, be safe and sound!\x02",
    )

    CloseMessageWindow()

    def lambda_4959():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4959)
    Sleep(100)

    def lambda_4969():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4969)
    Sleep(100)

    def lambda_4979():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4979)
    Sleep(100)

    def lambda_4989():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4989)
    Sleep(100)

    def lambda_4999():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4999)
    WaitChrThread(0x104, 1)

    def lambda_49AA():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_49AA)
    WaitChrThread(0x109, 1)

    def lambda_49C8():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_49C8)
    WaitChrThread(0x105, 1)

    def lambda_49E6():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_49E6)
    WaitChrThread(0x101, 1)

    def lambda_4A04():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4A04)
    WaitChrThread(0x102, 1)

    def lambda_4A22():
        OP_97(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4A22)

    def lambda_4A3C():

        label("loc_4A3C")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_4A3C")

    QueueWorkItem2(0x9, 1, lambda_4A3C)
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)
    OP_68(4059, 1100, 340, 4000)
    MoveCamera(41, 23, 0, 4000)
    OP_6E(380, 4000)
    SetCameraDistance(21210, 4000)
    BeginChrThread(0xC, 1, 0, 13)
    OP_63(0x1A2, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    WaitChrThread(0x102, 1)
    Sleep(2000)
    OP_64(0xFFFF)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    EndChrThread(0x9, 0x1)

    ChrTalk(
        0x1A2,
        "............\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x2)

    def lambda_4ADB():

        label("loc_4ADB")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_4ADB")

    QueueWorkItem2(0x9, 1, lambda_4ADB)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#11P#03200FHu hu, it seems you are tired by\x01",
            "having walked around the city.\x02\x03",
            "#03204FWe prepared some rare pastries\x01",
            "in your room, you know?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x1A2, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#5PI-I see.\x01",
            "You really are thoughtful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#5PYes, yes, I'll properly\x01",
            "report it to grandfather.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(4950, 1100, 3350, 3000)
    OP_95(0x1A2, 5000, 0, 5850, 2000, 0x0)
    OP_6F(0x1)
    Sound(103, 0, 100, 0)
    OP_71(0x3, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x3)
    Sleep(500)

    def lambda_4C43():
        OP_97(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_4C43)
    Sleep(500)

    def lambda_4C60():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_4C60)
    Sleep(500)
    Sound(104, 0, 100, 0)
    OP_71(0x3, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x3)
    Sleep(500)
    OP_6F(0x1)
    EndChrThread(0x9, 0x1)
    OP_68(5090, 1100, 880, 3000)
    OP_6F(0x1)

    ChrTalk(
        0x8,
        (
            "#11P#03204FHu hu, although young, he made us see\x01",
            "a glimpse of his wisdom and talent.\x02\x03",
            "#03202FWill he be useful to me in the future...?\x01",
            "I can't hardly wait.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x9,
        "#6P...Yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PStill, in that case, didn't we\x01",
            "overdo it in this matter...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PIn the remote event "they" targeted\x01",
            "Lord Shing, you would have been\x01",
            "held responsible too, Master Cao...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)

    ChrTalk(
        0x8,
        (
            "#11P#03200FHu hu, in that case it would have only meant that\x01",
            "his and mine destiny only amounted to that much.\x02\x03",
            "#03204FAlso, "they" wouldn't be that foolish to make\x01",
            "something happen at this point in time, no?\x02\x03",
            "#03201FSo── Have there been any movements?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PYes, we captured two targets who were\x01",
            "tailing Lord Shing and the others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6PWe are observing them at present.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#03204FVery good. Please let them\x01",
            "go free without noticing.\x02\x03",
            "#03200FAnd be very careful that the people\x01",
            "of the "company" don't interfere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6PCertainly.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Showing Shing Around The City]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x1000)
    OP_49()
    OP_D7(0x1E)
    RemoveParty(0xA1, 0xFF)
    OP_29(0x73, 0x4, 0x10)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_50CC")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_50F5")

    label("loc_50CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_50E3")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_50F5")

    label("loc_50E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_50F5")
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_50F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_510E")
    OP_2C(0x73, 0x3)
    Jump("loc_517C")

    label("loc_510E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_513B")
    OP_2C(0x73, 0x2)
    Jump("loc_517C")

    label("loc_513B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5168")
    OP_2C(0x73, 0x1)
    Jump("loc_517C")

    label("loc_5168")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_517C")
    OP_2C(0x73, 0x0)

    label("loc_517C")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    StopBGM(0xFA0)
    WaitBGM()
    EventEnd(0x5)
    SetScenarioFlags(0x22, 6)
    NewScene("c1200", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_12_3EDF end

    def Function_13_51A5(): pass

    label("Function_13_51A5")

    Sleep(1300)
    Sound(103, 0, 100, 0)
    Sleep(2000)
    Sound(104, 0, 100, 0)
    Return()

    # Function_13_51A5 end

    def Function_14_51B8(): pass

    label("Function_14_51B8")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The gate is firmly shut.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_14_51B8 end

    SaveToFile()

Try(main)
