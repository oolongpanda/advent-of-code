with open('input/day4.txt') as f:
    input = [l.strip() for l in f.readlines()]
    draws = input[0].split(',')
    
    count = 0
    boards = []
    currentboard = []
    for line in input[2:]:
        if (line != ''):
            currentboard.extend([line.split()])
        else:
            boards.extend([currentboard])
            currentboard = []
        count = count + 1 
    
    masterboards = boards

    bingo = False
    for draw in draws:
        for b, board in enumerate(boards):
            for r, row in enumerate(board):
                for n, number in enumerate(row):
                    if draw == number:
                        boards[b][r][n] = 'y'
                if (row == ['y'] * 5):
                    bingo = True
                    winner = boards[b]
            count = 0
            while (count < len(board[0])):
                test1 = [item[count] for item in board]
                if ([item[count] for item in board] == ['y'] * 5):
                    bingo = True
                    winner = boards[b]
                count = count + 1
        if bingo:
            lastcall = draw
            break

    winnernumbers = []
    for row in winner:
        winnernumbers = winnernumbers + row
    winnersum = 0
    for n in winnernumbers:
        if n != 'y':
            winnersum = winnersum + int(n)
    print ('Task 1:', winnersum*int(lastcall))

    #PART 2
    bingo = False
    board = masterboards
    bingoindex = [False]*len(boards)
    for draw in draws:
        for b, board in enumerate(boards):
            for r, row in enumerate(board):
                for n, number in enumerate(row):
                    if draw == number:
                        boards[b][r][n] = 'y'
                if (row == ['y'] * 5):
                    bingoindex[b] = True
                    if bingoindex.count(False) == 0:
                        lastcall = draw
                        loser = boards[b]
                        bingo = True
            count = 0
            while (count < len(board[0])):
                if ([item[count] for item in board] == ['y'] * 5):
                    bingoindex[b] = True
                    if len(boards) == 0:
                        lastcall = draw
                        loser = boards[b]
                        bingo = True
                count = count + 1
            if bingo:
                break
        if bingo:
            break
    
    losernumbers = []
    for row in loser:
        losernumbers = losernumbers + row
    losersum = 0
    for n in losernumbers:
        if n != 'y':
            losersum = losersum + int(n)
    print ('Task 2:', losersum*int(lastcall)