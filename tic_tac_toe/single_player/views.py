from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json, copy
# Create your views here.

nonegrid = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]

game_state = {
    'board': copy.deepcopy(nonegrid),
    'current_turn': 1,  # 1 for Player 1, 2 for Player 2
    'player1_name': "",
    'player2_name': "",
    "winner": None,
    "draw": None
}

def tictactoe(request):
    context = {
        'player1_name': game_state['player1_name'],
        'player2_name': game_state['player2_name'],
        'current_turn': game_state['player1_name'] if game_state['current_turn'] == 1 else game_state['player2_name'],
        'board': game_state['board'],
        'winner': game_state['winner'],
        'draw': game_state['draw']
    }
    return render(request, 'game.html', context)


def make_move(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        row = int(data.get('row'))
        col = int(data.get('col'))
        
        # Check if the selected tile is empty
        if game_state['board'][row][col] is None:
            # Update the board with the current player's move
            game_state['board'][row][col] = game_state['current_turn']
            
            # Check if the move results in a win or draw
            if check_winner(game_state['board'], game_state['current_turn']):
                game_state['winner'] = game_state['player1_name'] if game_state['current_turn'] == 1 else game_state['player2_name']
            elif check_draw(game_state['board']):
                game_state['draw'] = True
            else:
                # Switch turns if no winner or draw
                game_state['current_turn'] = 2 if game_state['current_turn'] == 1 else 1
            
            
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})
    return JsonResponse({'success': False})

def home(request):

    return render(request, 'home.html')

def play(request):

    return render(request, 'play.html')

def singlewindetails(request):

    if request.method == 'POST':
        data = request.POST
        game_state['player1_name'] = data.get('player1')
        game_state['player2_name'] = data.get('player2')
        game_state['board'] = copy.deepcopy(nonegrid)
        game_state['current_turn'] = 1
        game_state['winner'] = None
        game_state['draw'] = None
        return redirect('/game/')
    
    return render(request, 'single_window_details.html')

def restart_game(request):
    if request.method == 'POST':
        # Reset the game state
        game_state['board'] = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        game_state['current_turn'] = 1
        game_state['winner'] = None
        game_state['draw'] = False
        
        return JsonResponse({'success': True})
    
    return JsonResponse({'success': False})

def contact_page(request):

    return render(request, 'contact.html')

def about_page(request):

    return render(request, 'about.html')

def check_winner(board, player):
    # Define all possible winning combinations
    winning_combinations = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]

    # Check if any winning combination is filled by the same player
    for combo in winning_combinations:
        if all(board[row][col] == player for row, col in combo):
            return True
    return False

def check_draw(board):
    # If there is no empty spot left and no winner, it's a draw
    return all(all(cell is not None for cell in row) for row in board)

