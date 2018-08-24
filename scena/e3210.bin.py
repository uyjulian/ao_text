from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Princess Klaudia",       # 1
        "Captain Julia",          # 2
        "Prince Olivert",         # 3
        "Major Mueller",          # 4
        "Sieg",                   # 5
        "Bodyguard",              # 6
        "Bodyguard",              # 7
        "Bodyguard",              # 8
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
            "#11P#07104F─Excuse me, Your\x01",
            "Highness.\x02\x03",
            "I've brought the Special\x01",
            "Support Section, as you\x01",
            "requested.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Cool Voice",
        "#3C#2S#11PPlease, enter.\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(100, 0, 80, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x2)

    def lambda_BCC():
        OP_95(0xFE, -97800, 70, 3200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_BCC)
    WaitChrThread(0x9, 1)
    OP_93(0x9, 0xE1, 0x1F4)

    def lambda_BF1():

        label("loc_BF1")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_BF1")

    QueueWorkItem2(0x9, 2, lambda_BF1)

    ChrTalk(
        0x9,
        "#5P#07102FDo come in.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00001FR-Right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104FExcuse us.\x02",
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
        "#6P#00005FAh...\x02",
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
            "Haha, how do you do.\x02\x03",
            "I am the Liberl Kingdom's Crown\x01",
            "Princess Klaudia.\x02\x03",
            "I do apologize for having called\x01",
            "you all out here like this.\x02",
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
        "#5P#08009FScree.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00011FN-No, don't worry about it.\x02\x03",
            "#00003FHow do you do─ I am Lloyd\x01",
            "Bannings of the Crossbell\x01",
            "Police Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00104FElie MacDowell, of the\x01",
            "same.\x02\x03",
            "#00102FI am pleased to make the\x01",
            "Crown Princess'\x01",
            "acquaintance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07009F#5PHaha, incidentally, I\x01",
            "heard some things about\x01",
            "you, Elie.\x02\x03",
            "#07002FI am so very glad to\x01",
            "meet you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#6P#00105FReally?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07004F#5PYes. I had the chance to speak\x01",
            "with your grandfather, Chairman\x01",
            "MacDowell, a little while ago.\x02\x03",
            "#07000FAnd I have met with Miss\x01",
            "Mariabell several times.\x02\x03",
            "And I'm told that you\x01",
            "previously studied in Liberl?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00104FYes, about three months\x01",
            "ago, but...\x02\x03",
            "#00102FI apologize for not\x01",
            "coming to see you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07009FNo, no. I should\x01",
            "apologize too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FHaha... Hello. I'm Randy\x01",
            "Orlando.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#N#10100FN-Noｱl Seeker! Nice to\x01",
            "meet you!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#12P#10304FWazy Hemisphere. I'm\x01",
            "honored to meet a beautiful\x01",
            "princess such as yourself.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#07009F#5PWelcome, everyone.\x01",
            "Please, come in.\x02\x03",
            "#07004FActually, I wanted to\x01",
            "introduce you to someone\x01",
            "else, but...\x02\x03",
            "#07000FUmm, it seems he's a bit\x01",
            "late.\x02",
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
        "Whistling Voice",
        (
            "*whistle*... No need to\x01",
            "worry.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 2)), scpexpr(EXPR_END)), "loc_1E89")

    def lambda_1464():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1464)

    def lambda_1471():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1471)
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

    def lambda_1505():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1505)
    Sleep(50)

    def lambda_1515():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1515)
    Sleep(50)

    def lambda_1525():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1525)
    Sleep(50)

    def lambda_1535():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1535)
    Sleep(50)

    def lambda_1545():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1545)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#00005F#5PThat sound...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#5PI-I think we've heard\x01",
            "this before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F#5PWhoa, it can't be!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#07104F#5PHaha... It seems he has\x01",
            "arrived.\x02",
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

    def lambda_1721():
        OP_95(0xFE, -96300, 0, 101200, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1721)

    def lambda_173B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_173B)
    Sleep(700)

    def lambda_174F():
        OP_95(0xFE, -95100, 0, 101000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_174F)

    def lambda_1769():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1769)
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
        "#6P#00011F#4SHuh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10111FN-No way! That request\x01",
            "earlier was...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#07005F#6P#NOh, you've already met?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#12P#00109FYes, actually...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302FHaha... What a surprise.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Imperial Army Commisioned Officer",
        (
            "#5P#07303F─Ladies and gentlemen, I\x01",
            "apologize for my actions\x01",
            "earlier.\x02\x03",
            "#07308F#11PI must apologize to\x01",
            "Princess Klaudia too. I'm\x01",
            "terribly sorry we're late.\x02\x03",
            "#07301FThis idiot was getting\x01",
            "himself into all sorts of\x01",
            "trouble, as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#07009F#6P#NHaha, well...\x02",
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

    def lambda_1B0C():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1B0C)

    NpcTalk(
        0xA,
        "Blond Young Man",
        (
            "#5P#07204F─Hmph, allow me to\x01",
            "introduce myself once\x01",
            "again.\x02",
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
    SetChrName("Blond Young Man")

    AnonymousTalk(
        0xFF,
        (
            "I am Olivert Reise Arnor,\x01",
            "representing Emperor Eugent\x01",
            "of Erebonia.\x02\x03",
            "Of course, my true form is\x01",
            "that of unparalleled genius\x01",
            "musician Olivier Lenheim!\x02\x03",
            "Ha ha ha. Nice to meet you.\x02",
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
        "#6P#00011F......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00301FNo, that can't be.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Imperial Army Commisioned Officer",
        (
            "#5P#07306FThis is reality,\x01",
            "regrettable as that is.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Imperial Army Commissioned Officer")

    AnonymousTalk(
        0xFF,
        (
            "─Major Mueller Vander, Imperial\x01",
            "7th Armored Division.\x02\x03",
            "We came at Princess Klaudia's\x01",
            "invitation.\x02\x03",
            "Nice to formally meet you, ladies\x01",
            "and gentlemen of the Special\x01",
            "Support Section.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    Jump("loc_280E")

    label("loc_1E89")


    def lambda_1E8E():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1E8E)

    def lambda_1E9B():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1E9B)
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

    def lambda_1F23():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1F23)
    Sleep(50)

    def lambda_1F33():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1F33)
    Sleep(50)

    def lambda_1F43():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1F43)
    Sleep(50)

    def lambda_1F53():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1F53)
    Sleep(50)

    def lambda_1F63():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1F63)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#00005F#5PHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#5PThe sound of a lute...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#07104FHaha... It seems he has\x01",
            "arrived.\x02",
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

    def lambda_2107():
        OP_95(0xFE, -96300, 0, 101200, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2107)

    def lambda_2121():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2121)
    Sleep(700)

    def lambda_2135():
        OP_95(0xFE, -95100, 0, 101000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2135)

    def lambda_214F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_214F)
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
        "#6P#00011FAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10111FT-The Erebonian\x01",
            "Empire's...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105FCrown Prince\x01",
            "Olivert...!?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x8, 500)
    Sleep(150)

    NpcTalk(
        0xB,
        "Imperial Army Commisioned Officer",
        (
            "#07303F#11P─Princess Klaudia, I'm\x01",
            "terribly sorry we're\x01",
            "late.\x02\x03",
            "#07301FThis idiot was getting\x01",
            "himself into all sorts\x01",
            "of trouble, as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#07009F#6P#NHaha, well...\x02",
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

    def lambda_2419():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2419)

    ChrTalk(
        0xA,
        (
            "#5P#07204F─Hmph, a pleasure,\x01",
            "ladies and gentlemen.\x02",
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

    AnonymousTalk(
        0xA,
        (
            "I am Olivert Reise Arnor,\x01",
            "representing Emperor Eugent of\x01",
            "Erebonia.\x02\x03",
            "Well, to be quite honest, I want to\x01",
            "be a travelling musician seeking\x01",
            "love more than an Imperial prince.\x02\x03",
            "Ha ha ha. Nice to meet you.\x02",
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
        "#6P#00011FAh, umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00109FN-Nice to meet you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00305FYou're more easygoing\x01",
            "than I'd expect from an\x01",
            "Imperial prince...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305FBy the way, what's with\x01",
            "that lute?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Imperial Army Commisioned Officer",
        (
            "#5P#07306FWell, I'd like to avoid\x01",
            "discussing it if I\x01",
            "could.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Imperial Army Commissioned Officer")

    AnonymousTalk(
        0xFF,
        (
            "─Major Mueller Vander, Imperial\x01",
            "7th Armored Division.\x02\x03",
            "We came at Princess Klaudia's\x01",
            "invitation.\x02\x03",
            "Nice to formally meet you, ladies\x01",
            "and gentlemen of the Special\x01",
            "Support Section.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)

    label("loc_280E")

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
            "#00004FI see... So you heard\x01",
            "that from Estelle and\x01",
            "Joshua.\x02",
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
            "#6P#00102FTo think you both went\x01",
            "on an adventure with\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FHaha, you guys must've\x01",
            "been an unbeatable\x01",
            "combo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07204FWell, if thinking that puts\x01",
            "your mind at ease.\x02\x03",
            "#07202FUs, together with Estelle and\x01",
            "Joshua, are the team that stood\x01",
            "against the Liberl phenomenon.\x02\x03",
            "And all of you stood against\x01",
            "the Crossbell phenomenon\x01",
            "together with them.\x02\x03",
            "#07209FIn other words, it's our\x01",
            "destiny to become friends♪\x02",
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
            "#6P#00012FN-No, it can't be that\x01",
            "simple.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106FUh... Honestly, we're\x01",
            "humbled to be in your\x01",
            "presence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#07004FHaha. But really, be at ease.\x02\x03",
            "#07002FWhile it is certainly true that\x01",
            "I called you all here to get\x01",
            "your advice on something...\x02\x03",
            "Additionally, I would like to\x01",
            "get to know all of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FPrincess...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00309FOh, how moving!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10112FAwawa... W-We're\x01",
            "honored!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07204FIt seems Estelle and\x01",
            "Joshua enjoyed their\x01",
            "time in Crossbell.\x02\x03",
            "#07209FThere's even a theme\x01",
            "park. I think I'll stay\x01",
            "for about a month.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x2)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#07303F...Your schedule is full\x01",
            "for half a year, you\x01",
            "know.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#07201F#5PYou meanie! A man can\x01",
            "dream, can't he?\x02",
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
            "#5P#07104FAnd so, we have a\x01",
            "general idea of your\x01",
            "activities.\x02\x03",
            "#07100FBased on that, we have\x01",
            "several things to tell\x01",
            "you...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)
    Sleep(50)
    SetChrSubChip(0xA, 0x0)

    ChrTalk(
        0x101,
        (
            "#6P#00001F─That's the reason\x01",
            "you've called us here,\x01",
            "isn't it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00101FIs it something\x01",
            "concerning the trade\x01",
            "conference?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11P#07003FRight...\x02",
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

    def lambda_3139():
        OP_95(0xFE, -95000, 0, 55000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3139)
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
        "#10105FAh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00000FThat's an Epstein\x01",
            "Foundation system you're\x01",
            "using, isn't it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x9,
        (
            "#07104FYes. People from the\x01",
            "foundation installed this\x01",
            "ship's data processing system.\x02\x03",
            "#07101FPlease look here.\x02",
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
            "#00108FIt's His Excellency,\x01",
            "Chancellor Giliath\x01",
            "Osborne.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0xA,
        (
            "#07200FThe Blood and Iron Chancellor,\x01",
            "he's called.\x02\x03",
            "I have no intention of\x01",
            "speaking ill of the man to\x01",
            "people who have never met him.\x02\x03",
            "#07203FHowever, there is one thing I\x01",
            "would like you all to know.\x02\x03",
            "#07201F─At present, a civil war is\x01",
            "brewing in Erebonia.\x02",
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
        "#6P#00013FWha...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10107FR-Really!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07206FIt's the absolute truth, I'm sorry to say.\x02\x03",
            "#07208FSpecifically between the "Reformist Faction",\x01",
            "who, led by the chancellor, is trying to create\x01",
            "a new centralized authoritarian government.\x02\x03",
            "And the "Noble Faction", who, led by\x01",
            "influential nobles, are trying to maintain the\x01",
            "status quo.\x02\x03",
            "#07201F─These two groups are heading towards conflict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FReformists versus\x01",
            "nobles...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106FI had heard about that\x01",
            "before, but I had no\x01",
            "idea it was so serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#N#10300FHmm. May I then presume\x01",
            "that your position is\x01",
            "neutral, Your Highness?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#07202FHaha. Rather than remain\x01",
            "neutral, I'm thinking of going\x01",
            "with a third option.\x02\x03",
            "#07206FAlthough, it's a tough position\x01",
            "to be in. People from both\x01",
            "sides eye me with suspicion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#07303FWell, I can't deny that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00008FB-But... The civil war between\x01",
            "those two is about to break\x01",
            "out. Does that mean...\x02\x03",
            "#00013FCould the "concerning"\x01",
            "information you have be related\x01",
            "to the trade conference?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10111FAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#N#10306F...I see.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        (
            "#07306F─It is as you fear.\x02\x03",
            "#07301FDuke Cayenne, influential in\x01",
            "the Noble Faction, has acted.\x02\x03",
            "It seems he sent terrorists to\x01",
            "Crossbell to target Osborne\x01",
            "during the trade conference.\x02",
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
        "#6P#00010F...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00101FNot assassins, but\x01",
            "terrorists?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07203FThe chancellor has incurred\x01",
            "the wrath of a group other\x01",
            "than the noble faction.\x02\x03",
            "A powerful terrorist group\x01",
            "has formed within the\x01",
            "Empire.\x02\x03",
            "#07201FIt seems they're using mira\x01",
            "given to them discreetly by\x01",
            "the noble faction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FSo that's what's going\x01",
            "on...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#N#10304FSo they want to bury\x01",
            "their political\x01",
            "opponent, huh?\x02\x03",
            "#10305FBut, that's quite bad\x01",
            "isn't it?\x02",
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
            "#5P#00007FIt's not just bad! It's a disaster for\x01",
            "Crossbell!\x02\x03",
            "#00010FIf the imperial chancellor were to be\x01",
            "assassinated during the trade conference,\x01",
            "I can only guess at the consequences...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        "#6P#00006FS-Sorry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07204FIt's not just that I'm concerned\x01",
            "about.\x02\x03",
            "#07201FThe Empire would thrust enormous\x01",
            "reparations on Crossbell for having\x01",
            "failed to protect its chancellor.\x02\x03",
            "Even though the real cause is\x01",
            "conflict within the Empire itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FI-I don't believe\x01",
            "this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108FIt seems terrible, but\x01",
            "that's just another\x01",
            "aspect of diplomacy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00306F...That's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#07008F─There's more.\x02\x03",
            "#07003FActually, something\x01",
            "similar is happening in\x01",
            "the Republic.\x02",
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
        "#6P#00011F...What!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FR-Really!?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x2)
    Sleep(300)

    ChrTalk(
        0x8,
        "#11P#07001FJulia, if you please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#07100FMa'am.\x02",
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
            "#00101FThe Republican government\x01",
            "representative, President\x01",
            "Samuel Rocksmith.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x105,
        (
            "#10301FIs there some grudge\x01",
            "against him too?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x8,
        (
            "#07003FNo. It's not the man himself, but rather\x01",
            "the history of Calvard.\x02\x03",
            "It's a very difficult problem for\x01",
            "Calvard, which has accepted the various\x01",
            "cultures of West Zemuria for a long time.\x02\x03",
            "#07001FIn other words, it's a problem of Race\x01",
            "Relations.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        "#10101FRace relations...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x9,
        (
            "#07103FAs you know, Calvard has\x01",
            "accepted Eastern immigrants for\x01",
            "a long time.\x02\x03",
            "#07108FWhen it became a Republic, that\x01",
            "flow increased, and the enormous\x01",
            "Eastern Quarter was formed.\x02\x03",
            "#07101FNaturally, there were some who\x01",
            "opposed the influx of migrants.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00106FThe Anti-Immigration\x01",
            "League, right?\x02\x03",
            "#00108FI knew of a movement\x01",
            "like that, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00001FSo those nationalists\x01",
            "are targeting the\x01",
            "President?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x8,
        (
            "#07003FYes. It seems they have a deep-\x01",
            "pocketed sponsor as well...\x02\x03",
            "#07001FRecently, I've gotten word that they\x01",
            "supplied terrorists with weapons and\x01",
            "said terrorists have begun to act.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#00008F............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        "#00303F...That's not good.\x02",
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

    def lambda_4555():
        OP_95(0xFE, -96900, 0, 53300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4555)
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
            "#6P#00006F─We understand.\x02\x03",
            "#00001FBut, why are you telling\x01",
            "US all this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#N#10300FWouldn't contacting the\x01",
            "Crossbell government\x01",
            "directly have been better?\x02",
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
            "#6P#00106FEven if she wanted to,\x01",
            "there's some of this she\x01",
            "could never tell them.\x02\x03",
            "#00101FThat's what it is,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(100)

    ChrTalk(
        0x101,
        "#6P#00005FHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07203FIt's as Elie says.\x02\x03",
            "#07208FChancellor Osborne and\x01",
            "President Rocksmith\x01",
            "both...\x02\x03",
            "They must know of the\x01",
            "actions of the forces\x01",
            "targeting themselves.\x02\x03",
            "#07201FIn spite of this, neither\x01",
            "has told the Crossbell\x01",
            "government anything.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        "#6P#00013F...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#07003FWe don't know what kind of motive each of\x01",
            "them has for keeping quiet at the present\x01",
            "time, but...\x02\x03",
            "#07008FHowever, in a such a situation, we cannot\x01",
            "go telling Crossbell of the behind-the-\x01",
            "scenes affairs of the Empire and Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07206FAnd as a member of its royal family,\x01",
            "I cannot interfere with the policies\x01",
            "of the Imperial government.\x02\x03",
            "#07200FAnd so, the princess called you here\x01",
            "at my suggestion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FI see.\x02\x03",
            "#00000FThen, everything we've\x01",
            "talked about this evening\x01",
            "is off the record, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#07009FYes, it's a chat among\x01",
            "friends at a tea party.\x02\x03",
            "#07002FYou're free to tell\x01",
            "these rumors to anyone\x01",
            "you'd like, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00102FHaha, so that's how it\x01",
            "is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FMan... You guys are\x01",
            "bolder than I thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#N#10302FHaha. For a refined princess\x01",
            "such as yourself, you're\x01",
            "quite shrewd, aren't you?\x02",
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
            "#5P#10111FH-Hey, Wazy. Just how\x01",
            "rude are you going to\x01",
            "be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#07004FHaha, I don't mind.\x02\x03",
            "#07008FThe situation in\x01",
            "Crossbell is growing more\x01",
            "and more chaotic.\x02\x03",
            "#07000FWe struggle in vain to\x01",
            "get even a little clearer\x01",
            "view of the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07206FAt best, it seems all we can do is\x01",
            "control the information we're giving\x01",
            "to each of those troublesome guys.\x02\x03",
            "#07200FWe've got to make good use of\x01",
            "Estelle's connections.\x02",
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
        "#6P#00005FTroubling guys?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#07003FI think you know them.\x02\x03",
            "#07001FThey are Lechter Arundel\x01",
            "and Kilika Rouran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00001F...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103F...I see.\x02\x03",
            "#00101FThen, as for them not telling the\x01",
            "Crossbell government of the\x01",
            "information we've just learned...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#07103FThose two are probably intelligence\x01",
            "operatives.\x02\x03",
            "#07100FAs for Kilika, though she worked as a guild\x01",
            "receptionist before, she possesses insight so\x01",
            "keen, you could only say it's clairvoyance.\x02\x03",
            "With operatives of that level, you could\x01",
            "easily pull that off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00008FI see. We heard about\x01",
            "that in the guild too,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FThough she's an ally,\x01",
            "she'd be tough to deal\x01",
            "with if she were an enemy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#07303FAnd─ Lechter Arundel.\x02\x03",
            "His career history and\x01",
            "origin are unknown, but\x01",
            "we do know one thing.\x02\x03",
            "#07301FHe's said to be a member\x01",
            "of a group called the\x01",
            "Ironbloods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10111FI-Ironbloods?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#N#10306FAnother over the top name,\x01",
            "huh.\x02\x03",
            "#10300FIt sounds like their members\x01",
            "are connected to the Blood\x01",
            "and Iron Chancellor.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#07203FThey're the handpicked young\x01",
            "proteges of the chancellor.\x02\x03",
            "Though they're idiosyncratic, it\x01",
            "seems each possesses frightening\x01",
            "skills and abilities.\x02\x03",
            "#07200FAnd, it seems the noble faction\x01",
            "is on the lookout for them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11P#07008F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00003F...Ironbloods.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108FRather than a simple\x01",
            "intelligence officer, he seems\x01",
            "like a difficult opponent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#07103FOn top of that, there's the problem of\x01",
            "Heiyue and Red Constellation being in\x01",
            "Crossbell, too.\x02\x03",
            "#07100FEach of them has ties to the respective\x01",
            "governments, so I don't think it's likely\x01",
            "they're targeting the conference, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#07303FHowever, we've detected\x01",
            "suspicious movements\x01",
            "from both groups.\x02\x03",
            "#07300FActually, you guys might\x01",
            "be best informed about\x01",
            "the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FRight...\x02\x03",
            "#00000F─We'll tell you\x01",
            "everything we know at\x01",
            "present.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and the others\x01",
            "explained the actions of Red\x01",
            "Constellation and Heiyue.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#5P#07105FSo that's what's going\x01",
            "on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#07301FHmm. That assassin Yin\x01",
            "interests me a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07204FWell, I suppose there's no need\x01",
            "to worry that he's after the\x01",
            "chancellor or myself, right?\x02\x03",
            "#07200FAnd that Red Constellation\x01",
            "seems to be a terribly warlike\x01",
            "jaeger corps.\x02\x03",
            "Perhaps they feel like serving\x01",
            "as my guard is beneath them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FHaha... Could be.\x02\x03",
            "#00300FIf you were there, Major,\x01",
            "I think they'd want to\x01",
            "fight you, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#07303FI'm just a single\x01",
            "soldier. There's no way\x01",
            "I could win.\x02\x03",
            "#07300FIn any case, that's all\x01",
            "the information we have\x01",
            "at present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P#07108FThat's right...\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)

    ChrTalk(
        0x8,
        (
            "#11P#07004F─Everyone. Thank you for\x01",
            "telling us all of this.\x02\x03",
            "#07002FIt seems we'll now be\x01",
            "able to deal with\x01",
            "various situations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002FN-No, it was nothing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00102FAllow us to thank you too.\x01",
            "Thank you for giving us\x01",
            "such valuable information.\x02",
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
            "#07209FHa ha ha, it seems we're both each other's\x01",
            "informants.\x02\x03",
            "#07202FBut if that's how it's going to be, how about\x01",
            "taking me to some of Crossbell's famous night\x01",
            "life to show your gratitude instead?\x02\x03",
            "Wazy and Randy might know a few places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00305FOh, can we go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#N#10309FHaha, well I think I'll\x01",
            "show you to my favorite\x01",
            "spot, then.\x02",
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
            "#07212FYeah! It's decided then.\x01",
            "I just have to cancel\x01",
            "the dinner─\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x2)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#07306F─As if I'd let you do\x01",
            "that, moron.\x02\x03",
            "#07301FWe've got to get to the\x01",
            "Arc-en-Ciel performance\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#07201F#5PMrr... I guess you're\x01",
            "right.\x02\x03",
            "#07206FHmm, I did want to see\x01",
            "Arc-en-Ciel at least\x01",
            "once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00012FHaha... I think you'll\x01",
            "enjoy it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00109FI guarantee you'll stare\x01",
            "in wonder.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)
    Sleep(50)
    SetChrSubChip(0xA, 0x0)

    ChrTalk(
        0x8,
        (
            "#11P#07009FHaha, I'm looking forward\x01",
            "to it.\x02\x03",
            "#07002FI'll contact you again if\x01",
            "anything happens.\x02\x03",
            "Next time, I'll correspond\x01",
            "with you directly, without\x01",
            "relying on Sieg.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11P#08009FScree.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00004FHaha, understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00302FThat's pretty incredible\x01",
            "when you think about it.\x02",
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
