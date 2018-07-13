from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        [440, 441, 705, 860, 1006, 1063, 1197, 1426, 1498, 0, 1548, 0, 3309, 3456, 3513, 3667, 0, 3724, 0, 5, 15, 0, 0],
    )

    BuildStringList((
        "t1310_1",                # 0
    ))

    ChipFrameInfo(440, 0)                                        # 0

    ScpFunction((
        "Function_0_1B8",          # 00, 0
        "Function_1_1B9",          # 01, 1
        "Function_2_2C1",          # 02, 2
        "Function_3_35C",          # 03, 3
        "Function_4_3EE",          # 04, 4
        "Function_5_427",          # 05, 5
        "Function_6_4AD",          # 06, 6
        "Function_7_592",          # 07, 7
        "Function_8_5DA",          # 08, 8
        "Function_9_60C",          # 09, 9
        "Function_10_CED",         # 0A, 10
        "Function_11_D80",         # 0B, 11
        "Function_12_DB9",         # 0C, 12
        "Function_13_E53",         # 0D, 13
        "Function_14_E8C",         # 0E, 14
        "Function_15_F05",         # 0F, 15
        "Function_16_F9F",         # 10, 16
        "Function_17_1014",        # 11, 17
        "Function_18_1065",        # 12, 18
        "Function_19_1137",        # 13, 19
        "Function_20_11BF",        # 14, 20
        "Function_21_123E",        # 15, 21
        "Function_22_1320",        # 16, 22
        "Function_23_1368",        # 17, 23
        "Function_24_13A6",        # 18, 24
        "Function_25_1D11",        # 19, 25
        "Function_26_1DA4",        # 1A, 26
        "Function_27_1DDD",        # 1B, 27
        "Function_28_1E83",        # 1C, 28
        "Function_29_1F1B",        # 1D, 29
        "Function_30_1F54",        # 1E, 30
        "Function_31_1FF3",        # 1F, 31
        "Function_32_1FF4",        # 20, 32
        "Function_33_205B",        # 21, 33
        "Function_34_20F1",        # 22, 34
        "Function_35_2143",        # 23, 35
        "Function_36_21AF",        # 24, 36
        "Function_37_21CA",        # 25, 37
        "Function_38_2226",        # 26, 38
        "Function_39_2258",        # 27, 39
        "Function_40_22F7",        # 28, 40
        "Function_41_237C",        # 29, 41
        "Function_42_23A7",        # 2A, 42
        "Function_43_23CF",        # 2B, 43
        "Function_44_2479",        # 2C, 44
        "Function_45_24D6",        # 2D, 45
        "Function_46_2562",        # 2E, 46
        "Function_47_2642",        # 2F, 47
        "Function_48_268A",        # 30, 48
        "Function_49_26CE",        # 31, 49
        "Function_50_31A9",        # 32, 50
        "Function_51_323F",        # 33, 51
        "Function_52_3278",        # 34, 52
        "Function_53_32FA",        # 35, 53
        "Function_54_338B",        # 36, 54
        "Function_55_33C4",        # 37, 55
        "Function_56_342C",        # 38, 56
        "Function_57_34C6",        # 39, 57
        "Function_58_34FF",        # 3A, 58
        "Function_59_3581",        # 3B, 59
        "Function_60_361C",        # 3C, 60
        "Function_61_36D5",        # 3D, 61
        "Function_62_3741",        # 3E, 62
        "Function_63_3838",        # 3F, 63
        "Function_64_3894",        # 40, 64
        "Function_65_38D2",        # 41, 65
        "Function_66_391A",        # 42, 66
        "Function_67_39AE",        # 43, 67
        "Function_68_39EC",        # 44, 68
        "Function_69_3A71",        # 45, 69
        "Function_70_439C",        # 46, 70
        "Function_71_4431",        # 47, 71
        "Function_72_446A",        # 48, 72
        "Function_73_44F8",        # 49, 73
        "Function_74_4596",        # 4A, 74
        "Function_75_45C9",        # 4B, 75
        "Function_76_4612",        # 4C, 76
        "Function_77_467A",        # 4D, 77
        "Function_78_46B3",        # 4E, 78
        "Function_79_4780",        # 4F, 79
        "Function_80_4823",        # 50, 80
        "Function_81_4878",        # 51, 81
        "Function_82_48FA",        # 52, 82
        "Function_83_49E6",        # 53, 83
        "Function_84_4A18",        # 54, 84
        "Function_85_4A4A",        # 55, 85
        "Function_86_4AAF",        # 56, 86
        "Function_87_4B1E",        # 57, 87
        "Function_88_4BBD",        # 58, 88
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
        "#6P#5A──Senior!\x02",
    )


    def lambda_329():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF254, 0xFFFFBBA4, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_329)
    BeginChrThread(0x11, 3, 1, 3)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_2_2C1 end

    def Function_3_35C(): pass

    label("Function_3_35C")

    Sleep(500)
    Sound(809, 0, 100, 0)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)

    def lambda_377():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFBD98, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_377)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    Sound(442, 0, 90, 0)

    ChrTalk(
        0x11,
        "#5P#5AOrah!\x02",
    )


    def lambda_3B1():
        OP_96(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFCC0C, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3B1)
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

    # Function_3_35C end

    def Function_4_3EE(): pass

    label("Function_4_3EE")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_401():
        OP_9D(0xFE, 0x6A40, 0xFFFFEC78, 0xFFFFCD38, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_401)
    BeginChrThread(0x13, 3, 1, 5)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_4_3EE end

    def Function_5_427(): pass

    label("Function_5_427")

    SetChrFlags(0xFE, 0x20)

    def lambda_431():

        label("loc_431")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_431")

    QueueWorkItem2(0xFE, 2, lambda_431)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x1C)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    ChrTalk(
        0x13,
        "#12P#5AI leave it to you!\x02",
    )


    def lambda_47A():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF254, 0xFFFFC694, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_47A)
    BeginChrThread(0x10, 3, 1, 6)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_5_427 end

    def Function_6_4AD(): pass

    label("Function_6_4AD")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_4C8():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4C8)
    Sleep(600)

    ChrTalk(
        0x10,
        "#11P#4S#5AYah!!#3S\x02",
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

    # Function_6_4AD end

    def Function_7_592(): pass

    label("Function_7_592")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_96(0xFE, 0x5AD2, 0xFFFFE890, 0xFFFFADF8, 0x4E20, 0x0)
    Sound(443, 0, 100, 0)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x54F6, 0xFFFFE890, 0xFFFF8FBC, 0x3E8, 0x7D0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_7_592 end

    def Function_8_5DA(): pass

    label("Function_8_5DA")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x7D0)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_8_5DA end

    def Function_9_60C(): pass

    label("Function_9_60C")

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

    label("loc_704")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71B")
    Sleep(1)
    Jump("loc_704")

    label("loc_71B")

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
            "Use a Direct Attack Like This\x01",      # 0
            "Toss and Make Randy Hit it\x01",         # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_4C(0x14, 0xFF)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0F")
    MoveCamera(315, 25, 0, 1500)
    SetCameraDistance(15000, 1500)
    BeginChrThread(0x101, 3, 1, 18)
    WaitChrThread(0x101, 3)
    Sound(909, 0, 70, 0)
    Sleep(500)

    ChrTalk(
        0x10,
        "#13400F#5P#NThere, it's out!!\x02",
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
        "#12506F#6PDamn, I was too impatient...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x13, 0xE1, 0x1F4)

    ChrTalk(
        0x13,
        "#12902FHu hu, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#13006F#5P#NSo close...\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        "#12500FSorry, Randy!\x02",
    )

    CloseMessageWindow()
    OP_93(0x11, 0x10E, 0x1F4)

    ChrTalk(
        0x11,
        (
            "#12800F#12PDon't worry!\x01",
            "We'll recover now!\x02",
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
            "#13400F#5P...Game Set!!\x02\x03",
            "#13409FWazy team wins\x01",
            "with 7 - 12!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12506F#6P*haah*, we lost...\x02",
    )

    CloseMessageWindow()
    Jump("loc_CE1")

    label("loc_A0F")

    OP_2C(0xA5, 0x1)
    MoveCamera(315, 25, 0, 2000)
    SetCameraDistance(15000, 2000)
    BeginChrThread(0x101, 3, 1, 20)
    WaitChrThread(0x101, 3)
    Sound(909, 0, 70, 0)
    Sleep(500)

    ChrTalk(
        0x10,
        "#13405F#5P#NOoh, you're good, Randy!\x02",
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
        "#13002F#11P#NKh...wonderfully done.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x13,
        (
            "#12906F#11POh boy, this height\x01",
            "difference is really tough.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x11, 0x10E, 0x1F4)

    ChrTalk(
        0x11,
        (
            "#12809F#12PNice toss, Lloyd.\x01",
            "As expected of your judgement abilities.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#12509F#5PHa ha, I only jumped the gun there.\x02\x03",
            "#12500FAlright, let's press them on like this!!\x02",
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
            "#13400F#5P...Game Set!!\x02\x03",
            "#13409FThe younger brother's team wins with 12 - 8!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12500F#6PNice, we won!!\x02",
    )

    CloseMessageWindow()

    label("loc_CE1")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_9_60C end

    def Function_10_CED(): pass

    label("Function_10_CED")

    ClearChrFlags(0x14, 0x8)
    Sound(802, 0, 60, 0)

    def lambda_CFD():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_CFD)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1000)
    Sound(441, 0, 100, 0)
    SetChrSubChip(0xFE, 0x1)

    ChrTalk(
        0x12,
        "#11P#5AHaa!\x02",
    )


    def lambda_D3F():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFB6F4, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_D3F)
    BeginChrThread(0x101, 3, 1, 11)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_10_CED end

    def Function_11_D80(): pass

    label("Function_11_D80")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_D93():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEE6C, 0xFFFFB5C8, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_D93)
    BeginChrThread(0x11, 3, 1, 12)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_11_D80 end

    def Function_12_DB9(): pass

    label("Function_12_DB9")

    SetChrFlags(0xFE, 0x20)

    def lambda_DC3():

        label("loc_DC3")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_DC3")

    QueueWorkItem2(0xFE, 2, lambda_DC3)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    ChrTalk(
        0x11,
        "#6P#5AWhoa!\x02",
    )


    def lambda_DFE():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFCC0C, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_DFE)
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

    # Function_12_DB9 end

    def Function_13_E53(): pass

    label("Function_13_E53")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_E66():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEC78, 0xFFFFCD38, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_E66)
    BeginChrThread(0x12, 3, 1, 14)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_13_E53 end

    def Function_14_E8C(): pass

    label("Function_14_E8C")

    SetChrFlags(0xFE, 0x20)

    def lambda_E96():

        label("loc_E96")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_E96")

    QueueWorkItem2(0xFE, 2, lambda_E96)
    Sleep(350)

    ChrTalk(
        0x12,
        "#11P#5AWazy!\x02",
    )

    SetChrChipByIndex(0xFE, 0x15)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_ED2():
        OP_9D(0xFE, 0x6B6C, 0xFFFFF448, 0xFFFFC75C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_ED2)
    BeginChrThread(0x13, 3, 1, 15)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_14_E8C end

    def Function_15_F05(): pass

    label("Function_15_F05")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0x13,
        "#11P#5AHmph...!\x02",
    )

    Sound(809, 0, 100, 0)

    def lambda_F34():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F34)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)

    def lambda_F5C():
        OP_98(0xFE, 0x0, 0xFFFFFCE0, 0xFFFFF830, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_F5C)
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

    # Function_15_F05 end

    def Function_16_F9F(): pass

    label("Function_16_F9F")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    Sound(809, 0, 100, 0)

    def lambda_FB7():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FB7)
    WaitChrThread(0x14, 1)

    def lambda_FD8():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFCD38, 0x3E8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_FD8)
    BeginChrThread(0x12, 3, 1, 17)
    Sound(441, 0, 80, 0)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Return()

    # Function_16_F9F end

    def Function_17_1014(): pass

    label("Function_17_1014")

    WaitChrThread(0x14, 1)
    SetChrFlags(0xFE, 0x20)
    OP_93(0xFE, 0xB4, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_1038():
        OP_9D(0xFE, 0x5FB4, 0xFFFFED40, 0xFFFFB5C8, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1038)
    Sleep(300)
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_17_1014 end

    def Function_18_1065(): pass

    label("Function_18_1065")

    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_107D():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFBBA4, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_107D)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(442, 0, 100, 0)
    Sound(547, 0, 40, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x96)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 700, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(
        0x101,
        "#5P#5A#4SHaah!!#3S\x02",
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

    # Function_18_1065 end

    def Function_19_1137(): pass

    label("Function_19_1137")

    SetChrFlags(0x13, 0x20)

    def lambda_1141():

        label("loc_1141")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_1141")

    QueueWorkItem2(0x13, 2, lambda_1141)
    SetChrFlags(0x12, 0x20)

    def lambda_1158():

        label("loc_1158")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_1158")

    QueueWorkItem2(0x12, 2, lambda_1158)
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

    # Function_19_1137 end

    def Function_20_11BF(): pass

    label("Function_20_11BF")

    SetChrFlags(0xFE, 0x20)

    def lambda_11C9():

        label("loc_11C9")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_11C9")

    QueueWorkItem2(0xFE, 2, lambda_11C9)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    ChrTalk(
        0x101,
        "#5P#5APlease!!\x02",
    )


    def lambda_1207():
        OP_9D(0xFE, 0x6B6C, 0xFFFFF448, 0xFFFFBF8C, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1207)
    BeginChrThread(0x11, 3, 1, 21)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x11, 3)
    Return()

    # Function_20_11BF end

    def Function_21_123E(): pass

    label("Function_21_123E")

    Sleep(600)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_1259():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1259)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(442, 0, 100, 0)
    Sound(547, 0, 40, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x96)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 700, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(
        0x11,
        "#5P#5A#4SOraaaah!!#3S\x02",
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

    # Function_21_123E end

    def Function_22_1320(): pass

    label("Function_22_1320")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_96(0xFE, 0x6F9A, 0xFFFFE890, 0xFFFFCCCA, 0x4E20, 0x0)
    Sound(443, 0, 100, 0)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x7F76, 0xFFFFE7F0, 0x762, 0x1388, 0x3E8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_22_1320 end

    def Function_23_1368(): pass

    label("Function_23_1368")

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

    # Function_23_1368 end

    def Function_24_13A6(): pass

    label("Function_24_13A6")

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

    label("loc_149E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B5")
    Sleep(1)
    Jump("loc_149E")

    label("loc_14B5")

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
            "Anticipate the Heavy Blow and Block\x01",           # 0
            "Read Their Real Intentions and Step Back\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_4C(0x14, 0xFF)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1915")
    MoveCamera(315, 25, 0, 2000)
    SetCameraDistance(15000, 2000)
    BeginChrThread(0x13, 3, 1, 39)
    WaitChrThread(0x13, 3)
    Sound(909, 0, 70, 0)
    Sleep(500)

    ChrTalk(
        0x11,
        (
            "#12809F#5P#NMiss Ilya's team scores!\x02\x03",
            "#12803FStill, Wazy, really...\x01",
            "That's some cunnin' thing you did.\x02",
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
            "#12902F#12PHu hu, don't say a disreputable thing.\x01",
            "This too is a strategy, you know?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0x87, 0x1F4)

    ChrTalk(
        0x10,
        (
            "#13404F#5PWell, being the "serious guys" team our\x01",
            "opponent, this could be the best strategy, eh?\x02",
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
            "#13001F#5PM-Mr. Lloyd...\x01",
            "They're saying such things to us!?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#12510F#12PKh...as if I'd lose here!\x02\x03",
            "#12501FBeing the situation like this, it's guts time, Noｱl!\x01",
            "I'm gonna catch that ball at all costs!!\x02",
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
            "#12800F#5P...Game Set!!\x02\x03",
            "#12809FMiss Ilya's team wins\x01",
            "with 3 - 12!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12506F#6PKh...it was no good, eh...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D05")

    label("loc_1915")

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
            "#12800F#5P#NLloyd's team scores!\x02\x03",
            "#12809FHa ha, nicely done!\x02",
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
            "#12906F#11POh boy, I can't believe he saw through that.\x02\x03",
            "#12902FEven though it's the "serious guys" team,\x01",
            "they're actually pretty good, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12502F#6PConsidering Wazy's personality, I thought\x01",
            "that setting to hide something for sure.\x02\x03",
            "#12504FA frontal attack that would've made us fall.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x12, 0x5A, 0x1F4)

    ChrTalk(
        0x12,
        "#13000F#5PYou did, Mr. Lloyd!\x02",
    )

    CloseMessageWindow()
    OP_93(0x10, 0x5A, 0x1F4)

    ChrTalk(
        0x10,
        (
            "#13400F#5PUh uh, it seems we have\x01",
            "underestimated them too much, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#12904FHa ha, maybe so.\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#12500F#12PAlright, Noｱl!\x01",
            "Let's make the game's\x01",
            "flow ours like this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#13009F#5PYes, roger!\x02",
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
            "#12800F#5P...Game Set!!\x02\x03",
            "#12809FLloyd's team wins\x01",
            "with 12 - 11!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12512F#6PW-We did it...we barely won!\x02",
    )

    CloseMessageWindow()

    label("loc_1D05")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_24_13A6 end

    def Function_25_1D11(): pass

    label("Function_25_1D11")

    ClearChrFlags(0x14, 0x8)
    Sound(802, 0, 60, 0)

    def lambda_1D21():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1D21)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1000)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    ChrTalk(
        0x10,
        "#11P#5AHop!\x02",
    )


    def lambda_1D63():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFB6F4, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1D63)
    BeginChrThread(0x12, 3, 1, 26)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x3)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_25_1D11 end

    def Function_26_1DA4(): pass

    label("Function_26_1DA4")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_1DB7():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEDA4, 0xFFFFB5C8, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1DB7)
    BeginChrThread(0x101, 3, 1, 27)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_26_1DA4 end

    def Function_27_1DDD(): pass

    label("Function_27_1DDD")

    SetChrFlags(0xFE, 0x20)

    def lambda_1DE7():

        label("loc_1DE7")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_1DE7")

    QueueWorkItem2(0xFE, 2, lambda_1DE7)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 60, 0)

    ChrTalk(
        0x101,
        "#6P#5ANoｱl!\x02",
    )


    def lambda_1E22():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF448, 0xFFFFBBA4, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1E22)
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

    # Function_27_1DDD end

    def Function_28_1E83(): pass

    label("Function_28_1E83")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_1E9E():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFBD98, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1E9E)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(442, 0, 80, 0)

    ChrTalk(
        0x12,
        "#5P#5AHaah!!!\x02",
    )


    def lambda_1EDE():
        OP_96(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFCC0C, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1EDE)
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

    # Function_28_1E83 end

    def Function_29_1F1B(): pass

    label("Function_29_1F1B")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_1F2E():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF448, 0xFFFFC75C, 0xC80, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1F2E)
    BeginChrThread(0x10, 3, 1, 30)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_29_1F1B end

    def Function_30_1F54(): pass

    label("Function_30_1F54")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0x10,
        "#11P#5AToryah!\x02",
    )

    Sound(809, 0, 100, 0)

    def lambda_1F82():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1F82)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(442, 0, 80, 0)

    def lambda_1FB0():
        OP_96(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFB30C, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1FB0)
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

    # Function_30_1F54 end

    def Function_31_1FF3(): pass

    label("Function_31_1FF3")

    Return()

    # Function_31_1FF3 end

    def Function_32_1FF4(): pass

    label("Function_32_1FF4")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_2007():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEC78, 0xFFFFBD98, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2007)
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

    # Function_32_1FF4 end

    def Function_33_205B(): pass

    label("Function_33_205B")

    SetChrFlags(0xFE, 0x20)

    def lambda_2065():

        label("loc_2065")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_2065")

    QueueWorkItem2(0xFE, 2, lambda_2065)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x15)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_2090():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFCC0C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2090)
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

    # Function_33_205B end

    def Function_34_20F1(): pass

    label("Function_34_20F1")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    ChrTalk(
        0x13,
        "#12P#5AHere I go...!\x02",
    )


    def lambda_211D():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEC78, 0xFFFFC568, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_211D)
    BeginChrThread(0x10, 3, 1, 35)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_34_20F1 end

    def Function_35_2143(): pass

    label("Function_35_2143")

    SetChrFlags(0xFE, 0x20)

    def lambda_214D():

        label("loc_214D")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_214D")

    QueueWorkItem2(0xFE, 2, lambda_214D)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_2178():
        OP_9D(0xFE, 0x6B6C, 0xFFFFF448, 0xFFFFC75C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2178)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_35_2143 end

    def Function_36_21AF(): pass

    label("Function_36_21AF")

    Sleep(500)
    SetChrChipByIndex(0xFE, 0x3)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_36_21AF end

    def Function_37_21CA(): pass

    label("Function_37_21CA")

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

    # Function_37_21CA end

    def Function_38_2226(): pass

    label("Function_38_2226")

    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x7D0)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_38_2226 end

    def Function_39_2258(): pass

    label("Function_39_2258")

    BeginChrThread(0x101, 3, 1, 37)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_2276():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2276)
    Sleep(600)

    ChrTalk(
        0x13,
        "#12P#5A──Just kidding♪\x02",
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

    # Function_39_2258 end

    def Function_40_22F7(): pass

    label("Function_40_22F7")

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

    # Function_40_22F7 end

    def Function_41_237C(): pass

    label("Function_41_237C")

    BeginChrThread(0x10, 3, 1, 36)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    OP_98(0xFE, 0x0, 0x0, 0xFFFFF830, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_41_237C end

    def Function_42_23A7(): pass

    label("Function_42_23A7")

    Sleep(300)
    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_98(0xFE, 0x0, 0x0, 0xFFFFFC18, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_42_23A7 end

    def Function_43_23CF(): pass

    label("Function_43_23CF")

    BeginChrThread(0x101, 3, 1, 41)
    BeginChrThread(0x12, 3, 1, 42)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_23F3():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_23F3)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)

    ChrTalk(
        0x13,
        "#12P#5AWhat...!?\x02",
    )


    def lambda_2430():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFB118, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2430)
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

    # Function_43_23CF end

    def Function_44_2479(): pass

    label("Function_44_2479")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_248C():
        OP_9D(0xFE, 0x6590, 0xFFFFEC78, 0xFFFFB9B0, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_248C)
    BeginChrThread(0x12, 3, 1, 45)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    OP_98(0xFE, 0x0, 0x0, 0x5DC, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_44_2479 end

    def Function_45_24D6(): pass

    label("Function_45_24D6")

    SetChrFlags(0xFE, 0x20)

    def lambda_24E0():

        label("loc_24E0")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_24E0")

    QueueWorkItem2(0xFE, 2, lambda_24E0)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x15)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_250B():
        OP_9D(0xFE, 0x6B6C, 0xFFFFF448, 0xFFFFBBA4, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_250B)
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

    # Function_45_24D6 end

    def Function_46_2562(): pass

    label("Function_46_2562")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0x101,
        "#5P#5A#4SUwoooo!#3S\x02",
    )

    Sound(809, 0, 100, 0)

    def lambda_2595():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFBD98, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2595)
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

    # Function_46_2562 end

    def Function_47_2642(): pass

    label("Function_47_2642")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_96(0xFE, 0x6658, 0xFFFFE890, 0xFFFFCE5A, 0x4E20, 0x0)
    Sound(443, 0, 100, 0)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x774C, 0xFFFFE890, 0xFFFFFA9C, 0x1388, 0x3E8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_47_2642 end

    def Function_48_268A(): pass

    label("Function_48_268A")

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

    # Function_48_268A end

    def Function_49_26CE(): pass

    label("Function_49_26CE")

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

    label("loc_27C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27DD")
    Sleep(1)
    Jump("loc_27C6")

    label("loc_27DD")

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
            "Aim a Powerful Blow Between Ilya and Randy\x01",      # 0
            "Drop a Curve on the Line Side\x01",                   # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_4C(0x14, 0xFF)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D7A")
    MoveCamera(315, 25, 0, 2000)
    SetCameraDistance(15000, 2000)
    BeginChrThread(0x101, 3, 1, 62)
    WaitChrThread(0x101, 3)
    Sound(909, 0, 70, 0)
    Sleep(500)

    ChrTalk(
        0x12,
        "#13002F#5P#NPoint for Miss Ilya's team!\x02",
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
            "#12809F#5PAlright!!\x01",
            "As expected by Miss Ilya!!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0x10E, 0x1F4)

    ChrTalk(
        0x10,
        "#13400F#12PAhaha, is it all here what they have?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12906F#12P#NOh boy.\x01",
            "Did you think you could win against that\x01",
            "team's physical abilities with a frontal attack?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_29D6():
        OP_93(0x11, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_29D6)
    Sleep(30)

    def lambda_29E6():
        OP_93(0x10, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_29E6)
    Sleep(30)
    WaitChrThread(0x11, 0)
    WaitChrThread(0x10, 0)
    OP_93(0x101, 0x87, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#12506F#5PWell, I feel ashamed...\x02\x03",
            "#12505F...Even so, Wazy.\x01",
            "What did that "lie"\x01",
            "meant just now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12900F#12P#NWell, because Miss Ilya was likely\x01",
            "coming to block, even a powerful\x01",
            "blow would've been useless.\x02\x03",
            "#12904FWith "lie" I meant "line"...\x01",
            "In short, I wanted to tell you to hit it\x01",
            "like a curve and drop it on the line side.\x02",
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
            "#12506F#5PListen now...how could I ever get it\x01",
            "if you told me that all of a sudden!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12909F#12P#NAhaha, my bad, my bad.\x02\x03",
            "#12900FWell, let's pull ourselves together and\x01",
            "somehow make a come from behind, eh?\x02",
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
            "#13000F#5P...Game Set!!\x02\x03",
            "#13009FMiss Ilya's team wins\x01",
            "with 4 - 12!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12506F#6P*sigh*, we failed...\x02",
    )

    CloseMessageWindow()
    Jump("loc_319D")

    label("loc_2D7A")

    OP_2C(0xA5, 0x1)
    BeginChrThread(0x101, 3, 1, 66)
    WaitChrThread(0x101, 3)
    Sound(909, 0, 70, 0)
    Sleep(500)

    ChrTalk(
        0x12,
        "#13002F#5P#NPoint for Mr. Lloyd's team!\x02",
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
        "#12500F#6PAlright! \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#13406F#11POh no...a faint?\x01",
            "I thought it was a powerful blow coming for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#12806F#11PMan, they outsmarted us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#12902F#6P#NHu hu, you did a good performance.\x02",
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
            "#12504F#11P...Yeah, thanks to you giving\x01",
            "me the "lie" signal, Wazy.\x02\x03",
            "#12502FI noticed the side line was empty\x01",
            "and suddenly switched.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12904F#6P#NHu hu, because it was sudden I was\x01",
            "a little concerned if you would've got it.\x02\x03",
            "#12909FCould it be a move made possible by love?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#12506F#11PDon't say nonsense.\x02\x03",
            "#12500FAlright, let's keep attacking their weak spots\x01",
            "and make sport of Miss Ilya and Randy!\x02",
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
            "#13000F#5P...Game Set!!\x02\x03",
            "#13009FMr. Lloyd's team wins\x01",
            "with 12 - 10!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12509F#6PAlright, we won somehow!!\x02",
    )

    CloseMessageWindow()

    label("loc_319D")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_49_26CE end

    def Function_50_31A9(): pass

    label("Function_50_31A9")

    ClearChrFlags(0x14, 0x8)
    Sound(802, 0, 60, 0)

    def lambda_31B9():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_31B9)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1000)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    ChrTalk(
        0x13,
        "#6P#5AHmph...!\x02",
    )


    def lambda_31FE():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFCC0C, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_31FE)
    BeginChrThread(0x10, 3, 1, 51)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0xA)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_50_31A9 end

    def Function_51_323F(): pass

    label("Function_51_323F")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_3252():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEDA4, 0xFFFFCD38, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3252)
    BeginChrThread(0x11, 3, 1, 52)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_51_323F end

    def Function_52_3278(): pass

    label("Function_52_3278")

    SetChrFlags(0xFE, 0x20)

    def lambda_3282():

        label("loc_3282")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_3282")

    QueueWorkItem2(0xFE, 2, lambda_3282)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    Sound(441, 0, 60, 0)
    SetChrSubChip(0xFE, 0x1)

    def lambda_32AD():
        OP_9D(0xFE, 0x6B6C, 0xFFFFF448, 0xFFFFC75C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_32AD)
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

    # Function_52_3278 end

    def Function_53_32FA(): pass

    label("Function_53_32FA")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_3315():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3315)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    Sound(442, 0, 80, 0)
    EndChrThread(0x14, 0x1)

    ChrTalk(
        0x10,
        "#11P#5AHere!\x02",
    )


    def lambda_3354():
        OP_96(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFB6F4, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3354)
    BeginChrThread(0x101, 3, 1, 54)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_53_32FA end

    def Function_54_338B(): pass

    label("Function_54_338B")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_339E():
        OP_9D(0xFE, 0x6B6C, 0xFFFFED40, 0xFFFFB5C8, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_339E)
    BeginChrThread(0x13, 3, 1, 55)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_54_338B end

    def Function_55_33C4(): pass

    label("Function_55_33C4")

    SetChrFlags(0xFE, 0x20)

    def lambda_33CE():

        label("loc_33CE")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_33CE")

    QueueWorkItem2(0xFE, 2, lambda_33CE)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x1C)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    Sound(441, 0, 80, 0)
    SetChrSubChip(0xFE, 0x1)

    def lambda_33F9():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF448, 0xFFFFBBA4, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_33F9)
    BeginChrThread(0x101, 3, 1, 56)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_55_33C4 end

    def Function_56_342C(): pass

    label("Function_56_342C")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_3447():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFBD98, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3447)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(442, 0, 80, 0)

    ChrTalk(
        0x101,
        "#5P#5ABack you go...!\x02",
    )


    def lambda_348F():
        OP_96(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFCC0C, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_348F)
    BeginChrThread(0x11, 3, 1, 57)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_56_342C end

    def Function_57_34C6(): pass

    label("Function_57_34C6")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_34D9():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEC78, 0xFFFFC568, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_34D9)
    BeginChrThread(0x10, 3, 1, 58)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_57_34C6 end

    def Function_58_34FF(): pass

    label("Function_58_34FF")

    SetChrFlags(0xFE, 0x20)

    def lambda_3509():

        label("loc_3509")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_3509")

    QueueWorkItem2(0xFE, 2, lambda_3509)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    Sound(441, 0, 80, 0)
    SetChrSubChip(0xFE, 0x1)

    def lambda_3534():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF448, 0xFFFFC75C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3534)
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

    # Function_58_34FF end

    def Function_59_3581(): pass

    label("Function_59_3581")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_359C():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_359C)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)

    ChrTalk(
        0x11,
        "#11P#5AEat this!\x02",
    )


    def lambda_35D9():
        OP_96(0xFE, 0x5FB4, 0xFFFFF254, 0xFFFFBF8C, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_35D9)
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

    # Function_59_3581 end

    def Function_60_361C(): pass

    label("Function_60_361C")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    Sound(809, 0, 100, 0)

    def lambda_3634():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3634)
    WaitChrThread(0x14, 1)
    Sound(441, 0, 60, 0)

    def lambda_365B():
        OP_9D(0xFE, 0x6B6C, 0xFFFFED40, 0xFFFFB5C8, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_365B)
    BeginChrThread(0x13, 3, 1, 61)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Sleep(500)

    ChrTalk(
        0x13,
        "#6P#5ALie!\x02",
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

    # Function_60_361C end

    def Function_61_36D5(): pass

    label("Function_61_36D5")

    SetChrFlags(0xFE, 0x20)

    def lambda_36DF():

        label("loc_36DF")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_36DF")

    QueueWorkItem2(0xFE, 2, lambda_36DF)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x1C)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_370A():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF448, 0xFFFFBF8C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_370A)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_61_36D5 end

    def Function_62_3741(): pass

    label("Function_62_3741")

    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_3759():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFBD98, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3759)
    Sleep(600)

    ChrTalk(
        0x101,
        "#5P#5A#4S...Haah!#3S\x02",
    )

    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(442, 0, 100, 0)
    Sound(547, 0, 40, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x96)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 700, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_37EE():
        OP_96(0xFE, 0x6590, 0xFFFFF060, 0xFFFFC374, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_37EE)
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

    # Function_62_3741 end

    def Function_63_3838(): pass

    label("Function_63_3838")

    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    Sound(809, 0, 100, 0)

    def lambda_3850():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3850)
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

    # Function_63_3838 end

    def Function_64_3894(): pass

    label("Function_64_3894")

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

    # Function_64_3894 end

    def Function_65_38D2(): pass

    label("Function_65_38D2")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_96(0xFE, 0x6FB8, 0xFFFFE890, 0xFFFFBA00, 0x3A98, 0x0)
    Sound(443, 0, 100, 0)
    Sound(441, 0, 100, 0)
    OP_9D(0xFE, 0x7CC4, 0xFFFFE890, 0xFFFFAB50, 0xBB8, 0x3E8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_65_38D2 end

    def Function_66_391A(): pass

    label("Function_66_391A")

    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_3932():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFBD98, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3932)
    Sleep(600)

    ChrTalk(
        0x101,
        "#6P#5A#4S...Hah!#3S\x02",
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

    # Function_66_391A end

    def Function_67_39AE(): pass

    label("Function_67_39AE")

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

    # Function_67_39AE end

    def Function_68_39EC(): pass

    label("Function_68_39EC")

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

    # Function_68_39EC end

    def Function_69_3A71(): pass

    label("Function_69_3A71")

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

    label("loc_3B69")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B80")
    Sleep(1)
    Jump("loc_3B69")

    label("loc_3B80")

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
            "Use All Your Strength and Toss it High\x01",      # 0
            "Control Your Strength and Toss it Low\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_4C(0x14, 0xFF)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FEB")
    OP_2C(0xA5, 0x1)
    MoveCamera(315, 25, 0, 2000)
    SetCameraDistance(15000, 2000)
    BeginChrThread(0x101, 3, 1, 81)
    WaitChrThread(0x101, 3)
    Sound(909, 0, 70, 0)
    Sleep(500)

    ChrTalk(
        0x13,
        "#12902F#5P#NHu hu, perfect.\x02",
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
            "#12806FA-As expected from Miss Ilya...\x01",
            "She's got cheating-level physical abilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#13006FSuch a crazy height...\x01",
            "I could've never blocked it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    ChrTalk(
        0x10,
        "#13409F#6PUh uh, too easy.\x02",
    )

    CloseMessageWindow()
    OP_93(0x10, 0xE1, 0x1F4)

    ChrTalk(
        0x10,
        (
            "#13400F#12PYounger brother, you did well\x01",
            "doing such a high toss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12500F#5PHa ha, I thought that with Miss Ilya's \x01",
            "physical abilities it could've worked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#13409F#12PUh uh, excellent, excellent♪\x02\x03",
            "#13400FCome now, let's keep it up\x01",
            "and win the game in a flash!!\x02",
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
            "#12900F#5P#N...Game Set!!\x02\x03",
            "#12904FLloyd's team wins\x01",
            "with 12 - 4.\x01",
            "Hu hu, good job.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#12509F#6PGood, it's a complete victory!!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4390")

    label("loc_3FEB")

    MoveCamera(315, 25, 0, 2000)
    SetCameraDistance(15000, 2000)
    BeginChrThread(0x101, 3, 1, 86)
    WaitChrThread(0x101, 3)
    Sound(909, 0, 70, 0)
    Sleep(500)

    ChrTalk(
        0x13,
        (
            "#12902F#5P#NHu hu, too bad.\x01",
            "You couldn't seize the chance.\x02",
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
        "#12806F*pheeew*, that was close...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#13011FStill, what a jumping power...\x02\x03",
            "#13006FIf we had gotten attacked by such a height,\x01",
            "we couldn't really have defended.\x02",
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
        "#13406F#12POh no...sorry, younger brother.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12512FNo, likewise...\x01",
            "I shouldn't have thought you\x01",
            "to be able to jump so high.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#12800FHa ha, it seems that the\x01",
            "Goddess is smilin' on us.\x01",
            "Let's get this done in a flash, Noｱl!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#13009FYes!!\x02",
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
            "#12900F#5P...Game Set!!\x02\x03",
            "#12904FRandy's team wins\x01",
            "with 9 - 12.\x01",
            "Hu hu, good job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12506F#6PKh, we've lost, eh...?\x02",
    )

    CloseMessageWindow()

    label("loc_4390")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_69_3A71 end

    def Function_70_439C(): pass

    label("Function_70_439C")

    ClearChrFlags(0x14, 0x8)
    Sound(802, 0, 60, 0)

    def lambda_43AC():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_43AC)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1000)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    ChrTalk(
        0x101,
        "#5P#5A...Hah!\x02",
    )


    def lambda_43F0():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFCC70, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_43F0)
    BeginChrThread(0x11, 3, 1, 71)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_70_439C end

    def Function_71_4431(): pass

    label("Function_71_4431")

    WaitChrThread(0x14, 1)
    Sound(441, 0, 100, 0)
    SetChrSubChip(0xFE, 0x1)

    def lambda_4444():
        OP_9D(0xFE, 0x6AA4, 0xFFFFEC78, 0xFFFFCD38, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4444)
    BeginChrThread(0x12, 3, 1, 72)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_71_4431 end

    def Function_72_446A(): pass

    label("Function_72_446A")

    SetChrFlags(0xFE, 0x20)

    def lambda_4474():

        label("loc_4474")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_4474")

    QueueWorkItem2(0xFE, 2, lambda_4474)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x15)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    Sound(441, 0, 80, 0)
    SetChrSubChip(0xFE, 0x1)

    def lambda_449F():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF448, 0xFFFFC75C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_449F)
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

    # Function_72_446A end

    def Function_73_44F8(): pass

    label("Function_73_44F8")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0x11,
        "#11P#5ARight there!\x02",
    )

    Sound(809, 0, 100, 0)

    def lambda_452B():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_452B)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)

    def lambda_4553():
        OP_96(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFB6F4, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4553)
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

    # Function_73_44F8 end

    def Function_74_4596(): pass

    label("Function_74_4596")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)

    def lambda_45A3():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFB0B4, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_45A3)
    BeginChrThread(0x10, 3, 1, 75)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_74_4596 end

    def Function_75_45C9(): pass

    label("Function_75_45C9")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    ChrTalk(
        0x10,
        "#6P#5AHere!\x02",
    )


    def lambda_45EC():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEC78, 0xFFFFB5C8, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_45EC)
    BeginChrThread(0x101, 3, 1, 76)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_75_45C9 end

    def Function_76_4612(): pass

    label("Function_76_4612")

    SetChrFlags(0xFE, 0x20)

    def lambda_461C():

        label("loc_461C")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_461C")

    QueueWorkItem2(0xFE, 2, lambda_461C)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 60, 0)

    def lambda_4647():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFCC0C, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4647)
    BeginChrThread(0x12, 3, 1, 77)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_76_4612 end

    def Function_77_467A(): pass

    label("Function_77_467A")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_468D():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEC78, 0xFFFFC568, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_468D)
    BeginChrThread(0x11, 3, 1, 78)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_77_467A end

    def Function_78_46B3(): pass

    label("Function_78_46B3")

    SetChrFlags(0xFE, 0x20)

    def lambda_46BD():

        label("loc_46BD")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_46BD")

    QueueWorkItem2(0xFE, 2, lambda_46BD)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    ChrTalk(
        0x11,
        "#11P#5AGooo!\x02",
    )


    def lambda_46F9():
        OP_9D(0xFE, 0x6B6C, 0xFFFFF448, 0xFFFFC75C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_46F9)
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

    # Function_78_46B3 end

    def Function_79_4780(): pass

    label("Function_79_4780")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_479B():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_479B)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)

    ChrTalk(
        0x12,
        "#11P#5AWhat about this!?\x02",
    )

    Sound(442, 0, 80, 0)

    def lambda_47E6():
        OP_96(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFB6F4, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_47E6)
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

    # Function_79_4780 end

    def Function_80_4823(): pass

    label("Function_80_4823")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_4836():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEC78, 0xFFFFB5C8, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4836)
    SetChrFlags(0x101, 0x20)
    OP_93(0x101, 0x5A, 0x1F4)
    ClearChrFlags(0x101, 0x20)
    Sleep(300)
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    EndChrThread(0x101, 0x2)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_80_4823 end

    def Function_81_4878(): pass

    label("Function_81_4878")


    ChrTalk(
        0x101,
        "#5P#5AMiss Ilya!!\x02",
    )

    SetChrFlags(0xFE, 0x20)

    def lambda_4898():

        label("loc_4898")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_4898")

    QueueWorkItem2(0xFE, 2, lambda_4898)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_48C3():
        OP_9D(0xFE, 0x6B6C, 0xFFFFF448, 0xFFFFBBA4, 0xCE4, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_48C3)
    BeginChrThread(0x10, 3, 1, 82)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x10, 3)
    Return()

    # Function_81_4878 end

    def Function_82_48FA(): pass

    label("Function_82_48FA")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0x10,
        "#5P#5A#4SHaaaaaa!!#3S\x02",
    )

    Sound(809, 0, 100, 0)

    def lambda_492F():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFBD98, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_492F)
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

    # Function_82_48FA end

    def Function_83_49E6(): pass

    label("Function_83_49E6")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x7D0)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_83_49E6 end

    def Function_84_4A18(): pass

    label("Function_84_4A18")

    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x7D0)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_84_4A18 end

    def Function_85_4A4A(): pass

    label("Function_85_4A4A")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_96(0xFE, 0x64D2, 0xFFFFE890, 0xFFFFD29C, 0x61A8, 0x0)
    Sound(443, 0, 100, 0)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x54A6, 0xFFFFE890, 0x46A, 0x7D0, 0x3E8)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x48DA, 0xFFFFE890, 0x26B6, 0x3E8, 0x3E8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_85_4A4A end

    def Function_86_4AAF(): pass

    label("Function_86_4AAF")


    ChrTalk(
        0x101,
        "#5P#5AMiss Ilya!!\x02",
    )

    SetChrFlags(0xFE, 0x20)

    def lambda_4ACF():

        label("loc_4ACF")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_4ACF")

    QueueWorkItem2(0xFE, 2, lambda_4ACF)
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

    # Function_86_4AAF end

    def Function_87_4B1E(): pass

    label("Function_87_4B1E")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0x10,
        "#5P#5A#4SHaaah...#3Swait, no, what!?\x02",
    )

    Sound(809, 0, 100, 0)

    def lambda_4B62():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFBD98, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4B62)
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

    # Function_87_4B1E end

    def Function_88_4BBD(): pass

    label("Function_88_4BBD")

    Sound(443, 0, 40, 0)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFBD98, 0x898, 0x3E8)
    Sound(441, 0, 60, 0)
    OP_9D(0xFE, 0x6F54, 0xFFFFE890, 0xFFFFC091, 0x384, 0x3E8)
    Sound(441, 0, 60, 0)
    OP_9D(0xFE, 0x717A, 0xFFFFE890, 0xFFFFC1E4, 0x12C, 0x3E8)
    Return()

    # Function_88_4BBD end

    SaveToFile()

Try(main)
