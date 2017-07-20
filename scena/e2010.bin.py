from ScenarioHelper import *

def main():
    CreateScenaFile(
        "e2010.bin",                # FileName
        "e2010",                    # MapName
        "e2010",                    # Location
        0x0001,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0xFF,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e2010",                  # 0
        "Sergey Manager",           # 1
        "background",                   # 2
        "Yuri",                 # 3
        "Sykes",               # 4
        "Reggie",                 # 5
        "Minnes",               # 6
        "Black clothes",                   # 7
        "Black clothes",                   # 8
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(440, 0)                                        # 0

    ScpFunction((
        "Function_0_1B8",          # 00, 0
        "Function_1_2C1",          # 01, 1
        "Function_2_327",          # 02, 2
        "Function_3_34C",          # 03, 3
        "Function_4_7CB",          # 04, 4
        "Function_5_BE3",          # 05, 5
        "Function_6_1143",         # 06, 6
        "Function_7_17D9",         # 07, 7
        "Function_8_26DA",         # 08, 8
        "Function_9_32E6",         # 09, 9
        "Function_10_3730",        # 0A, 10
        "Function_11_3AEE",        # 0B, 11
        "Function_12_480E",        # 0C, 12
        "Function_13_668E",        # 0D, 13
        "Function_14_6995",        # 0E, 14
        "Function_15_6B1E",        # 0F, 15
        "Function_16_6C57",        # 10, 16
    ))


    def Function_0_1B8(): pass

    label("Function_0_1B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1CF")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 3)
    Jump("loc_2C0")

    label("loc_1CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_1E3")
    ClearScenarioFlags(0x22, 1)
    Event(0, 4)
    Jump("loc_2C0")

    label("loc_1E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1F7")
    ClearScenarioFlags(0x22, 2)
    Event(0, 5)
    Jump("loc_2C0")

    label("loc_1F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_20B")
    ClearScenarioFlags(0x22, 3)
    Event(0, 6)
    Jump("loc_2C0")

    label("loc_20B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_21F")
    ClearScenarioFlags(0x22, 4)
    Event(0, 7)
    Jump("loc_2C0")

    label("loc_21F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_233")
    ClearScenarioFlags(0x22, 5)
    Event(0, 8)
    Jump("loc_2C0")

    label("loc_233")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_24A")
    ClearScenarioFlags(0x22, 6)
    SetScenarioFlags(0x0, 2)
    Event(0, 9)
    Jump("loc_2C0")

    label("loc_24A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 7)), scpexpr(EXPR_END)), "loc_261")
    ClearScenarioFlags(0x22, 7)
    SetScenarioFlags(0x0, 3)
    Event(0, 10)
    Jump("loc_2C0")

    label("loc_261")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_END)), "loc_275")
    ClearScenarioFlags(0x23, 0)
    Event(0, 11)
    Jump("loc_2C0")

    label("loc_275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_END)), "loc_289")
    ClearScenarioFlags(0x23, 1)
    Event(0, 12)
    Jump("loc_2C0")

    label("loc_289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 3)), scpexpr(EXPR_END)), "loc_29D")
    ClearScenarioFlags(0x23, 3)
    Event(0, 13)
    Jump("loc_2C0")

    label("loc_29D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 4)), scpexpr(EXPR_END)), "loc_2B1")
    ClearScenarioFlags(0x23, 4)
    Event(0, 14)
    Jump("loc_2C0")

    label("loc_2B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 6)), scpexpr(EXPR_END)), "loc_2C0")
    ClearScenarioFlags(0x23, 6)
    Event(0, 16)

    label("loc_2C0")

    Return()

    # Function_0_1B8 end

    def Function_1_2C1(): pass

    label("Function_1_2C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2DB")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 1)
    Jump("loc_326")

    label("loc_2DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2F5")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 2)
    Jump("loc_326")

    label("loc_2F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_30F")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xCD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 3)
    Jump("loc_326")

    label("loc_30F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_326")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x23D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_326")

    Return()

    # Function_1_2C1 end

    def Function_2_327(): pass

    label("Function_2_327")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_34B")
    OP_82(0xA, 0xA, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_2_327")

    label("loc_34B")

    Return()

    # Function_2_327 end

    def Function_3_34C(): pass

    label("Function_3_34C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x8000000)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch02502.itc", 0x22)
    SoundLoad(460)
    OP_68(-1110, 500, 3290, 0)
    MoveCamera(323, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14280, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x0)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0x109, 0x1)
    ClearChrFlags(0x105, 0x1)
    SetChrPos(0x101, 1200, 100, -1900, 180)
    SetChrPos(0x102, -900, 100, -400, 180)
    SetChrPos(0x109, -900, 100, -1700, 180)
    SetChrPos(0x105, 1200, 100, -400, 180)
    SetChrPos(0x8, 200, 100, 1000, 180)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFrame(0xFF, "effect00_add", 0x0, 0x1)
    VolumeBGM(0x3C, 0x3E8)
    FadeToBright(1000, 0)
    OP_68(-570, 500, 500, 3000)
    MoveCamera(323, 22, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(14280, 3000)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#10109F#11PHa … … I will smell a new car ……\x02\x03",
            "#10102FIt seems easy to use around handles\x01",
            "This is a terrific car!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11PI feel comfortable to sit on the seat\x01",
            "Interior design is not too bad.\x02\x03",
            "#10302FHuh, I liked it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#12Pmy mother……\x01",
            "It certainly looks like a good car.\x02\x03",
            "#00002FAnd if this was the size\x01",
            "About eight people are likely to ride a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#5PHuhu, Tio and Randy\x01",
            "It seems to be okay if you come back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004F#11PWell, just start off.\x02\x03",
            "#01002FThe car is good or bad\x01",
            "It rolls and it is a number.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100F#11POK, then we will start off!\x02",
    )

    CloseMessageWindow()
    Sound(470, 0, 100, 0)
    OP_82(0xF, 0x23, 0xBB8, 0x1F4)
    Sleep(500)
    Sound(460, 2, 80, 0)
    BeginChrThread(0x101, 3, 0, 2)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x3)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    SetChrFlags(0x101, 0x1)
    SetChrFlags(0x102, 0x1)
    SetChrFlags(0x109, 0x1)
    SetChrFlags(0x105, 0x1)
    StopSound(460, 1000, 80)
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    VolumeBGM(0x64, 0x64)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x235), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("t6000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_3_34C end

    def Function_4_7CB(): pass

    label("Function_4_7CB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch02502.itc", 0x22)
    SoundLoad(460)
    OP_68(-720, 500, 200, 0)
    MoveCamera(323, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0x109, 0x1)
    ClearChrFlags(0x105, 0x1)
    SetChrPos(0x101, 1200, 100, -1900, 180)
    SetChrPos(0x102, -900, 100, -400, 180)
    SetChrPos(0x109, -900, 100, -1700, 180)
    SetChrPos(0x105, 1200, 100, -400, 180)
    SetChrPos(0x8, 200, 100, 1000, 180)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    BeginChrThread(0x101, 3, 0, 2)
    Sound(460, 2, 80, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(14500, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x109,
        "#10109F#5P~~~~ ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#12PThis is amazing …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#11PYes, although speed is on\x01",
            "It is very stable … ….\x02\x03",
            "#00102FThe engine sound is also very quiet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F#12PStill a pleasant vibration\x01",
            "It is nice to feel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004F#11PAs expected it is ZCF of the world.\x02\x03",
            "#01002FI also personally have one unit,\x01",
            "I want to ride around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#5PHa, the armored car of the guard too\x01",
            "It's my favorite though … ….\x02\x03",
            "#10106FIt seems to be cheating\x01",
            "I am somewhat overwhelmed … …\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(200)

    ChrTalk(
        0x101,
        "#00012F#12PIs not it such a thing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12PHuff, unique to Carmania\x01",
            "It sounds like sensibility.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(460, 1000, 80)
    Sleep(1000)
    EndChrThread(0x101, 0x3)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    SetChrFlags(0x101, 0x1)
    SetChrFlags(0x102, 0x1)
    SetChrFlags(0x109, 0x1)
    SetChrFlags(0x105, 0x1)
    SetScenarioFlags(0x22, 0)
    NewScene("r4000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_7CB end

    def Function_5_BE3(): pass

    label("Function_5_BE3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch02502.itc", 0x22)
    SoundLoad(460)
    OP_68(99290, 600, 1470, 0)
    MoveCamera(323, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14280, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0x109, 0x1)
    ClearChrFlags(0x105, 0x1)
    SetChrPos(0x101, 98950, 150, 1900, 0)
    SetChrPos(0x102, 101000, 150, 250, 0)
    SetChrPos(0x109, 101000, 150, 1800, 0)
    SetChrPos(0x105, 98950, 150, 250, 0)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 300, 100, 1100, 180)
    SetChrPos(0x8, 100000, 150, -1350, 0)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    BeginChrThread(0x101, 3, 0, 2)
    Sound(460, 2, 80, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(13280, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)
    Sleep(300)

    ChrTalk(
        0x8,
        "#01003F#6P─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#5PYeah ….\x01",
            "I already informed the department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#5PWell, I do not know who it is\x01",
            "Even though I think about it, it is not normal.\x02\x03",
            "#10301FSuch an unusual combat strength\x01",
            "I am not trying to hide it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01001F#6P…… The problem is there.\x02\x03",
            "#01003FIf you were a terrorist or hunter,\x01",
            "You should hide your combat strength.\x02\x03",
            "#01000FNo matter how much you crossbell,\x01",
            "Even if there is no legal law to be enforced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F#5PIs not it …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#12PBlack moon and the Imperial government also\x01",
            "It shows disturbing movements … ….\x02\x03",
            "#00101FShake back after Luberce disappears\x01",
            "It seems that it started under the water surface.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01006F#6PTo say under the water\x01",
            "It seems to be too explicit.\x02\x03",
            "#01000FThere is a commerce meeting at the end of this month.\x02\x03",
            "You too will be busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PYes, I understand.\x02\x03",
            "#00001F…… For the time being, the identity of that man\x01",
            "It seems necessary to make sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PI see …\x01",
            "Where are you staying?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(12780, 2000)
    OP_6F(0x79)
    OP_0D()
    StopSound(460, 1000, 80)
    Sleep(1000)
    EndChrThread(0x101, 0x3)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    SetChrFlags(0x101, 0x1)
    SetChrFlags(0x102, 0x1)
    SetChrFlags(0x109, 0x1)
    SetChrFlags(0x105, 0x1)
    SetScenarioFlags(0x22, 0)
    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_BE3 end

    def Function_6_1143(): pass

    label("Function_6_1143")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    SoundLoad(460)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xCC, 0x8F, 0x85, 0x0, 0xE6, 0x0)
    OP_68(-720, 500, 200, 0)
    MoveCamera(323, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x102, 1200, 100, -1900, 180)
    SetChrPos(0x101, -900, 100, -400, 180)
    SetChrPos(0x109, -900, 100, -1700, 180)
    SetChrPos(0x104, 1200, 100, -400, 180)
    SetChrPos(0x105, 0, 100, 1000, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0xB, 0x4)
    BeginChrThread(0x101, 3, 0, 2)
    Sound(460, 2, 80, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(14500, 2000)
    OP_6F(0x79)
    OP_0D()
    Sound(2367, 255, 80, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 4)), scpexpr(EXPR_END)), "loc_135F")

    ChrTalk(
        0x104,
        (
            "#00309F#11PI also thought of coming here\x01",
            "Really a good car.\x02\x03",
            "#00302FIf you can have such a car yourself\x01",
            "Is not it all - you - can - e?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13C2")

    label("loc_135F")


    ChrTalk(
        0x104,
        (
            "#00309F#11PIt's a nice car.\x02\x03",
            "#00302FIf you can have such a car yourself\x01",
            "Is not it all - you - can - e?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13C2")

    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00012F#5PYou know.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x1)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10302F#5PHuh, let's rely on Asi\x01",
            "You do not have much time yet?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x2)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00301F#11PUg ……\x01",
            "It is cheeky for juniors' habit.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00109F#6PHehu ……\x01",
            "As expected#2RFu#That's bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102F#5PRandy's senior proud proud\x01",
            "Waji, I do not have a shape, do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#11PHey, Noel!\x01",
            "Even though he is from the same guard, he is very heartless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10112F#5PHuh, I'm sorry.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 4)), scpexpr(EXPR_END)), "loc_171D")

    ChrTalk(
        0x101,
        (
            "#00005F#5PWell, Randy.\x02\x03",
            "#00000FI borrow a spare key from the section manager\x01",
            "You came in this car, were not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#6PDriven by the driving vehicle\x01",
            "Did you come to be able to do it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#11POh, between training\x01",
            "I just remembered it.\x02\x03",
            "#00300FYou guys also learn and remember?\x01",
            "It's pretty useful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#5PHaha, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#6PGiven the future\x01",
            "Remember, it may not be damaging.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#5PWell, I think that's somewhat\x01",
            "You had better drive.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_171D")

    Sleep(150)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10101F#11PAh……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x105, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x0)
    Sleep(300)
    SetCameraDistance(15000, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(460, 1000, 80)
    Sleep(1000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x104, 0x4)
    SetScenarioFlags(0x22, 2)
    NewScene("r2060", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_6_1143 end

    def Function_7_17D9(): pass

    label("Function_7_17D9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    SoundLoad(460)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xCC, 0x8F, 0x85, 0x0, 0xE6, 0x0)
    OP_68(150500, 700, 250, 0)
    MoveCamera(307, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14270, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 150400, 100, -1100, 90)
    SetChrPos(0x102, 151900, 100, 900, 90)
    SetChrPos(0x109, 151900, 100, -1100, 90)
    SetChrPos(0x105, 148800, 100, -100, 90)
    SetChrPos(0x104, 150400, 100, 900, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0xB, 0x4)
    BeginChrThread(0x101, 3, 0, 2)
    Sound(460, 2, 80, 0)
    SetCameraDistance(13770, 1000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00008F#5P…. Unity,\x01",
            "I wonder who was doing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11PThe purpose is not clear\x01",
            "It feels unnecessary creepy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#6PThat explosive ….\x01",
            "Where did you procure?\x02\x03",
            "Almost even the guards\x01",
            "It is not used … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#5POita, it remained in the former mine\x01",
            "blasting#4RHa ha#Is not it something you used?\x02\x03",
            "#10300FWell, for me also about gunpowder\x01",
            "I do not know much about it, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F#5PNo, not.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x105, 0x1)
    Sleep(300)

    ChrTalk(
        0x105,
        "#10305F#5POh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#12PDo you know something?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x2)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00301F#11PAround the entrance\x01",
            "Although it is drifting smoke … …\x02\x03",
            "About one or two years after being formulated\x01",
            "It was a smell of new explosives.\x02\x03",
            "Moreover, it is a rather high performance guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6PWell, maybe ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105F#6PBut you know well, do not you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F#11PA heavy weapon using explosives\x01",
            "Completely waste#2RSoda#It was not done.\x02\x03",
            "Although it is rarely used in the regular army\x01",
            "I still like the favorite things.\x02\x03",
            "#00303F…… especially hunters#6RJaeger#Nearby.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
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
        "#00013F#6PNo way ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#12PWell, that is ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#11PWell, it is the story of the possibility to the last.\x02\x03",
            "#00300FIncidentally, a pyrotechnic heavy weapon\x01",
            "Eleventh is the most used.\x02\x03",
            "Even now Rheinfault\x01",
            "I'm leaving a lineup.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#6PIs that so……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#5PHe is definitely familiar with it.\x02\x03",
            "#10303FBut Elevenia ……\x01",
            "Early signs will overlap.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#6PAh……\x01",
            "I guess there was also yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F#11PWhat, what happened?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#12PWell, actually.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I explained the circumstances of reuniting with Lecture Special Captain.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00301F#11P── That playboy,\x01",
            "Is it Ebonia's spy?\x02\x03",
            "Whatever you think is a Tada\x01",
            "I thought that it was not … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PRather than just a spy\x01",
            "It should be called an information officer.\x02\x03",
            "Before the trade meeting\x01",
            "It may be just collecting information\x01",
            "I do not think so.\x02\x03",
            "#00008F…… I was together.\x01",
            "I am worried about the redheaded child … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#12P…… Fuu, that child …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F#5PHuh, for you\x01",
            "You seem to have become traumatic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#11PWhat is it?\x01",
            "It seems like a sexy story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10112F#6PActually ……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I was with Rector\x01",
            "I explained about a redhead girl.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00305F#11P… …. Oh …………\x02\x03",
            "……………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00112F#12POh, let's stop that girl's story.\x02\x03",
            "#00113FTo Mr. Ilya at all\x01",
            "Lesha's being sexually harassed\x01",
            "I feel like I knew my feelings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PHaha, it is terrible persuasive power.\x02\x03",
            "#00008F…… But before unfamiliar\x01",
            "It was in my pocket … …\x02\x03",
            "#00001FI'm not just a civilian\x01",
            "I think there is no mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#6Pby the way……\x01",
            "People who met at the West Crossbell Highway\x01",
            "I came from the direction of the empire.\x02\x03",
            "#10105FOh, by the way,\x01",
            "That man was also redheaded ……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x0)
    Sleep(50)
    SetChrSubChip(0x101, 0x0)
    Sleep(200)

    ChrTalk(
        0x105,
        "#10305F#5POh, if you ask me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PCaptain Rector and that girl\x01",
            "Even redheads have different shades ….\x02\x03",
            "#00001FThinking about that, the man and the man of the eye of the eye\x01",
            "It may have been a color that looks exactly like that.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x105, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00011F#6Pthat……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#12PPossibly, …\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0x1770)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(2374, 255, 100, 0)

    ChrTalk(
        0x104,
        (
            "#00304F#11P#30Wmy mother……\x02\x03",
            "#00311F#30W─ ─ That means my redhead too\x01",
            "It is similar to them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10111F#6PAh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301F#5P…… even if not necessarily\x01",
            "It seems to me that?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(100)
    SetChrSubChip(0x104, 0x0)
    Sleep(200)
    Sound(2375, 255, 100, 0)
    Sleep(1300)

    ChrTalk(
        0x104,
        (
            "#00304F#5P#40W… … You came.\x02\x03",
            "#00312F#40W─ ─ ─ So you came#12R噵 噵 噵 噵 噵 噵#.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(13520, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(460, 1000, 80)
    Sleep(1000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x104, 0x4)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 3)
    NewScene("r2060", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_17D9 end

    def Function_8_26DA(): pass

    label("Function_8_26DA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_7D(0xBE, 0xBE, 0xBE, 0x0, 0x0)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    LoadChrToIndex("apl/ch50011.itc", 0x23)
    SoundLoad(460)
    SoundLoad(803)
    SoundLoad(3451)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(150500, 700, 250, 0)
    MoveCamera(307, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14270, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 150400, 100, -1100, 90)
    SetChrPos(0x102, 151900, 100, 900, 90)
    SetChrPos(0x109, 151900, 100, -1100, 90)
    SetChrPos(0x105, 148800, 100, -100, 90)
    SetChrPos(0x104, 150400, 100, 900, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0xB, 0x4)
    BeginChrThread(0x101, 3, 0, 2)
    PlayBGM("ed7516", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x204), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(460, 2, 80, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(13770, 1000)
    OP_0D()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00001F#6PCome on, Randy ─\x02",
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)
    Sleep(200)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    Sleep(50)
    SetChrSubChip(0x105, 0x2)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00006F#5PUh, at such a time …\x02",
    )

    CloseMessageWindow()
    Sound(804, 0, 100, 0)
    OP_24(0x323)
    Fade(250)
    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0x9)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    Sleep(500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    Sound(2084, 255, 100, 0)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00001F#3PYes, Special Affairs Support Division,\x01",
            "It is Lloyd · Bannings.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of a man")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3451V#40W── Bannings, I am.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xD7B)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005FOh, Mr. Dudley.\x02\x03",
            "#00000FI was told that I was on a business trip\x01",
            "You returned, did not you?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh, in the late afternoon.\x02\x03",
            "I heard the story from Emma.\x01",
            "You seem to have been taken care of.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00004FNo, please do not mind.\x02\x03",
            "#00001FMore than that …\x01",
            "what happened?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh, once again to you\x01",
            "I am thinking to tell him.\x02\x03",
            "─ ─ In the site of Rubathe\x01",
            "A new owner has been decided.\x02\x03",
            "It is a company called \"Crimson Shokai.\"\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005F\"Crimson Shokai\" … …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00011FWhat! Is it?\x01",
            "\"Black moon#4RHayuue#Is not it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Try to hide behind the guys\x01",
            "It seems that the contract was contracted in a shocking manner.\x02\x03",
            "Apparently from the direction of the Empire\x01",
            "It seems that there was also a back work.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00011FFrom the empire … …\x02\x03",
            "#00013FWhat on earth is your company?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is called \"Neue Bran\" in Teito\x01",
            "It is a company that runs high-end clubs.\x02\x03",
            "Crossbell City also has its branch\x01",
            "It is open about a year ago.\x02\x03",
            "The company is crossbelled\x01",
            "That's why we have made full-scale entry.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00001FBut, of course,\x01",
            "It is not just a company, is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ah……\x02\x03",
            "…… Orlando is there?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005FRandy?\x01",
            "Yes, as I got together … …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "About \"Crimson Shokai\"\x01",
            "You better listen to me.\x02\x03",
            "── Also contact at night.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(813, 0, 80, 0)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00011FAh……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(804, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)

    ChrTalk(
        0x102,
        "#00108F#11PWhere are you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301F#5PIt looks like a queen smelly\x01",
            "I guess I was talking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5P─ ─ I see.\x01",
            "Did you aim for the site of Rubatse?\x02\x03",
            "#00300F#11PNoel, when I reach the town\x01",
            "Would you please drop in at the entertainment district?\x02\x03",
            "Ask before the back street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F#6PWell, that does not matter … …\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrSubChip(0x101, 0x1)
    Sleep(200)
    SetChrSubChip(0x105, 0x0)

    ChrTalk(
        0x101,
        (
            "#00003F#6P…… Randy.\x02\x03",
            "#00013F\"Crimson Shokai\" is\x01",
            "What kind of company is it?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    SetChrSubChip(0x104, 0x0)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00306F#5P#30WAh……\x02\x03",
            "#00303FHigh class club \"Neue-Blanc\"\x01",
            "Company of the Empire of Japan to manage … …\x02\x03",
            "#00311FBut its actual situation is ──\x01",
            "Hunting Corps \"Red constellation\" has\x01",
            "It is a dummy company for financing.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(14270, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(460, 1000, 80)
    Sleep(1000)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x104, 0x4)
    OP_24(0x323)
    SetScenarioFlags(0x22, 0)
    NewScene("r2030", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_8_26DA end

    def Function_9_32E6(): pass

    label("Function_9_32E6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x101, 151950, 100, 950, 90)
    SetChrPos(0x102, 150400, 100, -1050, 90)
    SetChrPos(0x109, 151750, 170, -1150, 90)
    SetChrPos(0x103, 150400, 100, 950, 90)
    SetChrPos(0x104, 148850, 100, -950, 90)
    SetChrPos(0x105, 148850, 100, 750, 90)
    SetMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x1, 0x9)
    OP_49()
    SetChrPos(0x9, 150000, 0, 0, 270)
    OP_D5(0x9, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFrame(0x1, "main", 0x2, "stop")
    SetMapObjFrame(0xFF, "effect00_add", 0x0, 0x1)
    VolumeBGM(0x46, 0x3E8)
    OP_68(150000, 750, 0, 0)
    MoveCamera(305, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(15000, 1500)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00008F#5PThe current … …\x01",
            "Is it an ambulance to the hospital?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#5PYeah, Ursula hospital\x01",
            "Is it a registered vehicle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F#5PIs he three of them …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#5PAfter all the injured person of derailment accident\x01",
            "I wonder if they are carrying …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#5PWell, this timing\x01",
            "I guess there is no mistake?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5P…… Cecil's older sisters too\x01",
            "It seems to be busy.\x02\x03",
            "#00001FLet's hurry to the scene.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#5PRoger\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x103, 0x4)
    SetScenarioFlags(0x162, 6)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1D), scpexpr(EXPR_PUSH_LONG, 0x21410100), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36E4")
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    VolumeBGM(0x64, 0x64)
    SetScenarioFlags(0x22, 1)
    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_372F")

    label("loc_36E4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1D), scpexpr(EXPR_PUSH_LONG, 0x21302000), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3709")
    VolumeBGM(0x64, 0x3E8)
    Sleep(1000)
    NewScene("c0200", 99, 0, 0)
    IdleLoop()
    Jump("loc_372F")

    label("loc_3709")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1D), scpexpr(EXPR_PUSH_LONG, 0x21410000), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_372F")
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    VolumeBGM(0x64, 0x64)
    NewScene("r1000", 99, 0, 0)
    IdleLoop()

    label("loc_372F")

    Return()

    # Function_9_32E6 end

    def Function_10_3730(): pass

    label("Function_10_3730")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    OP_68(-440, 750, 140, 0)
    MoveCamera(317, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x2)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x2)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x103, 0x4)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0x109, 0x1)
    ClearChrFlags(0x105, 0x1)
    ClearChrFlags(0x104, 0x1)
    ClearChrFlags(0x103, 0x1)
    SetChrPos(0x101, 1300, 100, -1900, 180)
    SetChrPos(0x102, -800, 100, -400, 180)
    SetChrPos(0x109, -800, 100, -1700, 180)
    SetChrPos(0x103, 1300, 100, -400, 180)
    SetChrPos(0x104, -800, 100, 1100, 180)
    SetChrPos(0x105, 1300, 100, 1100, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x4, 0x9)
    OP_49()
    SetChrPos(0x9, -8000, 0, 4000, 180)
    OP_D5(0x9, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFrame(0x4, "main", 0x2, "stop")
    SetMapObjFrame(0x4, "obj00", 0x2, "stop")
    SetMapObjFrame(0xFF, "effect00_add", 0x0, 0x1)
    VolumeBGM(0x46, 0x3E8)
    FadeToBright(1000, 0)
    SetCameraDistance(15000, 1500)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        "#00001F#12PNow the bus is ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#11PTo and from the Republic\x01",
            "It is a passenger bus that is used.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#11PMaybe, passengers on the train\x01",
            "transfer#4RLooking back#I guess they are transporting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#11PWhew, it is serious.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#12P…… The scale of the accident\x01",
            "How is it?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(14500, 2000)
    OP_6F(0x79)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x103, 0x4)
    SetChrFlags(0x101, 0x1)
    SetChrFlags(0x102, 0x1)
    SetChrFlags(0x109, 0x1)
    SetChrFlags(0x105, 0x1)
    SetChrFlags(0x104, 0x1)
    SetChrFlags(0x103, 0x1)
    SetScenarioFlags(0x162, 7)
    SetScenarioFlags(0x22, 0)
    NewScene("r1010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_10_3730 end

    def Function_11_3AEE(): pass

    label("Function_11_3AEE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    SoundLoad(468)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    OP_68(100040, 950, 320, 0)
    MoveCamera(317, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15750, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x101, 98800, 100, 1700, 0)
    SetChrPos(0x102, 98800, 100, 100, 0)
    SetChrPos(0x109, 101000, 100, 1700, 0)
    SetChrPos(0x105, 101000, 100, -1400, 0)
    SetChrPos(0x104, 98800, 100, -1400, 0)
    SetChrPos(0x103, 101000, 100, 100, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    BeginChrThread(0x101, 3, 0, 2)
    VolumeBGM(0x46, 0x3E8)
    Sound(468, 2, 100, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(15000, 1500)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x109,
        "#5P#10110FTh-This is……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#5PSuch a terrible ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00311F#5P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00010FCow, anyway the situation\x01",
            "I have to make sure what's going on ……\x02",
        )
    )

    CloseMessageWindow()
    Sound(867, 0, 60, 0)
    Sleep(300)
    SetMessageWindowPos(220, 20, -1, -1)
    SetChrName("Voice of a man")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "── Sergei, can you hear it?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x101, 0x2)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x102, 0x0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x103, 0x0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5P#00007FManager……! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00101FIs it okay? Is it?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(220, 20, -1, -1)
    SetChrName("Sergei's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh, somehow.\x02\x03",
            "The police headquarters was attacked\x01",
            "The support department will contact you in each direction\x01",
            "It is a situation that it is taking charge of.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#5P#00013FThe police headquarters … …! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10107FWell, I have to go in a hurry …!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(220, 20, -1, -1)
    SetChrName("Sergei's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No, I already have it.\x01",
            "Sonja troops are heading.\x02\x03",
            "If you can, you\x01",
            "Towards the port area.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#5P#00005FPort area ……?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(220, 20, -1, -1)
    SetChrName("Sergei's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Just a few of the hunters\x01",
            "It seems he blew up the branch office of the black moon.\x02\x03",
            "Continue to IBC building\x01",
            "She seems to have gone on board.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(220, 20, -1, -1)
    SetChrName("Sergei's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Currently, the main force of the enemy is\x01",
            "I am attacking the Orkis Tower.\x02\x03",
            "Arios and Dudley\x01",
            "It seems to be holding,\x01",
            "The guard's help would be necessary.\x02\x03",
            "Other hypocrite men ……\x01",
            "Military demons released to the city area\x01",
            "It seems to be full because it clears up.\x02\x03",
            "If I could rush\x01",
            "There are only you.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x102,
        "#5P#00108FOkay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00201F…… Support Section#6Rthere#If you are\x01",
            "Are you okay?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(220, 20, -1, -1)
    SetChrName("Sergei's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Pedestrians are to the extent possible\x01",
            "I evacuated it in the support department.\x02\x03",
            "Because Zeit is turning\x01",
            "Military monsters will not come near.\x02\x03",
            "There is also Kaya properly,\x01",
            "Well do not worry.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x103,
        "#6P#00206F……Is that so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10301FI hear you're okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00013F─ ─ All right.\x01",
            "I will head to the port area from this.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(220, 20, -1, -1)
    SetChrName("Sergei's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ah……\x01",
            "Be wary of it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(899, 0, 80, 0)
    Sleep(500)

    ChrTalk(
        0x105,
        (
            "#6P#10308FIBC Building ……\x01",
            "Is it supposed to be Mira aim?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003FI do not know but …\x01",
            "It seems better to hurry anyway.\x02\x03",
            "#00008FActually it was attacked\x01",
            "I am worried about the police headquarters, though …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106F……Yes………\x01",
            "But let's hurry anyway.\x02\x03",
            "#10101FAlso in your IBC building\x01",
            "Did you know each other?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00106FI see …\x01",
            "The possibility that there is a bell is high.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00208FJonah and the chief … …\x01",
            "I think that he is in the office of the foundation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#5PTentatively\x01",
            "When I arrived at the port area\x01",
            "You had better stop the car.\x02\x03",
            "#00301FIf you approach the car badly\x01",
            "Anti-tank missile#14RPanzer Fausto#To\x01",
            "Maybe it will be blown off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00011FIs there a danger to that … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FOK.\x01",
            "I will hurry to the entrance of the port area.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    StopSound(468, 2000, 100)
    OP_68(100000, 850, -3500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "After that, head for the province\x01",
            "After breaking apart from the guard's car … …\x02\x03",
            "A guided vehicle with Lloyd's on it\x01",
            "While avoiding battle, via East Street\x01",
            "I arrived at the port area.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x103, 0x4)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7150", "ed7544")
    OP_24(0x1D4)
    SetScenarioFlags(0x22, 2)
    NewScene("c120B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_11_3AEE end

    def Function_12_480E(): pass

    label("Function_12_480E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch02902.itc", 0x22)
    LoadChrToIndex("chr/ch03102.itc", 0x23)
    LoadChrToIndex("chr/ch03202.itc", 0x24)
    LoadChrToIndex("chr/ch00902.itc", 0x25)
    OP_68(-610, 700, 50, 0)
    MoveCamera(321, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14400, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48BE")
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x0)

    label("loc_48BE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48D6")
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x105, 0x0)

    label("loc_48D6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48EE")
    SetChrChipByIndex(0x106, 0x24)
    SetChrSubChip(0x106, 0x0)

    label("loc_48EE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4906")
    SetChrChipByIndex(0x10A, 0x25)
    SetChrSubChip(0x10A, 0x0)

    label("loc_4906")

    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0xF4, 0x4)
    SetChrFlags(0xF5, 0x4)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0x103, 0x1)
    ClearChrFlags(0x104, 0x1)
    ClearChrFlags(0xF4, 0x1)
    ClearChrFlags(0xF5, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4A31")
    SetChrPos(0x109, -800, 100, -1700, 180)
    SetChrPos(0x101, 1300, 100, -1900, 180)
    SetChrPos(0x103, 1300, 100, -400, 180)
    SetChrPos(0x102, -800, 100, -400, 180)
    SetChrPos(0x104, -700, 100, 1100, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_49CD")
    SetChrPos(0x105, 300, 100, 1100, 180)
    Jump("loc_4A14")

    label("loc_49CD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_49F3")
    SetChrPos(0x106, 200, 100, 1100, 180)
    Jump("loc_4A14")

    label("loc_49F3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4A14")
    SetChrPos(0x10A, 300, 100, 1100, 180)

    label("loc_4A14")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0x101, 0x2)
    Jump("loc_4B16")

    label("loc_4A31")

    SetChrPos(0x101, -800, 100, -1700, 180)
    SetChrPos(0x102, 1300, 100, -1900, 180)
    SetChrPos(0x103, 1300, 100, -400, 180)
    SetChrPos(0x104, -800, 100, -400, 180)
    ClearScenarioFlags(0x0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4A9C")
    SetChrPos(0x10A, -700, 100, 1100, 180)
    SetScenarioFlags(0x0, 0)

    label("loc_4A9C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4ADD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ACC")
    SetChrPos(0x105, -700, 100, 1100, 180)
    Jump("loc_4ADD")

    label("loc_4ACC")

    SetChrPos(0x105, 300, 100, 1100, 180)

    label("loc_4ADD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4AFE")
    SetChrPos(0x106, 200, 100, 1100, 180)

    label("loc_4AFE")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0x102, 0x2)

    label("loc_4B16")

    SetMapObjFrame(0xFF, "effect00_add", 0x0, 0x1)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    VolumeBGM(0x3C, 0x3E8)
    FadeToBright(1000, 0)
    SetCameraDistance(13800, 2000)
    OP_6F(0x79)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_58AA")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4C46")

    ChrTalk(
        0x106,
        (
            "#10702F#11PWow …. For the first time,\x01",
            "It's nice decor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00009FAhah, thanks\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00202FThis car, Ka aa too\x01",
            "It was a favorite.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C46")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D22")

    ChrTalk(
        0x10A,
        (
            "#00605F#11PHmm. The new ZCF car model\x02\x03",
            "#00603FIt certainly looks good for usability.\x01",
            "I'd like to think about the operation in section I ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00106FGiven the situation across the continent\x01",
            "Import from Libert also\x01",
            "It may be difficult …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D22")

    OP_63(0x109, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x109)

    ChrTalk(
        0x109,
        (
            "#10104F#5PYeah, the maintenance situation is good,\x01",
            "You can move it without problems.\x02\x03",
            "#10100FCertainly this girl also breakthrough\x01",
            "It seems to do it without difficulty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FReally……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FWith this the vehicle for inrush\x01",
            "I could secure it … ….\x02\x03",
            "#00200FOnce the section chiefs\x01",
            "Shall we return?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00103FWell, final set-up is also\x01",
            "I want to hear it … ….\x02",
        )
    )

    CloseMessageWindow()
    Sound(867, 0, 80, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x109, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00013FThis is…\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4F8A")

    ChrTalk(
        0x10A,
        (
            "#00601F#11PIt's a car-mounted communication device.\x01",
            "It is contact from somewhere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FC8")

    label("loc_4F8A")


    ChrTalk(
        0x104,
        (
            "#11P#00301FIt's a car-mounted communication device.\x01",
            "I heard it from anywhere.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FC8")


    ChrTalk(
        0x109,
        (
            "#10113F#5PB, Mr. Lloyd.\x01",
            "what should we do……?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FAh……\x01",
            "Try it on.\x02\x03",
            "#00001FEveryone, just to be sure\x01",
            "Ask not to make a voice.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    Sleep(500)
    Sound(853, 0, 100, 0)
    Sleep(300)
    Sound(899, 0, 50, 0)
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("Female voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "── Long time no see.\x01",
            "Everyone in the Special Affairs Support Division.\x02\x03",
            "Kirika.\x01",
            "Kirika Lawran.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)

    ChrTalk(
        0x101,
        "#12P#00011FHuh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#00307FKillika!?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5221")

    ChrTalk(
        0x106,
        "#10701F#11PTanade#4Rtight#\"Hayan Red Soup#8RElephant#\"… …)\x02",
    )

    CloseMessageWindow()

    label("loc_5221")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_527C")

    ChrTalk(
        0x10A,
        (
            "#00601F#11PLocksmith engine chief … …\x01",
            "Have you been in Crossbell yet?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52E7")

    label("loc_527C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_52E7")

    ChrTalk(
        0x105,
        (
            "#10403F#11PCalvert's intelligence agency\x01",
            "Are you a sister ……\x02\x03",
            "#10400FI said that he was still in the crossbell.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52E7")


    ChrTalk(
        0x109,
        (
            "#10101F#5PBut why\x01",
            "Communication to a place like this …! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00101F…… Our movement\x01",
            "Do you understand everything?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("Kirika's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In this situation you\x01",
            "I just predicted how it will work.\x02\x03",
            "During busy, let me take the time\x01",
            "I'm sorry but …\x02\x03",
            "\"Information exchange\"\x01",
            "I do not care.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#12P#00008FThat is…\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_54FB")

    ChrTalk(
        0x10A,
        (
            "#00603F#11P(…… Bannings.\x01",
            "You decide. )\x02\x03",
            "#00601F(Our One Division has a pipe with her\x01",
            "I can not build it yet. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00003F#11PUnderstood\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Jump("loc_5513")

    label("loc_54FB")

    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    label("loc_5513")


    ChrTalk(
        0x101,
        (
            "#12P#00006FUnderstood, Killika\x02\x03",
            "#00001FWhere should we meet you\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("Kirika's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Crossbell station, to the 3rd home\x01",
            "To the second car of the train being stopped.\x02\x03",
            "Popular with the station#4ROne person#Because there is nothing\x01",
            "You should rest assured.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#12P#00004FI understand.\x01",
            "Third home train\x01",
            "It is the second car.\x02\x03",
            "#00013Fby the way……\x01",
            "Lector is also on that?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("Kirika's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Huh, you saw it.\x01",
            "── Well then.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(899, 0, 80, 0)
    Sleep(500)

    ChrTalk(
        0x103,
        (
            "#12P#00211F……As usual\x01",
            "It is like a clairvoyant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00108FBesides Captain Lector,\x01",
            "It seems there are … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#00306FWell, we just have to go and see\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FAh……\x01",
            "Let's go to Crossbell station.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#5PRoger\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5804")

    ChrTalk(
        0x106,
        (
            "#10701F#11P… … for a moment's time\x01",
            "Let's prepare for it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58A5")

    label("loc_5804")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5857")

    ChrTalk(
        0x105,
        (
            "#10404F#11PJust to be sure, just preparation\x01",
            "It might be better to do it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58A5")

    label("loc_5857")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_58A5")

    ChrTalk(
        0x10A,
        (
            "#00603F#11PJust to be sure, just preparation\x01",
            "It is better to keep it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58A5")

    Jump("loc_65E9")

    label("loc_58AA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5952")

    ChrTalk(
        0x106,
        (
            "#10702F#11PWow …. For the first time,\x01",
            "It's nice decor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009F#5PAhah, thanks\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00202FThis car, Ka aa too\x01",
            "It was a favorite.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5952")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A5B")

    ChrTalk(
        0x10A,
        (
            "#11P#00605FHmm. The new ZCF car model\x02\x03",
            "#00603FIt certainly looks good for usability.\x01",
            "I'd like to think about the operation in section I ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00106FGiven the situation across the continent\x01",
            "Import from Libert also\x01",
            "It may be difficult …\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A5B")

    ChrTalk(
        0x105,
        "#10403FHmm, certainly.\x02",
    )

    CloseMessageWindow()

    label("loc_5A5B")

    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00004F#5P── The maintenance situation is good,\x01",
            "It seems to work without problems.\x02\x03",
            "#00000FWhen the actual rush\x01",
            "You had better drive by Noel\x01",
            "It looks good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#00302FWell, she's the pro\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FWith this the vehicle for inrush\x01",
            "I could secure it … ….\x02\x03",
            "#00200FOnce the section chiefs\x01",
            "Shall we return?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FWell, final set-up is also\x01",
            "I want to hear it … ….\x02",
        )
    )

    CloseMessageWindow()
    Sound(867, 0, 80, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x101, 0x1)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#5PThis is…\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5CD9")

    ChrTalk(
        0x10A,
        (
            "#11P#00601FIt's a car-mounted communication device.\x01",
            "It is contact from somewhere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D17")

    label("loc_5CD9")


    ChrTalk(
        0x104,
        (
            "#11P#00301FIt's a car-mounted communication device.\x01",
            "I heard it from anywhere.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D17")


    ChrTalk(
        0x102,
        "#12P#00108FLloyd, what do we do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PAh……\x01",
            "Let's turn it ON for the time being.\x02\x03",
            "#00013FEveryone, just to be sure\x01",
            "Ask not to make a voice.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    Sleep(500)
    Sound(853, 0, 100, 0)
    Sleep(300)
    Sound(899, 0, 50, 0)
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("Female voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "── Long time no see.\x01",
            "Everyone in the Special Affairs Support Division.\x02\x03",
            "Kirika.\x01",
            "Kirika Lawran.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)

    ChrTalk(
        0x101,
        "#00011F#5PHuh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#00307FKillika!?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5F66")

    ChrTalk(
        0x106,
        "#10701F#11PTanade#4Rtight#\"Hayan Red Soup#8RElephant#\"… …)\x02",
    )

    CloseMessageWindow()

    label("loc_5F66")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5FC1")

    ChrTalk(
        0x10A,
        (
            "#11P#00601FLocksmith engine chief … …\x01",
            "Have you been in Crossbell yet?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_602C")

    label("loc_5FC1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_602C")

    ChrTalk(
        0x105,
        (
            "#11P#10403FCalvert's intelligence agency\x01",
            "Are you a sister ……\x02\x03",
            "#10400FI said that he was still in the crossbell.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_602C")


    ChrTalk(
        0x102,
        (
            "#12P#00101F…… Our movement\x01",
            "Do you understand everything?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("Kirika's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In this situation you\x01",
            "I just predicted how it will work.\x02\x03",
            "During busy, let me take the time\x01",
            "I'm sorry but …\x02\x03",
            "\"Information exchange\"\x01",
            "I do not care.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00008F#5PThat is…\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6201")

    ChrTalk(
        0x10A,
        (
            "#11P#00603F(…… Bannings.\x01",
            "You decide. )\x02\x03",
            "#00601F(Our One Division has a pipe with her\x01",
            "I can not build it yet. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#5PUnderstood\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Jump("loc_6219")

    label("loc_6201")

    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    label("loc_6219")


    ChrTalk(
        0x101,
        (
            "#00006F#5PUnderstood, Killika\x02\x03",
            "#00001FWhere should we meet you\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("Kirika's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Crossbell station, to the 3rd home\x01",
            "To the second car of the train being stopped.\x02\x03",
            "Popular with the station#4ROne person#Because there is nothing\x01",
            "You should rest assured.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00004F#5PI understand.\x01",
            "Third home train\x01",
            "It is the second car.\x02\x03",
            "#00013Fby the way……\x01",
            "Lector is also on that?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("Kirika's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Huh, you saw it.\x01",
            "── Well then.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(899, 0, 80, 0)
    Sleep(500)

    ChrTalk(
        0x103,
        (
            "#12P#00211F……As usual\x01",
            "It is like a clairvoyant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00108FBesides Captain Lector,\x01",
            "It seems there are … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#00306FWell, we just have to go and see\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#5PAh……\x01",
            "Let's go to Crossbell station.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_64C6")

    ChrTalk(
        0x10A,
        "#11P#00603FOK.\x02",
    )

    CloseMessageWindow()
    Jump("loc_64F3")

    label("loc_64C6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_64F3")

    ChrTalk(
        0x105,
        "#11P#10404FHuh, I understand.\x02",
    )

    CloseMessageWindow()

    label("loc_64F3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6548")

    ChrTalk(
        0x106,
        (
            "#10701F#11P… … for a moment's time\x01",
            "Let's prepare for it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65E9")

    label("loc_6548")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_659B")

    ChrTalk(
        0x105,
        (
            "#10402F#11PJust to be sure, just preparation\x01",
            "It might be better to do it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65E9")

    label("loc_659B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_65E9")

    ChrTalk(
        0x10A,
        (
            "#00601F#11PJust to be sure, just preparation\x01",
            "It is better to keep it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65E9")

    FadeToDark(1000, 0, -1)
    SetCameraDistance(14300, 2000)
    OP_6F(0x79)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0xFF)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0xFF)
    SetChrSubChip(0xF5, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0xF4, 0x4)
    ClearChrFlags(0xF5, 0x4)
    SetChrFlags(0x101, 0x1)
    SetChrFlags(0x102, 0x1)
    SetChrFlags(0x103, 0x1)
    SetChrFlags(0x104, 0x1)
    SetChrFlags(0xF4, 0x1)
    SetChrFlags(0xF5, 0x1)
    OP_37()
    SetScenarioFlags(0x1A5, 5)
    OP_29(0xB1, 0x1, 0x8)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7573", 0)
    EventEnd(0x5)
    NewScene("c0200", 113, 0, 0)
    IdleLoop()
    Return()

    # Function_12_480E end

    def Function_13_668E(): pass

    label("Function_13_668E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Call(0, 15)
    BeginChrThread(0x101, 3, 0, 2)
    SoundLoad(468)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    Sound(468, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67E1")

    ChrTalk(
        0x103,
        "#00211FIt has been released …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FWell,\x01",
            "What has come to safety\x01",
            "I do not think so ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FWell …………)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWas it a mistake in judgment …?\x02\x03",
            "#00007F……, anyway I will keep chasing!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6919")

    label("loc_67E1")


    ChrTalk(
        0x103,
        (
            "#00205FAlthough the condition of the road is bad due to rain,\x01",
            "To curve at such speed ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FBut, a bit\x01",
            "Is not it dangerous …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102FHuh, this level\x01",
            "Before breakfast!\x02\x03",
            "#10107FRunaway car …\x01",
            "I will not escape absolutely!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        "#00012FI wonder what he is doing …\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00001F……, Anyway\x01",
            "I will keep on tracking!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_6919")

    Sound(494, 0, 70, 0)
    OP_68(101440, 650, -16510, 3000)
    MoveCamera(311, 29, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(11280, 3000)
    Sleep(1000)
    StopSound(468, 1000, 100)
    StopSound(494, 1000, 60)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearScenarioFlags(0x178, 5)
    SetScenarioFlags(0x22, 5)
    NewScene("r1010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_668E end

    def Function_14_6995(): pass

    label("Function_14_6995")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Call(0, 15)
    BeginChrThread(0x101, 3, 0, 2)
    SoundLoad(468)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    Sound(468, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x109,
        (
            "#10110FDamn\x01",
            "They also do quite well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FAh……\x02\x03",
            "#00000FHowever, as it is\x01",
            "With the wide area crime prevention section waiting at the west entrance\x01",
            "It seems to be able to get caught nicely.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(100)

    ChrTalk(
        0x105,
        (
            "#10305FHmm……?\x02\x03",
            "That car, what?\x01",
            "Is not it strange?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FHuh……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    StopSound(468, 500, 100)
    SetScenarioFlags(0x22, 6)
    NewScene("r1010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_6995 end

    def Function_15_6B1E(): pass

    label("Function_15_6B1E")

    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    OP_68(100490, 650, -450, 0)
    MoveCamera(311, 29, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13160, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x103, 0x4)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0x109, 0x1)
    ClearChrFlags(0x105, 0x1)
    ClearChrFlags(0x104, 0x1)
    ClearChrFlags(0x103, 0x1)
    SetChrPos(0x101, 99000, 100, 1600, 0)
    SetChrPos(0x102, 99000, 100, 40, 0)
    SetChrPos(0x109, 101100, 100, 1600, 0)
    SetChrPos(0x105, 101100, 100, 40, 0)
    SetChrPos(0x104, 99000, 100, -1420, 0)
    SetChrPos(0x103, 101100, 100, -1420, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Return()

    # Function_15_6B1E end

    def Function_16_6C57(): pass

    label("Function_16_6C57")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    SoundLoad(468)
    SoundLoad(469)
    OP_68(-500, 650, 500, 0)
    MoveCamera(324, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13750, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    EndChrThread(0x101, 0x0)
    SetChrBattleFlags(0x101, 0x4)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    EndChrThread(0x102, 0x0)
    SetChrBattleFlags(0x102, 0x4)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    EndChrThread(0x109, 0x0)
    SetChrBattleFlags(0x109, 0x4)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x0)
    EndChrThread(0x105, 0x0)
    SetChrBattleFlags(0x105, 0x4)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    EndChrThread(0x104, 0x0)
    SetChrBattleFlags(0x104, 0x4)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    EndChrThread(0x103, 0x0)
    SetChrBattleFlags(0x103, 0x4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x103, 0x4)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0x109, 0x1)
    ClearChrFlags(0x105, 0x1)
    ClearChrFlags(0x104, 0x1)
    ClearChrFlags(0x103, 0x1)
    SetChrPos(0x101, 1300, 100, -1900, 180)
    SetChrPos(0x102, -800, 100, -400, 180)
    SetChrPos(0x109, -800, 100, -1700, 180)
    SetChrPos(0x105, 1300, 100, -400, 180)
    SetChrPos(0x104, -800, 100, 1100, 180)
    SetChrPos(0x103, 1300, 100, 1100, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    Sound(468, 2, 100, 0)
    Sound(469, 2, 60, 0)
    BeginChrThread(0x101, 3, 0, 2)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00010FDamn, being held down with a grenade\x01",
            "It is hard to get close …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FIn the performance of the car, the car\x01",
            "I have not lost … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F…… as it is to the city of Altair in the Republic\x01",
            "It seems to be troublesome to enter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FIf that happens,\x01",
            "The arrest is almost impossible\x01",
            "Okay, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00310FRight …… Masu.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FAnyways……\x01",
            "I have no choice but to chase!\x02\x03",
            "#00007FNoel to ask!\x01",
            "Not to be shaken off\x01",
            "Keep on tight!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107FYes, sir!\x02",
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x105,
        "#10305F… …. Oh … ….?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopSound(468, 300, 90)
    StopSound(469, 300, 50)
    SetScenarioFlags(0x22, 3)
    NewScene("e4101", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_6C57 end

    SaveToFile()

Try(main)
