from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1000_1.bin",                # FileName
        "map1",                    # MapName
        "map1",                    # Location
        0x0010,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("c1000", "c1000_1", "c1000_2", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [88, 720921, 0, -16777216, 11796682, 28573696, 256, 16777216, 256, 0, 0, 256, -65280, 1660944639, 1936291423, 12336, 11831, 29801, 112, 202, 1, 0, 0],
    )

    BuildStringList((
        "c1000_1",                # 0
    ))

    ChipFrameInfo(88, 0)                                         # 0

    ScpFunction((
        "Function_0_58",           # 00, 0
    ))


    def Function_0_58(): pass

    label("Function_0_58")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis232.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis233.itp")
    SoundLoad(803)
    SoundLoad(2711)
    SoundLoad(2712)
    Sleep(500)
    Sound(803, 2, 100, 0)
    Sleep(1600)
    Sound(804, 0, 100, 0)
    OP_24(0x323)
    OP_25(0x80, 0x28)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sound(2084, 255, 100, 0)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00005FYes, Special Affairs Support Division,\x01",
            "It is Lloyd · Bannings.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of Franc")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2711V#30WMr. Lloyd ~!\x02\x03",
            "#2712V#30WIt is a hard work in the rain.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xA98)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00002FOh, Fran?\x02\x03",
            "#00000FWhat happened?\x01",
            "Did you also enter an emergency request?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of Franc")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Er, that is ……\x02\x03",
            "Mayex's Mayor of town\x01",
            "Do you remember?\x02",
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
            "#00005FOh, of course.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(1000)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(300)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00001FPossibly\x01",
            "Did something happen in the mining town?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of Franc")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yeah, that is to mine\x01",
            "It seems that a monster has appeared … …\x02\x03",
            "Oh, by the way,\x01",
            "It is a little away from the town\x01",
            "It seems to be the former mine.\x02",
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
            "#00005F……?\x02\x03",
            "#00001FEven if a monster appears at such a place\x01",
            "I do not think it's strange … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of Franc")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yes, the miners hurt\x01",
            "I heard that he did not come across.\x02\x03",
            "Just inside, something strange\x01",
            "It seems they are getting … ….\x02\x03",
            "Just to be sure you can check it\x01",
            "That was it.\x02",
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
            "#00003FFunny thing …\x01",
            "There is little point.\x02\x03",
            "#00000F─ ─ It turned out.\x01",
            "I cleared up the emergency request in the city,\x01",
            "I will head to Mainz from now.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of Franc")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yes, please.\x02\x03",
            "Oh, I will tell you\x01",
            "In the direction of Mainz train direction earlier\x01",
            "Designation of an arrangement magical beast came out.\x02\x03",
            "If there is room\x01",
            "Please try to correspond.\x02",
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
            "#00002FThat's right, OK.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of Franc")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Also, unlike Crossbell City\x01",
            "The mountain road seems to be sunny.\x02\x03",
            "Because it's so hard to drive with a car\x01",
            "Why do not you visit?\x02",
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
            "#00004FIs it so … I knew.\x02\x03",
            "#00000FThank you, Fran.\x01",
            "Please contact me again if there is something.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of Franc")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yes, I will excuse myself.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(813, 0, 60, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sound(804, 0, 100, 0)
    Sleep(800)
    SetMessageWindowPos(240, 110, -1, -1)

    AnonymousTalk(
        0x109,
        "#10105FI'd like to be from Franc.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 40, -1, -1)

    AnonymousTalk(
        0x102,
        (
            "#00101FDirections to Mainz\x01",
            "It looks like something happened?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006FOh, in the place called the former mine\x01",
            "It seems that strange things have happened.\x02\x03",
            "#00000FI have also cleared up the city's support request,\x01",
            "Let's go when you are ready.\x02\x03",
            "#00002FOh, it seems that the direction of the mountain road is sunny\x01",
            "It may be good to go by car.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(130, 30, -1, -1)

    AnonymousTalk(
        0x105,
        "#10304FOK, the leader.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 110, -1, -1)

    AnonymousTalk(
        0x109,
        (
            "#10100FIf you go to mining town by car\x01",
            "Let's go to the back door of the support department.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "To the terminal of the investigation notebook and support department\x01",
            "A new arrangement demon was added.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x6D, 0x4, 0x2)
    OP_29(0xA1, 0x1, 0x12)
    OP_CC(0x1, 0xFF, 0x0)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x128, 7)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_25(0x80, 0x64)
    OP_24(0x323)
    EventEnd(0x5)
    Return()

    # Function_0_58 end

    SaveToFile()

Try(main)
