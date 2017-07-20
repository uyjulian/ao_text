from ScenarioHelper import *

def main():
    CreateScenaFile(
        "e3210.bin",                # FileName
        "e3210",                    # MapName
        "e3210",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "e3210",                  # 0
        "Claudia Hime",         # 1
        "Assistant Julia",             # 2
        "Prince Oliver",       # 3
        "Major Muller",           # 4
        "Sieg",                 # 5
        "The gentleman",                 # 6
        "The gentleman",                 # 7
        "The gentleman",                 # 8
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(428, 0)                                        # 0

    ScpFunction((
        "Function_0_1AC",          # 00, 0
        "Function_1_25C",          # 01, 1
        "Function_2_26C",          # 02, 2
        "Function_3_26D",          # 03, 3
        "Function_4_2ED",          # 04, 4
        "Function_5_2FF",          # 05, 5
        "Function_6_311",          # 06, 6
        "Function_7_34E",          # 07, 7
        "Function_8_3A3",          # 08, 8
        "Function_9_419",          # 09, 9
        "Function_10_471",         # 0A, 10
        "Function_11_4C9",         # 0B, 11
        "Function_12_521",         # 0C, 12
        "Function_13_597",         # 0D, 13
    ))


    def Function_0_1AC(): pass

    label("Function_0_1AC")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1E4"),
        (1, "loc_1F0"),
        (2, "loc_1FC"),
        (3, "loc_208"),
        (4, "loc_214"),
        (5, "loc_220"),
        (6, "loc_22C"),
        (SWITCH_DEFAULT, "loc_238"),
    )


    label("loc_1E4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_1F0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_1FC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_208")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_214")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_220")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_22C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_238")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_244")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_25B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_25B")

    Return()

    # Function_0_1AC end

    def Function_1_25C(): pass

    label("Function_1_25C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_26B")
    ClearScenarioFlags(0x22, 0)
    Event(0, 13)

    label("loc_26B")

    Return()

    # Function_1_25C end

    def Function_2_26C(): pass

    label("Function_2_26C")

    Return()

    # Function_2_26C end

    def Function_3_26D(): pass

    label("Function_3_26D")


    def lambda_272():
        OP_95(0xFE, 0, 0, 3300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_272)

    def lambda_28C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_28C)
    WaitChrThread(0xFE, 1)

    def lambda_2A1():
        OP_95(0xFE, -2000, 0, 3300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A1)
    WaitChrThread(0xFE, 1)

    def lambda_2BF():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2BF)
    Sleep(1000)

    def lambda_2DC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2DC)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_3_26D end

    def Function_4_2ED(): pass

    label("Function_4_2ED")

    Sleep(2500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xD, 0x29)
    SetChrSubChip(0xD, 0x0)
    Return()

    # Function_4_2ED end

    def Function_5_2FF(): pass

    label("Function_5_2FF")

    Sleep(7000)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xE, 0x29)
    SetChrSubChip(0xE, 0x0)
    Return()

    # Function_5_2FF end

    def Function_6_311(): pass

    label("Function_6_311")


    def lambda_316():
        OP_95(0xFE, -99000, 0, 3200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_316)
    WaitChrThread(0xFE, 1)

    def lambda_334():
        OP_95(0xFE, -99000, 0, 5200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_334)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_6_311 end

    def Function_7_34E(): pass

    label("Function_7_34E")


    def lambda_353():
        OP_95(0xFE, -99000, 0, 42400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_353)

    def lambda_36D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_36D)
    WaitChrThread(0xFE, 1)

    def lambda_382():
        OP_95(0xFE, -100900, 0, 44300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_382)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_7_34E end

    def Function_8_3A3(): pass

    label("Function_8_3A3")

    Sleep(700)

    def lambda_3AB():
        OP_95(0xFE, -99000, 0, 42400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3AB)

    def lambda_3C5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3C5)
    WaitChrThread(0xFE, 1)

    def lambda_3DA():
        OP_95(0xFE, -101400, 0, 43000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3DA)
    WaitChrThread(0xFE, 1)

    def lambda_3F8():
        OP_95(0xFE, -101600, 0, 45000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F8)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_8_3A3 end

    def Function_9_419(): pass

    label("Function_9_419")

    Sleep(1600)

    def lambda_421():
        OP_95(0xFE, -99000, 0, 42400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_421)

    def lambda_43B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_43B)
    WaitChrThread(0xFE, 1)

    def lambda_450():
        OP_95(0xFE, -102100, 0, 43700, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_450)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_9_419 end

    def Function_10_471(): pass

    label("Function_10_471")

    Sleep(2300)

    def lambda_479():
        OP_95(0xFE, -99000, 0, 42400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_479)

    def lambda_493():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_493)
    WaitChrThread(0xFE, 1)

    def lambda_4A8():
        OP_95(0xFE, -101400, 0, 43000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4A8)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_10_471 end

    def Function_11_4C9(): pass

    label("Function_11_4C9")

    Sleep(3000)

    def lambda_4D1():
        OP_95(0xFE, -99000, 0, 42400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4D1)

    def lambda_4EB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4EB)
    WaitChrThread(0xFE, 1)

    def lambda_500():
        OP_95(0xFE, -100200, 0, 43000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_500)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_11_4C9 end

    def Function_12_521(): pass

    label("Function_12_521")

    Sleep(3700)

    def lambda_529():
        OP_95(0xFE, -99000, 0, 42400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_529)

    def lambda_543():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_543)
    WaitChrThread(0xFE, 1)

    def lambda_558():
        OP_95(0xFE, -95500, 0, 44900, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_558)
    WaitChrThread(0xFE, 1)

    def lambda_576():
        OP_95(0xFE, -95500, 0, 48600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_576)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_12_521 end

    def Function_13_597(): pass

    label("Function_13_597")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11000.itc", 0x1E)
    LoadChrToIndex("chr/ch11100.itc", 0x1F)
    LoadChrToIndex("chr/ch11200.itc", 0x20)
    LoadChrToIndex("chr/ch11300.itc", 0x21)
    LoadChrToIndex("chr/ch13801.itc", 0x22)
    LoadChrToIndex("chr/ch41600.itc", 0x23)
    LoadChrToIndex("apl/ch51260.itc", 0x24)
    LoadChrToIndex("chr/ch11002.itc", 0x25)
    LoadChrToIndex("chr/ch11102.itc", 0x26)
    LoadChrToIndex("chr/ch11202.itc", 0x27)
    LoadChrToIndex("chr/ch11302.itc", 0x28)
    LoadChrToIndex("apl/ch51213.itc", 0x29)
    LoadChrToIndex("apl/ch51214.itc", 0x2A)
    LoadChrToIndex("apl/ch51215.itc", 0x2B)
    LoadChrToIndex("chr/ch00002.itc", 0x2C)
    LoadChrToIndex("chr/ch00102.itc", 0x2D)
    LoadChrToIndex("chr/ch00302.itc", 0x2E)
    LoadChrToIndex("chr/ch02902.itc", 0x2F)
    LoadChrToIndex("chr/ch03002.itc", 0x30)
    LoadChrToIndex("chr/ch13802.itc", 0x31)
    SoundLoad(498)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07000.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07201.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07300.itp")
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x4)
    SetChrPos(0x9, 0, 0, -13500, 0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xA, 0x2A)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xC, 0x22)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xD, 0x23)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 3200, 0, -6000, 270)
    SetChrChipByIndex(0xE, 0x23)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -3500, 0, 3500, 90)
    SetChrPos(0x101, 0, 0, -13500, 0)
    SetChrPos(0x102, 0, 0, -13500, 0)
    SetChrPos(0x104, 0, 0, -13500, 0)
    SetChrPos(0x109, 0, 0, -13500, 0)
    SetChrPos(0x105, 0, 0, -13500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMapObjFlags(0x4, 0x1000)
    OP_70(0x4, 0x0)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    OP_68(0, 1000, -10000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    OP_68(0, 1000, 1000, 7000)
    SetCameraDistance(20500, 7000)
    Sound(100, 0, 80, 0)
    FadeToBright(1000, 0)
    BeginChrThread(0xD, 3, 0, 4)
    BeginChrThread(0xE, 3, 0, 5)
    BeginChrThread(0x9, 3, 0, 3)
    Sleep(900)
    BeginChrThread(0x101, 3, 0, 3)
    Sleep(600)
    BeginChrThread(0x102, 3, 0, 3)
    Sleep(600)
    BeginChrThread(0x104, 3, 0, 3)
    Sleep(600)
    BeginChrThread(0x109, 3, 0, 3)
    Sleep(600)
    BeginChrThread(0x105, 3, 0, 3)
    Sleep(500)
    Sound(100, 0, 80, 0)
    OP_6F(0x79)
    SetCameraDistance(19000, 5000)
    WaitChrThread(0x9, 3)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x9, 0xFF)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0xD, 0x23)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -3410, 0, 96130, 270)
    BeginChrThread(0xD, 3, 0, 0)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 1850, 200, 97370, 90)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -3520, 200, 97470, 270)
    OP_68(-1000, 1500, 97000, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    OP_68(-1000, 2500, 96000, 7000)
    MoveCamera(35, 25, 0, 7000)
    SetCameraDistance(21500, 7000)
    Sound(498, 2, 30, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(3000)
    StopSound(498, 2000, 30)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_68(-99000, 1600, 2900, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, -99600, 70, 900, 0)
    SetChrPos(0x102, -98400, 70, 900, 0)
    SetChrPos(0x104, -97800, 60, -300, 0)
    SetChrPos(0x109, -99000, 70, -900, 0)
    SetChrPos(0x105, -100200, 60, -300, 0)
    SetChrPos(0x9, -99000, 70, 2500, 0)
    SetChrFlags(0x9, 0x4)
    SetChrPos(0x8, -99000, 70, 6500, 0)
    ClearChrFlags(0x8, 0x80)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-99000, 1100, 2900, 2000)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_AF5():
        OP_96(0xFE, 0xFFFE7D48, 0x46, 0xC80, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_AF5)
    WaitChrThread(0x9, 1)
    Sound(808, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x9,
        (
            "#11P#07104FYour Majesty, excuse me\x02\x03",
            "Mr. Managers of Special Affairs Support Division\x01",
            "I brought you.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "A cool voice",
        "#3C#2S#11PPlease enter\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(100, 0, 80, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x2)

    def lambda_BBD():
        OP_95(0xFE, -97800, 70, 3200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_BBD)
    WaitChrThread(0x9, 1)
    OP_93(0x9, 0xE1, 0x1F4)

    def lambda_BE2():

        label("loc_BE2")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_BE2")

    QueueWorkItem2(0x9, 2, lambda_BE2)

    ChrTalk(
        0x9,
        "#5P#07102FOk please head in\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00001FR-right\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104FExcuse us\x02",
    )

    CloseMessageWindow()
    OP_68(-99000, 1100, 3900, 2000)
    FadeToDark(2000, 0, -1)
    BeginChrThread(0x101, 3, 0, 6)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 6)
    Sleep(300)
    EndChrThread(0x9, 0x2)
    BeginChrThread(0x104, 3, 0, 6)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 6)
    Sleep(300)
    BeginChrThread(0x105, 3, 0, 6)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    SetChrChipByIndex(0x8, 0x25)
    SetChrSubChip(0x8, 0x1)
    SetChrPos(0x8, -96900, 50, 49350, 270)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x31)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, -98400, 700, 48350, 135)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x9, -99000, 0, 40500, 0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, -99000, 0, 40500, 0)
    SetChrPos(0x102, -99000, 0, 40500, 0)
    SetChrPos(0x104, -99000, 0, 40500, 0)
    SetChrPos(0x109, -99000, 0, 40500, 0)
    SetChrPos(0x105, -99000, 0, 40500, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-98700, 1100, 44800, 0)
    MoveCamera(27, 19, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21500, 0)
    OP_68(-98700, 1100, 46800, 4000)
    MoveCamera(41, 13, 0, 4000)
    OP_6E(450, 4000)
    SetCameraDistance(19290, 4000)
    FadeToBright(1000, 0)
    BeginChrThread(0x101, 3, 0, 7)
    BeginChrThread(0x102, 3, 0, 8)
    BeginChrThread(0x104, 3, 0, 9)
    BeginChrThread(0x109, 3, 0, 10)
    BeginChrThread(0x105, 3, 0, 11)
    BeginChrThread(0x9, 3, 0, 12)
    WaitChrThread(0x105, 3)

    ChrTalk(
        0x101,
        "#6P#00005FAh…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -96900, 0, 48600, 225)
    OP_0D()
    PlayBGM("ed7519", 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "Ehe, Nice to meet you\x02\x03",
            "King of Libert, the Otodo\x01",
            "I am Claudia.\x02\x03",
            "Call me in such a form\x01",
            "I'm so sorry.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0xC,
        "#5P#08009FScree\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00011FN-not at all\x02\x03",
            "#00003FNice to meet you ──\x01",
            "Crossbell Police, Special Affairs Support Division's\x01",
            "It is Lloyd · Bannings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00104FAlso,\x01",
            "It is Erie · Mcdael.\x02\x03",
            "#00102FYou are being placed in your Highness Prince Wang\x01",
            "Good mood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07009F#5PHehe, what about Ellie?\x01",
            "Actually, I heard a lot ……\x02\x03",
            "#07002FI'm glad to meet you\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#6P#00105FIs that right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07004F#5PYes, my grandfather's\x01",
            "Mr. MacDaely and Mr. President\x01",
            "I got the opportunity to talk.\x02\x03",
            "#07000FAlso, with Mariavell\x01",
            "I have some acquaintance several times.\x02\x03",
            "Everything before, also in Libert\x01",
            "Did you have an experience you were studying abroad?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00104FYes.\x01",
            "I stayed for about 3 months … …\x02\x03",
            "#00102FI apologize for not being able to meet you then\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#07009FNo not at all, same here\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FHa ha …. Thank you.\x01",
            "Randy Orlandosis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#N#10100FNo, it is Noel · seeker!\x01",
            "Thank you!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#12P#10304FWadi Hemisphere.\x01",
            "Beautiful#2RNoisy#It is an honor to meet the Princess.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#07009F#5PEhe, welcome all of you\x02\x03",
            "#07004FIf true, another person in this place,\x01",
            "There were people who wanted to introduce … …\x02\x03",
            "#07000FUh, but it seems he's a bit late\x02",
        )
    )

    CloseMessageWindow()
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x3)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -99000, 0, 39000, 0)
    VolumeBGM(0x32, 0x12C)
    Sound(849, 0, 100, 0)
    Sleep(2000)
    VolumeBGM(0x64, 0x3E8)

    NpcTalk(
        0xA,
        "Bold voice",
        (
            "Hydrofluoric acid\x01",
            "I do not need to worry.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 2)), scpexpr(EXPR_END)), "loc_1E13")

    def lambda_144D():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_144D)

    def lambda_145A():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_145A)
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

    def lambda_14EE():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_14EE)
    Sleep(50)

    def lambda_14FE():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_14FE)
    Sleep(50)

    def lambda_150E():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_150E)
    Sleep(50)

    def lambda_151E():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_151E)
    Sleep(50)

    def lambda_152E():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_152E)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#00005F#5PThat sound…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#5PI-I feel like I've heard it\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F#5PNo way it couldn't be…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#07104F#5PGiggle\x01",
            "You seem to have come.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-94200, 900, 101100, 0)
    MoveCamera(53, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x8, -101300, 0, 103300, 135)
    SetChrPos(0xC, -100800, 700, 102000, 90)
    SetChrPos(0x9, -99500, 0, 104700, 135)
    SetChrPos(0x101, -97700, 0, 99100, 0)
    SetChrPos(0x102, -97900, 0, 97700, 0)
    SetChrPos(0x104, -96700, 0, 97500, 0)
    SetChrPos(0x109, -96500, 0, 98900, 0)
    SetChrPos(0x105, -95300, 0, 98700, 315)
    SetChrPos(0xA, -92000, 0, 101200, 270)
    SetChrPos(0xB, -92000, 0, 101000, 270)
    ClearChrFlags(0xB, 0x80)
    OP_68(-95880, 900, 101590, 3000)
    MoveCamera(62, 16, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(15300, 3000)

    def lambda_1702():
        OP_95(0xFE, -96300, 0, 101200, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1702)

    def lambda_171C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_171C)
    Sleep(700)

    def lambda_1730():
        OP_95(0xFE, -95100, 0, 101000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1730)

    def lambda_174A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_174A)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#6P#00011F#4SHUH!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10111FMaybe\x01",
            "Request for support earlier! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#07005F#6P#NOh? You've already met?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#12P#00109FY-yes, actually\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FGiggle\x01",
            "It's a soldier surprise.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Imperial army officer",
        (
            "#5P#07303FI apologize for before all of you\x02\x03",
            "#07308F#11PHis Highness Claudia ……\x01",
            "Sorry for being late.\x02\x03",
            "#07301FAs usual, this play#2RTawa#Injury\x01",
            "I was thrusting my neck in various ways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#07009F#6P#NEhe, well\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(850, 0, 100, 0)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xA, 0x20)
    SetChrChipByIndex(0xA, 0x2B)
    SetChrSubChip(0xA, 0x0)
    Sleep(100)
    SetChrSubChip(0xA, 0x1)
    Sleep(100)
    SetChrSubChip(0xA, 0x2)
    Sleep(100)
    SetChrSubChip(0xA, 0x3)
    Sleep(100)
    SetChrSubChip(0xA, 0x4)
    Sleep(100)
    SetChrSubChip(0xA, 0x3)
    Sleep(100)
    SetChrSubChip(0xA, 0x2)
    Sleep(100)
    SetChrSubChip(0xA, 0x1)
    Sleep(100)
    SetChrSubChip(0xA, 0x0)
    Sleep(100)
    SetChrSubChip(0xA, 0x1)
    Sleep(100)
    SetChrSubChip(0xA, 0x2)
    Sleep(100)
    SetChrSubChip(0xA, 0x3)
    Sleep(100)
    SetChrSubChip(0xA, 0x4)
    Sleep(100)
    SetChrSubChip(0xA, 0x3)
    Sleep(100)
    SetChrSubChip(0xA, 0x2)
    Sleep(100)
    SetChrSubChip(0xA, 0x1)
    Sleep(100)
    SetChrSubChip(0xA, 0x0)
    Sleep(300)
    OP_63(0xA, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    SetChrSubChip(0xA, 0x8)
    Sleep(130)
    Sound(822, 0, 100, 0)
    SetChrSubChip(0xA, 0x9)
    Sleep(130)
    SetChrSubChip(0xA, 0xA)
    Sleep(500)
    SetChrSubChip(0xA, 0xB)
    Sleep(130)
    SetChrSubChip(0xA, 0xC)
    Sleep(130)
    SetChrSubChip(0xA, 0xD)
    Sleep(130)
    SetChrSubChip(0xA, 0xE)
    Sleep(130)
    SetChrSubChip(0xA, 0xF)
    Sleep(500)
    OP_64(0xA)
    SetChrChipByIndex(0xA, 0x2A)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x2)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xA, 0x20)
    OP_93(0xA, 0xB4, 0x1F4)
    Sleep(300)

    def lambda_1AAA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1AAA)

    NpcTalk(
        0xA,
        "Blond hair youth",
        (
            "#5P#07204F── Hui, once again\x01",
            "Let me introduce myself.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    SetMessageWindowPos(14, 280, -1, 3)
    Sleep(500)
    SetChrName("Blond hair youth")

    AnonymousTalk(
        0xFF,
        (
            "Eleventh Empire, Emperor Yugent is a name,\x01",
            "Oliverto · Rise · Arnol.\x02\x03",
            "Of course, the true figure is\x01",
            "As a genius of unprecedented bleachers,\x01",
            "Although it is Olivier · Renheim!\x02\x03",
            "Ha ha ha ha.\x01",
            "Thank you for asking.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    ChrTalk(
        0x101,
        "#6P#00011F…….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00301FNo that can't be\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Imperial army officer",
        (
            "#5P#07306FThis is the reality.\x01",
            "It is very regrettable.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Imperial army officer")

    AnonymousTalk(
        0xFF,
        (
            "─ ─ Imperial Army, 7 th Armored Division affiliation,\x01",
            "Major Mueller-Vandarl.\x02\x03",
            "At the invitation of your Highness Claudia\x01",
            "Together, I got invited.\x02\x03",
            "Nice to meet you, SSS\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    Jump("loc_271C")

    label("loc_1E13")


    def lambda_1E18():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1E18)

    def lambda_1E25():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1E25)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    def lambda_1EAD():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1EAD)
    Sleep(50)

    def lambda_1EBD():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1EBD)
    Sleep(50)

    def lambda_1ECD():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1ECD)
    Sleep(50)

    def lambda_1EDD():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1EDD)
    Sleep(50)

    def lambda_1EED():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1EED)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#00005F#5PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#5PSound of the lute … …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#07104FGiggle\x01",
            "You seem to have come.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-94200, 900, 101100, 0)
    MoveCamera(53, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x8, -101300, 0, 103300, 135)
    SetChrPos(0xC, -100800, 700, 102000, 90)
    SetChrPos(0x9, -99500, 0, 104700, 135)
    SetChrPos(0x101, -97700, 0, 99100, 0)
    SetChrPos(0x102, -97900, 0, 97700, 0)
    SetChrPos(0x104, -96700, 0, 97500, 0)
    SetChrPos(0x109, -96500, 0, 98900, 0)
    SetChrPos(0x105, -95300, 0, 98700, 315)
    SetChrPos(0xA, -92000, 0, 101200, 270)
    SetChrPos(0xB, -92000, 0, 101000, 270)
    ClearChrFlags(0xB, 0x80)
    OP_68(-95880, 900, 101590, 3000)
    MoveCamera(62, 16, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(15300, 3000)

    def lambda_2089():
        OP_95(0xFE, -96300, 0, 101200, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2089)

    def lambda_20A3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_20A3)
    Sleep(700)

    def lambda_20B7():
        OP_95(0xFE, -95100, 0, 101000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_20B7)

    def lambda_20D1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_20D1)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00011FAh…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10111FE, of the Eleven Empire ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105FPrince Oliver's Prince … …! Is it?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x8, 500)
    Sleep(150)

    NpcTalk(
        0xB,
        "Imperial army officer",
        (
            "#07303F#11P── His Highness, Claudia,\x01",
            "Sorry for being late.\x02\x03",
            "#07301FAs usual, this play#2RTawa#Injury\x01",
            "I was thrusting my neck in various ways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#07009F#6P#NEhe, well\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(850, 0, 100, 0)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xA, 0x20)
    SetChrChipByIndex(0xA, 0x2B)
    SetChrSubChip(0xA, 0x0)
    Sleep(100)
    SetChrSubChip(0xA, 0x1)
    Sleep(100)
    SetChrSubChip(0xA, 0x2)
    Sleep(100)
    SetChrSubChip(0xA, 0x3)
    Sleep(100)
    SetChrSubChip(0xA, 0x4)
    Sleep(100)
    SetChrSubChip(0xA, 0x3)
    Sleep(100)
    SetChrSubChip(0xA, 0x2)
    Sleep(100)
    SetChrSubChip(0xA, 0x1)
    Sleep(100)
    SetChrSubChip(0xA, 0x0)
    Sleep(100)
    SetChrSubChip(0xA, 0x1)
    Sleep(100)
    SetChrSubChip(0xA, 0x2)
    Sleep(100)
    SetChrSubChip(0xA, 0x3)
    Sleep(100)
    SetChrSubChip(0xA, 0x4)
    Sleep(100)
    SetChrSubChip(0xA, 0x3)
    Sleep(100)
    SetChrSubChip(0xA, 0x2)
    Sleep(100)
    SetChrSubChip(0xA, 0x1)
    Sleep(100)
    SetChrSubChip(0xA, 0x0)
    Sleep(300)
    OP_63(0xA, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    SetChrSubChip(0xA, 0x8)
    Sleep(130)
    Sound(822, 0, 100, 0)
    SetChrSubChip(0xA, 0x9)
    Sleep(130)
    SetChrSubChip(0xA, 0xA)
    Sleep(500)
    SetChrSubChip(0xA, 0xB)
    Sleep(130)
    SetChrSubChip(0xA, 0xC)
    Sleep(130)
    SetChrSubChip(0xA, 0xD)
    Sleep(130)
    SetChrSubChip(0xA, 0xE)
    Sleep(130)
    SetChrSubChip(0xA, 0xF)
    Sleep(500)
    OP_64(0xA)
    SetChrChipByIndex(0xA, 0x2A)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x2)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xA, 0x20)
    OP_93(0xA, 0xB4, 0x1F4)
    Sleep(300)

    def lambda_2387():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2387)

    ChrTalk(
        0xA,
        "#5P#07204FHuh, nice to meet you.\x02",
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    SetMessageWindowPos(14, 280, -1, 3)
    Sleep(500)

    AnonymousTalk(
        0xA,
        (
            "Eleventh Empire, Emperor Yugent is a name,\x01",
            "Oliverto · Rise · Arnol.\x02\x03",
            "Well, to be honest, than Prince\x01",
            "As a bleaching performer seeking love\x01",
            "I'd like to go on a trip.\x02\x03",
            "Ha ha ha ha.\x01",
            "Thank you for asking.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    ChrTalk(
        0x101,
        "#6P#00011FOh, um … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00109FOh, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00305FWhat is the Empire of the Empire\x01",
            "It's as light as I thought … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305FI mean, why lute?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Imperial army officer",
        (
            "#5P#07306FWell, as for kore\x01",
            "Please sink it if possible.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Imperial army officer")

    AnonymousTalk(
        0xFF,
        (
            "─ ─ Imperial Army, 7 th Armored Division affiliation,\x01",
            "Major Mueller-Vandarl.\x02\x03",
            "At the invitation of your Highness Claudia\x01",
            "Together, I got invited.\x02\x03",
            "Nice to meet you, SSS\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)

    label("loc_271C")

    SetCameraDistance(15800, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis313.itp")
    CreatePortrait(1, 160, 8, 416, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis314.itp")
    CreatePortrait(2, 160, 8, 416, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis315.itp")
    SetChrChipByIndex(0x8, 0x25)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xA, 0x26)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x22)
    SetChrSubChip(0xC, 0x2)
    SetChrPos(0x8, -96900, 50, 50900, 270)
    SetChrPos(0x9, -96900, 50, 52400, 270)
    SetChrPos(0xA, -96900, 50, 49350, 270)
    SetChrPos(0xB, -96900, 50, 47850, 270)
    SetChrPos(0xC, -98400, 700, 46000, 0)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 0x2C)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x2D)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0x2E)
    SetChrSubChip(0x104, 0x2)
    SetChrChipByIndex(0x109, 0x2F)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x30)
    SetChrSubChip(0x105, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, -101100, 50, 49350, 90)
    SetChrPos(0x102, -101100, 50, 50900, 90)
    SetChrPos(0x104, -101100, 50, 52400, 90)
    SetChrPos(0x109, -101100, 50, 47850, 90)
    SetChrPos(0x105, -101100, 50, 46450, 90)
    OP_68(-99250, 1600, 50090, 0)
    MoveCamera(38, 14, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(18950, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00004FI see……\x01",
            "Girlfriend#4Rester#Did you hear from us?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(-99250, 1100, 50090, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x102,
        (
            "#6P#00102FEveryone with Esther\x01",
            "It was a relationship with adventure ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FHaha, it keeps on\x01",
            "It's a terrible combination.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07204FWell, with that kind of work\x01",
            "Please bear in mind.\x02\x03",
            "#07202FBokura and Esther guys\x01",
            "A friend who faced an incident of Libert.\x02\x03",
            "And you and yours\x01",
            "A companion who faced an unusual change of Crossbell.\x02\x03",
            "#07209FIn other words,\x01",
            "It is a friend of destiny ♪\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00012FNo~.\x01",
            "I wonder if it is not so simple.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106FThat……\x01",
            "Honestly#2RLate#There are many.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#07004FHuh but, really\x01",
            "Please feel easy.\x02\x03",
            "#07002FI have something I would like to consult with\x01",
            "I certainly called you … …\x02\x03",
            "Beyond that, as you come closer to you\x01",
            "I thought that I wanted to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYour majesty…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00309FOhh, that's kind of awesome\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10112FW-we're honored!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07204FBut you also esters\x01",
            "Apparently I enjoyed it with Crossbell\x01",
            "You seem to have been spending it.\x02\x03",
            "#07209FThere are also theme parks,\x01",
            "I have stayed for about a month, too -\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x2)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#07303F…… Your schedule is\x01",
            "You are buried over half a year.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#07201F#5PMuller's Ike!\x01",
            "You can dream about it!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1300)
    SetChrSubChip(0x9, 0x1)
    Sleep(150)

    ChrTalk(
        0x9,
        (
            "#5P#07104FWell, for that reason\x01",
            "This is about you guys\x01",
            "It is a state that you know all the way.\x02\x03",
            "#07100FBased on that, some of you guys\x01",
            "There is something I want to tell … …\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)
    Sleep(50)
    SetChrSubChip(0xA, 0x0)

    ChrTalk(
        0x101,
        (
            "#6P#00001F── Yes.\x01",
            "That's the main theme.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00101FAnything concerning trade meeting\x01",
            "Do you have any information you care about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11P#07003FYes…\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    SetChrSubChip(0x8, 0x2)
    Sleep(300)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, -96900, 0, 53400, 270)
    OP_0D()
    OP_92(0x9, 0xFFFE8CE8, 0xD6D8, 0x1F4)

    def lambda_302E():
        OP_95(0xFE, -95000, 0, 55000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_302E)
    SetChrSubChip(0x109, 0x1)
    SetChrSubChip(0x104, 0x0)
    Sleep(50)
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x104, 0x1)
    WaitChrThread(0x9, 1)
    OP_93(0x9, 0x2D, 0x1F4)
    OP_68(-99000, 1000, 54550, 2000)
    MoveCamera(20, 17, 0, 2000)
    SetCameraDistance(20000, 2000)
    OP_6F(0x79)
    Sound(72, 0, 100, 0)
    OP_74(0x4, 0xF)
    OP_71(0x4, 0xB, 0x14, 0x0, 0x0)
    OP_79(0x4)
    Sleep(500)
    Sound(939, 0, 50, 0)
    OP_71(0x4, 0x15, 0x1E, 0x0, 0x0)
    OP_79(0x4)
    OP_74(0x4, 0x1E)
    OP_24(0x3AB)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)

    AnonymousTalk(
        0x109,
        "#10105FAh…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00000FEpstein Foundation's\x01",
            "You are using a system, are not you?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x9,
        (
            "#07104FOh, this ship's information processing system\x01",
            "We are introducing the Foundation's stuff.\x02\x03",
            "#07101FPlease look here\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(1021, 0, 100, 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_70(0x4, 0x28)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7151", 0)
    Sleep(500)

    AnonymousTalk(
        0x102,
        (
            "#00108F… … Evonian empire,\x01",
            "It is Gillius Osbourne Excellency.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0xA,
        (
            "#07200FThe Iron Blood Chancellor, just call him that\x02\x03",
            "To you who do not know his life\x01",
            "I do not mean to speak ill here.\x02\x03",
            "#07203FJust as one assumption\x01",
            "There is something I want you to know.\x02\x03",
            "#07201F── Currently within the Eleventh Empire\x01",
            "I do not care when a civil war will happen.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-99250, 1100, 50090, 0)
    MoveCamera(38, 14, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(18950, 0)
    SetChrSubChip(0x8, 0x0)
    TurnDirection(0x9, 0x8, 0)
    SetChrSubChip(0x104, 0x2)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x1, 0x3)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00013FWhat!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10107FR-really!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07206FIt's unfortunate but it's true\x02\x03",
            "#07208FSpecifically, it is centered on the prime minister\x01",
            "A new centralized system in the empire\x01",
            "\"Innovation faction\" trying to build up … …\x02\x03",
            "And with leading noblemen,\x01",
            "Trying to keep the old noble family system\x01",
            "\"Aristocrat\" … …\x02\x03",
            "#07201F─ ─ The confrontation between these two\x01",
            "I am going as far as to get there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00001FReformists versus nobles\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106F…… I was listening to the story\x01",
            "It seems like a serious situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#N#10300FHmm, I guess,\x01",
            "Is your husband in neutral position?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#07202FHuff, rather than neutral\x01",
            "I am planning to go through the third road.\x02\x03",
            "#07206FWell, either side\x01",
            "It is seen in a scattering bat\x01",
            "It's a bad position though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#07303FI can't deny that\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00008FBut, however …\x01",
            "The conflict between the two until just before the civil war\x01",
            "To say that you are arriving ……\x02\x03",
            "#00013FNo way about trade meeting\x01",
            "\"What is worrisome\" is! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10111FAh…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#N#10306FI see..\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        (
            "#07306FIt's as you suspect\x02\x03",
            "#07301FBe an influential person of \"aristocrat\"\x01",
            "There was movement in the public of Cayenne.\x02\x03",
            "Apparently, during this trade conference,\x01",
            "Terrorist who aims at Osborne's Prime Minister\x01",
            "It seems to send it to the crossbell.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#6P#00010FAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00101FThat, not a thugs\x01",
            "Is terrorist … …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07203FThe Prime Minister is also from outside the aristocracy\x01",
            "You are buying a hard resentment.\x02\x03",
            "The forces which were repressed domestically and abroad\x01",
            "We are forming a terrorist organization.\x02\x03",
            "#07201FSuch people, the aristocrats well\x01",
            "That is why I am using Mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00301FSo that's it\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#N#10304FDo not soil their hands\x01",
            "It 's okay to bury a political opponent.\x02\x03",
            "#10305FBut when that happens\x01",
            "Would not it be various Masui?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x101, 0x2)
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#5P#00007FI'm not at home!\x01",
            "It's also a big problem for crossbells!\x02\x03",
            "#00010FDuring the meeting held by the mayor\x01",
            "If the prime minister of the empire was assassinated\x01",
            "What kind of compensation is required ----\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        "#6P#00006FS-sorry\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07204FNo, we're worried about that too\x02\x03",
            "#07201FAs a price not to prevent the assassination\x01",
            "From the Empire to the Crossbell Autonomous Region\x01",
            "A huge amount of compensation will be confronted.\x02\x03",
            "Even if it is within the Empire\x01",
            "Even things that arise from conflict problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10106FU-unblelievable\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108F… … It looks ruthless\x01",
            "That is another aspect of diplomacy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00306FThat's right\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#07008FAlso…\x02\x03",
            "#07003FIn fact the same composition\x01",
            "It is also in the Republic.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00011FHuh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FReally?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x2)
    Sleep(300)

    ChrTalk(
        0x8,
        "#11P#07001FJulia, please\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#07100FRight\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x2D, 0x1F4)
    SetChrSubChip(0x109, 0x1)
    SetChrSubChip(0x104, 0x1)
    Sleep(50)
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x102, 0x1)
    Sleep(300)
    OP_74(0x4, 0xF)
    Sound(1021, 0, 100, 0)
    OP_71(0x4, 0x29, 0x32, 0x0, 0x0)
    OP_79(0x4)
    OP_74(0x4, 0x1E)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(1000)

    AnonymousTalk(
        0x102,
        (
            "#00101FRepresentative of the Republic of Calvert,\x01",
            "President Samuel Rock Smith ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x105,
        (
            "#10301FOgisan of this one\x01",
            "Do you have a resentment?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x8,
        (
            "#07003FNo, rather than what he is\x01",
            "It depends on the history of Calvert.\x02\x03",
            "In the West Zemria, various cultures\x01",
            "To the Calvado we have taken from the old days\x01",
            "There is a very difficult problem.\x02\x03",
            "#07001FIn other words, it's a racial issue\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        "#10101FA racial issue…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x9,
        (
            "#07103FAs you know, Calvado has long been\x01",
            "It is a country that has accepted immigrants of the eastern side.\x02\x03",
            "#07108FSince the transition to the Republic\x01",
            "It becomes noticeable, and a huge Oriental city street etc.\x01",
            "I was supposed to be born … ….\x02\x03",
            "#07101FNaturally, against such a flow\x01",
            "There is a reactionary thing.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00106FThe anti eastern immigration policy right?\x02\x03",
            "#00108FSuch movement exists in\x01",
            "I knew it as knowledge … …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00001FSuch a nationalist\x01",
            "Are you aiming at the president?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x8,
        (
            "#07003FYeah, I still have an abundant funding source\x01",
            "It seems that there is a sponsor ……\x02\x03",
            "#07001FThe latest armed militant extremist#6Rterrorist#But\x01",
            "Information that it is moving is contained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#00008F….\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        "#00303FThat's quite troubling\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x8, 0x0)
    TurnDirection(0x9, 0x8, 0)
    SetChrSubChip(0x104, 0x2)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)

    def lambda_430F():
        OP_95(0xFE, -96900, 0, 53300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_430F)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x2, 0x3)
    Sound(73, 0, 100, 0)
    OP_71(0x4, 0x33, 0x3C, 0x0, 0x0)
    WaitChrThread(0x9, 1)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, -96900, 50, 52400, 270)
    OP_0D()
    SetChrSubChip(0x9, 0x1)
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#6P#00006FWe understand\x02\x03",
            "#00001FHowever, why such a\x01",
            "A serious story to ourselves …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#N#10300FIndeed, directly to the autonomous state government\x01",
            "Is not it better to tell?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)
    OP_64(0x9)
    OP_64(0xA)
    OP_64(0xB)

    ChrTalk(
        0x102,
        (
            "#6P#00106F…… I want to tell you\x01",
            "There are circumstances that can not be told.\x02\x03",
            "#00101FThat's what it is right?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(100)

    ChrTalk(
        0x101,
        "#6P#00005FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07203FIt's as Elie says\x02\x03",
            "#07208FEven if you are the Osborne president\x01",
            "Even for President Rock Smith ……\x02\x03",
            "Naturally, the power to target them\x01",
            "You should know that it is moving.\x02\x03",
            "#07201FDespite this, the Crossbell government\x01",
            "That fact has not been totaken at all.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        "#6P#00013FAh…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#07003FWhat kind of speculation is there?\x01",
            "I do not know at the moment … …\x02\x03",
            "#07008FHowever, in such a situation\x01",
            "This is the back circumstances of the Empire and the Republic\x01",
            "I can not tell it without permission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07206FAnd I am also an imperial family,\x01",
            "I can not interfere with the policies of the Imperial Government … …\x02\x03",
            "#07200FSo at the suggestion of Princess Hime\x01",
            "That is why you called you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FI see…\x02\x03",
            "#00000FIn other words, the story here\x01",
            "Is it an unofficial to the last?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#07009FYes, those with common friends\x01",
            "A little chat in the tea room ……\x02\x03",
            "#07002FOf course, the gossip that I heard there\x01",
            "It is free to tell anyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00102FAha, I see\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FNo, no …\x01",
            "It is more bold than I thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#N#10302FHuff, for an elegant princess\x01",
            "You seem to be quite a handy one, are not you?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x109, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    SetChrSubChip(0x109, 0x2)
    Sleep(150)

    ChrTalk(
        0x109,
        (
            "#5P#10111FWait a minute, a bit.\x01",
            "Anything is rude …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#07004FEhe, it's fine\x02\x03",
            "#07008FThe circumstances surrounding the crossbell are\x01",
            "I am getting increasingly confused …\x02\x03",
            "#07000FIn order to improve the forecast even a little\x01",
            "There is nothing wrong with doing a sorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07206FEven just for the troublesome people\x01",
            "Information is being controlled\x01",
            "I do not see it.\x02\x03",
            "#07200FAbout Esther's connection\x01",
            "I have to make use of it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x109, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    SetChrSubChip(0x109, 0x0)
    OP_63(0x105, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00005FThe troubling guys\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#07003FI think you know them\x02\x03",
            "#07001FMr. Rector Alain Dorr\x01",
            "I am two of Ms. Kirika Lawran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00001FAh…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FI see..\x02\x03",
            "#00101FThe information I gave you to the Crossbell government\x01",
            "It is hardly communicated … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#07103FI believe those two are also information gatherers\x02\x03",
            "#07100FMs. Kirika was originally Libert\x01",
            "Although he was a receptionist of the Association of Priests\x01",
            "Hidden eyes to be a clairvoyant#4RCapital#You owner.\x02\x03",
            "With that information operation\x01",
            "It should be done without pain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00008FI see..\x01",
            "I heard even the guild people … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FRegardless of the ally, turning to the enemy\x01",
            "It is the most troublesome type … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#07303FAnd Lechter Arundel\x02\x03",
            "Unknown background, unknown yet\x01",
            "There is one thing that is clear.\x02\x03",
            "#07301FIt is \"Iron-Blooded Children#12RIdeal Bleed#It is called\x01",
            "That is one of the members.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10111FI-Iron Breed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#N#10306FAnother over the top name\x02\x03",
            "#10300FApparently I have a connection with the Iraqi Prime Minister\x01",
            "It looks like a member?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#07203FThe Prime Minister picked it up\x01",
            "It seems that they are young children.\x02\x03",
            "Although there is a habit, it is frighteningly capable\x01",
            "It seems to be doing various work.\x02\x03",
            "#07200FFrom aristocrats to the utmost\x01",
            "You seem to be alarmed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11P#07008F…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00003F…… \"Iron Blood Children#12RIdeal Bleed#\".\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108FMore than mere information officers\x01",
            "It seems like a hard party ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#07103F…… In addition, currently living in Crossbell\x01",
            "There are also problems of \"black moon\" and \"red constellation\".\x02\x03",
            "#07100FBecause they seem to be connected with the government\x01",
            "I do not think I will aim for a conference ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#07303FBut what is showing cryptic movements is\x01",
            "It is transmitted to here.\x02\x03",
            "#07300FAs for that, you guys\x01",
            "Although it may be detailed to the actual situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FYes…\x02\x03",
            "#00000F── What is it called returning?\x01",
            "About what we know at present\x01",
            "I will tell you.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd's \"Red constellation\"\x01",
            "I explained the movement of \"Black Moon\".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(
        0x9,
        "#5P#07105FI see…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#07301FHmm, that \"silver#2RIn#\"Thug users\x01",
            "Somewhat concerned … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07204FWell, the Prime Minister and me\x01",
            "I wonder if there is no worry aiming?\x02\x03",
            "#07200FAnd \"red constellation\" is\x01",
            "It seems to be a frightful combat hunting corps.\x02\x03",
            "I do not have much escorts\x01",
            "The other party like me as a target\x01",
            "Is not it enough?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FHa ha …\x01",
            "That may be so.\x02\x03",
            "#00300FIf there is a Major of Mr. there\x01",
            "A battle#2RYa#I heard that there are also people to follow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#07303FHe is one soldier.\x01",
            "It would not be realistic either.\x02\x03",
            "#07300FIn any case, at the present moment\x01",
            "Assuming every situation\x01",
            "It seems to be only to be prepared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P#07108FThat's right\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)

    ChrTalk(
        0x8,
        (
            "#11P#07004F── Everyone.\x01",
            "Thank you for telling me.\x02\x03",
            "#07002FThanks to this\x01",
            "It seems to be able to deal with various situations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002FN-no, not at all\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00102FThose who purposely bother\x01",
            "Tell me important information … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10109FThank you so much!\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)

    ChrTalk(
        0xA,
        (
            "#07209FHaha, no problem\x02\x03",
            "#07202FBut if that's the case\x01",
            "Thanks to the cross-bell sights of the night as well\x01",
            "Would you like me to show you around?\x02\x03",
            "Waji and Randy something\x01",
            "It seems to be detailed in various ways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00305FOh yeah that would be cool\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#N#10309FHuh, if you keep that\x01",
            "I think I can guide you to the spot.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#07212FOh, if you decide so\x01",
            "Cancel the dinner party ----\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x2)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#07306FShut up, moron\x02\x03",
            "#07301FFrom now on the alkane shell\x01",
            "I wonder if the performance will also be watching.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#07201F#5POh that's right\x02\x03",
            "#07206FWell, alkane shell, once,\x01",
            "I wanted to see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00012Fmy mother……\x01",
            "I'm sure you can enjoy it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00109FYes, to be rounded\x01",
            "I think that it is a guarantee.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)
    Sleep(50)
    SetChrSubChip(0xA, 0x0)

    ChrTalk(
        0x8,
        (
            "#11P#07009FHeh, we're very excited\x02\x03",
            "#07002F…… If something happens again\x01",
            "We will also contact you.\x02\x03",
            "Do not rely on Sieg this time,\x01",
            "I will give you direct communication.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11P#08009FScree\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00004FHaha, thanks for that\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00302FAs expected\x01",
            "I thought it was something.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19450, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    OP_24(0x1F2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    SetScenarioFlags(0x22, 2)
    NewScene("c010B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_597 end

    SaveToFile()

Try(main)
