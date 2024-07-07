'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
Dalumpines, Carl D.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    relationship = "rawr"
    for member in social_graph:
        if (to_member in social_graph[from_member]["following"]) and (from_member in social_graph[to_member]["following"]):
            relationship = "friends"
        elif to_member in social_graph[from_member]["following"]:
            relationship = "follower"
        elif from_member in social_graph[to_member]["following"]:
            relationship = "followed by"
        else:
            relationship = "no relationship"
    return relationship

    def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    winner = "NO WINNER"
    
    #column
    for i in range(len(board)):
        col = [row[i] for row in board]
        for c in col:
            if all(c==col[0] for c in col)==True:
                winner=col[0]
            else:
                continue
        #diagonal
        if all(board[i][i]==board[0][0] for i in range(len(board)))==True:
            winner=board[0][0]
        elif all(board[i][len(board)-i-1]==board[-1][0] for i in range(len(board)))==True:
            winner=board[-1][0]
        else:
            continue
    #row
    for row in board:
        for r in row:
            if all(r==row[0] for r in row)==True:
                winner=row[0]
            else:
                continue   
    if winner=="":
        winner="NO WINNER"
    return winner

    def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    total_time=0
    for i,key in list(enumerate(route_map.keys())):
        if first_stop==second_stop:
            total_time=0
            return total_time
        if first_stop in key[0] and second_stop in key[1]:
            total_time=route_map[key]["travel_time_mins"] 
            return total_time
        if first_stop in key[0]:
            #get index of the starting point
            firstIndex=i
        if second_stop in key[1]:
            #get index of the stop
            secondIndex=i
    #I feel like the error is somewhere here po, but it has not appeared in any of my tests
    if firstIndex<secondIndex:
        for i,key in list(enumerate(route_map.keys())):
            #get total time of everything between and including start and stop
            if i>=firstIndex and i<=secondIndex:
                total_time+=route_map[key]["travel_time_mins"]
    if firstIndex>secondIndex:
        for i,key in list(enumerate(route_map.keys())):
            #get total time of everything not between start and stop;
            if not (i<firstIndex and i>secondIndex):
                total_time+=route_map[key]["travel_time_mins"]
    return total_time
