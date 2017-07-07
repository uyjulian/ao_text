from ScenarioHelper import *

def main():
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
        "Tsao",                 # 1
        "Row",                   # 2
        "Singh",                   # 3
        "Black moon member",             # 4
        "SE control",                 # 5
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
        "Function_4_51B",          # 04, 4
        "Function_5_5DC",          # 05, 5
        "Function_6_6C2",          # 06, 6
        "Function_7_805",          # 07, 7
        "Function_8_D42",          # 08, 8
        "Function_9_28B7",         # 09, 9
        "Function_10_29D8",        # 0A, 10
        "Function_11_2C9E",        # 0B, 11
        "Function_12_3CBB",        # 0C, 12
        "Function_13_4EBB",        # 0D, 13
        "Function_14_4ECE",        # 0E, 14
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
    Jump("loc_517")

    label("loc_48A")


    ChrTalk(
        0x8,
        (
            "#03200FEven so,\x01",
            "Please come and see me\x01",
            "Really love you#4RCompetition#was.\x02\x03",
            "#03204FどうかSingh様のこと、\x01",
            "Thank you for your consideration.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_517")

    TalkEnd(0x8)
    Return()

    # Function_3_45A end

    def Function_4_51B(): pass

    label("Function_4_51B")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_54B")
    Call(0, 9)
    Jump("loc_5D8")

    label("loc_54B")


    ChrTalk(
        0x8,
        (
            "#03200FEven so,\x01",
            "Please come and see me\x01",
            "Really love you#4RCompetition#was.\x02\x03",
            "#03204FどうかSingh様のこと、\x01",
            "Thank you for your consideration.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D8")

    TalkEnd(0x8)
    Return()

    # Function_4_51B end

    def Function_5_5DC(): pass

    label("Function_5_5DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_687")

    ChrTalk(
        0x9,
        (
            "In the case of underwriting,\x01",
            "Please come back as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Singh様はもちろん、我々の待てる\x01",
            "Because time is limited, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BE")

    label("loc_687")


    ChrTalk(
        0x9,
        (
            "Singh様、どうかお気をつけて\x01",
            "Please do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BE")

    TalkEnd(0xFE)
    Return()

    # Function_5_5DC end

    def Function_6_6C2(): pass

    label("Function_6_6C2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_801")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_787")

    ChrTalk(
        0xA,
        (
            "older sister,\x01",
            "I will be waiting here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Please be sure to come back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FWell, I can not make a promise, but …\x01",
            "You let me do well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_801")

    label("loc_787")


    ChrTalk(
        0xA,
        (
            "I do not know anything about business,\x01",
            "You are done quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I do not want you to refuse\x01",
            "The choices are not forgiven!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_801")

    TalkEnd(0xFE)
    Return()

    # Function_6_6C2 end

    def Function_7_805(): pass

    label("Function_7_805")

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
            "#03204F── Aw, that's an interesting coincidence.\x02\x03",
            "#03210F\"Black auctioneer\" It is good\x01",
            "It seems that there is a border again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PしかしTsao様……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5POn the south coast of Elm Lake\x01",
            "What on earth are there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03204FWell, here is the intuition of \"him\"\x01",
            "There is no choice but to bet.\x02\x03",
            "#03200FTo devil a bad leader\x01",
            "Intervention of \"snakes\" and \"church\" … …\x02\x03",
            "To keep the blind spot down even a little\x01",
            "I have never done it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P……surely.\x02",
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
        "Voice of a man",
        "─ ─ Well, I will excuse you!\x02",
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

    def lambda_B80():
        OP_96(0xFE, 0x8FC, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_B80)

    def lambda_B9A():

        label("loc_B9A")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_B9A")

    QueueWorkItem2(0x8, 2, lambda_B9A)
    Sleep(50)

    def lambda_BAF():

        label("loc_BAF")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_BAF")

    QueueWorkItem2(0x9, 2, lambda_BAF)

    def lambda_BC1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_BC1)
    WaitChrThread(0xB, 1)
    EndChrThread(0x8, 0x2)
    EndChrThread(0x9, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x9,
        (
            "#11PWhat a fan!\x01",
            "Do not get distracted! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#6PI am sorry, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#6PThat … … from the monitoring team\x01",
            "Because there was a hard to believe report.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PUnbelievable report ……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#03205F…………………………………….\x02",
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
            "#03201F── Fans.\x01",
            "Please tell me a detailed story.\x02",
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

    # Function_7_805 end

    def Function_8_D42(): pass

    label("Function_8_D42")

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
            "#11P#03200FHello, are you?\x02\x03",
            "#03209FWelcome to \"Black Moon Trading Company\".\x01",
            "I will welcome you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00001F……Excuse me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FTo spare words\x01",
            "I got it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#03200FGiggle\x01",
            "Randy is also a long time.\x02\x03",
            "#03204FI was looking forward to returning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303F… … Hey, thanks.\x01",
            "You are as usual, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#03204FHaha, as a compliment\x01",
            "I will accept it.\x02\x03",
            "#03209FNo, but, Randy said\x01",
            "What is the official of Crimson Shokai?\x02\x03",
            "I was amazed as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00301FHan …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FApparently about \"them\"\x01",
            "You seem to know to some extent?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#03204FWell, actually it's a little,\x01",
            "It is not without rims.\x02\x03",
            "#03200FMaybe Randy\x01",
            "Do you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303FOh …… About a year ago,\x01",
            "Your uncle infiltrated the East Street Town\x01",
            "\"Black moon#4RYou#\"You heard that, did not you?\x02\x03",
            "#00301FFairly authentic Dokutachi\x01",
            "I heard that he did it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_121B")

    ChrTalk(
        0x101,
        "#6P#00003F… … That was right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108FMr. Dudley also said that\x01",
            "I was saying that … ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1272")

    label("loc_121B")


    ChrTalk(
        0x102,
        "#6P#00105Fby the way……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FMr. Dudley also said that\x01",
            "I was told …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1272")


    ChrTalk(
        0x8,
        (
            "#11P#03204FWell, well\x01",
            "Bustling#2RCurry#It is certain that he told me.\x02\x03",
            "#03200FFortunately, because it was hand-crafted\x01",
            "I have not left a grudge to each other … …\x02\x03",
            "#03209FAmong the elders of the black moon,\x01",
            "I still hear their name\x01",
            "Some people fainted too much due to anger.\x02",
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
        "#6P#10106FWell, until that … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FHuff, surely\x01",
            "I guess there were various things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#03203FWell, as for the site of Rubathe\x01",
            "I am sorry but I gave it up.\x02\x03",
            "#03200FUnlike Ruberculhe who was a mafia organization,\x01",
            "You can also confront directly with business\x01",
            "It will be less … ….\x02\x03",
            "#03210FOn that point\x01",
            "You may be safe, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F…… This is polite.\x01",
            "(I can not trust it at all, but …).\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FWell then,\x01",
            "What is \"What you want to ask\"?\x02\x03",
            "#00103FClearly the Crimson Shokai's\x01",
            "I thought about a case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Yes, in fact · · ·\x02",
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
        "Boys' Voices",
        (
            "#5P#Nおそいぞ、Tsao！\x01",
            "What on earth are you doing!\x02",
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

    def lambda_16EF():

        label("loc_16EF")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_16EF")

    QueueWorkItem2(0x101, 1, lambda_16EF)
    Sleep(50)

    def lambda_1704():

        label("loc_1704")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_1704")

    QueueWorkItem2(0x102, 1, lambda_1704)
    Sleep(50)

    def lambda_1719():

        label("loc_1719")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_1719")

    QueueWorkItem2(0x104, 1, lambda_1719)
    Sleep(50)

    def lambda_172E():

        label("loc_172E")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_172E")

    QueueWorkItem2(0x109, 1, lambda_172E)
    Sleep(50)

    def lambda_1743():

        label("loc_1743")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_1743")

    QueueWorkItem2(0x105, 1, lambda_1743)
    Sleep(50)

    def lambda_1758():

        label("loc_1758")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_1758")

    QueueWorkItem2(0x9, 1, lambda_1758)
    Sleep(300)
    OP_68(4460, 1100, 100, 3000)

    def lambda_177E():
        OP_95(0xFE, 5800, 0, 1300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_177E)
    Sleep(100)

    def lambda_179B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_179B)
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
        "#11P#03200Fおお、これはSingh様。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Did you have any inconvenience?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1A2,
        "boy",
        (
            "Any inconvenience,\x01",
            "I am going to keep you waiting!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1A2,
        "boy",
        (
            "When you become a guideman\x01",
            "I'm going to bring them! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "So, if I can be with you\x01",
            "Any number of guides ----\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1A2,
        "boy",
        "No, do not let it go over!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1A2,
        "boy",
        (
            "I came to visit Crossbell as much as I can\x01",
            "Your guidance will be fun! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#03209FBecause he is told so\x01",
            "I made arrangements according to this.\x02\x03",
            "#03204F\"They\" will be the guide.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1A2,
        "boy",
        "what……?\x02",
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

    def lambda_1A55():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A55)
    Sleep(50)

    def lambda_1A65():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1A65)
    Sleep(50)

    def lambda_1A75():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1A75)
    Sleep(50)

    def lambda_1A85():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1A85)
    Sleep(50)

    def lambda_1A95():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1A95)
    Sleep(300)

    ChrTalk(
        0x101,
        "#6P#00005Fあ、あの、Tsao支社長……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105FPossibly\x01",
            "\"What you want to ask\" ……\x02",
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
            "#11P#03200FI will introduce you.\x02\x03",
            "#03204FこちらはSingh様といいまして、\x01",
            "Elder who is a \"black moon\" monkey\x01",
            "You are a grandchild.\x02\x03",
            "#03209FBy all means,\x01",
            "Singh様にクロスベル市内を\x01",
            "I'd like you to show me around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00106FAnd after all …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00306FHey, are you serious?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10300FHuh, you ask Tadashi.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#11PThese guys ~ ~?\x01",
            "Is not it still waka?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#11PIria · Platier,\x01",
            "Dieter Crois or something,\x01",
            "Can not you bring them?\x02",
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
            "#11P#03209FHaha, as expected\x01",
            "It seems difficult, but …\x02\x03",
            "#03200FEven so,\x01",
            "Crossover is a celebrity?\x02\x03",
            "#03204FAnyway, I solved the case of the example\x01",
            "It is also a leading figure.\x02",
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
            "#11PYou settled the case incident\x01",
            "Is it \"a mission support section\"?\x02",
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

    def lambda_1F03():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F03)
    Sleep(50)

    def lambda_1F13():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1F13)
    Sleep(50)

    def lambda_1F23():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1F23)
    Sleep(50)

    def lambda_1F33():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1F33)
    Sleep(50)

    def lambda_1F43():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1F43)
    Sleep(300)

    ChrTalk(
        0x101,
        "#6P#00005FHuh……! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FWhy, why not ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Just the elder's grandchildren\x01",
            "Singh様はなかなかの情報通でして。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Before coming to the Crossbell\x01",
            "It seems that you have studied a whole line.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "#11PHuhun, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#11PAs the grandson of the old man who is the elder\x01",
            "I am the future of \"black moon\"\x01",
            "You are in a shoulder position.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#11PWhat are you guysock?\x01",
            "It is different from my mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00306F(This brat … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10102F(Somewhat, Randy seniors.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#11PWell, if you say absolutely\x01",
            "I do not have to admit it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#11PTalk about the case during a cult incident\x01",
            "You can ask me ─ ─\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "#11PHuh……\x02",
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
        "#6P#00005FIs it? Is it? Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FWhere are you?\x02",
    )

    CloseMessageWindow()

    def lambda_227E():

        label("loc_227E")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_227E")

    QueueWorkItem2(0x101, 1, lambda_227E)
    Sleep(50)

    def lambda_2293():

        label("loc_2293")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_2293")

    QueueWorkItem2(0x102, 1, lambda_2293)
    Sleep(50)

    def lambda_22A8():

        label("loc_22A8")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_22A8")

    QueueWorkItem2(0x104, 1, lambda_22A8)
    Sleep(50)

    def lambda_22BD():

        label("loc_22BD")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_22BD")

    QueueWorkItem2(0x109, 1, lambda_22BD)
    Sleep(50)

    def lambda_22D2():

        label("loc_22D2")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_22D2")

    QueueWorkItem2(0x105, 1, lambda_22D2)
    OP_95(0x1A2, 4900, 0, 2510, 2000, 0x0)
    TurnDirection(0x1A2, 0x102, 500)
    OP_63(0x1A2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "#11PCormorant#800WCormorant#800WWell …\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    ChrTalk(
        0x1A2,
        "#11P#5SA woman of destiny#4RPeople#It is …!\x02",
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

    def lambda_23BD():
        OP_95(0xFE, 2300, 0, 470, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_23BD)
    OP_93(0x101, 0x5A, 0x0)
    OP_93(0x104, 0x5A, 0x0)
    OP_93(0x109, 0x5A, 0x0)

    def lambda_23EC():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23EC)

    def lambda_2401():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2401)

    def lambda_2416():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2416)

    def lambda_242B():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_242B)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    TurnDirection(0x101, 0x1A2, 500)

    ChrTalk(
        0x101,
        "#6P#00011FWow …! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105FCash …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "A wonderful gaze!\x01",
            "Glossy pearl gray hair!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "And comprehensive\x01",
            "A wonderful proposal!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Here in my place\x01",
            "I can make it to the ideal human!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "older sister!\x01",
            "What is your name? Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FEr …\x01",
            "Ellie, McDael.\x02\x03",
            "#00109Fふふっ、よろしくね、Singh君。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Elly sister ……\x01",
            "…… The name is amazing …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "That's right, I am going to see this person\x01",
            "You came to crossbell … …!\x02",
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
        "#6P#00005F(What, what … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306F(It is not just cheeky\x01",
            "Is not it a solder masseaki? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10109F(Haha ……\x01",
            "Mr. Erie, Mote moto. )\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "#6PTsao、気にいったぞ！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PGet ready for this older sister\x01",
            "I will let you guide me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#03204FHuh, it looked like it.\x02\x03",
            "#03209F── Well then, everyone.\x01",
            "Singh様をよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00011FWait a moment, please!\x02\x03",
            "#00003F(An invitation from Elder Black Elm's grandchild … …\x01",
            "Can I accept as it is? )\x02",
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

    # Function_8_D42 end

    def Function_9_28B7(): pass

    label("Function_9_28B7")

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
            "#11P#03200FHow is Lloyd?\x02\x03",
            "Singh様のクロスベル案内を\x01",
            "May I ask you?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 10)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_9_28B7 end

    def Function_10_29D8(): pass

    label("Function_10_29D8")

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
            "Receive a request\x01",        # 0
            "I think once\x01",      # 1
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
        (0, "loc_2A44"),
        (1, "loc_2A4C"),
        (SWITCH_DEFAULT, "loc_2C48"),
    )


    label("loc_2A44")

    Call(0, 11)
    Jump("loc_2C48")

    label("loc_2A4C")


    ChrTalk(
        0x101,
        (
            "#6P#00003FExcuse me.\x01",
            "Now I can not take my hand …\x02",
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
            "#11PWhat, what …?\x01",
            "Are you refusing this guidance guide? Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00106Fごめんね、Singh君。\x01",
            "I wish I could clean up business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FWell, later again\x01",
            "May I accept the form as well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#03204FYes, of course.\x02\x03",
            "#03200Fただし、Singh様をあまり\x01",
            "I will not be able to keep you waiting.\x02\x03",
            "In that case, please return early.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "#11PI'll be waiting soon, I will!\x02",
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
    Jump("loc_2C48")

    label("loc_2C48")

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

    # Function_10_29D8 end

    def Function_11_2C9E(): pass

    label("Function_11_2C9E")


    ChrTalk(
        0x101,
        (
            "#6P#00003F……I understand.\x01",
            "Let's accept it.\x02\x03",
            "#00000FSo, concrete\x01",
            "Although it is the flow of city guidance ……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 6)), scpexpr(EXPR_END)), "loc_2F19")

    ChrTalk(
        0x8,
        (
            "#11P#03200FOh, that area\x01",
            "Singh様から直接お聞き下さい。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x2)

    ChrTalk(
        0x8,
        (
            "#11P#03209FそれではSingh様。\x01",
            "お気をつけてPlease do it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "#6POh, I understand!\x02",
    )

    CloseMessageWindow()

    def lambda_2DC0():

        label("loc_2DC0")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_2DC0")

    QueueWorkItem2(0x101, 1, lambda_2DC0)
    Sleep(50)

    def lambda_2DD5():

        label("loc_2DD5")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_2DD5")

    QueueWorkItem2(0x102, 1, lambda_2DD5)
    Sleep(50)

    def lambda_2DEA():

        label("loc_2DEA")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_2DEA")

    QueueWorkItem2(0x104, 1, lambda_2DEA)
    Sleep(50)

    def lambda_2DFF():

        label("loc_2DFF")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_2DFF")

    QueueWorkItem2(0x109, 1, lambda_2DFF)
    Sleep(50)

    def lambda_2E14():

        label("loc_2E14")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_2E14")

    QueueWorkItem2(0x105, 1, lambda_2E14)
    OP_95(0x1A2, 4900, 0, 2510, 2000, 0x0)
    OP_68(3060, 1100, -70, 2000)
    MoveCamera(52, 19, 0, 2000)
    OP_6E(380, 2000)
    SetCameraDistance(22270, 2000)
    SetChrSubChip(0x8, 0x0)
    OP_95(0x1A2, 2800, 0, 2150, 2000, 0x0)

    def lambda_2E80():
        OP_95(0xFE, 2300, 0, 470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_2E80)
    OP_93(0x101, 0x5A, 0x0)
    OP_93(0x104, 0x5A, 0x0)
    OP_93(0x109, 0x5A, 0x0)

    def lambda_2EAF():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2EAF)

    def lambda_2EC4():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2EC4)

    def lambda_2ED9():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2ED9)

    def lambda_2EEE():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2EEE)
    WaitChrThread(0x101, 1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    OP_6F(0x79)
    Jump("loc_2FAE")

    label("loc_2F19")


    ChrTalk(
        0x8,
        (
            "#11P#03200FOh, that area\x01",
            "Singh様から直接お聞き下さい。\x02\x03",
            "#03209FそれではSingh様。\x01",
            "お気をつけてPlease do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "#6POh, I understand!\x02",
    )

    CloseMessageWindow()

    label("loc_2FAE")

    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#5P──さあolder sister,\x01",
            "Let's go ahead!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2FEF():
        OP_95(0xFE, 1310, 0, -400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_2FEF)

    def lambda_3009():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3009)

    def lambda_3016():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3016)

    def lambda_3023():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3023)
    WaitChrThread(0x109, 1)

    def lambda_3034():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3034)

    def lambda_3049():
        OP_9B(0x1, 0xFE, 0xB4, 0x320, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3049)

    def lambda_305E():
        OP_9B(0x1, 0xFE, 0xB4, 0x320, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_305E)
    OP_68(930, 1100, -390, 1500)
    WaitChrThread(0x109, 1)

    def lambda_3088():

        label("loc_3088")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_3088")

    QueueWorkItem2(0x101, 1, lambda_3088)
    Sleep(50)

    def lambda_309D():

        label("loc_309D")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_309D")

    QueueWorkItem2(0x104, 1, lambda_309D)
    Sleep(50)

    def lambda_30B2():

        label("loc_30B2")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_30B2")

    QueueWorkItem2(0x109, 1, lambda_30B2)
    Sleep(50)

    def lambda_30C7():

        label("loc_30C7")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_30C7")

    QueueWorkItem2(0x105, 1, lambda_30C7)

    def lambda_30D9():
        OP_97(0xFE, 0xFFFFFA24, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_30D9)

    def lambda_30F3():
        OP_97(0xFE, 0xFFFFFA24, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_30F3)
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
        "#11P#00105Fちょ、ちょっとSingh君……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00005FWell, as it is\x01",
            "Are you going to go inside the city with two people?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#12PEh ~, because\x01",
            "It's uszzi to act.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PBesides, I am with sister\x01",
            "You should have two people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00001FWell, that's right.\x02\x03",
            "#00003F(Truly because the elders' grandchildren\x01",
            "I do not think I will be targeted … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00103F…… Kohon.\x02\x03",
            "#00100FSingh君、今は通商会議前だから\x01",
            "I do not know what it is.\x02\x03",
            "#00104FThinking about your safety\x01",
            "Do you think it would be better to have an escort?\x02",
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
            "#6PWell, my older sister\x01",
            "If it says so, why not?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#12PWell then, we have two more people.\x01",
            "So protect me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PTwo other people are …\x01",
            "With distance not far away\x01",
            "I wish I could watch over you.\x02",
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
        "#5P#00005FOh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00303F… … Do not chew on to what mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10100FYes, as a guardian\x01",
            "It is an effective arrangement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#11P#10300FHuh, it's a rule.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#11P#10300FAs one of your escorts,\x01",
            "Who is the other person?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00003FThat's right.\x02",
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
            "【Have the Randy accompany you】\x01",      # 0
            "【Have them accompany you to Noel】\x01",        # 1
            "【Have it accompanied by Waji】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_365B"),
        (1, "loc_37C3"),
        (2, "loc_3921"),
        (SWITCH_DEFAULT, "loc_3A84"),
    )


    label("loc_365B")

    SetScenarioFlags(0x1C4, 6)
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00000FWell then, Randy.\x01",
            "Can you come with me?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#6P#00300FOkay, okay.\x02\x03",
            "#00304FSoba, put in moderate spirit\x01",
            "Let's go with the guidance & escort mission.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00000FThe latter two, as he says,\x01",
            "Look at the situation#2RUkaga#While there\x01",
            "Follow me from behind.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        "#6P#10100FI understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10300FHuh, I understand.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A84")

    label("loc_37C3")

    SetScenarioFlags(0x1C4, 7)
    TurnDirection(0x101, 0x109, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00000FWell then, Noel.\x01",
            "Will you come with us?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#6P#10100FYes, I understand.\x02\x03",
            "#10101FBecause I am sightseeing, I must be careful\x01",
            "Let's escort firmly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00000FThe latter two, as he says,\x01",
            "Look at the situation#2RUkaga#While there\x01",
            "Follow me from behind.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        "#6P#00300FOh yeah, leave it to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10300FHuh, I understand.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A84")

    label("loc_3921")

    SetScenarioFlags(0x1C5, 0)
    TurnDirection(0x101, 0x105, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#00000FWell then, Wadi.\x01",
            "May I come with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHuh, I understand.\x02\x03",
            "#10302FIf so, thoroughly\x01",
            "Let's associate.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00000FThe latter two, as he says,\x01",
            "Look at the situation#2RUkaga#While there\x01",
            "Follow me from behind.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3A28():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3A28)
    Sleep(50)

    def lambda_3A38():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3A38)
    Sleep(300)

    ChrTalk(
        0x104,
        "#6P#00300FOh yeah, leave it to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10100FIt is okay.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A84")

    label("loc_3A84")

    TurnDirection(0x101, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#00000F… Well then.\x01",
            "こんな所でいいか、Singh君？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3ACA():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3ACA)
    Sleep(50)

    def lambda_3ADA():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3ADA)
    Sleep(50)

    def lambda_3AEA():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3AEA)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "#12POh, nice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PそれとボクのことはSinghと呼べ。\x01",
            "You are not a black moon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00009Fはは……分かった、Singh。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PGood!\x01",
            "Well then, I will go out soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PI want to go and Toko,\x01",
            "I will do detailed story outside!\x02",
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
            "クエスト【Singh少年への市街地案内】\x07\x00",
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

    # Function_11_2C9E end

    def Function_12_3CBB(): pass

    label("Function_12_3CBB")

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
            "#11P#03204F#N── Huh, enjoy\x01",
            "It seems to have come and what is more.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(1000, 0)
    OP_0D()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 2)), scpexpr(EXPR_END)), "loc_3E15")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3E15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 4)), scpexpr(EXPR_END)), "loc_3E28")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3E28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_END)), "loc_3E3B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3E3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_END)), "loc_3E4E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3E4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 1)), scpexpr(EXPR_END)), "loc_3E61")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3E61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 0)), scpexpr(EXPR_END)), "loc_3E74")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3E74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 5)), scpexpr(EXPR_END)), "loc_3E87")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3E87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 5)), scpexpr(EXPR_END)), "loc_3E9A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3E9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 0)), scpexpr(EXPR_END)), "loc_3EAD")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3EAD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3F6C")

    ChrTalk(
        0x1A2,
        "#5POh, it was very meaningful!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#5PCrossbell, alkane shell and\x01",
            "It's not just a theme park!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#5PIt's like you, kiremono\x01",
            "I think you will understand why you are stuck!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4047")

    label("loc_3F6C")


    ChrTalk(
        0x1A2,
        "#5POh, it was very meaningful!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#5PActually a little more\x01",
            "There was also a place I wanted to see … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#5PCrossbell, alkane shell and\x01",
            "It's not just a theme park!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#5PIt's like you, kiremono\x01",
            "I think you will understand why you are stuck!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4047")


    ChrTalk(
        0x8,
        "#11P#03200FHaha, this is excuse me.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#11P#03200FMr. Lloyd, Ellie.\x01",
            "Everyone else too.\x02\x03",
            "#03209FこんなにSingh様が喜ばれるとは\x01",
            "I did not even think.\x02\x03",
            "#03204FThank you very much.\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FNo, such a thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00102FHehe, we also\x01",
            "I had it entertained.\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x9, 2580, 0, 1630, 2000, 0x0)

    def lambda_41A0():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_41A0)
    Sleep(50)

    def lambda_41B0():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_41B0)
    Sleep(50)

    def lambda_41C0():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_41C0)
    Sleep(50)

    def lambda_41D0():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_41D0)
    Sleep(50)

    def lambda_41E0():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_41E0)
    Sleep(50)

    def lambda_41F0():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_41F0)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "── It's modest\x01",
            "Please accept this.\x02",
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
            "#12P#00003FOh, because we are police\x01",
            "To receive such things ─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#03204FHuh, I thought that would be the case\x01",
            "I have stopped harassing at Mira.\x02\x03",
            "#03210FNot myself\x01",
            "Singh様との#10R噵  噵  噵  噵  噵#お近づきの印として\x01",
            "Would you please accept it?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_43B6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_43B6)
    Sleep(50)

    def lambda_43C6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_43C6)
    Sleep(50)

    def lambda_43D6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_43D6)
    Sleep(50)

    def lambda_43E6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_43E6)
    Sleep(50)

    def lambda_43F6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_43F6)
    Sleep(300)

    ChrTalk(
        0x101,
        "#6P#00011FWow ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105Fthat is……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "#5PTsao、気がきくじゃないか！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#11PYeah yeah, I do not need refrain!\x01",
            "Bring it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00306F(Do not do it …).\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302F(Huh, if I were told like that\x01",
            "You have no choice but to receive it. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10106F(Yes, indeed.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001F……I understand.\x01",
            "If it is not Mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FThankfully I will receive it.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 500)
    Sleep(300)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4604")
    OP_29(0x73, 0x1, 0xD)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '月灵玉'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('月灵玉', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_4657")

    label("loc_4604")

    OP_29(0x73, 0x1, 0xE)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '云之使者'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('云之使者', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_4657")

    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#6P#00000FWell then,\x01",
            "Excuse me around here.\x02\x03",
            "#00009F──Singh、またな？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        "#6P#00109FHuh, do not you think?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "#11POh, your sisters are also luscious!\x02",
    )

    CloseMessageWindow()

    def lambda_471A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_471A)
    Sleep(100)

    def lambda_472A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_472A)
    Sleep(100)

    def lambda_473A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_473A)
    Sleep(100)

    def lambda_474A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_474A)
    Sleep(100)

    def lambda_475A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_475A)
    WaitChrThread(0x104, 1)

    def lambda_476B():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_476B)
    WaitChrThread(0x109, 1)

    def lambda_4789():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4789)
    WaitChrThread(0x105, 1)

    def lambda_47A7():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_47A7)
    WaitChrThread(0x101, 1)

    def lambda_47C5():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_47C5)
    WaitChrThread(0x102, 1)

    def lambda_47E3():
        OP_97(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_47E3)

    def lambda_47FD():

        label("loc_47FD")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_47FD")

    QueueWorkItem2(0x9, 1, lambda_47FD)
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
        "………………………………\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x2)

    def lambda_48A8():

        label("loc_48A8")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_48A8")

    QueueWorkItem2(0x9, 1, lambda_48A8)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#11P#03200FHuff, being to walk around the street\x01",
            "You seem to be tired.\x02\x03",
            "#03204FRare sweets for the room\x01",
            "We will prepare?\x02",
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
            "#5PIs that so?\x01",
            "You really do not care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#5PYeah yeah, my grandfather too\x01",
            "I will report it properly!\x02",
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

    def lambda_4A01():
        OP_97(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_4A01)
    Sleep(500)

    def lambda_4A1E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_4A1E)
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
            "#11P#03204FHuff, young but intelligent\x01",
            "You will see a glimpse of the big bowl.\x02\x03",
            "#03202FI wonder if I will gain my power in the future …\x01",
            "I'm looking forward to it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x9,
        "#6P……Yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PBut if that is the case\x01",
            "Is not this overkill … ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PIn the unlikely event that \"they\"\x01",
            "Singh様を狙ったりすれば、\x01",
            "Tsao様の責任問題にも……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)

    ChrTalk(
        0x8,
        (
            "#11P#03200FHuh, if you do, he and I will also have my luck\x01",
            "It was just that.\x02\x03",
            "#03204FAnd also \"them\", at this timing\x01",
            "It will not be foolish enough to cause things.\x02\x03",
            "#03201FSo … did you move?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6Pは、Singh様たちを尾行していた\x01",
            "We captured two subjects.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6PWe are monitoring each now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#03204FPretty well, I do not seem to be noticed as it is\x01",
            "Please let me swim.\x02\x03",
            "#03200FAs a sideways spear from the people of the \"business\"\x01",
            "Let's be careful.\x02",
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
            "クエスト【Singh少年への市街地案内】\x07\x00",
            "Achieved!\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_4DE2")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_4E0B")

    label("loc_4DE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_4DF9")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_4E0B")

    label("loc_4DF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_4E0B")
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4E0B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4E24")
    OP_2C(0x73, 0x3)
    Jump("loc_4E92")

    label("loc_4E24")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E51")
    OP_2C(0x73, 0x2)
    Jump("loc_4E92")

    label("loc_4E51")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E7E")
    OP_2C(0x73, 0x1)
    Jump("loc_4E92")

    label("loc_4E7E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_4E92")
    OP_2C(0x73, 0x0)

    label("loc_4E92")

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

    # Function_12_3CBB end

    def Function_13_4EBB(): pass

    label("Function_13_4EBB")

    Sleep(1300)
    Sound(103, 0, 100, 0)
    Sleep(2000)
    Sound(104, 0, 100, 0)
    Return()

    # Function_13_4EBB end

    def Function_14_4ECE(): pass

    label("Function_14_4ECE")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is tightly closed.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_14_4ECE end

    SaveToFile()

Try(main)
