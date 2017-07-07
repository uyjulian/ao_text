from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1310_1.bin",                # FileName
        "t1310",                    # MapName
        "t1310",                    # Location
        0x00BD,                     # MapIndex
        "ed7161",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [440, 441, 705, 859, 1008, 1065, 1191, 1425, 1497, 0, 1547, 0, 3336, 3487, 3544, 3701, 0, 3758, 0, 44, 15, 0, 0],
    )

    BuildStringList((
        "t1310_1",                # 0
    ))

    ChipFrameInfo(440, 0)                                        # 0

    ScpFunction((
        "Function_0_1B8",          # 00, 0
        "Function_1_1B9",          # 01, 1
        "Function_2_2C1",          # 02, 2
        "Function_3_35B",          # 03, 3
        "Function_4_3F0",          # 04, 4
        "Function_5_429",          # 05, 5
        "Function_6_4A7",          # 06, 6
        "Function_7_591",          # 07, 7
        "Function_8_5D9",          # 08, 8
        "Function_9_60B",          # 09, 9
        "Function_10_D08",         # 0A, 10
        "Function_11_D9F",         # 0B, 11
        "Function_12_DD8",         # 0C, 12
        "Function_13_E75",         # 0D, 13
        "Function_14_EAE",         # 0E, 14
        "Function_15_F2C",         # 0F, 15
        "Function_16_FC8",         # 10, 16
        "Function_17_103D",        # 11, 17
        "Function_18_108E",        # 12, 18
        "Function_19_1164",        # 13, 19
        "Function_20_11EC",        # 14, 20
        "Function_21_126B",        # 15, 21
        "Function_22_1356",        # 16, 22
        "Function_23_139E",        # 17, 23
        "Function_24_13DC",        # 18, 24
        "Function_25_1CBF",        # 19, 25
        "Function_26_1D56",        # 1A, 26
        "Function_27_1D8F",        # 1B, 27
        "Function_28_1E3A",        # 1C, 28
        "Function_29_1ED5",        # 1D, 29
        "Function_30_1F0E",        # 1E, 30
        "Function_31_1FB0",        # 1F, 31
        "Function_32_1FB1",        # 20, 32
        "Function_33_2018",        # 21, 33
        "Function_34_20AE",        # 22, 34
        "Function_35_2101",        # 23, 35
        "Function_36_216D",        # 24, 36
        "Function_37_2188",        # 25, 37
        "Function_38_21E4",        # 26, 38
        "Function_39_2216",        # 27, 39
        "Function_40_22B1",        # 28, 40
        "Function_41_2336",        # 29, 41
        "Function_42_2361",        # 2A, 42
        "Function_43_2389",        # 2B, 43
        "Function_44_2436",        # 2C, 44
        "Function_45_2493",        # 2D, 45
        "Function_46_251F",        # 2E, 46
        "Function_47_2606",        # 2F, 47
        "Function_48_264E",        # 30, 48
        "Function_49_2692",        # 31, 49
        "Function_50_30D1",        # 32, 50
        "Function_51_3169",        # 33, 51
        "Function_52_31A2",        # 34, 52
        "Function_53_3224",        # 35, 53
        "Function_54_32B8",        # 36, 54
        "Function_55_32F1",        # 37, 55
        "Function_56_3359",        # 38, 56
        "Function_57_33F4",        # 39, 57
        "Function_58_342D",        # 3A, 58
        "Function_59_34AF",        # 3B, 59
        "Function_60_354D",        # 3C, 60
        "Function_61_360A",        # 3D, 61
        "Function_62_3676",        # 3E, 62
        "Function_63_3771",        # 3F, 63
        "Function_64_37CD",        # 40, 64
        "Function_65_380B",        # 41, 65
        "Function_66_3853",        # 42, 66
        "Function_67_38EA",        # 43, 67
        "Function_68_3928",        # 44, 68
        "Function_69_39AD",        # 45, 69
        "Function_70_4258",        # 46, 70
        "Function_71_42F0",        # 47, 71
        "Function_72_4329",        # 48, 72
        "Function_73_43B7",        # 49, 73
        "Function_74_4451",        # 4A, 74
        "Function_75_4484",        # 4B, 75
        "Function_76_44D0",        # 4C, 76
        "Function_77_4538",        # 4D, 77
        "Function_78_4571",        # 4E, 78
        "Function_79_4641",        # 4F, 79
        "Function_80_46E1",        # 50, 80
        "Function_81_4736",        # 51, 81
        "Function_82_47BB",        # 52, 82
        "Function_83_48B0",        # 53, 83
        "Function_84_48E2",        # 54, 84
        "Function_85_4914",        # 55, 85
        "Function_86_4979",        # 56, 86
        "Function_87_49EB",        # 57, 87
        "Function_88_4A8E",        # 58, 88
    ))


    def Function_0_1B8(): pass

    label("Function_0_1B8")

    Return()

    # Function_0_1B8 end

    def Function_1_1B9(): pass

    label("Function_1_1B9")

    Call(1, 0)
    SetChrPos(0x11, 24500, -6000, -19000, 0)
    SetChrPos(0x12, 27500, -6000, -19000, 0)
    SetChrPos(0x10, 24500, -6000, -13000, 180)
    SetChrPos(0x13, 27500, -6000, -13000, 180)
    SetChrPos(0x14, 27500, -4000, -16000, 0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x13, 0x2E)
    SetChrSubChip(0x13, 0x0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(330, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    OP_68(26000, -5000, -16000, 8000)
    MoveCamera(295, 30, 0, 8000)
    OP_6E(650, 8000)
    SetCameraDistance(17000, 8000)
    FadeToBright(1000, 0)
    BeginChrThread(0x12, 3, 1, 2)

    label("loc_2A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BD")
    Sleep(1)
    Jump("loc_2A6")

    label("loc_2BD")

    OP_6F(0x79)
    OP_0D()
    Return()

    # Function_1_1B9 end

    def Function_2_2C1(): pass

    label("Function_2_2C1")


    def lambda_2C6():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEC78, 0xFFFFB6F4, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2C6)
    SetChrFlags(0xFE, 0x20)

    def lambda_2E8():

        label("loc_2E8")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_2E8")

    QueueWorkItem2(0xFE, 2, lambda_2E8)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x15)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    ChrTalk(
        0x12,
        "#6P#5ASenior!\x02",
    )


    def lambda_328():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF254, 0xFFFFBBA4, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_328)
    BeginChrThread(0x11, 3, 1, 3)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_2_2C1 end

    def Function_3_35B(): pass

    label("Function_3_35B")

    Sleep(500)
    Sound(809, 0, 100, 0)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)

    def lambda_376():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFBD98, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_376)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    Sound(442, 0, 90, 0)

    ChrTalk(
        0x11,
        "#5P#5AHey!\x02",
    )


    def lambda_3B3():
        OP_96(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFCC0C, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3B3)
    BeginChrThread(0x10, 3, 1, 4)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Return()

    # Function_3_35B end

    def Function_4_3F0(): pass

    label("Function_4_3F0")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_403():
        OP_9D(0xFE, 0x6A40, 0xFFFFEC78, 0xFFFFCD38, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_403)
    BeginChrThread(0x13, 3, 1, 5)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_4_3F0 end

    def Function_5_429(): pass

    label("Function_5_429")

    SetChrFlags(0xFE, 0x20)

    def lambda_433():

        label("loc_433")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_433")

    QueueWorkItem2(0xFE, 2, lambda_433)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x1C)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    ChrTalk(
        0x13,
        "#12P#5AThanks!\x02",
    )


    def lambda_474():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF254, 0xFFFFC694, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_474)
    BeginChrThread(0x10, 3, 1, 6)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_5_429 end

    def Function_6_4A7(): pass

    label("Function_6_4A7")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_4C2():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4C2)
    Sleep(600)

    ChrTalk(
        0x10,
        "#11P#4S#5AHey! It is!#3S\x02",
    )

    SetChrSubChip(0xFE, 0x1)
    OP_82(0x64, 0x0, 0xBB8, 0x96)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 700, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(442, 0, 100, 0)
    Sound(547, 0, 40, 0)
    BeginChrThread(0x14, 3, 1, 7)
    BeginChrThread(0x11, 3, 1, 8)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x11, 3)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_6_4A7 end

    def Function_7_591(): pass

    label("Function_7_591")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_96(0xFE, 0x5AD2, 0xFFFFE890, 0xFFFFADF8, 0x4E20, 0x0)
    Sound(443, 0, 100, 0)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x54F6, 0xFFFFE890, 0xFFFF8FBC, 0x3E8, 0x7D0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_7_591 end

    def Function_8_5D9(): pass

    label("Function_8_5D9")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x7D0)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_8_5D9 end

    def Function_9_60B(): pass

    label("Function_9_60B")

    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetChrPos(0x101, 24500, -6000, -19000, 0)
    SetChrPos(0x11, 27500, -6000, -19000, 0)
    SetChrPos(0x12, 24500, -6000, -10000, 180)
    SetChrPos(0x13, 27500, -6000, -13000, 180)
    SetChrPos(0x10, 21300, -6000, -16000, 90)
    SetChrPos(0x14, 24500, -5500, -10200, 0)
    SetChrFlags(0x14, 0x8)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x13, 0x2E)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17000, 0)
    OP_68(26000, -5000, -16000, 12000)
    MoveCamera(305, 30, 0, 12000)
    FadeToBright(1000, 0)
    OP_0D()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x12, 3, 1, 10)

    label("loc_703")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71A")
    Sleep(1)
    Jump("loc_703")

    label("loc_71A")

    OP_4B(0x14, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Decide direct attack as it is\x01",      # 0
            "Toss to make Randy strike\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_4C(0x14, 0xFF)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3B")
    MoveCamera(315, 25, 0, 1500)
    SetCameraDistance(15000, 1500)
    BeginChrThread(0x101, 3, 1, 18)
    WaitChrThread(0x101, 3)
    Sound(909, 0, 70, 0)
    Sleep(500)

    ChrTalk(
        0x10,
        "#13400F#5P#NYes, out ~! It is!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x13, 0xA)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12506F#6PDid you get too rash, …?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x13, 0xE1, 0x1F4)

    ChrTalk(
        0x13,
        "#12902FHuff, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#13006F#5P#NIt was dangerous … ….\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        "#12500FBad, Randy!\x02",
    )

    CloseMessageWindow()
    OP_93(0x11, 0x10E, 0x1F4)

    ChrTalk(
        0x11,
        (
            "#12800F#12PDon Mai Don Mai!\x01",
            "Let's get over this from you!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(909, 0, 70, 0)
    Sleep(500)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x13, 0x2E)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x0)
    SetChrPos(0x101, 24500, -6000, -19000, 0)
    SetChrPos(0x11, 27500, -6000, -20000, 0)
    SetChrPos(0x13, 24500, -6000, -12000, 180)
    SetChrPos(0x12, 27500, -6000, -13000, 180)
    SetChrFlags(0x14, 0x8)
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(17000, 1500)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x10,
        (
            "#13400F#5P…… Game set! It is!\x02\x03",
            "#13409F7 - 12,\x01",
            "Wazy team won ~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12506F#6PHaa, I lost … …\x02",
    )

    CloseMessageWindow()
    Jump("loc_CFC")

    label("loc_A3B")

    OP_2C(0xA5, 0x1)
    MoveCamera(315, 25, 0, 2000)
    SetCameraDistance(15000, 2000)
    BeginChrThread(0x101, 3, 1, 20)
    WaitChrThread(0x101, 3)
    Sound(909, 0, 70, 0)
    Sleep(500)

    ChrTalk(
        0x10,
        "#13405F#5P#NOh, I'll do it, Randy!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x13, 0xA)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)

    ChrTalk(
        0x12,
        "#13002F#11P#NCut … It is brilliant.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x13,
        (
            "#12906F#11PWhew, this height difference is\x01",
            "There are thawing pots indeed.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x11, 0x10E, 0x1F4)

    ChrTalk(
        0x11,
        (
            "#12809F#12PIt's Naistos, Lloyd.\x01",
            "Do you have the judgment of the truth?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#12509F#5PWell, that was where I was going ahead.\x02\x03",
            "#12500FOK, I'll fold in like this! It is!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(909, 0, 70, 0)
    Sleep(500)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x13, 0x2E)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x0)
    SetChrPos(0x101, 24500, -6000, -19000, 0)
    SetChrPos(0x11, 27500, -6000, -20000, 0)
    SetChrPos(0x13, 24500, -6000, -12000, 180)
    SetChrPos(0x12, 27500, -6000, -13000, 180)
    SetChrFlags(0x14, 0x8)
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(17000, 1500)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x10,
        (
            "#13400F#5P…… Game set! It is!\x02\x03",
            "#13409FAt 12-8, my brother's team won ~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12500F#6POkay, I've won! It is!\x02",
    )

    CloseMessageWindow()

    label("loc_CFC")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_9_60B end

    def Function_10_D08(): pass

    label("Function_10_D08")

    ClearChrFlags(0x14, 0x8)
    Sound(802, 0, 60, 0)

    def lambda_D18():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_D18)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1000)
    Sound(441, 0, 100, 0)
    SetChrSubChip(0xFE, 0x1)

    ChrTalk(
        0x12,
        "#11P#5AWhat!\x02",
    )


    def lambda_D5E():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFB6F4, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_D5E)
    BeginChrThread(0x101, 3, 1, 11)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_10_D08 end

    def Function_11_D9F(): pass

    label("Function_11_D9F")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_DB2():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEE6C, 0xFFFFB5C8, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_DB2)
    BeginChrThread(0x11, 3, 1, 12)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_11_D9F end

    def Function_12_DD8(): pass

    label("Function_12_DD8")

    SetChrFlags(0xFE, 0x20)

    def lambda_DE2():

        label("loc_DE2")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_DE2")

    QueueWorkItem2(0xFE, 2, lambda_DE2)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    ChrTalk(
        0x11,
        "#6P#5AYacht!\x02",
    )


    def lambda_E20():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFCC0C, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_E20)
    BeginChrThread(0x13, 3, 1, 13)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1500)
    SetChrChipByIndex(0xFE, 0x8)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_12_DD8 end

    def Function_13_E75(): pass

    label("Function_13_E75")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_E88():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEC78, 0xFFFFCD38, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_E88)
    BeginChrThread(0x12, 3, 1, 14)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_13_E75 end

    def Function_14_EAE(): pass

    label("Function_14_EAE")

    SetChrFlags(0xFE, 0x20)

    def lambda_EB8():

        label("loc_EB8")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_EB8")

    QueueWorkItem2(0xFE, 2, lambda_EB8)
    Sleep(350)

    ChrTalk(
        0x12,
        "#11P#5AWajima!\x02",
    )

    SetChrChipByIndex(0xFE, 0x15)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_EF9():
        OP_9D(0xFE, 0x6B6C, 0xFFFFF448, 0xFFFFC75C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_EF9)
    BeginChrThread(0x13, 3, 1, 15)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_14_EAE end

    def Function_15_F2C(): pass

    label("Function_15_F2C")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0x13,
        "#11P#5APretty!\x02",
    )

    Sound(809, 0, 100, 0)

    def lambda_F5D():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F5D)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)

    def lambda_F85():
        OP_98(0xFE, 0x0, 0xFFFFFCE0, 0xFFFFF830, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_F85)
    BeginChrThread(0x11, 3, 1, 16)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sound(442, 0, 80, 0)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Return()

    # Function_15_F2C end

    def Function_16_FC8(): pass

    label("Function_16_FC8")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    Sound(809, 0, 100, 0)

    def lambda_FE0():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FE0)
    WaitChrThread(0x14, 1)

    def lambda_1001():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFCD38, 0x3E8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1001)
    BeginChrThread(0x12, 3, 1, 17)
    Sound(441, 0, 80, 0)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Return()

    # Function_16_FC8 end

    def Function_17_103D(): pass

    label("Function_17_103D")

    WaitChrThread(0x14, 1)
    SetChrFlags(0xFE, 0x20)
    OP_93(0xFE, 0xB4, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_1061():
        OP_9D(0xFE, 0x5FB4, 0xFFFFED40, 0xFFFFB5C8, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1061)
    Sleep(300)
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_17_103D end

    def Function_18_108E(): pass

    label("Function_18_108E")

    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_10A6():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFBBA4, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10A6)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(442, 0, 100, 0)
    Sound(547, 0, 40, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x96)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 700, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(
        0x101,
        "#5P#5A#4SWhat! It is!#3S\x02",
    )

    BeginChrThread(0x14, 3, 1, 19)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    WaitChrThread(0x14, 3)
    Return()

    # Function_18_108E end

    def Function_19_1164(): pass

    label("Function_19_1164")

    SetChrFlags(0x13, 0x20)

    def lambda_116E():

        label("loc_116E")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_116E")

    QueueWorkItem2(0x13, 2, lambda_116E)
    SetChrFlags(0x12, 0x20)

    def lambda_1185():

        label("loc_1185")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_1185")

    QueueWorkItem2(0x12, 2, lambda_1185)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_96(0xFE, 0x68F6, 0xFFFFE890, 0xFFFFDDBE, 0x4E20, 0x0)
    Sound(443, 0, 100, 0)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x7A76, 0xFFFFE868, 0x1B58, 0x9C4, 0x3E8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    EndChrThread(0x13, 0x2)
    ClearChrFlags(0x13, 0x20)
    EndChrThread(0x12, 0x2)
    ClearChrFlags(0x12, 0x20)
    Return()

    # Function_19_1164 end

    def Function_20_11EC(): pass

    label("Function_20_11EC")

    SetChrFlags(0xFE, 0x20)

    def lambda_11F6():

        label("loc_11F6")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_11F6")

    QueueWorkItem2(0xFE, 2, lambda_11F6)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    ChrTalk(
        0x101,
        "#5P#5AI will ask!\x02",
    )


    def lambda_1234():
        OP_9D(0xFE, 0x6B6C, 0xFFFFF448, 0xFFFFBF8C, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1234)
    BeginChrThread(0x11, 3, 1, 21)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x11, 3)
    Return()

    # Function_20_11EC end

    def Function_21_126B(): pass

    label("Function_21_126B")

    Sleep(600)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_1286():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1286)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(442, 0, 100, 0)
    Sound(547, 0, 40, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x96)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 700, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(
        0x11,
        "#5P#5A#4SOh ah ah! It is!#3S\x02",
    )

    BeginChrThread(0x14, 3, 1, 22)
    BeginChrThread(0x13, 3, 1, 23)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x13, 3)
    Return()

    # Function_21_126B end

    def Function_22_1356(): pass

    label("Function_22_1356")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_96(0xFE, 0x6F9A, 0xFFFFE890, 0xFFFFCCCA, 0x4E20, 0x0)
    Sound(443, 0, 100, 0)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x7F76, 0xFFFFE7F0, 0x762, 0x1388, 0x3E8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_22_1356 end

    def Function_23_139E(): pass

    label("Function_23_139E")

    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    Sound(809, 0, 100, 0)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x7D0)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Return()

    # Function_23_139E end

    def Function_24_13DC(): pass

    label("Function_24_13DC")

    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetChrPos(0x101, 27500, -6000, -19000, 0)
    SetChrPos(0x12, 24500, -6000, -19000, 0)
    SetChrPos(0x10, 24500, -6000, -10000, 180)
    SetChrPos(0x13, 27500, -6000, -13000, 180)
    SetChrPos(0x11, 21300, -6000, -16000, 90)
    SetChrPos(0x14, 24500, -5500, -10200, 0)
    SetChrFlags(0x14, 0x8)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x2E)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17000, 0)
    OP_68(26000, -5000, -16000, 13000)
    MoveCamera(305, 30, 0, 13000)
    FadeToBright(1000, 0)
    OP_0D()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x10, 3, 1, 25)

    label("loc_14D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14EB")
    Sleep(1)
    Jump("loc_14D4")

    label("loc_14EB")

    OP_4B(0x14, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Read bang and join the block\x01",      # 0
            "Read the back and go back to the back\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_4C(0x14, 0xFF)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18ED")
    MoveCamera(315, 25, 0, 2000)
    SetCameraDistance(15000, 2000)
    BeginChrThread(0x13, 3, 1, 39)
    WaitChrThread(0x13, 3)
    Sound(909, 0, 70, 0)
    Sleep(500)

    ChrTalk(
        0x11,
        (
            "#12809F#5P#NIria's team, scoring points!\x02\x03",
            "#12803FHowever, fluff is a wadi ……\x01",
            "Cunning#2RRub#I'm going to make money.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0xA)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    OP_93(0x13, 0x10E, 0x1F4)

    ChrTalk(
        0x13,
        (
            "#12902F#12PHuh, I do not think he is bad.\x01",
            "Is this also one of the strategies?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0x87, 0x1F4)

    ChrTalk(
        0x10,
        (
            "#13404F#5PWell, if you are serious kun team opponent\x01",
            "It might be a great strategy, is not it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_93(0x12, 0x5A, 0x1F4)

    ChrTalk(
        0x12,
        (
            "#13001F#5PRo, Mr. Lloyd ……\x01",
            "Such a thing is said! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#12510F#12PCut … Well, I will lose to win!\x02\x03",
            "#12501FIt will be guts like this, Noel!\x01",
            "Anything will keep you scolded by the ball!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(909, 0, 70, 0)
    Sleep(500)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x2E)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrPos(0x101, 27500, -6000, -19000, 0)
    SetChrPos(0x12, 24500, -6000, -19000, 0)
    SetChrPos(0x10, 24500, -6000, -13000, 180)
    SetChrPos(0x13, 27500, -6000, -13000, 180)
    SetChrFlags(0x14, 0x8)
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(17000, 1500)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x11,
        (
            "#12800F#5P…… Game set! It is!\x02\x03",
            "#12809FIn 3-12,\x01",
            "Iria's team's win! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12506F#6PKuuu … … Was it useless …?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CB3")

    label("loc_18ED")

    OP_2C(0xA5, 0x1)
    MoveCamera(315, 25, 0, 2000)
    SetCameraDistance(15000, 2000)
    BeginChrThread(0x13, 3, 1, 43)
    WaitChrThread(0x13, 3)
    Sleep(600)
    Sound(909, 0, 70, 0)
    Sleep(500)

    ChrTalk(
        0x11,
        (
            "#12800F#5P#NLloyd team, scoring!\x02\x03",
            "#12809FHahaha, you do it!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0xA)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)

    ChrTalk(
        0x13,
        (
            "#12906F#11PWell, I guess you never read.\x02\x03",
            "#12902FBeing seriously serious,\x01",
            "Are you doing quite a bit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12502F#6PWaji's personality, if that scene\x01",
            "I am sure that it will reverse its backs.\x02\x03",
            "#12504FUntil we did the opposite direction.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x12, 0x5A, 0x1F4)

    ChrTalk(
        0x12,
        "#13000F#5PI did it, Mr. Lloyd!\x02",
    )

    CloseMessageWindow()
    OP_93(0x10, 0x5A, 0x1F4)

    ChrTalk(
        0x10,
        (
            "#13400F#5PGhost, apparently\x01",
            "Did not you despise too much?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#12904FHaha, maybe so.\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#12500F#12PAlright, Noel!\x01",
            "The flow of the game as it is\x01",
            "I will make this one!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#13009F#5POkay, okay! It is!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(909, 0, 70, 0)
    Sleep(500)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x2E)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrPos(0x101, 27500, -6000, -19000, 0)
    SetChrPos(0x12, 24500, -6000, -19000, 0)
    SetChrPos(0x10, 24500, -6000, -13000, 180)
    SetChrPos(0x13, 27500, -6000, -13000, 180)
    SetChrFlags(0x14, 0x8)
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(17000, 1500)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x11,
        (
            "#12800F#5P…… Game set! It is!\x02\x03",
            "#12809FAt 12-11,\x01",
            "Lloyd team wins! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12512F#6POh, you did it … you gotta win!\x02",
    )

    CloseMessageWindow()

    label("loc_1CB3")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_24_13DC end

    def Function_25_1CBF(): pass

    label("Function_25_1CBF")

    ClearChrFlags(0x14, 0x8)
    Sound(802, 0, 60, 0)

    def lambda_1CCF():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1CCF)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1000)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    ChrTalk(
        0x10,
        "#11P#5AHo!\x02",
    )


    def lambda_1D15():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFB6F4, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1D15)
    BeginChrThread(0x12, 3, 1, 26)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x3)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_25_1CBF end

    def Function_26_1D56(): pass

    label("Function_26_1D56")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_1D69():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEDA4, 0xFFFFB5C8, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1D69)
    BeginChrThread(0x101, 3, 1, 27)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_26_1D56 end

    def Function_27_1D8F(): pass

    label("Function_27_1D8F")

    SetChrFlags(0xFE, 0x20)

    def lambda_1D99():

        label("loc_1D99")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_1D99")

    QueueWorkItem2(0xFE, 2, lambda_1D99)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 60, 0)

    ChrTalk(
        0x101,
        "#6P#5ANoel!\x02",
    )


    def lambda_1DD9():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF448, 0xFFFFBBA4, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1DD9)
    BeginChrThread(0x12, 3, 1, 28)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1500)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_98(0xFE, 0x0, 0x0, 0xFFFFFC18, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_27_1D8F end

    def Function_28_1E3A(): pass

    label("Function_28_1E3A")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_1E55():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFBD98, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1E55)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(442, 0, 80, 0)

    ChrTalk(
        0x12,
        "#5P#5AWhat! It is!\x02",
    )


    def lambda_1E98():
        OP_96(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFCC0C, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1E98)
    BeginChrThread(0x13, 3, 1, 29)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Return()

    # Function_28_1E3A end

    def Function_29_1ED5(): pass

    label("Function_29_1ED5")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_1EE8():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF448, 0xFFFFC75C, 0xC80, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1EE8)
    BeginChrThread(0x10, 3, 1, 30)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_29_1ED5 end

    def Function_30_1F0E(): pass

    label("Function_30_1F0E")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0x10,
        "#11P#5AWell!\x02",
    )

    Sound(809, 0, 100, 0)

    def lambda_1F3F():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1F3F)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(442, 0, 80, 0)

    def lambda_1F6D():
        OP_96(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFB30C, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1F6D)
    BeginChrThread(0x12, 3, 1, 31)
    BeginChrThread(0x101, 3, 1, 32)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Return()

    # Function_30_1F0E end

    def Function_31_1FB0(): pass

    label("Function_31_1FB0")

    Return()

    # Function_31_1FB0 end

    def Function_32_1FB1(): pass

    label("Function_32_1FB1")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_1FC4():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEC78, 0xFFFFBD98, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1FC4)
    BeginChrThread(0x12, 3, 1, 33)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_98(0xFE, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_32_1FB1 end

    def Function_33_2018(): pass

    label("Function_33_2018")

    SetChrFlags(0xFE, 0x20)

    def lambda_2022():

        label("loc_2022")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_2022")

    QueueWorkItem2(0xFE, 2, lambda_2022)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x15)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_204D():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFCC0C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_204D)
    BeginChrThread(0x13, 3, 1, 34)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1700)
    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_98(0xFE, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_33_2018 end

    def Function_34_20AE(): pass

    label("Function_34_20AE")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    ChrTalk(
        0x13,
        "#12P#5AI'm going!\x02",
    )


    def lambda_20DB():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEC78, 0xFFFFC568, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_20DB)
    BeginChrThread(0x10, 3, 1, 35)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_34_20AE end

    def Function_35_2101(): pass

    label("Function_35_2101")

    SetChrFlags(0xFE, 0x20)

    def lambda_210B():

        label("loc_210B")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_210B")

    QueueWorkItem2(0xFE, 2, lambda_210B)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_2136():
        OP_9D(0xFE, 0x6B6C, 0xFFFFF448, 0xFFFFC75C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2136)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_35_2101 end

    def Function_36_216D(): pass

    label("Function_36_216D")

    Sleep(500)
    SetChrChipByIndex(0xFE, 0x3)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_36_216D end

    def Function_37_2188(): pass

    label("Function_37_2188")

    BeginChrThread(0x10, 3, 1, 36)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    OP_98(0xFE, 0x0, 0x0, 0x5DC, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x7D0)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_37_2188 end

    def Function_38_21E4(): pass

    label("Function_38_21E4")

    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x7D0)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_38_21E4 end

    def Function_39_2216(): pass

    label("Function_39_2216")

    BeginChrThread(0x101, 3, 1, 37)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_2234():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2234)
    Sleep(600)

    ChrTalk(
        0x13,
        "#12P#5A─ ─ Anyway ♪\x02",
    )

    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    BeginChrThread(0x14, 3, 1, 40)
    BeginChrThread(0x12, 3, 1, 38)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    Sound(441, 0, 100, 0)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x12, 3)
    Return()

    # Function_39_2216 end

    def Function_40_22B1(): pass

    label("Function_40_22B1")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_9D(0xFE, 0x639C, 0xFFFFE890, 0xFFFFAC04, 0x7D0, 0x3E8)
    Sound(443, 0, 40, 0)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x639C, 0xFFFFE890, 0xFFFFA628, 0x3E8, 0x3E8)
    Sound(441, 0, 60, 0)
    OP_9D(0xFE, 0x639C, 0xFFFFE890, 0xFFFFA240, 0x1F4, 0x3E8)
    Sound(441, 0, 40, 0)
    OP_9D(0xFE, 0x639C, 0xFFFFE890, 0xFFFFA04C, 0xC8, 0x3E8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_40_22B1 end

    def Function_41_2336(): pass

    label("Function_41_2336")

    BeginChrThread(0x10, 3, 1, 36)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    OP_98(0xFE, 0x0, 0x0, 0xFFFFF830, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_41_2336 end

    def Function_42_2361(): pass

    label("Function_42_2361")

    Sleep(300)
    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_98(0xFE, 0x0, 0x0, 0xFFFFFC18, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_42_2361 end

    def Function_43_2389(): pass

    label("Function_43_2389")

    BeginChrThread(0x101, 3, 1, 41)
    BeginChrThread(0x12, 3, 1, 42)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_23AD():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_23AD)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)

    ChrTalk(
        0x13,
        "#12P#5AUh ……! Is it?\x02",
    )


    def lambda_23ED():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFB118, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_23ED)
    BeginChrThread(0x101, 3, 1, 44)
    Sleep(100)
    Sound(441, 0, 100, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Sleep(5500)
    Return()

    # Function_43_2389 end

    def Function_44_2436(): pass

    label("Function_44_2436")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_2449():
        OP_9D(0xFE, 0x6590, 0xFFFFEC78, 0xFFFFB9B0, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2449)
    BeginChrThread(0x12, 3, 1, 45)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    OP_98(0xFE, 0x0, 0x0, 0x5DC, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_44_2436 end

    def Function_45_2493(): pass

    label("Function_45_2493")

    SetChrFlags(0xFE, 0x20)

    def lambda_249D():

        label("loc_249D")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_249D")

    QueueWorkItem2(0xFE, 2, lambda_249D)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x15)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_24C8():
        OP_9D(0xFE, 0x6B6C, 0xFFFFF448, 0xFFFFBBA4, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_24C8)
    BeginChrThread(0x101, 3, 1, 46)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    OP_98(0x10, 0x0, 0x0, 0x5DC, 0xFA0, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    Return()

    # Function_45_2493 end

    def Function_46_251F(): pass

    label("Function_46_251F")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0x101,
        "#5P#5A#4SOooooooooooooooo!#3S\x02",
    )

    Sound(809, 0, 100, 0)

    def lambda_2559():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFBD98, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2559)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(442, 0, 100, 0)
    Sound(547, 0, 40, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x96)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 700, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x14, 3, 1, 47)
    BeginChrThread(0x13, 3, 1, 48)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x13, 3)
    Return()

    # Function_46_251F end

    def Function_47_2606(): pass

    label("Function_47_2606")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_96(0xFE, 0x6658, 0xFFFFE890, 0xFFFFCE5A, 0x4E20, 0x0)
    Sound(443, 0, 100, 0)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x774C, 0xFFFFE890, 0xFFFFFA9C, 0x1388, 0x3E8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_47_2606 end

    def Function_48_264E(): pass

    label("Function_48_264E")

    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    Sound(809, 0, 100, 0)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x7D0)
    Sound(441, 0, 80, 0)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Return()

    # Function_48_264E end

    def Function_49_2692(): pass

    label("Function_49_2692")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetChrPos(0x101, 24500, -6000, -19000, 0)
    SetChrPos(0x13, 27500, -6000, -22000, 0)
    SetChrPos(0x11, 24500, -6000, -13000, 180)
    SetChrPos(0x10, 27500, -6000, -13000, 180)
    SetChrPos(0x12, 21300, -6000, -16000, 90)
    SetChrPos(0x14, 27500, -5500, -21800, 0)
    SetChrFlags(0x14, 0x8)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x13, 0xA)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17000, 0)
    OP_68(26000, -5000, -16000, 15000)
    MoveCamera(305, 30, 0, 15000)
    FadeToBright(1000, 0)
    OP_0D()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x13, 3, 1, 50)

    label("loc_278A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27A1")
    Sleep(1)
    Jump("loc_278A")

    label("loc_27A1")

    OP_4B(0x14, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Battle between the Irians and smashed\x01",      # 0
            "When dropping onto the mountain to the line\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_4C(0x14, 0xFF)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CC2")
    MoveCamera(315, 25, 0, 2000)
    SetCameraDistance(15000, 2000)
    BeginChrThread(0x101, 3, 1, 62)
    WaitChrThread(0x101, 3)
    Sound(909, 0, 70, 0)
    Sleep(500)

    ChrTalk(
        0x12,
        "#13002F#5P#NIria's team is the point!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x13, 0xA)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    OP_93(0x11, 0x5A, 0x1F4)

    ChrTalk(
        0x11,
        (
            "#12809F#5PGood-bye! It is!\x01",
            "As expected, Ilya! It is!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0x10E, 0x1F4)

    ChrTalk(
        0x10,
        "#13400F#12PHaha, I wonder if such a thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12906F#12P#NWhew.\x01",
            "Go from the front and that team's\x01",
            "Did you think that he could win the physical ability?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_296B():
        OP_93(0x11, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_296B)
    Sleep(30)

    def lambda_297B():
        OP_93(0x10, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_297B)
    Sleep(30)
    WaitChrThread(0x11, 0)
    WaitChrThread(0x10, 0)
    OP_93(0x101, 0x87, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#12506F#5PNo, nothing ….\x02\x03",
            "#12505F…… Wadi in any case.\x01",
            "The earlier \"Rai\" is\x01",
            "What did you mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12900F#12P#NNo, Mr. Ilya\x01",
            "Because it will come to the block,\x01",
            "I think that it is useless to swipe.\x02\x03",
            "#12904F\"Rye\" is a line …\x01",
            "In short, beat the mountain\x01",
            "Being able to drop it on line.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12506F#5PYou know … suddenly said\x01",
            "You do not understand! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12909F#12P#NHaha, I'm sorry.\x02\x03",
            "#12900FWell, take care of yourself again\x01",
            "Let's reverse it somehow.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(909, 0, 70, 0)
    Sleep(500)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x13, 0x2E)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrPos(0x101, 24500, -6000, -19000, 0)
    SetChrPos(0x13, 27500, -6000, -20000, 0)
    SetChrPos(0x11, 24500, -6000, -12000, 180)
    SetChrPos(0x10, 27500, -6000, -13000, 180)
    SetChrFlags(0x14, 0x8)
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(17000, 1500)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x12,
        (
            "#13000F#5P…… Game set! It is!\x02\x03",
            "#13009F4-12,\x01",
            "Iria's team is the winner!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12506F#6PHuh, it is totally defeated ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_30C5")

    label("loc_2CC2")

    OP_2C(0xA5, 0x1)
    BeginChrThread(0x101, 3, 1, 66)
    WaitChrThread(0x101, 3)
    Sound(909, 0, 70, 0)
    Sleep(500)

    ChrTalk(
        0x12,
        "#13002F#5P#NLloyd's team is the point!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x13, 0xA)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)

    ChrTalk(
        0x101,
        "#12500F#6PAlright ……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#13406F#11PTea … …. Feinto.\x01",
            "I thought whether he would come with a strong bang.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#12806F#11PWell, it was the backside.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#12902F#6P#NHuh, it is not good.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x87, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#12504F#11P…… Oh, Wadi\x01",
            "Because they gave me a signal \"Lai\".\x02\x03",
            "#12502FNoticing that the line is empty,\x01",
            "I switched quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12904F#6P#NHuh, because it was sudden, can you understand?\x01",
            "I was slightly worried.\x02\x03",
            "#12909FThis is also a bad guy to let love do?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#12506F#11PDo not be stupid.\x02\x03",
            "#12500FAlright, while mixing hands with this condition,\x01",
            "I will keep tossing around the Ilia!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(909, 0, 70, 0)
    Sleep(500)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x13, 0x2E)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrPos(0x101, 24500, -6000, -19000, 0)
    SetChrPos(0x13, 27500, -6000, -20000, 0)
    SetChrPos(0x11, 24500, -6000, -12000, 180)
    SetChrPos(0x10, 27500, -6000, -13000, 180)
    SetChrFlags(0x14, 0x8)
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(17000, 1500)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x12,
        (
            "#13000F#5P…… Game set! It is!\x02\x03",
            "#13009F12 - 10,\x01",
            "Lloyd's team is the winner! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12509F#6PAlright, I managed to win! It is!\x02",
    )

    CloseMessageWindow()

    label("loc_30C5")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_49_2692 end

    def Function_50_30D1(): pass

    label("Function_50_30D1")

    ClearChrFlags(0x14, 0x8)
    Sound(802, 0, 60, 0)

    def lambda_30E1():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_30E1)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1000)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    ChrTalk(
        0x13,
        "#6P#5APretty!\x02",
    )


    def lambda_3128():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFCC0C, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3128)
    BeginChrThread(0x10, 3, 1, 51)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0xA)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_50_30D1 end

    def Function_51_3169(): pass

    label("Function_51_3169")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_317C():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEDA4, 0xFFFFCD38, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_317C)
    BeginChrThread(0x11, 3, 1, 52)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_51_3169 end

    def Function_52_31A2(): pass

    label("Function_52_31A2")

    SetChrFlags(0xFE, 0x20)

    def lambda_31AC():

        label("loc_31AC")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_31AC")

    QueueWorkItem2(0xFE, 2, lambda_31AC)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    Sound(441, 0, 60, 0)
    SetChrSubChip(0xFE, 0x1)

    def lambda_31D7():
        OP_9D(0xFE, 0x6B6C, 0xFFFFF448, 0xFFFFC75C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_31D7)
    BeginChrThread(0x10, 3, 1, 53)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x8)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_52_31A2 end

    def Function_53_3224(): pass

    label("Function_53_3224")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_323F():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_323F)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    Sound(442, 0, 80, 0)
    EndChrThread(0x14, 0x1)

    ChrTalk(
        0x10,
        "#11P#5AYes!\x02",
    )


    def lambda_3281():
        OP_96(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFB6F4, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3281)
    BeginChrThread(0x101, 3, 1, 54)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_53_3224 end

    def Function_54_32B8(): pass

    label("Function_54_32B8")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_32CB():
        OP_9D(0xFE, 0x6B6C, 0xFFFFED40, 0xFFFFB5C8, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_32CB)
    BeginChrThread(0x13, 3, 1, 55)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_54_32B8 end

    def Function_55_32F1(): pass

    label("Function_55_32F1")

    SetChrFlags(0xFE, 0x20)

    def lambda_32FB():

        label("loc_32FB")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_32FB")

    QueueWorkItem2(0xFE, 2, lambda_32FB)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x1C)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    Sound(441, 0, 80, 0)
    SetChrSubChip(0xFE, 0x1)

    def lambda_3326():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF448, 0xFFFFBBA4, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3326)
    BeginChrThread(0x101, 3, 1, 56)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_55_32F1 end

    def Function_56_3359(): pass

    label("Function_56_3359")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_3374():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFBD98, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3374)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(442, 0, 80, 0)

    ChrTalk(
        0x101,
        "#5P#5AIn return … …!\x02",
    )


    def lambda_33BD():
        OP_96(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFCC0C, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_33BD)
    BeginChrThread(0x11, 3, 1, 57)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_56_3359 end

    def Function_57_33F4(): pass

    label("Function_57_33F4")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_3407():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEC78, 0xFFFFC568, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3407)
    BeginChrThread(0x10, 3, 1, 58)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_57_33F4 end

    def Function_58_342D(): pass

    label("Function_58_342D")

    SetChrFlags(0xFE, 0x20)

    def lambda_3437():

        label("loc_3437")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_3437")

    QueueWorkItem2(0xFE, 2, lambda_3437)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    Sound(441, 0, 80, 0)
    SetChrSubChip(0xFE, 0x1)

    def lambda_3462():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF448, 0xFFFFC75C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3462)
    BeginChrThread(0x11, 3, 1, 59)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x3)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_58_342D end

    def Function_59_34AF(): pass

    label("Function_59_34AF")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_34CA():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_34CA)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)

    ChrTalk(
        0x11,
        "#11P#5AI am disappointed!\x02",
    )


    def lambda_350A():
        OP_96(0xFE, 0x5FB4, 0xFFFFF254, 0xFFFFBF8C, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_350A)
    BeginChrThread(0x101, 3, 1, 60)
    Sleep(100)
    Sound(442, 0, 100, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Return()

    # Function_59_34AF end

    def Function_60_354D(): pass

    label("Function_60_354D")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    Sound(809, 0, 100, 0)

    def lambda_3565():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3565)
    WaitChrThread(0x14, 1)
    Sound(441, 0, 60, 0)

    def lambda_358C():
        OP_9D(0xFE, 0x6B6C, 0xFFFFED40, 0xFFFFB5C8, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_358C)
    BeginChrThread(0x13, 3, 1, 61)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Sleep(500)

    ChrTalk(
        0x13,
        "#6P#5ARide!\x02",
    )

    Sleep(500)
    SetChrFlags(0x10, 0x20)
    OP_93(0x10, 0xB4, 0x1F4)
    ClearChrFlags(0x10, 0x20)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    OP_98(0x10, 0xFFFFFA24, 0x0, 0x0, 0xFA0, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    Return()

    # Function_60_354D end

    def Function_61_360A(): pass

    label("Function_61_360A")

    SetChrFlags(0xFE, 0x20)

    def lambda_3614():

        label("loc_3614")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_3614")

    QueueWorkItem2(0xFE, 2, lambda_3614)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x1C)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_363F():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF448, 0xFFFFBF8C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_363F)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_61_360A end

    def Function_62_3676(): pass

    label("Function_62_3676")

    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_368E():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFBD98, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_368E)
    Sleep(600)

    ChrTalk(
        0x101,
        "#5P#5A#4S……What!#3S\x02",
    )

    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(442, 0, 100, 0)
    Sound(547, 0, 40, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x96)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 700, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_3727():
        OP_96(0xFE, 0x6590, 0xFFFFF060, 0xFFFFC374, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3727)
    BeginChrThread(0x11, 3, 1, 64)
    Sleep(30)
    BeginChrThread(0x10, 3, 1, 63)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    WaitChrThread(0x10, 3)
    Return()

    # Function_62_3676 end

    def Function_63_3771(): pass

    label("Function_63_3771")

    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    Sound(809, 0, 100, 0)

    def lambda_3789():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3789)
    WaitChrThread(0x14, 1)
    Sound(441, 0, 80, 0)
    BeginChrThread(0x14, 3, 1, 65)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    WaitChrThread(0x14, 3)
    Return()

    # Function_63_3771 end

    def Function_64_37CD(): pass

    label("Function_64_37CD")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x1388)
    Sound(809, 0, 100, 0)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Return()

    # Function_64_37CD end

    def Function_65_380B(): pass

    label("Function_65_380B")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_96(0xFE, 0x6FB8, 0xFFFFE890, 0xFFFFBA00, 0x3A98, 0x0)
    Sound(443, 0, 100, 0)
    Sound(441, 0, 100, 0)
    OP_9D(0xFE, 0x7CC4, 0xFFFFE890, 0xFFFFAB50, 0xBB8, 0x3E8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_65_380B end

    def Function_66_3853(): pass

    label("Function_66_3853")

    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_386B():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFBD98, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_386B)
    Sleep(600)

    ChrTalk(
        0x101,
        "#6P#5A#4S…… Ha ha!#3S\x02",
    )

    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(441, 0, 100, 0)
    BeginChrThread(0x14, 3, 1, 68)
    BeginChrThread(0x11, 3, 1, 64)
    Sleep(30)
    BeginChrThread(0x10, 3, 1, 67)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    WaitChrThread(0x14, 3)
    Return()

    # Function_66_3853 end

    def Function_67_38EA(): pass

    label("Function_67_38EA")

    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    Sound(809, 0, 100, 0)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x1388)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x18)
    Sound(30, 0, 100, 0)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_67_38EA end

    def Function_68_3928(): pass

    label("Function_68_3928")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_9D(0xFE, 0x639C, 0xFFFFE890, 0xFFFFD508, 0x7D0, 0x3E8)
    Sound(443, 0, 50, 0)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x639C, 0xFFFFE890, 0xFFFFDAE4, 0x3E8, 0x3E8)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x639C, 0xFFFFE890, 0xFFFFDECC, 0x1F4, 0x3E8)
    Sound(441, 0, 60, 0)
    OP_9D(0xFE, 0x639C, 0xFFFFE890, 0xFFFFE0C0, 0xC8, 0x3E8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_68_3928 end

    def Function_69_39AD(): pass

    label("Function_69_39AD")

    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetChrPos(0x101, 24500, -6000, -22000, 0)
    SetChrPos(0x10, 27500, -6000, -19000, 0)
    SetChrPos(0x11, 24500, -6000, -13000, 180)
    SetChrPos(0x12, 27500, -6000, -13000, 180)
    SetChrPos(0x13, 21300, -6000, -16000, 90)
    SetChrPos(0x14, 24500, -5500, -21800, 0)
    SetChrFlags(0x14, 0x8)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x0)
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17000, 0)
    OP_68(26000, -5000, -16000, 15000)
    MoveCamera(305, 30, 0, 15000)
    FadeToBright(1000, 0)
    OP_0D()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x101, 3, 1, 70)

    label("loc_3AA5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3ABC")
    Sleep(1)
    Jump("loc_3AA5")

    label("loc_3ABC")

    OP_4B(0x14, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Together with all your strength\x01",      # 0
            "Lower the force and lower the toss\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_4C(0x14, 0xFF)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EC4")
    OP_2C(0xA5, 0x1)
    MoveCamera(315, 25, 0, 2000)
    SetCameraDistance(15000, 2000)
    BeginChrThread(0x101, 3, 1, 81)
    WaitChrThread(0x101, 3)
    Sound(909, 0, 70, 0)
    Sleep(500)

    ChrTalk(
        0x13,
        "#12902F#5P#NHuh, this is brilliant.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)
    OP_63(0x11, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x11,
        (
            "#12806FWell, surely Iria … …\x01",
            "It is a physical skill of a foul fight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#13006FSuch a ridiculous height ……\x01",
            "I can not block anything.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    ChrTalk(
        0x10,
        "#13409F#6PHuh, this is roughly like this.\x02",
    )

    CloseMessageWindow()
    OP_93(0x10, 0xE1, 0x1F4)

    ChrTalk(
        0x10,
        (
            "#13400F#12PMy brother also took such a high toss\x01",
            "You gave me a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12500F#5PHaha, if Iría's physical ability\x01",
            "Because I thought I could go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#13409F#12Pふ ぶ, え い い え い ♪\x02\x03",
            "#13400FNow leave the game as it is\x01",
            "I will win it at once! It is!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(909, 0, 70, 0)
    Sleep(500)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x0)
    SetChrPos(0x101, 24500, -6000, -19000, 0)
    SetChrPos(0x10, 27500, -6000, -20000, 0)
    SetChrPos(0x11, 24500, -6000, -12000, 180)
    SetChrPos(0x12, 27500, -6000, -13000, 180)
    SetChrFlags(0x14, 0x8)
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(17000, 1500)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x13,
        (
            "#12900F#5P#N…… Game set! It is!\x02\x03",
            "#12904FAt 12 - 4,\x01",
            "The Lloyd team wins.\x01",
            "Huh, good job.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#12509F#6PAlright, it is a victory! It is!\x02",
    )

    CloseMessageWindow()
    Jump("loc_424C")

    label("loc_3EC4")

    MoveCamera(315, 25, 0, 2000)
    SetCameraDistance(15000, 2000)
    BeginChrThread(0x101, 3, 1, 86)
    WaitChrThread(0x101, 3)
    Sound(909, 0, 70, 0)
    Sleep(500)

    ChrTalk(
        0x13,
        (
            "#12902F#5P#NHuh, sorry.\x01",
            "I could not grasp the opportunity.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)

    ChrTalk(
        0x11,
        "#12806FHie, that's … …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#13011FBut what a jumping force ……\x02\x03",
            "#13006FI was attacked from such a height\x01",
            "As expected it could not be prevented.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_93(0x10, 0xE1, 0x1F4)

    ChrTalk(
        0x10,
        "#13406F#12POh yeah …… Sorry, my brother.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12512FNo, thank you.\x01",
            "No way I could fly so much\x01",
            "I did not see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#12800FHaha, the goddess\x01",
            "Let me know about you.\x01",
            "Go ahead at once, Noel!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#13009FYes!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(909, 0, 70, 0)
    Sleep(500)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x0)
    SetChrPos(0x101, 24500, -6000, -19000, 0)
    SetChrPos(0x10, 27500, -6000, -20000, 0)
    SetChrPos(0x11, 24500, -6000, -12000, 180)
    SetChrPos(0x12, 27500, -6000, -13000, 180)
    SetChrFlags(0x14, 0x8)
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(17000, 1500)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x13,
        (
            "#12900F#5P…… Game set! It is!\x02\x03",
            "#12904F9 - 12,\x01",
            "The Randy team wins.\x01",
            "Huh, good job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12506F#6PWell, have you lost? …\x02",
    )

    CloseMessageWindow()

    label("loc_424C")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_69_39AD end

    def Function_70_4258(): pass

    label("Function_70_4258")

    ClearChrFlags(0x14, 0x8)
    Sound(802, 0, 60, 0)

    def lambda_4268():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4268)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1000)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    ChrTalk(
        0x101,
        "#5P#5A…… Ha ha!\x02",
    )


    def lambda_42AF():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFCC70, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_42AF)
    BeginChrThread(0x11, 3, 1, 71)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_70_4258 end

    def Function_71_42F0(): pass

    label("Function_71_42F0")

    WaitChrThread(0x14, 1)
    Sound(441, 0, 100, 0)
    SetChrSubChip(0xFE, 0x1)

    def lambda_4303():
        OP_9D(0xFE, 0x6AA4, 0xFFFFEC78, 0xFFFFCD38, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4303)
    BeginChrThread(0x12, 3, 1, 72)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_71_42F0 end

    def Function_72_4329(): pass

    label("Function_72_4329")

    SetChrFlags(0xFE, 0x20)

    def lambda_4333():

        label("loc_4333")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_4333")

    QueueWorkItem2(0xFE, 2, lambda_4333)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x15)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    Sound(441, 0, 80, 0)
    SetChrSubChip(0xFE, 0x1)

    def lambda_435E():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF448, 0xFFFFC75C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_435E)
    BeginChrThread(0x11, 3, 1, 73)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x1, 0x10, 0x0, 0xFFFFFA24, 0xFA0, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    Return()

    # Function_72_4329 end

    def Function_73_43B7(): pass

    label("Function_73_43B7")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0x11,
        "#11P#5AQuick haste!\x02",
    )

    Sound(809, 0, 100, 0)

    def lambda_43E6():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_43E6)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)

    def lambda_440E():
        OP_96(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFB6F4, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_440E)
    BeginChrThread(0x101, 3, 1, 74)
    Sleep(100)
    Sound(442, 0, 80, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Return()

    # Function_73_43B7 end

    def Function_74_4451(): pass

    label("Function_74_4451")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)

    def lambda_445E():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFB0B4, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_445E)
    BeginChrThread(0x10, 3, 1, 75)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_74_4451 end

    def Function_75_4484(): pass

    label("Function_75_4484")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    ChrTalk(
        0x10,
        "#6P#5AYes!\x02",
    )


    def lambda_44AA():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEC78, 0xFFFFB5C8, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_44AA)
    BeginChrThread(0x101, 3, 1, 76)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_75_4484 end

    def Function_76_44D0(): pass

    label("Function_76_44D0")

    SetChrFlags(0xFE, 0x20)

    def lambda_44DA():

        label("loc_44DA")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_44DA")

    QueueWorkItem2(0xFE, 2, lambda_44DA)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 60, 0)

    def lambda_4505():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFCC0C, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4505)
    BeginChrThread(0x12, 3, 1, 77)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_76_44D0 end

    def Function_77_4538(): pass

    label("Function_77_4538")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_454B():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEC78, 0xFFFFC568, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_454B)
    BeginChrThread(0x11, 3, 1, 78)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_77_4538 end

    def Function_78_4571(): pass

    label("Function_78_4571")

    SetChrFlags(0xFE, 0x20)

    def lambda_457B():

        label("loc_457B")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_457B")

    QueueWorkItem2(0xFE, 2, lambda_457B)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    ChrTalk(
        0x11,
        "#11P#5AGo!\x02",
    )


    def lambda_45BA():
        OP_9D(0xFE, 0x6B6C, 0xFFFFF448, 0xFFFFC75C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_45BA)
    BeginChrThread(0x12, 3, 1, 79)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    OP_9B(0x1, 0x10, 0x0, 0x5DC, 0xFA0, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x11, 0x20)
    OP_93(0x11, 0xB4, 0x1F4)
    ClearChrFlags(0x11, 0x20)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    OP_98(0x11, 0x5DC, 0x0, 0x0, 0xFA0, 0x0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    Return()

    # Function_78_4571 end

    def Function_79_4641(): pass

    label("Function_79_4641")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_465C():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_465C)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)

    ChrTalk(
        0x12,
        "#11P#5AIn this case! Is it?\x02",
    )

    Sound(442, 0, 80, 0)

    def lambda_46A4():
        OP_96(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFB6F4, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_46A4)
    BeginChrThread(0x10, 3, 1, 80)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Return()

    # Function_79_4641 end

    def Function_80_46E1(): pass

    label("Function_80_46E1")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_46F4():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEC78, 0xFFFFB5C8, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_46F4)
    SetChrFlags(0x101, 0x20)
    OP_93(0x101, 0x5A, 0x1F4)
    ClearChrFlags(0x101, 0x20)
    Sleep(300)
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    EndChrThread(0x101, 0x2)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_80_46E1 end

    def Function_81_4736(): pass

    label("Function_81_4736")


    ChrTalk(
        0x101,
        "#5P#5AIria! It is!\x02",
    )

    SetChrFlags(0xFE, 0x20)

    def lambda_4759():

        label("loc_4759")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_4759")

    QueueWorkItem2(0xFE, 2, lambda_4759)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_4784():
        OP_9D(0xFE, 0x6B6C, 0xFFFFF448, 0xFFFFBBA4, 0xCE4, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4784)
    BeginChrThread(0x10, 3, 1, 82)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x10, 3)
    Return()

    # Function_81_4736 end

    def Function_82_47BB(): pass

    label("Function_82_47BB")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0x10,
        "#5P#5A#4SHa ha! It is!#3S\x02",
    )

    Sound(809, 0, 100, 0)

    def lambda_47F9():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFBD98, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_47F9)
    Sleep(700)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(442, 0, 100, 0)
    Sound(547, 0, 40, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x96)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 700, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x14, 3, 1, 85)
    BeginChrThread(0x11, 3, 1, 83)
    BeginChrThread(0x12, 3, 1, 84)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
    Return()

    # Function_82_47BB end

    def Function_83_48B0(): pass

    label("Function_83_48B0")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x7D0)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_83_48B0 end

    def Function_84_48E2(): pass

    label("Function_84_48E2")

    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x7D0)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_84_48E2 end

    def Function_85_4914(): pass

    label("Function_85_4914")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_96(0xFE, 0x64D2, 0xFFFFE890, 0xFFFFD29C, 0x61A8, 0x0)
    Sound(443, 0, 100, 0)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x54A6, 0xFFFFE890, 0x46A, 0x7D0, 0x3E8)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x48DA, 0xFFFFE890, 0x26B6, 0x3E8, 0x3E8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_85_4914 end

    def Function_86_4979(): pass

    label("Function_86_4979")


    ChrTalk(
        0x101,
        "#5P#5AIria! It is!\x02",
    )

    SetChrFlags(0xFE, 0x20)

    def lambda_499C():

        label("loc_499C")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_499C")

    QueueWorkItem2(0xFE, 2, lambda_499C)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 60, 0)
    BeginChrThread(0x14, 3, 1, 88)
    BeginChrThread(0x10, 3, 1, 87)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x10, 3)
    Return()

    # Function_86_4979 end

    def Function_87_49EB(): pass

    label("Function_87_49EB")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0x10,
        "#5P#5A#4SOkay ….#3SWhat is it! Is it?\x02",
    )

    Sound(809, 0, 100, 0)

    def lambda_4A33():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFBD98, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4A33)
    Sleep(700)
    SetChrSubChip(0xFE, 0x1)
    Sound(590, 0, 100, 0)
    BeginChrThread(0x11, 3, 1, 83)
    BeginChrThread(0x12, 3, 1, 84)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
    Return()

    # Function_87_49EB end

    def Function_88_4A8E(): pass

    label("Function_88_4A8E")

    Sound(443, 0, 40, 0)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFBD98, 0x898, 0x3E8)
    Sound(441, 0, 60, 0)
    OP_9D(0xFE, 0x6F54, 0xFFFFE890, 0xFFFFC091, 0x384, 0x3E8)
    Sound(441, 0, 60, 0)
    OP_9D(0xFE, 0x717A, 0xFFFFE890, 0xFFFFC1E4, 0x12C, 0x3E8)
    Return()

    # Function_88_4A8E end

    SaveToFile()

Try(main)
