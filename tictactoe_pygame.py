import pygame
pygame.init()

win = pygame.display.set_mode((660, 660))
pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()
button_notpressed = (245, 245, 50)
button_pressed = (200, 200, 50)


def mainmenu():
    run = True
    while run:
        clock.tick(30)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 225 <= mouse[0] <= 435 and 358 <= mouse[1] <= 418:
                    if event.button == 1:
                        gameboard = [0, " ", " ", " ", " ", " ", " ", " ", " ", " "]
                        startgame(gameboard, "X")
                        run = False
                if 225 <= mouse[0] <= 435 and 448 <= mouse[1] <= 508:
                    if event.button == 1:
                        about()
                if 225 <= mouse[0] <= 435 and 538 <= mouse[1] <= 598:
                    if event.button == 1:
                        run = False
        if run:
            drawmainmenu()
            pygame.display.update()


def drawmainmenu():
    mouse = pygame.mouse.get_pos()
    win.fill((175, 175, 175))

    pygame.draw.rect(win, (0, 0, 0), (310, 237, 5, 100))
    pygame.draw.rect(win, (0, 0, 0), (345, 237, 5, 100))
    pygame.draw.rect(win, (0, 0, 0), (280, 267, 100, 5))
    pygame.draw.rect(win, (0, 0, 0), (280, 302, 100, 5))

    titlefont = pygame.font.Font("Chunkfive.otf", 100)
    title = titlefont.render("Tic-Tac-Toe", 1, (0, 0, 0))
    win.blit(title, ((660 / 2) - (title.get_rect().width / 2), 75))

    subtitlefont = pygame.font.Font("Chunkfive.otf", 30)
    subtitle = subtitlefont.render("by Sawyer Scott Stahl", 1, (0, 0, 0))
    win.blit(subtitle, ((660 / 2) - (subtitle.get_rect().width / 2), 185))

    buttonfont = pygame.font.Font("Chunkfive.otf", 40)
    starttext = buttonfont.render("Start", 1, (0, 0, 0))
    abouttext = buttonfont.render("About", 1, (0, 0, 0))
    quittext = buttonfont.render("Quit", 1, (0, 0, 0))

    pygame.draw.rect(win, (0, 0, 0), (225, 358, 210, 60))
    if 225 <= mouse[0] <= 435 and 358 <= mouse[1] <= 418:
        pygame.draw.rect(win, (200, 200, 50), (230, 363, 200, 50))
    else:
        pygame.draw.rect(win, (245, 245, 50), (230, 363, 200, 50))
    win.blit(starttext, ((660 / 2) - (starttext.get_rect().width / 2), 373))

    pygame.draw.rect(win, (0, 0, 0), (225, 448, 210, 60))
    if 225 <= mouse[0] <= 435 and 448 <= mouse[1] <= 508:
        pygame.draw.rect(win, (200, 200, 50), (230, 453, 200, 50))
    else:
        pygame.draw.rect(win, (245, 245, 50), (230, 453, 200, 50))
    win.blit(abouttext, ((660 / 2) - (abouttext.get_rect().width / 2), 463))

    pygame.draw.rect(win, (0, 0, 0), (225, 538, 210, 60))
    if 225 <= mouse[0] <= 435 and 538 <= mouse[1] <= 598:
        pygame.draw.rect(win, (200, 200, 50), (230, 543, 200, 50))
    else:
        pygame.draw.rect(win, (245, 245, 50), (230, 543, 200, 50))
    win.blit(quittext, ((660/2) - (quittext.get_rect().width/2), 553))


def startgame(gameboard, turn):
    run = True
    while run:
        clock.tick(30)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 61 <= mouse[0] <= 241 and 536 <= mouse[1] <= 606:
                    if event.button == 1:
                        run = False
                        mainmenu()
                if 461 <= mouse[0] <= 601 and 536 <= mouse[1] <= 606:
                    if event.button == 1:
                        run = False
                        gameboard = [0, " ", " ", " ", " ", " ", " ", " ", " ", " "]
                        startgame(gameboard, "X")

                if event.button == 1:
                    if gameboard[1] == " ":
                        if 141 <= mouse[0] <= 260 and 311 <= mouse[1] <= 430:
                            gameboard[1] = turn
                            winnercheck(gameboard, turn)
                            run = False
                    if gameboard[2] == " ":
                        if 271 <= mouse[0] <= 390 and 311 <= mouse[1] <= 430:
                            gameboard[2] = turn
                            winnercheck(gameboard, turn)
                            run = False
                    if gameboard[3] == " ":
                        if 401 <= mouse[0] <= 520 and 311 <= mouse[1] <= 430:
                            gameboard[3] = turn
                            winnercheck(gameboard, turn)
                            run = False
                    if gameboard[4] == " ":
                        if 141 <= mouse[0] <= 260 and 181 <= mouse[1] <= 300:
                            gameboard[4] = turn
                            winnercheck(gameboard, turn)
                            run = False
                    if gameboard[5] == " ":
                        if 271 <= mouse[0] <= 390 and 181 <= mouse[1] <= 300:
                            gameboard[5] = turn
                            winnercheck(gameboard, turn)
                            run = False
                    if gameboard[6] == " ":
                        if 401 <= mouse[0] <= 520 and 181 <= mouse[1] <= 300:
                            gameboard[6] = turn
                            winnercheck(gameboard, turn)
                            run = False
                    if gameboard[7] == " ":
                        if 141 <= mouse[0] <= 260 and 51 <= mouse[1] <= 170:
                            gameboard[7] = turn
                            winnercheck(gameboard, turn)
                            run = False

                    if gameboard[8] == " ":
                        if 271 <= mouse[0] <= 390 and 51 <= mouse[1] <= 170:
                            gameboard[8] = turn
                            winnercheck(gameboard, turn)
                            run = False
                    if gameboard[9] == " ":
                        if 401 <= mouse[0] <= 520 and 51 <= mouse[1] <= 170:
                            gameboard[9] = turn
                            winnercheck(gameboard, turn)
                            run = False

        if run:
            drawgame(gameboard, turn)
            pygame.display.update()


def drawgame(gameboard, turn):
    win.fill((175, 175, 175))
    mouse = pygame.mouse.get_pos()

    mod1 = 0
    mod2 = 0
    mod3 = 0
    mod4 = 0
    mod5 = 0
    mod6 = 0
    mod7 = 0
    mod8 = 0
    mod9 = 0

    piececolor1 = (0, 0, 0)
    piececolor2 = (0, 0, 0)
    piececolor3 = (0, 0, 0)
    piececolor4 = (0, 0, 0)
    piececolor5 = (0, 0, 0)
    piececolor6 = (0, 0, 0)
    piececolor7 = (0, 0, 0)
    piececolor8 = (0, 0, 0)
    piececolor9 = (0, 0, 0)

    if gameboard[1] == " ":
        piececolor1 = (0, 0, 0)
        mod1 = 0
    elif gameboard[1] == "X":
        piececolor1 = (0, 0, 255)
        mod1 = 0
    elif gameboard[1] == "O":
        piececolor1 = (255, 0, 0)
        mod1 = 4
    if gameboard[2] == " ":
        piececolor2 = (0, 0, 0)
        mod2 = 0
    elif gameboard[2] == "X":
        piececolor2 = (0, 0, 255)
        mod2 = 0
    elif gameboard[2] == "O":
        piececolor2 = (255, 0, 0)
        mod2 = 4
    if gameboard[3] == " ":
        piececolor3 = (0, 0, 0)
        mod3 = 0
    elif gameboard[3] == "X":
        piececolor3 = (0, 0, 255)
        mod3 = 0
    elif gameboard[3] == "O":
        piececolor3 = (255, 0, 0)
        mod3 = 4
    if gameboard[4] == " ":
        piececolor4 = (0, 0, 0)
        mod4 = 0
    elif gameboard[4] == "X":
        piececolor4 = (0, 0, 255)
        mod4 = 0
    elif gameboard[4] == "O":
        piececolor4 = (255, 0, 0)
        mod4 = 4
    if gameboard[5] == " ":
        piececolor5 = (0, 0, 0)
        mod5 = 0
    elif gameboard[5] == "X":
        piececolor5 = (0, 0, 255)
        mod5 = 0
    elif gameboard[5] == "O":
        piececolor5 = (255, 0, 0)
        mod5 = 4
    if gameboard[6] == " ":
        piececolor6 = (0, 0, 0)
        mod6 = 0
    elif gameboard[6] == "X":
        piececolor6 = (0, 0, 255)
        mod6 = 0
    elif gameboard[6] == "O":
        piececolor6 = (255, 0, 0)
        mod6 = 4
    if gameboard[7] == " ":
        piececolor7 = (0, 0, 0)
        mod7 = 0
    elif gameboard[7] == "X":
        piececolor7 = (0, 0, 255)
        mod7 = 0
    elif gameboard[7] == "O":
        piececolor7 = (255, 0, 0)
        mod7 = 4
    if gameboard[8] == " ":
        piececolor8 = (0, 0, 0)
        mod8 = 0
    elif gameboard[8] == "X":
        piececolor8 = (0, 0, 255)
        mod8 = 0
    elif gameboard[8] == "O":
        piececolor8 = (255, 0, 0)
        mod8 = 4
    if gameboard[9] == " ":
        piececolor9 = (0, 0, 0)
        mod9 = 0
    elif gameboard[9] == "X":
        piececolor9 = (0, 0, 255)
        mod9 = 0
    elif gameboard[9] == "O":
        piececolor9 = (255, 0, 0)
        mod9 = 4

    piecefont = pygame.font.Font("opensans.ttf", 100)
    piecetext1 = piecefont.render(gameboard[1], 1, piececolor1)
    piecetext2 = piecefont.render(gameboard[2], 1, piececolor2)
    piecetext3 = piecefont.render(gameboard[3], 1, piececolor3)
    piecetext4 = piecefont.render(gameboard[4], 1, piececolor4)
    piecetext5 = piecefont.render(gameboard[5], 1, piececolor5)
    piecetext6 = piecefont.render(gameboard[6], 1, piececolor6)
    piecetext7 = piecefont.render(gameboard[7], 1, piececolor7)
    piecetext8 = piecefont.render(gameboard[8], 1, piececolor8)
    piecetext9 = piecefont.render(gameboard[9], 1, piececolor9)

    if turn == "X":
        piecetest = piecefont.render("X", 1, (0, 0, 255))
    elif turn == "O":
        piecetest = piecefont.render("O", 1, (255, 0, 0))
    else:
        piecetest = piecefont.render("WHAT", 1, (255, 255, 255))

    if gameboard[1] == " ":
        if 141 <= mouse[0] <= 260 and 311 <= mouse[1] <= 430:
            pygame.draw.rect(win, (100, 100, 100), (141, 311, 120, 120))
            win.blit(piecetest, (166 - mod1, 301))
        else:
            pygame.draw.rect(win, (175, 175, 175), (141, 311, 120, 120))
    else:
        pygame.draw.rect(win, (175, 175, 175), (141, 311, 120, 120))

    if gameboard[2] == " ":
        if 271 <= mouse[0] <= 390 and 311 <= mouse[1] <= 430:
            pygame.draw.rect(win, (100, 100, 100), (271, 311, 120, 120))
            win.blit(piecetest, (295 - mod2, 301))
        else:
            pygame.draw.rect(win, (175, 175, 175), (271, 311, 120, 120))
    else:
        pygame.draw.rect(win, (175, 175, 175), (271, 311, 120, 120))

    if gameboard[3] == " ":
        if 401 <= mouse[0] <= 520 and 311 <= mouse[1] <= 430:
            pygame.draw.rect(win, (100, 100, 100), (401, 311, 120, 120))
            win.blit(piecetest, (425 - mod3, 301))
        else:
            pygame.draw.rect(win, (175, 175, 175), (401, 311, 120, 120))
    else:
        pygame.draw.rect(win, (175, 175, 175), (401, 311, 120, 120))

    if gameboard[4] == " ":
        if 141 <= mouse[0] <= 260 and 181 <= mouse[1] <= 300:
            pygame.draw.rect(win, (100, 100, 100), (141, 181, 120, 120))
            win.blit(piecetest, (166 - mod4, 171))
        else:
            pygame.draw.rect(win, (175, 175, 175), (141, 181, 120, 120))
    else:
        pygame.draw.rect(win, (175, 175, 175), (141, 181, 120, 120))

    if gameboard[5] == " ":
        if 271 <= mouse[0] <= 390 and 181 <= mouse[1] <= 300:
            pygame.draw.rect(win, (100, 100, 100), (271, 181, 120, 120))
            win.blit(piecetest, (295 - mod5, 171))
        else:
            pygame.draw.rect(win, (175, 175, 175), (271, 181, 120, 120))
    else:
        pygame.draw.rect(win, (175, 175, 175), (271, 181, 120, 120))

    if gameboard[6] == " ":
        if 401 <= mouse[0] <= 520 and 181 <= mouse[1] <= 300:
            pygame.draw.rect(win, (100, 100, 100), (401, 181, 120, 120))
            win.blit(piecetest, (425 - mod6, 171))
        else:
            pygame.draw.rect(win, (175, 175, 175), (401, 181, 120, 120))
    else:
        pygame.draw.rect(win, (175, 175, 175), (401, 181, 120, 120))

    if gameboard[7] == " ":
        if 141 <= mouse[0] <= 260 and 51 <= mouse[1] <= 170:
            pygame.draw.rect(win, (100, 100, 100), (141, 51, 120, 120))
            win.blit(piecetest, (166 - mod7, 40))
        else:
            pygame.draw.rect(win, (175, 175, 175), (141, 51, 120, 120))
    else:
        pygame.draw.rect(win, (175, 175, 175), (141, 51, 120, 120))

    if gameboard[8] == " ":
        if 271 <= mouse[0] <= 390 and 51 <= mouse[1] <= 170:
            pygame.draw.rect(win, (100, 100, 100), (271, 51, 120, 120))
            win.blit(piecetest, (295 - mod8, 40))
        else:
            pygame.draw.rect(win, (175, 175, 175), (271, 51, 120, 120))
    else:
        pygame.draw.rect(win, (175, 175, 175), (271, 51, 120, 120))

    if gameboard[9] == " ":
        if 401 <= mouse[0] <= 520 and 51 <= mouse[1] <= 170:
            pygame.draw.rect(win, (100, 100, 100), (401, 51, 120, 120))
            win.blit(piecetest, (425 - mod9, 40))
        else:
            pygame.draw.rect(win, (175, 175, 175), (401, 51, 120, 120))
    else:
        pygame.draw.rect(win, (175, 175, 175), (401, 51, 120, 120))

    pygame.draw.rect(win, (0, 0, 0), (261, 51, 10, 380))
    pygame.draw.rect(win, (0, 0, 0), (391, 51, 10, 380))
    pygame.draw.rect(win, (0, 0, 0), (141, 171, 380, 10))
    pygame.draw.rect(win, (0, 0, 0), (141, 301, 380, 10))

    # 7
    win.blit(piecetext7, (166 - mod7, 40))
    # 8
    win.blit(piecetext8, (295 - mod8, 40))
    # 9
    win.blit(piecetext9, (425 - mod9, 40))
    # 4
    win.blit(piecetext4, (166 - mod4, 171))
    # 5
    win.blit(piecetext5, (295 - mod5, 171))
    # 6
    win.blit(piecetext6, (425 - mod6, 171))
    # 1
    win.blit(piecetext1, (166 - mod1, 301))
    # 2
    win.blit(piecetext2, (295 - mod2, 301))
    # 3
    win.blit(piecetext3, (425 - mod3, 301))

    pygame.draw.rect(win, (0, 0, 0), (0, 476, 660, 5))

    pygame.draw.rect(win, (100, 100, 100), (0, 481, 660, 180))

    pygame.draw.rect(win, (0, 0, 0), (61, 536, 140, 70))
    if 61 <= mouse[0] <= 201 and 536 <= mouse[1] <= 606:
        pygame.draw.rect(win, (200, 200, 50), (66, 541, 130, 60))
    else:
        pygame.draw.rect(win, (245, 245, 0), (66, 541, 130, 60))
    menufont = pygame.font.Font("Chunkfive.otf", 40)
    menutext = menufont.render("Menu", 1, (0, 0, 0))
    win.blit(menutext, (75, 555))

    pygame.draw.rect(win, (0, 0, 0), (461, 536, 140, 70))
    if 461 <= mouse[0] <= 601 and 536 <= mouse[1] <= 606:
        pygame.draw.rect(win, (200, 200, 50), (466, 541, 130, 60))
    else:
        pygame.draw.rect(win, (245, 245, 0), (466, 541, 130, 60))
    restartfont = pygame.font.Font("Chunkfive.otf", 33)
    restarttext = restartfont.render("Restart", 1, (0, 0, 0))
    win.blit(restarttext, (472, 556))

    pygame.draw.rect(win, (0, 0, 0), (261, 546, 50, 50))
    if turn == "X":
        pygame.draw.rect(win, (175, 175, 175), (266, 551, 40, 40))
    else:
        pygame.draw.rect(win, (100, 100, 100), (266, 551, 40, 40))
    xfont = pygame.font.Font("opensans.ttf", 40)
    xtext = xfont.render("X", 1, (0, 0, 255))
    win.blit(xtext, (272, 543))

    pygame.draw.rect(win, (0, 0, 0), (351, 546, 50, 50))
    if turn == "O":
        pygame.draw.rect(win, (175, 175, 175), (356, 551, 40, 40))
    else:
        pygame.draw.rect(win, (100, 100, 100), (356, 551, 40, 40))
    ofont = pygame.font.Font("opensans.ttf", 40)
    otext = ofont.render("O", 1, (255, 0, 0))
    win.blit(otext, (360, 543))


def about():
    run = True
    while run:
        clock.tick(30)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 225 <= mouse[0] <= 435 and 538 <= mouse[1] <= 598:
                        run = False
        drawabout()
        pygame.display.update()


def drawabout():
    win.fill((175, 175, 175))
    mouse = pygame.mouse.get_pos()

    abouttitlefont = pygame.font.Font("Chunkfive.otf", 75)
    abouttitle = abouttitlefont.render("About", 1, (0, 0, 0))

    aboutfont = pygame.font.Font("Chunkfive.otf", 30)
    abouttext1 = aboutfont.render("Welcome to Tic-Tac-Toe!", 1, (0, 0, 0))
    abouttext2 = aboutfont.render("This is a Tic-Tac-Toe game", 1, (0, 0, 0))
    abouttext3 = aboutfont.render("made in Python 3 using pygame.", 1, (0, 0, 0))
    abouttext4 = aboutfont.render("It was made by Sawyer Scott Stahl.", 1, (0, 0, 0))
    abouttext5 = aboutfont.render("Have fun!", 1, (0, 0, 0))

    buttonfont = pygame.font.Font("Chunkfive.otf", 40)
    buttontext = buttonfont.render("Menu", 1, (0, 0, 0))

    win.blit(abouttitle, (216, 75))
    win.blit(abouttext1, (147, 251))
    win.blit(abouttext2, (129, 292))
    win.blit(abouttext3, (93, 333))
    win.blit(abouttext4, (70, 374))
    win.blit(abouttext5, (259, 446))

    pygame.draw.rect(win, (0, 0, 0), (225, 538, 210, 60))
    if 225 <= mouse[0] <= 435 and 538 <= mouse[1] <= 598:
        pygame.draw.rect(win, (200, 200, 50), (230, 543, 200, 50))
    else:
        pygame.draw.rect(win, (245, 245, 50), (230, 543, 200, 50))
    win.blit(buttontext, (274, 551))


def winnercheck(gameboard, turn):
    winner = "cont"
    if gameboard[7] == gameboard[8] == gameboard[9] and gameboard[7] != " ":
        wincon = 789
        if gameboard[7] == "X":
            winner = "x"
        elif gameboard[7] == "O":
            winner = "o"
    elif gameboard[4] == gameboard[5] == gameboard[6] and gameboard[4] != " ":
        wincon = 456
        if gameboard[4] == "X":
            winner = "x"
        elif gameboard[4] == "O":
            winner = "o"
    elif gameboard[1] == gameboard[2] == gameboard[3] and gameboard[1] != " ":
        wincon = 123
        if gameboard[1] == "X":
            winner = "x"
        elif gameboard[1] == "O":
            winner = "o"
    elif gameboard[7] == gameboard[4] == gameboard[1] and gameboard[7] != " ":
        wincon = 741
        if gameboard[7] == "X":
            winner = "x"
        elif gameboard[7] == "O":
            winner = "o"
    elif gameboard[8] == gameboard[5] == gameboard[2] and gameboard[8] != " ":
        wincon = 852
        if gameboard[8] == "X":
            winner = "x"
        elif gameboard[8] == "O":
            winner = "o"
    elif gameboard[9] == gameboard[6] == gameboard[3] and gameboard[9] != " ":
        wincon = 963
        if gameboard[9] == "X":
            winner = "x"
        elif gameboard[9] == "O":
            winner = "o"
    elif gameboard[7] == gameboard[5] == gameboard[3] and gameboard[7] != " ":
        wincon = 753
        if gameboard[7] == "X":
            winner = "x"
        elif gameboard[7] == "O":
            winner = "o"
    elif gameboard[9] == gameboard[5] == gameboard[1] and gameboard[9] != " ":
        wincon = 951
        if gameboard[9] == "X":
            winner = "x"
        elif gameboard[9] == "O":
            winner = "o"
    elif " " not in gameboard:
        wincon = 000
        winner = "draw"
    else:
        wincon = 000
        winner = "cont"

    if winner == "x":
        resultscreen(gameboard, "X", wincon, turn,)
    elif winner == "o":
        resultscreen(gameboard, "O", wincon, turn,)
    elif winner == "draw":
        resultscreen(gameboard, "draw", wincon, turn,)
    elif winner == "cont":
        if turn == "X":
            startgame(gameboard, "O")
        elif turn == "O":
            startgame(gameboard, "X")


def resultscreen(gameboard, winner, wincon, turn,):
    run = True
    while run:
        clock.tick(30)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 61 <= mouse[0] <= 201 and 536 <= mouse[1] <= 606:
                    if event.button == 1:
                        run = False
                        mainmenu()
                if 461 <= mouse[0] <= 601 and 536 <= mouse[1] <= 606:
                    if event.button == 1:
                        run = False
                        gameboard = [0, " ", " ", " ", " ", " ", " ", " ", " ", " "]
                        startgame(gameboard, "X")

        if run:
            pygame.display.update()
            drawresult(gameboard, winner, wincon)


def drawresult(gameboard, winner, wincon):
    win.fill((175, 175, 175))
    mouse = pygame.mouse.get_pos()

    pygame.draw.rect(win, (0, 0, 0), (261, 51, 10, 380))
    pygame.draw.rect(win, (0, 0, 0), (391, 51, 10, 380))
    pygame.draw.rect(win, (0, 0, 0), (141, 171, 380, 10))
    pygame.draw.rect(win, (0, 0, 0), (141, 301, 380, 10))
    pygame.draw.rect(win, (0, 0, 0), (0, 476, 660, 5))

    if wincon == 789:
        pygame.draw.rect(win, (100, 100, 100), (141, 51, 120, 120))
        pygame.draw.rect(win, (100, 100, 100), (271, 51, 120, 120))
        pygame.draw.rect(win, (100, 100, 100), (401, 51, 120, 120))

    elif wincon == 456:
        pygame.draw.rect(win, (100, 100, 100), (141, 181, 120, 120))
        pygame.draw.rect(win, (100, 100, 100), (271, 181, 120, 120))
        pygame.draw.rect(win, (100, 100, 100), (401, 181, 120, 120))

    elif wincon == 123:
        pygame.draw.rect(win, (100, 100, 100), (141, 311, 120, 120))
        pygame.draw.rect(win, (100, 100, 100), (271, 311, 120, 120))
        pygame.draw.rect(win, (100, 100, 100), (401, 311, 120, 120))

    elif wincon == 741:
        pygame.draw.rect(win, (100, 100, 100), (141, 51, 120, 120))
        pygame.draw.rect(win, (100, 100, 100), (141, 181, 120, 120))
        pygame.draw.rect(win, (100, 100, 100), (141, 311, 120, 120))

    elif wincon == 852:
        pygame.draw.rect(win, (100, 100, 100), (271, 51, 120, 120))
        pygame.draw.rect(win, (100, 100, 100), (271, 181, 120, 120))
        pygame.draw.rect(win, (100, 100, 100), (271, 311, 120, 120))

    elif wincon == 963:
        pygame.draw.rect(win, (100, 100, 100), (401, 51, 120, 120))
        pygame.draw.rect(win, (100, 100, 100), (401, 181, 120, 120))
        pygame.draw.rect(win, (100, 100, 100), (401, 311, 120, 120))

    elif wincon == 753:
        pygame.draw.rect(win, (100, 100, 100), (141, 51, 120, 120))
        pygame.draw.rect(win, (100, 100, 100), (271, 181, 120, 120))
        pygame.draw.rect(win, (100, 100, 100), (401, 311, 120, 120))

    elif wincon == 951:
        pygame.draw.rect(win, (100, 100, 100), (401, 51, 120, 120))
        pygame.draw.rect(win, (100, 100, 100), (271, 181, 120, 120))
        pygame.draw.rect(win, (100, 100, 100), (141, 311, 120, 120))

    mod1 = 0
    mod2 = 0
    mod3 = 0
    mod4 = 0
    mod5 = 0
    mod6 = 0
    mod7 = 0
    mod8 = 0
    mod9 = 0

    piececolor1 = (0, 0, 0)
    piececolor2 = (0, 0, 0)
    piececolor3 = (0, 0, 0)
    piececolor4 = (0, 0, 0)
    piececolor5 = (0, 0, 0)
    piececolor6 = (0, 0, 0)
    piececolor7 = (0, 0, 0)
    piececolor8 = (0, 0, 0)
    piececolor9 = (0, 0, 0)

    if gameboard[1] == " ":
        piececolor1 = (0, 0, 0)
        mod1 = 0
    elif gameboard[1] == "X":
        piececolor1 = (0, 0, 255)
        mod1 = 0
    elif gameboard[1] == "O":
        piececolor1 = (255, 0, 0)
        mod1 = 4
    if gameboard[2] == " ":
        piececolor2 = (0, 0, 0)
        mod2 = 0
    elif gameboard[2] == "X":
        piececolor2 = (0, 0, 255)
        mod2 = 0
    elif gameboard[2] == "O":
        piececolor2 = (255, 0, 0)
        mod2 = 4
    if gameboard[3] == " ":
        piececolor3 = (0, 0, 0)
        mod3 = 0
    elif gameboard[3] == "X":
        piececolor3 = (0, 0, 255)
        mod3 = 0
    elif gameboard[3] == "O":
        piececolor3 = (255, 0, 0)
        mod3 = 4
    if gameboard[4] == " ":
        piececolor4 = (0, 0, 0)
        mod4 = 0
    elif gameboard[4] == "X":
        piececolor4 = (0, 0, 255)
        mod4 = 0
    elif gameboard[4] == "O":
        piececolor4 = (255, 0, 0)
        mod4 = 4
    if gameboard[5] == " ":
        piececolor5 = (0, 0, 0)
        mod5 = 0
    elif gameboard[5] == "X":
        piececolor5 = (0, 0, 255)
        mod5 = 0
    elif gameboard[5] == "O":
        piececolor5 = (255, 0, 0)
        mod5 = 4
    if gameboard[6] == " ":
        piececolor6 = (0, 0, 0)
        mod6 = 0
    elif gameboard[6] == "X":
        piececolor6 = (0, 0, 255)
        mod6 = 0
    elif gameboard[6] == "O":
        piececolor6 = (255, 0, 0)
        mod6 = 4
    if gameboard[7] == " ":
        piececolor7 = (0, 0, 0)
        mod7 = 0
    elif gameboard[7] == "X":
        piececolor7 = (0, 0, 255)
        mod7 = 0
    elif gameboard[7] == "O":
        piececolor7 = (255, 0, 0)
        mod7 = 4
    if gameboard[8] == " ":
        piececolor8 = (0, 0, 0)
        mod8 = 0
    elif gameboard[8] == "X":
        piececolor8 = (0, 0, 255)
        mod8 = 0
    elif gameboard[8] == "O":
        piececolor8 = (255, 0, 0)
        mod8 = 4
    if gameboard[9] == " ":
        piececolor9 = (0, 0, 0)
        mod9 = 0
    elif gameboard[9] == "X":
        piececolor9 = (0, 0, 255)
        mod9 = 0
    elif gameboard[9] == "O":
        piececolor9 = (255, 0, 0)
        mod9 = 4

    piecefont = pygame.font.Font("opensans.ttf", 100)
    piecetext1 = piecefont.render(gameboard[1], 1, piececolor1)
    piecetext2 = piecefont.render(gameboard[2], 1, piececolor2)
    piecetext3 = piecefont.render(gameboard[3], 1, piececolor3)
    piecetext4 = piecefont.render(gameboard[4], 1, piececolor4)
    piecetext5 = piecefont.render(gameboard[5], 1, piececolor5)
    piecetext6 = piecefont.render(gameboard[6], 1, piececolor6)
    piecetext7 = piecefont.render(gameboard[7], 1, piececolor7)
    piecetext8 = piecefont.render(gameboard[8], 1, piececolor8)
    piecetext9 = piecefont.render(gameboard[9], 1, piececolor9)

    # 7
    win.blit(piecetext7, (166 - mod7, 40))
    # 8
    win.blit(piecetext8, (295 - mod8, 40))
    # 9
    win.blit(piecetext9, (425 - mod9, 40))
    # 4
    win.blit(piecetext4, (166 - mod4, 171))
    # 5
    win.blit(piecetext5, (295 - mod5, 171))
    # 6
    win.blit(piecetext6, (425 - mod6, 171))
    # 1
    win.blit(piecetext1, (166 - mod1, 301))
    # 2
    win.blit(piecetext2, (295 - mod2, 301))
    # 3
    win.blit(piecetext3, (425 - mod3, 301))

    pygame.draw.rect(win, (100, 100, 100), (0, 481, 660, 180))

    pygame.draw.rect(win, (0, 0, 0), (61, 536, 140, 70))
    if 61 <= mouse[0] <= 201 and 536 <= mouse[1] <= 606:
        pygame.draw.rect(win, (200, 200, 50), (66, 541, 130, 60))
    else:
        pygame.draw.rect(win, (245, 245, 0), (66, 541, 130, 60))
    menufont = pygame.font.Font("Chunkfive.otf", 40)
    menutext = menufont.render("Menu", 1, (0, 0, 0))
    win.blit(menutext, (75, 555))

    pygame.draw.rect(win, (0, 0, 0), (461, 536, 140, 70))
    if 461 <= mouse[0] <= 601 and 536 <= mouse[1] <= 606:
        pygame.draw.rect(win, (200, 200, 50), (466, 541, 130, 60))
    else:
        pygame.draw.rect(win, (245, 245, 0), (466, 541, 130, 60))
    restartfont = pygame.font.Font("Chunkfive.otf", 33)
    restarttext = restartfont.render("Restart", 1, (0, 0, 0))
    win.blit(restarttext, (472, 556))

    pygame.draw.rect(win, (0, 0, 0), (241, 526, 180, 90))
    pygame.draw.rect(win, (175, 175, 175), (246, 531, 170, 80))
    resultfont = pygame.font.Font("Chunkfive.otf", 40)
    xwinstext = resultfont.render("X wins!", 1, (0, 0, 0))
    owinstext = resultfont.render("O wins!", 1, (0, 0, 0))
    drawtext = resultfont.render("Draw!", 1, (0, 0, 0))

    if winner == "X":
        win.blit(xwinstext, (257, 554))

    if winner == "O":
        win.blit(owinstext, (257, 554))

    if winner == "draw":
        win.blit(drawtext, (274, 556))


mainmenu()
