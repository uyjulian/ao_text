﻿from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e4213.bin",                # FileName
        "e4213",                    # MapName
        "e4213",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e4213",                  # 0
        "Estelle",                # 1
        "Joshua",                 # 2
        "Renne",                  # 3
        "Pater-Mater",            # 4
        "SE制御",                 # 5
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(388, 0)                                        # 0

    ScpFunction((
        "Function_0_184",          # 00, 0
        "Function_1_194",          # 01, 1
        "Function_2_195",          # 02, 2
        "Function_3_9B4",          # 03, 3
        "Function_4_9DC",          # 04, 4
        "Function_5_A27",          # 05, 5
        "Function_6_A4B",          # 06, 6
        "Function_7_A6F",          # 07, 7
        "Function_8_AB8",          # 08, 8
        "Function_9_ADC",          # 09, 9
        "Function_10_B1C",         # 0A, 10
        "Function_11_B47",         # 0B, 11
        "Function_12_B7F",         # 0C, 12
        "Function_13_B94",         # 0D, 13
        "Function_14_BB3",         # 0E, 14
        "Function_15_C1B",         # 0F, 15
        "Function_16_CD2",         # 10, 16
        "Function_17_D89",         # 11, 17
        "Function_18_DD0",         # 12, 18
        "Function_19_E48",         # 13, 19
        "Function_20_EF7",         # 14, 20
        "Function_21_FE0",         # 15, 21
        "Function_22_1103",        # 16, 22
        "Function_23_11C7",        # 17, 23
        "Function_24_11E1",        # 18, 24
    ))


    def Function_0_184(): pass

    label("Function_0_184")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_193")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_193")

    Return()

    # Function_0_184 end

    def Function_1_194(): pass

    label("Function_1_194")

    Return()

    # Function_1_194 end

    def Function_2_195(): pass

    label("Function_2_195")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00600.itc", 0x1E)
    LoadChrToIndex("chr/ch00700.itc", 0x1F)
    LoadChrToIndex("chr/ch09500.itc", 0x20)
    LoadChrToIndex("apl/ch51729.itc", 0x21)
    LoadChrToIndex("apl/ch51730.itc", 0x22)
    LoadEffect(0x0, "event/ev17063.eff")
    SoundLoad(132)
    SoundLoad(868)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis344.itp")
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrChipByIndex(0xA, 0x21)
    SetChrSubChip(0xA, 0x18)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xA, 0x1000)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xA, 20500, 0, 4250, 90)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 15000, 0, 5400, 90)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 15000, 0, 6400, 90)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 22000, 0, 3750, 0)
    OP_74(0x0, 0x1E)
    OP_78(0x0, 0xB)
    OP_93(0xB, 0x10E, 0x0)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x8000)
    SetMapObjFlags(0x0, 0x1000)
    OP_70(0x0, 0xA)
    Sound(132, 2, 60, 0)
    Sound(868, 2, 40, 0)
    BeginChrThread(0xC, 1, 0, 22)
    FadeToBright(1000, 0)
    OP_68(-44590, 2800, -10690, 0)
    MoveCamera(17, 8, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(57290, 0)
    SetCameraDistance(54290, 2500)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-44590, 1800, -10690, 0)
    MoveCamera(31, 28, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(45000, 0)
    SetCameraDistance(45000, 2000)
    OP_68(14850, 2400, 8900, 12000)
    MoveCamera(45, 11, 0, 12000)
    Sleep(900)
    OP_6E(500, 11000)
    SetCameraDistance(66770, 11000)
    OP_6F(0x79)
    BeginChrThread(0xC, 1, 0, 23)
    Fade(500)
    OP_68(21680, 1100, 4800, 0)
    MoveCamera(57, 13, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(42000, 0)
    SetCameraDistance(38000, 4000)
    Sleep(3200)
    Fade(500)
    OP_68(21680, 500, 4800, 0)
    MoveCamera(56, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetCameraDistance(17000, 1500)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0x9, 0x8)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0xA,
        (
            "#03315F#6P#40W...Pater-Mater... You're\x01",
            "all right, right...?\x02\x03",
            "Even with such severe\x01",
            "damage... If grandpa\x01",
            "patches you up, then...\x02\x03",
            "You'll be right back to\x01",
            "how you were before...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    BeginChrThread(0xB, 1, 0, 19)
    Sound(903, 0, 70, 0)
    Sleep(1000)
    BeginChrThread(0xA, 1, 0, 3)
    WaitChrThread(0xA, 1)
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xA,
        (
            "#03310F#6P#30WNo... ...It's not true!\x02\x03",
            "#03316F#30W...I won't believe it! I\x01",
            "won't believe iiit!!\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xA, 1, 0, 4)
    WaitChrThread(0xA, 1)
    Sleep(300)
    Fade(500)
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0x9, 0x8)
    OP_68(17700, 1100, 5360, 0)
    MoveCamera(61, 12, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16690, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "#00808F#6P#30W...Renne...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#00906F#6P#30W...His logic unit has\x01",
            "suffered fatal damage...\x02\x03",
            "#00908FA Gordias-class system\x01",
            "can't be backed up...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x2)
    ClearChrFlags(0xA, 0x1000)
    OP_68(17840, 1100, 5160, 0)
    MoveCamera(136, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(14300, 0)
    OP_0D()
    BeginChrThread(0xB, 0, 0, 9)
    Sleep(1600)
    BeginChrThread(0xB, 1, 0, 20)
    Sound(903, 0, 70, 0)
    Sleep(500)
    OP_63(0xA, 0x0, 1500, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0xA, 0xB4, 0x1F4)
    WaitChrThread(0xB, 0)

    ChrTalk(
        0xA,
        (
            "#03315F#6PPater-Mater!?\x02\x03",
            "#03314FIt's all right! I'll fix\x01",
            "you... for sure...!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(17970, 1100, 4660, 1000)
    MoveCamera(136, 16, 0, 1000)
    OP_6E(500, 1000)
    SetCameraDistance(14300, 1000)
    BeginChrThread(0xA, 1, 0, 7)
    WaitChrThread(0xA, 1)
    Sleep(300)
    VolumeBGM(0x50, 0x1F4)
    FadeToDark(500, 0, -1)
    Sound(824, 0, 70, 0)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    BeginChrThread(0xB, 1, 0, 21)
    Sound(1009, 0, 100, 0)
    Sleep(500)
    FadeToBright(800, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_0D()
    VolumeBGM(0x64, 0x3E8)
    Sleep(300)
    OP_63(0xA, 0x0, 1500, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(18770, 1100, 5270, 1500)
    MoveCamera(130, 16, 0, 1500)
    OP_6E(500, 1500)
    SetCameraDistance(13590, 1500)
    BeginChrThread(0xA, 1, 0, 8)
    WaitChrThread(0xA, 1)
    BeginChrThread(0xC, 1, 0, 24)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x5B, 0x8C, 0x1, 0x0)
    OP_79(0x0)
    Sleep(300)
    BeginChrThread(0xA, 1, 0, 10)
    WaitChrThread(0xA, 1)

    ChrTalk(
        0xA,
        "#03316F#12P#40WAh...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    BeginChrThread(0xA, 1, 0, 11)
    WaitChrThread(0xA, 1)
    OP_68(19520, 1100, 4610, 2000)
    MoveCamera(129, 16, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(12810, 2000)
    BeginChrThread(0x8, 0, 0, 12)
    BeginChrThread(0x9, 0, 0, 13)
    WaitChrThread(0x8, 0)
    BeginChrThread(0x8, 1, 0, 14)
    WaitChrThread(0x8, 1)
    OP_6F(0x79)
    SetCameraDistance(11620, 5000)
    BeginChrThread(0xA, 1, 0, 16)
    BeginChrThread(0x8, 1, 0, 15)

    ChrTalk(
        0xA,
        "#03313F#11P#60W#30A...Uuuh... Aaaah...\x02",
    )

    WaitChrThread(0xA, 1)
    WaitChrThread(0x8, 1)
    CloseMessageWindow()
    Sleep(500)
    OP_68(19520, 1100, 4610, 8500)
    MoveCamera(123, 27, 0, 8500)
    OP_6E(500, 8500)
    SetCameraDistance(50000, 8500)
    BeginChrThread(0xA, 1, 0, 17)
    WaitChrThread(0xA, 1)
    BeginChrThread(0x8, 1, 0, 18)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    ChrTalk(
        0xA,
        "#03310F#11P#5S#25AUAAAAAAAAAH!!\x02",
    )

    CloseMessageWindow()
    StopSound(868, 1000, 20)
    StopSound(132, 1000, 50)
    FadeToDark(3000, 0, -1)
    OP_0D()
    StopBGM(0x1770)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("c1583", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_195 end

    def Function_3_9B4(): pass

    label("Function_3_9B4")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x18)
    Sleep(100)
    SetChrSubChip(0xFE, 0x19)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1A)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1B)
    Return()

    # Function_3_9B4 end

    def Function_4_9DC(): pass

    label("Function_4_9DC")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x1B)
    Sleep(120)
    SetChrSubChip(0xFE, 0x1C)
    Sleep(120)
    SetChrSubChip(0xFE, 0x1D)
    Sleep(120)
    SetChrSubChip(0xFE, 0x1E)
    Sleep(120)
    SetChrSubChip(0xFE, 0x1F)
    Sleep(120)
    SetChrSubChip(0xFE, 0x1E)
    Sleep(120)
    SetChrSubChip(0xFE, 0x1D)
    Sleep(120)
    SetChrSubChip(0xFE, 0x1C)
    Sleep(120)
    SetChrSubChip(0xFE, 0x1B)
    Return()

    # Function_4_9DC end

    def Function_5_A27(): pass

    label("Function_5_A27")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    SetChrSubChip(0xFE, 0x2)
    Sleep(300)
    Return()

    # Function_5_A27 end

    def Function_6_A4B(): pass

    label("Function_6_A4B")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    Return()

    # Function_6_A4B end

    def Function_7_A6F(): pass

    label("Function_7_A6F")

    OP_9B(0x1, 0xFE, 0x19, 0x64, 0x3E8, 0x0)
    OP_9B(0x1, 0xFE, 0x19, 0x30C, 0x5DC, 0x0)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x14)
    Sleep(111)
    SetChrSubChip(0xFE, 0x15)
    Sleep(111)
    SetChrSubChip(0xFE, 0x16)
    Sleep(111)
    SetChrSubChip(0xFE, 0x17)
    Sleep(333)
    Return()

    # Function_7_A6F end

    def Function_8_AB8(): pass

    label("Function_8_AB8")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(300)
    Return()

    # Function_8_AB8 end

    def Function_9_ADC(): pass

    label("Function_9_ADC")

    Sound(904, 2, 100, 0)
    OP_74(0x0, 0x5)
    OP_71(0x0, 0xA, 0xD, 0x1, 0x0)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0xE, 0x2D, 0x1, 0x0)
    OP_79(0x0)
    OP_74(0x0, 0x5)
    OP_71(0x0, 0x2D, 0x32, 0x1, 0x0)
    StopSound(904, 1000, 100)
    Return()

    # Function_9_ADC end

    def Function_10_B1C(): pass

    label("Function_10_B1C")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x2)
    Sleep(125)
    SetChrSubChip(0xFE, 0x3)
    Sleep(125)
    SetChrSubChip(0xFE, 0x4)
    Sleep(125)
    SetChrSubChip(0xFE, 0x5)
    Sleep(500)
    Return()

    # Function_10_B1C end

    def Function_11_B47(): pass

    label("Function_11_B47")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    Sound(812, 0, 100, 0)
    SetChrSubChip(0xFE, 0x5)
    Sleep(125)
    SetChrSubChip(0xFE, 0x6)
    Sleep(125)
    SetChrSubChip(0xFE, 0x7)
    Sleep(125)
    SetChrSubChip(0xFE, 0x8)
    Sleep(125)
    SetChrSubChip(0xFE, 0x9)
    Sleep(375)
    Return()

    # Function_11_B47 end

    def Function_12_B7F(): pass

    label("Function_12_B7F")

    OP_96(0xFE, 0x4A92, 0x0, 0xF96, 0x3E8, 0x0)
    Return()

    # Function_12_B7F end

    def Function_13_B94(): pass

    label("Function_13_B94")

    Sleep(500)
    OP_95(0xFE, 19410, 0, 5320, 1000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_13_B94 end

    def Function_14_BB3(): pass

    label("Function_14_BB3")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Sleep(571)
    Sound(812, 0, 100, 0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1)
    Sleep(143)
    SetChrSubChip(0xFE, 0x2)
    Sleep(143)
    SetChrSubChip(0xFE, 0x3)
    Sleep(143)
    SetChrSubChip(0xFE, 0x4)
    Sleep(143)
    SetChrSubChip(0xFE, 0x4)
    Sleep(571)
    Sound(898, 0, 100, 0)
    SetChrSubChip(0xFE, 0x4)
    Sleep(167)
    SetChrSubChip(0xFE, 0x5)
    Sleep(167)
    SetChrSubChip(0xFE, 0x6)
    Sleep(167)
    SetChrSubChip(0xFE, 0x7)
    Sleep(667)
    Return()

    # Function_14_BB3 end

    def Function_15_C1B(): pass

    label("Function_15_C1B")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x7)
    Sleep(143)
    SetChrSubChip(0xFE, 0x8)
    Sleep(143)
    SetChrSubChip(0xFE, 0x9)
    Sleep(143)
    SetChrSubChip(0xFE, 0xA)
    Sleep(143)
    SetChrSubChip(0xFE, 0xB)
    Sleep(143)
    SetChrSubChip(0xFE, 0xC)
    Sleep(143)
    SetChrSubChip(0xFE, 0x7)
    Sleep(143)
    SetChrSubChip(0xFE, 0x7)
    Sleep(143)
    SetChrSubChip(0xFE, 0x7)
    Sleep(143)
    SetChrSubChip(0xFE, 0x8)
    Sleep(143)
    SetChrSubChip(0xFE, 0x9)
    Sleep(143)
    SetChrSubChip(0xFE, 0xA)
    Sleep(143)
    SetChrSubChip(0xFE, 0xB)
    Sleep(143)
    SetChrSubChip(0xFE, 0xC)
    Sleep(143)
    SetChrSubChip(0xFE, 0x7)
    Sleep(143)
    SetChrSubChip(0xFE, 0x7)
    Sleep(143)
    SetChrSubChip(0xFE, 0x7)
    Sleep(143)
    SetChrSubChip(0xFE, 0x8)
    Sleep(143)
    SetChrSubChip(0xFE, 0x9)
    Sleep(143)
    SetChrSubChip(0xFE, 0xA)
    Sleep(143)
    SetChrSubChip(0xFE, 0xB)
    Sleep(143)
    SetChrSubChip(0xFE, 0xC)
    Sleep(143)
    SetChrSubChip(0xFE, 0x7)
    Sleep(143)
    SetChrSubChip(0xFE, 0x7)
    Sleep(143)
    Return()

    # Function_15_C1B end

    def Function_16_CD2(): pass

    label("Function_16_CD2")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x9)
    Sleep(143)
    SetChrSubChip(0xFE, 0xA)
    Sleep(143)
    SetChrSubChip(0xFE, 0xB)
    Sleep(143)
    SetChrSubChip(0xFE, 0xC)
    Sleep(143)
    SetChrSubChip(0xFE, 0xD)
    Sleep(143)
    SetChrSubChip(0xFE, 0xE)
    Sleep(143)
    SetChrSubChip(0xFE, 0x9)
    Sleep(143)
    SetChrSubChip(0xFE, 0x9)
    Sleep(143)
    SetChrSubChip(0xFE, 0x9)
    Sleep(143)
    SetChrSubChip(0xFE, 0xA)
    Sleep(143)
    SetChrSubChip(0xFE, 0xB)
    Sleep(143)
    SetChrSubChip(0xFE, 0xC)
    Sleep(143)
    SetChrSubChip(0xFE, 0xD)
    Sleep(143)
    SetChrSubChip(0xFE, 0xE)
    Sleep(143)
    SetChrSubChip(0xFE, 0x9)
    Sleep(143)
    SetChrSubChip(0xFE, 0x9)
    Sleep(143)
    SetChrSubChip(0xFE, 0x9)
    Sleep(143)
    SetChrSubChip(0xFE, 0xA)
    Sleep(143)
    SetChrSubChip(0xFE, 0xB)
    Sleep(143)
    SetChrSubChip(0xFE, 0xC)
    Sleep(143)
    SetChrSubChip(0xFE, 0xD)
    Sleep(143)
    SetChrSubChip(0xFE, 0xE)
    Sleep(143)
    SetChrSubChip(0xFE, 0x9)
    Sleep(143)
    SetChrSubChip(0xFE, 0x9)
    Sleep(143)
    Return()

    # Function_16_CD2 end

    def Function_17_D89(): pass

    label("Function_17_D89")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0xA)
    Sleep(143)
    SetChrSubChip(0xFE, 0xB)
    Sleep(143)
    SetChrSubChip(0xFE, 0xC)
    Sleep(143)
    SetChrSubChip(0xFE, 0xD)
    Sleep(143)
    SetChrSubChip(0xFE, 0xE)
    Sleep(143)
    SetChrSubChip(0xFE, 0xF)
    Sleep(143)
    SetChrSubChip(0xFE, 0x10)
    Sleep(143)
    SetChrSubChip(0xFE, 0x11)
    Sleep(571)
    Return()

    # Function_17_D89 end

    def Function_18_DD0(): pass

    label("Function_18_DD0")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x8)
    Sleep(125)
    SetChrSubChip(0xFE, 0x9)
    Sleep(125)
    SetChrSubChip(0xFE, 0xA)
    Sleep(125)
    SetChrSubChip(0xFE, 0xB)
    Sleep(125)
    SetChrSubChip(0xFE, 0xC)
    Sleep(125)
    SetChrSubChip(0xFE, 0x7)
    Sleep(125)
    SetChrSubChip(0xFE, 0xD)
    Sleep(125)
    SetChrSubChip(0xFE, 0xE)
    Sleep(125)
    SetChrSubChip(0xFE, 0xF)
    Sleep(125)
    SetChrSubChip(0xFE, 0xF)
    Sleep(571)
    SetChrSubChip(0xFE, 0xF)
    Sleep(143)
    SetChrSubChip(0xFE, 0x10)
    Sleep(143)
    SetChrSubChip(0xFE, 0x11)
    Sleep(143)
    SetChrSubChip(0xFE, 0x12)
    Sleep(143)
    SetChrSubChip(0xFE, 0x13)
    Sleep(571)
    Return()

    # Function_18_DD0 end

    def Function_19_E48(): pass

    label("Function_19_E48")

    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 21670, 1300, 4640, 0, 0, 0, 250, 250, 250, 0xFF, 0, 0, 0, 0)
    Sleep(350)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 21670, 1300, 4640, 0, 0, 0, 450, 450, 450, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 21670, 1300, 4640, 0, 0, 0, 350, 350, 350, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Return()

    # Function_19_E48 end

    def Function_20_EF7(): pass

    label("Function_20_EF7")

    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 21670, 1300, 4640, 0, 0, 0, 200, 200, 200, 0xFF, 0, 0, 0, 0)
    Sleep(350)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 21670, 1300, 4640, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sleep(700)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 21670, 1300, 4640, 0, 0, 0, 350, 350, 350, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 21670, 1300, 4640, 0, 0, 0, 250, 250, 250, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Return()

    # Function_20_EF7 end

    def Function_21_FE0(): pass

    label("Function_21_FE0")

    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 21670, 1300, 4640, 0, 0, 0, 250, 250, 250, 0xFF, 0, 0, 0, 0)
    Sleep(350)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 21670, 1300, 4640, 0, 0, 0, 240, 240, 240, 0xFF, 0, 0, 0, 0)
    Sleep(350)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 21670, 1300, 4640, 0, 0, 0, 220, 220, 220, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 21670, 1300, 4640, 0, 0, 0, 180, 180, 180, 0xFF, 0, 0, 0, 0)
    Sleep(450)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 21670, 1300, 4640, 0, 0, 0, 130, 130, 130, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Return()

    # Function_21_FE0 end

    def Function_22_1103(): pass

    label("Function_22_1103")

    Sound(203, 0, 25, 0)
    Sleep(900)
    Sound(203, 0, 25, 0)
    Sleep(600)
    Sound(887, 0, 15, 0)
    Sleep(500)
    Sound(203, 0, 25, 0)
    Sleep(900)
    Sound(203, 0, 25, 0)
    Sleep(600)
    Sound(887, 0, 15, 0)
    Sleep(500)
    Sound(203, 0, 20, 0)
    Sleep(900)
    Sound(203, 0, 20, 0)
    Sleep(600)
    Sound(887, 0, 10, 0)
    Sleep(500)
    Sound(203, 0, 20, 0)
    Sleep(900)
    Sound(203, 0, 20, 0)
    Sleep(600)
    Sound(887, 0, 10, 0)
    Sleep(500)
    Sound(203, 0, 20, 0)
    Sleep(900)
    Sound(203, 0, 20, 0)
    Sleep(600)
    Sound(887, 0, 10, 0)
    Sleep(500)
    Sound(203, 0, 15, 0)
    Sleep(900)
    Sound(203, 0, 15, 0)
    Sleep(600)
    Sound(887, 0, 10, 0)
    Sleep(500)
    Sound(203, 0, 10, 0)
    Sleep(900)
    Sound(203, 0, 10, 0)
    Sleep(600)
    Sound(887, 0, 10, 0)
    Sleep(500)
    Sound(203, 0, 5, 0)
    Return()

    # Function_22_1103 end

    def Function_23_11C7(): pass

    label("Function_23_11C7")

    OP_25(0x364, 0x23)
    Sleep(200)
    OP_25(0x364, 0x1E)
    Sleep(200)
    OP_25(0x364, 0x19)
    Sleep(200)
    OP_25(0x364, 0x14)
    Return()

    # Function_23_11C7 end

    def Function_24_11E1(): pass

    label("Function_24_11E1")

    Sound(954, 0, 100, 0)
    Sleep(200)
    Sound(905, 0, 100, 0)
    Sleep(400)
    Sound(902, 0, 50, 0)
    Sleep(800)
    Sound(880, 0, 40, 0)
    Return()

    # Function_24_11E1 end

    SaveToFile()

Try(main)
