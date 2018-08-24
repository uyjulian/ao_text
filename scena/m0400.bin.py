from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m0400.bin",                # FileName
        "m0400",                    # MapName
        "m0400",                    # Location
        0x00A9,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, -5000, 0, 0, 1, 169, 0, 0, 0, 1],
    )

    BuildStringList((
        "m0400",                  # 0
        "Arios",                  # 1
        "Detective Dudley",       # 2
        "SE制御",                 # 3
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 22,  171.0,                 4.0,                   0.0,                   20.25,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -57.0,                 -1.3333333730697632,   -0.0,                  1.0])

    DeclActor(4294967246, 0,       33570,   1000,    4294967246, 1500,    33570,   0x007C, 0,  23, 0x0000)

    ChipFrameInfo(460, 0)                                        # 0

    ScpFunction((
        "Function_0_1CC",          # 00, 0
        "Function_1_228",          # 01, 1
        "Function_2_390",          # 02, 2
        "Function_3_397",          # 03, 3
        "Function_4_7D1",          # 04, 4
        "Function_5_830",          # 05, 5
        "Function_6_88F",          # 06, 6
        "Function_7_8EF",          # 07, 7
        "Function_8_94F",          # 08, 8
        "Function_9_9AF",          # 09, 9
        "Function_10_A0F",         # 0A, 10
        "Function_11_A6F",         # 0B, 11
        "Function_12_AEA",         # 0C, 12
        "Function_13_F43",         # 0D, 13
        "Function_14_F80",         # 0E, 14
        "Function_15_FCE",         # 0F, 15
        "Function_16_101C",        # 10, 16
        "Function_17_1071",        # 11, 17
        "Function_18_10C6",        # 12, 18
        "Function_19_1114",        # 13, 19
        "Function_20_117D",        # 14, 20
        "Function_21_11C5",        # 15, 21
        "Function_22_1352",        # 16, 22
        "Function_23_1394",        # 17, 23
    ))


    def Function_0_1CC(): pass

    label("Function_0_1CC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E4")
    ClearScenarioFlags(0x25, 1)
    Call(0, 2)

    label("loc_1E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1FB")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 3)
    Jump("loc_20D")

    label("loc_1FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_20D")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 0)
    Event(0, 21)

    label("loc_20D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_227")
    Event(0, 12)

    label("loc_227")

    Return()

    # Function_0_1CC end

    def Function_1_228(): pass

    label("Function_1_228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B2")
    SetMapObjFrame(0xFF, "rai00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "04_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "05_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "under_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ugoku01", 0x0, 0x1)
    Jump("loc_329")

    label("loc_2B2")

    SetMapObjFrame(0xFF, "rai00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "04_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "05_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "under_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ugoku01", 0x1, 0x1)

    label("loc_329")

    ModifyEventFlags(0, 0, 0x80)
    SetMapObjFlags(0x0, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_34D")
    ModifyEventFlags(1, 0, 0x80)
    ClearMapObjFlags(0x0, 0x10)

    label("loc_34D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_361")
    OP_24(0x94)
    ClearScenarioFlags(0x0, 0)
    Jump("loc_38F")

    label("loc_361")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_389")
    OP_24(0x94)
    Jump("loc_38F")

    label("loc_389")

    Sound(148, 1, 100, 0)

    label("loc_38F")

    Return()

    # Function_1_228 end

    def Function_2_390(): pass

    label("Function_2_390")

    Sound(160, 0, 100, 0)
    Return()

    # Function_2_390 end

    def Function_3_397(): pass

    label("Function_3_397")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02400.itc", 0x1E)
    LoadChrToIndex("chr/ch02401.itc", 0x1F)
    LoadChrToIndex("chr/ch00900.itc", 0x20)
    LoadChrToIndex("chr/ch00901.itc", 0x21)
    SoundLoad(4052)
    SoundLoad(3458)
    OP_68(171500, 2700, -100, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 171500, 0, 5500, 180)
    SetChrPos(0x102, 171500, 0, 5500, 180)
    SetChrPos(0x103, 171500, 0, 5500, 180)
    SetChrPos(0x104, 171500, 0, 5500, 180)
    SetChrPos(0x109, 171500, 0, 5500, 180)
    SetChrPos(0x105, 171500, 0, 5500, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 171500, 0, 5500, 180)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 171500, 0, 5500, 180)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(160, 0, 100, 0)
    Sleep(300)
    OP_68(171500, 1200, -100, 3000)
    FadeToBright(2000, 0)
    Sleep(1000)
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    BeginChrThread(0x8, 3, 0, 4)
    Sleep(500)
    BeginChrThread(0x9, 3, 0, 5)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 6)
    Sleep(500)
    BeginChrThread(0x102, 3, 0, 7)
    Sleep(700)
    WaitChrThread(0x8, 3)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x8,
        (
            "#12P#01401F#4052V#30W#15A─Time is short. I'm\x01",
            "going ahead.\x02",
        )
    )

    BeginChrThread(0x103, 3, 0, 8)
    Sleep(500)
    BeginChrThread(0x104, 3, 0, 9)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 10)
    Sleep(500)
    BeginChrThread(0x105, 3, 0, 11)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#00607F#3458V#30W#15A#11PFollow us, and don't\x01",
            "fall behind!\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)

    def lambda_625():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_625)
    Sleep(100)

    def lambda_635():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_635)
    WaitChrThread(0x8, 2)

    ChrTalk(
        0x101,
        "#00005F#11P#10AAh...\x02",
    )

    OP_68(166500, 1100, -100, 2000)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)

    def lambda_678():
        OP_95(0xFE, 157000, 0, -1300, 5500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_678)
    WaitChrThread(0x9, 2)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x0)

    def lambda_69E():
        OP_95(0xFE, 157000, 0, -1300, 5500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_69E)
    CloseMessageWindow()
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)
    Fade(500)
    OP_68(171500, 1200, 1100, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#00306F#11PMan... Those guys are\x01",
            "excited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#11PLet's hurry too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00007F#5PRight!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_37()
    SetChrPos(0x0, 171500, 0, 1500, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x142, 6)
    OP_29(0xA4, 0x1, 0x6)
    ModifyEventFlags(1, 0, 0x80)
    ClearMapObjFlags(0x0, 0x10)
    EventEnd(0x5)
    Return()

    # Function_3_397 end

    def Function_4_7D1(): pass

    label("Function_4_7D1")


    def lambda_7D6():
        OP_96(0xFE, 0x29DEC, 0x0, 0x9C4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7D6)

    def lambda_7F0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7F0)
    WaitChrThread(0xFE, 1)

    def lambda_805():
        OP_96(0xFE, 0x29ACC, 0x0, 0xFFFFFAEC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_805)
    WaitChrThread(0xFE, 1)

    def lambda_823():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_823)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_4_7D1 end

    def Function_5_830(): pass

    label("Function_5_830")


    def lambda_835():
        OP_96(0xFE, 0x29DEC, 0x0, 0x9C4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_835)

    def lambda_84F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_84F)
    WaitChrThread(0xFE, 1)

    def lambda_864():
        OP_96(0xFE, 0x2A10C, 0x0, 0xFFFFFAEC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_864)
    WaitChrThread(0xFE, 1)

    def lambda_882():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_882)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_5_830 end

    def Function_6_88F(): pass

    label("Function_6_88F")


    def lambda_894():
        OP_96(0xFE, 0x29DEC, 0x0, 0x9C4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_894)

    def lambda_8AE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8AE)
    WaitChrThread(0xFE, 1)

    def lambda_8C3():
        OP_96(0xFE, 0x29B94, 0x0, 0x1F4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8C3)
    WaitChrThread(0xFE, 1)

    def lambda_8E1():

        label("loc_8E1")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_8E1")

    QueueWorkItem2(0xFE, 2, lambda_8E1)
    Return()

    # Function_6_88F end

    def Function_7_8EF(): pass

    label("Function_7_8EF")


    def lambda_8F4():
        OP_96(0xFE, 0x29DEC, 0x0, 0x9C4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8F4)

    def lambda_90E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_90E)
    WaitChrThread(0xFE, 1)

    def lambda_923():
        OP_96(0xFE, 0x2A044, 0x0, 0x1F4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_923)
    WaitChrThread(0xFE, 1)

    def lambda_941():

        label("loc_941")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_941")

    QueueWorkItem2(0xFE, 2, lambda_941)
    Return()

    # Function_7_8EF end

    def Function_8_94F(): pass

    label("Function_8_94F")


    def lambda_954():
        OP_96(0xFE, 0x29DEC, 0x0, 0x9C4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_954)

    def lambda_96E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_96E)
    WaitChrThread(0xFE, 1)

    def lambda_983():
        OP_95(0xFE, 169900, 0, 1300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_983)
    WaitChrThread(0xFE, 1)

    def lambda_9A1():

        label("loc_9A1")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_9A1")

    QueueWorkItem2(0xFE, 2, lambda_9A1)
    Return()

    # Function_8_94F end

    def Function_9_9AF(): pass

    label("Function_9_9AF")


    def lambda_9B4():
        OP_96(0xFE, 0x29DEC, 0x0, 0x9C4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9B4)

    def lambda_9CE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9CE)
    WaitChrThread(0xFE, 1)

    def lambda_9E3():
        OP_96(0xFE, 0x2A42C, 0x0, 0x514, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9E3)
    WaitChrThread(0xFE, 1)

    def lambda_A01():

        label("loc_A01")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_A01")

    QueueWorkItem2(0xFE, 2, lambda_A01)
    Return()

    # Function_9_9AF end

    def Function_10_A0F(): pass

    label("Function_10_A0F")


    def lambda_A14():
        OP_96(0xFE, 0x29DEC, 0x0, 0x9C4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A14)

    def lambda_A2E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A2E)
    WaitChrThread(0xFE, 1)

    def lambda_A43():
        OP_96(0xFE, 0x29B94, 0x0, 0x76C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A43)
    WaitChrThread(0xFE, 1)

    def lambda_A61():

        label("loc_A61")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_A61")

    QueueWorkItem2(0xFE, 2, lambda_A61)
    Return()

    # Function_10_A0F end

    def Function_11_A6F(): pass

    label("Function_11_A6F")


    def lambda_A74():
        OP_96(0xFE, 0x29DEC, 0x0, 0x9C4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A74)

    def lambda_A8E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A8E)
    WaitChrThread(0xFE, 1)
    Sound(107, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)

    def lambda_AB5():
        OP_96(0xFE, 0x2A044, 0x0, 0x76C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AB5)
    WaitChrThread(0xFE, 1)

    def lambda_AD3():

        label("loc_AD3")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_AD3")

    QueueWorkItem2(0xFE, 2, lambda_AD3)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    Return()

    # Function_11_A6F end

    def Function_12_AEA(): pass

    label("Function_12_AEA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02401.itc", 0x1E)
    LoadChrToIndex("chr/ch00901.itc", 0x1F)
    SoundLoad(1007)
    SetChrPos(0x101, 35500, 0, 0, 270)
    SetChrPos(0x102, 35500, 0, 0, 270)
    SetChrPos(0x103, 35500, 0, 0, 270)
    SetChrPos(0x104, 35500, 0, 0, 270)
    SetChrPos(0x109, 35500, 0, 0, 270)
    SetChrPos(0x105, 35500, 0, 0, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 8000, 0, 0, 180)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 8000, 0, 0, 180)
    OP_68(0, -40000, 0, 0)
    MoveCamera(90, 17, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(35500, 0)
    OP_68(0, 0, 0, 9000)
    SetCameraDistance(40500, 9000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    BeginChrThread(0xA, 1, 0, 20)
    BeginChrThread(0x8, 3, 0, 13)
    Sleep(500)
    OP_68(0, -3000, 0, 7000)
    MoveCamera(40, 33, 0, 7000)
    SetCameraDistance(58500, 7000)
    Sleep(100)
    BeginChrThread(0x9, 3, 0, 13)
    OP_6F(0x79)
    Sleep(1000)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    StopSound(1007, 2000, 100)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Fade(500)
    OP_68(27000, 1000, 0, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(18500, 0)
    OP_68(32000, 1000, 0, 3000)
    SetCameraDistance(15500, 3000)
    OP_0D()
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x1)
    BeginChrThread(0x101, 3, 0, 14)
    Sleep(500)
    BeginChrThread(0x102, 3, 0, 15)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 16)
    Sleep(500)
    BeginChrThread(0x104, 3, 0, 17)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 18)
    Sleep(500)
    BeginChrThread(0x105, 3, 0, 19)
    OP_6F(0x79)
    WaitChrThread(0x105, 3)

    ChrTalk(
        0x101,
        "#00011F#11PThis place is amazing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10111F#11PIt's overwhelming...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F#11PWow... What is this\x01",
            "place even for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00203FThe Orchis Tower main\x01",
            "shaft.\x02\x03",
            "#00200FIt seems it's for\x01",
            "distributing the tower's\x01",
            "immense weight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11PI heard about it, but...\x01",
            "I didn't know its room\x01",
            "was so big.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(150)

    ChrTalk(
        0x104,
        (
            "#00301F#5PWell anyway, let's\x01",
            "hurry.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xE1, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#5P#00001FYeah. We're heading\x01",
            "south.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_37()
    SetChrPos(0x0, 32000, 0, 0, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_24(0x3EF)
    SetScenarioFlags(0x142, 7)
    EventEnd(0x5)
    Return()

    # Function_12_AEA end

    def Function_13_F43(): pass

    label("Function_13_F43")


    def lambda_F48():
        OP_95(0xFE, 0, 0, -8000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F48)
    WaitChrThread(0xFE, 1)

    def lambda_F66():
        OP_95(0xFE, 0, 0, -38000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F66)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_13_F43 end

    def Function_14_F80(): pass

    label("Function_14_F80")


    def lambda_F85():
        OP_96(0xFE, 0x82DC, 0x0, 0x12C, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F85)

    def lambda_F9F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F9F)
    WaitChrThread(0xFE, 1)

    def lambda_FB4():
        OP_96(0xFE, 0x79E0, 0x0, 0x1C2, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FB4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_14_F80 end

    def Function_15_FCE(): pass

    label("Function_15_FCE")


    def lambda_FD3():
        OP_96(0xFE, 0x82DC, 0x0, 0xFFFFFED4, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FD3)

    def lambda_FED():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FED)
    WaitChrThread(0xFE, 1)

    def lambda_1002():
        OP_96(0xFE, 0x7AA8, 0x0, 0xFFFFFE3E, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1002)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_15_FCE end

    def Function_16_101C(): pass

    label("Function_16_101C")


    def lambda_1021():
        OP_96(0xFE, 0x82DC, 0x0, 0xFFFFFED4, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1021)

    def lambda_103B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_103B)
    WaitChrThread(0xFE, 1)

    def lambda_1050():
        OP_95(0xFE, 32400, 0, -1300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1050)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_16_101C end

    def Function_17_1071(): pass

    label("Function_17_1071")


    def lambda_1076():
        OP_96(0xFE, 0x82DC, 0x0, 0x12C, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1076)

    def lambda_1090():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1090)
    WaitChrThread(0xFE, 1)

    def lambda_10A5():
        OP_95(0xFE, 32200, 0, 1300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10A5)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_17_1071 end

    def Function_18_10C6(): pass

    label("Function_18_10C6")


    def lambda_10CB():
        OP_96(0xFE, 0x82DC, 0x0, 0x12C, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10CB)

    def lambda_10E5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10E5)
    WaitChrThread(0xFE, 1)

    def lambda_10FA():
        OP_96(0xFE, 0x7FBC, 0x0, 0x1C2, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10FA)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_18_10C6 end

    def Function_19_1114(): pass

    label("Function_19_1114")


    def lambda_1119():
        OP_96(0xFE, 0x82DC, 0x0, 0xFFFFFED4, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1119)

    def lambda_1133():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1133)
    WaitChrThread(0xFE, 1)

    def lambda_1148():
        OP_96(0xFE, 0x8084, 0x0, 0xFFFFFE3E, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1148)
    WaitChrThread(0xFE, 1)
    Sound(107, 0, 100, 0)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    Return()

    # Function_19_1114 end

    def Function_20_117D(): pass

    label("Function_20_117D")

    Sound(1007, 2, 20, 0)
    Sleep(200)
    OP_25(0x3EF, 0x1E)
    Sleep(200)
    OP_25(0x3EF, 0x28)
    Sleep(200)
    OP_25(0x3EF, 0x32)
    Sleep(200)
    OP_25(0x3EF, 0x3C)
    Sleep(200)
    OP_25(0x3EF, 0x46)
    Sleep(200)
    OP_25(0x3EF, 0x50)
    Sleep(200)
    OP_25(0x3EF, 0x5A)
    Sleep(200)
    OP_25(0x3EF, 0x64)
    Sleep(5200)
    StopSound(1007, 2000, 90)
    Return()

    # Function_20_117D end

    def Function_21_11C5(): pass

    label("Function_21_11C5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(931)
    SoundLoad(825)
    SetMapObjFrame(0xFF, "rai00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "04_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "05_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "under_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ugoku01", 0x0, 0x1)
    OP_68(-12000, -12000, -2500, 0)
    MoveCamera(75, 63, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(39500, 0)
    SetChrPos(0x0, 0, 0, 0, 0)
    SetChrPos(0x1, 0, 0, 0, 0)
    SetChrPos(0x2, 0, 0, 0, 0)
    SetChrPos(0x3, 0, 0, 0, 0)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    OP_68(0, -3000, 0, 12000)
    MoveCamera(130, 63, 0, 12000)
    SetCameraDistance(79500, 12000)
    Sound(930, 0, 100, 0)
    Sound(929, 0, 50, 0)
    Sound(931, 2, 80, 0)
    Sound(825, 2, 100, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(3000)
    Sound(929, 0, 60, 0)
    Sleep(3000)
    Sound(929, 0, 60, 0)
    Sleep(2000)
    StopSound(931, 2000, 80)
    StopSound(825, 2000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("m0209", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_21_11C5 end

    def Function_22_1352(): pass

    label("Function_22_1352")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FLet's hurry on ahead\x01",
            "ourselves!\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 171130, 0, 1480, 180)
    EventEnd(0x4)
    Return()

    # Function_22_1352 end

    def Function_23_1394(): pass

    label("Function_23_1394")

    EventBegin(0x2)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※　Shaft Control Room Ahead　※\x01",
            "※ Authorized Personnel Only ※\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14F0")

    ChrTalk(
        0x104,
        (
            "#00303FNo way they went this\x01",
            "way, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FYes. The security here is\x01",
            "still active, so they\x01",
            "couldn't have gone this way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F...Then, let's follow\x01",
            "Dudley and Arios.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101FYes, let's head south.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C7, 5)

    label("loc_14F0")

    EventEnd(0x3)
    Return()

    # Function_23_1394 end

    SaveToFile()

Try(main)
