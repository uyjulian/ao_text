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
        "Function_4_7D9",          # 04, 4
        "Function_5_838",          # 05, 5
        "Function_6_897",          # 06, 6
        "Function_7_8F7",          # 07, 7
        "Function_8_957",          # 08, 8
        "Function_9_9B7",          # 09, 9
        "Function_10_A17",         # 0A, 10
        "Function_11_A77",         # 0B, 11
        "Function_12_AF2",         # 0C, 12
        "Function_13_F82",         # 0D, 13
        "Function_14_FBF",         # 0E, 14
        "Function_15_100D",        # 0F, 15
        "Function_16_105B",        # 10, 16
        "Function_17_10B0",        # 11, 17
        "Function_18_1105",        # 12, 18
        "Function_19_1153",        # 13, 19
        "Function_20_11BC",        # 14, 20
        "Function_21_1204",        # 15, 21
        "Function_22_1391",        # 16, 22
        "Function_23_13CD",        # 17, 23
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
            "#12P#01401F#4052V#30W#15A──Time is of essence.\x01",
            "We're going ahead.\x02",
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
        "#00607F#3458V#30W#15A#11PFollow us without delay!\x02",
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
            "#00306F#11POh man...\x01",
            "What energetic dudes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#11PLet's make haste too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00007F#5PYeah...!\x02",
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

    def Function_4_7D9(): pass

    label("Function_4_7D9")


    def lambda_7DE():
        OP_96(0xFE, 0x29DEC, 0x0, 0x9C4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7DE)

    def lambda_7F8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7F8)
    WaitChrThread(0xFE, 1)

    def lambda_80D():
        OP_96(0xFE, 0x29ACC, 0x0, 0xFFFFFAEC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_80D)
    WaitChrThread(0xFE, 1)

    def lambda_82B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_82B)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_4_7D9 end

    def Function_5_838(): pass

    label("Function_5_838")


    def lambda_83D():
        OP_96(0xFE, 0x29DEC, 0x0, 0x9C4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_83D)

    def lambda_857():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_857)
    WaitChrThread(0xFE, 1)

    def lambda_86C():
        OP_96(0xFE, 0x2A10C, 0x0, 0xFFFFFAEC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_86C)
    WaitChrThread(0xFE, 1)

    def lambda_88A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_88A)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_5_838 end

    def Function_6_897(): pass

    label("Function_6_897")


    def lambda_89C():
        OP_96(0xFE, 0x29DEC, 0x0, 0x9C4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_89C)

    def lambda_8B6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8B6)
    WaitChrThread(0xFE, 1)

    def lambda_8CB():
        OP_96(0xFE, 0x29B94, 0x0, 0x1F4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8CB)
    WaitChrThread(0xFE, 1)

    def lambda_8E9():

        label("loc_8E9")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_8E9")

    QueueWorkItem2(0xFE, 2, lambda_8E9)
    Return()

    # Function_6_897 end

    def Function_7_8F7(): pass

    label("Function_7_8F7")


    def lambda_8FC():
        OP_96(0xFE, 0x29DEC, 0x0, 0x9C4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8FC)

    def lambda_916():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_916)
    WaitChrThread(0xFE, 1)

    def lambda_92B():
        OP_96(0xFE, 0x2A044, 0x0, 0x1F4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_92B)
    WaitChrThread(0xFE, 1)

    def lambda_949():

        label("loc_949")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_949")

    QueueWorkItem2(0xFE, 2, lambda_949)
    Return()

    # Function_7_8F7 end

    def Function_8_957(): pass

    label("Function_8_957")


    def lambda_95C():
        OP_96(0xFE, 0x29DEC, 0x0, 0x9C4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_95C)

    def lambda_976():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_976)
    WaitChrThread(0xFE, 1)

    def lambda_98B():
        OP_95(0xFE, 169900, 0, 1300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_98B)
    WaitChrThread(0xFE, 1)

    def lambda_9A9():

        label("loc_9A9")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_9A9")

    QueueWorkItem2(0xFE, 2, lambda_9A9)
    Return()

    # Function_8_957 end

    def Function_9_9B7(): pass

    label("Function_9_9B7")


    def lambda_9BC():
        OP_96(0xFE, 0x29DEC, 0x0, 0x9C4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9BC)

    def lambda_9D6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9D6)
    WaitChrThread(0xFE, 1)

    def lambda_9EB():
        OP_96(0xFE, 0x2A42C, 0x0, 0x514, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9EB)
    WaitChrThread(0xFE, 1)

    def lambda_A09():

        label("loc_A09")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_A09")

    QueueWorkItem2(0xFE, 2, lambda_A09)
    Return()

    # Function_9_9B7 end

    def Function_10_A17(): pass

    label("Function_10_A17")


    def lambda_A1C():
        OP_96(0xFE, 0x29DEC, 0x0, 0x9C4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A1C)

    def lambda_A36():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A36)
    WaitChrThread(0xFE, 1)

    def lambda_A4B():
        OP_96(0xFE, 0x29B94, 0x0, 0x76C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A4B)
    WaitChrThread(0xFE, 1)

    def lambda_A69():

        label("loc_A69")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_A69")

    QueueWorkItem2(0xFE, 2, lambda_A69)
    Return()

    # Function_10_A17 end

    def Function_11_A77(): pass

    label("Function_11_A77")


    def lambda_A7C():
        OP_96(0xFE, 0x29DEC, 0x0, 0x9C4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A7C)

    def lambda_A96():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A96)
    WaitChrThread(0xFE, 1)
    Sound(107, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)

    def lambda_ABD():
        OP_96(0xFE, 0x2A044, 0x0, 0x76C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_ABD)
    WaitChrThread(0xFE, 1)

    def lambda_ADB():

        label("loc_ADB")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_ADB")

    QueueWorkItem2(0xFE, 2, lambda_ADB)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    Return()

    # Function_11_A77 end

    def Function_12_AF2(): pass

    label("Function_12_AF2")

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
        "#00011F#11PWe...came out into an amazing place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10111F#11PSomehow it's overwhelming...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F#11PWow...\x01",
            "What kind of place is this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00203FI think this is Orchis\x01",
            "Tower main shaft.\x02\x03",
            "#00200FIt seems it is a place for dispersing\x01",
            "the weight of the giant tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11PI had heard about it, but...\x01",
            "I didn't know it was such\x01",
            "a big shaft.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(150)

    ChrTalk(
        0x104,
        "#00301F#5PWell, at any rate, let's hurry.\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xE1, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x101,
        "#5P#00001FYeah, we're going south.\x02",
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

    # Function_12_AF2 end

    def Function_13_F82(): pass

    label("Function_13_F82")


    def lambda_F87():
        OP_95(0xFE, 0, 0, -8000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F87)
    WaitChrThread(0xFE, 1)

    def lambda_FA5():
        OP_95(0xFE, 0, 0, -38000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FA5)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_13_F82 end

    def Function_14_FBF(): pass

    label("Function_14_FBF")


    def lambda_FC4():
        OP_96(0xFE, 0x82DC, 0x0, 0x12C, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FC4)

    def lambda_FDE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FDE)
    WaitChrThread(0xFE, 1)

    def lambda_FF3():
        OP_96(0xFE, 0x79E0, 0x0, 0x1C2, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FF3)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_14_FBF end

    def Function_15_100D(): pass

    label("Function_15_100D")


    def lambda_1012():
        OP_96(0xFE, 0x82DC, 0x0, 0xFFFFFED4, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1012)

    def lambda_102C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_102C)
    WaitChrThread(0xFE, 1)

    def lambda_1041():
        OP_96(0xFE, 0x7AA8, 0x0, 0xFFFFFE3E, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1041)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_15_100D end

    def Function_16_105B(): pass

    label("Function_16_105B")


    def lambda_1060():
        OP_96(0xFE, 0x82DC, 0x0, 0xFFFFFED4, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1060)

    def lambda_107A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_107A)
    WaitChrThread(0xFE, 1)

    def lambda_108F():
        OP_95(0xFE, 32400, 0, -1300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_108F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_16_105B end

    def Function_17_10B0(): pass

    label("Function_17_10B0")


    def lambda_10B5():
        OP_96(0xFE, 0x82DC, 0x0, 0x12C, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10B5)

    def lambda_10CF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10CF)
    WaitChrThread(0xFE, 1)

    def lambda_10E4():
        OP_95(0xFE, 32200, 0, 1300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10E4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_17_10B0 end

    def Function_18_1105(): pass

    label("Function_18_1105")


    def lambda_110A():
        OP_96(0xFE, 0x82DC, 0x0, 0x12C, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_110A)

    def lambda_1124():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1124)
    WaitChrThread(0xFE, 1)

    def lambda_1139():
        OP_96(0xFE, 0x7FBC, 0x0, 0x1C2, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1139)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_18_1105 end

    def Function_19_1153(): pass

    label("Function_19_1153")


    def lambda_1158():
        OP_96(0xFE, 0x82DC, 0x0, 0xFFFFFED4, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1158)

    def lambda_1172():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1172)
    WaitChrThread(0xFE, 1)

    def lambda_1187():
        OP_96(0xFE, 0x8084, 0x0, 0xFFFFFE3E, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1187)
    WaitChrThread(0xFE, 1)
    Sound(107, 0, 100, 0)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    Return()

    # Function_19_1153 end

    def Function_20_11BC(): pass

    label("Function_20_11BC")

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

    # Function_20_11BC end

    def Function_21_1204(): pass

    label("Function_21_1204")

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

    # Function_21_1204 end

    def Function_22_1391(): pass

    label("Function_22_1391")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        "#00001FLet's hurry on ahead too!\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 171130, 0, 1480, 180)
    EventEnd(0x4)
    Return()

    # Function_22_1391 end

    def Function_23_13CD(): pass

    label("Function_23_13CD")

    EventBegin(0x2)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※　Shaft Control Room Ahead　※\x01",
            "※　Authorized Personnel Only　※\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1563")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1563")

    ChrTalk(
        0x104,
        (
            "#00303FDon't tell me that they've\x01",
            "gone in this direction, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FNo, since it doesn't appear\x01",
            "that security has been called off,\x01",
            "they shouldn't have gone this way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F...Then, let's chase after\x01",
            "Mr. Dudley and Mr. Arios.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101FYes, let's head south.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C7, 5)

    label("loc_1563")

    EventEnd(0x3)
    Return()

    # Function_23_13CD end

    SaveToFile()

Try(main)
