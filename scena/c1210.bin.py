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
        "Function_4_502",          # 04, 4
        "Function_5_5AA",          # 05, 5
        "Function_6_69B",          # 06, 6
        "Function_7_7D8",          # 07, 7
        "Function_8_D55",          # 08, 8
        "Function_9_28A4",         # 09, 9
        "Function_10_29B7",        # 0A, 10
        "Function_11_2CAE",        # 0B, 11
        "Function_12_3C59",        # 0C, 12
        "Function_13_4EFC",        # 0D, 13
        "Function_14_4F0F",        # 0E, 14
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
    Jump("loc_4FE")

    label("loc_48A")


    ChrTalk(
        0x8,
        (
            "#03200FNevertheless, it was\x01",
            "really fortuitous that\x01",
            "you all came.\x02\x03",
            "#03204FPlease, take good care\x01",
            "of Lord Shing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FE")

    TalkEnd(0x8)
    Return()

    # Function_3_45A end

    def Function_4_502(): pass

    label("Function_4_502")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_532")
    Call(0, 9)
    Jump("loc_5A6")

    label("loc_532")


    ChrTalk(
        0x8,
        (
            "#03200FNevertheless, it was\x01",
            "really fortuitous that\x01",
            "you all came.\x02\x03",
            "#03204FPlease, take good care\x01",
            "of Lord Shing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A6")

    TalkEnd(0x8)
    Return()

    # Function_4_502 end

    def Function_5_5AA(): pass

    label("Function_5_5AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_65E")

    ChrTalk(
        0x9,
        (
            "If you decide you would\x01",
            "like to accept, please\x01",
            "return quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There is a limit to how\x01",
            "long both we and Lord\x01",
            "Shing can wait.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_697")

    label("loc_65E")


    ChrTalk(
        0x9,
        (
            "Lord Shing, please be\x01",
            "careful and have a nice\x01",
            "tour.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_697")

    TalkEnd(0xFE)
    Return()

    # Function_5_5AA end

    def Function_6_69B(): pass

    label("Function_6_69B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D4")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_767")

    ChrTalk(
        0xA,
        (
            "Miss, I'll be waiting\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Please, you have to come\x01",
            "back for me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FUmm, I can't promise you\x01",
            "that, but... I'll see\x01",
            "what I can do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D4")

    label("loc_767")


    ChrTalk(
        0xA,
        (
            "I don't care what you\x01",
            "have to do, just finish\x01",
            "it and come back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I won't forgive you if\x01",
            "you refuse!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D4")

    TalkEnd(0xFE)
    Return()

    # Function_6_69B end

    def Function_7_7D8(): pass

    label("Function_7_7D8")

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
            "#03204F─Oh, what an interesting\x01",
            "coincidence.\x02\x03",
            "#03210FConsidering the Schwarz\x01",
            "Auction, it seems they\x01",
            "really are connected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PBut Master Cao...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PJust what is on the\x01",
            "south side of Elm Lake?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03204FWell, we must rely on "his"\x01",
            "intuition in this case.\x02\x03",
            "#03200FThe Snake that demonized the\x01",
            "delinquent leader, and the\x01",
            "Church that intervened...\x02\x03",
            "I don't think it's anything\x01",
            "more than eliminating a few\x01",
            "blind spots, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PIndeed.\x02",
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
        "─E-Excuse me!\x02",
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

    def lambda_B9E():
        OP_96(0xFE, 0x8FC, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_B9E)

    def lambda_BB8():

        label("loc_BB8")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_BB8")

    QueueWorkItem2(0x8, 2, lambda_BB8)
    Sleep(50)

    def lambda_BCD():

        label("loc_BCD")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_BCD")

    QueueWorkItem2(0x9, 2, lambda_BCD)

    def lambda_BDF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_BDF)
    WaitChrThread(0xB, 1)
    EndChrThread(0x8, 0x2)
    EndChrThread(0x9, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x9,
        "#11PFan!? Are you ok!?\x02",
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
            "#6PYou see... A moment ago I\x01",
            "received an unbelievable report\x01",
            "from our surveillance team.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAn unbelievable\x01",
            "report...?\x02",
        )
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
            "#03201F─Fan. Please tell us the\x01",
            "details.\x02",
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

    # Function_7_7D8 end

    def Function_8_D55(): pass

    label("Function_8_D55")

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
            "#11P#03200FWonderful! You're all\x01",
            "here.\x02\x03",
            "#03209FWelcome to Heiyue\x01",
            "Trading Company. Allow\x01",
            "me to welcome you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00001F...Please excuse us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FAllow us to take you up\x01",
            "on your offer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#03200F...Long time no see,\x01",
            "Randy.\x02\x03",
            "#03204FI've been looking\x01",
            "forward to your return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303F...Nice to see you too.\x01",
            "You're the same as ever,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#03204FHaha. I'll take that as\x01",
            "a compliment.\x02\x03",
            "#03209FOh, but to think Randy\x01",
            "was connected to that\x01",
            "Crimson & Co.\x02\x03",
            "Even I was caught off\x01",
            "guard by this.\x02",
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
            "#6P#00001FIt looks like you have\x01",
            "some intel on them, am I\x01",
            "wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#03204FActually, we're more\x01",
            "than a little connected.\x02\x03",
            "#03200FPerhaps Randy here could\x01",
            "shed some light on our\x01",
            "new friends?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303FYeah... I know that my uncle\x01",
            "led some fights against\x01",
            "Heiyue about a year ago.\x02\x03",
            "#00301FIt was quite the full-blown\x01",
            "conflict, from what I heard.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_122D")

    ChrTalk(
        0x101,
        "#6P#00003F...Sounds about right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108FDudley mentioned\x01",
            "something like that...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_128A")

    label("loc_122D")


    ChrTalk(
        0x102,
        "#6P#00105FCome to think of it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FDudley mentioned\x01",
            "something like that...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_128A")


    ChrTalk(
        0x8,
        (
            "#11P#03204FHaha. Well they're certainly\x01",
            "doing well for themselves.\x02\x03",
            "#03200FLuckily, since we made a deal,\x01",
            "neither side bears any further\x01",
            "grudge.\x02\x03",
            "#03209FThough among the Heiyue\x01",
            "elders, there are some who get\x01",
            "angry just hearing the name.\x02",
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
        "#6P#10106FS-Still, huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FA lot must've happened\x01",
            "between you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#03203FWell regarding the old Revache\x01",
            "building, it's a pity, but we\x01",
            "had to give up on it.\x02\x03",
            "#03200FUnlike Revache, a mafia\x01",
            "organization, we have few direct\x01",
            "competitors in our business...\x02\x03",
            "#03210FYou can rest assured in that\x01",
            "regard, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F...How kind of you. (I\x01",
            "can't completely believe\x01",
            "him, though...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FUm, sorry to interrupt,\x01",
            "but you said you had a\x01",
            ""request"?\x02\x03",
            "#00103FSurely it has something\x01",
            "to do with Crimson & Co.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Oh, actually─\x02",
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
            "#5P#NYou're slow, Cao! What\x01",
            "the heck are you doing!?\x02",
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

    def lambda_1738():

        label("loc_1738")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_1738")

    QueueWorkItem2(0x101, 1, lambda_1738)
    Sleep(50)

    def lambda_174D():

        label("loc_174D")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_174D")

    QueueWorkItem2(0x102, 1, lambda_174D)
    Sleep(50)

    def lambda_1762():

        label("loc_1762")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_1762")

    QueueWorkItem2(0x104, 1, lambda_1762)
    Sleep(50)

    def lambda_1777():

        label("loc_1777")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_1777")

    QueueWorkItem2(0x109, 1, lambda_1777)
    Sleep(50)

    def lambda_178C():

        label("loc_178C")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_178C")

    QueueWorkItem2(0x105, 1, lambda_178C)
    Sleep(50)

    def lambda_17A1():

        label("loc_17A1")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_17A1")

    QueueWorkItem2(0x9, 1, lambda_17A1)
    Sleep(300)
    OP_68(4460, 1100, 100, 3000)

    def lambda_17C7():
        OP_95(0xFE, 5800, 0, 1300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_17C7)
    Sleep(100)

    def lambda_17E4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_17E4)
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
        (
            "#11P#03200FOh, if it isn't Lord\x01",
            "Shing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Is something troubling\x01",
            "you?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1A2,
        "Boy",
        (
            "What's troubling me is\x01",
            "how long you're making\x01",
            "me wait!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1A2,
        "Boy",
        (
            "When is the guide\x01",
            "coming!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, if you don't mind,\x01",
            "I'll be your gui─\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1A2,
        "Boy",
        (
            "Shut up you! How many\x01",
            "times do I have to tell\x01",
            "you!?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1A2,
        "Boy",
        (
            "It's my long-awaited visit to\x01",
            "Crossbell! Being guided by someone\x01",
            "like you would just ruin it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#03209FHaha. Don't worry, I've\x01",
            "arranged something for\x01",
            "you.\x02\x03",
            "#03204FThey will guide you.\x02",
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

    def lambda_1AA2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1AA2)
    Sleep(50)

    def lambda_1AB2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1AB2)
    Sleep(50)

    def lambda_1AC2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1AC2)
    Sleep(50)

    def lambda_1AD2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1AD2)
    Sleep(50)

    def lambda_1AE2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1AE2)
    Sleep(300)

    ChrTalk(
        0x101,
        "#6P#00005FU-Uh, Cao?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105F...Could this be the\x01",
            ""request"?\x02",
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
            "#11P#03200FLet me properly\x01",
            "introduce you.\x02\x03",
            "#03204FThis is Lord Shing, a\x01",
            "certain Heiyue elder's\x01",
            "grandson.\x02\x03",
            "#03209FWe want you to show Lord\x01",
            "Shing around Crossbell\x01",
            "City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00106FI-I knew it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00306FWhoa, seriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHaha. What an unexpected\x01",
            "request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#11PThese guys are my\x01",
            "guides? Aren't they just\x01",
            "a bunch of kids?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#11PCould you introduce me\x01",
            "to Ilya Platiere or\x01",
            "Dieter Crois?\x02",
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
            "#11P#03209FHaha. As you might\x01",
            "imagine, that would be\x01",
            "rather difficult...\x02\x03",
            "#03200FThey are quite the\x01",
            "celebrities themselves,\x01",
            "you know.\x02\x03",
            "#03204FAnd, they played a\x01",
            "leading role in the\x01",
            "resolution of that case.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "#11POh, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#11PSo you're the Special\x01",
            "Support Section that\x01",
            "solved the cult case, huh.\x02",
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

    def lambda_1F43():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F43)
    Sleep(50)

    def lambda_1F53():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1F53)
    Sleep(50)

    def lambda_1F63():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1F63)
    Sleep(50)

    def lambda_1F73():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1F73)
    Sleep(50)

    def lambda_1F83():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1F83)
    Sleep(300)

    ChrTalk(
        0x101,
        "#6P#00005FHuh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FW-Why do you know that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Being one of the elders'\x01",
            "grandsons, Lord Shing is a\x01",
            "very well-informed person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I heard he did quite a\x01",
            "bit of studying before\x01",
            "coming to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "#11PHehe, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#11PAs a proud grandson of the elder's, I have\x01",
            "to be knowledgeable and dependable, as the\x01",
            "future of Heiyue rests on my shoulders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#11PYou regular people\x01",
            "wouldn't understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00306F(This brat...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10102F(Now now, Randy.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#11PWell, if you insist,\x01",
            "I'll have to accept,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#11PI also want to ask you\x01",
            "about the Cult incident─\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "#11PHuh...\x02",
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

    def lambda_22D8():

        label("loc_22D8")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_22D8")

    QueueWorkItem2(0x101, 1, lambda_22D8)
    Sleep(50)

    def lambda_22ED():

        label("loc_22ED")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_22ED")

    QueueWorkItem2(0x102, 1, lambda_22ED)
    Sleep(50)

    def lambda_2302():

        label("loc_2302")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_2302")

    QueueWorkItem2(0x104, 1, lambda_2302)
    Sleep(50)

    def lambda_2317():

        label("loc_2317")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_2317")

    QueueWorkItem2(0x109, 1, lambda_2317)
    Sleep(50)

    def lambda_232C():

        label("loc_232C")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_232C")

    QueueWorkItem2(0x105, 1, lambda_232C)
    OP_95(0x1A2, 4900, 0, 2510, 2000, 0x0)
    TurnDirection(0x1A2, 0x102, 500)
    OP_63(0x1A2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "#11PTh-#400Wth-#400Wth....\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    ChrTalk(
        0x1A2,
        "#11P#5STHE WOMAN OF MY DREAMS!\x02",
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

    def lambda_2412():
        OP_95(0xFE, 2300, 0, 470, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_2412)
    OP_93(0x101, 0x5A, 0x0)
    OP_93(0x104, 0x5A, 0x0)
    OP_93(0x109, 0x5A, 0x0)

    def lambda_2441():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2441)

    def lambda_2456():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2456)

    def lambda_246B():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_246B)

    def lambda_2480():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2480)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    TurnDirection(0x101, 0x1A2, 500)

    ChrTalk(
        0x101,
        "#6P#00011FW-Wha...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105FHuh....\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "So beautiful! Glossy\x01",
            "pearl grey hair!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "And such wonderful\x01",
            "proportions too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "I-I've finally found my\x01",
            "dream girl!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Miss! Can I have your\x01",
            "name!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FUm... It's Elie. Elie\x01",
            "MacDowell.\x02\x03",
            "#00109FHehe, nice to meet you,\x01",
            "Shing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Elie... What a lovely\x01",
            "name!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "I know! I was destined\x01",
            "to meet you in\x01",
            "Crossbell!\x02",
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
        (
            "#6P#00005F(W-What do you even say\x01",
            "to that?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306F(Jeez, not only is he\x01",
            "impudent, he's a super\x01",
            "precocious brat.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10109F(Ahaha... You're so\x01",
            "popular, Elie.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "#6PCao, this is perfect!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PI want her to show me\x01",
            "around town!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#03204FHaha. Good to hear.\x02\x03",
            "#03209F─Well then, everyone.\x01",
            "Please take care of\x01",
            "Shing for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00011FW-Wait a minute!\x02\x03",
            "#00003F(Showing a Heiyue elder's\x01",
            "grandson around town... Should\x01",
            "we really do this now?)\x02",
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

    # Function_8_D55 end

    def Function_9_28A4(): pass

    label("Function_9_28A4")

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
            "#11P#03200FWell, Lloyd?\x02\x03",
            "Can I ask you to show\x01",
            "Shing around Crossbell?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 10)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_9_28A4 end

    def Function_10_29B7(): pass

    label("Function_10_29B7")

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
            "Accept\x01",                      # 0
            "Think about it for now\x01",      # 1
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
        (0, "loc_2A25"),
        (1, "loc_2A2D"),
        (SWITCH_DEFAULT, "loc_2C58"),
    )


    label("loc_2A25")

    Call(0, 11)
    Jump("loc_2C58")

    label("loc_2A2D")


    ChrTalk(
        0x101,
        (
            "#6P#00003FSorry. Our hands are\x01",
            "full at the moment...\x02",
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
            "#11PW-What did you say!? Are\x01",
            "you refusing ME!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00106FSorry, Shing. We can do\x01",
            "it once we finish our\x01",
            "other business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FUmm, is it all right if\x01",
            "we accept your offer\x01",
            "later?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#03204FYes, I have no problem\x01",
            "with that of course.\x02\x03",
            "#03200FIt's just, I can't keep\x01",
            "Lord Shing waiting much\x01",
            "longer, you see.\x02\x03",
            "Accordingly, please\x01",
            "return soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#11PI'll be waiting, so do\x01",
            "it fast!\x02",
        )
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
    Jump("loc_2C58")

    label("loc_2C58")

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

    # Function_10_29B7 end

    def Function_11_2CAE(): pass

    label("Function_11_2CAE")


    ChrTalk(
        0x101,
        (
            "#6P#00003FUnderstood. We accept.\x02\x03",
            "#00000FSo, how specifically\x01",
            "will this tour go?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 6)), scpexpr(EXPR_END)), "loc_2F07")

    ChrTalk(
        0x8,
        (
            "#11P#03200FPlease ask Lord Shing\x01",
            "directly for those\x01",
            "details.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x2)

    ChrTalk(
        0x8,
        (
            "#11P#03209FWell then, Lord Shing.\x01",
            "Enjoy your tour.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "#6PYeah, sure!\x02",
    )

    CloseMessageWindow()

    def lambda_2DAE():

        label("loc_2DAE")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_2DAE")

    QueueWorkItem2(0x101, 1, lambda_2DAE)
    Sleep(50)

    def lambda_2DC3():

        label("loc_2DC3")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_2DC3")

    QueueWorkItem2(0x102, 1, lambda_2DC3)
    Sleep(50)

    def lambda_2DD8():

        label("loc_2DD8")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_2DD8")

    QueueWorkItem2(0x104, 1, lambda_2DD8)
    Sleep(50)

    def lambda_2DED():

        label("loc_2DED")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_2DED")

    QueueWorkItem2(0x109, 1, lambda_2DED)
    Sleep(50)

    def lambda_2E02():

        label("loc_2E02")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_2E02")

    QueueWorkItem2(0x105, 1, lambda_2E02)
    OP_95(0x1A2, 4900, 0, 2510, 2000, 0x0)
    OP_68(3060, 1100, -70, 2000)
    MoveCamera(52, 19, 0, 2000)
    OP_6E(380, 2000)
    SetCameraDistance(22270, 2000)
    SetChrSubChip(0x8, 0x0)
    OP_95(0x1A2, 2800, 0, 2150, 2000, 0x0)

    def lambda_2E6E():
        OP_95(0xFE, 2300, 0, 470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_2E6E)
    OP_93(0x101, 0x5A, 0x0)
    OP_93(0x104, 0x5A, 0x0)
    OP_93(0x109, 0x5A, 0x0)

    def lambda_2E9D():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2E9D)

    def lambda_2EB2():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2EB2)

    def lambda_2EC7():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2EC7)

    def lambda_2EDC():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2EDC)
    WaitChrThread(0x101, 1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    OP_6F(0x79)
    Jump("loc_2F8D")

    label("loc_2F07")


    ChrTalk(
        0x8,
        (
            "#11P#03200FPlease ask Lord Shing\x01",
            "directly for those\x01",
            "details.\x02\x03",
            "#03209FWell then, Lord Shing.\x01",
            "Enjoy your tour.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "#6PYeah, sure!\x02",
    )

    CloseMessageWindow()

    label("loc_2F8D")

    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#5P─Ok miss, let's go\x01",
            "already!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2FC1():
        OP_95(0xFE, 1310, 0, -400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_2FC1)

    def lambda_2FDB():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2FDB)

    def lambda_2FE8():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2FE8)

    def lambda_2FF5():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2FF5)
    WaitChrThread(0x109, 1)

    def lambda_3006():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3006)

    def lambda_301B():
        OP_9B(0x1, 0xFE, 0xB4, 0x320, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_301B)

    def lambda_3030():
        OP_9B(0x1, 0xFE, 0xB4, 0x320, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3030)
    OP_68(930, 1100, -390, 1500)
    WaitChrThread(0x109, 1)

    def lambda_305A():

        label("loc_305A")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_305A")

    QueueWorkItem2(0x101, 1, lambda_305A)
    Sleep(50)

    def lambda_306F():

        label("loc_306F")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_306F")

    QueueWorkItem2(0x104, 1, lambda_306F)
    Sleep(50)

    def lambda_3084():

        label("loc_3084")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_3084")

    QueueWorkItem2(0x109, 1, lambda_3084)
    Sleep(50)

    def lambda_3099():

        label("loc_3099")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_3099")

    QueueWorkItem2(0x105, 1, lambda_3099)

    def lambda_30AB():
        OP_97(0xFE, 0xFFFFFA24, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_30AB)

    def lambda_30C5():
        OP_97(0xFE, 0xFFFFFA24, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_30C5)
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
        "#11P#00105FH-Hey, Shing!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00005FUm, you're going with\x01",
            "just the two of you?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#12PYup. Because large\x01",
            "groups are annoying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PBesides, I'm fine with\x01",
            "just the two of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00001FHmm. Well, if you say so.\x02\x03",
            "#00003F(I don't think he'll be\x01",
            "targeted just because he's\x01",
            "an elder's grandson, but...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00103F...Ahem.\x02\x03",
            "#00100FShing, the trade\x01",
            "conference is coming up.\x01",
            "So anything could happen.\x02\x03",
            "#00104FFor your safety, wouldn't\x01",
            "it be better if you had\x01",
            "guards with you?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "#6PUuh, if you say so.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#12PTwo more, then. You guys\x01",
            "protect us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PAnd regarding the other\x01",
            "two... Keep watch from a\x01",
            "reasonable distance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "#12PHow about that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00005FWow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00303F...I guess even a broken\x01",
            "orbal clock is right\x01",
            "twice a day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10100FYes, that's an effective\x01",
            "deployment for a VIP's\x01",
            "guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#11P#10300FHehe. It's decided then.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#11P#10300FAssuming you'll be one\x01",
            "of the guards, who will\x01",
            "be the other?\x02",
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
        (0, "loc_362C"),
        (1, "loc_377D"),
        (2, "loc_38D3"),
        (SWITCH_DEFAULT, "loc_3A18"),
    )


    label("loc_362C")

    SetScenarioFlags(0x1C4, 6)
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00000FThen, Randy? Can you\x01",
            "come with us?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#6P#00300FYeah, got it.\x02\x03",
            "#00304FAlright then. Let's get\x01",
            "fired up for our tour\x01",
            "and escort mission.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00000FThe other two will follow\x01",
            "behind and observe the\x01",
            "surroundings.\x02",
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
        "#12P#10300FHaha, roger.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A18")

    label("loc_377D")

    SetScenarioFlags(0x1C4, 7)
    TurnDirection(0x101, 0x109, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00000FNoｱl? Can you come with\x01",
            "us?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#6P#10100FYes, understood.\x02\x03",
            "#10101FThough it's just sightseeing,\x01",
            "let's not lose focus and\x01",
            "guard him properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00000FThe other two will follow\x01",
            "behind and observe the\x01",
            "surroundings.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        "#6P#00300FSure, leave it to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10300FHaha, roger.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A18")

    label("loc_38D3")

    SetScenarioFlags(0x1C5, 0)
    TurnDirection(0x101, 0x105, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#00000FWazy. Can you come with\x01",
            "us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHehe, roger.\x02\x03",
            "#10302FI guess I'll stick with\x01",
            "you 'til the end.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00000FThe other two will follow\x01",
            "behind and observe the\x01",
            "surroundings.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_39B8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_39B8)
    Sleep(50)

    def lambda_39C8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_39C8)
    Sleep(300)

    ChrTalk(
        0x104,
        "#6P#00300FSure, leave it to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10100FRoger that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A18")

    label("loc_3A18")

    TurnDirection(0x101, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#00000F...Now then. Master\x01",
            "Shing, are you ready?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3A60():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3A60)
    Sleep(50)

    def lambda_3A70():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3A70)
    Sleep(50)

    def lambda_3A80():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3A80)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "#12PYep, all set.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PAlso, you don't have to\x01",
            "be so formal. You guys\x01",
            "aren't Heiyue, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00009FHaha... Got it, Shing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12POkay! Let's get a move\x01",
            "on already!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PI'll explain the details\x01",
            "of where I want to go\x01",
            "outside!\x02",
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
            "Quest [Showing Shing\x01",
            "Around]\x07\x00",
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

    # Function_11_2CAE end

    def Function_12_3C59(): pass

    label("Function_12_3C59")

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
            "#11P#03204F#N─Haha, I'm glad you had\x01",
            "a good time.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(1000, 0)
    OP_0D()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 2)), scpexpr(EXPR_END)), "loc_3DAB")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3DAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 4)), scpexpr(EXPR_END)), "loc_3DBE")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3DBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_END)), "loc_3DD1")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3DD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_END)), "loc_3DE4")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3DE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 1)), scpexpr(EXPR_END)), "loc_3DF7")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3DF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 0)), scpexpr(EXPR_END)), "loc_3E0A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3E0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 5)), scpexpr(EXPR_END)), "loc_3E1D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3E1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 5)), scpexpr(EXPR_END)), "loc_3E30")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3E30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 0)), scpexpr(EXPR_END)), "loc_3E43")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3E43")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3F1C")

    ChrTalk(
        0x1A2,
        (
            "#5PYeah, it was really\x01",
            "worthwhile!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#5PCrossbell isn't just\x01",
            "Arc-en-Ciel and the\x01",
            "theme park!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#5PI feel like I understand why\x01",
            "shrewd businessmen like yourself\x01",
            "make such a fuss over it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_401D")

    label("loc_3F1C")


    ChrTalk(
        0x1A2,
        (
            "#5PYeah, it was really\x01",
            "worthwhile!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#5PActually, I wanted to\x01",
            "see a few more places,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#5PCrossbell isn't just\x01",
            "Arc-en-Ciel and the\x01",
            "theme park!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#5PI feel like I understand why\x01",
            "shrewd businessmen like yourself\x01",
            "make such a fuss over it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_401D")


    ChrTalk(
        0x8,
        (
            "#11P#03200FHaha. Well color me\x01",
            "surprised.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#11P#03200FLloyd, Elie. And\x01",
            "everyone else, too.\x02\x03",
            "#03209FI would have never have\x01",
            "imagined Lord Shing\x01",
            "would be this pleased.\x02\x03",
            "#03204FThank you very much.\x01",
            "Excellent work,\x01",
            "everyone.\x02",
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
            "#6P#00102F*giggle*. We had a good\x01",
            "time as well.\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x9, 2580, 0, 1630, 2000, 0x0)

    def lambda_4184():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4184)
    Sleep(50)

    def lambda_4194():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4194)
    Sleep(50)

    def lambda_41A4():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_41A4)
    Sleep(50)

    def lambda_41B4():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_41B4)
    Sleep(50)

    def lambda_41C4():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_41C4)
    Sleep(50)

    def lambda_41D4():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_41D4)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "─It isn't much, but\x01",
            "please accept this.\x02",
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
            "#12P#00003FAh, since we're police\x01",
            "we can't accept such a─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#03204FHaha. I thought you might say\x01",
            "that, so I passed on giving\x01",
            "you mira.\x02\x03",
            "#03210FMight you be able to accept it\x01",
            "as a token of friendship? Not\x01",
            "with us, but with Lord Shing.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_437E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_437E)
    Sleep(50)

    def lambda_438E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_438E)
    Sleep(50)

    def lambda_439E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_439E)
    Sleep(50)

    def lambda_43AE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_43AE)
    Sleep(50)

    def lambda_43BE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_43BE)
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
        (
            "#5PCao, how thoughtful of\x01",
            "you!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#11PYes, yes, no need to\x01",
            "hold back! Take it!\x02",
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
            "#6P#10302F(Haha. If he says it like\x01",
            "that, then I guess we have\x01",
            "no choice but to accept it.)\x02",
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
            "#6P#00001F...All right. As long as\x01",
            "it's not mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FWe accept it with\x01",
            "gratitude.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 500)
    Sleep(300)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_45C5")
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
    Jump("loc_4614")

    label("loc_45C5")

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

    label("loc_4614")

    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#6P#00000FThen, we'll excuse\x01",
            "ourselves here.\x02\x03",
            "#00009F─See you again. Alright,\x01",
            "Shing?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        "#6P#00109F*giggle*. Be well.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#11PYeah. Take care,\x01",
            "everyone!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_46D8():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_46D8)
    Sleep(100)

    def lambda_46E8():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_46E8)
    Sleep(100)

    def lambda_46F8():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_46F8)
    Sleep(100)

    def lambda_4708():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4708)
    Sleep(100)

    def lambda_4718():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4718)
    WaitChrThread(0x104, 1)

    def lambda_4729():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4729)
    WaitChrThread(0x109, 1)

    def lambda_4747():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4747)
    WaitChrThread(0x105, 1)

    def lambda_4765():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4765)
    WaitChrThread(0x101, 1)

    def lambda_4783():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4783)
    WaitChrThread(0x102, 1)

    def lambda_47A1():
        OP_97(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_47A1)

    def lambda_47BB():

        label("loc_47BB")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_47BB")

    QueueWorkItem2(0x9, 1, lambda_47BB)
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

    def lambda_485A():

        label("loc_485A")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_485A")

    QueueWorkItem2(0x9, 1, lambda_485A)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#11P#03200FHaha. You seem tired\x01",
            "from all that walking\x01",
            "around.\x02\x03",
            "#03204FWe have some rare\x01",
            "pastries ready for you\x01",
            "in your room, you know.\x02",
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
            "#5PI-I see. You really are\x01",
            "thoughtful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#5PYes, yes, I'll be sure\x01",
            "to tell grandfather all\x01",
            "about it!\x02",
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

    def lambda_49C6():
        OP_97(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_49C6)
    Sleep(500)

    def lambda_49E3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_49E3)
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
            "#11P#03204FHaha. Though he is young, we\x01",
            "got a glimpse of his great\x01",
            "wisdom and talent today.\x02\x03",
            "#03202FWill he be useful to us in\x01",
            "the future? I can't wait to\x01",
            "find out.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x9,
        "#6P...Yes, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PBut if that's the case,\x01",
            "didn't we overdo it in\x01",
            "today's case?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PIn the unlikely event "they" targeted\x01",
            "Lord Shing, you would have been held\x01",
            "responsible too, Master Cao...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)

    ChrTalk(
        0x8,
        (
            "#11P#03200FHaha. In that case, it would have\x01",
            "meant only that his and my destinies\x01",
            "only amounted to that much.\x02\x03",
            "#03204FAnd, "they" aren't stupid enough to\x01",
            "start something with this timing,\x01",
            "I'm sure.\x02\x03",
            "#03201FSo─ Have there been any movements?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PYes. We detected two\x01",
            "targets tailing Lord\x01",
            "Shing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PWe are observing them at\x01",
            "present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#03204FVery good. Please let\x01",
            "them go so they don't\x01",
            "notice us.\x02\x03",
            "#03200FAnd take care not to let\x01",
            "that "company"\x01",
            "interfere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6PUnderstood.\x02",
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
            "Quest [Showing Shing\x01",
            "Around]\x07\x00",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_4E23")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_4E4C")

    label("loc_4E23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_4E3A")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_4E4C")

    label("loc_4E3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_4E4C")
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4E4C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4E65")
    OP_2C(0x73, 0x3)
    Jump("loc_4ED3")

    label("loc_4E65")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E92")
    OP_2C(0x73, 0x2)
    Jump("loc_4ED3")

    label("loc_4E92")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EBF")
    OP_2C(0x73, 0x1)
    Jump("loc_4ED3")

    label("loc_4EBF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_4ED3")
    OP_2C(0x73, 0x0)

    label("loc_4ED3")

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

    # Function_12_3C59 end

    def Function_13_4EFC(): pass

    label("Function_13_4EFC")

    Sleep(1300)
    Sound(103, 0, 100, 0)
    Sleep(2000)
    Sound(104, 0, 100, 0)
    Return()

    # Function_13_4EFC end

    def Function_14_4F0F(): pass

    label("Function_14_4F0F")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is firmly shut.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_14_4F0F end

    SaveToFile()

Try(main)
