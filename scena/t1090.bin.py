from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1090.bin",                # FileName
        "t1090",                    # MapName
        "t1090",                    # Location
        0x0042,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 66, 0, 2, 0, 3],
    )

    BuildStringList((
        "t1090",                  # 0
        "KeA",                    # 1
        "Tio",                    # 2
        "Elie",                   # 3
    ))

    AddCharChip((
        "chr/ch08200.itc",                   # 00
        "chr/ch00200.itc",                   # 01
        "chr/ch00100.itc",                   # 02
    ))

    DeclNpc(4294869097, 800,     4294963406, 0,    389,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(4294868926, 0,       4294967096, 180,  389,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(4294871296, 0,       3400,    0,    389,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)

    DeclActor(4294869096, 0,       4294964656, 1200,    4294869096, 2500,    4294963406, 0x007E, 0,  4,  0x0000)

    ChipFrameInfo(312, 0)                                        # 0

    ScpFunction((
        "Function_0_138",          # 00, 0
        "Function_1_1F0",          # 01, 1
        "Function_2_2C1",          # 02, 2
        "Function_3_35F",          # 03, 3
        "Function_4_372",          # 04, 4
        "Function_5_438",          # 05, 5
        "Function_6_519",          # 06, 6
        "Function_7_756",          # 07, 7
    ))


    def Function_0_138(): pass

    label("Function_0_138")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
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

    # Function_0_138 end

    def Function_1_1F0(): pass

    label("Function_1_1F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2C0")
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x258, 0xDAC)
    Sleep(400)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x190, 0xEA6)
    Sleep(250)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xDAC)
    Sleep(400)
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x190, 0xEA6)
    Sleep(250)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x258, 0xDAC)
    Sleep(400)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xEA6)
    Sleep(350)
    Jump("Function_1_1F0")

    label("loc_2C0")

    Return()

    # Function_1_1F0 end

    def Function_2_2C1(): pass

    label("Function_2_2C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_2CF")
    Jump("loc_35E")

    label("loc_2CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_2DD")
    Jump("loc_35E")

    label("loc_2DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_2EB")
    Jump("loc_35E")

    label("loc_2EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_2F9")
    Jump("loc_35E")

    label("loc_2F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_307")
    Jump("loc_35E")

    label("loc_307")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_315")
    Jump("loc_35E")

    label("loc_315")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_323")
    Jump("loc_35E")

    label("loc_323")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_355")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x8, 0x1)
    BeginChrThread(0x8, 0, 0, 1)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_35E")

    label("loc_355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_35E")

    label("loc_35E")

    Return()

    # Function_2_2C1 end

    def Function_3_35F(): pass

    label("Function_3_35F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_371")
    OP_65(0x0, 0x1)

    label("loc_371")

    Return()

    # Function_3_35F end

    def Function_4_372(): pass

    label("Function_4_372")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_383")
    Jump("loc_434")

    label("loc_383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_391")
    Jump("loc_434")

    label("loc_391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_39F")
    Jump("loc_434")

    label("loc_39F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_3AD")
    Jump("loc_434")

    label("loc_3AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_3BB")
    Jump("loc_434")

    label("loc_3BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_3C9")
    Jump("loc_434")

    label("loc_3C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_42B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E4")
    Call(0, 6)
    Jump("loc_426")

    label("loc_3E4")

    SetChrPos(0x8, -98200, 800, -3890, 0)

    ChrTalk(
        0x8,
        (
            "#01109FA soft and fluffy bed,\x01",
            "it's so nice!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_426")

    Jump("loc_434")

    label("loc_42B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_434")

    label("loc_434")

    TalkEnd(0x8)
    Return()

    # Function_4_372 end

    def Function_5_438(): pass

    label("Function_5_438")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_449")
    Jump("loc_515")

    label("loc_449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_457")
    Jump("loc_515")

    label("loc_457")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_465")
    Jump("loc_515")

    label("loc_465")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_475")
    Jump("loc_515")

    label("loc_475")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_483")
    Jump("loc_515")

    label("loc_483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_491")
    Jump("loc_515")

    label("loc_491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_49F")
    Jump("loc_515")

    label("loc_49F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_50C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BA")
    Call(0, 6)
    Jump("loc_507")

    label("loc_4BA")


    ChrTalk(
        0x9,
        (
            "#00202FI'm drawn to these beds,\x01",
            "but...\x02\x03",
            "#00206F...For now, I'll unpack.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_507")

    Jump("loc_515")

    label("loc_50C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_515")

    label("loc_515")

    TalkEnd(0xFE)
    Return()

    # Function_5_438 end

    def Function_6_519(): pass

    label("Function_6_519")

    OP_4B(0x9, 0xFF)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x8, -98200, 800, -3890, 0)

    def lambda_537():
        TurnDirection(0x0, 0x8, 0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_537)
    Sleep(0)

    def lambda_547():
        TurnDirection(0x1, 0x8, 0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_547)
    Sleep(0)

    def lambda_557():
        TurnDirection(0x2, 0x8, 0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_557)
    Sleep(0)
    WaitChrThread(0x0, 0)
    WaitChrThread(0x1, 0)
    WaitChrThread(0x2, 0)

    ChrTalk(
        0x8,
        (
            "#01109FLook, look Tio! It's\x01",
            "sooo soft and fluffy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#00202FIt looks like these beds\x01",
            "were made with pretty\x01",
            "good materials.\x02\x03",
            "#00204FSince I'm here, I'll\x01",
            "join you...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_61E():
        TurnDirection(0x0, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_61E)
    Sleep(50)

    def lambda_62E():
        TurnDirection(0x1, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_62E)
    Sleep(50)

    def lambda_63E():
        TurnDirection(0x2, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_63E)
    Sleep(50)
    WaitChrThread(0x0, 0)
    WaitChrThread(0x1, 0)
    WaitChrThread(0x2, 0)

    ChrTalk(
        0x101,
        (
            "#00006FIf you guys do that\x01",
            "together, don't you think\x01",
            "it'll be kind of annoying?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)

    ChrTalk(
        0x9,
        (
            "#00206F...Naturally, it was a\x01",
            "joke.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#00306F(I bet she was dead\x01",
            "serious...)\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 3)
    OP_4C(0x9, 0xFF)
    OP_4C(0x8, 0xFF)
    TurnDirection(0x9, 0x8, 0)
    Return()

    # Function_6_519 end

    def Function_7_756(): pass

    label("Function_7_756")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_767")
    Jump("loc_A15")

    label("loc_767")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_775")
    Jump("loc_A15")

    label("loc_775")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_783")
    Jump("loc_A15")

    label("loc_783")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_793")
    Jump("loc_A15")

    label("loc_793")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_7A1")
    Jump("loc_A15")

    label("loc_7A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_7AF")
    Jump("loc_A15")

    label("loc_7AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_7BD")
    Jump("loc_A15")

    label("loc_7BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_A0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_987")

    ChrTalk(
        0xA,
        (
            "#00100FI can't believe Cecil\x01",
            "and the others are\x01",
            "really here.\x02\x03",
            "#00106FI don't know if plans\x01",
            "like these are typical\x01",
            "of Bell or what...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHehe. Thanks to her, the\x01",
            "male to female ratio has\x01",
            "suddenly become threatening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FStill, it's true that it\x01",
            "was a happy surprise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00109FW-Well, I suppose.\x02\x03",
            "#00106FShe's been surprising me in one way\x01",
            "or another ever since we were\x01",
            "children. It's a little embarrassing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_A07")

    label("loc_987")


    ChrTalk(
        0xA,
        (
            "#00100FOh, right. Bell told me\x01",
            "the beach is a very pretty\x01",
            "place a while back.\x02\x03",
            "#00109F*giggle*. I'm looking\x01",
            "forward to it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A07")

    Jump("loc_A15")

    label("loc_A0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_A15")

    label("loc_A15")

    TalkEnd(0xFE)
    Return()

    # Function_7_756 end

    SaveToFile()

Try(main)
