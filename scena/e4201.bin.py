from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e4201.bin",                # FileName
        "e4201",                    # MapName
        "e4201",                    # Location
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
        "e4201",                  # 0
        "Squire Cesar",           # 1
        "Squire Marcus",          # 2
        "Sister Ries",            # 3
        "Father Kevin",           # 4
        "APL表示用",              # 5
        "SE制御",                 # 6
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(360, 0)                                        # 0

    ScpFunction((
        "Function_0_168",          # 00, 0
        "Function_1_178",          # 01, 1
        "Function_2_179",          # 02, 2
        "Function_3_946",          # 03, 3
        "Function_4_9CB",          # 04, 4
        "Function_5_A2C",          # 05, 5
        "Function_6_A5B",          # 06, 6
        "Function_7_A85",          # 07, 7
        "Function_8_AA8",          # 08, 8
        "Function_9_AD2",          # 09, 9
        "Function_10_B45",         # 0A, 10
    ))


    def Function_0_168(): pass

    label("Function_0_168")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_177")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_177")

    Return()

    # Function_0_168 end

    def Function_1_178(): pass

    label("Function_1_178")

    Return()

    # Function_1_178 end

    def Function_2_179(): pass

    label("Function_2_179")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch48400.itc", 0x20)
    LoadChrToIndex("apl/ch51728.itc", 0x21)
    SoundLoad(132)
    SoundLoad(868)
    SetChrChipByIndex(0xC, 0x21)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 3000, 0, -13000, 180)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xC, 0x1000)
    SetChrFlags(0xC, 0x800)
    ClearChrFlags(0xC, 0x1)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 2500, -500, -13000, 180)
    SetChrFlags(0xB, 0x1000)
    SetChrFlags(0xB, 0x8)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 3500, 0, -13000, 180)
    SetChrFlags(0xA, 0x8)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 2250, 0, -2600, 0)
    BeginChrThread(0x8, 0, 0, 3)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 14750, 0, -2380, 315)
    BeginChrThread(0x9, 0, 0, 4)
    Sound(132, 2, 60, 0)
    Sound(868, 2, 40, 0)
    BeginChrThread(0xD, 1, 0, 9)
    OP_68(-87080, 3400, 29630, 0)
    MoveCamera(322, 4, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(77770, 0)
    FadeToBright(1000, 0)
    OP_68(-87080, 3400, 29630, 4500)
    MoveCamera(324, 7, 0, 4500)
    OP_6E(500, 4500)
    SetCameraDistance(67500, 4500)
    Sleep(4400)
    OP_68(-89870, 1500, 33150, 0)
    MoveCamera(22, 32, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(47450, 0)
    Fade(500)
    SetCameraDistance(40450, 3500)
    Sleep(1000)
    BeginChrThread(0xD, 2, 0, 10)
    Sleep(2000)
    Sleep(1000)
    OP_68(1230, 1500, 6790, 10000)
    MoveCamera(328, 14, 0, 10000)
    OP_6E(500, 10000)
    SetCameraDistance(47040, 10000)
    OP_6F(0x79)
    PlayBGM("ed7574", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x23E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(3000, 1130, -13000, 0)
    MoveCamera(311, 5, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    Fade(500)
    OP_68(3000, 1002, -13000, 25000)
    MoveCamera(321, 12, 0, 25000)
    OP_6E(500, 25000)
    SetCameraDistance(17500, 25000)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#04306F#6P#40W......Ghhhh......\x02\x03",
            "#04310F...Going head to head\x01",
            "against it was really\x01",
            "reckless, I guess...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#13811F#11P...You reap what you sow.\x02\x03",
            "#13806FReleasing that much Stigma power\x01",
            "in the real world...\x02\x03",
            "#13801FIf my big sister were here, I\x01",
            "think she would've been mad about\x01",
            "such recklessness for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#04306F#6P#30WRight... Looks like the\x01",
            "Grand Master's gonna rip\x01",
            "me a new one...\x02\x03",
            "#04308FI've also broken the\x01",
            "Merkabah...\x02",
        )
    )

    CloseMessageWindow()
    OP_68(3000, 1400, -13000, 0)
    OP_6E(500, 0)
    SetCameraDistance(23000, 0)
    MoveCamera(3, 3, 0, 0)
    Fade(500)
    BeginChrThread(0xB, 0, 0, 5)
    OP_0D()
    BeginChrThread(0xC, 0, 0, 6)
    WaitChrThread(0xC, 0)
    Sleep(500)

    ChrTalk(
        0xB,
        (
            "#04303F#6P#30W*sigh*... If it turns out that\x01",
            "it can't be fixed, will I get\x01",
            "fired from being a Dominion...?\x02\x03",
            "#04300FWell, if that happens, I guess\x01",
            "it'd be alright to make a fresh\x01",
            "start as a Squire once again...\x02\x03",
            "#04304FWhen you become a Knight, I\x01",
            "could support you as well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#13812F#11P...You idiot.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xC, 0, 0, 7)
    WaitChrThread(0xC, 0)

    ChrTalk(
        0xB,
        "#04305F#5P#30WH-Hey...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#13813F#11P#30W......Thank goodness...\x01",
            "......You're really\x01",
            "safe......\x02\x03",
            "The place that big sister\x01",
            "was aiming for is still so\x01",
            "far away, and yet you...\x02\x03",
            "#13812FReally... You always do\x01",
            "these insane stunts...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#04308F#5P#30WRies...\x02\x03",
            "#04304F...Yeah... There's still\x01",
            "so much ahead to do...\x02",
        )
    )

    CloseMessageWindow()
    OP_68(3030, 1360, -14200, 12000)
    SetCameraDistance(16000, 12000)
    MoveCamera(358, 15, 0, 12000)
    BeginChrThread(0xC, 0, 0, 8)
    WaitChrThread(0xC, 0)

    ChrTalk(
        0xB,
        (
            "#04303F#5P#30W...I might always do\x01",
            "crazy things like this,\x01",
            "but...\x02\x03",
            "#04300FWill you keep supporting\x01",
            "me...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#13814F#11P#30W...Of course... How\x01",
            "could I leave you\x01",
            "alone...\x02",
        )
    )

    CloseMessageWindow()
    StopSound(132, 1000, 50)
    StopSound(868, 1000, 10)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("e4213", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_179 end

    def Function_3_946(): pass

    label("Function_3_946")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9CA")
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x13B, 0x12C)
    Sleep(700)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(1000)
    OP_9B(0x0, 0xFE, 0x2D, 0xDAC, 0x3E8, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(2000)
    OP_9B(0x1, 0xFE, 0x5A, 0x3E8, 0x3E8, 0x0)
    Sleep(2000)
    OP_9B(0x1, 0xFE, 0x10E, 0x3E8, 0x3E8, 0x0)
    Sleep(2000)
    OP_9B(0x0, 0xFE, 0x10E, 0xDAC, 0x3E8, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(2000)
    Jump("Function_3_946")

    label("loc_9CA")

    Return()

    # Function_3_946 end

    def Function_4_9CB(): pass

    label("Function_4_9CB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A2B")
    OP_93(0xFE, 0x10E, 0x12C)
    Sleep(700)
    OP_93(0xFE, 0x0, 0x12C)
    Sleep(700)
    OP_93(0xFE, 0x13B, 0x12C)
    Sleep(1000)
    OP_9B(0x1, 0xFE, 0x5A, 0x3E8, 0x3E8, 0x0)
    OP_93(0xFE, 0x10E, 0x12C)
    Sleep(700)
    OP_93(0xFE, 0x13B, 0x12C)
    Sleep(1000)
    OP_9B(0x1, 0xFE, 0x10E, 0x3E8, 0x3E8, 0x0)
    Jump("Function_4_9CB")

    label("loc_A2B")

    Return()

    # Function_4_9CB end

    def Function_5_A2C(): pass

    label("Function_5_A2C")

    OP_68(3030, 1660, -14200, 25000)
    MoveCamera(359, 12, 0, 25000)
    OP_6E(500, 15000)
    SetCameraDistance(20000, 19000)
    Return()

    # Function_5_A2C end

    def Function_6_A5B(): pass

    label("Function_6_A5B")

    Sound(812, 0, 100, 0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    SetChrSubChip(0xFE, 0x2)
    Sleep(150)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    SetChrSubChip(0xFE, 0x4)
    Sleep(450)
    Return()

    # Function_6_A5B end

    def Function_7_A85(): pass

    label("Function_7_A85")

    Sound(898, 0, 100, 0)
    SetChrSubChip(0xFE, 0x4)
    Sleep(150)
    SetChrSubChip(0xFE, 0x5)
    Sleep(150)
    SetChrSubChip(0xFE, 0x6)
    Sleep(150)
    SetChrSubChip(0xFE, 0x7)
    Sleep(450)
    Return()

    # Function_7_A85 end

    def Function_8_AA8(): pass

    label("Function_8_AA8")

    Sound(898, 0, 100, 0)
    SetChrSubChip(0xFE, 0x8)
    Sleep(150)
    SetChrSubChip(0xFE, 0x9)
    Sleep(150)
    SetChrSubChip(0xFE, 0xA)
    Sleep(150)
    SetChrSubChip(0xFE, 0xB)
    Sleep(150)
    SetChrSubChip(0xFE, 0xC)
    Sleep(450)
    Return()

    # Function_8_AA8 end

    def Function_9_AD2(): pass

    label("Function_9_AD2")

    Sound(203, 0, 25, 0)
    Sleep(900)
    Sound(203, 0, 25, 0)
    Sleep(600)
    Sound(887, 0, 15, 0)
    Sleep(500)
    Sound(203, 0, 25, 0)
    Sleep(900)
    Sound(203, 0, 20, 0)
    Sleep(600)
    Sound(887, 0, 15, 0)
    Sleep(500)
    Sound(203, 0, 20, 0)
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

    # Function_9_AD2 end

    def Function_10_B45(): pass

    label("Function_10_B45")

    OP_25(0x364, 0x23)
    Sleep(200)
    OP_25(0x364, 0x1E)
    Sleep(200)
    OP_25(0x364, 0x19)
    Sleep(200)
    OP_25(0x364, 0x14)
    Return()

    # Function_10_B45 end

    SaveToFile()

Try(main)
