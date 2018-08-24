from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m9011.bin",                # FileName
        "m9011",                    # MapName
        "m9011",                    # Location
        0x0094,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 148, 0, 0, 0, 1],
    )

    BuildStringList((
        "m9011",                  # 0
        "昇降機",                 # 1
    ))

    DeclNpc(0,       0,       0,       0,    508,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(6500,    4294966796, 4294963296, 1200,    6500,    500,     4294963296, 0x007C, 0,  2,  0x0000)
    DeclActor(0,       0,       0,       1200,    0,       2000,    0,       0x007C, 0,  5,  0x0000)

    ChipFrameInfo(276, 0)                                        # 0

    ScpFunction((
        "Function_0_114",          # 00, 0
        "Function_1_152",          # 01, 1
        "Function_2_198",          # 02, 2
        "Function_3_28C",          # 03, 3
        "Function_4_84E",          # 04, 4
        "Function_5_9DA",          # 05, 5
        "Function_6_B09",          # 06, 6
    ))


    def Function_0_114(): pass

    label("Function_0_114")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13C")
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13C")
    OP_D2(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 6)

    label("loc_13C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_151")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 3)

    label("loc_151")

    Return()

    # Function_0_114 end

    def Function_1_152(): pass

    label("Function_1_152")

    OP_F0(0x1, 0x320)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_16B")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x161), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_16B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_17F")
    OP_24(0x6D)
    ClearScenarioFlags(0x0, 1)
    Jump("loc_185")

    label("loc_17F")

    Sound(109, 1, 100, 0)

    label("loc_185")

    Sound(125, 1, 60, 0)
    OP_71(0x0, 0x0, 0x0, 0x0, 0x1000)
    Return()

    # Function_1_152 end

    def Function_2_198(): pass

    label("Function_2_198")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's an orbment charging station.\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest Here\x01",      # 0
            "Cancel\x01",         # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27D")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x1, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x1, 0x0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x1)
    OP_71(0x1, 0x1F, 0x186, 0x0, 0x20)
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
    OP_70(0x1, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_27D")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_2_198 end

    def Function_3_28C(): pass

    label("Function_3_28C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(109)
    Call(0, 4)
    SetChrPos(0x101, -900, 0, 1500, 315)
    SetChrPos(0x102, 900, 0, 1500, 45)
    SetChrPos(0x103, -1600, 0, 0, 270)
    SetChrPos(0x104, 1600, 0, 0, 90)
    SetChrPos(0xF4, -900, 0, -1500, 225)
    SetChrPos(0xF5, 900, 0, -1500, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_78(0x0, 0x8)
    SetChrPos(0x8, 0, 0, 0, 0)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0xF4, 0x4)
    SetChrFlags(0xF5, 0x4)
    OP_68(0, 5300, 200000, 0)
    MoveCamera(0, 14, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(275000, 0)
    SetCameraDistance(250000, 3500)
    Sound(109, 2, 100, 0)
    StopBGM(0x2EE0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_68(-10210, 2500, 83680, 8000)
    MoveCamera(336, 5, 0, 8000)
    OP_6E(1000, 8000)
    SetCameraDistance(152870, 8000)
    PlaceName2(340, 200, "c_plac62", 0x0, 2000)
    OP_6F(0x79)
    Fade(500)
    OP_68(1120, 17600, 45350, 0)
    MoveCamera(0, -1, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(12000, 0)
    OP_68(170, 3400, 1100, 7000)
    MoveCamera(0, -1, 0, 7000)
    OP_6E(1000, 7000)
    SetCameraDistance(12000, 7000)

    def lambda_445():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_445)
    Sleep(50)

    def lambda_455():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_455)
    Sleep(50)

    def lambda_465():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_465)
    Sleep(50)

    def lambda_475():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_475)
    Sleep(50)

    def lambda_485():
        OP_93(0xF4, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_485)
    Sleep(50)

    def lambda_495():
        OP_93(0xF5, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_495)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Sleep(6000)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0xF4, 0x4)
    ClearChrFlags(0xF5, 0x4)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xF4)
    OP_64(0xF5)
    Sleep(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BE")

    ChrTalk(
        0x102,
        (
            "#00103F#12P#NThere's nothing...\x01",
            "further to say.\x02\x03",
            "#00101FLloyd, let's go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D9")

    label("loc_5BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61B")

    ChrTalk(
        0x103,
        (
            "#00203F#6P#NWords are no longer\x01",
            "necessary.\x02\x03",
            "#00201FLloyd, let's go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D9")

    label("loc_61B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_677")

    ChrTalk(
        0x104,
        (
            "#00303F#12P#NThere's nothin' more to\x01",
            "say.\x02\x03",
            "#00301FLloyd, let's go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D9")

    label("loc_677")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6A0")
    OP_FC(0xFFFA)
    Jump("loc_6A3")

    label("loc_6A0")

    OP_FC(0xFFF4)

    label("loc_6A3")


    ChrTalk(
        0x105,
        (
            "#10404F#13P...Hehe. Words are\x01",
            "unnecessary.\x02\x03",
            "#10400FShall we, Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D9")

    label("loc_6F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_71A")
    OP_FC(0xFFFA)
    Jump("loc_71D")

    label("loc_71A")

    OP_FC(0xFFF4)

    label("loc_71D")


    ChrTalk(
        0x109,
        (
            "#10103F#13PThere's no more need for\x01",
            "words.\x02\x03",
            "#10101FLloyd, let's go!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D9")

    label("loc_76B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_794")
    OP_FC(0xFFFA)
    Jump("loc_797")

    label("loc_794")

    OP_FC(0xFFF4)

    label("loc_797")


    ChrTalk(
        0x106,
        (
            "#10700F#13PThere's no more need for\x01",
            "words.\x02\x03",
            "Lloyd, let's go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D9")

    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_802")

    ChrTalk(
        0x101,
        "#00013F#5PRight!\x02",
    )

    CloseMessageWindow()

    label("loc_802")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 0, 0, 3500, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A9, 6)
    OP_29(0xB2, 0x1, 0xA)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_3_28C end

    def Function_4_84E(): pass

    label("Function_4_84E")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 1)), scpexpr(EXPR_END)), "loc_870")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9D9")

    label("loc_870")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 2)), scpexpr(EXPR_END)), "loc_888")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9D9")

    label("loc_888")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 3)), scpexpr(EXPR_END)), "loc_8A0")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9D9")

    label("loc_8A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 4)), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8C3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9D9")

    label("loc_8C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 5)), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8E6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9D9")

    label("loc_8E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 6)), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_909")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9D9")

    label("loc_909")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_927")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9D9")

    label("loc_927")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_945")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9D9")

    label("loc_945")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_963")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9D9")

    label("loc_963")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_98C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9D9")

    label("loc_98C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9B5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9D9")

    label("loc_9B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9D9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9D9")

    Return()

    # Function_4_84E end

    def Function_5_9DA(): pass

    label("Function_5_9DA")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    SoundLoad(832)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a lift. Use it?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B01")
    Fade(500)
    SetChrPos(0x0, 0, 0, -1500, 180)
    SetChrPos(0x1, -2000, 0, 0, 270)
    SetChrPos(0x2, 2000, 0, 0, 90)
    SetChrPos(0x3, 0, 0, 1500, 0)
    OP_68(0, 2000, 0, 0)
    MoveCamera(0, 44, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(16000, 0)
    OP_0D()
    Sleep(500)
    Sound(832, 2, 100, 0)
    Sound(935, 0, 70, 0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x3C, 0x5A, 0x0, 0x0)
    OP_68(0, -4000, 0, 4000)
    MoveCamera(359, 14, 0, 4000)
    StopSound(109, 1700, 100)
    StopSound(125, 1700, 60)
    Sleep(1800)
    StopSound(832, 500, 100)
    OP_D2(0x0, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m9008", 0, 0, 0)
    IdleLoop()

    label("loc_B01")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_5_9DA end

    def Function_6_B09(): pass

    label("Function_6_B09")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    SoundLoad(832)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    OP_6F(0x1)
    OP_70(0x0, 0x5A)
    Sleep(1)
    OP_68(0, -2750, 1500, 0)
    MoveCamera(0, 49, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(16000, 0)
    OP_90(0x0, 0, 0, -1500, 180)
    OP_90(0x1, -2000, 0, 0, 270)
    OP_90(0x2, 2000, 0, 0, 90)
    OP_90(0x3, 0, 0, 1500, 0)
    Sound(832, 2, 100, 0)
    MoveCamera(0, 40, 0, 3000)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x5A, 0x78, 0x0, 0x0)
    FadeToBright(500, 0)
    Sleep(2000)
    OP_24(0x340)
    Sound(149, 0, 60, 0)
    Sleep(1400)
    Sleep(500)
    OP_79(0x0)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_6_B09 end

    SaveToFile()

Try(main)
