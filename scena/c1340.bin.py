from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1340.bin",                # FileName
        "c1340",                    # MapName
        "c1340",                    # Location
        0x001D,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 53000, 0, 20000, 0, 0, 1, 29, 0, 0, 0, 2],
    )

    BuildStringList((
        "c1340",                  # 0
        "Marybele",             # 1
    ))

    AddCharChip((
        "chr/ch05502.itc",                   # 00
    ))

    DeclNpc(55029,   180,     128820,  180,  389,  0x0, 0,   0,   0,   255, 255, 0,   5,   255,  0)

    DeclActor(47960,   0,       123700,  1200,    47960,   800,     123700,  0x007C, 0,  3,  0x0000)
    DeclActor(53000,   0,       45600,   1200,    53000,   800,     45600,   0x007C, 0,  6,  0x0000)
    DeclActor(55000,   150,     128800,  2500,    55000,   1800,    128800,  0x007E, 0,  4,  0x0000)

    ChipFrameInfo(324, 0)                                        # 0

    ScpFunction((
        "Function_0_144",          # 00, 0
        "Function_1_19E",          # 01, 1
        "Function_2_1A5",          # 02, 2
        "Function_3_1C2",          # 03, 3
        "Function_4_26C",          # 04, 4
        "Function_5_270",          # 05, 5
        "Function_6_3DF",          # 06, 6
        "Function_7_1D53",         # 07, 7
        "Function_8_2AF8",         # 08, 8
    ))


    def Function_0_144(): pass

    label("Function_0_144")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15C")
    ClearScenarioFlags(0x25, 1)
    Call(0, 1)

    label("loc_15C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18E")
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)

    label("loc_18E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_19D")
    ClearScenarioFlags(0x22, 1)
    Event(0, 7)

    label("loc_19D")

    Return()

    # Function_0_144 end

    def Function_1_19E(): pass

    label("Function_1_19E")

    Sound(160, 0, 100, 0)
    Return()

    # Function_1_19E end

    def Function_2_1A5(): pass

    label("Function_2_1A5")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C1")
    ClearMapObjFlags(0x2, 0x10)
    OP_66(0x1, 0x1)

    label("loc_1C1")

    Return()

    # Function_2_1A5 end

    def Function_3_1C2(): pass

    label("Function_3_1C2")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a car magazine \"Monthly Carmania vol.2\".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('狂野色彩', 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_268")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "Paint pattern\x01\x07\x02",
            "\"Wild color\"\x07\x00",
            "I learned.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber('狂野色彩', 1)

    label("loc_268")

    TalkEnd(0xFF)
    Return()

    # Function_3_1C2 end

    def Function_4_26C(): pass

    label("Function_4_26C")

    Call(0, 5)
    Return()

    # Function_4_26C end

    def Function_5_270(): pass

    label("Function_5_270")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34E")

    ChrTalk(
        0x8,
        (
            "#02901FStolen by hatred Kaitou B\x01",
            "There are five Rosenberg dolls.\x02\x03",
            "#02903FMy precious girls\x01",
            "How to fix it ……\x01",
            "It is a matter of fact that I can not forgive at all.\x02\x03",
            "#02900FEveryone, please\x01",
            "I asked for your best regards.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3DB")

    label("loc_34E")


    ChrTalk(
        0x8,
        (
            "#02903FMy precious girls\x01",
            "How to fix it ……\x01",
            "It is a matter of fact that I can not forgive at all.\x02\x03",
            "#02901FEveryone, please\x01",
            "I asked for your best regards.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DB")

    TalkEnd(0x8)
    Return()

    # Function_5_270 end

    def Function_6_3DF(): pass

    label("Function_6_3DF")

    EventBegin(0x0)
    Fade(1000)
    OP_68(53250, 1500, 45110, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18430, 0)
    SetChrPos(0x102, 52950, 0, 44240, 0)
    SetChrPos(0x101, 52220, 0, 43070, 0)
    SetChrPos(0x104, 53710, 0, 43070, 0)
    SetChrPos(0x109, 51640, 0, 42010, 0)
    SetChrPos(0x103, 52930, 0, 42010, 0)
    SetChrPos(0x105, 54450, 0, 42010, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    OP_9B(0x0, 0x102, 0x0, 0x3E8, 0x5DC, 0x0)
    Sound(808, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x102,
        "#12P#00100F─ ─ Bell, me.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 50, -1, -1)
    SetChrName("Marybeleのvoice")

    AnonymousTalk(
        0xFF,
        "Well, come in.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x102,
        "#12P#00100FIt will be rude.\x02",
    )

    CloseMessageWindow()
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x2)
    Sleep(300)

    def lambda_54B():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_54B)
    Sleep(100)

    def lambda_568():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_568)

    def lambda_582():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_582)

    def lambda_59C():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_59C)

    def lambda_5B6():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5B6)

    def lambda_5D0():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5D0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    OP_68(54290, 1230, 126800, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17010, 0)
    SetChrPos(0x101, 54960, 30, 125480, 0)
    SetChrPos(0x102, 53750, 30, 125480, 0)
    SetChrPos(0x104, 56190, 30, 125480, 0)
    SetChrPos(0x109, 54960, 30, 124330, 0)
    SetChrPos(0x103, 53750, 30, 124330, 0)
    SetChrPos(0x105, 56190, 30, 124330, 0)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis348.itp")
    SetMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0x0, 0x0, 0x0)
    OP_65(0x1, 0x1)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x105, 0x0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x102,
        "#12P#00102FHehe, for the first time in a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02904FErie …\x01",
            "Also, everyone at the Special Affairs Division\x01",
            "It's been a long time.\x02\x03",
            "#02900FTio also last night\x01",
            "It seems that you returned,\x01",
            "Were there any changes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00200FYes, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02909FUhufu, that was nice.\x02\x03",
            "#02900FToday is the day of the plenary session\x01",
            "I think that I am variously busy,\x01",
            "Everyone please do your best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10109FHuh, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300Fそういえば、Marybeleさんは\x01",
            "Today for the tower\x01",
            "Do not you face it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02900FYes, to me\x01",
            "On behalf of your father\x01",
            "I also have bank work … …\x02\x03",
            "The division of the trade meeting is to your father\x01",
            "I will leave it all.\x02\x03",
            "#02906FAnd … Apologize to everyone\x01",
            "You must leave it.\x02\x03",
            "I am busy. In this kind of thing\x01",
            "I suddenly called you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FNo, such a thing ……\x01",
            "I am indebted\x01",
            "Marybeleさんの依頼ですし。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FAnything, antique doll\x01",
            "It was a stolen thing … …\x02\x03",
            "#00301FCan you tell me a detailed story?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02903F… … I understand.\x02\x03",
            "#02900FI made of Rosenberg\x01",
            "What I love to love dolls,\x01",
            "I guess everyone knows … …\x02\x03",
            "#02900FIn the private room in the IBC,\x01",
            "Especially 5 favorite dolls\x01",
            "I kept it.\x02\x03",
            "#02903FHowever, last night, in the space where I left my room by myself\x01",
            "Somebody invaded and all of them\x01",
            "I stole it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00205FMade by Rosenberg\x01",
            "Five antique dolls ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FWell, that's it.\x01",
            "You should have been quite expensive.\x02\x03",
            "#10106FWhen it becomes big\x01",
            "Millions of millions do not go down ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02903FThe amount is not a big problem.\x02\x03",
            "More than anything, in a place to be\x01",
            "Lost feeling that no one's important … …\x02\x03",
            "#02910FAhh, with this hand a damned pirate\x01",
            "I want to break it up! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006FPlease calm down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105FBell's private room ……\x01",
            "It's about the next room here, is not it?\x02\x03",
            "#00103FIBC security\x01",
            "To scratch and break into invading,\x01",
            "How in the world?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02903F…… Kohon.\x01",
            "Yes, I also wonder\x01",
            "I thought … ….\x02\x03",
            "#02901FLooking at the items left at the site,\x01",
            "The point of intersection went soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00205FResidents ……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02901FAbout that\x01",
            "It would be faster to have it seen.\x01",
            "…… This is it.\x02",
        )
    )

    CloseMessageWindow()
    Sound(18, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_123C")

    AnonymousTalk(
        0x101,
        "#00011FTh-This is……!\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x102,
        "#00105FThe crime card of \"Kaitou B\" …! Is it?\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x8,
        (
            "#02901FNumerous artworks from all over the continent\x01",
            "Make it a phantom of stealing a deadly devil\x01",
            "A riddle thief - calling a man \"Kaitou B\".\x02\x03",
            "#02903FManipulate many mysterious magic\x01",
            "It is said that they steal victims vividly,\x01",
            "Cards are always left in the crime scene … …\x02\x03",
            "#02901FPerhaps he would also infiltrate the IBC\x01",
            "It was a fun thing.\x02\x03",
            "#02902FAlso, you guys\x01",
            "You seem to have dealt with it, do not you think?\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x109,
        "#10105FWell, was that so! Is it?\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x103,
        (
            "#00200FSurely it was in the present municipal hall\x01",
            "The statue was stolen, did not he?\x02\x03",
            "#00203FAfter all I could not arrest him … …\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x104,
        (
            "#00310FWell, again on the crossbell\x01",
            "It seems that it has appeared.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x105,
        (
            "#10304FHuh, you guys also happened to various incidents\x01",
            "You seem to be caught up.\x02\x03",
            "#10305FSo … what on the card\x01",
            "Were you written?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14FF")

    label("loc_123C")


    AnonymousTalk(
        0x101,
        "#00011Fthis is……!\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x102,
        (
            "#00101FDid you mean ……\x01",
            "The crime card of \"Kaitou B\" …! Is it?\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x109,
        (
            "#10105FKaitou B … …?\x01",
            "You seem to have heard it somewhere.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x8,
        (
            "#02900FEli and Mr. Lloyd\x01",
            "You seem to know.\x02\x03",
            "#02901FNumerous artworks from all over the continent\x01",
            "Make it a phantom of stealing a deadly devil\x01",
            "A riddle thief - calling a man \"Kaitou B\".\x02\x03",
            "#02903FManipulate many mysterious magic\x01",
            "It is said that they steal victims vividly,\x01",
            "Cards are always left in the crime scene … …\x02\x03",
            "#02901FIn the empire that is the center of activity\x01",
            "There is no one who does not know his name.\x02\x03",
            "#02906FPerhaps he would also infiltrate the IBC\x01",
            "It was a fun thing.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x103,
        (
            "#00200FI am as well as a name\x01",
            "I heard that before.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x104,
        (
            "#00301FChi, That's the crossbell.\x01",
            "It seems that it has appeared.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x105,
        (
            "#10305FSo …\x01",
            "カードには何てWere you written?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14FF")


    AnonymousTalk(
        0x8,
        "#02903F…… The content is this.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Young people from the Special Affairs Division.\x01",
            "Daughter's love affair and five girls\x01",
            "It is in my hand.\x02\x03",
            "If they want their freedom\x01",
            "Trapped and five cages\x01",
            "Leave it open with the key of truth.\x02\x03",
            "The first cage is in the market.\x01",
            "\"The commander of the clown\x01",
            "Look for a seat chair \".\x01",
            "── Kaito B\x07\x00\x02",
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
        0x8,
        (
            "#5P#02901F… … You got it understood?\x01",
            "I want you guys\x01",
            "The biggest reason for calling me is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FKaito B is our company support department\x01",
            "I am hitting the challenge … …\x02\x03",
            "In other words, is that something like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10306Ffor that reason\x01",
            "Take five bombs\x01",
            "Is that why you steal?\x02\x03",
            "#10302FHuff, a considerable odd person\x01",
            "It looks like no mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301Fanyway……\x01",
            "The reality is damaging,\x01",
            "It would be impossible to overlook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FWell … what was stolen\x01",
            "I take care of the bell.\x01",
            "It's a Rosenberg doll.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02902FHuhu, thank you Ellie.\x01",
            "Thank you for your consideration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FWell then, before starting the survey\x01",
            "About the text of the card again\x01",
            "Let's verify.\x02\x03",
            "#00003FFirst of all, the word \"five girls\" …\x02\x03",
            "This is about five stolen dolls\x01",
            "I think that it points.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FAnd \"five cages\" …\x02\x03",
            "#00200FPerhaps, those dolls\x01",
            "It is hidden in total of 5 places\x01",
            "I guess they are showing up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FThat means,\x01",
            "I have to find 5 places in total\x01",
            "Is that it?\x02\x03",
            "#10106FIt seems tough, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FAnd, perhaps important\x01",
            "『市中』と\"The commander of the clown\x01",
            "Sitting chair \".\x02\x03",
            "#10304FProbably not a cache\x01",
            "It might be a hint … ….\x01",
            "Hmm, is it the analogy of something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F\"Frown hands\" …\x01",
            "Recently, something like that\x01",
            "I feel like heard it … …\x02\x03",
            "#00300FAnyhow, even if I am worried it does not start.\x01",
            "Let's start surveying quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02904FUhufu, I'm expecting you,\x01",
            "Everyone in the Special Affairs Division.\x02\x03",
            "#02900FMy precious girls,\x01",
            "Please please regain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYes, please leave it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00104FFor the contents of the card for the moment\x01",
            "I kept a note in the investigation notebook.\x02\x03",
            "#00100FLet's begin the investigation with this as a clue.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest 【Searching for missing collections】\x07\x00",
            "I started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 54990, 30, 124960, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_29(0x7A, 0x1, 0x1)
    SetScenarioFlags(0x1C6, 3)
    EventEnd(0x5)
    Return()

    # Function_6_3DF end

    def Function_7_1D53(): pass

    label("Function_7_1D53")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(54970, 1230, 123580, 0)
    MoveCamera(46, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17010, 0)
    SetChrPos(0x101, 54960, 30, 123480, 0)
    SetChrPos(0x102, 53750, 30, 123480, 0)
    SetChrPos(0x104, 56190, 30, 123480, 0)
    SetChrPos(0x109, 54960, 30, 122330, 0)
    SetChrPos(0x103, 53750, 30, 122330, 0)
    SetChrPos(0x105, 56190, 30, 122330, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    LoadChrToIndex("chr/ch05500.itc", 0x1E)
    SetChrChipByIndex(0x8, 0x1E)
    ClearChrBattleFlags(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 54960, 30, 125480, 180)
    Sleep(1500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#02903F──Well, I understand the situation in general.\x02\x03",
            "#02901FKaitou B is the \"one company\" of \"association\"\x01",
            "Surely I was surprised … …\x02\x03",
            "#02906FIf that is the case it can not be helped.\x02\x03",
            "#02910FWhen I caught it, I was living\x01",
            "Punish enough to regret it\x01",
            "I was planning to give it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#00306F(Oh, I say horrible things … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FWell, sorry,\x01",
            "We were also in the place I wanted to arrest … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FFor now, collected dolls\x01",
            "I will get it back to the bell.\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x1, 0x101, 0x0, 0x3E8, 0x7D0, 0x0)
    Sleep(500)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "5 train of Rosenberg dolls\x01",
            "Marybeleに渡した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_9B(0x1, 0x101, 0xB4, 0x3E8, 0x7D0, 0x0)

    ChrTalk(
        0x8,
        (
            "#02909FUhufu, go home.\x01",
            "Alice, Canaan, Liete,\x01",
            "Mister, Sharon …\x02\x03",
            "#02904F… Well good.\x01",
            "I will not complain at this time.\x02\x03",
            "#02900FThus my cute\x01",
            "Rosenberg dolls\x01",
            "It is that it came back intact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FWell, that point is Kaitou B\x01",
            "It seems they were thorough.\x02\x03",
            "#10300FIn such a sturdy trunk,\x01",
            "In places like to lazy\x01",
            "I did not put it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105FOh, that 's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00206FWell, if you do not have to steal it in the first place\x01",
            "It is only a good story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00009FHaha, that is true.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02903FAnyway, in the future\x01",
            "To avoid this kind of thing\x01",
            "I will strengthen security thoroughly.\x02\x03",
            "#02900FMore than ever in the security department\x01",
            "I have to work firmly.\x02\x03",
            "#02909FHuh, you guys really\x01",
            "I am indebted to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00109FHehe, do not mind bell.\x01",
            "When troubled, they are mutually like.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2897")
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#12P#00005F(Yes, certainly the last time … …)\x02",
    )

    CloseMessageWindow()
    OP_95(0x101, 54960, 30, 124080, 2000, 0x0)

    ChrTalk(
        0x101,
        "#12P#00001F(Seriously ……)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105FMr. Lloyd, Mr. Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02905F… … What are you going for?\x01",
            "Suddenly with delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FNo.\x02\x03",
            "#00001FWhen I solved the incident before\x01",
            "Kaito B disguised as a client's figure\x01",
            "Because there was something that appeared … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FOh, I see.\x01",
            "I also had such a thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00205FNo, but this time ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F…… That, I will ask you straight away.\x02\x03",
            "#00001Fあなたは、Marybeleさんですよね──\x02",
        )
    )

    CloseMessageWindow()
    Sound(802, 0, 100, 0)

    def lambda_263C():
        OP_99(0xFE, 0x101, 0x258, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_263C)
    WaitChrThread(0x8, 1)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x4)
    OP_52(0x101, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2669():
        OP_A6(0xFE, 0x32, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2669)

    def lambda_2682():
        OP_98(0xFE, 0x0, 0xC8, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2682)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)

    ChrTalk(
        0x101,
        "#12P#00011FHuh …! Is it?\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#02902FUhufu, Lloyd san.\x02\x03",
            "#02909FPeople are obedient and honest\x01",
            "Even though I appreciate it,\x01",
            "Is not it rude indeed?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#12P#00011FWell, sorry ……\x02\x03",
            "#00006F(Yes, this is definitely\x01",
            "  Marybeleさん、だ……ガクッ。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00106FAlready, Lloyd's ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10309FWhew, it will not be closed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_29DE")

    label("loc_2897")


    ChrTalk(
        0x101,
        (
            "#12P#00000FWell then, we\x01",
            "I will be sorry about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02909FHuhu, today is really\x01",
            "Thank you very much.\x02\x03",
            "#02900FYou too,\x01",
            "As security at today's trade meeting\x01",
            "I hear you are going to join.\x02\x03",
            "#02904FAt best, at the same time sharing your father\x01",
            "Please help me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FWell, please leave it to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100FWell then, bell.\x02",
    )

    CloseMessageWindow()

    label("loc_29DE")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_29F5")
    Call(0, 8)

    label("loc_29F5")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "After that, Lloyd's\x01",
            "It was issued at the reception of 1F\x01",
            "I returned an IBC certification card.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest 【Searching for missing collections】\x07\x00",
            "Achieved!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x7A, 0x1, 0x6)
    OP_29(0x7A, 0x1, 0x7)
    OP_29(0x7A, 0x4, 0x10)
    SubItemNumber('ＩＢＣ认证卡片', 1)
    SubItemNumber('罗赞贝尔克人偶·Ｃ', 1)
    SubItemNumber('罗赞贝尔克人偶·Ｒ', 1)
    SubItemNumber('罗赞贝尔克人偶·Ｍ', 1)
    SubItemNumber('罗赞贝尔克人偶·Ｓ', 1)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x22, 1)
    NewScene("c1310", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_1D53 end

    def Function_8_2AF8(): pass

    label("Function_8_2AF8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(803)
    OP_68(54590, 1500, 13640, 0)
    MoveCamera(55, 28, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20420, 0)
    SetChrPos(0x101, 53930, 0, 14020, 90)
    SetChrPos(0x102, 53440, 0, 15190, 90)
    SetChrPos(0x104, 53440, 0, 12670, 90)
    SetChrPos(0x109, 52520, 0, 13810, 90)
    SetChrPos(0x103, 52020, 0, 15160, 90)
    SetChrPos(0x105, 52020, 0, 12580, 90)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(107, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0xA, 0x1, 0x8)
    Sleep(1000)

    def lambda_2BC3():
        OP_95(0xFE, 56930, 0, 14020, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2BC3)

    def lambda_2BDD():
        OP_95(0xFE, 56440, 0, 15190, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2BDD)

    def lambda_2BF7():
        OP_95(0xFE, 56440, 0, 12670, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2BF7)

    def lambda_2C11():
        OP_95(0xFE, 55520, 0, 13810, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2C11)

    def lambda_2C2B():
        OP_95(0xFE, 55020, 0, 15160, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2C2B)

    def lambda_2C45():
        OP_95(0xFE, 55020, 0, 12580, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2C45)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x105, 0x1)
    LoadChrToIndex("apl/ch51274.itc", 0x1F)
    CreatePortrait(1, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(55700, 1400, 130699, 0)
    MoveCamera(44, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16250, 0)
    SetChrPos(0x8, 56030, 0, 130930, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(250)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x1)
    Sound(802, 0, 100, 0)
    Sleep(500)
    Sound(804, 0, 100, 0)
    OP_24(0x323)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x1, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#02904FHello.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7580", 0)
    Sleep(500)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──やあ、麗しのMarybele嬢。\x01",
            "How is your hospitality?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#02912FIt is a place I told you.\x02\x03",
            "#02913FAs with your \"entertainment\"\x01",
            "I could enjoy it enough.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Huh, that was nice.\x02\x03",
            "An important collection\x01",
            "I appreciate it for letting me.\x02\x03",
            "Although I am acquainted with Meister,\x01",
            "Only that number of works\x01",
            "I do not have the opportunity to see it all at once.\x02\x03",
            "Exactly the most beautiful ─\x01",
            "I will reward you again.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#02909FUfufu …. treat it politely\x01",
            "It seems that you can do it,\x01",
            "That point was relieved.\x02\x03",
            "#02911FIf even one of the scratches is attached,\x01",
            "That was my \"castle\"\x01",
            "It was a place to invite me.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ha ha ha …\x01",
            "Was it a pity with that?\x02\x03",
            "Well, I collected it quickly\x01",
            "I would like to thank the members of the support department.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#02913FGiggle\x01",
            "So you are going to\x01",
            "What are you going to do?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh, the crossbell\x01",
            "I will leave right away.\x02\x03",
            "To the fact that the Empire direction is interesting\x01",
            "It seems to be getting.\x01",
            "I am going to go there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#02912FI see.\x01",
            "Good day thank you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Regarding \"plan\" there,\x01",
            "I am watching from the empire too\x01",
            "Let's get it.\x02\x03",
            "Huff, in \"association\"\x01",
            "Also about your future.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#02902FUhufu …. What should I do?\x01",
            "I have not decided.\x02\x03",
            "#02913FWell then, within close range\x01",
            "Let's meet - ─\x02",
            "#02911F\"Kaito gentleman\".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Kaito Bull Blanc")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Haha, that time\x01",
            "I will look forward to it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Return()

    # Function_8_2AF8 end

    SaveToFile()

Try(main)
