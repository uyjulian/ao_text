from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t210d.bin",                # FileName
        "t210d",                    # MapName
        "t210d",                    # Location
        0x0059,                     # MapIndex
        "ed7151",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1C,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "t210d",                  # 0
        "Sonya Command",           # 1
        "Soldier Brood",           # 2
        "Soldier Dahlia",             # 3
        "tourist",                 # 4
    ))

    AddCharChip((
        "chr/ch12200.itc",                   # 00
        "chr/ch41400.itc",                   # 01
        "chr/ch41800.itc",                   # 02
        "chr/ch33000.itc",                   # 03
    ))

    DeclNpc(4294957296, 10000,   0,       270,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(4294953467, 10000,   4294964336, 270,  261,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(4294953236, 10000,   2900,    270,  261,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4294948696, 5000,    4294950126, 270,  389,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)

    DeclActor(1500,    5050,    4294947296, 1200,    1500,    6050,    4294947296, 0x007C, 0,  3,  0x0000)

    ChipFrameInfo(348, 0)                                        # 0

    ScpFunction((
        "Function_0_15C",          # 00, 0
        "Function_1_20C",          # 01, 1
        "Function_2_21B",          # 02, 2
        "Function_3_25C",          # 03, 3
        "Function_4_3AD",          # 04, 4
        "Function_5_593",          # 05, 5
        "Function_6_732",          # 06, 6
        "Function_7_862",          # 07, 7
        "Function_8_9C3",          # 08, 8
    ))


    def Function_0_15C(): pass

    label("Function_0_15C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_194"),
        (1, "loc_1A0"),
        (2, "loc_1AC"),
        (3, "loc_1B8"),
        (4, "loc_1C4"),
        (5, "loc_1D0"),
        (6, "loc_1DC"),
        (SWITCH_DEFAULT, "loc_1E8"),
    )


    label("loc_194")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1A0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1AC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1B8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1C4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1D0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1DC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1E8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1F4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_20B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_20B")

    Return()

    # Function_0_15C end

    def Function_1_20C(): pass

    label("Function_1_20C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_21A")
    ClearChrFlags(0xB, 0x80)

    label("loc_21A")

    Return()

    # Function_1_20C end

    def Function_2_21B(): pass

    label("Function_2_21B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_22D")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x236), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_22D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_244")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    Jump("loc_244")

    label("loc_244")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_257")
    OP_70(0x2, 0x0)
    Jump("loc_25B")

    label("loc_257")

    OP_70(0x2, 0x1E)

    label("loc_25B")

    Return()

    # Function_2_21B end

    def Function_3_25C(): pass

    label("Function_3_25C")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35C")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('回复药', 1)"), scpexpr(EXPR_END)), "loc_2E5")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1ED, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_357")

    label("loc_2E5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_357")

    Jump("loc_3A1")

    label("loc_35C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In the treasure box何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_3A1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_25C end

    def Function_4_3AD(): pass

    label("Function_4_3AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BB")
    Call(0, 8)
    Return()

    label("loc_3BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_509")

    ChrTalk(
        0x8,
        (
            "#10600FRegarding the future response,\x01",
            "Douglas deputy commander to McDowell\x01",
            "I'm going to consult him.\x02\x03",
            "As a commander of the regular army,\x01",
            "Alert attitude to the empire / republic\x01",
            "We must keep it in perfect condition.\x02\x03",
            "#10603FAfter all is over, what to do\x01",
            "I do not know yet …\x02\x03",
            "#10600FAnyway, now as a commander\x01",
            "I will do as much as I can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_58F")

    label("loc_509")


    ChrTalk(
        0x8,
        (
            "#10603FAfter all is over, what to do\x01",
            "I do not know yet …\x02\x03",
            "#10600FAnyway, now as a commander\x01",
            "I will do as much as I can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58F")

    TalkEnd(0xFE)
    Return()

    # Function_4_3AD end

    def Function_5_593(): pass

    label("Function_5_593")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_694")

    ChrTalk(
        0x9,
        (
            "In any empire, during the civil war\x01",
            "Things like 'flying warships'\x01",
            "It seems that it is being developed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Such an imperial army\x01",
            "Once you join the Armored Division,\x01",
            "Honestly I can not put my hands …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If that \"god machine\" is there … …\x01",
            "That's what I think\x01",
            "I wonder if only ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_72E")

    label("loc_694")


    ChrTalk(
        0x9,
        (
            "\"Flying warship\" something\x01",
            "Once you join the Armored Division,\x01",
            "Imperial troops will not be able to touch their hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If that \"god machine\" is there … …\x01",
            "That's what I think\x01",
            "I wonder if only ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72E")

    TalkEnd(0xFE)
    Return()

    # Function_5_593 end

    def Function_6_732(): pass

    label("Function_6_732")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D6")

    ChrTalk(
        0xA,
        (
            "I thought that the \"god machine\" was lost\x01",
            "I think that it was good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Weapons with such power,\x01",
            "What we can deal with\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_85E")

    label("loc_7D6")


    ChrTalk(
        0xA,
        (
            "\"God machine\" … … Such a thing,\x01",
            "I do not think we were beaten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "…… Looking at the existence of the galleria fortress,\x01",
            "Even now my spine froze.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85E")

    TalkEnd(0xFE)
    Return()

    # Function_6_732 end

    def Function_7_862(): pass

    label("Function_7_862")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93F")

    ChrTalk(
        0xB,
        (
            "I thought that I managed to return to the empire\x01",
            "I came to the Belgard gate … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, no way, \"Galleria Fortress\"\x01",
            "What is it supposed to be like that …?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Here, whatever happens\x01",
            "It is impossible to return home ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_9BF")

    label("loc_93F")


    ChrTalk(
        0xB,
        (
            "Well, no way, \"Galleria Fortress\"\x01",
            "What is it supposed to be like that …?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Here, whatever happens\x01",
            "It is impossible to return home ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9BF")

    TalkEnd(0xFE)
    Return()

    # Function_7_862 end

    def Function_8_9C3(): pass

    label("Function_8_9C3")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x236), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-6780, 12170, -1160, 0)
    MoveCamera(303, 28, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(12280, 0)
    SetChrPos(0x101, -8000, 10000, 500, 270)
    SetChrPos(0x102, -7900, 10000, -500, 270)
    SetChrPos(0x103, -7000, 10000, 1400, 270)
    SetChrPos(0x104, -6800, 10000, -1500, 270)
    SetChrPos(0xF4, -6000, 10000, 500, 270)
    SetChrPos(0xF5, -5800, 10000, -500, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#00002FSonya Command……\x01",
            "I was in such a place.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        "#10605F#5Pyou……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-68290, 12670, -3030, 0)
    MoveCamera(239, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(127990, 0)
    OP_0D()
    MoveCamera(303, 17, 0, 40000)
    Sleep(1000)
    SetMessageWindowPos(14, 280, -1, 3)

    AnonymousTalk(
        0x104,
        (
            "#00301F…… Sorry it's a questionable thing.\x02\x03",
            "#00303FThat white doll carries a train cannon\x01",
            "It was without a trace and it disappeared\x01",
            "I was watching with the video … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00008F…… Indirectly,\x01",
            "By the power of Kia a this\x01",
            "It has become … …\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    AnonymousTalk(
        0x8,
        (
            "#10603F…… This is from the empire side\x01",
            "Indefinite incoming\x01",
            "It's information … ….\x02\x03",
            "#10600FIn that \"god machine\" attack,\x01",
            "Human damage to the Imperial army\x01",
            "I heard there was not much.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    AnonymousTalk(
        0x101,
        "#12P#00005FIs it true? Is it?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#12P#00105FOh, that situation is only a miracle\x01",
            "There is not anything to say but ……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    AnonymousTalk(
        0x8,
        (
            "#10600FBecause I can not confirm the fact\x01",
            "I do not know the actual place, but …\x02\x03",
            "#10604FWithout involving humans\x01",
            "It says to erase only inorganic matter\x01",
            "It might be power.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    AnonymousTalk(
        0x103,
        (
            "#12P#00202FIf that is true,\x01",
            "Kea unconsciously \"miracle\"\x01",
            "It may have interfered.\x02\x03",
            "#00204FThe reason why the empire suffered great damage\x01",
            "There is no mistake … …\x01",
            "I was a little relieved.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(-6780, 12170, -1160, 0)
    MoveCamera(303, 28, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(12280, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#10604F#5P…… You guys, I heard the story.\x02\x03",
            "#10602FCrossbell City 's release strategy,\x01",
            "It seems that it worked well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00309FHaha, I can not be honest, though.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FC8")

    ChrTalk(
        0x109,
        (
            "#12P#10104FSonya Commandのおかげです！\x02\x03",
            "#10102FBecause of that advice,\x01",
            "The way of independent ineffective declaration\x01",
            "I was able to find out!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10FB")

    label("loc_FC8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1065")

    ChrTalk(
        0x105,
        (
            "#12P#10400FHuh, it was also thanks to the commander.\x02\x03",
            "#10404FBecause of that advice,\x01",
            "The way of independent ineffective declaration\x01",
            "I could find it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10FB")

    label("loc_1065")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10FB")

    ChrTalk(
        0x106,
        (
            "#12P#10704FI think thanks to you.\x02\x03",
            "#10702FBecause of that advice,\x01",
            "The way of independent ineffective declaration\x01",
            "It was possible to find out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10FB")


    ChrTalk(
        0x8,
        (
            "#10602F#5PHehe, I have not done anything.\x01",
            "All that you did …\x02\x03",
            "#10603F…… Speaking of what I did,\x01",
            "As preserved by the president's policy\x01",
            "Just saying that we operated a defense army.\x02\x03",
            "#10608FNow that the legitimacy of an independent country is frustrated,\x01",
            "As a commander in the person I am\x01",
            "It may not be qualified.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(10)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(10)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(10)
    OP_63(0x5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00011FWell, that is ….\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12EC")

    ChrTalk(
        0x10A,
        (
            "#12P#00606F…… What you imagine so far\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_138F")

    label("loc_12EC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1341")

    ChrTalk(
        0x105,
        (
            "#12P#10406F…… Thinking to that extent\x01",
            "Is not it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_138F")

    label("loc_1341")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_138F")

    ChrTalk(
        0x109,
        (
            "#12P#10113FThat's why\x01",
            "Is not it …?! Is it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_138F")


    ChrTalk(
        0x8,
        (
            "#10602F#5PHehu, of course what I have to do now\x01",
            "I'm going for it.\x02\x03",
            "#10604FAfter all is over, what to do\x01",
            "I do not know yet …\x02\x03",
            "#10600FAnyway, now as a commander\x01",
            "I will do as much as I can.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0x8, 0xFF)
    OP_93(0x8, 0x10E, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1AC, 0)
    EventEnd(0x5)
    Return()

    # Function_8_9C3 end

    SaveToFile()

Try(main)
