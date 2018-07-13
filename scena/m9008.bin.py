from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m9008.bin",                # FileName
        "m9008",                    # MapName
        "m9008",                    # Location
        0x00C5,                     # MapIndex
        "ed7353",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 197, 0, 0, 0, 1],
    )

    BuildStringList((
        "m9008",                  # 0
        "昇降機",                 # 1
    ))

    DeclNpc(0,       0,       0,       0,    508,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(3500,    0,       4294934546, 1200,    3500,    1500,    4294934546, 0x007C, 0,  2,  0x0000)
    DeclActor(0,       2750,    0,       1200,    0,       4750,    0,       0x007C, 0,  17, 0x0000)

    ChipFrameInfo(568, 0)                                        # 0

    ScpFunction((
        "Function_0_238",          # 00, 0
        "Function_1_2A3",          # 01, 1
        "Function_2_337",          # 02, 2
        "Function_3_42D",          # 03, 3
        "Function_4_6AD",          # 04, 4
        "Function_5_800",          # 05, 5
        "Function_6_1602",         # 06, 6
        "Function_7_165B",         # 07, 7
        "Function_8_175C",         # 08, 8
        "Function_9_2116",         # 09, 9
        "Function_10_2435",        # 0A, 10
        "Function_11_24D6",        # 0B, 11
        "Function_12_24FA",        # 0C, 12
        "Function_13_2521",        # 0D, 13
        "Function_14_2548",        # 0E, 14
        "Function_15_256F",        # 0F, 15
        "Function_16_2596",        # 10, 16
        "Function_17_25BD",        # 11, 17
        "Function_18_2728",        # 12, 18
        "Function_19_27C9",        # 13, 19
    ))


    def Function_0_238(): pass

    label("Function_0_238")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_249")
    Event(0, 3)

    label("loc_249")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_271")
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_271")
    OP_D2(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 19)

    label("loc_271")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_282")
    Event(0, 5)

    label("loc_282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_293")
    Event(0, 8)

    label("loc_293")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_2A2")
    ClearScenarioFlags(0x22, 0)
    Event(0, 7)

    label("loc_2A2")

    Return()

    # Function_0_238 end

    def Function_1_2A3(): pass

    label("Function_1_2A3")

    OP_F0(0x1, 0x320)
    OP_1B(0x2, 0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C4")
    OP_1B(0x1, 0x0, 0x9)
    Jump("loc_2C7")

    label("loc_2C4")

    OP_10(0x1, 0x0)

    label("loc_2C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 2)), scpexpr(EXPR_END)), "loc_2DC")
    ClearMapObjFlags(0x2, 0x2)
    SetMapObjFlags(0x2, 0x4)

    label("loc_2DC")

    SetMapObjFrame(0xFF, "CA_stop", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_303")
    SetMapObjFrame(0xFF, "CA_stop", 0x1, 0x2)

    label("loc_303")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_324")
    SetMapObjFrame(0xFF, "magi_07d_add", 0x0, 0x1)

    label("loc_324")

    OP_71(0x1, 0x0, 0x0, 0x0, 0x1000)
    Sound(112, 1, 50, 0)
    Return()

    # Function_1_2A3 end

    def Function_2_337(): pass

    label("Function_2_337")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is an orbment charging station.\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest Here\x01",      # 0
            "Quit\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41E")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x0, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x0, 0x0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0x0, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_41E")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_2_337 end

    def Function_3_42D(): pass

    label("Function_3_42D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\ev202_00.eff")
    OP_68(-1120, 2000, -23660, 0)
    MoveCamera(46, 35, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16250, 0)
    SetChrPos(0x0, 0, 0, -20000, 180)
    SetChrPos(0x1, 0, 0, -20000, 180)
    SetChrPos(0x2, 0, 0, -20000, 180)
    SetChrPos(0x3, 0, 0, -20000, 180)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_53D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_53D)

    def lambda_54E():
        OP_95(0xFE, 100, -250, -25660, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_54E)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_5A5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_5A5)

    def lambda_5B6():
        OP_95(0xFE, -1490, -250, -25500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_5B6)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_613():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_613)

    def lambda_624():
        OP_95(0xFE, 1930, -250, -24970, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_624)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_67B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_67B)

    def lambda_68C():
        OP_95(0xFE, -3010, -250, -24850, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_68C)
    WaitChrThread(0x3, 1)
    Sleep(500)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_3_42D end

    def Function_4_6AD(): pass

    label("Function_4_6AD")

    EventBegin(0x0)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\evwarp.eff")
    Sound(936, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_706():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_706)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_751():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_751)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_79C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_79C)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_7E7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_7E7)
    Sleep(1000)
    NewScene("m9080", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_6AD end

    def Function_5_800(): pass

    label("Function_5_800")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    SoundLoad(4059)
    SoundLoad(4060)
    SoundLoad(4061)
    SoundLoad(4062)
    SoundLoad(4063)
    LoadChrToIndex("apl/ch51768.itc", 0x1E)
    OP_69(0x3, 0x0)
    SetChrPos(0x101, 0, -250, -33000, 0)
    SetChrPos(0x102, 1300, -250, -33600, 0)
    SetChrPos(0x103, -100, -250, -34300, 0)
    SetChrPos(0x104, -1300, -250, -34000, 0)
    SetChrPos(0xF4, -700, -250, -35800, 0)
    SetChrPos(0xF5, 900, -250, -35500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(0, 1750, -30000, 0)
    MoveCamera(0, 41, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17500, 0)
    OP_68(0, 1750, -24850, 5000)
    MoveCamera(359, 29, 0, 5000)
    OP_6E(700, 5000)
    SetCameraDistance(20260, 5000)
    FadeToBright(1000, 0)

    def lambda_90B():
        OP_9B(0x0, 0xFE, 0x0, 0x1D4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_90B)
    Sleep(50)

    def lambda_923():
        OP_9B(0x0, 0xFE, 0x0, 0x1DB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_923)
    Sleep(50)

    def lambda_93B():
        OP_9B(0x0, 0xFE, 0x0, 0x1E14, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_93B)
    Sleep(50)

    def lambda_953():
        OP_9B(0x0, 0xFE, 0x0, 0x1E78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_953)
    Sleep(50)

    def lambda_96B():
        OP_9B(0x0, 0xFE, 0x0, 0x1EDC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_96B)
    Sleep(50)

    def lambda_983():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_983)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0xF4, 1)
    WaitChrThread(0xF5, 1)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        "#00105F#12PThis place...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#6P...It looks like this place\x01",
            "is the "Sanctuary" terminus...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 2350, -19650, 0)
    MoveCamera(0, 16, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(31000, 0)
    MoveCamera(0, 18, 0, 3500)
    SetCameraDistance(38000, 3500)
    OP_6F(0x79)

    ChrTalk(
        0x103,
        "#00201F#12P#NThere is a gate to a "territory"...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        "#00301F#6P#NAnd a "magical barrier" further in, huh...?\x02",
    )

    OP_6F(0x79)
    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(0, 1250, -25500, 0)
    MoveCamera(0, 21, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16000, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B85")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B3A")
    OP_FC(0x6)
    Jump("loc_B3D")

    label("loc_B3A")

    OP_FC(0xC)

    label("loc_B3D")


    ChrTalk(
        0x10A,
        (
            "#00601F#13P...If there's a "territory"\x01",
            "in this place, then...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C70")

    label("loc_B85")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BFF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BAF")
    OP_FC(0x6)
    Jump("loc_BB2")

    label("loc_BAF")

    OP_FC(0xC)

    label("loc_BB2")


    ChrTalk(
        0x109,
        (
            "#10101F#13P...If there's a "territory"\x01",
            "here, then it means that...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C70")

    label("loc_BFF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C70")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C29")
    OP_FC(0x6)
    Jump("loc_C2C")

    label("loc_C29")

    OP_FC(0xC)

    label("loc_C2C")


    ChrTalk(
        0x106,
        (
            "#10701F#13P...If there is a "territory"\x01",
            "in this place, then...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C70")


    ChrTalk(
        0x101,
        "#00003F#6P............\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_68(0, 1250, -20700, 3000)
    MoveCamera(0, 18, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(16500, 3000)
    BeginChrThread(0x101, 0, 0, 6)
    WaitChrThread(0x101, 0)
    OP_6F(0x79)
    Sleep(500)
    Sound(921, 0, 100, 0)
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_C9(0x0, 0x800)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#40W#4059V#18A──So you've come.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00001F#6P#30W...Mr.... Arios.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E50")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E26")
    OP_FC(0xFFFA)
    Jump("loc_E29")

    label("loc_E26")

    OP_FC(0xFFF4)

    label("loc_E29")


    ChrTalk(
        0x109,
        "#10106F#13P...As expected..\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_EA1")

    label("loc_E50")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EA1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E7A")
    OP_FC(0xFFFA)
    Jump("loc_E7D")

    label("loc_E7A")

    OP_FC(0xFFF4)

    label("loc_E7D")


    ChrTalk(
        0x10A,
        "#00601F#13P...As I thought...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_EA1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EF4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ECB")
    OP_FC(0xFFFA)
    Jump("loc_ECE")

    label("loc_ECB")

    OP_FC(0xFFF4)

    label("loc_ECE")


    ChrTalk(
        0x105,
        "#10403F#13PWell, seems obvious.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_EF4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F48")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F1E")
    OP_FC(0xFFFA)
    Jump("loc_F21")

    label("loc_F1E")

    OP_FC(0xFFF4)

    label("loc_F21")


    ChrTalk(
        0x106,
        "#10701F#13PI imagined it, but...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_F48")

    FadeToDark(300, 0, 100)
    OP_0D()
    OP_C9(0x0, 0x800)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#40W#4060V#41AHmph... Who could've thought that\x01",
            "you'd have defeated that ogre.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#40W#4061V#35AYou don't seem to have that uncertainty\x01",
            "the first time we met anymore.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    Fade(500)
    Sound(202, 0, 100, 0)
    Sound(223, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x2)
    SetMapObjFlags(0x2, 0x4)
    Sleep(500)
    SetChrSubChip(0x101, 0x4)
    Sleep(150)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrSubChip(0x101, 0x0)
    Sleep(1500)
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#40W#4062V#20A──No need for words.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#40W#4063V#31AI'll wait at the end of my "territory".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    OP_C9(0x1, 0x800)
    OP_68(0, 1250, -24850, 3500)
    MoveCamera(0, 11, 0, 3500)
    OP_6E(700, 3500)
    SetCameraDistance(14500, 3500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xF4)
    OP_64(0xF5)
    OP_6F(0x79)

    ChrTalk(
        0x104,
        "#00306F#6P#30W...So, we've finally reached 'im.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#12P#30WYes... He's our target, the greatest\x01",
            "rival of the Special Support Section...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#6P#30W...Come to think of it, it was our\x01",
            "fate since the time we met him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5P#30WYeah...he saved us when we\x01",
            "were helping Ryｹ and Henri who\x01",
            "had dived into the Geofront...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_137F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_135D")
    OP_FC(0x6)
    Jump("loc_1360")

    label("loc_135D")

    OP_FC(0xC)

    label("loc_1360")


    ChrTalk(
        0x10A,
        "#00602F#13P...I see.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1417")

    label("loc_137F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13CC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13A9")
    OP_FC(0x6)
    Jump("loc_13AC")

    label("loc_13A9")

    OP_FC(0xC)

    label("loc_13AC")


    ChrTalk(
        0x109,
        "#10100F#13PReally...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1417")

    label("loc_13CC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1417")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13F6")
    OP_FC(0x6)
    Jump("loc_13F9")

    label("loc_13F6")

    OP_FC(0xC)

    label("loc_13F9")


    ChrTalk(
        0x106,
        "#10710F#13PWas it so...?\x02",
    )

    CloseMessageWindow()

    label("loc_1417")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_147D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1441")
    OP_FC(0x6)
    Jump("loc_1444")

    label("loc_1441")

    OP_FC(0xC)

    label("loc_1444")


    ChrTalk(
        0x105,
        (
            "#10404F#13PHu hu...\x01",
            "Surely a fated connection.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1536")

    label("loc_147D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14DC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14A7")
    OP_FC(0x6)
    Jump("loc_14AA")

    label("loc_14A7")

    OP_FC(0xC)

    label("loc_14AA")


    ChrTalk(
        0x106,
        "#10704F#13PA fated connection, it is...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1536")

    label("loc_14DC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1536")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1506")
    OP_FC(0x6)
    Jump("loc_1509")

    label("loc_1506")

    OP_FC(0xC)

    label("loc_1509")


    ChrTalk(
        0x109,
        "#10106F#13PReally a fated connection...\x02",
    )

    CloseMessageWindow()

    label("loc_1536")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00013F#5P──Let's go.\x01",
            "Mr. Arios is waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00107F#12PYes...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#6PGotcha.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 0, -250, -26000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    OP_D7(0x1E)
    OP_37()
    SetScenarioFlags(0x1A9, 2)
    OP_29(0xB2, 0x1, 0x7)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_5_800 end

    def Function_6_1602(): pass

    label("Function_6_1602")

    OP_95(0xFE, 0, 0, -22300, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(200)
    OP_9B(0x0, 0xFE, 0x0, 0x2BC, 0x3E8, 0x0)
    Sleep(600)
    Sound(812, 0, 100, 0)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrSubChip(0xFE, 0xA)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x4)
    Sleep(150)
    SetChrSubChip(0xFE, 0x5)
    Return()

    # Function_6_1602 end

    def Function_7_165B(): pass

    label("Function_7_165B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadEffect(0x2, "event/ev17018.eff")
    OP_69(0x3, 0x0)
    OP_68(0, 4200, -17250, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34000, 0)
    FadeToBright(1000, 0)
    OP_68(0, 4100, -1300, 5000)
    MoveCamera(0, 16, 0, 5000)
    SetCameraDistance(27720, 5000)
    OP_0D()
    Sleep(3200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 0, 5300, -5500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(202, 0, 50, 0)
    Sound(223, 0, 100, 0)
    Sleep(300)
    SetMapObjFrame(0xFF, "magi_07d_add", 0x0, 0x1)
    Sleep(1500)
    StopSound(112, 1000, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("m9082", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_165B end

    def Function_8_175C(): pass

    label("Function_8_175C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\ev202_00.eff")
    OP_68(0, 1750, -22750, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17800, 0)
    SetChrPos(0x101, 0, 0, -20000, 180)
    SetChrPos(0x102, 0, 0, -20000, 180)
    SetChrPos(0x103, 0, 0, -20000, 180)
    SetChrPos(0x104, 0, 0, -20000, 180)
    SetChrPos(0xF4, 0, 0, -20000, 180)
    SetChrPos(0xF5, 0, 0, -20000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetMapObjFrame(0xFF, "magi_07d_add", 0x0, 0x1)
    SetCameraDistance(18800, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x102, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_18D5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_18D5)

    def lambda_18E6():
        OP_9B(0x0, 0xFE, 0x0, 0x16A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_18E6)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0x103, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_1938():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1938)

    def lambda_1949():
        OP_9B(0x0, 0xFE, 0x15A, 0x1450, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1949)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x104, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_19A1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_19A1)

    def lambda_19B2():
        OP_9B(0x0, 0xFE, 0xE, 0x13EC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_19B2)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0xF4, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_1A04():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_1A04)

    def lambda_1A15():
        OP_9B(0x0, 0xFE, 0x14D, 0x1194, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_1A15)
    Sleep(400)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xF5, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_1A6D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_1A6D)

    def lambda_1A7E():
        OP_9B(0x0, 0xFE, 0x1B, 0x1130, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_1A7E)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0x101, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_1AD0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1AD0)

    def lambda_1AE1():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1AE1)
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(0, 2550, -18840, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(35510, 0)
    OP_68(0, 2550, -9250, 2500)
    OP_0D()

    def lambda_1BAE():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1BAE)
    Sleep(50)

    def lambda_1BBE():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1BBE)
    Sleep(50)

    def lambda_1BCE():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1BCE)
    Sleep(50)

    def lambda_1BDE():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1BDE)
    Sleep(50)

    def lambda_1BEE():
        OP_93(0xF4, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_1BEE)
    Sleep(50)

    def lambda_1BFE():
        OP_93(0xF5, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_1BFE)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Sleep(500)
    OP_6F(0x79)

    ChrTalk(
        0x103,
        (
            "#00201F#11PThat...\x01",
            "It looks like a lift.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#5PThen...\x01",
            "KeA is above that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#5PYeah...no doubt.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#5P#30W............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(0, 1150, -24500, 0)
    MoveCamera(0, 22, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14280, 0)
    Fade(500)
    OP_0D()
    OP_93(0x101, 0xB4, 0x1F4)

    def lambda_1CFE():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1CFE)
    Sleep(50)

    def lambda_1D0E():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1D0E)
    Sleep(50)

    def lambda_1D1E():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1D1E)
    Sleep(50)

    def lambda_1D2E():
        TurnDirection(0xF4, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_1D2E)
    Sleep(50)

    def lambda_1D3E():
        TurnDirection(0xF5, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_1D3E)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00001F#5PWe bested Mr. Arios, but...\x01",
            "That mysterious Miss\x01",
            "Mariabell still remains.\x02\x03",
            "#00003FIf possible, let's return to the Merkabah\x01",
            "and make our final preparations.\x02\x03",
            "#00013FIn order to bring back KeA\x01",
            "without fail── At any cost!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E96")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E76")
    OP_FC(0xC)
    Jump("loc_1E79")

    label("loc_1E76")

    OP_FC(0x6)

    label("loc_1E79")


    ChrTalk(
        0x109,
        "#10101F#13PYes...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F26")

    label("loc_1E96")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1EE1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1EC0")
    OP_FC(0xC)
    Jump("loc_1EC3")

    label("loc_1EC0")

    OP_FC(0x6)

    label("loc_1EC3")


    ChrTalk(
        0x105,
        "#10401F#13PYeah...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F26")

    label("loc_1EE1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F26")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F0B")
    OP_FC(0xC)
    Jump("loc_1F0E")

    label("loc_1F0B")

    OP_FC(0x6)

    label("loc_1F0E")


    ChrTalk(
        0x106,
        "#10701F#13PYes...!\x02",
    )

    CloseMessageWindow()

    label("loc_1F26")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1FB6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F50")
    OP_FC(0xC)
    Jump("loc_1F53")

    label("loc_1F50")

    OP_FC(0x6)

    label("loc_1F53")


    ChrTalk(
        0x10A,
        (
            "#00603F#13P...We can go around every place,\x01",
            "but it looks like this will be our last one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20C9")

    label("loc_1FB6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2043")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1FE0")
    OP_FC(0xC)
    Jump("loc_1FE3")

    label("loc_1FE0")

    OP_FC(0x6)

    label("loc_1FE3")


    ChrTalk(
        0x106,
        (
            "#10703F#13P...We can go around every place,\x01",
            "but it appears this will be our last one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20C9")

    label("loc_2043")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_20C9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_206D")
    OP_FC(0xC)
    Jump("loc_2070")

    label("loc_206D")

    OP_FC(0x6)

    label("loc_2070")


    ChrTalk(
        0x105,
        (
            "#10403F#13P...We can go around every place,\x01",
            "but it seems this will be our last one.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20C9")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 0, -250, -26000, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A9, 5)
    OP_29(0xB2, 0x1, 0x9)
    OP_1B(0x1, 0x0, 0x9)
    OP_10(0x1, 0x1)
    OP_E2(0x2)
    Sleep(300)
    EventEnd(0x5)
    Return()

    # Function_8_175C end

    def Function_9_2116(): pass

    label("Function_9_2116")

    EventBegin(0x0)
    SoundLoad(832)
    SetChrPos(0x101, -50, 2750, -5770, 0)
    SetChrPos(0x102, 930, 2750, -6110, 0)
    SetChrPos(0x103, -1060, 2750, -6040, 0)
    SetChrPos(0x104, -130, 2750, -7330, 0)
    SetChrPos(0xF4, -1260, 2750, -7350, 0)
    SetChrPos(0xF5, 1080, 2750, -7380, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_78(0x1, 0x8)
    SetChrPos(0x8, 0, 2750, 0, 0)
    SetChrFlags(0x8, 0x4)
    OP_68(0, 4150, -4500, 0)
    MoveCamera(0, 28, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16500, 0)
    Fade(500)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00003F#5P(KeA is up ahead...\x01",
            "Also, the entire truth awaits.)\x02\x03",
            "#00013F(Let's strengthen our resolve...\x01",
            "To solve this case completely!)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Use the Lift\x01",      # 0
            "Step Away\x01",         # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_22C0"),
        (1, "loc_2408"),
        (SWITCH_DEFAULT, "loc_2434"),
    )


    label("loc_22C0")

    OP_68(100, 2750, 0, 4500)
    MoveCamera(0, 40, 0, 4500)
    OP_6E(700, 4500)
    SetCameraDistance(29006, 4500)
    BeginChrThread(0x101, 0, 0, 11)
    Sleep(200)
    BeginChrThread(0x102, 0, 0, 12)
    Sleep(100)
    BeginChrThread(0x103, 0, 0, 13)
    Sleep(100)
    BeginChrThread(0x104, 0, 0, 14)
    Sleep(100)
    BeginChrThread(0xF4, 0, 0, 15)
    Sleep(100)
    BeginChrThread(0xF5, 0, 0, 16)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Sleep(500)
    Sound(832, 2, 100, 0)
    Sound(935, 0, 70, 0)
    OP_68(100, 20150, -4500, 8000)
    MoveCamera(0, 24, 0, 8000)
    SetCameraDistance(16500, 8000)
    BeginChrThread(0x8, 0, 0, 10)
    Sleep(1500)

    def lambda_237B():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_237B)
    Sleep(50)

    def lambda_238B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_238B)
    Sleep(50)

    def lambda_239B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_239B)
    Sleep(50)

    def lambda_23AB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_23AB)
    Sleep(50)

    def lambda_23BB():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_23BB)
    Sleep(50)

    def lambda_23CB():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_23CB)
    Sleep(1250)
    Sleep(2000)
    StopSound(832, 500, 100)
    StopSound(112, 500, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x8, 0x0)
    Sleep(1000)
    SetScenarioFlags(0x22, 0)
    NewScene("m9010", 0, 0, 0)
    IdleLoop()
    Jump("loc_2434")

    label("loc_2408")

    SetChrPos(0x0, 0, 2750, -6890, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Jump("loc_2434")

    label("loc_2434")

    Return()

    # Function_9_2116 end

    def Function_10_2435(): pass

    label("Function_10_2435")

    OP_98(0xFE, 0x0, 0x1F4, 0x0, 0x3E8, 0x0)
    OP_98(0xFE, 0x0, 0xBB8, 0x0, 0x7D0, 0x0)
    OP_98(0xFE, 0x0, 0x1388, 0x0, 0xBB8, 0x0)
    OP_98(0xFE, 0x0, 0xBB8, 0x0, 0xFA0, 0x0)
    OP_98(0xFE, 0x0, 0x7D0, 0x0, 0x1388, 0x0)
    OP_98(0xFE, 0x0, 0x3E8, 0x0, 0x1770, 0x0)
    OP_98(0xFE, 0x0, 0x3E8, 0x0, 0x1B58, 0x0)
    OP_98(0xFE, 0x0, 0x2710, 0x0, 0x1F40, 0x0)
    Return()

    # Function_10_2435 end

    def Function_11_24D6(): pass

    label("Function_11_24D6")

    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x1)
    OP_95(0xFE, -820, 2750, 1300, 2000, 0x0)
    Return()

    # Function_11_24D6 end

    def Function_12_24FA(): pass

    label("Function_12_24FA")

    Sleep(50)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x1)
    OP_95(0xFE, 820, 3050, 1300, 2000, 0x0)
    Return()

    # Function_12_24FA end

    def Function_13_2521(): pass

    label("Function_13_2521")

    Sleep(100)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x1)
    OP_95(0xFE, -1480, 3050, -80, 1000, 0x0)
    Return()

    # Function_13_2521 end

    def Function_14_2548(): pass

    label("Function_14_2548")

    Sleep(150)
    OP_9B(0x0, 0xFE, 0x1, 0x157C, 0x7D0, 0x1)
    OP_95(0xFE, 1480, 3050, -80, 1000, 0x0)
    Return()

    # Function_14_2548 end

    def Function_15_256F(): pass

    label("Function_15_256F")

    Sleep(200)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x1)
    OP_95(0xFE, -810, 3050, -1400, 1000, 0x0)
    Return()

    # Function_15_256F end

    def Function_16_2596(): pass

    label("Function_16_2596")

    Sleep(250)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x1)
    OP_95(0xFE, 810, 3050, -1400, 1000, 0x0)
    Return()

    # Function_16_2596 end

    def Function_17_25BD(): pass

    label("Function_17_25BD")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    SoundLoad(832)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a lift.\x01",
            "Move?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2720")
    Fade(500)
    SetChrPos(0x0, 0, 3050, -1500, 180)
    SetChrPos(0x1, -2000, 3050, 0, 270)
    SetChrPos(0x2, 2000, 3050, 0, 90)
    SetChrPos(0x3, 0, 3050, 1500, 0)
    OP_68(100, 2750, 0, 0)
    MoveCamera(0, 40, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(29006, 0)
    OP_78(0x1, 0x8)
    SetChrPos(0x8, 0, 2750, 0, 0)
    SetChrFlags(0x8, 0x4)
    OP_0D()
    Sleep(500)
    Sound(832, 2, 100, 0)
    Sound(935, 0, 70, 0)
    OP_68(100, 20150, -4500, 8000)
    MoveCamera(0, 24, 0, 8000)
    SetCameraDistance(16500, 8000)
    BeginChrThread(0x8, 0, 0, 10)
    Sleep(1500)
    Sleep(50)
    Sleep(50)
    Sleep(50)
    Sleep(50)
    Sleep(50)
    Sleep(1250)
    Sleep(2000)
    StopSound(832, 500, 100)
    StopSound(112, 500, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x8, 0x0)
    Sleep(50)
    OP_D2(0x0, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m9011", 0, 0, 0)
    IdleLoop()

    label("loc_2720")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_17_25BD end

    def Function_18_2728(): pass

    label("Function_18_2728")

    OP_98(0xFE, 0x0, 0xFFFFEC78, 0x0, 0x1388, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x1194, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0xFA0, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFF830, 0x0, 0xDAC, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFF448, 0x0, 0xBB8, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFEC78, 0x0, 0xBB8, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFF448, 0x0, 0x7D0, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFFE0C, 0x0, 0x3E8, 0x0)
    Return()

    # Function_18_2728 end

    def Function_19_27C9(): pass

    label("Function_19_27C9")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    SoundLoad(832)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    OP_68(0, 20150, -4500, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16500, 0)
    OP_78(0x1, 0x8)
    SetChrPos(0x8, 0, 23750, 0, 0)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x0, 0, 24050, -1500, 180)
    SetChrPos(0x1, -2000, 24050, 0, 270)
    SetChrPos(0x2, 2000, 24050, 0, 90)
    SetChrPos(0x3, 0, 24050, 1500, 0)
    Sound(832, 2, 100, 0)
    MoveCamera(0, 35, 0, 3000)
    OP_68(100, 2000, 0, 8000)
    MoveCamera(0, 48, 0, 8000)
    SetCameraDistance(37710, 8000)
    BeginChrThread(0x8, 0, 0, 18)
    FadeToBright(500, 0)
    Sleep(2000)
    Sleep(1500)
    Sleep(1250)
    Sleep(2000)
    OP_24(0x340)
    Sound(149, 0, 60, 0)
    Sleep(1400)
    Sleep(500)
    OP_79(0xF)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_19_27C9 end

    SaveToFile()

Try(main)
